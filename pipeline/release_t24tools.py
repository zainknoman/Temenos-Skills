#!/usr/bin/env python3
"""Gate + export in one step: run the golden accuracy suite for a release; only
if it passes, write that release's T24Tools knowledge export
(build/t24tools/<release>/: fields.json, descriptions.json, classes.json) and templates.json (build/t24tools/templates.json,
proven against every release DB that has been built).

  python pipeline/release_t24tools.py --release R23
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def release(golden_cmd, export_cmd, templates_cmd=None, class_cmd=None):
    if subprocess.run(golden_cmd).returncode != 0:
        print("Golden suite failed -- export NOT written.")
        return 1
    rc = subprocess.run(export_cmd).returncode
    for cmd in (class_cmd, templates_cmd):
        if rc == 0 and cmd:
            rc = subprocess.run(cmd).returncode
    return rc


TEMPLATES_SNIPPET = (
    "import sys; sys.path.insert(0, sys.argv[1])\n"
    "from artefact_templates import export_templates\n"
    "from releases import RELEASES, db_path, open_release_db\n"
    "conns = {r: open_release_db(r) for r in RELEASES if db_path(r).is_file()}\n"
    "doc = export_templates(sys.argv[2], conns=conns)\n"
    "proven = [t['id'] for l in doc['languages'] for t in l['types'] if t['proven']]\n"
    "print(f'templates.json: {len(proven)} proven types against {sorted(conns)}: {proven}')\n"
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", required=True, help="release of the knowledge DB, e.g. R23")
    ap.add_argument("--install", default=None, help="T24 install for the golden compile (see run_golden.py --install)")
    args = ap.parse_args()
    install = ["--install", args.install] if args.install else []
    sys.exit(release(
        golden_cmd=[sys.executable, str(HERE / "run_golden.py"), "--release", args.release, *install],
        export_cmd=[sys.executable, str(HERE / "export_t24tools.py"), "--release", args.release,
                    "--db", str(_db(args.release)), "--out", f"build/t24tools/{args.release}"],
        class_cmd=[sys.executable, str(HERE / "class_export.py"), "--release", args.release,
                   "--out", f"build/t24tools/{args.release}"],
        templates_cmd=[sys.executable, "-c", TEMPLATES_SNIPPET, str(HERE), "build/t24tools/templates.json"],
    ))


def _db(release):
    sys.path.insert(0, str(HERE))
    from releases import db_path
    return db_path(release)


if __name__ == "__main__":
    main()
