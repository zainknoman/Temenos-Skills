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

# Which T24 install to compile against. C:\R25 stays the default; when it is absent the first other
# known install that exists is used, so the same pipeline runs on an R25 machine and an R23 machine
# without code changes. Override with --install PATH or the T24_INSTALL environment variable.
INSTALL_ENV = "T24_INSTALL"
JAVA_HOME_ENV = "T24_JAVA_HOME"
KNOWN_INSTALLS = (R25, Path(r"E:\Temenos"))


def bnk_dir(root):
    """C:\\R25 keeps bnk\\ at the root; a TAFJ installer layout (E:\\Temenos) has it under T24\\bnk."""
    root = Path(root)
    for cand in (root / "bnk", root / "T24" / "bnk"):
        if cand.is_dir():
            return cand
    return root / "bnk"


def install_present(root):
    root = Path(root)
    return (root / "TAFJ" / "bin" / "tCompile.bat").is_file() or (bnk_dir(root) / "t24lib").is_dir()


def find_install(explicit=None, env=None, known=KNOWN_INSTALLS):
    """--install PATH > $T24_INSTALL > first known install present > C:\\R25 (compiles then SKIP)."""
    env = os.environ if env is None else env
    if explicit:
        return Path(explicit)
    if env.get(INSTALL_ENV):
        return Path(env[INSTALL_ENV])
    for cand in known:
        if install_present(cand):
            return Path(cand)
    return R25


def install_release(root):
    """Release from a t24lib JAR manifest (e.g. 'R23_AMR.0' -> 'R23'); None if it cannot be read."""
    import zipfile
    lib = bnk_dir(root) / "t24lib"
    try:
        jar = next(p for p in sorted(lib.glob("*.jar")))
        manifest = zipfile.ZipFile(jar).read("META-INF/MANIFEST.MF").decode("latin-1")
    except (StopIteration, OSError, KeyError, zipfile.BadZipFile):
        return None
    m = re.search(r"Implementation-Version:\s*(R\d\d)", manifest)
    return m.group(1) if m else None


def add_install_args(ap):
    ap.add_argument("--install", default=None,
                    help=f"T24 install to compile against (default: ${INSTALL_ENV}, else the first of "
                         f"{', '.join(str(k) for k in KNOWN_INSTALLS)} that exists)")


def use_install(args):
    """Apply --install for this process and describe the install the compile will use."""
    if getattr(args, "install", None):
        os.environ[INSTALL_ENV] = str(args.install)
    root = find_install()
    if not install_present(root):
        return f"Compile install: none found (looked at {', '.join(str(k) for k in KNOWN_INSTALLS)}) -- compiles SKIP"
    return f"Compile install: {root} ({install_release(root) or 'release unknown'})"


def install_java_home(root, env=None):
    """JDK for tCompile. $T24_JAVA_HOME wins. For an install other than C:\\R25, its bundled
    3rdParty\\JDK (older TAFJ .bat files break on a JAVA_HOME with spaces, e.g. C:\\Program Files).
    None = inherit JAVA_HOME (C:\\R25 behaves exactly as before)."""
    env = os.environ if env is None else env
    if env.get(JAVA_HOME_ENV):
        return Path(env[JAVA_HOME_ENV])
    if Path(root) == R25:
        return None
    jdks = sorted(p for p in (Path(root) / "3rdParty" / "JDK").glob("jdk*") if (p / "bin").is_dir())
    return jdks[-1] if jdks else None

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
    # .component compiles write TAFC stub .b/.h files here (R25 default: TAFJ/tafc_components/**).
    "temn.tafj.compiler.tafc.component.dir": "tafc_components",
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
            try:
                mtime = path.stat().st_mtime
            except OSError:  # broken link/junction (e.g. a JBoss module dir in a moved install)
                continue
            if mtime > since:
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


def java_classpath(r25=R25):
    # t24lib = T24 API/record classes; TAFJ/lib = TStructure/TField/T24Record;
    # TAFJ/ext = third-party jars the record classes reference (org.json via json.jar).
    r25 = Path(r25)
    return ";".join(f"{d}\\*" for d in (bnk_dir(r25) / "t24lib", r25 / "TAFJ" / "lib", r25 / "TAFJ" / "ext"))


def javac_command(javac, src, out_dir, cp):
    # Empty -sourcepath: R25 JARs ship .java doc stubs beside the .class files, and
    # javac would otherwise compile those stubs (765 errors) instead of using the classes.
    return [javac, "-proc:none", "-nowarn", "-sourcepath", "", "-d", str(Path(out_dir) / "classes"),
            "-cp", cp, str(src)]


def compile_java(src, out_dir, r25=None):
    r25 = find_install() if r25 is None else r25
    src, out_dir, r25 = Path(src), Path(out_dir), Path(r25)
    if not (bnk_dir(r25) / "t24lib").is_dir():
        return CompileResult("SKIPPED", f"R25 libraries not found at {r25}")
    javac = shutil.which("javac")
    if not javac:
        return CompileResult("SKIPPED", "javac not on PATH")
    cp = java_classpath(r25)

    def run():
        proc = subprocess.run(javac_command(javac, src, out_dir, cp), capture_output=True, text=True)
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
        lines.append(f"{key}={path}/**" if sub == "tafc_components" else f"{key}={path}")
    # An install copied/moved to another drive keeps its old tafj.home / t24.home, so
    # <t24.home>\t24lib (precompiled I_COMMON etc.) would not resolve. Repoint them in this
    # scratch copy only, and only when the configured directory does not exist.
    for key, actual in (("tafj.home", r25 / "TAFJ"), ("t24.home", bnk_dir(r25))):
        configured = next((l.split("=", 1)[1].strip() for l in lines if l.split("=", 1)[0].strip() == key), None)
        if configured is not None and not Path(configured).is_dir():
            lines = [l for l in lines if l.split("=", 1)[0].strip() != key]
            lines.insert(0, f"{key}={actual}")
    props = out_dir / "tafj-scratch.properties"
    props.write_text("\n".join(lines) + "\n", encoding="latin-1")
    return props


def compile_order(src):
    """A componentised routine only compiles once its .component definition is
    compiled ("No method is pointing to <ROUTINE> in <PACKAGE>"), so .component
    files beside a .b go first, into the same classes directory."""
    src = Path(src)
    if src.suffix == ".component":
        return [src]
    return sorted(src.parent.glob("*.component")) + [src]


def compile_jbc(src, out_dir, r25=None):
    r25 = find_install() if r25 is None else r25
    src, out_dir, r25 = Path(src).resolve(), Path(out_dir).resolve(), Path(r25)
    tcompile = r25 / "TAFJ" / "bin" / "tCompile.bat"
    if not tcompile.is_file():
        return CompileResult("SKIPPED", f"tCompile not found at {tcompile}")
    out_dir.mkdir(parents=True, exist_ok=True)
    props = _scratch_properties(src, out_dir, r25)
    env = scratch_env(out_dir)
    java_home = install_java_home(r25)
    if java_home:
        env["JAVA_HOME"] = str(java_home)

    def run():
        outputs = []
        for item in compile_order(src):
            proc = subprocess.run(
                ["cmd", "/c", str(tcompile), "-cf", str(props), str(item)],
                capture_output=True, text=True, env=env,
            )
            text = proc.stdout + proc.stderr
            outputs.append(f"== {item.name}\n{text}")
            if jbc_status(proc.returncode, text) != "OK":
                return CompileResult("FAIL", "\n".join(outputs))
        return CompileResult("OK", "\n".join(outputs))

    return _guarded(run, out_dir, r25)
