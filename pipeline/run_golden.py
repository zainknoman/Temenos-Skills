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

from compile_check import add_install_args, find_install, install_release, use_install
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


def outcome(case, report, lost):
    """PASS / FAIL, or PEND for a case marked "compiled": false whose compile could not run (no R25
    install): its fields passed, but it is still waiting for its first compile."""
    if report["passed"] and not lost:
        return "PASS"
    fields_ok = all(not f.get("error") and not f["missing"] for f in report["fields"])
    if case.get("compiled", True) is False and report["compile"]["status"] == "SKIPPED" and fields_ok and not lost:
        return "PEND"
    return "FAIL"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case")
    add_release_args(ap)
    add_install_args(ap)
    args = ap.parse_args()
    print(use_install(args))
    compiled_on = install_release(find_install()) or "this install"

    conn = connect(args)
    failures = 0
    for r in run_cases(conn, args.case):
        failures += r["result"] == "FAIL"
        detail = r["report"]["compile"]["status"] + (f" expected-fields-not-seen={r['lost']}" if r["lost"] else "")
        if r["result"] == "PASS" and r["compiled"] is False:
            detail += f' -- now compiles on {compiled_on}: remove "compiled": false from its case.json'
        print(f"{r['result']}  {r['case']:<40} {detail}")
        if not r["report"]["passed"] and r["report"]["compile"]["status"] != "OK":
            print(r["report"]["compile"]["output"][-2000:])
    conn.close()
    sys.exit(1 if failures else 0)


def run_cases(conn, only=None, root=GOLDEN):
    """Verify every golden case (or just `only`), yielding {"case", "result", "lost", "compiled", "report"}
    as each one finishes. result is PASS / FAIL / PEND (see outcome)."""
    for case in load_cases(root):
        if only and case["name"] != only:
            continue
        report = verify(case["dir"] / case["file"], case["apps"], conn, Path("build/verify/golden"),
                        no_app_ok=not case["apps"])
        expected = set(case.get("expected_fields", []))
        seen = {f for r in report["fields"] for f in r["verified"] + r.get("compiler_checked", [])}
        lost = expected - seen if not case["file"].endswith(".java") else set()
        yield {"case": case["name"], "result": outcome(case, report, lost), "lost": sorted(lost),
               "compiled": case.get("compiled", True), "report": report}


if __name__ == "__main__":
    main()
