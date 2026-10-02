# Accuracy Harness + T24Tools Export — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Temenos-Skills *measurably* accurate (generated artefacts are field-checked and compiled against the real R25 install), then export its verified knowledge as a small data contract that T24Tools (zainknoman/T24Tools) can consume.

**Architecture:** A Python harness (`pipeline/verify_artefact.py`) runs two gates on any generated artefact: (1) a field gate reusing the Layer A SQLite DB, (2) a compile gate — `tCompile` for jBC/Infobasic and `javac` for L3 Java, both against `C:\R25`, writing only to a git-ignored `build/verify/`. A golden-case suite (`tests/golden/`) pins one known-good reference per artefact type. A separate exporter (`pipeline/export_t24tools.py`) turns the DB into `fields.json` + `descriptions.json` + `manifest.json`.

**Tech Stack:** Python 3.13 (`C:\Users\asus\AppData\Local\Programs\Python\Python313\python.exe` — the `python` on PATH is the Microsoft Store stub and does not work), pytest, SQLite (`temenos_knowledge.db`), TAFJ R25 `tCompile`, JDK 21 `javac`.

**Spec:** This plan's own "Decisions" section below (agreed in the 2026-10-02 session; there is no separate spec doc).

---

## Roadmap (where this plan sits)

| Phase | What | Repo | Status / plan |
|---|---|---|---|
| 0 | **Licensing gate** | — | **Resolved 2026-10-02** — see Decisions 5–6 and Task 0. |
| 1 | **Accuracy harness** — field gate + compile gate + golden cases | Temenos-Skills | **This plan, Tasks 1–6** |
| 2 | **Knowledge gaps** — P5 TDD/`.tut` (from `TAFJ-UnitTestFramework.pdf`), `temenos-l3` additions (`PaymentLifecycle.validatePaymentForClearing`, `isOverrideAutoApprove`, AA `Calculation`, outbound-HTTP-from-hook guidance) | Temenos-Skills | Separate plan, written after Task 6 — each gap lands with a golden case so the harness proves it |
| 3 | **Export contract** — `fields.json` / `descriptions.json` / `manifest.json` | Temenos-Skills | **This plan, Tasks 7–8** |
| 4 | **T24Tools uses a user-loaded `fields.json`** (file picker, never bundled) behind one `getApp(name)`; deterministic generators per artefact; optional guarded AI (BYO key, off by default) | T24Tools | Separate plan **in the T24Tools repo**, written against the contract from Task 7. See "What gets built where". |
| 5 | **Sync** — JAR change → regenerate → harness must pass → export → T24Tools release | both | Folded into Task 8 (CI-ready command) + Phase 4 plan |

## Decisions (do not re-litigate)

