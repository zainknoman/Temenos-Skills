# DE Workflow: Configuration, Firing, and Carrier Stages

## 1. T24 DE Configuration Sequence

To enable DE for a new document type, configure these applications in order:

```
DE.ADDRESS  →  DE.PRODUCT  →  DE.FORMAT  →  DE.MAPPING
                                               ↓
                                    <PKG>.DE.EVENT.MAPPING
                                    (links txn type → DE.MAPPING key)
```

### DE.ADDRESS
Defines where a message goes:
- `DESCRIPTION` — free text label
- `DELIVERY.TYPE` — e.g., `PRINT`, `EMAIL`, `SMS`, `SEC.MSG`
- `PRINT.CARRIER` — for print-type: subroutine called to deliver (e.g., `<PKG>.DE.PRINT.INTERFACE`)
- `EMAIL.ADDRESS` / `SMS.ADDRESS` — for non-print carriers

### DE.PRODUCT
Links format + carrier:
- `DE.FORMAT` — the formatting template record id
- `DE.ADDRESS` — the address record id
- `DELIVERY.CLASS` — `OB` (outbound) or `IB` (inbound)

### DE.FORMAT
Defines the message template/formatter.

### DE.MAPPING
The record ID used as `MapKey` in `DE.API.ApplicationHandoff`:
- `MAP.DESCRIPTION` — description
- `DE.PRODUCT` — linked product
- `DELIVERY.CLASS` — `OB` or `IB`

---

## 2. `<PKG>.DE.EVENT.MAPPING` Table

This is the project-specific bridge between a T24 transaction type code and one or more `DE.MAPPING` keys.

**Record ID** = the transaction type code (e.g., `FT.OWN.ACC` for FT).

### Field Layout (from `<PKG>.DE.EVENT.MAPPING.FIELDS`)

```
@ID             — transaction type code
LL.DESCRIPTION  — free text description
DR.DE.MAPPING   — multi-value: DE.MAPPING key(s) for DR side
  DR.CATEGORY   — sub-value per DR.DE.MAPPING: account category filter
  DR.DOC.CODE   — sub-value: document code sent to Docupilot
  DR.USER.REF   — sub-value: user reference
  DR.PARAM.CODE — sub-value: parameter code sent to Docupilot
CR.DE.MAPPING   — multi-value: DE.MAPPING key(s) for CR side
  CR.CATEGORY   — sub-value per CR.DE.MAPPING: account category filter
  CR.DOC.CODE   — sub-value: document code
  CR.USER.REF   — sub-value: user reference
  CR.PARAM.CODE — sub-value: parameter code
LOCAL.REF       — local reference (optional)
```

**Field notation in FIELDS routine:**
- `XX<FIELDNAME` — multi-value (linked to previous `<` field)
- `XX-XX.SUBFIELD` — sub-value (child of multi-value above)
- `XX>FIELDNAME` — sub-multi-value

### Category Filter Logic

In the handoff routine, only fire DE if the account's category matches the configured filter:
```jBC
IF INDEX(DrCategory, debitAccountCategory, 1) THEN
    ;* populate Array.5 and call ApplicationHandoff
END
```
`DrCategory` can be a space-delimited list of valid categories.

---

## 3. DE Firing Flow (Outward)

```
T24 transaction AUTHORISE
        ↓
Version routine / AA Activity Hook calls handoff routine
<PKG>.DE.FT.DETAILS / <PKG>.DE.TT.DETAILS / <PKG>.DE.AA.DETAILS
        ↓
Read <PKG>.DE.EVENT.MAPPING by transaction type
        ↓
For each DR/CR mapping key:
  - Filter by account category
  - Populate Array.5
  - DE.API.ApplicationHandoff(Rec1..Rec9, MapKey, VKey, ErrorMsg)
        ↓
VKey = DE message reference (stored in DeliveryOutref)
        ↓
DE framework fires <PKG>.DE.PRINT.INTERFACE (the carrier)
        ↓
<PKG>.DE.PRINT.INTERFACE:
  1. Read <PKG>.GATEWAY.PARAM 'DOCUPILOT' for credentials
  2. Extract documentCode, userReference, parameterCode from deliveryPackage
  3. Extract TRANS.REF (=DE message ID) from deliveryPackage
  4. Build JSON payload
  5. Call <PKG>.DE.DOCU.PROCESS.API → CALLJ to Java Docupilot client
  6. Log request/response
  7. Write audit to <PKG>.DE.DOCU.RESPONSE
```

---

## 4. Delivery Package Fields

When `<PKG>.DE.PRINT.INTERFACE` is called by the DE framework, `deliveryPackage` is a field-mark-delimited string. Keys are located with `FINDSTR`:

