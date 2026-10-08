# Temenos T24 Development — Project Context

This file is read automatically by Claude Code at the start of every session.
It encodes all architectural decisions made during the design phase so you never
have to re-explain the project structure.

---

## What this project is

A Temenos T24/Transact customisation skill system for Claude Code. The goal is
to analyse business requirements, look up real T24 table schemas and Java APIs,
then generate correct, compilable code in Infobasic (jBASE BASIC) and Java.

**The single most important rule:** never invent a T24 field name. Every field
used in generated code must be verified against `skills/temenos-dev/references/table-schema/`
before the code is emitted. If the field is not in that file, halt and ask.

---

## Repository layout

```
project-root/
├── CLAUDE.md                          ← you are here (read every session)
├── CLI.md                             ← t24skills guide (also the help page's "Command line" section)
├── t24skills.cmd / t24skills          ← launchers for pipeline/t24skills.py
├── pipeline/
│   ├── t24skills.py                   ← one CLI: status, fields, rules, topics, samples, sample, template, generate,
│   │                                     verify, golden, diff, stages, run <stage>; --json = machine contract
│   ├── extract.py                     ← Phase 1: extract classes from 2,050 JARs
│   ├── aggregate.py                   ← Phase 2: generate reference .md files
│   ├── insert_parse.py                ← Phase 1b: extract table schemas from INSERTS/I_F.* in the JARs
│   ├── html_parse.py                  ← Phase 1c: enrich fields with type/mandatory/description from 35,235 HTML files
│   ├── pdf_extract.py                 ← Phase 1d: chunk + TF-IDF embed PDFs into Chroma (docs/, 3,481 files)
│   ├── query_docs.py                  ← Query Layer B: semantic search over PDF business rules (CLI)
│   └── validate_fields.py             ← Field Verification Gate: mechanical field-name check (Layer A)
├── mcp_server/
│   └── server.py                      ← Optional MCP server: lookup_fields(app), search_rules(query)
├── cache/                             ← SHA-256 incremental cache (git-ignored, ~620 MB)
├── jar/                               ← 2,050 T24 JAR files (not in repo)
├── T24.javadoc/                       ← 35,235 HTML JavaDoc files (not in repo)
├── docs/                              ← Temenos PDF documentation files (not in repo)
│   ├── <business-topic folders>       ← original training archive (AA, ACCOUNT, DE, OFS, ...)
│   ├── TAFJ-Admin/                    ← 28 install/runtime PDFs, sourced from a real installed
│   ├── TAFJ-Migration/                ← R25 Model Bank (C:\R25\TAFJ\doc) on 2026-07-31 — see
│   ├── TAFJ-Integration/              ← plan/state/r25-scan-report.md for the full recon.
│   ├── TAFJ-DevSecOps/                ←
│   └── T24-Componentisation/          ←
└── skills/
    ├── temenos-dev/                       ← Entry-point skill (routes to sub-skills)
    │   ├── SKILL.md
    │   └── references/
    │       ├── table-schema/          ← ONE .md per T24 application (ACCOUNT.md, etc.)
    │       ├── classes/class-index.md ← 77,762 classes from JAR extraction
    │       ├── packages/              ← $USING declarations
    │       ├── apis/java-api.md       ← Method signatures for 157 public-api classes
    │       ├── hooks/                 ← lifecycle, validation, event hooks
    │       ├── architecture/          ← application-map, dependency-graph
    │       └── relationships/
    ├── temenos-infobasic/  ← Sub-skill: VVR, VIR, VAR, VCRR, NoFile, DE
    ├── temenos-l3/         ← Sub-skill: RecordLifecycle, Java hooks
    ├── temenos-jbc/        ← Sub-skill: jBC component authoring
    ├── temenos-de/         ← Sub-skill: Delivery Engine pipeline
    ├── temenos-admin/      ← Install, runtime config, DB/app-server admin, TemnMonitor, TemnXACML
    ├── temenos-migration/  ← TAFJ patching (Patch.xml), RELEASE manifests, version upgrade, ChangeSet installs
    ├── temenos-integration/ ← ESB/non-ESB payment packages, service extensions, Email/SMS/MQ/JMS integration
    ├── temenos-devsecops/  ← Precompiler/debugger/unit-test/Maven/SonarQube tooling, Rules Engine, multi-tenant, Keycloak/Kerberos
    └── temenos-architect/  ← Componentisation architecture, package/routine naming-convention structure
```

