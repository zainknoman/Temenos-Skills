#!/usr/bin/env python3
"""Run every golden case in tests/golden through verify_artefact (fields +
compile against R25). Exit 1 if any case fails. This is the accuracy
regression suite: a skill change that breaks a golden case is a bug.

  python pipeline/run_golden.py [--case NAME]
"""
import argparse
import json
import sys
from pathlib import Path

from verify_artefact import verify
from releases import add_release_args, connect

GOLDEN = Path("tests/golden")


def load_cases(root=GOLDEN):
    cases = []
    for case_json in sorted(Path(root).glob("*/case.json")):
        case = json.loads(case_json.read_text(encoding="utf-8"))
        case["dir"] = case_json.parent
        cases.append(case)
    return cases


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case")
    add_release_args(ap)
    args = ap.parse_args()

    conn = connect(args)
    failures = 0
    for case in load_cases():
        if args.case and case["name"] != args.case:
            continue
        report = verify(case["dir"] / case["file"], case["apps"], conn, Path("build/verify/golden"))
        expected = set(case.get("expected_fields", []))
        seen = {f for r in report["fields"] for f in r["verified"] + r.get("compiler_checked", [])}
        lost = expected - seen if not case["file"].endswith(".java") else set()
        ok = report["passed"] and not lost
        failures += not ok
        detail = report["compile"]["status"] + (f" expected-fields-not-seen={sorted(lost)}" if lost else "")
        print(f"{'PASS' if ok else 'FAIL'}  {case['name']:<40} {detail}")
        if not report["passed"] and report["compile"]["status"] != "OK":
            print(report["compile"]["output"][-2000:])
    conn.close()
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
