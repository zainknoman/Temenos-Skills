# Temenos Skills — T24 Development Intelligence

A Temenos T24/Transact customisation and operations skill system for Claude
Code, backed by a three-layer knowledge base built from real T24 product
JARs, JavaDoc, business-rule documentation, and a real installed R25 Model
Bank — not invented field names, guessed API signatures, or guessed config.

**At a glance**

- **11 skills** for code generation (Infobasic, jBC, L3 Java, Delivery Engine) and for operations (admin, migration, integration, devsecops, architecture, component analysis).
- **Two T24 releases**: a complete knowledge base for **R23** and for **R25** (fields, positions, types, componentised jBC names), plus a generated R23→R25 change report.
- **59 artefact types, every one proven**: 19 Infobasic, 16 jBC and 24 L3 Java hook templates. Each template's example compiles against a real R25 install and has its fields verified on both releases.
- **An accuracy check for generated code**: `pipeline/verify_artefact.py` verifies every field and compiles the file against R25 before it's presented.
- **A command line, `t24skills`**: one command for field checks, business-rule search, the 62 samples, generating code from the templates, verify/compile, the golden suite, the release diff and every pipeline stage. Every command takes `--json` for other programs. See [CLI.md](CLI.md).
- **Help page**: open [`Temenos-Skills-HelpText.html`](Temenos-Skills-HelpText.html) in a browser. It's a JavaDoc-style index of every skill, reference file, artefact template (grouped as in T24Tools), golden case, pipeline tool (in execution order) and release, with search. Its *Command line* section has the CLI guide, every `rules --topic` topic, and the commands for all 62 samples. Rebuild it with `t24skills run help` (or `python pipeline/build_help.py`).

---

## Install the Skills

Install all ten T24 skills into Claude Code — four code-generation sub-skills
plus `temenos-dev` itself, and five domain/operations skills (admin, migration,
integration, devsecops, architecture):

```
/plugin marketplace add zainknoman/Temenos-Skills
/plugin install temenos-skills@temenos-skills
```

