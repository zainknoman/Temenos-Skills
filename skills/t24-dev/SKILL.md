---
name: t24-dev
description: >
  Use when developing, reviewing, debugging, or analyzing any Temenos T24/Transact artifact:
  Java services, Infobasic routines, jBC components, or any T24 framework integration.
  Covers Core Banking, AA, OFS, DE, TPH, ATM, COB, Payments, Accounts, Customers, REST, EB APIs.
  Triggers: Temenos, T24, Transact, JAR analysis, JavaDoc, jBC, Infobasic, componentise,
  AA framework, DE handoff, OFS, TPH, ATM, COB, CustomerRecord, AccountRecord,
  AAActivityRecord, EB.API, lifecycle hook, version routine, VVR, VIR, VAR, VCRR,
  NoFile enquiry, SUBROUTINE, FUNCTION, $USING, $PACKAGE, ApplicationHandoff,
  OfsBuildRecord, QueryBuilder, REST API, impact analysis, code generation.
---

# T24 Dev — Temenos Development Intelligence

## Architecture Overview

Three layers:

1. **Knowledge Base** — generated from JAR analysis, JavaDoc, decompiled sources, XML metadata,
   BPMN, and properties files covering all Temenos products and frameworks.
2. **Development Intelligence** — framework-aware code generation, review, debug, refactor,
   impact analysis, and business-to-code mapping for every discovered artifact.
3. **Skill Router** — routes requests to the correct domain based on context.

---

## Reference Files

All reference files live under `references/` relative to this skill.

| File | When to load |
|------|-------------|
| [references/architecture/products.md](references/architecture/products.md) | Product map, framework overview, module ownership |
| [references/architecture/frameworks.md](references/architecture/frameworks.md) | EB.API, AA, OFS, DE, TPH, COB, ATM internal architecture |
| [references/architecture/dependencies.md](references/architecture/dependencies.md) | Cross-JAR dependency graph, package relationships |
| [references/architecture/application-map.md](references/architecture/application-map.md) | T24 application -> class -> JAR -> product mapping |
| [references/products/aa.md](references/products/aa.md) | AA framework: arrangements, activities, properties, schedules, hooks |
| [references/products/accounts.md](references/products/accounts.md) | ACCOUNT, AC.AccountOpening, balances, postings |
| [references/products/customer.md](references/products/customer.md) | CUSTOMER, ST.Customer, KYC, local references |
| [references/products/lending.md](references/products/lending.md) | LD, AA lending, schedules, interest, repayments |
| [references/products/deposits.md](references/products/deposits.md) | TD, AA deposits, maturity, rollover |
| [references/products/payments.md](references/products/payments.md) | FT, payments framework, routing, SWIFT |
| [references/products/tph.md](references/products/tph.md) | TPH classes, payment hub extensions, adapters |
| [references/products/atm.md](references/products/atm.md) | ATM classes, teller, cash management |
| [references/apis/java-api.md](references/apis/java-api.md) | Java API classes, method signatures, parameters, return types |
| [references/apis/rest-api.md](references/apis/rest-api.md) | REST endpoints, annotations, request/response models |
| [references/apis/ofs-api.md](references/apis/ofs-api.md) | OFS patterns, OfsBuildRecord, OfsCallBulkManager, message formats |
| [references/hooks/lifecycle-hooks.md](references/hooks/lifecycle-hooks.md) | All lifecycle hook classes, when they fire, parameters |
| [references/hooks/event-hooks.md](references/hooks/event-hooks.md) | Event framework, listeners, event types per product |
| [references/hooks/validation-hooks.md](references/hooks/validation-hooks.md) | Validation classes, authorization classes, getRNew/setE patterns |
| [references/classes/class-index.md](references/classes/class-index.md) | Master class index: name, JAR, package, product, framework |
| [references/packages/package-index.md](references/packages/package-index.md) | Package index with $USING declarations and namespace map |
| [references/javadocs/javadoc-index.md](references/javadocs/javadoc-index.md) | JavaDoc summaries merged with decompiled class documentation |
| [references/relationships/object-relationships.md](references/relationships/object-relationships.md) | Class/Application/Product/Event/Hook relationship graph |
| [references/relationships/dependency-graph.md](references/relationships/dependency-graph.md) | Impact analysis: used-by, calls, called-by, triggers |

**Loading guide:**
- Code generation: `class-index.md` + relevant product file + hooks files
- Impact analysis: `dependency-graph.md` + `object-relationships.md`
- JavaDoc lookup: `javadoc-index.md` + `class-index.md`
- Framework questions: `frameworks.md` + relevant product file
- Direct factual question: answer inline if the answer is clear without loading files

