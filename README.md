# Temenos Skills — T24 JAR Analysis Pipeline

A two-phase Python pipeline that decompiles 2,050 Temenos T24 JAR files and parses existing T24 JavaDoc HTML to populate the `t24-dev` Claude skill with accurate, structured knowledge of the T24/Transact Java API.

---

## Install the Skills

Install all five T24 skills into Claude Code:

```
/plugin marketplace add zainknoman/Temenos-Skills
/plugin install temenos-skills@temenos-skills
```

Or browse and install from the Claude Code plugin directory:
**[claude.ai/admin-settings/directory](https://claude.ai/admin-settings/directory)** → search `temenos-skills`

Once installed, the skills activate automatically when you work on T24 artifacts. You can also invoke the entry-point skill directly:

```
/t24-dev
```

---

## What Was Built

### The Problem

The `t24-dev` Claude skill ships with 30 reference stub files containing `(populate)` placeholders. Without real API knowledge, Claude cannot reliably write correct T24 hook implementations, know which JAR a class lives in, or validate method signatures.

### The Solution

A pipeline that reads the actual T24 product JARs and JavaDoc and generates populated reference files that Claude loads when answering T24 questions.

```
jar/t24lib/          T24.javadoc/
  (2,050 JARs)         (35,222 HTML)
       |                     |
       v                     v
   Phase 1: extract.py  ──────────────>  cache/*.json
                                              |
                                              v
                                    Phase 2: aggregate.py
                                              |
                                              v
                                    skills/t24-dev/references/
```

### Results

| Metric | Value |
|--------|-------|
| JARs processed | 2,050 / 2,050 (0 errors) |
| Classes extracted | 77,762 |
| JavaDoc pages parsed | 387 |
| Reference files populated | 20 / 30 |
| Cache size | ~620 MB (incremental, SHA-256 hashed) |
| Phase 1 first-run time | ~90 min (subsequent runs: ~2 min, incremental) |
| Phase 2 run time | ~2 min |
| Test suite | 89 / 89 passing |

The 10 remaining stub files (ATM, Customer, Deposits, TPH, OFS API, object relationships, architecture diagrams) require manual curation — they cover areas not derivable from JAR bytecode alone.

---

## Skill Architecture

`t24-dev` is the single entry point. It detects context and delegates to one of four specialist sub-skills:

| Sub-skill | Covers | Triggers |
|-----------|--------|----------|
| `temenos-l3-java` | L3 Java hooks: RecordLifecycle, ServiceLifecycle, ActivityLifecycle, Enquiry; Core APIs (Amount, Date, ExchangeRate, Customer, Limit, Session, AA Contract) | `L3 java`, `RecordLifecycle`, `validateRecord`, `checkId`, `com.temenos` |
| `jbc-componentise` | jBC component authoring — full 5-phase DEVELOP workflow, 8 artefact templates (GET_API, WRITE_API, ENQUIRY, VALIDATION, TEMPLATE, DE_HANDLER), Phase 5 checklist | `jBC`, `.component`, `.b file`, `metamodelVersion`, `$PACKAGE` |
| `infobasic` | Infobasic/jBASE BASIC routines: VVR, VIR, VAR, VCRR, NoFile Enquiry, AA calculation/getter/check, service routines, batch programs | `VVR`, `VIR`, `VAR`, `VCRR`, `NoFile`, `Infobasic`, `GOSUB` |
| `temenos-de` | Delivery Engine pipeline: ApplicationHandoff routines, Array.5 mapping, event mapping table, print interface carrier, document-data FUNCTIONs | `DE handoff`, `ApplicationHandoff`, `Array.5`, `DE.API` |

The `t24-dev` skill itself handles Java API reference lookups, impact analysis, EXPLAIN/REVIEW/ANALYZE modes, and any domain not covered by a sub-skill.

---

## Repository Structure

```
Temenos-Skills/
├── pipeline/
│   ├── classify.py          # Component type detector (11 rules)
│   ├── javap_parser.py      # javap output parser + batched JAR extractor
│   ├── javadoc_parser.py    # Regex-based HTML parser (threaded)
│   ├── cache_utils.py       # SHA-256 incremental cache helpers
│   ├── extract.py           # Phase 1 CLI: JARs + JavaDoc → cache/
│   ├── aggregate.py         # Phase 2 CLI: cache/ → references/
│   ├── requirements.txt
│   └── templates/
│       ├── product.md.j2    # Per-domain product reference
│       ├── hooks.md.j2      # Hook reference (lifecycle / validation / event)
│       ├── class-index.md.j2
│       ├── api-catalog.md.j2
│       └── package-index.md.j2
├── cache/                   # Phase 1 output (git-ignored, ~620 MB)
│   ├── AA_Account.json      # One file per JAR
│   ├── ...
│   └── javadoc.json         # Merged JavaDoc descriptions
├── tests/
│   └── pipeline/            # 89 pytest tests
├── jar/t24lib/              # Source JARs (not in repo)
├── T24.javadoc/             # Source JavaDoc HTML (not in repo)
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest — enables /plugin install
└── skills/                  # Plugin skills directory (standard agentskills.io layout)
    ├── t24-dev/             # Entry-point skill — routes to sub-skills below
    │   └── references/
    │       ├── products/    # aa.md, payments.md, accounts.md, ...
    │       ├── hooks/       # lifecycle-hooks.md, validation-hooks.md, event-hooks.md
    │       ├── apis/        # java-api.md (157 classes), rest-api.md
    │       ├── classes/     # class-index.md (77,762 entries)
    │       ├── packages/    # package-index.md (137 packages)
    │       ├── architecture/# application-map.md (1,453 classes)
    │       └── relationships/ # dependency-graph.md (2,048 JARs)
    ├── temenos-l3-java/     # Sub-skill: L3 Java hooks & Core APIs
    ├── jbc-componentise/    # Sub-skill: jBC component authoring (5-phase workflow)
    ├── infobasic/           # Sub-skill: Infobasic/jBASE BASIC routines
    └── temenos-de/          # Sub-skill: Delivery Engine pipeline
```

---

## Prerequisites

- Python 3.10+
- JDK with `javap` on PATH (verify: `javap -version`)
- T24 JAR files in `jar/t24lib/`
- T24 JavaDoc HTML in `T24.javadoc/T24.javadoc/`

```bash
pip install -r pipeline/requirements.txt
```

---

## How to Run

### Phase 1 — Extract (first run ~90 min, subsequent runs ~2 min)

```bash
python pipeline/extract.py \
  --jars jar/t24lib \
  --javadoc T24.javadoc/T24.javadoc \
  --cache cache \
  --workers 8
```

This processes all JARs in parallel using 8 worker threads. Each JAR is cached as `cache/<name>.json` with a SHA-256 hash; re-runs skip unchanged JARs (incremental). JavaDoc is parsed last and written to `cache/javadoc.json`.

**Options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--jars` | required | Directory containing T24 JARs |
| `--javadoc` | required | Root of JavaDoc HTML tree |
| `--cache` | required | Output directory for cache JSON |
| `--workers` | 8 | Parallel worker threads |

### Phase 2 — Aggregate (~2 min)

```bash
python pipeline/aggregate.py \
  --cache cache \
  --output skills/t24-dev/references
```

Reads all cache JSON files, classifies every class (lifecycle-hook, service-hook, public-api, record-model, etc.), groups by domain, and renders the reference markdown files via Jinja2 templates.

### Run Tests

```bash
python -m pytest tests/pipeline/ -v
```

---

## What the Reference Files Contain

### `references/products/<domain>.md`

Per-domain breakdown of all classes in that T24 product area:

- **Lifecycle / AA Activity / Service Hooks** — classes and their public method signatures
- **Validation & Authorization Hooks** — class name, JAR, superclass
- **Public APIs** — full method catalog with return types
- **Enquiry Routines** — class + superclass
- **Record Models** — class + public fields
- **JAR Inventory** — every JAR in the domain, class count, component types present

Domains: `aa`, `payments`, `accounts`, `lending`, `securities`, `asset-management`, `teller`, `cob`, `dx`, `regulatory`, `misc`

### `references/hooks/*.md`

Cross-domain hook catalogs:

- `lifecycle-hooks.md` — RecordLifecycle, ActivityLifecycle, ServiceLifecycle contracts + T24 override-point table
- `validation-hooks.md` — validation and auth hook classes
- `event-hooks.md` — event hook classes

> Note: T24 product JARs ship hook *interfaces*, not customer implementations. The hooks files document the T24 API contracts (method signatures, when each fires) so Claude can guide you to implement them correctly. Concrete implementations are written in L3 customization code, not shipped in the product.

### `references/apis/java-api.md`

157 public API classes with full method signatures and parameter lists, enriched with JavaDoc descriptions where available. Example:

```
ActivityLifecycle.validateRecord(AaAccountDetailsRecord, AaArrangementActivityRecord, ...)
  → com.temenos.api.TValidationResponse
```

### `references/classes/class-index.md`

Master index of all 77,762 classes across all JARs — class name, JAR, package, domain, component type.

### `references/packages/package-index.md`

137 unique packages with canonical JAR and domain.

### `references/relationships/dependency-graph.md`

All 2,048 JARs with domain and class count.

### `references/architecture/application-map.md`

1,453 classes whose names contain key domain terms (Account, Payment, Arrangement, etc.) — a cross-cutting view of core T24 object types.

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

The cache uses SHA-256 hashes stored as `"sha256:<64-char-hex>"`. If a JAR's hash matches its cache file, Phase 1 skips it entirely. When T24 ships a new release, only changed JARs are re-processed — a typical patch run takes 2–5 minutes instead of 90.

To force a full re-extract, delete the `cache/` directory.

---

## Re-running After a T24 Upgrade

```bash
# Re-run Phase 1 (only changed JARs will be processed)
python pipeline/extract.py --jars jar/t24lib --javadoc T24.javadoc/T24.javadoc --cache cache --workers 8

# Re-render reference files
python pipeline/aggregate.py --cache cache --output skills/t24-dev/references
```

---

## Coverage Notes

**Fully auto-populated (20 files):** All product domain files, hooks, java-api, class-index, package-index, dependency-graph, application-map.

**Skeleton / manual curation needed (10 files):**

| File | Reason |
|------|--------|
| `products/atm.md` | ATM module uses a separate integration layer |
| `products/customer.md` | CIF data not modelled in product JARs |
| `products/deposits.md` | Deposits often overlap with AA module |
| `products/tph.md` | TPH is a separate product tier |
| `apis/ofs-api.md` | OFS (Online Financial Service) is TAFC-based, not Java |
| `apis/rest-api.md` | REST endpoints detected: 0 in analysed JARs |
| `architecture/dependencies.md` | Requires runtime dependency tracing |
| `architecture/frameworks.md` | Framework docs are not in product JARs |
| `architecture/products.md` | High-level product map — manual |
| `relationships/object-relationships.md` | Runtime object graph — not in bytecode |
| `javadocs/javadoc-index.md` | JavaDoc index — manual or separate scrape |
