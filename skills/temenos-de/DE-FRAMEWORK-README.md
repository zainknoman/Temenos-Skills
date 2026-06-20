# Delivery Engine (DE) Framework — Developer Guide

This guide covers how to develop with the T24 Delivery Engine in the `<PKG>.LocalDevelopments` package, and how to use the `temenos-de` Claude skill to accelerate that work.

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Using the temenos-de Skill](#using-the-temenos-de-skill)
3. [Creating a New Handoff Routine](#creating-a-new-handoff-routine)
4. [Creating a New Document FUNCTION](#creating-a-new-document-function)
5. [Setting Up `<PKG>.DE.EVENT.MAPPING`](#setting-up-pkgdeeventmapping)
6. [T24 DE Application Configuration](#t24-de-application-configuration)
7. [Troubleshooting and Repair](#troubleshooting-and-repair)
8. [Reference: Key Files](#reference-key-files)

---

## Architecture Overview

The DE pipeline has three layers:

```
T24 Transaction AUTHORISE
        │
        ▼
[Layer 1] Handoff Routine (<PKG>.DE.*.DETAILS)
  - Reads <PKG>.DE.EVENT.MAPPING to find DE.MAPPING keys
  - Populates Array.5 with document data
  - Calls DE.API.ApplicationHandoff → writes F.DE.O.HANDOFF
        │
        ▼  (T24 DE Mapping Stage — automatic)
[Layer 2] T24 DE Framework
  - DE.MESSAGE + DE.MAPPING → map variables
  - DE.PRODUCT + DE.ADDRESS → decide carrier and address
  - BNK/PRINT.OUT service → DE.OUTWARD → DE.FORMAT.PRINT
        │
        ▼  (T24 DE Formatting + Carrier Stage)
[Layer 3] Carrier — <PKG>.DE.PRINT.INTERFACE
  - Reads <PKG>.GATEWAY.PARAM 'DOCUPILOT' for credentials
  - Extracts documentCode, userReference, parameterCode from deliveryPackage
  - Builds JSON payload
  - Calls <PKG>.DE.DOCU.PROCESS.API → CALLJ → Java Docupilot client
  - Logs to <PKG>.DE.DOCU.RESPONSE audit table
        │
        ▼
[REST Endpoint] Document Data FUNCTION (<PKG>.GET.ACCxx.* / <PKG>.GET.ISSxx.*)
  - Docupilot calls the REST endpoint with the transaction ID
  - Reads live or history T24 record
  - Returns typed outRecord to Docupilot for PDF generation
```

Supporting files:
| File | Purpose |
|------|---------|
| `<PKG>.DE.EVENT.MAPPING` | Maps transaction type code → DR/CR DE.MAPPING keys + doc codes |
| `<PKG>.DE.EVENT.MAPPING.FIELDS` | Field definitions for the mapping table |
| `<PKG>.DE.DOCU.PROCESS.API` | CALLJ wrapper for Docupilot Java client |
| `<PKG>.DE.DOCU.RESPONSE` | Audit log table for Docupilot request/response |
| `<PKG>.GATEWAY.PARAM` | External gateway credentials; record `DOCUPILOT` |

---

## Using the temenos-de Skill

The `temenos-de` skill is installed at:
```
C:\Users\Lenovo\.claude\skills\temenos-de\
```

### Installation

If not already installed, copy `temenos-de.skill` to your Claude Code skills directory:
1. Copy `temenos-de.skill` from this project root to `C:\Users\Lenovo\.claude\skills\`.
2. Claude Code will auto-discover it.

### Triggering the Skill

The skill activates automatically when you mention any of:
- `DE handoff`, `ApplicationHandoff`, `Array.5`, `DE.API`
- `DE.MAPPING`, `<PKG>.DE.`, `<PKG>.GET.ACC`, `<PKG>.GET.ISS`
- `Docupilot`, `DE event mapping`, `delivery engine`
- `print interface`, `DE outward`, `DE inward`, `document routine`

You can also trigger it explicitly:
```
/temenos-de
```

### What the Skill Provides

| Reference File | Contents |
|----------------|---------|
| `de-arrays.md` | Array.5 position tables for FT DR/CR and TT; F.DE.O.HANDOFF row structure |
| `de-applications.md` | All `$USING` packages, field equates, T24 DE application field descriptions |
| `de-workflows.md` | DE firing flow; T24 classic pipeline stages; queue files; repair/resubmit; soft delivery; inward SWIFT |
| `de-code-patterns.md` | Full jBC templates for handoff routines, document FUNCTIONs, event mapping tables |

### Example Prompts

```
"Generate a new DE handoff routine for the AA (Arrangement Architecture) application"

"Review this <PKG>.DE.FT.DETAILS.b code against the framework standards"

"What DE.PRODUCT record ID format should I use for a FT credit advice for account 123456?"

"How do I resubmit a delivery advice that went to repair?"

"What queue file holds unformatted PRINT advice IDs?"
```

---

## Creating a New Handoff Routine

### Step 1 — Determine the application

Identify the T24 application: `FT`, `TT`, `AA`, `FX`, `MM`, `REPO`, or `SEC`.

### Step 2 — Create the `.b` file

Name: `<PKG>.DE.<APP>.DETAILS.b`

Structure follows the **FT template** (use `de-code-patterns.md` from the skill):
- `$PACKAGE <PKG>.LocalDevelopments`
- `$USING` the relevant T24 packages
- Read `<PKG>.DE.EVENT.MAPPING` by the transaction type code
- Loop over DR and CR mapping keys
- Apply category filter: `IF INDEX(DrCategory, debitAccountCategory, 1) THEN`
- Populate `Array.5` — positions 1–30 (see `de-arrays.md` for exact mapping)
- Call `DE.API.ApplicationHandoff(Rec1..Rec9, MapKey, VKey, ErrorMsg)`
- Append `VKey` to `DeliveryOutref` multi-value field

**AA variant** has a different signature — two parameters (`handOffRecord INOUT, errorMsg OUT`).

### Step 3 — Register in the component file

In `<PKG>.LocalDevelopments.component`, add:

```
private method cbiDe<App>Details () {
    jBC: <PKG>.DE.<APP>.DETAILS
}
```

For AA:
```
public method cbiDeAaDetails (INOUT handOffRecord string, OUT errorMsg string) {
    jBC: <PKG>.DE.AA.DETAILS
}
```

### Step 4 — Compile

In the EDS/TAFJ IDE, compile `<PKG>.DE.<APP>.DETAILS.b` with the R22_AMR.0 compiler under package `<PKG>.LocalDevelopments`.

---

## Creating a New Document FUNCTION

Document FUNCTIONs are REST endpoints called by Docupilot to fetch document data.

### Step 1 — Name the file

Convention: `<PKG>.GET.<CATEGORY><NN>.<DESCRIPTIVE>.b`
- Examples: `<PKG>.GET.ACC12.USDINWARD.b`, `<PKG>.GET.ISS06.CHQREQ.b`

### Step 2 — Write the FUNCTION

```jbc
$PACKAGE <PKG>.LocalDevelopments
$USING <PKG>.LocalDevelopments
$USING FT.Contract.FundsTransfer
; ... other $USING as needed

FUNCTION <PKG>.GET.<CATEGORY><NN>.<DESCRIPTIVE>(transactionId)

    outRecord = ""
    
    ; Initialisation guard
    IF <PKG>.LocalDevelopments.getinitialised() NE 'Y' THEN
        <PKG>.LocalDevelopments.initialiseDigiArena()
    END
    
    ; Read live record; fall back to history
    ftRecord = ""
    READ ftRecord FROM FT.Contract.FundsTransfer.getRFile(), transactionId ELSE
        transactionId = transactionId:';1'
        READ ftRecord FROM FT.Contract.FundsTransfer.getRFile(), transactionId ELSE
            RETURN outRecord
        END
    END
    
    ; Populate outRecord using component equates
    outRecord<<PKG>.LocalDevelopments.<docStruct>.fieldName> = ftRecord<FT.Contract.FundsTransfer.TransactionType>
    ; ... more fields
    
    RETURN outRecord

END
```

### Step 3 — Register in the component file

```
@Response("")
@Path("/get/<endpoint>")
@GET
public method get<Name> : Docupilot:<docStruct>(
    @QueryParam("transactionId")
    IN transactionId string
)
{
    jBC: <PKG>.GET.<CATEGORY><NN>.<DESCRIPTIVE>
}
```

### Step 4 — Compile and test

Compile with R22_AMR.0. Test the REST endpoint via the component's base URL.

---

## Setting Up <PKG>.DE.EVENT.MAPPING

Each T24 transaction type that should trigger a DE advice needs a record in `<PKG>.DE.EVENT.MAPPING`.

### Record ID

The `@ID` is the transaction type code. For FT, this is the value of `FT.Contract.FundsTransfer.TransactionType` (e.g., `AC`, `OT`, `FT.OWN.ACC`).

### Fields

| Field | Notes |
|-------|-------|
| `DR.DE.MAPPING` | Multi-value list of DE.MAPPING record IDs for the debit advice (e.g., `900.FT.1`) |
| `DR.CATEGORY` | Sub-value per mapping: space-delimited account category codes that must match the debit account; blank = all categories |
| `DR.DOC.CODE` | Sub-value: Docupilot document code sent in the payload |
| `DR.USER.REF` | Sub-value: user reference label |
| `DR.PARAM.CODE` | Sub-value: parameter code sent to Docupilot |
| `CR.DE.MAPPING` | Same as DR fields but for credit side |
| … (CR.CATEGORY, CR.DOC.CODE, CR.USER.REF, CR.PARAM.CODE) | |

### Category Filter

The handoff routine uses the category filter to decide whether to fire DE:
```jbc
IF INDEX(DrCategory, debitAccountCategory, 1) THEN
    ; fire DE for this mapping key
END
```
`DrCategory` is the space-delimited string from `<PKG>.H.DR.CATEGORY`. If blank, DE fires for all categories.

---

## T24 DE Application Configuration

For a new document type, configure these T24 applications **in order**:

### 1. DE.MESSAGE

Defines the variable names for the advice. ID = numeric (e.g., `900`). Pre-configured by T24 — check if existing record covers your message type before creating a new one.

Key fields: `FIELD.NAME` (variable name), `LENGTH`, `PRINT.TYPE` (A/N), `SINGLE.MULTI` (S/M), `MANDATORY` (Y/N).

### 2. DE.MAPPING

Maps each variable in DE.MESSAGE to a position in F.DE.O.HANDOFF. **ID = `<MsgType>.<App>.<CurrNo>`** e.g. `900.FT.1`.

Key fields: `INPUT.REC.NO` (which row of HANDOFF contains R.NEW), `INPUT.FILE` (e.g. `FUNDS.TRANSFER`), `FIELD.NAME` (variable), `INPUT.POSITION` (e.g. `5.12` for row 5 position 12), or `INPUT.NAME` for field-name mapping.

### 3. DE.PRODUCT

Decides how and where to send the advice. **ID = `<Company>[.C-Cust|.A-Acct].<MsgType>.<App>`** e.g. `GB0010001.900.FT`.

Search order (most specific wins): Account → Customer → Message-specific → App-specific → `ALL.ALL`.

Key fields: `MESSAGE.STATUS` (NORMAL/HOLD/DELETE), `CARRIER.ADDR.NO` (e.g. `PRINT.1`), `LANGUAGE`, `FORMAT` (version number), `COPIES`.

### 4. DE.ADDRESS

Physical delivery address per customer. **`PRINT.1`** record is auto-created when a CUSTOMER record is authorised (cannot be edited). `SWIFT.1` must be created manually.

For custom carrier: set `PRINT.CARRIER = <PKG>.DE.PRINT.INTERFACE` in the address record.

### 5. DE.FORMAT.PRINT

Layout template for PRINT advices. **ID = `<MsgType>.<AppFormat>.<Version>.<Language>`** e.g. `900.1.1.GB`.

Application Format component is passed by the application to APPLICATION.HANDOFF (hard-coded). Version and Language come from DE.PRODUCT.

---

## Troubleshooting and Repair

### Viewing a delivery advice status

1. Open the T24 record (e.g., FT contract).
2. Look at the `DELIVERY.OUTREF` field — contains the Delivery Reference IDs.
3. Open `DE.O.HEADER` with that ID to see `DISPOSITION` and `MSG.DISPOSITION`.
4. Run enquiry `DE.HANDOFF.DETS` to view the raw HANDOFF data.

### Common repair causes

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| DISPOSITION = REPAIR after mapping | Mandatory DE.MESSAGE variable has no value in Array.5 | Check handoff routine populates the correct position; check DE.MAPPING INPUT.POSITION |
| MSG.DISPOSITION = REPAIR after formatting | DE.FORMAT.PRINT record missing or wrong ID | Create/correct DE.FORMAT.PRINT record; resubmit |
| No advice generated at all | `DR.ADVICE.REQD` / `CR.ADVICE.REQD` not set to `Y` | Open `FT.TXN.TYPE.CONDITION` for the transaction type and set both fields to `Y` |
| Wrong DE.PRODUCT selected | More-specific record missing | Create account/customer-level DE.PRODUCT or check search order |
| Docupilot not called | DE.PRODUCT CARRIER.ADDR.NO not pointing to <PKG>.DE.PRINT.INTERFACE address | Check DE.ADDRESS `PRINT.CARRIER` field |

### Resubmitting a repair

1. Fix the root cause (e.g., add missing DE.FORMAT.PRINT record).
2. Open the `DE.O.HEADER` record for the Delivery Reference ID.
3. Change `DISPOSITION` to `Resubmit`.
4. Authorise the record.
5. The advice moves from `F.DE.O.REPAIR` back to `F.PRINT.OUT.LIST` for another formatting attempt.

### Re-routing to a different address

1. Create a record in `DE.ALTERNATE` (same level as the DE.PRODUCT that was read; ends with carrier sequence).
2. Set the new `CARRIER.ADDR.NO`, `LANGUAGE`, `FORMAT`, `COPIES` as needed.
3. In `DE.O.HEADER`, set `MSG.DISPOSITION = REROUTE` and authorise.

---

## Reference: Key Files

### jBC Source Files

| File | Purpose |
|------|---------|
| `<PKG>.DE.FT.DETAILS.b` | FT handoff routine (full implementation) |
| `<PKG>.DE.TT.DETAILS.b` | TT (Teller) handoff routine |
| `<PKG>.DE.AA.DETAILS.b` | AA handoff stub (to be implemented) |
| `<PKG>.DE.PRINT.INTERFACE.b` | DE carrier — calls Docupilot |
| `<PKG>.DE.DOCU.PROCESS.API.b` | CALLJ wrapper for Docupilot Java |
| `<PKG>.DE.EVENT.MAPPING.b` | Event mapping table template definition |
| `<PKG>.DE.EVENT.MAPPING.FIELDS.b` | Event mapping field definitions |
| `<PKG>.DE.DOCU.RESPONSE.b` | Audit log table template definition |
| `<PKG>.DE.DOCU.RESPONSE.FIELDS.b` | Audit log field definitions |
| `<PKG>.GATEWAY.PARAM.b` | Gateway credentials table |
| `<PKG>.GET.ACC12.USDINWARD.b` | Example document FUNCTION (ACC12) |
| `<PKG>.GET.ACC14.INWARD.b` | Example document FUNCTION (ACC14) |
| `<PKG>.LocalDevelopments.component` | Component registration for all methods/endpoints |

### Skill Reference Files

| File | When to use |
|------|------------|
| `references/de-code-patterns.md` | Copy-paste templates for handoff routines and document FUNCTIONs |
| `references/de-arrays.md` | Array.5 position tables (FT DR/CR, TT), HANDOFF row structure |
| `references/de-applications.md` | T24 application field descriptions, `$USING` equates |
| `references/de-workflows.md` | Firing flow, queue file names, pipeline stages, repair/soft delivery/inward |