---

## Identifying Multivalue Core Fields from JAR Structure

Before generating or reviewing code for any T24 application, check whether its fields are multivalue:

1. Navigate to `jar\com\temenos\t24\api\records\` in the JAR folder
2. Find the subfolder for the application (e.g., `aaaccountarrangement\` for `AA.ARR.ACCOUNT`)
3. Inspect the files in that subfolder:
   - **Primary file** `<AppNameCamelCase>Record.java` + `.class` (e.g., `AaArrAccountRecord.java`) = the record class — not a field
   - **Every other** `*Class.java` + `.class` file (e.g., `AltIdTypeClass.java`, `PostingRestrictClass.java`) = a **multivalue core field group class**
4. **Each extra class = one multivalue field** on that application record

**Example:** `AA.ARR.ACCOUNT` subfolder contains:
- `AaArrAccountRecord.java` → record class (ignored for MV detection)
- `AltIdTypeClass.java` → `ALT.ACCT.TYPE` is multivalue
- `PostingRestrictClass.java` → `POSTING.RESTRICT` is multivalue

**Enforcement:** never read a detected MV field as a scalar. Route to the appropriate sub-skill for correct MV coding patterns:
- Infobasic → `FOR/NEXT + DCOUNT` / `record<POS, i>` / `FIELD(rec, @VM, i)`
- jBC component → `DCOUNT(@VM)` loop + `*` marker in `.complex` for MV output fields
- L3 Java → `List<XxxClass>` typed accessor via generated record class

---

## Mode Detection

Read the request and identify the operating mode, then announce it before proceeding:
> "Mode: GENERATE -- loading framework context and selecting template."

| Signal | Mode |
|--------|------|
| "what does", "explain", "describe", "what is", "show JavaDoc" | **EXPLAIN** |
| "review", "check", "assess", "is this correct" | **REVIEW** |
| "debug", "why is this failing", "what is wrong", "fix" | **DEBUG** |
| "refactor", "improve", "optimise", "clean up" | **REFACTOR** |
| "generate", "write", "create", "build", "implement" | **GENERATE** |
| "impact", "what breaks", "depends on", "used by", "calls" | **ANALYZE** |

---

## Skill Router

Route to the correct domain. For rows marked **REQUIRED SUB-SKILL**, invoke that skill now and follow its workflow.

| Detected context | Action |
|-----------------|--------|
| AA, AAActivityRecord, ARRANGEMENT, property, schedule | AA Framework (inline) |
| RecordLifecycle, ServiceLifecycle, ActivityLifecycle, Enquiry, L3 Java, hook, validateRecord, checkId, autoField, com.temenos | **REQUIRED SUB-SKILL:** `temenos-l3-java` |
| DE.API, ApplicationHandoff, Array.5, DE.EVENT.MAPPING | **REQUIRED SUB-SKILL:** `temenos-de` |
| TPH, payment hub, adapter, payment message | TPH (inline) |
| OFS, OfsBuildRecord, OfsCallBulkManager | OFS (inline) |
| CustomerRecord, CUSTOMER, ST.Customer | Customer (inline) |
| AccountRecord, ACCOUNT, AC.AccountOpening | Accounts (inline) |
| FT, FUNDS.TRANSFER, payments routing | Payments (inline) |
| REST, @GET, @POST, @Path, @QueryParam | REST API (inline) |
| COB, batch, end-of-day, COB.SERVICE | COB (inline) |
| ATM, TT.Contract.Teller, cash, denomination | ATM/Teller (inline) |
| VVR, VIR, VAR, VCRR, NoFile, Infobasic, SUBROUTINE, GOSUB | **REQUIRED SUB-SKILL:** `infobasic` |
| jBC, .component, .b file, metamodelVersion, $PACKAGE | **REQUIRED SUB-SKILL:** `jbc-componentise` |

If multiple domains are detected, activate all relevant domain skills and synthesize.

---

## EXPLAIN Mode

When explaining any discovered artifact, generate:

**Type** / **Package** / **JAR** / **Product** / **Framework** / **JavaDoc Summary** /
**Technical Description** / **Business Description** / **Key Methods** (name, params, return,
purpose) / **Dependencies** ($USING, referenced classes, called APIs) / **Related Applications** /
**Related Events** / **Related Hooks** / **Usage Examples** (compilable) / **Impact** (used-by list)

---

## GENERATE Mode

### Step 1 -- Classify the requirement

Identify: target product/framework, operation type, target T24 application(s), artefact type.

| Operation | Code artefact |
|-----------|--------------|
| Read and return T24 record data | GET_API / VIR / NoFile Enquiry |
| Create or amend via OFS | WRITE_API / OFS routine / VVR |
| Validate field or record on commit | VALIDATION hook / VAR / VCRR |
| Fire on lifecycle event | Event listener / AA hook / EB.ACTIVITY |
| Run scheduled or batch job | COB service / Batch routine |
| Feed Document Engine print | DE handoff routine / DE.GET.* FUNCTION |
| Expose as REST endpoint | REST jBC component / Java REST class |
| AA property calculation | AA Calculation / AA Getter / AA Check |
| Define custom application schema | TEMPLATE definition |
| Handle inbound integration | OFS processor / Integration adapter |

### Step 2 -- Select and apply template

**Infobasic** — **REQUIRED SUB-SKILL:** `infobasic`:
VVR | VIR | VAR | VCRR | NoFile Enquiry | Service | Batch | DE Routine |
OFS Routine | AA Calculation | AA Check | AA Getter | Conversion Routine

**jBC Componentization** — **REQUIRED SUB-SKILL:** `jbc-componentise` (apply full 5-phase workflow):
GET_API | WRITE_API | ENQUIRY | VALIDATION | TEMPLATE | DE_HANDLER +
.complex DTO and .component declaration files

**Java** — **REQUIRED SUB-SKILL:** `temenos-l3-java`:
RecordLifecycle | ServiceLifecycle | ActivityLifecycle | Enquiry | NoFile Enquiry |
version routines (checkId, validateRecord, autoField, input, beforeAuth, auth) |
Core APIs (Amount, Date, ExchangeRate, Customer, Limit, Session, AA Contract)

### Step 3 -- Generate

Produce complete, compilable code including:
- All mandatory headers and $PACKAGE / $USING declarations
- Author block
- Full implementation with GOSUB structure where required
- Initialisation guard where applicable
- History fallback (.ReadHis) for archiving applications
- outRecord population with qualified field positions
- Error handling
- Return statement matching artefact type (FUNCTION vs SUBROUTINE)

### Step 4 -- Validation checklist

Run the full checklist for the generated artefact type before presenting output.

---

## Business Requirement to Code Mapping

For every business requirement, generate the complete chain:

**Requirement** -> **T24 Applications** -> **Classes** -> **APIs** -> **Hooks** ->
**Events** -> **Records** -> **Example Code**

```
Requirement: [stated business need]

