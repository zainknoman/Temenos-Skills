# SEPA / TPH Knowledge Base — Provenance

Every claim in this knowledge base carries a provenance tag. This file defines
the tags and records exactly what was scanned.

## Confidence tiers

| Tag | Meaning |
|-----|---------|
| `[JAR]` | Read from compiled bytecode in `jar/` (class name, method signature, `INSERTS/I_F.<APP>` field name/position). Exact — a name that appears here exists. |
| `[SCHEMA]` | Read from `skills/temenos-dev/references/table-schema/<APP>.md`, generated from `INSERTS/I_F.<APP>`. Field name and position exact; type/mandatory/description backfilled from JavaDoc HTML and present for ~59% of fields only. |
| `[PDF p.N]` | Retrieved from a Temenos PDF indexed in the Layer B vector DB (`vectordb/`). Vendor documentation — authoritative for behaviour, but version-dated. |
| `[CLIENT]` | Read from a client-supplied document under `D:\Prema\Development\RasheedBank\review\`. Scheme-local — see the scope warning in `message-mapping.md`. |
| `[PUBLIC]` | Temenos Developer Portal or general ISO 20022 knowledge. **Not verified against these artifacts.** |
| `[GAP]` | Known unknown. Named here so it is not mistaken for a fact. |

Anything with no tag in this knowledge base is a structural statement about the
knowledge base itself, not a claim about T24.

---

## What was scanned

### JAR set — `jar/` (2,053 JARs)

Extraction cache: `cache/*.json` (2,051 entries, SHA-256 keyed, produced by
`pipeline/extract.py`). Payment-domain slice re-read by `pipeline/sepa_extract.py`:

| Metric | Count |
|--------|-------|
| Payment-domain JARs scanned | 155 |
| Classes in those JARs | 8,498 |
| Compiled jBC routines / component methods | 7,339 |
| Generated record model classes | 831 |
| Hook API classes (customisation surface) | 16 |
| Complex DTO packages | 13 |

JAR-name prefixes treated as payment domain: `PP_` (Temenos Payments / TPH),
`EP_` (European Payments — the Transact-native SEPA module), `PI_` (Payment
Initiation / Payment Order), `PW_` (Payment Workflow), `DD_` (Direct Debit),
`DB_` (Debit Collection Order), plus five named clearing JARs (`FT_Clearing`,
`FT_ClearingHook`, `AC_ClearingServiceHook`, `ACHFRM_ClearingHouseHook`,
`ACHFRM_Foundation`).

Method signatures were re-read directly from bytecode with `javap -p` for all 16
hook classes — see `java-api.md`; raw output kept under `work/javap/`.

### Field schemas — `temenos_knowledge.db` (`fields` table, 162,842 rows)

382 payment-domain applications (`PP.`, `PPT.`, `POR.`, `PAYMENT.`, `PI.`,
`SEPA.`, `EP.`, `PW.` prefixes) with exact field name + file position + Java
alias, from `INSERTS/I_F.<APP>` inside the JARs. Listed in `applications.md`;
full field lists in `skills/temenos-dev/references/table-schema/<APP>.md`.

### PDF corpus — Layer B vector DB (`vectordb/`, 32,657 chunks across 54 topics)

Re-indexed twice on 2026-08-09. Second pass added the two clearing guides that
are the authoritative sources for `config-reference.md` and the pacs.008
configuration page:

| Added | Topic | Chunks | Why it matters |
|---|---|---|---|
| `TPH Configuring Clearing.pdf` (60 pp, dated 12 Apr 2026) | `TPH-Clearing` | 88 | The authoritative `PP.CLEARING` / `PP.CLEARING.SETTING` reference. Settles the 990-vs-999 and `PPRTGF`/`PPACHF` questions, and gives the full 20-code clearing transaction type list and the file-level settlement matrix. |
| `Working with CT & DD (ACH) Clearing.pdf` (30 pp) | `TPH-R21` | 27 | Run-time counterpart: inward DD rejection (`PP0` → `DRP` → `PH0`), incoming reversal accept/reject, repair-queue flows. **Indexed but not yet mined.** |

First pass copied 84 PDFs from `D:\Learning\TPH` (→ `docs/TPH-R21/`) and
`D:\Learning\TPH Setup` (→ `docs/TPH-Setup/`). Outcome, measured not assumed:

- **7 genuinely new PDFs** entered the index, under topic `TPH-R21` (126 chunks).
  The most valuable are `SEPA/Configuring SEPA Credit Transfer.pdf` (16 chunks)
  and `Clearing/Introduction to Clearing Directory.pdf` (19 chunks) — neither was
  previously indexed.
- **All 51 `TPH Setup` PDFs are byte-identical duplicates** of files already
  indexed under the `Core/PAYMENT HUB/` tree. They contributed 0 chunks; topic
  `TPH-Setup` is empty. The copy was redundant. `[GAP]`
- The rest of `D:\Learning\TPH` duplicates the existing `TPH` / `TPH - Copy`
  topics — that archive was the original source for them.

**Coverage warning on the TPH parameter guides.** They are screenshot-heavy, so
`pdfplumber` extracts very little text: `Core/…/2 Parameters/Local Clearing.pdf`
yields 11 chunks from 784 KB; `Bank Conditions.pdf`, `Risk Filter.pdf`,
`Payment Router.pdf`, `Clearing Directory GUI.pdf` yield **1 chunk each**;
`Payment Initiation Foundation CB1PRTPI R21 Revision.pdf` yields 1 chunk from
5 MB. Do not read a Layer B miss on a configuration question as "not documented" —
it is more likely "documented in a screenshot." `[GAP]`

Payment-relevant topics present:

| Topic | Chunks | Notable sources |
|-------|--------|-----------------|
| `SEPA` | 264 | STEP2 2023 Impact Document; Rulebook Changes 2019 (TPH + EP variants); Rulebook Changes 2021 (Temenos Payments, EP Sepa, Instant) |
| `SWIFT MX` | 477 | Introduction to SWIFT MX |
| `TPH - Copy` | 262 | Intro Temenos Payments; Payments Extensibility; Messaging Framework; Payment Initiation; PAYMENT ORDER; Inward Flow; Outward and Inward Flow; FAMS (Funds Authorisation Microservice) |
| `TPH` | 91 | Introduction to Client Extensions; Introduction to Local Clearing Extensions; PAYMENT APPLICATIONS AND FLOW; TPH-APIs |
| `ISO20022` | 151 | SWIFT ISO 20022 for Dummies (6th ed. 2022); Understanding ISO 20022 |
| `Core` | 757 | includes `Core/PAYMENT HUB/.../2 Parameters/Local Clearing.pdf`, `Message Acceptance.pdf` |
| `PAYMENTS` | 4 | International Payments |
| `TPH-R21` | 126 | **Configuring SEPA Credit Transfer**; Introduction to Clearing Directory; Client Extensions; Local Clearing Extensions |

Query with `python pipeline/query_docs.py "<question>" [--topic SEPA] [-n 5]`.

**Note:** the source PDFs for the original training archive are no longer on
disk under `docs/` (only `TAFJ-*`, `T24-Componentisation`, `TPH-R21` and
`TPH-Setup` remain). The chunks are still indexed and queryable, and each carries
its original `source` path, but those PDFs cannot be re-opened for page images or
re-chunking without restoring the archive. `[GAP]`

### Not indexed — no PDF equivalent exists

Three directly on-topic documents in `D:\Learning\TPH` are `.docx` only, so the
PDF pipeline cannot see them. They are the largest remaining knowledge gap:

| File | Size | Why it matters |
|---|---|---|
| `Working with CT & DD (ACH) Clearing.docx` | 9.5 MB | Credit-transfer and direct-debit ACH clearing operation |
| `SEPA\Introduction to SEPA Credit Transfer.docx` | 307 KB | The conceptual half of the SEPA CT pair whose config half *is* indexed |
| `Configuring SEPA Credit Transfer.docx` | 1.8 MB | duplicate of the indexed PDF |

Also unread: `TPH Configuring Clearing.docx/.pdf`,
`Temenos_TPH_CT_Configuration_Guide_Phase1 V02.docx` and
`CT_Configuration_User_Guide V02.docx` under
`D:\Prema\Development\RasheedBank\review\`. `[GAP]`

### Client documents — `D:\Prema\Development\RasheedBank\review\`

| File | Read | Used in |
|------|------|---------|
| `Client Doc - IQ ACH.docx` | Full (2,390 lines extracted) | `message-mapping.md` |
| `TPH Configuring Clearing.pdf` | **Full (60 pages, read page-by-page)** | `config-reference.md`, `architecture.md`, pacs.008 config page |
| `Introduction to Payment Initiation.pdf` | Indexed in Layer B (`TPH - Copy` topic) | `architecture.md` |
| `PAYMENT APPLICATIONS AND FLOW.pdf` | Indexed in Layer B (`TPH` topic) | `architecture.md` |
| `Temenos_TPH_CT_Configuration_Guide_Phase1 V02.docx` | Not yet read | — `[GAP]` |
| `CT_Configuration_User_Guide V02.docx` / `.pdf` | Not yet read | — `[GAP]` |
| `Inward Flow.pdf`, `Outward and Inward Flow.pdf`, `PAYMENT ORDER.pdf`, `TPH Messaging Framework.pdf`, `Introduction to Messaging Framework.pdf` | Indexed in Layer B | `architecture.md` |
| `CT_Flowcharts.html`, `JIB.png` | Not read | — `[GAP]` |

---

## Known gaps

- **No `T24.javadoc/` tree on disk.** The `fields` table carries JavaDoc-derived
  descriptions for ~59% of fields; the rest have a blank type/mandatory cell.
  A blank means *not captured*, never *optional*. `[GAP]`
- **No decompiled bodies.** Routine and class *names* are ground truth; their
  *logic* is not captured. Decompile with CFR/Procyon if behaviour matters. `[GAP]`
- **No `pacs`/`pain`/`camt`-named Java classes exist in this JAR set.** ISO 20022
  message structure lives in configuration (the `UNIFI.XML.*` applications for
  the EP module) and in XSD/XSLT files on the file system, not in bytecode.
  Searching the JARs for `pacs` returns zero classes. `[JAR]`
- **The `classes`/`methods` tables in `temenos_knowledge.db` were built from an
  older, dot-named JAR set** (`PP.DataAccessApi.jar`) and hold only 9,000 public
  API classes. The `fields` table and `cache/*.json` reflect the current
  underscore-named set (`PP_DataAccessApi.jar`). Prefer `cache/` and `fields`.
  `[GAP]`
- **Release version of the JAR set is not recorded anywhere in the artifacts.**
  Configuration and customisation guidance below should be re-checked against the
  target environment's actual release before deployment. `[GAP]`