```jBC
FINDSTR 'documentCode'  IN deliveryPackage SETTING pos THEN documentCode  = deliveryPackage<pos+1>
FINDSTR 'userReference' IN deliveryPackage SETTING pos THEN userReference = deliveryPackage<pos+1>
FINDSTR 'parameterCode' IN deliveryPackage SETTING pos THEN parameterCode = deliveryPackage<pos+1>
FINDSTR 'TRANS.REF'     IN deliveryPackage SETTING pos THEN transactionId = deliveryPackage<pos+1>
```

`genericData` (parameter 3) carries the full DE message ID in `FIELD(genericData,@FM,1)`.

---

## 5. Docupilot JSON Payload Format

```json
{
  "documentCode": "<doc code>",
  "userReferenceId": "<user ref>",
  "parameters": [
    { "code": "<param code>", "value": "<transaction id>" }
  ]
}
```

Full payload sent to Java: `username|password|tokenUrl|endpointUrl|{json}` (pipe-delimited).

---

## 6. EB.API Configuration for Java Bridge

The Java class is configured in `EB.API` table, record `<PKG>.DOCUPILOT.CLIENT`:

| Field | Meaning |
|-------|---------|
| `EB.SystemTables.Api.ApiJavaClass` | Java class name |
| `EB.SystemTables.Api.ApiJavaMethod` | Java method to invoke |
| `EB.SystemTables.Api.ApiJavaPackage` | Java package name |

Called via:
```jBC
CALLJ fullClassName, methodName, fullPayload SETTING theResponse ON ERROR
    errorMsg = SYSTEM(0)
END
```

CALLJ error codes: 1=JVM thread, 2=JVM DLL missing, 3=class not found, 4=Unicode error, 5=method not found, 6=constructor missing, 7=instantiation failed.

---

## 7. T24 Classic DE Pipeline (Outward)

Understanding the three lifecycle stages helps troubleshoot DE issues:

### Stage 1 — Mapping (automatic, on authorise)
1. T24 application calls `APPLICATION.HANDOFF` with 9 data arrays + MapKey.
2. Values written to `F.DE.O.HANDOFF` (10-row dimensioned array; row 9 = user-defined; row 10 = reserved).
3. Row 0 positions hardcoded: `0.0=DELIVERY.KEY`, `0.1=MAPPING.KEY`, `0.2=BANK.DATE`.
4. `DE.O.MAP.MESSAGE` maps HANDOFF positions → DE.MESSAGE variables using DE.MAPPING record.
5. `DE.DETERMINE.CARRIER` reads DE.ROUTING → DE.PRODUCT (most specific match) → DE.ADDRESS.
6. `DE.O.HEADER` record created with initial status `UNFORMATTED`.
7. Delivery ID written to activation file: `F.PRINT.OUT.LIST` (print) or `F.SWIFT.OUT.LIST` (SWIFT) or `F.EMAIL.OUT.LIST` / `F.SMS.OUT.LIST` / `F.SECUREMSG.OUT.LIST`.
8. Actual unformatted message written to `F.DE.O.MSG`.
9. Errors → ID written to `F.DE.O.REPAIR`.
10. HOLD → ID written to `F.DE.O.HOLD.KEY`.

**Prerequisite for FT:** `FT.TXN.TYPE.CONDITION` record for the transaction type must have `DR.ADVICE.REQD=Y` and `CR.ADVICE.REQD=Y`.

### Stage 2 — Formatting (user-started services)

| Service | Runs routine | Reads format app |
|---------|-------------|-----------------|
| `BNK/PRINT.OUT` | `DE.OUTWARD` | `DE.FORMAT.PRINT` |
| `BNK/SWIFT.OUT` | `DE.OUTWARD` | `DE.FORMAT.SWIFT` |
| `BNK/EMAIL.OUT` | `DE.OUTWARD` | `DE.FORMAT.XML` |
| `BNK/SMS.OUT` | `DE.OUTWARD` | `DE.FORMAT.XML` |
| `BNK/SECUREMSG.OUT` | `DE.OUTWARD` | `DE.FORMAT.XML` |

`DE.OUTWARD` flow: read `DE.CARRIER` → determine FORMAT.MODULE → read format record → format advice → write to formatted queue → update DE.O.HEADER to `FORMATTED`.

**Formatted queues:**
| Queue | Contents |
|-------|---------|
| `F.DE.O.PRI.FORMS` | PRINT formatted IDs |
| `F.DE.O.MSG.<FORM.TYPE>` | PRINT formatted messages |
| `F.DE.O.PRI.SWIFT` | SWIFT formatted IDs (no interface) |
| `F.DE.O.MSG.SWIFT` | SWIFT formatted messages (no interface) |
| `F.DE.O.MSG.<INTERFACE>` | Messages for a custom interface |
| `F.DE.O.PRI.EMAIL` | EMAIL formatted IDs |
| `F.DE.O.MSG.EMAIL` | EMAIL formatted messages |
| `F.DE.O.PRI.SMS` | SMS formatted IDs |
| `F.DE.O.MSG.SMS` | SMS formatted messages |
| `F.DE.O.PRI.SECUREMSG` | SECUREMSG formatted IDs |
| `F.DE.O.MSG.SECUREMSG` | SECUREMSG formatted messages |

