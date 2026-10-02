#!/usr/bin/env python3
"""Phase 1 extraction for the SEPA / TPH knowledge base.

Reads the per-JAR extraction cache produced by ``pipeline/extract.py`` (one
JSON per JAR under ``cache/``) and the field schemas in
``temenos_knowledge.db``, and emits a payment-domain inventory under
``knowledge/sepa/``.

Nothing here invents names: every class, method and field printed comes from a
cache entry or a DB row, and each output line carries the JAR it came from.

Usage:
    python pipeline/sepa_extract.py --cache cache --db temenos_knowledge.db \
        --out knowledge/sepa
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from collections import defaultdict
from pathlib import Path

# JAR-name prefixes that make up the payment domain in this JAR set.
#   PP_ = Temenos Payments / TPH        EP_ = European Payments (native SEPA)
#   PI_ = Payment Initiation / Order    PW_ = Payment Workflow
#   DD_ = Direct Debit                  DB_ = Debit Collection Order
PAYMENT_JAR_PREFIXES = ("PP_", "EP_", "PI_", "PW_", "DD_", "DB_")

# Extra JARs outside those prefixes that carry payment/clearing logic.
EXTRA_JARS = {
    "FT_Clearing.jar",
    "FT_ClearingHook.jar",
    "AC_ClearingServiceHook.jar",
    "ACHFRM_ClearingHouseHook.jar",
    "ACHFRM_Foundation.jar",
}

# T24 application-name prefixes that belong to the payment domain.
PAYMENT_APP_PREFIXES = (
    "PP.", "PPT.", "POR.", "PAYMENT.", "PI.", "SEPA.", "EP.", "PW.",
)

# TAFJ generates one wrapper class per compiled jBC routine. These are noise in
# a class index but their *names* are the routine names, which we do want.
JBC_WRAPPER = re.compile(r"^(.*)_cl$")
JBC_METHOD_WRAPPER = re.compile(r"^(.*?)_([A-Za-z][A-Za-z0-9]*)_\d+_cl$")
COMPONENT_WRAPPER = re.compile(r"^component_.*_\d+_cl$")


def is_payment_jar(jar_name: str) -> bool:
    return jar_name.startswith(PAYMENT_JAR_PREFIXES) or jar_name in EXTRA_JARS


def load_cache(cache_dir: Path) -> dict[str, dict]:
    """Return {jar_file_name: cache_entry} for payment-domain JARs only."""
    entries: dict[str, dict] = {}
    for path in sorted(cache_dir.glob("*.json")):
        jar = path.stem + ".jar"
        if not is_payment_jar(jar):
            continue
        try:
            entries[jar] = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            print(f"  ! skipping unreadable cache entry {path.name}: {exc}")
    return entries


def classify(cls: dict) -> str:
    """Bucket a class into one artefact kind, using its own package/name."""
    q = cls.get("qualified", "")
    name = cls.get("name", "")
    pkg = cls.get("package", "")

    if COMPONENT_WRAPPER.match(name):
        return "component-descriptor"
    if pkg.startswith("com.temenos.t24.api.hook"):
        return "hook-api"
    if pkg.startswith("com.temenos.t24.api.complex."):
        return "complex-dto"
    if pkg.startswith("com.temenos.t24.api.records."):
        return "record-model"
    if pkg.startswith("com.temenos.t24.api."):
        return "public-api"
    if name.endswith("_cl"):
        # Compiled jBC. Split "method wrappers" (Service_method_NN_cl) from
        # plain routine wrappers (ROUTINE_NAME_cl).
        return "jbc-method" if JBC_METHOD_WRAPPER.match(name) else "jbc-routine"
    if q.startswith("com.temenos.t24"):
        return "t24-class"
    return "other"


def routine_name(cls: dict) -> str:
    """Recover the jBC routine (or component method) name from a wrapper class."""
    name = cls.get("name", "")
    m = JBC_METHOD_WRAPPER.match(name)
    if m:
        return f"{m.group(1)}.{m.group(2)}"
    m = JBC_WRAPPER.match(name)
    return m.group(1) if m else name


def collect(entries: dict[str, dict]) -> dict:
    buckets: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    per_jar_counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    for jar, entry in entries.items():
        for cls in entry.get("classes", []):
            kind = classify(cls)
            buckets[kind].append((jar, cls))
            per_jar_counts[jar][kind] += 1

    return {"buckets": buckets, "per_jar": per_jar_counts}


def payment_apps(db_path: Path) -> dict[str, list[tuple[str, int]]]:
    """{app: [(source_jar, field_count)]} for payment-domain applications."""
    con = sqlite3.connect(db_path)
    where = " or ".join("app like ?" for _ in PAYMENT_APP_PREFIXES)
    rows = con.execute(
        f"select app, source_jar, count(*) from fields where {where} "
        "group by app, source_jar order by app",
        tuple(p + "%" for p in PAYMENT_APP_PREFIXES),
    ).fetchall()
    con.close()

    out: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for app, jar, n in rows:
        out[app].append((jar, n))
    return out


def write_class_index(out_dir: Path, data: dict, entries: dict[str, dict]) -> None:
    buckets = data["buckets"]
    lines = [
        "# SEPA / TPH — Payment-Domain Class Index",
        "",
        "> Generated by `pipeline/sepa_extract.py` from the per-JAR extraction cache",
        "> (`cache/*.json`, produced by `pipeline/extract.py`). Every row names the JAR",
        "> it was read from. No entry here is inferred — if a class is absent from this",
        "> index it was not found in the scanned JARs.",
        "",
        f"Scanned {len(entries)} payment-domain JARs "
        f"({', '.join(PAYMENT_JAR_PREFIXES)} prefixes plus "
        f"{len(EXTRA_JARS)} named clearing JARs).",
        "",
        "## Artefact counts",
        "",
        "| Artefact kind | Count |",
        "|---------------|-------|",
    ]
    for kind in sorted(buckets, key=lambda k: -len(buckets[k])):
        lines.append(f"| `{kind}` | {len(buckets[kind])} |")
    lines.append("")

    # Hook APIs and public APIs are the customisation surface — list in full.
    for kind, heading in (
        ("hook-api", "Hook APIs (customisation extension points)"),
        ("public-api", "Public APIs"),
    ):
        lines += [f"## {heading}", "", "| Class | JAR |", "|-------|-----|"]
        for jar, cls in sorted(buckets.get(kind, []), key=lambda x: x[1]["qualified"]):
            lines.append(f"| `{cls['qualified']}` | `{jar}` |")
        lines.append("")

    # Complex DTO packages — group, since there are hundreds of individual DTOs.
    dto_pkgs: dict[str, tuple[str, int]] = {}
    for jar, cls in buckets.get("complex-dto", []):
        pkg = cls["package"]
        jar_name, n = dto_pkgs.get(pkg, (jar, 0))
        dto_pkgs[pkg] = (jar_name, n + 1)
    lines += [
        "## Complex DTO packages",
        "",
        "Parameter/return types for the hook APIs above. One package per hook.",
        "",
        "| Package | DTOs | JAR |",
        "|---------|------|-----|",
    ]
    for pkg in sorted(dto_pkgs):
        jar, n = dto_pkgs[pkg]
        lines.append(f"| `{pkg}` | {n} | `{jar}` |")
    lines.append("")

    # Record models — group by application package.
    rec_pkgs: dict[str, tuple[str, int]] = {}
    for jar, cls in buckets.get("record-model", []):
        pkg = cls["package"].rsplit(".", 1)[-1]
        jar_name, n = rec_pkgs.get(pkg, (jar, 0))
        rec_pkgs[pkg] = (jar_name, n + 1)
    lines += [
        "## Record model packages",
        "",
        "Generated typed record classes. A package with more than one class has",
        "multivalue field groups: every class other than `*Record` is one MV field",
        "(see the MV-detection rule in `skills/temenos-dev/SKILL.md`).",
        "",
        "| Package | Classes | MV field groups | JAR |",
        "|---------|---------|-----------------|-----|",
    ]
    for pkg in sorted(rec_pkgs):
        jar, n = rec_pkgs[pkg]
        lines.append(f"| `com.temenos.t24.api.records.{pkg}` | {n} | {max(n - 1, 0)} | `{jar}` |")
    lines.append("")

    (out_dir / "class-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  wrote {out_dir / 'class-index.md'}")


def write_routine_index(out_dir: Path, data: dict) -> None:
    buckets = data["buckets"]
    rows = []
    for kind in ("jbc-routine", "jbc-method"):
        for jar, cls in buckets.get(kind, []):
            rows.append((routine_name(cls), kind, jar, len(cls.get("methods", []))))
    rows.sort()

    lines = [
        "# SEPA / TPH — Compiled jBC Routine Index",
        "",
        "> Generated by `pipeline/sepa_extract.py`. Each row is a TAFJ-compiled jBC",
        "> artefact found in a payment-domain JAR. `jbc-routine` = a standalone",
        "> routine (`NAME_cl`); `jbc-method` = a component method",
        "> (`Component_method_NN_cl`), rendered here as `Component.method`.",
        "",
        "> The routine *name* is ground truth (it is the class name). The routine's",
        "> behaviour is not captured here — decompile the class if you need the logic.",
        "",
        f"{len(rows)} routines across the payment JAR set.",
        "",
        "| Routine | Kind | JAR |",
        "|---------|------|-----|",
    ]
    for name, kind, jar, _ in rows:
        lines.append(f"| `{name}` | {kind} | `{jar}` |")

    (out_dir / "routine-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  wrote {out_dir / 'routine-index.md'} ({len(rows)} routines)")


def write_applications(out_dir: Path, apps: dict[str, list[tuple[str, int]]]) -> None:
    lines = [
        "# SEPA / TPH — Payment-Domain Applications",
        "",
        "> Generated by `pipeline/sepa_extract.py` from the `fields` table of",
        "> `temenos_knowledge.db` (built by `pipeline/insert_parse.py` from",
        "> `INSERTS/I_F.<APP>` inside the JARs). Field counts are exact.",
        "",
        "> Full field lists live in `skills/temenos-dev/references/table-schema/<APP>.md`.",
        "> **Never use a field name that is not in that file** — run",
        "> `python pipeline/validate_fields.py --app <APP> --fields \"F1,F2\"` first.",
        "",
        f"{len(apps)} applications.",
        "",
        "| Application | Fields | Source JAR |",
        "|-------------|--------|------------|",
    ]
    for app in sorted(apps):
        for jar, n in apps[app]:
            lines.append(f"| `{app}` | {n} | `{jar}` |")

    (out_dir / "applications.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  wrote {out_dir / 'applications.md'} ({len(apps)} applications)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cache", type=Path, default=Path("cache"))
    ap.add_argument("--db", type=Path, default=Path("temenos_knowledge.db"))
    ap.add_argument("--out", type=Path, default=Path("knowledge/sepa"))
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)

    print(f"Reading payment-domain JAR cache from {args.cache} ...")
    entries = load_cache(args.cache)
    print(f"  {len(entries)} payment JARs, "
          f"{sum(len(e.get('classes', [])) for e in entries.values())} classes")

    data = collect(entries)
    write_class_index(args.out, data, entries)
    write_routine_index(args.out, data)

    print(f"Reading payment-domain applications from {args.db} ...")
    apps = payment_apps(args.db)
    write_applications(args.out, apps)


if __name__ == "__main__":
    main()