1. **Hybrid generation.** Deterministic core (catalog, positions, headers, `$PACKAGE`/`$USING`, error handling) is always on and offline. AI is an optional layer that writes only business-logic bodies, is constrained to catalog-verified fields, and its output goes through the same validator before display.
2. **Export layout = 2 data files + manifest**, not per-app files and not hash buckets. Measured 2026-10-02: core (name, position, type, mandatory) for 4,596 apps / 162,842 fields = 7.1 MB raw / **1.07 MB gzip**; with descriptions = 4.3 MB gzip. T24Tools hides lookups behind `getApp(name)` so the layout can change later without touching callers. Revisit only if core gzip > 5 MB.
3. **Accuracy is measured by compiling**, not by eyeballing — `plan/state/skill-test-prompts.md` stays as the manual trigger check; the harness is the correctness check.
4. **External GitHub repos** (JBL-L3-Java-2024, JBLR22NEW, T24-Training, …) are pattern references only. Most have no licence — never copy their code verbatim into skills.
5. **Two repos, two audiences.** Temenos-Skills is a **private repo for personal use** — it may hold Temenos-derived knowledge (schemas, descriptions, PDF index). T24Tools is a **public repo + public GitHub Pages site** — it contains **only self-authored code and generic sample data**. Nothing exported from Temenos-Skills (`fields.json`, `descriptions.json`, PDF text, code copied from `C:\R25`) is ever committed to T24Tools. For personal use, T24Tools loads `fields.json` from the user's own disk via a file picker, stored in the browser (IndexedDB), never uploaded.
6. **Generic sample naming in anything public or shared.** Bank/client identifiers (`JIB`, `JS`, `HBL`, `JBL`, `KMB`, `AOAB`, `PK.*`, people's names, real-looking account numbers, client OFS sources such as `BALOFS`) and `GLOBUS` release stamps/prose are replaced with `SAMPLE.*` / `TEST.*` names. **Real T24 identifiers are never renamed**, even if they contain those letters: `OFS.GLOBUS.MANAGER`, the `GLOBUS.BP` insert directory, the OFS `SOURCE.TYPE` value `GLOBUS`, the `GLOBUS.REF` argument, and schema fields such as `IDPMS.BOE.HBL.NUMBER` (HBL = House Bill of Lading).

## Global Constraints

- `C:\R25` is **read-only**. No task may create, modify or delete anything under it — including config files, logs, caches or compiled classes. Task 3 proves this with a before/after scan.
- Never invent a T24 field name, `$USING` component, class or method. Everything in golden reference files must be verified (field gate, `javap`, or a successful compile).
- All harness output goes to `build/verify/` (git-ignored). Exports go to `build/t24tools/` (git-ignored).
- No network access at runtime. No new dependencies beyond `pytest`.
- Run Python as `"$PY"` where `PY=/c/Users/asus/AppData/Local/Programs/Python/Python313/python.exe` (Git Bash).
- Commit after each task. End commit messages with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Review Focus

1. **Field token that isn't a field** — `AC.ACCOUNT.TITLE.1` is a field, but a componentised method call like `AC.AccountOpening.Account.Read(id, err)` is not. Expected: calls (token followed by `(`) are never reported as missing fields. Pinned by a test in Task 2.
2. **App with zero schema rows** (typo `ACCOUT`) — expected: hard failure naming the app, never "0 fields checked = pass". Pinned in Task 2.
3. **tCompile silently writing into `C:\R25`** (logs, `data/tafj/classes`, `conf/.default`) — expected: harness refuses to run if the write-free invocation isn't proven. Pinned by Task 3's scan step and the `R25_WRITE_GUARD` check in Task 3.
4. **Compiler not installed / path wrong** — expected: a clear "SKIPPED: tCompile not found at …" result with non-zero exit, not a crash and not a pass. Pinned in Task 3.
5. **Export of fields with blank type/mandatory** (41% of rows) — expected: exported as `null`, never as `"No"`/optional. Pinned in Task 7.

## File Structure

| File | Responsibility |
|---|---|
| `pipeline/artefact_fields.py` | Extract T24 field references from source text; check them against the DB. Pure functions, no I/O except the DB connection passed in. |
| `pipeline/compile_check.py` | Run `tCompile` / `javac` into `build/verify/`; return a structured result. Owns the R25 write guard. |
| `pipeline/verify_artefact.py` | CLI: field gate + compile gate on one file → exit 0/1 + optional JSON report. |
| `pipeline/run_golden.py` | Run `verify_artefact` over every case in `tests/golden/`; summary table; exit 1 on any failure. |
| `pipeline/export_t24tools.py` | DB → `fields.json`, `descriptions.json`, `manifest.json`. |
| `tests/golden/<case>/case.json` + reference source | One known-good artefact per type. |
| `tests/pipeline/test_*.py` | Unit tests for the modules above. |
| `build/verify/tafj-scratch.properties` | Generated at runtime — never committed. |

---

### Task 0: Licensing decision — RESOLVED 2026-10-02

Outcome: **`PRIVATE_ONLY`** (Decisions 5–6). Temenos-Skills stays private for personal use; public T24Tools ships *without* Temenos data and loads a user-supplied `fields.json` locally.

- [x] **Step 1:** Decision made by the developer (Temenos-Skills private, T24Tools public tools only).
- [x] **Step 2:** T24Tools legacy templates anonymised — branch `chore/generic-sample-names`, commit `4701c9d` in `D:\Personal\Projects\T24Tools` (`PK.GEN.GL.FILE`→`SAMPLE.WRITE.LOG.FILE`, `PK.M.OMER.TEST`→`SAMPLE.OFS.OPM.TEST`, `BALOFS`→`TEST.OFS`, version `DMG`→`TEST`, `Sh-title 0000400403`→`SAMPLE TITLE 0001`, GLOBUS release stamp/prose replaced; `OFS.GLOBUS.MANAGER` unchanged). `npm run check`: 80 tests passed, build OK. **Not pushed** — pushing to `main` redeploys the public site.
- [ ] **Step 3:** Developer pushes the branch / merges to `main` when ready.
- [ ] **Step 4:** Copy Decisions 5–6 into `plan/state/decisions.md` and commit.

Tasks 1–8 do not depend on this.

---

### Task 1: Test scaffolding

**Files:**
- Create: `requirements-dev.txt`, `tests/__init__.py`, `tests/pipeline/__init__.py`, `tests/conftest.py`
- Modify: `.gitignore`

- [ ] **Step 1: Add dev requirements and ignore build output**

`requirements-dev.txt`:
```
pytest>=8.4
```

Append to `.gitignore`:
```
# Harness / export output (regenerable)
build/
```

- [ ] **Step 2: Shared fixture — tiny in-memory schema DB**

`tests/conftest.py`:
```python
import sqlite3
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pipeline"))

SCHEMA = """CREATE TABLE fields (
    app TEXT, field_name TEXT, position INTEGER, java_alias TEXT,
    source_jar TEXT, field_type TEXT, mandatory TEXT, description TEXT)"""

ROWS = [
    ("ACCOUNT", "AC.CUSTOMER", 1, "Account_Customer", "AC_AccountOpening.jar", "TField", "Yes", "Customer id"),
    ("ACCOUNT", "AC.CATEGORY", 2, "Account_Category", "AC_AccountOpening.jar", "TField", "Yes", "Category"),
    ("ACCOUNT", "AC.ACCOUNT.TITLE.1", 3, "Account_AccountTitle1", "AC_AccountOpening.jar", None, None, None),
    ("CUSTOMER", "EB.CUS.MNEMONIC", 1, "Customer_Mnemonic", "ST_Customer.jar", "TField", "Yes", "Mnemonic"),
    ("CUSTOMER", "EB.CUS.SHORT.NAME", 2, "Customer_ShortName", "ST_Customer.jar", None, None, None),
]


@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO fields VALUES (?,?,?,?,?,?,?,?)", ROWS)
    yield conn
    conn.close()
```

Create empty `tests/__init__.py` and `tests/pipeline/__init__.py`.

- [ ] **Step 3: Install and run**

Run: `"$PY" -m pip install -r requirements-dev.txt && "$PY" -m pytest -q`
Expected: `no tests ran` (exit 5) — scaffolding only.

- [ ] **Step 4: Commit**

```bash
git add requirements-dev.txt .gitignore tests/__init__.py tests/pipeline/__init__.py tests/conftest.py
git commit -m "test: add pytest scaffolding and shared schema fixture"
```

---

### Task 2: Field-reference extraction and check

**Files:**
- Create: `pipeline/artefact_fields.py`
- Test: `tests/pipeline/test_artefact_fields.py`

**Interfaces:**
- Produces:
  - `app_prefix(conn, app: str) -> str` — e.g. `"AC."`, `"EB.CUS."`; raises `UnknownApp` if the app has no rows.
  - `extract_refs(source: str, prefix: str, record_class: str) -> FieldRefs` where `FieldRefs = namedtuple("FieldRefs", "legacy componentised")`, both `set[str]`. `legacy` holds `AC.CATEGORY`-style names; `componentised` holds java aliases like `Account_Category`.
  - `check_fields(conn, app: str, source: str) -> FieldCheck` where `FieldCheck = namedtuple("FieldCheck", "app verified missing")`, `verified`/`missing` sorted lists.
  - `record_class(app: str) -> str` — `"ACCOUNT"` → `"Account"`, `"FUNDS.TRANSFER"` → `"FundsTransfer"`.

- [ ] **Step 1: Write the failing tests**

```python
import pytest

from artefact_fields import UnknownApp, app_prefix, check_fields, extract_refs, record_class


def test_prefix_is_common_dotted_prefix(db):
    assert app_prefix(db, "ACCOUNT") == "AC."
    assert app_prefix(db, "CUSTOMER") == "EB.CUS."


def test_unknown_app_is_an_error_not_a_pass(db):
    with pytest.raises(UnknownApp):
        app_prefix(db, "ACCOUT")


def test_record_class():
    assert record_class("ACCOUNT") == "Account"
    assert record_class("FUNDS.TRANSFER") == "FundsTransfer"


def test_legacy_refs():
    src = "lvCat = R.NEW(AC.CATEGORY)\nlvT = R.NEW(AC.ACCOUNT.TITLE.1)\n"
    refs = extract_refs(src, "AC.", "Account")
    assert refs.legacy == {"AC.CATEGORY", "AC.ACCOUNT.TITLE.1"}


def test_componentised_refs_skip_method_calls():
    src = (
        "x = EB.SystemTables.getRNew(AC.AccountOpening.Account.Category)\n"
        "r = AC.AccountOpening.Account.Read(id, err)\n"
    )
    refs = extract_refs(src, "AC.", "Account")
    assert refs.componentised == {"Account_Category"}


def test_comments_are_ignored():
    src = "* uses AC.NOT.A.FIELD in a comment\nRETURN\n"
    assert extract_refs(src, "AC.", "Account").legacy == set()


def test_check_reports_missing(db):
    src = "a = R.NEW(AC.CATEGORY)\nb = R.NEW(AC.CATEGORYY)\nc = AC.AccountOpening.Account.Customer\n"
    result = check_fields(db, "ACCOUNT", src)
    assert result.verified == ["AC.CATEGORY", "Account_Customer"]
    assert result.missing == ["AC.CATEGORYY"]
```

- [ ] **Step 2: Run to verify failure**

Run: `"$PY" -m pytest tests/pipeline/test_artefact_fields.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'artefact_fields'`

- [ ] **Step 3: Implement**

```python
#!/usr/bin/env python3
"""Find T24 field references in generated source and check them against
the Layer A schema DB. Legacy Infobasic uses EQU names (AC.CATEGORY);
componentised jBC uses <Comp>.<Module>.<Record>.<Field>, which maps to the
java_alias column (<Record>_<Field>). Java L3 code is not checked here --
javac against the R25 record classes is the field gate for Java."""
import os
import re
from collections import namedtuple

FieldRefs = namedtuple("FieldRefs", "legacy componentised")
FieldCheck = namedtuple("FieldCheck", "app verified missing")


class UnknownApp(Exception):
    pass


def record_class(app):
    return "".join(part.capitalize() for part in app.split("."))


def app_prefix(conn, app):
    names = [r[0] for r in conn.execute("SELECT field_name FROM fields WHERE app = ?", (app,))]
    if not names:
        raise UnknownApp(f"no schema rows for app '{app}'")
    common = os.path.commonprefix(names)
    return common[: common.rfind(".") + 1]


def _strip_comments(source):
    lines = []
    for line in source.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("*") or stripped.startswith("!"):
            continue
        lines.append(line.split(";*")[0])
    return "\n".join(lines)


def extract_refs(source, prefix, record_cls):
    code = _strip_comments(source)
    legacy = set()
    if prefix:
        pattern = re.compile(r"(?<![\w.])" + re.escape(prefix) + r"[A-Z0-9]+(?:\.[A-Z0-9]+)*(?![\w.(])")
        legacy = set(pattern.findall(code))
    comp_pattern = re.compile(
        r"\b[A-Z]{2,}\.[A-Z][A-Za-z0-9]*\." + re.escape(record_cls) + r"\.([A-Z][A-Za-z0-9]*)\b(?!\s*\()"
    )
    componentised = {f"{record_cls}_{m}" for m in comp_pattern.findall(code)}
    return FieldRefs(legacy, componentised)


def check_fields(conn, app, source):
    app = app.upper()
    prefix = app_prefix(conn, app)
    refs = extract_refs(source, prefix, record_class(app))
    rows = conn.execute("SELECT field_name, java_alias FROM fields WHERE app = ?", (app,)).fetchall()
    names = {r[0] for r in rows}
    aliases = {r[1] for r in rows}
    found = refs.legacy | refs.componentised
    missing = sorted(f for f in found if f not in names and f not in aliases)
    verified = sorted(found - set(missing))
    return FieldCheck(app, verified, missing)
```

- [ ] **Step 4: Run to verify pass**

Run: `"$PY" -m pytest tests/pipeline/test_artefact_fields.py -q`
Expected: 7 passed.

- [ ] **Step 5: Sanity-check against the real DB**

Run: `"$PY" -c "import sys,sqlite3;sys.path.insert(0,'pipeline');from artefact_fields import app_prefix;c=sqlite3.connect('temenos_knowledge.db');print(app_prefix(c,'ACCOUNT'),app_prefix(c,'CUSTOMER'),app_prefix(c,'FUNDS.TRANSFER'))"`
Expected: `AC. EB.CUS. FT.` — if any prefix is empty, that app has mixed prefixes; note it in the commit message (the componentised path still works for it).

- [ ] **Step 6: Commit**

```bash
git add pipeline/artefact_fields.py tests/pipeline/test_artefact_fields.py
git commit -m "feat(harness): extract and verify T24 field references in generated source"
```

---

### Task 3: Compile gate (spike first, then module)

**Files:**
- Create: `pipeline/compile_check.py`
- Test: `tests/pipeline/test_compile_check.py`

**Interfaces:**
- Produces:
  - `CompileResult = namedtuple("CompileResult", "status output")`; `status` ∈ `{"OK", "FAIL", "SKIPPED"}`.
  - `compile_java(src: Path, out_dir: Path, r25: Path = R25) -> CompileResult`
  - `compile_jbc(src: Path, out_dir: Path, r25: Path = R25) -> CompileResult`
  - `r25_writes_since(marker: Path, r25: Path = R25) -> list[Path]` — files under `r25` newer than `marker`.

- [ ] **Step 1: Spike — prove a write-free tCompile invocation (manual, ~30 min)**

The R25 config (`C:\R25\TAFJ\conf\tafj.properties`) points `temn.tafj.directory.java` and `.classes` at `C:\R25\TAFJ\data/tafj/...`, so the default invocation **writes into C:\R25** — forbidden. The PDFs (`TAFJ ... T3TAFJ - R19.pdf` p.41–42) document `tCompile -cf <config>`, which picks the config file.

```bash
mkdir -p build/verify/spike/{java,classes,src}
touch build/verify/spike/marker
cp /c/R25/TAFJ/conf/tafj.properties build/verify/spike/tafj-scratch.properties   # copy OUT of R25 — read only
# edit build/verify/spike/tafj-scratch.properties: point these 2 keys at build/verify/spike (absolute D:\ paths):
#   temn.tafj.directory.java    temn.tafj.directory.classes
printf 'PROGRAM SPIKE.HELLO\n    CRT "hi"\nEND\n' > build/verify/spike/src/SPIKE.HELLO.b
cmd //c "C:\\R25\\TAFJ\\bin\\tCompile.bat -cf D:\\Personal\\Projects\\Temenos-Skills\\build\\verify\\spike\\tafj-scratch.properties D:\\Personal\\Projects\\Temenos-Skills\\build\\verify\\spike\\src\\SPIKE.HELLO.b"
find /c/R25 -newer build/verify/spike/marker -type f 2>/dev/null | head
```

Pass condition — **all three**: (a) a `.class` for `SPIKE.HELLO` appears under `build/verify/spike/classes`; (b) the `find` prints nothing; (c) the output has no "configuration not found".

If `-cf` rejects an absolute path, or the `find` lists anything (logs, `conf/.default`, `uid_lock`, …): **STOP and ask the developer.** Do not work around it by writing into `C:\R25`. Record what was written so the developer can decide (e.g. approve a dedicated, separate TAFJ copy for compiling).

Record the working command line and any extra keys you had to override (log directories etc.) in `plan/state/decisions.md` under "tCompile invocation".

- [ ] **Step 2: Write the failing tests**

```python
from pathlib import Path

from compile_check import CompileResult, compile_java, compile_jbc, r25_writes_since


def test_missing_r25_is_skipped_not_passed(tmp_path):
    src = tmp_path / "A.java"
    src.write_text("class A {}")
    result = compile_java(src, tmp_path / "out", r25=tmp_path / "no-such-r25")
    assert result.status == "SKIPPED"
    assert "no-such-r25" in result.output


def test_jbc_missing_r25_is_skipped(tmp_path):
    src = tmp_path / "X.b"
    src.write_text("PROGRAM X\nEND\n")
    assert compile_jbc(src, tmp_path / "out", r25=tmp_path / "nope").status == "SKIPPED"


def test_write_guard_finds_newer_files(tmp_path):
    marker = tmp_path / "marker"
    marker.write_text("")
    fake_r25 = tmp_path / "r25"
    fake_r25.mkdir()
    newer = fake_r25 / "touched.log"
    newer.write_text("x")
    import os, time
    old = time.time() - 60
    os.utime(marker, (old, old))
    assert r25_writes_since(marker, r25=fake_r25) == [newer]
```

- [ ] **Step 3: Run to verify failure**

Run: `"$PY" -m pytest tests/pipeline/test_compile_check.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'compile_check'`

- [ ] **Step 4: Implement** (fill `TCOMPILE_OVERRIDES` with the keys recorded in Step 1 — the two below are the known minimum)

```python
#!/usr/bin/env python3
"""Compile gate for generated artefacts. Compiles against the read-only R25
install and writes ONLY under the out_dir given (build/verify/...). Every
compile is bracketed by a write guard: if anything under C:\\R25 changed,
the result is FAIL regardless of compiler output."""
import shutil
import subprocess
import time
from collections import namedtuple
from pathlib import Path

R25 = Path(r"C:\R25")
CompileResult = namedtuple("CompileResult", "status output")

# Keys verified in Task 3 Step 1 -- see plan/state/decisions.md "tCompile invocation".
TCOMPILE_OVERRIDES = ("temn.tafj.directory.java", "temn.tafj.directory.classes")


def r25_writes_since(marker, r25=R25):
    since = marker.stat().st_mtime
    return sorted(p for p in Path(r25).rglob("*") if p.is_file() and p.stat().st_mtime > since)


def _guarded(run, out_dir, r25):
    out_dir.mkdir(parents=True, exist_ok=True)
    marker = out_dir / ".r25-marker"
    marker.write_text("")
    time.sleep(1)  # mtime resolution
    result = run()
    writes = r25_writes_since(marker, r25 / "TAFJ") + r25_writes_since(marker, r25 / "bnk" / "T24_BP")
    if writes:
        listed = "\n".join(str(w) for w in writes[:20])
        return CompileResult("FAIL", f"R25_WRITE_GUARD: compile wrote into {r25}:\n{listed}")
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
            [javac, "-proc:none", "-nowarn", "-d", str(out_dir), "-cp", cp, str(src)],
            capture_output=True, text=True,
        )
        return CompileResult("OK" if proc.returncode == 0 else "FAIL", proc.stdout + proc.stderr)

    return _guarded(run, out_dir, r25)


def _scratch_properties(out_dir, r25):
    base = (r25 / "TAFJ" / "conf" / "tafj.properties").read_text(encoding="latin-1").splitlines()
    targets = {
        "temn.tafj.directory.java": out_dir / "java",
        "temn.tafj.directory.classes": out_dir / "classes",
    }
    lines = [l for l in base if l.split("=", 1)[0].strip() not in TCOMPILE_OVERRIDES]
    for key in TCOMPILE_OVERRIDES:
        path = targets.get(key, out_dir / key.rsplit(".", 1)[-1])
        path.mkdir(parents=True, exist_ok=True)
        lines.append(f"{key}={path}")
    props = out_dir / "tafj-scratch.properties"
    props.write_text("\n".join(lines) + "\n", encoding="latin-1")
    return props


def compile_jbc(src, out_dir, r25=R25):
    src, out_dir, r25 = Path(src), Path(out_dir), Path(r25)
    tcompile = r25 / "TAFJ" / "bin" / "tCompile.bat"
    if not tcompile.is_file():
        return CompileResult("SKIPPED", f"tCompile not found at {tcompile}")
    out_dir.mkdir(parents=True, exist_ok=True)
    props = _scratch_properties(out_dir, r25)

    def run():
        proc = subprocess.run(
            ["cmd", "/c", str(tcompile), "-cf", str(props.resolve()), str(src.resolve())],
            capture_output=True, text=True,
        )
        text = proc.stdout + proc.stderr
        failed = proc.returncode != 0 or "error" in text.lower()
        return CompileResult("FAIL" if failed else "OK", text)

    return _guarded(run, out_dir, r25)
```

- [ ] **Step 5: Run unit tests**

Run: `"$PY" -m pytest tests/pipeline/test_compile_check.py -q`
Expected: 3 passed.

- [ ] **Step 6: Real compile smoke test** (requires `C:\R25`)

Run: `"$PY" -c "import sys;sys.path.insert(0,'pipeline');from pathlib import Path;from compile_check import compile_jbc;print(compile_jbc(Path('build/verify/spike/src/SPIKE.HELLO.b'),Path('build/verify/smoke')))"`
Expected: `CompileResult(status='OK', ...)`. If the "error" substring check misfires on a clean compile (e.g. the banner contains "error"), tighten it to the exact failure marker seen in the spike output and add that string to a test.

- [ ] **Step 7: Commit**

```bash
git add pipeline/compile_check.py tests/pipeline/test_compile_check.py plan/state/decisions.md
git commit -m "feat(harness): compile gate for jBC (tCompile) and L3 Java (javac) with R25 write guard"
```

---

### Task 4: `verify_artefact.py` CLI

**Files:**
- Create: `pipeline/verify_artefact.py`
- Test: `tests/pipeline/test_verify_artefact.py`

**Interfaces:**
- Consumes: `check_fields` (Task 2), `compile_java`, `compile_jbc` (Task 3).
- Produces: `verify(path: Path, apps: list[str], conn, out_dir: Path, compile_fn=None) -> dict` with keys `file`, `fields` (list of `{app, verified, missing}`), `compile` (`{status, output}`), `passed` (bool). CLI: `verify_artefact.py --file F --app A [--app B] [--json] [--no-compile]`, exit 0 iff `passed`.

- [ ] **Step 1: Write the failing tests**

```python
from pathlib import Path

from compile_check import CompileResult
from verify_artefact import verify

OK = lambda src, out: CompileResult("OK", "")
FAIL = lambda src, out: CompileResult("FAIL", "boom")


def test_pass_when_fields_ok_and_compiles(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("x = R.NEW(AC.CATEGORY)\n")
    report = verify(f, ["ACCOUNT"], db, tmp_path / "out", compile_fn=OK)
    assert report["passed"] is True
    assert report["fields"][0]["missing"] == []


def test_fail_on_missing_field_even_if_compiles(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("x = R.NEW(AC.NOPE)\n")
    assert verify(f, ["ACCOUNT"], db, tmp_path / "out", compile_fn=OK)["passed"] is False


def test_fail_on_compile_error(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("x = R.NEW(AC.CATEGORY)\n")
    report = verify(f, ["ACCOUNT"], db, tmp_path / "out", compile_fn=FAIL)
    assert report["passed"] is False
    assert report["compile"]["output"] == "boom"


def test_skipped_compile_is_not_a_pass(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("x = R.NEW(AC.CATEGORY)\n")
    skip = lambda s, o: CompileResult("SKIPPED", "no R25")
    assert verify(f, ["ACCOUNT"], db, tmp_path / "out", compile_fn=skip)["passed"] is False


def test_unknown_app_fails_cleanly(db, tmp_path):
    f = tmp_path / "V.b"
    f.write_text("RETURN\n")
    report = verify(f, ["ACCOUT"], db, tmp_path / "out", compile_fn=OK)
    assert report["passed"] is False
    assert "ACCOUT" in report["fields"][0]["error"]
```

- [ ] **Step 2: Run to verify failure**

Run: `"$PY" -m pytest tests/pipeline/test_verify_artefact.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'verify_artefact'`

- [ ] **Step 3: Implement**

```python
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
    return {"file": str(path), "fields": fields, "compile": compiled, "passed": ok}


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
```

Note `--no-compile` makes `passed` reflect fields only; it exists for quick iteration and must never be used by `run_golden.py`.

- [ ] **Step 4: Run to verify pass**

Run: `"$PY" -m pytest tests/pipeline -q`
Expected: all tests pass (15).

- [ ] **Step 5: Commit**

```bash
git add pipeline/verify_artefact.py tests/pipeline/test_verify_artefact.py
git commit -m "feat(harness): verify_artefact CLI combining field and compile gates"
```

---

### Task 5: Golden cases + runner

**Files:**
- Create: `tests/golden/l3-account-category-guard/case.json`, `tests/golden/l3-account-category-guard/AcCategoryGuard.java`
- Create: `tests/golden/jbc-customer-mnemonic-vvr/case.json`, `tests/golden/jbc-customer-mnemonic-vvr/V.CUS.MNEMONIC.CHECK.b`
- Create: `pipeline/run_golden.py`
- Test: `tests/pipeline/test_run_golden.py`

**Interfaces:**
- Consumes: `verify` (Task 4).
- Produces: `load_cases(root: Path) -> list[dict]` (each `case.json` + `"dir"`); `run_golden.py [--case NAME]` prints one line per case and exits 1 on any failure.

`case.json` schema:
```json
{
  "name": "l3-account-category-guard",
  "artefact": "L3 RecordLifecycle.validateRecord",
  "skill": "temenos-l3",
  "requirement": "Block an ACCOUNT input if CATEGORY is empty.",
  "apps": ["ACCOUNT"],
  "file": "AcCategoryGuard.java",
  "expected_fields": ["AC.CATEGORY"]
}
```

- [ ] **Step 1: Golden case 1 — L3 Java** (every type/method below verified with `javap` against R25 on 2026-10-02: `RecordLifecycle`/`TransactionContext` in `EB_TemplateHook.jar`; `AccountRecord(TStructure)`, `getCategory()`, `toStructure()` in `AC_AccountOpening.jar`; `TField.getValue()`/`setError(String)`, `T24Record.getValidationResponse()` in `TAFJClient.jar`)

`tests/golden/l3-account-category-guard/AcCategoryGuard.java`:
```java
package com.temenos.t24.custom.golden;
// Implements: RecordLifecycle from EB_TemplateHook.jar
// T24 Application: ACCOUNT
// Hook type: RecordLifecycle

import com.temenos.api.TStructure;
import com.temenos.api.TValidationResponse;
import com.temenos.t24.api.complex.eb.templatehook.TransactionContext;
import com.temenos.t24.api.hook.system.RecordLifecycle;
import com.temenos.t24.api.records.account.AccountRecord;

public class AcCategoryGuard extends RecordLifecycle {

    @Override
    public TValidationResponse validateRecord(String application, String currentRecordId,
            TStructure currentRecord, TStructure unauthorisedRecord,
            TStructure liveRecord, TransactionContext transactionContext) {

        AccountRecord rec = new AccountRecord(currentRecord);
        String category = rec.getCategory().getValue();
        if (category == null || category.isEmpty()) {
            rec.getCategory().setError("CATEGORY IS MANDATORY");
        }
        currentRecord.set(rec.toStructure());
        return rec.getValidationResponse();
    }
}
```
Plus `case.json` exactly as in the schema example above.

- [ ] **Step 2: Verify case 1 compiles**

Run: `"$PY" pipeline/verify_artefact.py --file tests/golden/l3-account-category-guard/AcCategoryGuard.java --app ACCOUNT`
Expected: `COMPILE: OK` / `PASS`. If `currentRecord.set(...)` fails to compile, run `javap -cp "C:/R25/TAFJ/lib/TAFJClient.jar" com.temenos.api.TStructure`, fix the golden file **and** the matching snippet in `skills/temenos-l3/SKILL.md` ("Always commit the record back"), and note the fix in the commit.

- [ ] **Step 3: Golden case 2 — componentised jBC VVR (this one is expected to expose a skill bug)**

`skills/temenos-jbc/SKILL.md` Template C currently shows `EB.SystemTables.getRNew('<T24.FIELD.NAME>', '', 1, '')` — a field-name string and four arguments. That signature could not be confirmed from the JARs (no compiled `getRNew` class exists; it is a component accessor). The compiler decides. Start with the field-position form:

`tests/golden/jbc-customer-mnemonic-vvr/V.CUS.MNEMONIC.CHECK.b`:
```
*-----------------------------------------------------------------------------
* Program    : V.CUS.MNEMONIC.CHECK
* Type       : VVR
* Description: Reject CUSTOMER input when MNEMONIC is empty
* Application: CUSTOMER
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* 2026-10-02 | golden-case     | Initial version
*-----------------------------------------------------------------------------
$PACKAGE GOLDEN.Validation
SUBROUTINE V.CUS.MNEMONIC.CHECK
    $USING EB.SystemTables
    $USING ST.Customer

    lvMnemonic = EB.SystemTables.getRNew(ST.Customer.Customer.Mnemonic)
    IF lvMnemonic EQ '' THEN
        EB.SystemTables.setE('MNEMONIC IS MANDATORY')
    END
RETURN
END
```
`case.json`: name `jbc-customer-mnemonic-vvr`, artefact `jBC VVR`, skill `temenos-jbc`, apps `["CUSTOMER"]`, file `V.CUS.MNEMONIC.CHECK.b`, expected_fields `["Customer_Mnemonic"]`.

- [ ] **Step 4: Iterate case 2 until it compiles — compiler is the authority**

Run: `"$PY" pipeline/verify_artefact.py --file tests/golden/jbc-customer-mnemonic-vvr/V.CUS.MNEMONIC.CHECK.b --app CUSTOMER`
- Field part must show `VERIFIED in CUSTOMER: Customer_Mnemonic`.
- If tCompile rejects a `$USING`, an accessor or `setE`: read the error, find the real name (`"$PY" pipeline/query_docs.py "getRNew setE componentised" -n 5`, `$PACKAGE`/`$USING` examples in `C:\R25\bnk\T24_BP\*.b` via grep), change **one thing at a time**, recompile.
- When it compiles: update `skills/temenos-jbc/SKILL.md` Template C (and any other `getRNew(` / `setE(` snippet in `temenos-jbc`, `temenos-infobasic`) to the compiled form. Record the before/after in the commit message.
- If it cannot be made to compile within ~1 hour, STOP and report the exact compiler output to the developer.

- [ ] **Step 5: Write the runner test**

```python
import json
from pathlib import Path

from run_golden import load_cases


def test_load_cases_reads_case_json(tmp_path):
    case_dir = tmp_path / "c1"
    case_dir.mkdir()
    (case_dir / "case.json").write_text(json.dumps({"name": "c1", "apps": ["ACCOUNT"], "file": "A.b"}))
    (tmp_path / "not-a-case").mkdir()
    cases = load_cases(tmp_path)
    assert [c["name"] for c in cases] == ["c1"]
    assert cases[0]["dir"] == case_dir
```

- [ ] **Step 6: Implement the runner**

```python
#!/usr/bin/env python3
"""Run every golden case in tests/golden through verify_artefact (fields +
compile against R25). Exit 1 if any case fails. This is the accuracy
regression suite: a skill change that breaks a golden case is a bug."""
import argparse
import json
import sqlite3
import sys
from pathlib import Path

from verify_artefact import verify

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
    ap.add_argument("--db", default="temenos_knowledge.db")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    failures = 0
    for case in load_cases():
        if args.case and case["name"] != args.case:
            continue
        report = verify(case["dir"] / case["file"], case["apps"], conn, Path("build/verify/golden"))
        expected = set(case.get("expected_fields", []))
        seen = {f for r in report["fields"] for f in r["verified"]}
        lost = expected - seen if case["file"].endswith(".b") else set()
        ok = report["passed"] and not lost
        failures += not ok
        detail = report["compile"]["status"] + (f" expected-fields-not-seen={sorted(lost)}" if lost else "")
        print(f"{'PASS' if ok else 'FAIL'}  {case['name']:<40} {detail}")
    conn.close()
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 7: Run everything**

Run: `"$PY" -m pytest tests/pipeline -q && "$PY" pipeline/run_golden.py`
Expected: unit tests pass; `PASS  jbc-customer-mnemonic-vvr  OK` and `PASS  l3-account-category-guard  OK`.

- [ ] **Step 8: Commit**

```bash
git add tests/golden pipeline/run_golden.py tests/pipeline/test_run_golden.py skills/
git commit -m "feat(harness): golden-case suite; first L3 Java and jBC VVR cases compile against R25"
```

---

### Task 6: Wire the harness into the skills

**Files:**
- Modify: `skills/temenos-dev/SKILL.md` (Field Verification Gate section)
- Modify: `CLAUDE.md` (Step 5 checklist, Running the pipeline, Next tasks)

- [ ] **Step 1:** In `skills/temenos-dev/SKILL.md`, directly after the existing `validate_fields.py` instruction in the Field Verification Gate, add:

```markdown
**After generating** a `.b` or `.java` artefact, save it and run the full gate:

    python pipeline/verify_artefact.py --file <path> --app <APP> [--app <APP2>]

`PASS` = every field verified and the file compiled against the R25 install.
`FAIL` = fix and re-run before presenting the code. `COMPILE: SKIPPED` (no
C:\R25 on this machine) = say so explicitly to the developer; never present
the code as compile-verified.
```

- [ ] **Step 2:** In `CLAUDE.md`:
  - Step 5 checklist: add `- [ ] pipeline/verify_artefact.py returns PASS (or SKIPPED is stated to the developer)`.
  - "Running the extraction pipeline": add the `verify_artefact.py` and `run_golden.py` commands.
  - "Next tasks": add `- [ ] **P7** Accuracy harness + T24Tools export — plan/2026-10-02-accuracy-harness-and-t24tools-export.md`.

- [ ] **Step 3:** Run `"$PY" pipeline/run_golden.py` — expected unchanged (2 PASS).

- [ ] **Step 4: Commit**

```bash
git add skills/temenos-dev/SKILL.md CLAUDE.md
git commit -m "docs: require verify_artefact gate before presenting generated code"
```

---

### Task 7: T24Tools export

**Files:**
- Create: `pipeline/export_t24tools.py`
- Test: `tests/pipeline/test_export_t24tools.py`

**Interfaces:**
- Produces files in `--out` (default `build/t24tools/R25/`). This is the **contract** the Phase 4 plan builds against:

`fields.json`
```json
{
  "release": "R25",
  "apps": {
    "ACCOUNT": {
      "prefix": "AC.",
      "recordClass": "Account",
      "fields": [[1, "AC.CUSTOMER", "Account_Customer", "TField", "Yes"]]
    }
  }
}
```
Field tuple = `[position, name, javaAlias, type|null, mandatory|null]`, sorted by position. `null` means "not captured" — consumers must never treat it as optional.

`descriptions.json`
```json
{ "release": "R25", "apps": { "ACCOUNT": { "AC.CUSTOMER": "Identifies the Customer ..." } } }
```
Only non-empty descriptions are included.

`manifest.json`
```json
{ "release": "R25", "schemaVersion": 1, "generated": "<ISO-8601 UTC>",
  "apps": 4596, "fields": 162842,
  "files": { "fields.json": {"bytes": 0, "sha256": "..."}, "descriptions.json": {"bytes": 0, "sha256": "..."} } }
```

- Python API: `build_export(conn, release: str) -> tuple[dict, dict]` (fields doc, descriptions doc); `write_export(conn, out_dir: Path, release: str, now: str) -> dict` (returns manifest).

- [ ] **Step 1: Write the failing tests**

```python
import json

from export_t24tools import build_export, write_export


def test_fields_doc_shape_and_nulls(db):
    fields, _ = build_export(db, "R25")
    acc = fields["apps"]["ACCOUNT"]
    assert acc["prefix"] == "AC."
    assert acc["recordClass"] == "Account"
    assert acc["fields"][0] == [1, "AC.CUSTOMER", "Account_Customer", "TField", "Yes"]
    assert acc["fields"][2] == [3, "AC.ACCOUNT.TITLE.1", "Account_AccountTitle1", None, None]


def test_descriptions_skip_empty(db):
    _, desc = build_export(db, "R25")
    assert desc["apps"]["ACCOUNT"] == {"AC.CUSTOMER": "Customer id", "AC.CATEGORY": "Category"}


def test_output_is_deterministic(db, tmp_path):
    m1 = write_export(db, tmp_path / "a", "R25", now="2026-10-02T00:00:00Z")
    m2 = write_export(db, tmp_path / "b", "R25", now="2026-10-02T00:00:00Z")
    assert m1 == m2
    assert (tmp_path / "a" / "fields.json").read_bytes() == (tmp_path / "b" / "fields.json").read_bytes()


def test_manifest_counts(db, tmp_path):
    m = write_export(db, tmp_path, "R25", now="2026-10-02T00:00:00Z")
    assert (m["apps"], m["fields"], m["schemaVersion"]) == (2, 5, 1)
    assert json.loads((tmp_path / "manifest.json").read_text()) == m
```

- [ ] **Step 2: Run to verify failure**

Run: `"$PY" -m pytest tests/pipeline/test_export_t24tools.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'export_t24tools'`

- [ ] **Step 3: Implement**

```python
#!/usr/bin/env python3
"""Export the Layer A schema DB as the T24Tools data contract:
fields.json (positions/types, ~1 MB gzip), descriptions.json (lazy-loaded),
manifest.json (counts + sha256). Output is byte-for-byte deterministic for
the same DB, so CI can diff it.

  python pipeline/export_t24tools.py --out build/t24tools/R25 --release R25
"""
import argparse
import gzip
import hashlib
import json
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from artefact_fields import record_class

SCHEMA_VERSION = 1
GZIP_WARN_BYTES = 5_000_000


def _blank_to_none(value):
    return value if value not in (None, "") else None


def _prefix(names):
    import os
    common = os.path.commonprefix(names)
    return common[: common.rfind(".") + 1]


def build_export(conn, release):
    rows = conn.execute(
        "SELECT app, position, field_name, java_alias, field_type, mandatory, description "
        "FROM fields ORDER BY app, position, field_name"
    ).fetchall()
    by_app = defaultdict(list)
    for row in rows:
        by_app[row[0]].append(row[1:])
    apps, descs = {}, {}
    for app in sorted(by_app):
        recs = by_app[app]
        apps[app] = {
            "prefix": _prefix([r[1] for r in recs]),
            "recordClass": record_class(app),
            "fields": [[r[0], r[1], r[2], _blank_to_none(r[3]), _blank_to_none(r[4])] for r in recs],
        }
        d = {r[1]: r[5] for r in recs if _blank_to_none(r[5])}
        if d:
            descs[app] = d
    return {"release": release, "apps": apps}, {"release": release, "apps": descs}


def _dump(doc, path):
    data = json.dumps(doc, ensure_ascii=False, separators=(",", ":"), sort_keys=False).encode("utf-8")
    path.write_bytes(data)
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}, data