---

## Knowledge base: three layers

### Layer A — exact lookup (always available)
- Location: `skills/temenos-dev/references/table-schema/<APP>.md` (4,596 files) and `temenos_knowledge.db` (table `fields`, 162,842 rows)
- Contents today: field name + file position + Java alias per application (ground-truth from `INSERTS/I_F.<APP>` inside the JARs), plus type/mandatory/description for 96,159 rows (59%) backfilled from JavaDoc HTML by `html_parse.py`
- Coverage gap: the remaining 41% have no type/mandatory/description — mostly MV fields with no no-arg getter, or apps with no `Record.html`. A blank in those columns means "not captured," never treat it as "optional." MV/SV flag lives separately in `com/temenos/t24/api/records/<app>/` — cross-check per the MV-field-detection rule in `skills/temenos-dev/SKILL.md`, don't assume it from this file
- Use for: validation gate before code generation, field name verification
- **Release: the JARs in `jar/` are R23** (`META-INF/MANIFEST.MF`: `R23_AMR.0`, built 2023-05-22), so `fields`, `component_fields` and `table-schema/` describe **R23**. The compile gate uses the R25 install at `C:\R25` (`R25_AMR.0`). Found 2026-10-02.
- **Per-release knowledge (R23 + R25).** Each release has its own *complete* DB — never a delta (`plan/2026-10-02-releases-and-artefact-generator.md` Decision 8): R23 = `temenos_knowledge.db` (default), R25 = `releases/R25/temenos_knowledge.db` (4,838 apps / 171,858 fields / 69,119 jBC names), built read-only from `C:\R25` by `pipeline/build_release.py`. Pass `--release R25` to `validate_fields.py`, `verify_artefact.py`, `run_golden.py`; without it they use R23. What changed R23→R25 (245 apps added, 1,740 jBC names renamed, …): `build/releases/R23-to-R25.md` from `pipeline/release_diff.py`. The skills' `table-schema/*.md` stays R23.
- Componentised (jBC) names: table `component_fields` (62,238 fields / 1,815 apps for R23), built by `pipeline/component_parse.py` from the `public static int _<Record>_<Field> = <position>` constants in each `component_<Mod>_<Name>_<n>_cl.class`, joined to `fields` on (app, position) and kept only when the name spells the EQU name. `validate_fields.py` prints them.
- Generated by: `pipeline/insert_parse.py` from `INSERTS/I_F.*` in the JARs (regenerate after any JAR set change: `python pipeline/insert_parse.py --jars jar --db temenos_knowledge.db --out skills/temenos-dev/references/table-schema`)

