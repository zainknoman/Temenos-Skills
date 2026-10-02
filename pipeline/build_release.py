#!/usr/bin/env python3
"""Build the complete knowledge DB for one release into releases/<R>/ --
fields (insert_parse), type/mandatory/description (html_parse) and
componentised names (component_parse). Each release is stored complete, never
as a delta (plan Decision 8).

Sources are only READ: the JARs at RELEASES[<R>] and the release's
T24.javadoc.jar, which is copied into build/ and generated there (`java -jar`
writes a T24.javadoc/ folder next to where it runs). Markdown output goes to
build/releases/<R>/table-schema (scratch -- the skills' table-schema/ stays R23).
The whole run is bracketed by the C:\\R25 write guard.

  python pipeline/build_release.py --release R25 \\
      --javadoc-jar "C:\\R25\\bnk\\Transact_L3_Javadoc\\T24.javadoc.jar"
"""
import argparse
import subprocess
import sys
import time
from collections import namedtuple
from pathlib import Path

from releases import RELEASES, db_path

HERE = Path(__file__).resolve().parent
Step = namedtuple("Step", "name cmd writes cwd")


def plan_steps(release, javadoc_jar):
    if release == "R23":
        raise ValueError("R23 is built from jar/ by the original commands in CLAUDE.md -- not by build_release.py")
    db_path(release)  # validates the release name
    db = db_path(release)
    scratch = Path("build") / "releases" / release
    md_out = scratch / "table-schema"
    py = sys.executable
    steps = []
    if javadoc_jar:
        jdoc = scratch / "javadoc"
        steps += [
            Step("copy-javadoc",
                 [py, "-c", "import shutil, sys; shutil.copy2(sys.argv[1], sys.argv[2])",
                  str(javadoc_jar), str(jdoc / Path(javadoc_jar).name)],
                 [jdoc / Path(javadoc_jar).name], None),
            Step("generate-javadoc", ["java", "-jar", Path(javadoc_jar).name], [jdoc / "T24.javadoc"], jdoc),
        ]
    steps.append(Step("insert_parse",
                      [py, str(HERE / "insert_parse.py"), "--jars", str(RELEASES[release]),
                       "--db", str(db), "--out", str(md_out)],
                      [db, md_out], None))
    if javadoc_jar:
        steps.append(Step("html_parse",
                          [py, str(HERE / "html_parse.py"), "--html", str(scratch / "javadoc" / "T24.javadoc"),
                           "--db", str(db), "--out", str(md_out)],
                          [db, md_out], None))
    steps.append(Step("component_parse",
                      [py, str(HERE / "component_parse.py"), "--jars", str(RELEASES[release]),
                       "--db", str(db), "--release", release],
                      [db], None))
    steps.append(Step("record_parse",
                      [py, str(HERE / "record_parse.py"), "--jars", str(RELEASES[release]),
                       "--db", str(db), "--release", release],
                      [db], None))
    return steps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", required=True)
    ap.add_argument("--javadoc-jar", type=Path, help="the release's T24.javadoc.jar (read-only source)")
    args = ap.parse_args()

    from compile_check import r25_writes_since

    steps = plan_steps(args.release, args.javadoc_jar)
    db = db_path(args.release)
    db.parent.mkdir(parents=True, exist_ok=True)
    if db.exists():
        db.unlink()
    for step in steps:
        if step.cwd:
            Path(step.cwd).mkdir(parents=True, exist_ok=True)
        for out in step.writes:
            Path(out).parent.mkdir(parents=True, exist_ok=True)

    marker = db.parent / ".r25-marker"
    marker.write_text("")
    time.sleep(1)
    for step in steps:
        print(f"== {step.name}", flush=True)
        if subprocess.run(step.cmd, cwd=step.cwd).returncode != 0:
            sys.exit(f"{step.name} failed")
    writes = r25_writes_since(marker)
    if writes:
        sys.exit("R25_WRITE_GUARD: build wrote into C:\\R25:\n" + "\n".join(map(str, writes[:20])))
    print(f"Built {db}")


if __name__ == "__main__":
    main()
