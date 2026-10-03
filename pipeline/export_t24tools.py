#!/usr/bin/env python3
"""Export the Layer A schema DB as the T24Tools data contract:
fields.json (positions/types, ~1 MB gzip), descriptions.json (lazy-loaded),
manifest.json (counts + sha256). Output is byte-for-byte deterministic for
the same DB, so CI can diff it.

The export is Temenos-derived data: it stays in build/ for personal use and is
never committed to the public T24Tools repo (plan/state/decisions.md).

  python pipeline/export_t24tools.py --release R23   (jar/ is R23 -- see MANIFEST.MF)
"""
import argparse
import gzip
import hashlib
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from artefact_fields import _has_component_table, dotted_prefix, record_class
from releases import connect

SCHEMA_VERSION = 3  # v2: per-field componentised name + per-app components; v3: per-field value kind
GZIP_WARN_BYTES = 5_000_000


def _blank_to_none(value):
    return value if value not in (None, "") else None


def _component_names(conn):
    """({app: [component, ...] most fields first}, {(app, position): full componentised name}).
    A field exposed by several components (ACCOUNT via AC.AccountOpening and
    AZ.Contract) takes its name from the component with the most fields for that app."""
    if not _has_component_table(conn):
        return {}, {}
    counts = defaultdict(lambda: defaultdict(int))
    rows = conn.execute("SELECT app, component, record, comp_field, position FROM component_fields").fetchall()
    for app, comp, *_ in rows:
        counts[app][comp] += 1
    order = {app: sorted(c, key=lambda k: (-c[k], k)) for app, c in counts.items()}
    names = {}
    for app, comp, record, field, pos in sorted(rows, key=lambda r: order[r[0]].index(r[1])):
        names.setdefault((app, pos), f"{comp}.{record}.{field}")
    return order, names


def build_export(conn, release):
    if not release:
        raise ValueError("release is required (the release of the JARs the DB was built from, e.g. R23)")
    rows = conn.execute(
        "SELECT app, position, field_name, java_alias, field_type, mandatory, description "
        "FROM fields ORDER BY app, position, field_name"
    ).fetchall()
    by_app = defaultdict(list)
    for row in rows:
        by_app[row[0]].append(row[1:])
    components, comp_names = _component_names(conn)
    kinds = {}
    if conn.execute("SELECT 1 FROM sqlite_master WHERE name = 'field_kinds'").fetchone():
        kinds = {(a, f): k for a, f, k in conn.execute("SELECT app, field_name, kind FROM field_kinds")}
    apps, descs = {}, {}
    for app in sorted(by_app):
        recs = by_app[app]
        apps[app] = {
            "prefix": dotted_prefix([r[1] for r in recs]),
            "recordClass": record_class(app),
            "components": components.get(app, []),
            # [position, name, javaAlias, type, mandatory, jbcName, kind] -- kind: SV / MV / MV-GROUP / null (unknown)
            "fields": [[r[0], r[1], r[2], _blank_to_none(r[3]), _blank_to_none(r[4]), comp_names.get((app, r[0])),
                        kinds.get((app, r[1]))] for r in recs],
        }
        d = {r[1]: r[5] for r in recs if _blank_to_none(r[5])}
        if d:
            descs[app] = d
    head = {"release": release, "schemaVersion": SCHEMA_VERSION}
    return {**head, "apps": apps}, {**head, "apps": descs}


def _dump(doc, path):
    data = json.dumps(doc, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    path.write_bytes(data)
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}, data


def write_export(conn, out_dir, release, now=None):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    fields, descs = build_export(conn, release)
    f_meta, f_bytes = _dump(fields, out_dir / "fields.json")
    d_meta, _ = _dump(descs, out_dir / "descriptions.json")
    manifest = {
        "release": release,
        "schemaVersion": SCHEMA_VERSION,
        "generated": now or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "apps": len(fields["apps"]),
        "fields": sum(len(a["fields"]) for a in fields["apps"].values()),
        "files": {"fields.json": f_meta, "descriptions.json": d_meta},
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    gz = len(gzip.compress(f_bytes, 9))
    if gz > GZIP_WARN_BYTES:
        print(f"WARNING: fields.json is {gz / 1e6:.1f} MB gzipped -- revisit the single-file layout (Decision 2)")
    return manifest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", help="explicit DB path; default: the --release's knowledge DB")
    ap.add_argument("--out", help="default: build/t24tools/<release>")
    ap.add_argument("--release", required=True, help="release of the JARs the DB was built from, e.g. R23")
    args = ap.parse_args()
    conn = connect(args)  # never default to the R23 DB for another release
    out = Path(args.out or f"build/t24tools/{args.release}")
    m = write_export(conn, out, args.release)
    conn.close()
    print(f"Exported {m['apps']} apps / {m['fields']} fields ({args.release}) to {out}")


if __name__ == "__main__":
    main()