def write_export(conn, out_dir, release, now=None):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    fields, descs = build_export(conn, release)
    f_meta, f_bytes = _dump(fields, out_dir / "fields.json")
    d_meta, _ = _dump(descs, out_dir / "descriptions.json")
    manifest = {
        "release": release,
        "schemaVersion": SCHEMA_VERSION,
        "generated": now or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "apps": len(fields["apps"]),
        "fields": sum(len(a["fields"]) for a in fields["apps"].values()),
        "files": {"fields.json": f_meta, "descriptions.json": d_meta},
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    gz = len(gzip.compress(f_bytes, 9))
    if gz > GZIP_WARN_BYTES:
        print(f"WARNING: fields.json is {gz/1e6:.1f} MB gzipped -- revisit the single-file layout (Decision 2)")
    return manifest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="temenos_knowledge.db")
    ap.add_argument("--out", default="build/t24tools/R25")
    ap.add_argument("--release", default="R25")
    args = ap.parse_args()
    conn = sqlite3.connect(args.db)
    m = write_export(conn, Path(args.out), args.release)
    conn.close()
    print(f"Exported {m['apps']} apps / {m['fields']} fields to {args.out}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests**

Run: `"$PY" -m pytest tests/pipeline -q`
Expected: all pass.

- [ ] **Step 5: Real export**

Run: `"$PY" pipeline/export_t24tools.py`
Expected: `Exported 4596 apps / 162842 fields to build/t24tools/R25`, no WARNING. Then `gzip -9 -c build/t24tools/R25/fields.json | wc -c` ≈ 1.0–1.2 MB.

- [ ] **Step 6: Commit**

```bash
git add pipeline/export_t24tools.py tests/pipeline/test_export_t24tools.py
git commit -m "feat(export): T24Tools data contract (fields/descriptions/manifest)"
```

---

### Task 8: One release command (Phase 5 hook)

**Files:**
- Create: `pipeline/release_t24tools.py`
- Modify: `CLAUDE.md` (Running the pipeline)

- [ ] **Step 1: Implement** — golden suite must pass before an export is produced:

```python
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", default="R25")
    args = ap.parse_args()
    golden = subprocess.run([sys.executable, str(HERE / "run_golden.py")])
    if golden.returncode != 0:
        print("Golden suite failed -- export NOT written.")
        sys.exit(1)
    sys.exit(subprocess.run([
        sys.executable, str(HERE / "export_t24tools.py"),
        "--release", args.release, "--out", f"build/t24tools/{args.release}",
    ]).returncode)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it**

Run: `"$PY" pipeline/release_t24tools.py`
Expected: two `PASS` golden lines, then `Exported 4596 apps / 162842 fields ...`.

- [ ] **Step 3:** Add to CLAUDE.md "Running the extraction pipeline":
```bash
# Accuracy gate + T24Tools export (P7) -- export is only written if golden cases pass
python pipeline/release_t24tools.py --release R25
```

- [ ] **Step 4: Commit**

```bash
git add pipeline/release_t24tools.py CLAUDE.md
git commit -m "feat(export): gated release command for the T24Tools data contract"
```

---

### Task 9: Anonymise bank names in Temenos-Skills + fix a verified API error

Temenos-Skills is private (Decision 5), so this is hygiene, not a legal blocker — but skill text is what gets sent to an AI and what ends up in generated code, so client names must not leak into output. Scan run 2026-10-02 (`git grep -w`, excluding `table-schema/` and `classes/`): `JS` 0, `HBL` 0, `JBL` 0, `JIB` 5 lines, `KMB` 5 lines, `AOAB` 2 lines, `GLOBUS` 48 lines (all real identifiers — keep, per Decision 6).

**Files:**
- Modify: `skills/temenos-l3/README.md:8,288`
- Modify: `skills/temenos-l3/SKILL.md:840,865,1371,2123,2126,2363,2452,2453`
- Modify: `skills/temenos-dev/references/apis/ofs-api.md` (`OFS.POST.MESSAGE` section, ~line 185)

- [ ] **Step 1: Exact replacements** (line numbers as of commit `10b37cb`)

| File:line | Before | After |
|---|---|---|
| `temenos-l3/README.md:8` | `real bank implementation code (JIB/AOAB)` | `real bank implementation code (anonymised client projects)` |
| `temenos-l3/README.md:288` | `from JIB/AOAB bank projects` | `from anonymised bank projects` |
| `temenos-l3/SKILL.md:840` | `"CUSTOMER,JIB.OFS.UPDATE"` | `"CUSTOMER,SAMPLE.OFS.UPDATE"` |
| `temenos-l3/SKILL.md:865` | `"EB.JIB.GOAML.TXN.LIST"` | `"EB.SAMPLE.GOAML.TXN.LIST"` |
| `temenos-l3/SKILL.md:1371` | `` `EB.JIB.POST.RESTRICT` → `EbJibPostRestrictRecord` `` | `` `EB.SAMPLE.POST.RESTRICT` → `EbSamplePostRestrictRecord` `` |
| `temenos-l3/SKILL.md:2123,2126` | `"KMB.CHILD.CIF"` (both) | `"L.CHILD.CIF"` |
| `temenos-l3/SKILL.md:2363` | `",KMB.AC.INPUT"` | `",SAMPLE.AC.INPUT"` |
| `temenos-l3/SKILL.md:2452` | `"LIMIT,KMB.INPUT"` | `"LIMIT,SAMPLE.INPUT"` |
| `temenos-l3/SKILL.md:2453` | `"KMB.OFS.LIMIT"` | `"SAMPLE.OFS.LIMIT"` |

Do **not** touch: `OFS.GLOBUS.MANAGER`, `GLOBUS.BP`, `SOURCE.TYPE` value `GLOBUS`, `GLOBUS.REF`, or anything under `table-schema/` / `classes/` (e.g. `IDPMS.BOE.HBL.NUMBER` is a real field).

- [ ] **Step 2: Fix the `OFS.POST.MESSAGE` signature.** `ofs-api.md` documents `CALL OFS.POST.MESSAGE(OFS.SOURCE.ID, OFS.MESSAGES, QUEUE.KEY)` — 3 arguments. Every call in R25's `C:\R25\bnk\T24_BP\*.b` uses **4**: `OfsPostMessage(ofsMsg, ofsMsgId, ofsSourceId, options)` (12 call sites checked 2026-10-02). Replace the signature and its argument table with the 4-argument form: message, message id (out), OFS source id, options. Add a golden case for it in the Phase 2 plan.

- [ ] **Step 3: Verify nothing bank-specific remains and nothing real was renamed**

Run: `git grep -n -w -I -E "JIB|KMB|AOAB|JBL|HBL|JS" -- skills ':!skills/temenos-dev/references/table-schema' ':!skills/temenos-dev/references/classes'`
Expected: no output.
Run: `git grep -c "OFS.GLOBUS.MANAGER" -- skills | wc -l`
Expected: same count as before the change (non-zero).

- [ ] **Step 4: Commit**

```bash
git add skills/temenos-l3/README.md skills/temenos-l3/SKILL.md skills/temenos-dev/references/apis/ofs-api.md
git commit -m "chore(skills): anonymise client names in temenos-l3; fix OFS.POST.MESSAGE to R25 4-arg signature"
```

Note: older commit *messages* in this repo mention client names (e.g. `d8755aa ... from KMB implementation files`). Rewriting history isn't worth the risk while the repo stays private. Revisit only if the repo is ever shared.

---

## What gets built where

### Temenos-Skills (private, personal use): the knowledge and the proof

| Change | Task |
|---|---|
| Field checker for generated code (legacy `R.NEW(AC.CATEGORY)` and componentised `AC.AccountOpening.Account.Category`) | 2 |
| Compile check against `C:\R25` (`tCompile` for jBC, `javac` for L3 Java), with an R25 write guard | 3 |
| `verify_artefact.py` — one PASS/FAIL gate for any generated file | 4 |
| Golden cases + `run_golden.py`, starting with an L3 hook and a jBC VVR; fix `temenos-jbc` `getRNew`/`setE` template to whatever compiles | 5 |
| Skills and `CLAUDE.md` require the gate before code is shown | 6 |
| Export `fields.json` / `descriptions.json` / `manifest.json` (stays in `build/`, never committed to T24Tools) | 7 |
| Gated release command (golden cases must pass before export) | 8 |
| Anonymise client names in `temenos-l3`; fix `OFS.POST.MESSAGE` signature | 9 |
| Phase 2 (own plan): golden cases + skill fixes for VIR, NoFile, `.tut`, ServiceLifecycle, ActivityLifecycle, PaymentLifecycle, AA Calculation; P5 TDD step | — |

### T24Tools (public): self-authored tools only

| Change | Status |
|---|---|
| Legacy templates anonymised (generic sample names, no GLOBUS stamps) | **Done** — branch `chore/generic-sample-names`, not pushed |
| Footer + README disclaimer: "Independent project, not affiliated with or endorsed by Temenos. Temenos, T24 and Transact are trademarks of Temenos AG." | Phase 4 plan |
| **"Load knowledge file"**: file picker for a user-supplied `fields.json` (+ optional `descriptions.json`), validated against `manifest.json` `schemaVersion`, kept in IndexedDB, never uploaded. Without it, the tool works exactly as today. | Phase 4 plan |
| `getApp(name)` / `listApps()` — one lookup module over the built-in sample catalog *or* the loaded file; every caller goes through it | Phase 4 plan |
| Routine Creator uses loaded data: application search across all apps, verified field positions, mandatory/type hints, description tooltips | Phase 4 plan |
| New deterministic generators, one artefact type at a time (VVR, VIR, NoFile, L3 RecordLifecycle hook, jBC component + `.b`, `.tut` test), each matching a golden case from Temenos-Skills | Phase 4 plan |
| JS port of `check_fields`, used to validate any generated or pasted code against the loaded file | Phase 4 plan |
| Optional AI mode (off by default, user's own API key): sends only the requirement, the selected fields and the matching skill text; output must pass the JS field check before it is shown | Phase 4 plan, last |

## After this plan

1. **Phase 2 plan** (Temenos-Skills): one golden case per artefact type still missing — VIR, NoFile enquiry, `.tut` unit test, ServiceLifecycle, ActivityLifecycle, PaymentLifecycle, AA Calculation, `OFS.POST.MESSAGE` — each fixing the owning skill until it compiles.
2. **Phase 4 plan** (written in the T24Tools repo) covering the T24Tools rows above, built against the Task 7 export contract and Decisions 5–6.