T24 Applications: [APPLICATION.NAME list]
Classes: [fully qualified class names]
APIs: [method signatures with parameters]
Hooks: [hook type and trigger point]
Events: [event names and when fired]
OFS Pattern: [if create/amend/delete]
Example Code: [complete compilable implementation]
```

---

## REVIEW Mode

```
ANALYSIS -- [FileName]
  Artefact type: [Infobasic | jBC component | Java | REST]
  Domain: [AA | DE | OFS | TPH | Customer | Accounts | Payments | COB | ATM]
  Issues found:
    [CRITICAL] description -- causes compile error or runtime failure
    [WARNING]  description -- causes incorrect behaviour
    [STYLE]    description -- deviates from Temenos standards
  Best practices violated: [list]
  Anti-patterns detected: [list]
  Performance concerns: [list]
  Security concerns: [list]
  Suggested fixes: [specific line-level corrections]
  Checklist result: PASS / FAIL (n issues)
```

---

## ANALYZE Mode -- Impact Analysis

```
Impact Analysis -- [ClassName / methodName]

Used By:        [classes and routines that call this]
Calls:          [classes and APIs this invokes]
Called By:      [hooks, events, services that trigger this]
Dependencies:   [JARs, packages, applications required]
Database:       [T24 records read and written]
Events Fired:   [events triggered by this artifact]
Services:       [services that depend on this]
Applications:   [T24 applications affected]

Risk Assessment:
  Modifying this artifact affects: [impact list]
  Breaking change risk: HIGH / MEDIUM / LOW
  Regression scope: [what to test]
```

---

## Framework-Specific Coding Standards

For every detected framework, enforce:

- **Best Practices**: canonical patterns from discovered implementations
- **Anti-Patterns**: detected misuse patterns with corrections
- **Common Bugs**: known failure modes with fixes
- **Performance Issues**: identified bottlenecks with optimisations
- **Security Concerns**: exposure risks with mitigations
- **Upgrade Risks**: version-sensitive patterns flagged for review
- **Refactoring Recommendations**: modernisation paths
