#!/usr/bin/env python3
"""Mechanically verify T24 field names against the schema DB (Layer A) --
the concrete implementation of the Field Verification Gate in
skills/temenos-dev/SKILL.md. Run this before emitting any code that reads or
writes T24 fields; don't rely on eyeballing table-schema/<APP>.md alone.

Exit code 0 = every field verified. Exit code 1 = at least one field missing
-- HALT and ask the developer for the correct name, per CLAUDE.md's single
most important rule: never invent a T24 field name.
"""
import argparse
import sqlite3
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", required=True, help="T24 application, e.g. ACCOUNT")
    ap.add_argument("--fields", required=True, help="comma-separated field names to verify")
    ap.add_argument("--db", default="temenos_knowledge.db")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    app = args.app.upper()
    requested = [f.strip().upper() for f in args.fields.split(",") if f.strip()]

    rows = conn.execute(
        "SELECT field_name, position, java_alias, field_type, mandatory FROM fields WHERE app = ?",
        (app,),
    ).fetchall()
    known = {r[0].upper(): r for r in rows}
    conn.close()

    if not rows:
        print(f"HALT: no schema found for app '{app}'. Regenerate table-schema or check the app name.")
        sys.exit(1)

    missing = [f for f in requested if f not in known]
    if missing:
        print(f"HALT: {len(missing)} field(s) not found in {app} schema -- never guess, ask the developer:")
        for f in missing:
            print(f"  NOT FOUND: {f}")
        sys.exit(1)

    print(f"VERIFIED: all {len(requested)} field(s) exist in {app} schema:")
    for f in requested:
        field_name, position, java_alias, field_type, mandatory = known[f]
        print(
            f"  {field_name}  (pos {position}, alias {java_alias}, "
            f"type={field_type or '?'}, mandatory={mandatory or '?'})"
        )
    sys.exit(0)


if __name__ == "__main__":
    main()
