#!/usr/bin/env python3
"""Accuracy gate for a generated T24 artefact: field check (Layer A) +
compile against R25. Exit 0 only if every field is verified AND the
compile status is OK -- a SKIPPED compile is a failure, not a pass.

  python pipeline/verify_artefact.py --file out/V.CUS.CHECK.b --app CUSTOMER
"""
import argparse
import json
import sqlite3
import sys
from pathlib import Path

from artefact_fields import UnknownApp, check_fields
from compile_check import compile_java, compile_jbc

DEFAULT_OUT = Path("build/verify")


def _default_compiler(path):
    return compile_java if path.suffix == ".java" else compile_jbc


def verify(path, apps, conn, out_dir, compile_fn=None, skip_compile=False):
    path = Path(path)
    source = path.read_text(encoding="utf-8", errors="replace")
    fields, ok = [], True
    if path.suffix != ".java":  # javac is the field gate for Java
        if not apps:
            fields.append({"app": None, "error": "no --app given: fields in a jBC/Infobasic file cannot be checked",
                           "verified": [], "missing": []})
            ok = False
        for app in apps:
            try:
                res = check_fields(conn, app, source)
                fields.append({"app": res.app, "verified": res.verified, "missing": res.missing})
                ok &= not res.missing
            except UnknownApp as exc:
                fields.append({"app": app, "error": str(exc), "verified": [], "missing": []})
                ok = False
    if skip_compile:
        compiled = {"status": "NOT_RUN", "output": ""}
    else:
        result = (compile_fn or _default_compiler(path))(path, Path(out_dir) / path.stem)
        compiled = {"status": result.status, "output": result.output}
        ok &= result.status == "OK"
    return {"file": str(path), "fields": fields, "compile": compiled, "passed": bool(ok)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--app", action="append", default=[], help="repeatable")
    ap.add_argument("--db", default="temenos_knowledge.db")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-compile", action="store_true", help="field gate only (development use)")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    report = verify(Path(args.file), [a.upper() for a in args.app], conn, args.out,
                    skip_compile=args.no_compile)
    conn.close()

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for f in report["fields"]:
            if f.get("error"):
                print(f"HALT: {f['error']}")
            for m in f["missing"]:
                print(f"NOT FOUND in {f['app']}: {m}")
            if f["verified"]:
                print(f"VERIFIED in {f['app']}: {', '.join(f['verified'])}")
        print(f"COMPILE: {report['compile']['status']}")
        if report["compile"]["status"] not in ("OK", "NOT_RUN"):
            print(report["compile"]["output"][-3000:])
        print("PASS" if report["passed"] else "FAIL")
    sys.exit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
