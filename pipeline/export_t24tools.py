#!/usr/bin/env python3
"""Export the Layer A schema DB as the T24Tools data contract:
fields.json (positions/types, ~1 MB gzip), descriptions.json (lazy-loaded),
manifest.json (counts + sha256). Output is byte-for-byte deterministic for
the same DB, so CI can diff it.

The export is Temenos-derived data: it stays in build/ for personal use and is
never committed to the public T24Tools repo (plan/state/decisions.md).

  python pipeline/export_t24tools.py --out build/t24tools/R25 --release R25
"""
import argparse
import gzip
import hashlib
import json
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from artefact_fields import dotted_prefix, record_class

SCHEMA_VERSION = 1
GZIP_WARN_BYTES = 5_000_000


def _blank_to_none(value):
    return value if value not in (None, "") else None


def build_export(conn, release):
    rows = conn.execute(
        "SELECT app, position, field_name, java_alias, field_type, mandatory, description "
        "FROM fields ORDER BY app, position, field_name"
    ).fetchall()
    by_app = defaultdict(list)
    for row in rows:
        by_app[row[0]].append(row[1:])
    apps, descs = {}, {}
    for app in sorted(by_app):
        recs = by_app[app]
        apps[app] = {
            "prefix": dotted_prefix([r[1] for r in recs]),
            "recordClass": record_class(app),
            "fields": [[r[0], r[1], r[2], _blank_to_none(r[3]), _blank_to_none(r[4])] for r in recs],
        }
        d = {r[1]: r[5] for r in recs if _blank_to_none(r[5])}
        if d:
            descs[app] = d
    return {"release": release, "apps": apps}, {"release": release, "apps": descs}


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
    ap.add_argument("--db", default="temenos_knowledge.db")
    ap.add_argument("--out", default="build/t24tools/R25")
    ap.add_argument("--release", default="R25")
    args = ap.parse_args()
    conn = sqlite3.connect(args.db)
    m = write_export(conn, Path(args.out), args.release)
    conn.close()
    print(f"Exported {m['apps']} apps / {m['fields']} fields to {args.out}")


if __name__ == "__main__":
    main()