### Stage 3 — Carrier Control

- **PRINT**: start `XXX/DE.PRINT` → sends to physical printer; on success `MSG.DISPOSITION=ACK`; messages removed from formatted queue
- **SWIFT (no interface)**: start `XXX/SWIFT.OUT`
- **SWIFT (with interface)**: `DE.OUTWARD` invokes the interface routine directly; no extra service needed
- **EMAIL**: `DE.EMAIL.JAVA.INTERFACE` → `EB.API` record `DE.EMAIL.CLIENT` → Java → SMTP server
- **SMS**: `DE.SMS.JAVA.INTERFACE` → `EB.API` record `DE.SMS.CLIENT` → Clickatell SMS gateway
- **SECUREMSG**: `SECURE.MSG.INTERFACE` → OFS string → `F.OFS.MESSAGE.QUEUE` → service `BNK/OFS.MESSAGE.SERVICE` → creates `EB.SECURE.MESSAGE` record

All sent messages stored in `F.DE.SENT.<CARRIER>`; history in `F.DE.O.HISTORY`.

---

## 7a. Complete Queue File Reference

| File | Purpose | Stage |
|------|---------|-------|
| `F.DE.O.HANDOFF` | Raw data arrays from APPLICATION.HANDOFF | Mapping |
| `F.PRINT.OUT.LIST` | Unformatted PRINT advice IDs | Mapping |
| `F.SWIFT.OUT.LIST` | Unformatted SWIFT advice IDs | Mapping |
| `F.EMAIL.OUT.LIST` | Unformatted EMAIL advice IDs | Mapping |
| `F.SMS.OUT.LIST` | Unformatted SMS advice IDs | Mapping |
| `F.SECUREMSG.OUT.LIST` | Unformatted SECUREMSG advice IDs | Mapping |
| `F.DE.O.MSG` | Actual unformatted messages | Mapping |
| `F.DE.O.REPAIR` | Repair queue (failed mapping or formatting) | All |
| `F.DE.O.HOLD.KEY` | Messages placed on HOLD | Mapping |
| `F.DE.O.PRI.FORMS` | Formatted PRINT IDs | Formatting |
| `F.DE.O.MSG.<FORM.TYPE>` | Formatted PRINT messages | Formatting |
| `F.DE.O.PRI.SWIFT` | Formatted SWIFT IDs | Formatting |
| `F.DE.O.MSG.SWIFT` | Formatted SWIFT messages | Formatting |
| `F.DE.O.MSG.<INTERFACE>` | Formatted messages for interface | Formatting |
| `F.DE.SENT.<CARRIER>` | Successfully sent messages | Carrier |
| `F.DE.O.HISTORY` | All formatted advices ever sent | Carrier |
| `F.CUSTOMER.HOLD` | Messages held for customer (HOLD.OUTPUT=Y) | Carrier |
| `F.SWIFT.IN.LIST` | Inward SWIFT IDs (unformatted) | Inward |
| `F.DE.I.MSG` | Inward unformatted messages | Inward |
| `F.DE.I.MSG.<APP.QUEUE>` | Inward messages for specific application | Inward |
| `F.DE.XML.SCHEMA` | XML schema definitions (XSD) for XML format records | Formatting |
| `F.OFS.MESSAGE.QUEUE` | OFS strings for SECUREMSG processing | Carrier |
| `F.OFS.RESPONSE.QUEUE` | Responses from OFS.MESSAGE.SERVICE | Carrier |

---

## 7b. Repair and Resubmit

**Repair** occurs when:
- A mandatory DE.MESSAGE variable has no value in HANDOFF
- DE.FORMAT.PRINT/SWIFT record missing
- Page overflow on a NO-overflow field

**To resubmit** after fixing the root cause:
1. Fix the underlying config (e.g., add missing DE.FORMAT.PRINT record).
2. Open the `DE.O.HEADER` record for the delivery ID.
3. Set `DISPOSITION` to `Resubmit` and authorise.
4. Advice moves from `F.DE.O.REPAIR` back to unformatted queue; original error preserved in history.

**MSG.DISPOSITION REROUTE** (temporary address change):
1. Create record in `DE.ALTERNATE` (ID mirrors DE.PRODUCT level, ends with carrier sequence).
2. In `DE.O.HEADER` set `MSG.DISPOSITION=REROUTE`; system reads DE.ALTERNATE for new carrier/address/language/format/copies.