Or browse and install from the Claude Code plugin directory:
**[claude.ai/admin-settings/directory](https://claude.ai/admin-settings/directory)** → search `temenos-skills`

Once installed, the skills activate automatically when you work on T24 artifacts. You can also invoke the entry-point skill directly:

```
/temenos-dev
```

| Scope | How |
|-------|-----|
| Current project only | Run the install commands inside that project directory |
| All projects (global) | Install from the Claude.ai admin settings directory — applies org-wide |

Skills live under `~/.claude/plugins/` after install.

---

## Component Analyzer

A dedicated `temenos-component-analyzer` skill is included for developer-facing T24
application/component dependency analysis. It covers PGM.FILE, FILE.CONTROL,
STANDARD.SELECTION, VERSION, ENQUIRY, routine source, EB.API and the R19
Job → Batch → Service → Workload execution chain.

The implementation includes an executable mainline:

```
EB.COMPONENT.ANALYZER.MAIN CUSTOMER
```

See `skills/temenos-component-analyzer/references/implementation-guide.md`
for the deployment model, release-sensitive field positions, source-analysis
limitations, and R19 multithreading checklist.

## How to Use After Install

**Auto-trigger (passive)** — skills detect context from your words, just describe what you're building:

> "Write a RecordLifecycle hook for CUSTOMER validation"
> "Create a jBC component to read ACCOUNT balance"
> "Write a VVR routine for FUNDS.TRANSFER"

Claude routes automatically:
- RecordLifecycle / ActivityLifecycle / Java hook → `temenos-l3`
- $PACKAGE / .b file / .component → `temenos-jbc`
- VVR / VIR / VAR / Infobasic → `temenos-infobasic`
- DE handoff / ApplicationHandoff → `temenos-de`

The five domain/operations skills auto-trigger the same way, on their own
description keywords — they aren't code-generation artefacts, so they sit
alongside `temenos-dev` rather than being routed through it:

> "Why does my compile fail with a tools.jar error?"
> "What directories does a TAFJ patch touch?"
> "List the ESB payment-integration packages"
> "How do I set up the JBC precompiler / remote debugger?"
> "Explain the T24 componentisation model"

- Install/runtime/config/observability → `temenos-admin`
- Patch/upgrade/ChangeSet installation → `temenos-migration`
- ESB/integration packages, MQ/JMS, Email/SMS → `temenos-integration`
- Build/test/debug tooling, security, multi-tenancy → `temenos-devsecops`
- Componentisation architecture, package/routine structure → `temenos-architect`

**Manual invoke (explicit):**

```
/temenos-dev         ← master entry point, routes to code-gen sub-skills
/temenos-infobasic   ← Infobasic/jBASE BASIC direct
/temenos-l3          ← L3 Java hooks direct
/temenos-jbc         ← jBC component workflow direct
/temenos-de          ← Delivery Engine direct
/temenos-admin       ← install, runtime config, DB/app-server admin
/temenos-migration   ← patching, version upgrade, ChangeSet installs
/temenos-integration ← ESB/non-ESB packages, service extensions, MQ/JMS
/temenos-devsecops   ← build/test/debug tooling, security, multi-tenancy
/temenos-architect   ← componentisation architecture, package structure
```

---

## Knowledge Base: Three Layers

The skill never invents a T24 field name or API signature — everything is
verified against a knowledge base built from real T24 artifacts.

| Layer | What | Built from | Query |
|-------|------|------------|-------|
| **A — exact lookup** | Field name, position, Java alias, type/mandatory/description per T24 application | `INSERTS/I_F.*` inside the JARs + JavaDoc HTML | `skills/temenos-dev/references/table-schema/<APP>.md`, or `pipeline/validate_fields.py --app ACCOUNT --fields "AC.CUSTOMER"` |
| **B — semantic search** | Business rules and module documentation ("what controls dormancy in ACCOUNT?") | T24 PDF documentation, chunked and TF-IDF embedded (fully offline, no model download) | `pipeline/query_docs.py "<question>" [--topic ACCOUNT]` |
| **C — skill context** | Routine templates, coding standards, hook patterns, API examples | Curated + JAR/JavaDoc extraction | `skills/*/references/*.md`, loaded automatically at generation time |

Layer A is the ground truth for field names — if a field isn't in
`table-schema/<APP>.md`, the skill halts and asks rather than guessing (see
[Field Verification Gate](#field-verification-gate) below).

An optional MCP server (`mcp_server/server.py`) exposes Layer A/B as
structured tool calls instead of file reads — see [MCP Server](#mcp-server-optional).

---

## Releases (R23 + R25)

Each release has its own **complete** knowledge DB. It is never stored as a delta over another release, because a delta would silently return the R23 answer for anything R25 removed, renamed or moved.

| Release | Built from (read-only) | Apps | Fields | Fields with a jBC name | DB |
|---|---|---|---|---|---|
| **R23** (default) | `jar/` (MANIFEST `R23_AMR.0`) | 4,596 | 162,842 | 62,238 | `temenos_knowledge.db` |
| **R25** | `C:\R25\bnk\t24lib` + `T24.javadoc.jar` | 4,838 | 171,858 | 69,119 | `releases/R25/temenos_knowledge.db` |

- Pass `--release R25` to `validate_fields.py`, `verify_artefact.py` and `run_golden.py`. Without it they use R23.
- `pipeline/build_release.py --release R25` builds the R25 DB. It reads from `C:\R25` and fails if anything there changes.
- `pipeline/release_diff.py --old R23 --new R25` writes `build/releases/R23-to-R25.md`: 245 apps added, 3 removed, 557 changed, 2,580 fields added, 651 removed, 177 moved and **1,740 jBC names renamed** (R25 keeps the app prefix in many local modules).
- **Componentised (jBC) field names are not Java aliases.** `EB.CUS.SHORT.NAME` is `ST.Customer.Customer.EbCusShortName`, while `AC.CATEGORY` is `AC.AccountOpening.Account.Category`. `pipeline/component_parse.py` reads them from the component classes in the JARs, and `validate_fields.py` prints them.
- **Single- vs multi-value** comes from the record classes: `<Rec>Record.get<Field>()` returning `TField` = `SV`, returning `List` = `MV`, getter only on a group class = `MV-GROUP` (`pipeline/record_parse.py`, table `field_kinds`; R23 133k / R25 143k fields classified). Java templates accept only `SV` fields; `validate_fields.py` prints `value=SV|MV|MV-GROUP`.

---

## Accuracy Harness

Generated code is checked, not eyeballed:

```bash
python pipeline/verify_artefact.py --file out/V.CUS.CHECK.b --app CUSTOMER [--release R25]
```

1. **Field check.** Legacy EQU names (`AC.CATEGORY`) and componentised names (`ST.Customer.Customer.EbCusMnemonic`) are verified against the release DB.
2. **Compile check.** jBC and Infobasic compile with R25 `tCompile` (any sibling `.component` first). L3 Java compiles with `javac` against the R25 JARs.
3. **Write guard.** Compiling writes only to `build/verify/`. Afterwards `C:\R25` is scanned, and the result is FAIL if anything there changed. The setup is described in `plan/state/decisions.md`.

`PASS` needs both checks. A skipped compile (no `C:\R25`) counts as FAIL, never as a pass.

`tests/golden/` holds one reference case per artefact type, and `python pipeline/run_golden.py --release R25` runs them all.

---

## Artefact Templates (59 types)

`templates/<language>/<type>/` holds `template.json` (inputs) and source files with `{{PLACEHOLDER}}`s. A **field** input becomes the EQU name for Infobasic, the componentised name for jBC, or the getter suffix for Java, taken from the selected release.

A template is **proven** when rendering its golden case's inputs reproduces that golden case byte-for-byte, and the golden case passes the accuracy harness. Proven status is computed when `templates.json` is exported, never set by hand.

| Language | Types |
|---|---|
| Infobasic (19) | VVR, VIR, VAR, NoFile enquiry, OFS routine, ID routine, check-record, auto-field, before-auth, after-unauth, auth routine, enquiry conversion / build, multi-threaded COB service, DE conversion, AA calculation, AA getter, batch PROGRAM, local table (TAFJ Infobasic `I_Table` style). R25 requires `$PACKAGE` and a `.component` even for `$INSERT`-style routines, so both are generated. |
| jBC (16) | Validation routine, GET method, WRITE method (OFS), NoFile enquiry, ID routine, input routine, check-record, before-auth, enquiry conversion / build, query method, DE conversion, multi-threaded COB service, package initialise, GET with a `.complex` DTO, local table (componentised `EB.Template`) |
| Java L3 hooks (24) | RecordLifecycle `checkId`, `defaultFieldValues`, `defaultFieldValuesOnHotField`, `validateRecord`, `validateField` (deprecated in R25), `updateRecord`, `updateCoreRecord`, `postUpdateRequest`, `isOverrideAutoApprove`; ServiceLifecycle; Enquiry `setIds` / `setFilterCriteria` / `setValue`; AA `ActivityLifecycle` `validateRecord` / `defaultFieldValues` / `postCoreTableUpdate` / `updateLookupTable` / `generateSecondaryActivity`; AA `Calculation` `getChargeAmount` / `calculatePayment` / `getAdjustedChargeAmount` / `getInterestCustomRate`; `PaymentLifecycle.validatePaymentForClearing`; `PaymentOrderLifecycle.validatePaymentOrderRecord` |

`python pipeline/release_t24tools.py --release R25` runs the golden cases. Only if they pass does it write the T24Tools export: `build/t24tools/<R>/` (fields, Temenos-derived, for personal use only) and `templates.json` (the templates themselves).

Each type in `templates/catalogue.json` has a `group`, the same groups the T24Tools Artefact Generator uses for its routine-type cards:

| Language | Groups |
|---|---|
| Infobasic | Version routines · Enquiry · Batch and services · Messaging and delivery · Arrangements (AA) · Tables |
| jBC | Version routines · Enquiry · Component methods · Batch and services · Messaging and delivery · Tables |
| Java | RecordLifecycle · Enquiry · Services · AA activity · AA calculation · Payments |

---

## T24Tools Artefact Generator

T24Tools (a separate repo) loads `templates.json` and a release's `fields.json`, and generates routines in the browser with no network calls. The flow has five steps:

1. **Release**: the app-wide active release (header buttons; R25 loads at start-up). The Artefact Generator, Routine Builder, JAR Viewer and Application Viewer all use it.
2. **Language**: Infobasic (legacy), jBC (componentised) or Java (L3 hooks).
3. **Routine type**: the 59 types as cards, grouped as in the table above, with a filter box. Every one is compile-verified on R25. T24Tools adds a seventh Infobasic group, **Legacy templates (Routine Builder)**: four recovered templates (Standard Routine, OFS Routine, OFS OPM Routine, F.WRITE Routine). They are not Temenos-Skills templates and have never been compiled.
4. **Inputs**: each field input is a filterable list of the application's fields, with position and `SV` / `MV` / `MV-GROUP`. Fields the language cannot use are disabled, with the reason. 38 types accept **several fields** for at least one input. For those types, only the field-specific statements repeat: a check per field, `AND`-ed selections, fields returned together, or every field written in one OFS message. The multi-field forms have not been compiled on T24.
5. **Generate**: editable code, one tab per file, with **Copy** and **Download**. A toolbar of **building blocks** (Files, Select, Strings, Dates, Local ref, Messages; 20 in all) inserts code at the cursor in the routine's language. That means legacy `CALL` for Infobasic, componentised names such as `EB.DataAccess.FRead` for jBC, and `DataAccess` / `Session` for Java. Each block is filled from the template's application and field, and its `$INSERT` / `$USING` / `import` lines are added once. The field check reruns on every edit. **Reset to template** undoes all changes.

Generation never leaves a `{{PLACEHOLDER}}` in the output. Componentised names differ between R23 and R25, so generate for the release you will deploy to.

---

## Pipeline

```
jar/                    T24.javadoc/              docs/
  (T24 product JARs)      (JavaDoc HTML)             (T24 PDF documentation)
       |                        |                          |
       v                        v                          v
  extract.py            insert_parse.py            pdf_extract.py
  (Phase 1: classes)    (Phase 1b: field schema)    (Phase 1d: chunk + embed)
       |                        |                          |
       v                        v                          v
   cache/*.json         temenos_knowledge.db          vectordb/
                          (table `fields`)          (Chroma, TF-IDF)
       |                        ^
       v                        |
  aggregate.py           html_parse.py
  (Phase 2: reference    (Phase 1c: backfill
   markdown)              type/mandatory/desc)
       |
       v
  skills/temenos-dev/references/
```

### Results

| Metric | Value |
|--------|-------|
| JARs processed | 2,050 |
| Classes extracted | 77,762 |
| T24 fields catalogued (Layer A) | 162,842, across 4,596 applications |
| Fields enriched with type/mandatory/description | 96,159 (59% — remainder are MV fields with no no-arg getter, or apps with no `Record.html`) |
| Business-rule PDFs indexed (Layer B) | 3,534 — 3,481 from the original training/doc archive (4 corrupt source files skipped) + 53 official Temenos install/admin/migration/integration/devsecops/componentisation PDFs added 2026-07-31 from a real installed R25 Model Bank's `TAFJ_HOME/doc` |
| Vector chunks embedded | 32,657, in 54 topics (`t24skills topics`) |
| Cache size | ~620 MB (incremental, SHA-256 hashed) |

`jar/`, `T24.javadoc/`, and `docs/` are not shipped in this repo (large
binaries) — supply your own T24 product JARs, JavaDoc HTML export, and PDF
documentation to regenerate the knowledge base for your release.

The 53 R25-sourced PDFs live under five new topic folders —
`docs/TAFJ-Admin/`, `docs/TAFJ-Migration/`, `docs/TAFJ-Integration/`,
`docs/TAFJ-DevSecOps/`, `docs/T24-Componentisation/` — queryable the same
way as any other topic: `pipeline/query_docs.py "<question>" --topic TAFJ-Admin`.
See `plan/state/r25-scan-report.md` for the full recon of what was and
wasn't indexed (e.g. `bnk/t24lib`'s compiled JARs and the 8.7GB
`3rdParty/Database/MBR25.bak` were deliberately excluded).

---

## The Knowledge DB

`temenos_knowledge.db` lives at the repo root — gitignored, regenerable, not committed.

Tables:
- `classes` — Java API classes: qualified name, package, jar, module
- `methods` — method name/params/return per class
- `fields` — T24 field name, position, Java alias, source jar, plus `field_type` / `mandatory` / `description` where backfilled from JavaDoc
- `*_fts` — full-text search indexes on classes/methods

### Querying

```bash
sqlite3 temenos_knowledge.db

-- all fields for an app, in position order
SELECT position, field_name, java_alias, field_type, mandatory FROM fields WHERE app='ACCOUNT' ORDER BY position;

-- does a field exist anywhere?
SELECT app, position FROM fields WHERE field_name='AC.CUSTOMER';

-- find a class
SELECT qualified, jar FROM classes WHERE simple_name='AaArrAccountRecord';

-- methods on a class
SELECT name, params_json FROM methods WHERE class_qualified LIKE '%ActivityLifecycle';

-- full-text search across class descriptions
SELECT * FROM classes_fts WHERE classes_fts MATCH 'validation';
```

```python
import sqlite3
conn = sqlite3.connect("temenos_knowledge.db")
rows = conn.execute("SELECT * FROM fields WHERE app=?", ("CUSTOMER",)).fetchall()
```

---

## Field Verification Gate

Every field the skill uses in generated code is checked mechanically, not
eyeballed:

```bash
python pipeline/validate_fields.py --app ACCOUNT --fields "AC.CUSTOMER,AC.CATEGORY"
```

Exit 0 = every field verified (prints position/alias/type/mandatory for
each). Exit 1 = at least one field not found, with the exact missing names
listed — the skill halts and asks rather than guessing.

---

## MCP Server (optional)

`mcp_server/server.py` exposes the knowledge base as two MCP tools:

- `lookup_fields(app)` — Layer A field lookup (same data as `table-schema/<APP>.md`)
- `search_rules(query, topic=None, n_results=5)` — Layer B semantic search

This is an accelerator, not a dependency — the skill works with zero setup
by reading `table-schema/*.md` and running `pipeline/query_docs.py` /
`pipeline/validate_fields.py` directly. Register it only if you want
structured tool calls instead:

```bash
claude mcp add t24-knowledge -- python mcp_server/server.py
```

---

## Skill Architecture

`temenos-dev` is the single entry point. It detects context and delegates to one of four specialist sub-skills:

| Sub-skill | Covers | Triggers |
|-----------|--------|----------|
| `temenos-l3` | L3 Java hooks: RecordLifecycle, ServiceLifecycle, ActivityLifecycle, Enquiry; Core APIs (Amount, Date, ExchangeRate, Customer, Limit, Session, AA Contract) | `L3 java`, `RecordLifecycle`, `validateRecord`, `checkId`, `com.temenos` |
| `temenos-jbc` | jBC component authoring — full 5-phase DEVELOP workflow, 8 artefact templates (GET_API, WRITE_API, ENQUIRY, VALIDATION, TEMPLATE, DE_HANDLER), Phase 5 checklist | `jBC`, `.component`, `.b file`, `metamodelVersion`, `$PACKAGE` |
| `temenos-infobasic` | Infobasic/jBASE BASIC routines: VVR, VIR, VAR, VCRR, NoFile Enquiry, AA calculation/getter/check, service routines, batch programs | `VVR`, `VIR`, `VAR`, `VCRR`, `NoFile`, `Infobasic`, `GOSUB` |
| `temenos-de` | Delivery Engine pipeline: ApplicationHandoff routines, Array.5 mapping, event mapping table, print interface carrier, document-data FUNCTIONs | `DE handoff`, `ApplicationHandoff`, `Array.5`, `DE.API` |

The `temenos-dev` skill itself handles Java API reference lookups, field
verification, semantic business-rule search, impact analysis, and
EXPLAIN/REVIEW/ANALYZE modes.

### Domain / Operations Skills (standalone, auto-triggered)

Five further skills cover installation, operations, and architecture
knowledge that isn't code generation, so they sit alongside `temenos-dev` rather
than being routed through its Step-3 artefact table. Each is grounded in a
real installed R25 Model Bank (`C:\R25`) rather than general T24 knowledge —
every config key, script name, or PDF cited in these skills traces back to a
file actually found there; see `plan/state/r25-scan-report.md` for the recon.

| Skill | Covers | Triggers | Deep-dive topic |
|-------|--------|----------|------------------|
| `temenos-admin` | TAFJ install, `tafj.properties`/runtime config, app-server (JBoss EAP/WebLogic/WebSphere Liberty), DB drivers & provisioning, TemnMonitor observability stack (Grafana/Prometheus/Jaeger/ELK/OpenTelemetry), TemnXACML entitlements, the JDK21 `tools.jar` compile-bug fix | `TAFJ install`, `tafj.properties`, `JBoss EAP`, `DB driver`, `TemnMonitor`, `XACML`, `tools.jar error` | `TAFJ-Admin` |
| `temenos-migration` | `Patch.xml` directory-scoped patch contract, `RELEASE` manifest, GIT/RTC ChangeSet installation, `DSPackageInstaller`, version-upgrade evidence (`tafj.properties.pre-v8.4.1.bak`) | `T24 upgrade`, `Patch.xml`, `ChangeSet installation`, `DSPackageInstaller` | `TAFJ-Migration` |
| `temenos-integration` | 72 ESB + 11 non-ESB payment-integration packages, `bnk/Extensions` service modules (`EB_*`/`IF_*`), `ofsml`, T24Email/T24Sms, IBM MQ/JMS, CALLJEE | `ESB project`, `payment scheme`, `IBM MQ`, `T24Email`, `CALLJEE` | `TAFJ-Integration` |
| `temenos-devsecops` | JBC precompiler rules, remote debugger, unit test framework, Maven plugin, SonarQube/code coverage, Rules Engine, multi-tenancy, Keycloak/Kerberos auth | `JBC precompiler`, `remote debugger`, `SonarQube`, `Rules Engine`, `Keycloak`, `multi-tenant` | `TAFJ-DevSecOps` |
| `temenos-architect` | Componentisation architecture (jBC components, REST exposure), the 2,955-routine `T24_BP` naming-convention structure, package/extension packaging pattern | `T24 architecture`, `componentisation architecture`, `T24_BP`, `routine naming convention` | `T24-Componentisation` |

Each of these skills routes deep-dive questions to Layer B rather than
duplicating PDF content into markdown:
```bash
python pipeline/query_docs.py "<question>" --topic TAFJ-Admin -n 5
```

---

## Repository Structure

```
Temenos-Skills/
├── CLAUDE.md                          ← architecture decisions, read every session
├── CLI.md                             ← the command line: every command with examples
├── t24skills.cmd / t24skills          ← launchers for the command line
├── pipeline/
│   ├── t24skills.py                   ← the command line: status, fields, rules, topics, samples, sample,
│   │                                     template, generate, verify, golden, diff, stages, run <stage>
│   ├── extract.py                     ← Phase 1: extract classes from JARs
│   ├── aggregate.py                   ← Phase 2: generate reference .md files
│   ├── insert_parse.py                ← Phase 1b: field name/position schema from INSERTS/I_F.*
│   ├── html_parse.py                  ← Phase 1c: backfill type/mandatory/description from JavaDoc HTML
│   ├── pdf_extract.py                 ← Phase 1d: chunk + TF-IDF embed PDFs into Chroma (Layer B)
│   ├── query_docs.py                  ← Query Layer B (CLI); topics() lists the --topic names
│   ├── validate_fields.py             ← Field Verification Gate (CLI, prints jBC names)
│   ├── component_parse.py             ← componentised (jBC) field names from component classes
│   ├── record_parse.py                ← single / multi-value flag per field (record-class getters)
│   ├── releases.py / build_release.py ← per-release knowledge DBs (R23, R25)
│   ├── release_diff.py                ← R23 → R25 change report
│   ├── artefact_fields.py             ← field references in generated code
│   ├── compile_check.py               ← tCompile / javac against R25 + write guard
│   ├── verify_artefact.py             ← accuracy gate: fields + compile
│   ├── run_golden.py                  ← run every golden case
│   ├── artefact_templates.py          ← template resolve / render / prove / export
│   ├── make_goldens.py                ← render golden cases from templates
│   ├── export_t24tools.py / release_t24tools.py ← T24Tools data + templates export (gated)
│   └── build_help.py + help_template.html ← builds Temenos-Skills-HelpText.html
├── templates/                         ← artefact templates (catalogue.json + <language>/<type>/)
├── tests/
│   ├── pipeline/                      ← unit tests (pytest)
│   └── golden/                        ← one compile-verified reference case per artefact type
├── releases/                          ← per-release knowledge DBs (git-ignored)
├── Temenos-Skills-HelpText.html       ← generated help (open in a browser)
├── mcp_server/
│   └── server.py                      ← Optional MCP server: lookup_fields, search_rules
├── cache/                             ← SHA-256 incremental cache (git-ignored)
├── jar/                                ← T24 JAR files (not in repo — supply your own)
├── T24.javadoc/                        ← T24 JavaDoc HTML (not in repo — supply your own)
├── docs/                               ← T24 PDF documentation (not in repo — supply your own)
│   ├── <business-topic folders>        ← original training/doc archive (AA, ACCOUNT, DE, OFS, ...)
│   ├── TAFJ-Admin/                     ← 28 install/runtime PDFs, sourced from a real R25 install
│   ├── TAFJ-Migration/                 ←
│   ├── TAFJ-Integration/                ←
│   ├── TAFJ-DevSecOps/                 ←
│   └── T24-Componentisation/           ←
├── vectordb/                            ← Layer B Chroma DB (git-ignored, generated)
├── plan/state/                          ← state-persistence files (e.g. r25-scan-report.md)
├── tests/
│   └── pipeline/                       ← pytest tests
├── .claude-plugin/
│   └── plugin.json                     ← Plugin manifest — enables /plugin install
└── skills/                             ← Plugin skills directory (agentskills.io layout)
    ├── temenos-dev/         ← Entry-point skill — routes to code-gen sub-skills below
    │   └── references/
    │       ├── table-schema/           ← Layer A: one .md per T24 application
    │       ├── products/               ← aa.md, payments.md, accounts.md, ...
    │       ├── hooks/                  ← lifecycle-hooks.md, validation-hooks.md, event-hooks.md
    │       ├── apis/                   ← java-api.md, rest-api.md, ofs-api.md
    │       ├── classes/                ← class-index.md
    │       ├── packages/               ← package-index.md
    │       ├── architecture/           ← application-map.md, dependency-graph.md
    │       └── relationships/
    ├── temenos-l3/          ← Sub-skill: L3 Java hooks & Core APIs
    ├── temenos-jbc/         ← Sub-skill: jBC component authoring
    ├── temenos-infobasic/   ← Sub-skill: Infobasic/jBASE BASIC routines
    ├── temenos-de/          ← Sub-skill: Delivery Engine pipeline
    ├── temenos-admin/       ← Domain skill: install, runtime config, DB/app-server admin
    │   └── references/                 ← install-and-runtime.md, database-and-config.md, observability-and-security.md
    ├── temenos-migration/   ← Domain skill: patching, version upgrade, ChangeSet installs
    │   └── references/                 ← patch-and-release.md, changeset-and-upgrade.md
    ├── temenos-integration/ ← Domain skill: ESB/non-ESB packages, service extensions, MQ/JMS
    │   └── references/                 ← esb-packages.md, service-extensions-and-messaging.md
    ├── temenos-devsecops/   ← Domain skill: build/test/debug tooling, security, multi-tenancy
    │   └── references/                 ← build-test-debug.md, security-multitenancy-rules.md
    └── temenos-architect/   ← Domain skill: componentisation architecture, package structure
        └── references/                 ← componentisation-model.md, package-and-routine-structure.md
```

---

## Prerequisites

- Python 3.10+ (dev: `pip install -r requirements-dev.txt` for pytest)
- JDK 21 with `javac` on PATH, and the R25 install at `C:\R25` — for the compile gate (optional; without it compiles report SKIPPED = FAIL)
- JDK with `javap` on PATH (verify: `javap -version`) — for `extract.py` only
- T24 JAR files in `jar/`
- T24 JavaDoc HTML in `T24.javadoc/T24.javadoc/`
- T24 PDF documentation in `docs/` (optional — only needed for Layer B)

```bash
pip install javatools pdfplumber beautifulsoup4 lxml chromadb scikit-learn joblib mcp
```

---

## Command Line (`t24skills`)

One entry point for the everyday commands and every pipeline stage. On Windows: `.\t24skills.cmd` in the repository folder (PowerShell needs the `.\`), or put the repository on your PATH once and type `t24skills` anywhere (see [CLI.md](CLI.md#put-it-on-your-path-once)). In sh: `./t24skills`. Anywhere: `python pipeline/t24skills.py`. Every command with examples and sample output: [CLI.md](CLI.md) (also the "Command line" page of the help).

```bash
t24skills status                                    # what is built, per release; is the help page stale?
t24skills fields ACCOUNT [--release R25]            # an application's fields (position, SV/MV, jBC name)
t24skills fields ACCOUNT --check AC.CUSTOMER,AC.CATEGORY   # Field Verification Gate (exit 1 if one is missing)
t24skills rules "what controls dormancy?" --topic ACCOUNT  # business-rule PDFs (never for field names)
t24skills verify out/V.CUS.CHECK.b --app CUSTOMER --release R25 [--no-compile]   # --no-app for a new local table
t24skills golden --release R25 [--case NAME]
t24skills diff R23 R25 [--full]
t24skills stages                                    # the pipeline stages, in execution order
t24skills topics                                    # the topics rules --topic accepts
t24skills samples [FILTER] [--language jbc]         # the 62 artefact samples (golden cases)
t24skills sample jbc/local-table [--file F] [--out DIR]   # one sample's requirement, inputs and code
t24skills template jbc/validation                   # a template's inputs + a generate command that works
t24skills generate jbc/validation --from-sample --set FIELD=EB.CUS.SECTOR --release R25 --out .\work
t24skills run r23|docs|refs|sepa|r25|golden|export|help [--release R25] [--dry-run]
```

**For other programs:** add `--json` to any command and stdout is one JSON object: `{"schemaVersion": 1, "command": "...", "ok": true|false, ...}`. With `run --json`, the stage's own output goes to stderr. Exit codes: `0` ok, `1` the check failed (a field is missing; verify, golden or a stage step fails), `2` cannot run (no knowledge DB or vectordb, unknown application or file). Without `--release`, commands use R23, like the pipeline scripts.

---

## How to Run

```bash
# Phase 1a — extract classes from JARs (~90 min first run, ~2 min incremental)
python pipeline/extract.py --jars jar --cache cache --workers 8

# Phase 1b — extract field schemas from INSERTS/I_F.* (Layer A ground truth)
python pipeline/insert_parse.py --jars jar --db temenos_knowledge.db --out skills/temenos-dev/references/table-schema

# Phase 1c — backfill type/mandatory/description from JavaDoc HTML
python pipeline/html_parse.py --html T24.javadoc/T24.javadoc --db temenos_knowledge.db --out skills/temenos-dev/references/table-schema

# Phase 1d — chunk + embed PDF business rules (Layer B, offline TF-IDF)
python pipeline/pdf_extract.py --pdfs docs --vectordb vectordb --cache cache/pdf_extracts

# Phase 2 — generate class/API reference markdown (~2 min)
python pipeline/aggregate.py --cache cache --out skills/temenos-dev/references

# Query Layer B
python pipeline/query_docs.py "what controls dormancy in ACCOUNT?" --topic ACCOUNT -n 5

# Verify fields before generating code
python pipeline/validate_fields.py --app ACCOUNT --fields "AC.CUSTOMER,AC.CATEGORY"

# Componentised (jBC) names for R23
python pipeline/component_parse.py --jars jar --release R23

# Single- vs multi-value flag per field (record-class getters) into table field_kinds
python pipeline/record_parse.py --jars jar --release R23

# R25 knowledge DB (read-only from C:\R25) and the R23 -> R25 change report
python pipeline/build_release.py --release R25 --javadoc-jar "C:\R25\bnk\Transact_L3_Javadoc\T24.javadoc.jar"
python pipeline/release_diff.py --old R23 --new R25

# Accuracy gate for one generated file, and every golden case
python pipeline/verify_artefact.py --file out/V.CUS.CHECK.b --app CUSTOMER --release R25
python pipeline/run_golden.py --release R25

# Gated T24Tools export (fields + templates.json)
python pipeline/release_t24tools.py --release R25

# Rebuild the help page
python pipeline/build_help.py
```

Each phase caches its own inputs by SHA-256, so re-running after adding JARs,
JavaDoc, or PDFs only reprocesses what changed — except Phase 1d's embedding
step, which always rebuilds the full Chroma collection (TF-IDF's vocabulary
has to reflect the whole corpus, not just the newly-changed files).

### Run Tests

```bash
python -m pytest tests/pipeline/ -v
```

`tests/pipeline/test_t24skills.py` covers the command line on a temporary DB; it needs no T24 install.

---

## What the Reference Files Contain

### `references/table-schema/<APP>.md`

One file per T24 application (Layer A) — field name, position, Java alias,
and type/mandatory/description where backfilled from JavaDoc. This is the
file the skill checks before ever emitting a field name in generated code.

### `references/products/<domain>.md`

Per-domain breakdown of all classes in that T24 product area:

- **Lifecycle / AA Activity / Service Hooks** — classes and their public method signatures
- **Validation & Authorization Hooks** — class name, JAR, superclass
- **Public APIs** — full method catalog with return types
- **Enquiry Routines** — class + superclass
- **Record Models** — class + public fields
- **JAR Inventory** — every JAR in the domain, class count, component types present

### `references/hooks/*.md`

Cross-domain hook catalogs:

- `lifecycle-hooks.md` — RecordLifecycle, ActivityLifecycle, ServiceLifecycle contracts + T24 override-point table
- `validation-hooks.md` — validation and auth hook classes
- `event-hooks.md` — event hook classes

> T24 product JARs ship hook *interfaces*, not customer implementations. The hooks files document the T24 API contracts (method signatures, when each fires) so Claude can guide you to implement them correctly.

### `references/apis/java-api.md`

Public API classes with full method signatures and parameter lists, enriched with JavaDoc descriptions where available:

```
ActivityLifecycle.validateRecord(AaAccountDetailsRecord, AaArrangementActivityRecord, ...)
  → com.temenos.api.TValidationResponse
```

### `references/classes/class-index.md`

Master index of all 77,762 classes across all JARs — class name, JAR, package, domain, component type.

---

## Component Type Classification

Every class is classified into one of these types:

| Type | Detection Rule |
|------|---------------|
| `lifecycle-hook` | Extends `RecordLifecycle` |
| `aa-activity-hook` | Extends `ActivityLifecycle` |
| `service-hook` | Extends `ServiceLifecycle` |
| `validation-hook` | Name ends `Validation` |
| `auth-hook` | Name ends `Authorization` |
| `enquiry-routine` | Extends `EnquiryRoutine` or `ScreenRoutine` |
| `rest-endpoint` | Annotated `@Path` or `@RestController` |
| `public-api` | In `com.temenos.t24.api` package |
| `service-interface` | Is an interface in a service package |
| `record-model` | Name ends `Record` or in `.api.records.` package |
| `event` | Implements an event interface |
| `unknown` | None of the above |

---

## Incremental Caching

Each pipeline phase caches its own input by SHA-256:

- `extract.py`: one `cache/<jar>.json` per JAR — unchanged JARs are skipped entirely
- `insert_parse.py` / `html_parse.py`: rerun in full each time (fast enough not to need caching — a few minutes over the whole JAR/JavaDoc set)
- `pdf_extract.py`: `cache/pdf_extracts/<sha256>.json` per PDF, tracked in a manifest — unchanged PDFs skip re-extraction; the embedding step always rebuilds the full Chroma collection

To force a full re-extract of a given phase, delete its cache directory (`cache/`, or `cache/pdf_extracts/`).

---

## Re-running After a T24 Upgrade

```bash
python pipeline/extract.py --jars jar --cache cache --workers 8
python pipeline/insert_parse.py --jars jar --db temenos_knowledge.db --out skills/temenos-dev/references/table-schema
python pipeline/html_parse.py --html T24.javadoc/T24.javadoc --db temenos_knowledge.db --out skills/temenos-dev/references/table-schema
python pipeline/aggregate.py --cache cache --out skills/temenos-dev/references
```

Re-run `pdf_extract.py` separately whenever `docs/` changes — it's independent of the JAR/JavaDoc release cycle.
