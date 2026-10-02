# Multi-release Knowledge + T24Tools Artefact Generator — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** T24Tools gets a new **Artefact Generator** tool that asks *release → language → routine type*, loads the matching template, takes the developer's inputs, and generates source code checked against that release's real field list — using knowledge built by Temenos-Skills for **R23 and R25**.

**Architecture:** Temenos-Skills builds one knowledge DB per release (`releases/<R>/temenos_knowledge.db`) from that release's JARs, and exports (a) per-release `fields.json` — Temenos-derived, loaded by the user from disk, never published — and (b) `templates.json` — the user's own templates, each proven by rendering it with a golden case's inputs and requiring the output to be byte-identical to that golden file, which compiles against R25. T24Tools bundles `templates.json`, stores loaded knowledge files in IndexedDB, and renders templates in the browser.

**Tech Stack:** Python 3.13 + pytest + SQLite (Temenos-Skills); React 19 + Vite + Vitest + Playwright (T24Tools, Node 22+).

**Spec:** Decisions agreed 2026-10-02 (below) + `plan/state/decisions.md` + `plan/2026-10-02-accuracy-harness-and-t24tools-export.md` (Decisions 1–6).

## Decisions (agreed 2026-10-02 — do not re-litigate)

1. **Releases: R23 + R25.** R23 from `jar/` (as today). R25 built **read-only** from `C:\R25\bnk\t24lib` (JARs) and `C:\R25\bnk\Transact_L3_Javadoc\T24.javadoc.jar` (unzipped into `build/`, never into `C:\R25`).
2. **Flow:** release → language (Infobasic / jBC / Java) → routine type → inputs → generate. Field pickers only offer fields of the chosen release; jBC uses the componentised name automatically.
3. **Unproven types are shown disabled** ("coming soon"). A type is enabled only when its template is proven (Decision 6).
4. **New separate tool** tab `Artefact Generator` (`?tool=artefact`). The Routine Creator is not changed.
5. **Templates are bundled** in T24Tools (they are the user's own writing). **Field data is never bundled** — the user loads `fields.json` per release from disk.
6. **A template is "proven"** when rendering it with its golden case's `inputs` produces the golden reference file byte-for-byte (`tests/golden/<case>/`), and that golden file passes `run_golden.py` (fields verified + compiles against R25).
7. **R25 table-schema markdown is not committed** to the skills in this plan (4,596 more files). The R25 DB is queryable via `--release R25`; the skill markdown stays R23. Revisit later.
8. **Each release is stored complete, not as a delta over R23** (user asked 2026-10-02; agreed after discussion). Reason: a delta needs merge logic in every consumer (field check, validate_fields, export, T24Tools) and silently returns the R23 answer for anything removed, renamed or moved in R25 — the exact error class the harness exists to catch. Size is not a constraint (~2.4 MB gzip per release). The "what changed" view is a **generated report** (`release_diff.py`, Task A2 Step 7). When no release is given, tools default to **R23** (the current DB) and say so.

## Global Constraints

- `C:\R25` is read-only. Read JARs/javadoc from it; write only under `build/` and `releases/`. Compile only via `pipeline/compile_check.py`.
- Never invent a field, component, class or method — templates use only names verified for the chosen release.
- Python: `PY=/c/Users/asus/AppData/Local/Programs/Python/Python313/python.exe`. T24Tools: `npm run check` must pass before every T24Tools commit.
- T24Tools is public: no Temenos-derived data (fields, descriptions, PDF text) in its repo; generic `SAMPLE.*`/`TEST.*` names; footer disclaimer "Independent project, not affiliated with or endorsed by Temenos. Temenos, T24 and Transact are trademarks of Temenos AG."
- Commits end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Review Focus

1. **Knowledge file from a different release than selected** (R23 file loaded, user picks R25) — expected: R25 is offered only if an R25 file is loaded; the generator never mixes releases.
2. **Field with no componentised name in jBC** (38% coverage in R23) — expected: field is listed but disabled for jBC with "no jBC name in <release>", never rendered with a guessed name.
3. **Corrupt / wrong-schema file loaded** (old schemaVersion 1, random JSON) — expected: a clear rejection message, nothing stored.
4. **Template placeholder left unfilled** — expected: generation refuses (lists the missing inputs); output never contains `{{`.
5. **Storage blocked** (private mode, IndexedDB unavailable) — expected: the loaded file still works for the session, with a notice that it won't be remembered.

---

## Part A — Temenos-Skills

### File Structure (Part A)

| File | Responsibility |
|---|---|
| `pipeline/releases.py` | Release registry: `db_path(release)`, `RELEASES` (`R23` → `jar/`, `R25` → `C:\R25\bnk\t24lib`). |
| `pipeline/build_release.py` | Builds one release DB end-to-end (insert_parse → html_parse → component_parse) into `releases/<R>/`. |
| `templates/<language>/<type>/template.json` + source files | The user's templates with `{{PLACEHOLDER}}`s. |
| `pipeline/templates.py` | Load, render and prove templates; export `templates.json`. |
| `pipeline/validate_fields.py`, `verify_artefact.py`, `run_golden.py`, `export_t24tools.py`, `release_t24tools.py` | Gain `--release`, resolved through `releases.py`. |

### Task A1: Release registry and `--release` everywhere

**Files:** Create `pipeline/releases.py`, `tests/pipeline/test_releases.py`; Modify `pipeline/validate_fields.py`, `pipeline/verify_artefact.py`, `pipeline/run_golden.py`, `pipeline/release_t24tools.py`, `.gitignore`.

**Interfaces — Produces:**
- `RELEASES: dict[str, Path]` — `{"R23": Path("jar"), "R25": Path(r"C:\R25\bnk\t24lib")}`
- `db_path(release: str) -> Path` — `R23` → `temenos_knowledge.db` (existing file, unchanged location); any other → `releases/<release>/temenos_knowledge.db`; unknown release → `ValueError` listing known ones.
- CLI flag `--release` (default `R23`) on `validate_fields.py`, `verify_artefact.py`, `run_golden.py`; `--db` still overrides.

- [ ] **Step 1: Failing tests**

```python
import pytest

from releases import RELEASES, db_path


def test_r23_keeps_the_existing_db_location():
    assert str(db_path("R23")) == "temenos_knowledge.db"


def test_other_releases_live_under_releases_dir():
    assert db_path("R25").as_posix() == "releases/R25/temenos_knowledge.db"


def test_unknown_release_is_an_error():
    with pytest.raises(ValueError, match="R23"):
        db_path("R99")


def test_registry_points_r25_at_the_installed_model_bank():
    assert RELEASES["R25"].as_posix().endswith("R25/bnk/t24lib")
```

- [ ] **Step 2:** Run `"$PY" -m pytest tests/pipeline/test_releases.py -q` → FAIL (`No module named 'releases'`).
- [ ] **Step 3: Implement**

```python
#!/usr/bin/env python3
"""Knowledge is built per T24 release. jar/ is R23 (MANIFEST R23_AMR.0); the
installed Model Bank C:\\R25 is R25 (read-only). See plan/state/decisions.md."""
from pathlib import Path

RELEASES = {
    "R23": Path("jar"),
    "R25": Path(r"C:\R25\bnk\t24lib"),
}


def db_path(release):
    if release not in RELEASES:
        raise ValueError(f"unknown release '{release}' -- known: {', '.join(sorted(RELEASES))}")
    if release == "R23":
        return Path("temenos_knowledge.db")
    return Path("releases") / release / "temenos_knowledge.db"
```

- [ ] **Step 4:** In each of `validate_fields.py`, `verify_artefact.py`, `run_golden.py`: add `ap.add_argument("--release", default="R23")`, change `--db` default to `None`, and resolve `db = args.db or str(db_path(args.release))`. Add a CLI test per script in its existing test file using `--db` (as `test_validate_fields.py` does). Add `releases/` to `.gitignore` under "Harness / export output".
- [ ] **Step 5:** `"$PY" -m pytest tests/pipeline -q` → all pass; `"$PY" pipeline/run_golden.py` → 2 PASS.
- [ ] **Step 6:** Commit `feat(releases): release registry; --release on validate/verify/golden`.

### Task A2: Build the R25 knowledge DB (read-only from `C:\R25`)

**Files:** Create `pipeline/build_release.py`, `tests/pipeline/test_build_release.py`.

**Interfaces — Consumes:** `RELEASES`, `db_path` (A1); `insert_parse.py` CLI (`--jars --db --out`); `html_parse.py` CLI (`--html --db --out`); `component_parse.build_component_fields`.
**Produces:** `build_release.py --release R25 [--javadoc-jar PATH]` → `releases/R25/temenos_knowledge.db` with tables `fields`, `component_fields`; markdown to `build/releases/R25/table-schema/` (scratch, Decision 7).

- [ ] **Step 1: Failing test** — `plan_steps("R25", javadoc_jar=Path("x.jar"))` returns the exact command list, and every output path is under `releases/` or `build/` (never `C:\R25`):

```python
from pathlib import Path

from build_release import plan_steps


def test_r25_build_writes_only_to_releases_and_build():
    steps = plan_steps("R25", javadoc_jar=Path(r"C:\R25\bnk\Transact_L3_Javadoc\T24.javadoc.jar"))
    names = [s.name for s in steps]
    assert names == ["unzip-javadoc", "insert_parse", "html_parse", "component_parse"]
    for step in steps:
        for out in step.writes:
            assert out.parts[0] in ("releases", "build"), (step.name, out)


def test_r23_rebuild_is_refused():
    import pytest
    with pytest.raises(ValueError, match="R23"):
        plan_steps("R23", javadoc_jar=None)
```

- [ ] **Step 2:** Run → FAIL.
- [ ] **Step 3: Implement** `Step = namedtuple("Step", "name cmd writes")`; `plan_steps(release, javadoc_jar)` builds: unzip `javadoc_jar` → `build/releases/<R>/javadoc/`; `insert_parse.py --jars RELEASES[R] --db db_path(R) --out build/releases/<R>/table-schema`; `html_parse.py --html build/releases/<R>/javadoc/<root containing *Record.html> --db … --out build/releases/<R>/table-schema`; `component_parse.py --jars RELEASES[R] --db … --release R`. `main()` runs them in order, `db_path(R).parent.mkdir(parents=True)`, deletes an existing `db_path(R)` first, and refuses `R23` (it is built by the original commands in CLAUDE.md). Wrap the run in the R25 write guard: take a marker before, call `compile_check.r25_writes_since(marker)` after, exit 1 if non-empty.
- [ ] **Step 4:** `"$PY" -m pytest tests/pipeline -q` → pass.
- [ ] **Step 5: Real build** — `"$PY" pipeline/build_release.py --release R25 --javadoc-jar "C:\R25\bnk\Transact_L3_Javadoc\T24.javadoc.jar"`. Expected: prints row counts for `fields` and `component_fields`, R25 write guard clean. Check: `"$PY" pipeline/validate_fields.py --release R25 --app CUSTOMER --fields "EB.CUS.MNEMONIC"` → VERIFIED with `jBC ST.Customer.Customer.EbCusMnemonic`. Record R23-vs-R25 counts (apps, fields, component fields) in `plan/state/decisions.md`.
- [ ] **Step 6:** `"$PY" pipeline/run_golden.py --release R25` → 2 PASS (golden cases now field-checked against **R25**, matching the R25 compile).
- [ ] **Step 7: R23 → R25 change report.** Create `pipeline/release_diff.py` (+ `tests/pipeline/test_release_diff.py`, failing first) with `diff_releases(old_conn, new_conn) -> dict` returning, per app: `apps_added`, `apps_removed`, and for common apps `fields_added`, `fields_removed`, `fields_moved` (same name, different position), `jbc_renamed` (same EQU field, different componentised name). Tests use two in-memory fixture DBs covering each category. CLI: `release_diff.py --old R23 --new R25 --out build/releases/R23-to-R25.md` writes a readable Markdown report (summary counts first, then per-app tables) plus `.json`. Record the summary counts in `plan/state/decisions.md`. This report is the "what changed" view; lookups always use the full DB of the selected release (Decision 8).
- [ ] **Step 8:** Commit `feat(releases): build R25 knowledge DB read-only from C:\R25; R23->R25 change report`.

### Task A3: Template format, renderer and proof

**Files:** Create `pipeline/templates.py`, `tests/pipeline/test_templates.py`, `templates/java/record-lifecycle-validate/{template.json,{{CLASS_NAME}}.java}`, `templates/jbc/validation/{template.json,{{ROUTINE_NAME}}.b,{{PACKAGE}}.component}`; Modify `tests/golden/*/case.json` (add `template` + `inputs`).

**Interfaces — Produces:**

`template.json`:
```json
{
  "id": "jbc/validation",
  "language": "jbc",
  "type": "validation",
  "label": "Validation routine (VVR)",
  "goldenCase": "jbc-customer-mnemonic-vvr",
  "inputs": [
    {"id": "PACKAGE", "label": "Package", "kind": "package", "example": "SAMPLE.Validation"},
    {"id": "ROUTINE_NAME", "label": "Routine name", "kind": "routineName", "example": "V.SAMPLE.CHECK"},
    {"id": "METHOD_NAME", "label": "Component method", "kind": "identifier", "example": "vSampleCheck"},
    {"id": "APP", "label": "Application", "kind": "app"},
    {"id": "FIELD", "label": "Field", "kind": "field", "of": "APP"},
    {"id": "ERROR_TEXT", "label": "Error message", "kind": "text", "example": "FIELD IS MANDATORY"}
  ],
  "files": ["{{ROUTINE_NAME}}.b", "{{PACKAGE}}.component"]
}
```
Field inputs render per language: `{{FIELD}}` = EQU name (Infobasic), componentised name (jBC), java getter suffix (Java, from the alias). `{{APP_COMPONENT}}` (jBC) = the component part of the field's componentised name. `{{TODAY}}` = render date `YYYY-MM-DD`.

- `load_templates(root=Path("templates")) -> list[dict]`
- `render(template: dict, values: dict[str, str]) -> dict[str, str]` (filename → content); raises `MissingInputs([...])` if any `{{X}}` remains.
- `prove(template, golden_root=Path("tests/golden")) -> bool` — renders with the golden case's `inputs` (stored in its `case.json`) and compares byte-for-byte to the golden files.

- [ ] **Step 1: Failing tests** — render fills placeholders and file names; unfilled placeholder raises `MissingInputs` naming it; `prove()` is True for both shipped templates and False after changing one character in a temp copy of a golden file.
- [ ] **Step 2:** Run → FAIL.
- [ ] **Step 3:** Write the two templates by **replacing values in the existing golden files with placeholders** (so the proof is exact), add `"template"` and `"inputs"` to each golden `case.json`, implement `templates.py` (`re.sub(r"{{([A-Z_]+)}}", ...)`, no third-party templating).
- [ ] **Step 4:** `"$PY" -m pytest tests/pipeline -q` → pass; `"$PY" pipeline/run_golden.py --release R25` → 2 PASS.
- [ ] **Step 5:** Commit `feat(templates): template format, renderer and golden-case proof`.

### Task A4: Export `templates.json` and the language/type catalogue

**Files:** Modify `pipeline/templates.py`, `pipeline/release_t24tools.py`; Test `tests/pipeline/test_templates.py`.

**Interfaces — Produces:** `export_templates(out: Path) -> dict` writes `templates.json`:
```json
{
  "schemaVersion": 1,
  "languages": [
    {"id": "infobasic", "label": "Infobasic (legacy)", "types": [
      {"id": "vvr", "label": "Validation routine (VVR)", "proven": false},
      {"id": "vir", "label": "Input routine (VIR)", "proven": false},
      {"id": "nofile", "label": "NoFile enquiry", "proven": false},
      {"id": "ofs-routine", "label": "OFS routine (OFS.POST.MESSAGE)", "proven": false}]},
    {"id": "jbc", "label": "jBC (componentised)", "types": [
      {"id": "validation", "label": "Validation routine (VVR)", "proven": true, "template": "jbc/validation"},
      {"id": "get-api", "label": "GET method", "proven": false},
      {"id": "write-api", "label": "WRITE method (OFS)", "proven": false}]},
    {"id": "java", "label": "Java (L3)", "types": [
      {"id": "record-lifecycle-validate", "label": "RecordLifecycle.validateRecord", "proven": true, "template": "java/record-lifecycle-validate"},
      {"id": "service-lifecycle", "label": "ServiceLifecycle", "proven": false},
      {"id": "enquiry", "label": "NoFile Enquiry", "proven": false}]}
  ],
  "templates": { "jbc/validation": { "...": "template.json + file sources" } }
}
```
`proven` is computed by `prove()` at export time — never hand-set. The language/type list lives in `templates/catalogue.json` (user-maintained); types without a template export `proven: false`.

- [ ] **Step 1: Failing tests** — export marks the 2 shipped templates proven; a catalogue type with no template is `proven: false`; a template whose proof fails is exported `proven: false` and the export prints a warning naming it.
- [ ] **Step 2–4:** Implement; `release_t24tools.py --release R` also writes `build/t24tools/templates.json` (release-independent). Run tests + `"$PY" pipeline/release_t24tools.py --release R23` and `--release R25`.
- [ ] **Step 5:** Commit `feat(templates): export templates.json with proven language/type catalogue`.

### Task A5: Docs

- [ ] `CLAUDE.md`: Layer A per-release section, `build_release.py` and `--release` commands, templates folder + proof rule. `skills/temenos-dev/SKILL.md`: pass `--release` to `validate_fields.py`/`verify_artefact.py` when the developer names a release (default R23; say which was used). Commit `docs: per-release knowledge and templates`.

---

## Part B — T24Tools (`D:\Personal\Projects\T24Tools`, branch `feat/artefact-generator`)

### File Structure (Part B)

| File | Responsibility |
|---|---|
| `src/data/templates.json` | Copied from Temenos-Skills `build/t24tools/templates.json` (own templates only). |
| `src/features/artefactGenerator/knowledgeStore.js` | Validate a loaded `fields.json` (schemaVersion 2), keep it in IndexedDB per release, list loaded releases. |
| `src/features/artefactGenerator/catalog.js` | `getApp(release, name)`, `listApps(release, query)`, `fieldsFor(release, app, language)`. The only module that reads field data. |
| `src/features/artefactGenerator/render.js` | Render a template with inputs (same rules as `pipeline/templates.py`), refuse unfilled placeholders. |
| `src/features/artefactGenerator/fieldCheck.js` | JS port of `check_fields` for the generated output. |
| `src/features/artefactGenerator/ArtefactGenerator.jsx` | The wizard UI. |
| `src/navigation.js`, `src/App.jsx` | Register tab `['artefact', 'Artefact Generator']`. |
| `tests/e2e/artefact.spec.js` + `tests/e2e/fixtures/knowledge-R23.sample.json` | E2E with a **synthetic** knowledge file (sample apps/fields only — no Temenos data). |

### Task B1: `render.js` parity with the Python renderer

- [ ] Failing Vitest: given `src/data/templates.json`'s `jbc/validation` and its golden `inputs` (also exported), output equals the golden source shipped in `templates.json` under `goldenOutput` (A4 must include it); missing input → throws `MissingInputs` with the ids. Implement; `npm run check`; commit.

### Task B2: `knowledgeStore.js`

- [ ] Failing Vitest (with `fake-indexeddb` dev dependency): accepts a schemaVersion-2 file and returns `{release, apps, fields}` counts; rejects schemaVersion 1 / missing `release` / non-JSON with a readable message; `listReleases()` returns loaded releases sorted; when IndexedDB throws, `load()` still returns the data and sets `persisted: false`. Implement; check; commit.

### Task B3: `catalog.js`

- [ ] Failing Vitest on a synthetic in-memory knowledge doc: `listApps('R23','cust')` matches case-insensitively and ranks prefix matches first; `fieldsFor(release, app, 'jbc')` marks fields with `comp === null` as `disabled: 'no jBC name in R23'`; `fieldsFor(…,'java')` returns getter suffix from the alias (`Customer_ShortName` → `ShortName`). Implement; check; commit.

### Task B4: `fieldCheck.js`

- [ ] Failing Vitest mirroring `tests/pipeline/test_artefact_fields.py` (legacy refs, componentised refs verified against the release's `comp` names, method calls skipped, comments ignored). Implement; check; commit.

### Task B5: Wizard UI + tab

- [ ] Steps in one screen, each enabled after the previous is answered: **1 Release** (radio list from `listReleases()`; if none: "Load a knowledge file" button + one-line explanation that the file stays in the browser), **2 Language** (from `templates.json`), **3 Routine type** (unproven types disabled with "coming soon"), **4 Inputs** (generated from the template's `inputs`; `app` = searchable picker, `field` = picker filtered by app and language), **5 Generate** → file tabs with copy/download, plus the field-check result.
- [ ] Footer disclaimer (Global Constraints) on the whole site.
- [ ] Register `['artefact', 'Artefact Generator']` in `NAV_TABS`; lazy-load like the other tools; `?tool=artefact` deep link.
- [ ] `npm run check`; commit.

### Task B6: E2E

- [ ] Playwright with the synthetic fixture: load file → pick R23 → jBC → Validation → fill inputs → output contains `EB.SystemTables.getRNew(<synthetic comp name>)` and a `.component` file; an unproven type is disabled; switching release with no file for it shows the load prompt; reloading the page keeps the loaded release (IndexedDB). `npm run test:e2e`; commit.

### Task B7: Ship

- [ ] Update `README.md` + `docs/TOOLS.md` (how to produce `fields.json` is documented only as "a knowledge file exported from your own Temenos-Skills" — no Temenos data or instructions to obtain it). `npm run check` + `npm run test:e2e`. Merge/push only on the developer's go-ahead (push to `main` redeploys the public site).

---

## After this plan

- Phase 2 (per artefact type): add a golden case + template for each disabled type; each one flips to enabled in T24Tools on the next `templates.json` export.
- Optional AI mode (BYO key) — after the deterministic generators exist.
- Optional: R25 `table-schema/` markdown for the skills (Decision 7).
