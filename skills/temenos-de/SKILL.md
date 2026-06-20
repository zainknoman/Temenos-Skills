---
name: temenos-de
description: >
  Expert assistant for Temenos T24/Transact Delivery Engine (DE) customisation in jBC.
  Covers the full DE pipeline: ApplicationHandoff routine authoring (FT, TT, AA, FX, MM, REPO, SEC);
  Array.5 position mapping; project DE.EVENT.MAPPING table setup (template + fields routines);
  print interface carrier; document-data FUNCTION routines (<PKG>.GET.*);
  and the project LocalDevelopments component file.
  Triggers: 'DE handoff', 'ApplicationHandoff', 'Array.5', 'DE.API', 'DE.MAPPING',
  'Docupilot', 'DE event mapping', 'delivery engine', 'print interface',
  'DE outward', 'DE inward', 'document routine'.
---

# Temenos DE (Delivery Engine) — jBC Skill

> **Naming convention:** Throughout this skill, `<PKG>` is a placeholder for your project package name (e.g., `MY.BANK`, `CORP.CUSTOM`). Replace it with your actual package prefix in all routine names, component declarations, and T24 table names. `<Pkg>` is the PascalCase form used in component class aliases.

## Architecture Overview

The DE pipeline has three layers:

1. **Handoff Routines** (`<PKG>.DE.*.DETAILS`) — called by T24 at transaction authorisation; populate `Array.5` and call `DE.API.ApplicationHandoff`.
2. **Event Mapping Table** (`<PKG>.DE.EVENT.MAPPING` + `<PKG>.DE.EVENT.MAPPING.FIELDS`) — maps a transaction type code to one or more `DE.MAPPING` keys, category filters, doc codes, user refs, and param codes.
3. **Document Data Routines** (`<PKG>.GET.ACCxx.*` / `<PKG>.GET.ISSxx.*`) — REST FUNCTION endpoints called by Docupilot after DE fires; read live/history records and return a typed `outRecord`.

Supporting infrastructure:
- `<PKG>.DE.PRINT.INTERFACE` — DE delivery carrier; invokes Docupilot Java client.
- `<PKG>.DE.DOCU.PROCESS.API` — CALLJ wrapper around the Docupilot Java class.
- `<PKG>.DE.DOCU.RESPONSE` / `<PKG>.DE.DOCU.RESPONSE.FIELDS` — audit log table for request/response payloads.
- `<PKG>.GATEWAY.PARAM` — credential/URL store for external gateways (record id `DOCUPILOT`).

## Reference Files

| File | When to read |
|------|-------------|
| [de-arrays.md](references/de-arrays.md) | Writing or reviewing any `Array.5` population block |
| [de-applications.md](references/de-applications.md) | Looking up T24 field equates, `$USING` packages, or application structure |
| [de-workflows.md](references/de-workflows.md) | Understanding how DE fires, event mapping setup, or carrier/formatter flow |
| [de-code-patterns.md](references/de-code-patterns.md) | Generating new handoff routines, document routines, or reviewing existing code |

---

## Generating a New Handoff Routine

Read [de-code-patterns.md](references/de-code-patterns.md) first, then follow this checklist:

1. Determine the **source application** (FT / TT / AA / FX / MM / REPO / SEC).
2. Copy the correct template from `de-code-patterns.md` — choose FT or TT variant.
3. Replace `$USING` packages, `getRNew` field equates, and `Array.5` positions per [de-arrays.md](references/de-arrays.md).
4. Name the routine `<PKG>.DE.<APP>.DETAILS` and declare it `private method <pkg>De<App>Details` in the component file.
5. The routine is **parameter-less** (all data via `getRNew`); do **not** add parameters unless it is an AA variant (`handOffRecord INOUT, errorMsg OUT`).
6. Register it in `<PKG>.DE.EVENT.MAPPING.FIELDS` — the transaction type code goes in the `@ID` field.

## Generating a New Document Data FUNCTION

Read [de-code-patterns.md](references/de-code-patterns.md) (section "Document Data FUNCTION") first.

1. Name: `<PKG>.GET.<CATEGORY><NN>.<DESCRIPTIVE>` (e.g., `<PKG>.GET.ACC17.ACCTRANSFER`).
2. Signature: `FUNCTION <PKG>.GET.<X>(transactionId)` — single IN parameter.
3. Initialisation guard: always call `<PKG>.LocalDevelopments.initialise<PackageName>()` if `getinitialised() NE 'Y'`.
4. Read live record first; fall back to history with `;1` suffix.
5. Populate `outRecord` using the component's typed struct equates (`<PKG>.LocalDevelopments.<docStruct>.<fieldName>`).
6. Register as a `@GET` REST endpoint in the component file.

## Reviewing Existing DE Code

Check against these standards:
- `Array.5` positions are populated correctly per [de-arrays.md](references/de-arrays.md).
- `DR` side uses positions 1,2,3,4,6,8,10,12,14,16,18,20,22-30; `CR` side uses 1,2,3,5,7,9,11,13,15,17,19,20,21-30.
- `DeliveryOutref` multi-value append uses `<1,-1>` idiom.
- Amount strip: `amountDebited[4,LEN(amountDebited)]` removes 3-char CCY prefix.
- Date format: `YYYY-MM-DD HH:MM` assembled from `OCONV(DATE(),'D4-')` + `dateTime[7,2]`/`[9,2]`.
- Language guard: `'1'` = English, `'2'` = Arabic — always set currency name display accordingly.
- Category filter: `INDEX(DrCategory,debitAccountCategory,1)` — correct pattern.
- Error propagation: `errorResponse = 'STOP-':errorMessage` in print interface.

## Answering Setup Questions

- **DE.MESSAGE / DE.MAPPING / DE.PRODUCT / DE.ADDRESS / DE.CARRIER / DE.FORMAT.PRINT / DE.FORMAT.SWIFT** — see [de-applications.md](references/de-applications.md) for all field descriptions, ID formats, and search order.
- **Full T24 DE pipeline stages (Mapping → Formatting → Carrier), queue file names, services** — see [de-workflows.md](references/de-workflows.md) sections 7–7b.
- **Repair, resubmit, re-route, DE.DISP.CONTROL** — see [de-workflows.md](references/de-workflows.md) section 7b.
- **Soft Delivery (AA, LC, BL)** — `EB.ACTIVITY`, `EB.ADVICES`, `EB.MESSAGE.CLASS`; see [de-workflows.md](references/de-workflows.md) section 7c.
- **EMAIL / SMS / SECUREMSG carriers** — `DE.FORMAT.XML`, `EB.TRANSFORM`; see [de-workflows.md](references/de-workflows.md) section 7 (Stage 3).
- **Inward SWIFT flow** — tSS → OFS.DE.PROCESSING → DE.I.HEADER → BNK/SWIFT.IN → DE.INWARD → OFS.GLOBUS.MANAGER; see [de-workflows.md](references/de-workflows.md) section 8.
- **EB.API records** — see [de-applications.md](references/de-applications.md).
- **`<PKG>.GATEWAY.PARAM`** — record id `DOCUPILOT`; fields: `<Pkg>HUsername`, `<Pkg>HPassword`, `<Pkg>HEndpointUrl`, `<Pkg>HTokenUrl`.
- **F.DE.O.HANDOFF row structure** — see [de-arrays.md](references/de-arrays.md) section "F.DE.O.HANDOFF Row Structure".
