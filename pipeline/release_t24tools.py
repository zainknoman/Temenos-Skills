#!/usr/bin/env python3
"""Gate + export in one step: run the golden accuracy suite; only if it
passes, write the T24Tools export. Use after any JAR/DB regeneration.

  python pipeline/release_t24tools.py --release R25
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def release(golden_cmd, export_cmd):
    if subprocess.run(golden_cmd).returncode != 0:
        print("Golden suite failed -- export NOT written.")
        return 1
    return subprocess.run(export_cmd).returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", default="R25")
    args = ap.parse_args()
    sys.exit(release(
        golden_cmd=[sys.executable, str(HERE / "run_golden.py")],
        export_cmd=[sys.executable, str(HERE / "export_t24tools.py"),
                    "--release", args.release, "--out", f"build/t24tools/{args.release}"],
    ))


if __name__ == "__main__":
    main()
