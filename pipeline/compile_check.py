#!/usr/bin/env python3
"""Compile gate for generated artefacts. Compiles against the read-only R25
install and writes ONLY under the out_dir given (build/verify/...). Every
compile is bracketed by a write guard: if anything under C:\\R25 changed,
the result is FAIL regardless of compiler output.

The write-free tCompile invocation (config overrides + log env vars) was
verified on 2026-10-02 -- see plan/state/decisions.md "tCompile invocation"."""
import os
import re
import shutil
import subprocess
import time
from collections import namedtuple
from pathlib import Path

R25 = Path(r"C:\R25")
CompileResult = namedtuple("CompileResult", "status output")

# Third-party trees the guard does not walk (JBoss, DB backup) -- tCompile never touches them.
GUARD_SKIP = ("TAFJ/3rdParty", "TAFJ/appserver")

# tafj.properties keys that point into C:\R25 and must be redirected -> scratch subdirectory.
TCOMPILE_OVERRIDES = {
    "temn.tafj.directory.basic": "src",
    "temn.tafj.directory.java": "java",
    "temn.tafj.directory.classes": "classes",
    "temn.tafj.runtime.directory.current": "UD",
    "temn.tafj.runtime.directory.como": "como",
    "temn.tafj.directory.updates": "updates",
}

# Read by TAFJ\bin\tafj_conf.bat; without them tCompile appends to C:\R25\TAFJ\log\compiler.log.
LOG_ENV_VARS = ("temenos.log.directory", "temenos.log.directory.t24", "temenos.log.directory.como")


def r25_writes_since(marker, r25=R25, skip=GUARD_SKIP):
    since = Path(marker).stat().st_mtime
    skipped = {Path(r25, s) for s in skip}
    newer = []
    for dirpath, dirnames, filenames in os.walk(r25):
        dirnames[:] = [d for d in dirnames if Path(dirpath, d) not in skipped]
        for name in filenames:
            path = Path(dirpath, name)
            if path.stat().st_mtime > since:
                newer.append(path)
    return sorted(newer)


def _guarded(run, out_dir, r25):
    out_dir.mkdir(parents=True, exist_ok=True)
    marker = out_dir / ".r25-marker"
    marker.write_text("")
    time.sleep(1)  # mtime resolution
    result = run()
    writes = r25_writes_since(marker, r25)
    if writes:
        listed = "\n".join(str(w) for w in writes[:20])
        return CompileResult("FAIL", f"R25_WRITE_GUARD: compile wrote into {r25}:\n{listed}\n\n{result.output}")
    return result


def compile_java(src, out_dir, r25=R25):
    src, out_dir, r25 = Path(src), Path(out_dir), Path(r25)
    if not (r25 / "bnk" / "t24lib").is_dir():
        return CompileResult("SKIPPED", f"R25 libraries not found at {r25}")
    javac = shutil.which("javac")
    if not javac:
        return CompileResult("SKIPPED", "javac not on PATH")
    cp = f"{r25 / 'bnk' / 't24lib'}\\*;{r25 / 'TAFJ' / 'lib'}\\*"

    def run():
        proc = subprocess.run(
            [javac, "-proc:none", "-nowarn", "-d", str(out_dir / "classes"), "-cp", cp, str(src)],
            capture_output=True, text=True,
        )
        return CompileResult("OK" if proc.returncode == 0 else "FAIL", proc.stdout + proc.stderr)

    return _guarded(run, out_dir, r25)


def jbc_status(returncode, output):
    if returncode != 0 or re.search(r"^\s*\[ERROR\]", output, re.MULTILINE):
        return "FAIL"
    if "Compilation completed" not in output:
        return "FAIL"
    return "OK"


def scratch_env(out_dir):
    log_dir = Path(out_dir).resolve() / "log"
    log_dir.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    for var in LOG_ENV_VARS:
        env[var] = str(log_dir)
    return env


def _scratch_properties(src, out_dir, r25):
    base = (r25 / "TAFJ" / "conf" / "tafj.properties").read_text(encoding="latin-1").splitlines()
    lines = [l for l in base if l.split("=", 1)[0].strip() not in TCOMPILE_OVERRIDES]
    for key, sub in TCOMPILE_OVERRIDES.items():
        path = src.parent if sub == "src" else out_dir / sub
        path.mkdir(parents=True, exist_ok=True)
        lines.append(f"{key}={path}")
    props = out_dir / "tafj-scratch.properties"
    props.write_text("\n".join(lines) + "\n", encoding="latin-1")
    return props


def compile_jbc(src, out_dir, r25=R25):
    src, out_dir, r25 = Path(src).resolve(), Path(out_dir).resolve(), Path(r25)
    tcompile = r25 / "TAFJ" / "bin" / "tCompile.bat"
    if not tcompile.is_file():
        return CompileResult("SKIPPED", f"tCompile not found at {tcompile}")
    out_dir.mkdir(parents=True, exist_ok=True)
    props = _scratch_properties(src, out_dir, r25)
    env = scratch_env(out_dir)

    def run():
        proc = subprocess.run(
            ["cmd", "/c", str(tcompile), "-cf", str(props), str(src)],
            capture_output=True, text=True, env=env,
        )
        text = proc.stdout + proc.stderr
        return CompileResult(jbc_status(proc.returncode, text), text)

    return _guarded(run, out_dir, r25)
