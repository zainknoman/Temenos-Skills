#!/usr/bin/env python3
"""
aggregate.py — Phase 2 of the Temenos T24 knowledge pipeline.

Reads all JSON cache files produced by extract.py, merges them into
a set of structured Markdown reference files that the t24-dev skill
loads at code-generation time.

Usage:
    python aggregate.py --cache cache --out skills/t24-dev/references

Output files (all relative to --out):
    classes/class-index.md          — master index: all 77k+ classes
    packages/package-index.md       — 137 packages → $USING declarations
    apis/java-api.md                — 157 public-api classes with full method signatures
    hooks/lifecycle-hooks.md        — RecordLifecycle, ActivityLifecycle, ServiceLifecycle
    hooks/validation-hooks.md       — validation + auth hook classes
    hooks/event-hooks.md            — event listener classes
    relationships/dependency-graph.md — JAR → class → method cross-reference
    architecture/application-map.md — T24 application → class → JAR → domain mapping
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("aggregate")

NOW = datetime.now(timezone.utc).isoformat()

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_cache(cache_dir: Path) -> list[dict]:
    """Load all JAR JSON cache files, return flat list of jar dicts."""
    jars = []
    for f in sorted(cache_dir.glob("*.json")):
        if f.name == "javadoc.json":
            continue
        try:
            jars.append(json.loads(f.read_text(encoding="utf-8")))
        except Exception as e:
            log.warning("Skipping corrupt cache file %s: %s", f.name, e)
    log.info("Loaded %d JAR cache files", len(jars))
    return jars


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    log.info("  wrote  %s  (%d bytes)", path, len(content))


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    sep = ["-" * max(len(h), 4) for h in headers]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(sep)    + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

def gen_class_index(jars: list[dict], out_dir: Path) -> None:
    """Master class index — one row per class."""
    rows = []
    for jar in jars:
        for cls in jar["classes"]:
            rows.append([
                f'`{cls["name"]}`',
                f'`{jar["jar"]}`',
                f'`{cls["package"]}`',
                cls["domain"],
                cls["component_type"],
                f'`{cls["superclass"]}`' if cls["superclass"] else "",
            ])
    rows.sort(key=lambda r: r[0])

    total = sum(len(j["classes"]) for j in jars)
    body = md_table(
        ["Class", "JAR", "Package", "Domain", "Component Type", "Superclass"],
        rows
    )
    content = (
        f"# T24 Master Class Index\n"
        f"> Source: JAR analysis ({NOW[:10]}). "
        f"Trimmed to public-api component types only. "
        f"Full index: {total:,} classes across {len(jars):,} JARs.\n\n"
        + body
    )
    write(out_dir / "classes" / "class-index.md", content)


def gen_package_index(jars: list[dict], out_dir: Path) -> None:
    """Package → $USING declaration map."""
    packages: dict[str, tuple[str, str]] = {}   # package → (jar, domain)
    for jar in jars:
        for cls in jar["classes"]:
            pkg = cls["package"]
            if pkg and pkg not in packages:
                packages[pkg] = (jar["jar"], cls["domain"])

    rows = sorted(
        [[f'`{pkg}`', f'`{jar}`', dom, f'`$USING {pkg}`']
         for pkg, (jar, dom) in packages.items()],
        key=lambda r: r[0]
    )
    body = md_table(
        ["Package", "JAR", "Domain", "`$USING` Declaration"],
        rows
    )
    content = (
        f"# T24 Package Index\n"
        f"> Generated {NOW} — {len(packages):,} packages.\n\n"
        + body
    )
    write(out_dir / "packages" / "package-index.md", content)


def gen_java_api(jars: list[dict], out_dir: Path) -> None:
    """Full method signatures for every public-api class."""
    api_classes = [
        (jar["jar"], cls)
        for jar in jars
        for cls in jar["classes"]
        if cls["component_type"] == "public-api"
    ]
    api_classes.sort(key=lambda t: t[1]["name"])

    sections: list[str] = [
        f"# T24 Java API Catalog\n"
        f"> Generated {NOW} — {len(api_classes):,} public API classes.\n"
    ]

    for jar_name, cls in api_classes:
        header = (
            f"\n## `{cls['name']}`\n"
            f"**JAR:** `{jar_name}`  "
            f"**Package:** `{cls['package']}`\n"
        )
        if cls["superclass"]:
            header += f"**Extends:** `{cls['superclass']}`\n"
        if cls["interfaces"]:
            ifaces = ", ".join(f'`{i}`' for i in cls["interfaces"])
            header += f"**Implements:** {ifaces}\n"

        if cls["methods"]:
            method_rows = [
                [
                    f'`{m["name"]}`',
                    f'`{m["return_type"]}`',
                    ", ".join(f'`{p}`' for p in m["params"]) or "",
                ]
                for m in cls["methods"]
            ]
            methods_table = md_table(
                ["Method", "Returns", "Parameters"],
                method_rows
            )
            sections.append(header + methods_table)
        else:
            sections.append(header + "_No public methods._")

    write(out_dir / "apis" / "java-api.md", "\n".join(sections))


def gen_hooks(jars: list[dict], out_dir: Path) -> None:
    """Three hook reference files: lifecycle, validation, event."""
    lifecycle_keywords = {
        "RecordLifecycle", "ActivityLifecycle", "ServiceLifecycle",
        "Lifecycle", "checkId", "validateRecord", "autoField",
        "beforeAuth", "afterAuth"
    }
    validation_keywords = {
        "Validation", "Authorization", "AuthorisationHook",
        "ValidHook", "getRNew", "setE", "AuthHook"
    }
    event_keywords = {
        "Event", "Listener", "EventHook", "EB.EVENT"
    }

    def matches(cls_name: str, kws: set) -> bool:
        return any(k in cls_name for k in kws)

    lifecycle, validation, events = [], [], []

    for jar in jars:
        for cls in jar["classes"]:
            name = cls["name"]
            row = [
                f'`{name}`',
                f'`{jar["jar"]}`',
                f'`{cls["package"]}`',
                cls["domain"],
                ", ".join(f'`{m["name"]}`' for m in cls["methods"][:5]),
            ]
            if matches(name, lifecycle_keywords):
                lifecycle.append(row)
            elif matches(name, validation_keywords):
                validation.append(row)
            elif matches(name, event_keywords):
                events.append(row)

    headers = ["Class", "JAR", "Package", "Domain", "Key Methods (first 5)"]

    def hook_file(title: str, rows: list) -> str:
        return (
            f"# {title}\n"
            f"> Generated {NOW} — {len(rows):,} classes.\n\n"
            + md_table(headers, sorted(rows, key=lambda r: r[0]))
        )

    write(out_dir / "hooks" / "lifecycle-hooks.md",
          hook_file("T24 Lifecycle Hook Classes", lifecycle))
    write(out_dir / "hooks" / "validation-hooks.md",
          hook_file("T24 Validation & Authorization Hook Classes", validation))
    write(out_dir / "hooks" / "event-hooks.md",
          hook_file("T24 Event Listener Classes", events))


def gen_dependency_graph(jars: list[dict], out_dir: Path) -> None:
    """
    JAR dependency graph — for each JAR, lists which other JARs' types
    appear in its method parameter/return types (cross-JAR references).
    """
    # Build a map: qualified class name → jar
    class_to_jar: dict[str, str] = {}
    for jar in jars:
        for cls in jar["classes"]:
            class_to_jar[cls["qualified"]] = jar["jar"]

    sections: list[str] = [
        f"# T24 JAR Dependency Graph\n"
        f"> Generated {NOW} — {len(jars):,} JARs analysed.\n\n"
        "> A → B means JAR A's public API references a type defined in JAR B.\n"
    ]

    for jar in sorted(jars, key=lambda j: j["jar"]):
        deps: set[str] = set()
        for cls in jar["classes"]:
            for m in cls["methods"]:
                all_types = [m["return_type"]] + m["params"]
                for t in all_types:
                    # Strip generics and arrays
                    base = t.split("<")[0].rstrip("[]").strip()
                    dep_jar = class_to_jar.get(base)
                    if dep_jar and dep_jar != jar["jar"]:
                        deps.add(dep_jar)

        if deps:
            dep_list = "\n".join(f"  - `{d}`" for d in sorted(deps))
            sections.append(f"\n## `{jar['jar']}`\n**References:**\n{dep_list}")

    write(out_dir / "relationships" / "dependency-graph.md",
          "\n".join(sections))


def gen_application_map(jars: list[dict], out_dir: Path) -> None:
    """
    T24 application → class → JAR → domain mapping.
    Groups classes by their T24 application prefix (first component of the JAR name).
    """
    by_app: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for jar in jars:
        # T24 JARs follow the pattern: <APP>_<Name>.jar
        prefix = jar["jar"].split("_")[0] if "_" in jar["jar"] else "MISC"
        for cls in jar["classes"]:
            by_app[prefix].append((cls["name"], jar["jar"], cls["domain"]))

    sections = [
        f"# T24 Application Map\n"
        f"> Generated {NOW} — {len(by_app):,} application prefixes.\n"
    ]

    for app in sorted(by_app):
        entries = sorted(by_app[app], key=lambda t: t[0])
        rows = [[f'`{name}`', f'`{jar}`', domain]
                for name, jar, domain in entries]
        table = md_table(["Class", "JAR", "Domain"], rows)
        sections.append(f"\n## `{app}`\n{table}")

    write(out_dir / "architecture" / "application-map.md",
          "\n".join(sections))


# ---------------------------------------------------------------------------
# Javadoc merge (optional — if cache/javadoc.json exists from html_parse.py)
# ---------------------------------------------------------------------------

def gen_javadoc_index(jars: list[dict], cache_dir: Path, out_dir: Path) -> None:
    """Merge JavaDoc descriptions (from html_parse.py) into a class summary."""
    javadoc_path = cache_dir / "javadoc.json"
    javadoc: dict[str, str] = {}
    if javadoc_path.exists():
        try:
            javadoc = json.loads(javadoc_path.read_text(encoding="utf-8"))
            log.info("Loaded javadoc.json — %d descriptions", len(javadoc))
        except Exception as e:
            log.warning("Could not load javadoc.json: %s", e)

    rows = []
    for jar in jars:
        for cls in jar["classes"]:
            raw  = javadoc.get(cls["qualified"], javadoc.get(cls["name"], ""))
            desc = raw.get("description", "") if isinstance(raw, dict) else (raw or "")
            rows.append([
                f'`{cls["name"]}`',
                f'`{cls["package"]}`',
                desc[:120] + ("…" if len(desc) > 120 else ""),
            ])
    rows.sort(key=lambda r: r[0])

    content = (
        f"# T24 JavaDoc Index\n"
        f"> Generated {NOW} — {len(rows):,} entries "
        f"({'with' if javadoc else 'without'} JavaDoc descriptions).\n\n"
        + md_table(["Class", "Package", "Description"], rows)
    )
    write(out_dir / "javadocs" / "javadoc-index.md", content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Phase 2: aggregate JAR cache → skill reference .md files."
    )
    ap.add_argument("--cache", required=True,
                    help="Cache directory produced by extract.py")
    ap.add_argument("--out",   required=True,
                    help="Output directory for reference .md files")
    args = ap.parse_args()

    cache_dir = Path(args.cache)
    out_dir   = Path(args.out)

    if not cache_dir.is_dir():
        sys.exit(f"ERROR: --cache directory not found: {cache_dir}")

    jars = load_cache(cache_dir)
    if not jars:
        sys.exit("ERROR: No cache files found. Run extract.py first.")

    total_classes = sum(len(j["classes"]) for j in jars)
    log.info("Total classes across all JARs: %d", total_classes)

    log.info("Generating class-index.md …")
    gen_class_index(jars, out_dir)

    log.info("Generating package-index.md …")
    gen_package_index(jars, out_dir)

    log.info("Generating java-api.md …")
    gen_java_api(jars, out_dir)

    log.info("Generating hook reference files …")
    gen_hooks(jars, out_dir)

    log.info("Generating dependency-graph.md …")
    gen_dependency_graph(jars, out_dir)

    log.info("Generating application-map.md …")
    gen_application_map(jars, out_dir)

    log.info("Generating javadoc-index.md …")
    gen_javadoc_index(jars, cache_dir, out_dir)

    log.info("─" * 60)
    log.info("Aggregation complete. Reference files written to: %s/", out_dir)


if __name__ == "__main__":
    main()