### Layer B — semantic search (on-demand, LIVE)
- Location: local Chroma vector DB at `vectordb/` (collection `t24_docs`, 32,657 chunks in 54 topics) + `vectordb/tfidf_vectorizer.joblib`
- Topics: a chunk's `topic` is the top-level `docs/` folder (or the PDF name for a file directly in `docs/`), never a T24 application (there is no `CUSTOMER` topic; the CUSTOMER user guide is under `Temenos_Applications`). List them with `t24skills topics` (reads `vectordb/chroma.sqlite3` read-only, ~1 s). `t24skills rules --topic` accepts any case and exits 2 with suggestions for an unknown topic; `query_docs.py --topic` is still exact and silently returns nothing for an unknown one.
- Contents: 3,481 T24 PDFs (4 corrupt/unreadable source files skipped) copied from a personal training/doc archive into `docs/` (topic-per-folder: AA, ACCOUNT, DE, OFS, TPH, Payments, Microbanking, Treasury, ...), chunked per-page (~1200 chars, 150 overlap). Duplicate files (same content copied under multiple topic folders in the source archive) are deduped by SHA-256 before embedding. Plus 53 official Temenos install/admin/migration/integration/devsecops/componentisation PDFs added 2026-07-31 from a real installed R25 Model Bank's `TAFJ_HOME/doc` (`C:\R25`, read-only source — see P6 in Next tasks), under topic folders `TAFJ-Admin`, `TAFJ-Migration`, `TAFJ-Integration`, `TAFJ-DevSecOps`, `T24-Componentisation`.
- Embedding: TF-IDF (scikit-learn), not a downloaded transformer model — this sandbox has no reliable outbound access to huggingface.co (persistent 429s from sentence-transformers and Chroma's `DefaultEmbeddingFunction` alike), so embeddings are fit locally with zero network dependency. Weaker semantic recall than a dense transformer embedding, fine for T24's exact-terminology-heavy business rules; revisit if a model becomes reachable.
- Use for: "what controls dormancy in ACCOUNT?", "what triggers ACCOUNT.OFFICER validation?" — query via `python pipeline/query_docs.py "<question>" [--topic ACCOUNT] [-n 5]`
- Generated by: `pipeline/pdf_extract.py --pdfs docs --vectordb vectordb --cache cache/pdf_extracts` (two phases: pdfplumber extraction cached by SHA-256 in `cache/pdf_extracts/`, then a full TF-IDF refit + Chroma rebuild — the embed phase always rebuilds from all cached chunks since TF-IDF's vocabulary must reflect the whole corpus, not just changed files)

### Layer C — skill context (loaded at generation time)
- Location: `skills/*/references/*.md`
- Contents: routine templates, coding standards, hook patterns, API examples
- Use for: code generation templates, naming conventions, error handling patterns

---

## Code generation workflow (mandatory — do not skip steps)

### Step 1 — classify the requirement
Identify: target T24 application(s), operation type, artefact type.

| Operation | Artefact |
|-----------|----------|
| Read and return T24 data | VIR / NoFile Enquiry / GET_API |
| Create or amend via OFS | VVR / OFS routine / WRITE_API |
| Validate field on commit | VAR / VCRR / VALIDATION hook |
| Fire on lifecycle event | RecordLifecycle / ActivityLifecycle |
| AA property calculation | AA Calculation / AA Check / AA Getter |
| Expose as REST endpoint | REST jBC component |

### Step 2 — load and verify schema (MANDATORY)
1. Load `skills/temenos-dev/references/table-schema/<APP>.md` for every target application
2. List every field the code will read or write
3. Verify each field name exists exactly in the schema file
4. **If any field is missing: HALT. Ask the developer for the correct field name. Never guess.**

### Step 3 — route to sub-skill
| Context detected | Sub-skill to activate |
|------------------|-----------------------|
| VVR, VIR, VAR, VCRR, GOSUB, Infobasic | `temenos-infobasic` |
| RecordLifecycle, validateRecord, Java hook | `temenos-l3` |
| jBC, .component, $PACKAGE | `temenos-jbc` |
| DE, ApplicationHandoff, Array.5 | `temenos-de` |

### Step 4 — generate complete, compilable code
- Include all mandatory headers (ValidationCode block)
- Include all $PACKAGE / $USING declarations
- Include complete GOSUB structure with region markers
- Include error handling (STORE.END.ERROR / setE / V$ERROR)
- Include return statement matching artefact type

### Step 5 — validation checklist (before presenting output)
- [ ] Every field name verified against table-schema reference
- [ ] $PACKAGE and $USING declarations correct
- [ ] Error handling present
- [ ] File header present with ValidationCode block
- [ ] Return type matches artefact type (FUNCTION vs SUBROUTINE)
- [ ] `python pipeline/verify_artefact.py --file <path> --app <APP>` returns PASS (or COMPILE: SKIPPED is stated to the developer)

---

## Patterns stolen from agentic-studio (apply these)

**Validation gate:** Before any code, explicitly state which fields you will use
and confirm they exist in the schema. Output: "Using fields: X, Y, Z — all
verified in ACCOUNT.md" before the code block.

**TDD-first:** For complex routines, generate the test stub first (EQUATE-based
assertions in Infobasic, or JUnit class for Java), get developer confirmation
that the test captures the requirement, then generate the full implementation.

**State persistence for multi-routine tasks:** When generating 3+ routines for
one requirement, write a `plan/state/task-state.json` file so the session can
resume if interrupted. Format:
```json
{
  "requirement": "...",
  "routines": [
    {"name": "CUST-VVR-001", "status": "done", "file": "src/CUST-VVR-001.b"},
    {"name": "CUST-VIR-001", "status": "in_progress"},
    {"name": "CUST-VAR-001", "status": "pending"}
  ]
}
```

---

## Running the extraction pipeline

Shortcut: `t24skills` (`t24skills.cmd` / `./t24skills` / `python pipeline/t24skills.py`) wraps the
commands below: `t24skills stages` lists them in execution order and `t24skills run <stage>` runs one.
Other programs call it with `--json` (one JSON object, `schemaVersion` 1; exit 0 ok / 1 check failed /
2 cannot run). Temenos-Engineering-Platform and CI should use it, not import pipeline modules.
It also has `fields APP --check` (the Field Verification Gate), `topics`, `samples` / `sample` (the 59
golden cases), `template` / `generate` (render a proven template with your own inputs + field check;
one field per field input) and `verify --no-app` (a new local table). Every command with examples: `CLI.md`.

```bash
# Install dependencies
pip install javatools pdfplumber beautifulsoup4 lxml chromadb scikit-learn joblib mcp

# Phase 1a — extract from JARs (~90 min first run, ~2 min incremental)
python pipeline/extract.py \
  --jars jar \
  --cache cache \
  --workers 8

# Phase 1b — extract table schemas from JAR INSERTS/I_F.* (DONE — rerun after JAR set changes)
python pipeline/insert_parse.py \
  --jars jar \
  --db temenos_knowledge.db \
  --out skills/temenos-dev/references/table-schema

# Phase 1c — enrich fields with type/mandatory/description from HTML JavaDoc (DONE — rerun after JAR/HTML set changes)
python pipeline/html_parse.py \
  --html T24.javadoc/T24.javadoc \
  --db temenos_knowledge.db \
  --out skills/temenos-dev/references/table-schema

# Phase 1d — extract business rules from PDFs (DONE — rerun after docs/ changes)
python pipeline/pdf_extract.py \
  --pdfs docs \
  --vectordb vectordb \
  --cache cache/pdf_extracts

# Query Layer B (semantic search over PDF business rules)
python pipeline/query_docs.py "what controls dormancy in ACCOUNT?" --topic ACCOUNT -n 5

# Field Verification Gate — mechanical check, run before emitting code (P1)
python pipeline/validate_fields.py --app ACCOUNT --fields "AC.CUSTOMER,AC.CATEGORY"

# Accuracy gate (P7) — field check + compile against C:\R25 (read-only; writes only to build/verify/)
python pipeline/verify_artefact.py --file out/V.CUS.CHECK.b --app CUSTOMER
python pipeline/run_golden.py          # every golden case in tests/golden must PASS
# Compile install: C:\R25 by default; else the first of E:\Temenos (R23) ... that exists. Choose with
# --install PATH (run_golden / verify_artefact / release_t24tools) or $T24_INSTALL. See decisions.md.
python -m pytest tests/pipeline -q     # harness unit tests (pip install -r requirements-dev.txt)

# T24Tools export (P7) -- written to build/t24tools/<release>/ only if every golden case passes.
# Published with T24Tools (docs/t24tools/<R>/: fields.json, classes.json, manifest.json), loadable in-tool; no download link in the T24Tools header.
python pipeline/release_t24tools.py --release R23

# Class -> JAR index (classes.json) for the T24Tools JAR Viewer; release_t24tools.py runs it after fields.json.
# R23 from the extract.py cache; R25 straight from C:\R25 JAR headers (bnk/t24lib + the TAFJ*/Temn* JARs in
# TAFJ/lib, type "tafj", which hold the T24 classes' superclasses) + build/releases/R25 and TAFJClient JavaDoc
# (read-only). No R23 TAFJ is available, so R23 has no tafj classes.
python pipeline/class_export.py --release R23

# Componentised (jBC) field names -- from component_*_cl.class in the JARs into table component_fields
python pipeline/component_parse.py --jars jar --release R23

# Single- vs multi-value flag per field (record-class getters) into table field_kinds
python pipeline/record_parse.py --jars jar --release R23

# R25 knowledge DB, read-only from C:\R25 (copies + generates the javadoc in build/; write guard on)
python pipeline/build_release.py --release R25 --javadoc-jar "C:\R25\bnk\Transact_L3_Javadoc\T24.javadoc.jar"
python pipeline/release_diff.py --old R23 --new R25          # what changed -> build/releases/R23-to-R25.md
python pipeline/release_t24tools.py --release R25            # R25 export + templates.json

# Artefact templates (templates/<language>/<type>/): each is PROVEN when rendering its golden case's
# userInputs reproduces tests/golden/<case>/ byte-for-byte; proven-ness is computed at export, never hand-set.
# Add a type: write the golden case (must pass run_golden.py), then the template, then add it to templates/catalogue.json.

# Optional: register the MCP server (P4) for lookup_fields/search_rules as tool calls
claude mcp add t24-knowledge -- python mcp_server/server.py

# Phase 2 — generate reference .md files (~2 min)
python pipeline/aggregate.py \
  --cache cache \
  --out skills/temenos-dev/references
```

---

## Key decisions made (do not re-litigate)

1. **No vector DB for field names.** Field names are exact identifiers. Vector
   similarity search is wrong for this. SQLite + markdown for all schema lookups.

2. **Do not replace the Temenos skill with agentic-studio.** Agentic-studio is a
   general-purpose SDLC orchestrator. It has zero T24 knowledge. Keep the
   existing skill, steal patterns (validation gate, TDD-first, state persistence).

3. **JAR INSERTS first, HTML second, PDFs third.** `INSERTS/I_F.<APP>` inside the
   JARs is structured EQU data (field name + position, zero parse ambiguity) —
   built first via `insert_parse.py`. The 35,235 HTML JavaDoc files are machine-
   readable and add type/mandatory/description metadata on top — build
   `html_parse.py` next, before the PDF extraction pipeline.

4. **Three knowledge layers, not one.** Exact lookup (SQLite/markdown) for
   schemas and APIs. Vector search (Chroma) for PDF business rules. Skill context
   (markdown templates) for code generation patterns.

5. **The skill runs inside Claude Code with no API key.** No external service
   calls, no separate process required. The skill is instruction files that
   Claude reads from disk. `mcp_server/server.py` (P4) is an *optional*
   accelerator on top of this, not a replacement — everything it exposes
   (`lookup_fields`, `search_rules`) is also reachable by reading
   `table-schema/*.md` directly or running `pipeline/validate_fields.py` /
   `pipeline/query_docs.py` via Bash, so the skill still works with zero
   setup if the MCP server isn't registered.

---

## T24 coding standards (quick reference)

### Infobasic file header
```
*-----------------------------------------------------------------------------
* Program    : <ROUTINE-NAME>
* Type       : <VVR|VIR|VAR|VCRR|FUNCTION|SUBROUTINE>
* Description: <one-line description>
* Application: <T24-APPLICATION-NAME>
*
* Modification History:
* Date       | Author          | Description
* -----------|-----------------|--------------------------------------------
* YYYY-MM-DD | <developer>     | Initial version
*-----------------------------------------------------------------------------
$PACKAGE <ModulePrefix>.<RoutineType>
```

### Java hook file header
```java
package com.temenos.t24.custom.<module>;
// Implements: <InterfaceName> from <JAR-name>
// T24 Application: <APPLICATION-NAME>
// Hook type: <RecordLifecycle|ActivityLifecycle|ServiceLifecycle>
```

### Field naming (Infobasic)
- Local variables: `lv<FieldName>` (e.g. `lvAccountNo`)
- Output record fields: use exact T24 field name as variable suffix
- Error variables: `lvError`, `lvErrorCode`

---

## Next tasks (priority order)

- [x] **P0** Build `pipeline/insert_parse.py` — extract field name/position schemas from `INSERTS/I_F.*` into SQLite + `table-schema/*.md` (4,596 apps, 162,873 fields)
- [x] **P0b** Build `pipeline/html_parse.py` — enrich `fields` table with type/mandatory/description from the 35,235 HTML JavaDoc files. Matches on `java_alias` (exact key: `<ClassName>_<GetterSuffix>` from `*Record.html`, no fuzzy matching). Enriched 96,159 / 162,842 rows (59% — remainder are MV fields with no no-arg getter, or apps with no `Record.html`). Usage: `python pipeline/html_parse.py --html T24.javadoc/T24.javadoc --db temenos_knowledge.db --out skills/temenos-dev/references/table-schema` (no `--cache` flag — a single run over 5,973 Record.html files is fast enough not to need one).
- [x] **P1** Add validation gate to `skills/temenos-dev/SKILL.md` — halt if field not in schema. Done: "Field Verification Gate" section (`skills/temenos-dev/SKILL.md`, right after Reference Files) — load `table-schema/<APP>.md`, verify every field, HALT and ask if missing, state verified fields before the code block. Verification is mechanical, not eyeballed: `python pipeline/validate_fields.py --app <APP> --fields "F1,F2"` — exit 0/1, lists missing fields by name.
- [x] **P2** Generate `skills/temenos-dev/references/table-schema/` — done by `insert_parse.py`, re-enriched by `html_parse.py`
- [x] **P3** Build `pipeline/pdf_extract.py` — chunk PDFs and embed into Chroma (TF-IDF, offline — see Layer B above). 3,481 PDFs sourced from a personal T24 training archive (`E:\Learning`), copied into `docs/`, 30,476 chunks embedded. Query via `pipeline/query_docs.py`.
- [x] **P4** Build MCP server exposing `lookup_fields(app)` and `search_rules(query)` tools — `mcp_server/server.py` (FastMCP, stdio transport). Optional accelerator, not a dependency: the skill works without it via `table-schema/*.md` + `pipeline/query_docs.py`/`validate_fields.py`. Register with `claude mcp add t24-knowledge -- python mcp_server/server.py`.
- [ ] **P5** Add TDD-first step to `skills/temenos-infobasic/SKILL.md`
- [x] **P6** Scan a real installed R25 Model Bank (`C:\R25`, external/read-only —
  never modify it, only read) and build five new skills from what was actually
  found there (not invented): `temenos-admin`, `temenos-migration`,
  `temenos-integration`, `temenos-devsecops`, `temenos-architect`. Recon report
  at `plan/state/r25-scan-report.md`. New PDFs (53 official Temenos docs from
  `TAFJ_HOME/doc`) copied into `docs/TAFJ-Admin/`, `docs/TAFJ-Migration/`,
  `docs/TAFJ-Integration/`, `docs/TAFJ-DevSecOps/`, `docs/T24-Componentisation/`
  and embedded into the existing Layer B vectordb via
  `pipeline/pdf_extract.py` (adds to, does not replace, the original corpus).
  Excluded from indexing as noted in the scan report: `bnk/UD` (live runtime
  data), `bnk/t24lib` (650MB compiled JARs, redundant with `jar/`),
  `3rdParty/Database/MBR25.bak` (8.7GB DB backup binary), `jboss-eap-8.1` and
  `DesignStudioT24` internals (third-party/IDE, not T24 knowledge).
- [ ] **P7** Accuracy harness + T24Tools export — `plan/2026-10-02-accuracy-harness-and-t24tools-export.md`.
  Gate: `pipeline/verify_artefact.py` (field check + R25 compile), golden cases in
  `tests/golden/`. Write-free tCompile setup and output format: `plan/state/decisions.md`.
- [ ] **P8** Multi-release knowledge + T24Tools Artefact Generator — `plan/2026-10-02-releases-and-artefact-generator.md`.
  Part A (Temenos-Skills) done 2026-10-02: R25 DB, release diff, proven templates, templates.json. Part B (T24Tools) pending.
  2026-10-06: 59 artefact types (19 Infobasic, 16 jBC, 24 Java), every golden case PASSes on R25 (`run_golden.py --release R25`);
  no case is `"compiled": false`. Local tables come in two styles: `infobasic/local-table` (TAFJ `I_Table`) and
  `jbc/local-table` (componentised `EB.Template`). Details: `plan/state/decisions.md`.
- [x] **P9** Command line `t24skills` (2026-10-08) — `pipeline/t24skills.py`, launchers `t24skills.cmd` / `t24skills`,
  guide `CLI.md`. `--json` is the contract for other programs (`schemaVersion` 1). Catalogue types carry a
  `group` (T24Tools' step-3 groups); the help page shows templates by group, pipeline tools in execution order,
  and generated CLI pages (stages, `rules` topics, all 62 samples with their commands). Details:
  `plan/state/decisions.md` "Command line".
- [ ] **P10** Temenos-Engineering-Platform: switch `src/adapters/temenos-skills.js` from inline Python to
  `python pipeline/t24skills.py <cmd> --json` (parse stdout on exit 1, reject only exit 2; keys are
  `field`/`javaAlias`). Fixes its `compareReleases` (ImportError) and `searchRules` (float.strip) calls.