**DE.DISP.CONTROL** (automatic rule-based disposition):
- Numeric ID records evaluated in order at Mapping stage.
- Multiple conditions within same record joined by AND.
- First matching record wins (order by numeric ID = importance order).
- `STATUS` values: `HOLD`, `DELETE`, `WAIT HH:MM`, `REROUTE`, `RESUBMIT`, `RELEASE`, `PRINT`.
- Service `BNK/DE.DISP.TIMECHECK` releases timed holds (`HOLD 21:30` or `WAIT 06:00`).

Viewing mapped data: enquiry `DE.HANDOFF.DETS` (select by DELIVERY.REF).

---

## 7c. Soft Delivery (AA, LC, BL, MD, SW)

Soft delivery allows choosing advice type per activity/message-class combination.

| Application | Purpose |
|-------------|---------|
| `EB.ACTIVITY` | Pre-configured activity codes per module; ID = `<App>-<4digitCode>` e.g. `LC-2801` |
| `EB.MESSAGE.CLASS` | Generic names for application-specific message classes; links param table → EB.ADVICES |
| `EB.ADVICES` | For each activity code: lists message types, message classes, mapping keys, print formats to produce; ID same as EB.ACTIVITY |

`EB.ADVICES` key fields:
| Field | Notes |
|-------|-------|
| `MESSAGE.TYPE` | DE.MESSAGE ID to use |
| `MSG.CLASS` | EB.MESSAGE.CLASS record ID |
| `MAPPING.KEY` | DE.MAPPING record ID |
| `PRINT.FORMAT` | APPLICATION.FORMAT component of DE.FORMAT.PRINT ID |
| `EXTRA.ADVICE` | ID of another EB.ADVICES record to also read (additional advices) |
| `USE.RECORD` | ID of another EB.ADVICES record to read INSTEAD (alternative advices) |
| `DEAL.SLIP` | DEAL.SLIP.FORMAT record ID for deal slip generation |

Soft delivery flow: application logic calls `EB.HANDOFF(activityCode, messageClass)` → reads EB.ADVICES → for each matching advice calls `APPLICATION.HANDOFF` → same pipeline as hard delivery from that point.

Preview functionality: requires `ADDITIONAL.INFO=.PREVIEW` in PGM.FILE for the application → enquiry `DE.PREVIEW` → temporary message in `F.DE.PREVIEW.MSG`.

---

## 8. T24 Classic Inward SWIFT Flow

1. External interface → TCServer (appends `DECARRIER=SWIFT` prefix) → spawns tSS process.
2. `tSS` → `OFS.BULK.MANAGER` → `OFS.PROCESS.MANAGER` (detects `DECARRIER`) → `OFS.DE.REQUEST` → `OFS.DE.PROCESSING`.
3. `OFS.DE.PROCESSING` creates `DE.I.HEADER` record + Delivery Reference ID (starts with `R`).
4. Unformatted ID written to `F.SWIFT.IN.LIST`; unformatted message to `F.DE.I.MSG`.
5. Start service `BNK/SWIFT.IN` → runs `DE.INWARD` multi-threaded:
   a. Read DE.I.HEADER for carrier info.
   b. Call `DE.I.FORMAT.SWIFT.MESSAGE`.
   c. Read DE.MESSAGE by message type → get APPLICATION.QUEUE.
   d. If APPLICATION.QUEUE blank → default to FT; call INWARD.OFS.ROUTINE.
   e. If APPLICATION.QUEUE set → put message in `F.DE.I.MSG.<APP>`, call `<APP>.INWARD`.
   f. Call `OFS.GLOBUS.MANAGER` → creates T24 record in IHLD (hold) status.
6. DE.I.HEADER DISPOSITION updated to `OFS FORMATTED`.

DE.STP.REPAIR.PARM: repair parameters for STP; reverse company-specific record to bypass VIVEO repair in test.

---

## 9. Component File Registration

Every new method must be declared in `<PKG>.LocalDevelopments.component`:

**Handoff routine** (private, no params):
```
private method <pkg>De<App>Details () {
    jBC: <PKG>.DE.<APP>.DETAILS
}
```

**Document FUNCTION** (public REST endpoint):
```
@Response("")
@Path("/get/<endpoint>")
@GET
public method get<Name> : Docupilot:<docStruct>(
    @QueryParam("<paramName>")
    IN <paramName> string
)
{
    jBC: <PKG>.GET.<CATEGORY><NN>.<NAME>
}
```

**AA activity method** (public, with INOUT/OUT params):
```
public method <pkg>DeAaDetails (INOUT handOffRecord string, OUT errorMsg string) {
    jBC: <PKG>.DE.AA.DETAILS
}
```
