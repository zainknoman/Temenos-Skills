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
import sys

from releases import add_release_args, connect


def _has_table(conn, name):
    return conn.execute("SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ?", (name,)).fetchone()


def app_fields(conn, app):
    """Every field of `app` in position order: name, position, Java alias, type, mandatory,
    description, single/multi-value kind and componentised (jBC) names. [] if the app is unknown."""
    app = app.upper()
    rows = conn.execute(
        "SELECT field_name, position, java_alias, field_type, mandatory, description FROM fields "
        "WHERE app = ? ORDER BY position", (app,)).fetchall()
    comp_names = {}
    if _has_table(conn, "component_fields"):
        for field_name, comp, record, comp_field in conn.execute(
                "SELECT field_name, component, record, comp_field FROM component_fields WHERE app = ? "
                "ORDER BY component", (app,)):
            comp_names.setdefault(field_name.upper(), []).append(f"{comp}.{record}.{comp_field}")
    kinds = {}
    if _has_table(conn, "field_kinds"):
        kinds = {f.upper(): k for f, k in conn.execute(
            "SELECT field_name, kind FROM field_kinds WHERE app = ?", (app,))}
    return [{"field": name, "position": position, "javaAlias": alias, "type": ftype or None,
             "mandatory": mandatory or None, "description": desc or None,
             "kind": kinds.get(name.upper()), "jbc": comp_names.get(name.upper(), [])}
            for name, position, alias, ftype, mandatory, desc in rows]


def check(conn, app, requested):
    """{"app", "known": bool, "verified": [field dicts], "missing": [names]} for the requested names."""
    fields = app_fields(conn, app)
    known = {f["field"].upper(): f for f in fields}
    requested = [r.strip().upper() for r in requested if r.strip()]
    return {"app": app.upper(), "known": bool(fields),
            "verified": [known[r] for r in requested if r in known],
            "missing": [r for r in requested if r not in known]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", required=True, help="T24 application, e.g. ACCOUNT")
    ap.add_argument("--fields", required=True, help="comma-separated field names to verify")
    add_release_args(ap)
    args = ap.parse_args()

    conn = connect(args)
    app = args.app.upper()
    result = check(conn, app, args.fields.split(","))
    conn.close()

    if not result["known"]:
        print(f"HALT: no schema found for app '{app}'. Regenerate table-schema or check the app name.")
        sys.exit(1)

    missing = result["missing"]
    if missing:
        print(f"HALT: {len(missing)} field(s) not found in {app} schema -- never guess, ask the developer:")
        for f in missing:
            print(f"  NOT FOUND: {f}")
        sys.exit(1)

    print(f"VERIFIED: all {len(result['verified'])} field(s) exist in {app} schema:")
    for f in result["verified"]:
        jbc = f", jBC {' | '.join(f['jbc'])}" if f["jbc"] else ""
        print(
            f"  {f['field']}  (pos {f['position']}, alias {f['javaAlias']}, "
            f"type={f['type'] or '?'}, mandatory={f['mandatory'] or '?'}, value={f['kind'] or '?'}{jbc})"
        )
    sys.exit(0)


if __name__ == "__main__":
    main()
