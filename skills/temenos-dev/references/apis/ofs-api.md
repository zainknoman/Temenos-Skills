# OFS API Reference

> OFS (Open Financial Services) is Temenos's programmatic transaction interface — TAFC/jBC based, not Java.
> Sources: JAR analysis of the 2050 distribution; Temenos Education Centre PDF learning materials (OFS User Guide, UsingOFS, OFS Message Format, OFSML 1.5, T24 Technical OFS).

---

## OFS Overview

OFS allows any jBC code or external system to create, amend, authorise, or delete T24 records by building and submitting OFS messages without opening a screen session. The canonical jBC call is:

```basic
CALL OFS.GLOBUS.MANAGER(OFS.SOURCE.ID, OFS.MSG)
```

- `OFS.SOURCE.ID` — registered OFS source (defined in OFS.SOURCE application), e.g. `'OFS.LOAD'`, `'CHGOFS'`
- `OFS.MSG` — on input: the OFS request string; on return: the response string

> **IMPORTANT**: When calling OFS from within jBC API code (version routines, hooks), do NOT call `OFS.GLOBUS.MANAGER`, `OFS.REQUEST.MANAGER`, or `OFS.PROCESSOR.MANAGER` directly — these are internal routines and will corrupt transaction boundaries. Use `OFS.POST.MESSAGE` instead. See the dedicated section below.

OFS is the single point of entry to T24. Every interaction with T24 is driven through OFS. It offers the following distinct request types:
- Transactions (I / A / D / R / P)
- Enquiries (`ENQUIRY.SELECT`)
- Clearing (`CLEARING`)
- XML Report requests (`XML.REPORT`)
- TEC OFS Interface (`TEC.OFS.INTERFACE`)

---

## Message Format

### Request Structure

```
APPLICATION,FUNCTION/SESSION.TOKEN/RECORD.ID/ADDITIONAL.DATA/
FIELD.1:::VALUE.1/
FIELD.2:::VALUE.2/
MULTI.VALUE.FIELD:1:::MV1/
MULTI.VALUE.FIELD:2:::MV2/
SUB.VALUE.FIELD:1:1:::SV1/
```

The full canonical structure is:

```
OPERATION, OPTIONS, USER INFORMATION, ID INFORMATION, DATA
```

Each section is comma-delimited.

### Field Position Syntax

| Syntax | Meaning |
|--------|---------|
| `FIELD.NAME:::VALUE` | Simple field |
| `FIELD.NAME:1:::VALUE` | First multi-value |
| `FIELD.NAME:2:::VALUE` | Second multi-value |
| `FIELD.NAME:1:1:::VALUE` | First sub-value of first multi-value |
| `FIELD.NAME:2:3:::VALUE` | Third sub-value of second multi-value |

In the OFS User Guide (`.txt`) format (using `=` as separator instead of `:::`):

```
FieldName:MultiValueNumber:SubValueNumber=Content
```

Both `:::` and `=` are accepted separators depending on OFS source `SYNTAX.TYPE`.

### Transaction Function Codes

| Code | Meaning |
|------|---------|
| `I` | Input (create/amend — routes to INAU) |
| `A` | Authorise (moves from $NAU to live) |
| `IA` | Input and Authorise in one step (single-authoriser) |
| `R` | Reverse |
| `D` | Delete |
| `P` | Print |
| `V` | See/View (use with caution — may trigger long-running processes) |
| `S` | See (retrieve a specific record) |

### OPTIONS Field Detail

The OPTIONS section of a transaction request has the format:

```
VERSION-NAME/FUNCTION/PROCESS.TYPE/GTS.CONTROL/NO.OF.AUTHORISERS
```

Example: `TRG/I/VALIDATE/1/2`

| Element | Description |
|---------|-------------|
| VERSION-NAME | Optional — uses default version if omitted |
| FUNCTION | I, A, R, D, P, V — defaults to `I` if blank |
| PROCESS.TYPE | `PROCESS` (commit) or `VALIDATE` (dry-run, no DB update) — defaults to `PROCESS` |
| GTS.CONTROL | Override/error handling policy — see GTS.CONTROL table below |
| NO.OF.AUTHORISERS | Number of authorisers required |

### GTS.CONTROL Values

Controls what OFS does when it encounters errors or override conditions:

| Value | On Error | On Override |
|-------|----------|-------------|
| null | Reject record, return error response | Approve automatically and commit |
| 1 | Write to $NAU with status HOLD | Approve automatically and commit |
| 2 | Reject record, return error response | Write to $NAU with status HOLD |
| 3 | Write to $NAU with status HOLD | Write to $NAU with status HOLD |
| 4 | Write ALL transactions to $NAU with status HOLD | Write ALL transactions to $NAU with status HOLD |

### NAU.PROCESSING Values

The `NAU.PROCESSING` field on VERSION controls what happens when an NAU ($NAU) record already exists for the transaction being processed:

| Value | Applies To | Behaviour |
|-------|------------|-----------|
| 0 | Input and Reversals | Reject — cannot update existing NAU record |
| 1 | Input only | Overwrite the existing NAU record with new values |
| 2 | Reversals only | Delete NAU record and reverse the live record |
| 3 | Input and Reversals | Combines option 1 and option 2 |

### USER INFORMATION Field

```
USER.NAME/PASSWORD/COMPANY
```

Company is optional. If omitted, the default company for the user is used.

A special `Replace` flag can be appended to clear and re-input multi-value sets:

```
TEST.USER/654321/GB0010001///1
```

---

## OFS Response Format

The response is returned in `OFS.MSG` after the call:

```
RECORD.ID/MESSAGE.ID/SUCCESS.INDICATOR,RESPONSE.DATA
```

| Part | How to extract (jBC) |
|------|---------------------|
| Status (`0`=error, `1`=success) | `FIELD(FIELD(OFS.MSG,'/',3),',',1)` |
| Record ID | `OFS.MSG[1,13]` or `FIELD(OFS.MSG,'/',1)` |
| Error text | `FIELD(OFS.MSG,'/',4)` when status=0 |
| Override text | Status `3` means override required |

### Status Codes

| Status | Meaning |
|--------|---------|
| 1 | Successful transaction |
| -1 | Error encountered during processing |
| -2 | Override condition encountered |
| -3 | System offline |
| 5 | Record in unauthorised queue (IA not used) |

A successfully processed update returns the fully populated record as a repeating comma-separated string:

```
FieldName:MultiValueNumber:SubValueNumber=Content,...
```

A transaction with errors returns the fields in error:

```
FieldName:MultiValueNumber:SubValueNumber=ErrorMessage,...
```

---

## OFS.POST.MESSAGE (Preferred API for Code)

**Do not call `OFS.GLOBUS.MANAGER`, `OFS.REQUEST.MANAGER`, or `OFS.PROCESSOR.MANAGER` directly from API code.** These are internal routines that do not form part of the T24 public API. Calling them directly will **corrupt transaction boundaries**.

Instead, use `OFS.POST.MESSAGE`:

```basic
CALL OFS.POST.MESSAGE(OFS.SOURCE.ID, OFS.MESSAGES, QUEUE.KEY)
```

- `OFS.SOURCE.ID` — the OFS.SOURCE record to use
- `OFS.MESSAGES` — one or many OFS messages (multiple messages delimited by a Value Mark, `@VM`)
- `QUEUE.KEY` — on return: the key to the `OFS.MESSAGE.QUEUE` table entry

### How OFS.POST.MESSAGE Works

1. Writes the request to `OFS.MESSAGE.QUEUE` (the trigger table for `OFS.MESSAGE.SERVICE`).
2. `OFS.MESSAGE.SERVICE` (TSA service) picks up the message and processes it via `OFS.PROCESS.MANAGER`.
3. On completion, the record is removed from `OFS.MESSAGE.QUEUE` and posted to `OFS.RESPONSE.QUEUE` with the same key — first field is the success/fail flag, second field is the OFS response.
4. A second service, `OFS.RESPONSE.QUEUE`, purges the response queue according to minutes set in `ATTRIBUTE.VALUE` on the `TSA.SERVICE` record.

### TSA Services Required

Both of the following TSA services must be running (set `SERVICE.CONTROL` to `AUTO`):

| Service | Purpose |
|---------|---------|
| `OFS.MESSAGE.SERVICE` | Picks up and processes messages from `OFS.MESSAGE.QUEUE` |
| `OFS.RESPONSE.QUEUE` | Purges `OFS.RESPONSE.QUEUE` after `ATTRIBUTE.VALUE` minutes |

The TSM service must also be running.

---

## Bulk OFS / Local Requests API

For submitting multiple OFS requests within the same BEFORE.AUTH.RTN context, use the Local OFS API so that all sub-transactions are part of the same bulk transaction scope.

### Required Insert

```basic
$INSERT I_OFS.LOCAL.PROCESS.COMMON
```

This insert provides:
- `OFS$LOCAL.QUEUE.PROCESS` — the queue variable that collects local OFS requests
- `OFS$PARENT.ID` — the parent transaction ID

### API Methods

```basic
* Add a request to the local OFS bulk queue
CALL ofs.addLocalRequest(ofsRequest, insertOrAppend, error)

* Check if the bulk process has any errors
CALL ofs.isTxnSuccessful(status)

* Check if the local queue exists
CALL ofs.localRequestExists(queueAvailable)

* Initialize local OFS request variables
CALL ofs.initLocalRequest
```

| Method | Parameters | Description |
|--------|-----------|-------------|
| `ofs.addLocalRequest` | `ofsRequest` — OFS message string; `insertOrAppend` — `INSERT` or `APPEND`; `error` — error output | Adds an OFS request to the bulk transaction queue |
| `ofs.isTxnSuccessful` | `status` — status output | Returns whether the bulk process completed without errors |
| `ofs.localRequestExists` | `queueAvailable` — boolean output | Checks if a local OFS queue exists for the current context |
| `ofs.initLocalRequest` | none | Initialises the local OFS request variables |

### Usage Pattern (BEFORE.AUTH.RTN)

```basic
SUBROUTINE MY.BEFORE.AUTH.RTN

    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_OFS.LOCAL.PROCESS.COMMON

    CALL ofs.initLocalRequest

    * Build your OFS message
    ofsRequest  = 'FUNDS.TRANSFER,CUSTOMER.TRANSFER//'
    ofsRequest := 'DEBIT.ACCT.NO:::' : debitAccount : '/'
    ofsRequest := 'CREDIT.ACCT.NO:::' : creditAccount : '/'
    ofsRequest := 'DEBIT.AMOUNT:::' : amount : '/'
    ofsRequest := 'DEBIT.CURRENCY:::' : currency : '/'

    error = ''
    CALL ofs.addLocalRequest(ofsRequest, 'APPEND', error)

    IF error NE '' THEN
        * Handle error
    END

END
```

### Bulk OFS Constraints

The local/bulk OFS mechanism has the following limitations:

- Only vanilla OFS messages — no XML (`OFSML`) or SOAP format
- Only `I`, `A`, `D`, `R` functions are supported (no `ENQUIRY.SELECT`)
- Cannot include `ENQUIRY.SELECT` requests in a bulk queue
- All messages in the queue share the same transaction boundary

---

## OFS Enquiry Request Syntax

To run an enquiry via OFS, use `ENQUIRY.SELECT` as the operation:

```
ENQUIRY.SELECT,,USER.NAME/PASSWORD,ENQUIRY-NAME,CRITERIA
```

### Components

| Part | Description |
|------|-------------|
| `ENQUIRY.SELECT` | Fixed operation keyword |
| OPTIONS | Always empty for enquiries |
| USER INFORMATION | `USER.NAME/PASSWORD/COMPANY` |
| ID INFORMATION | The enquiry ID (e.g. `CURRENCY-LIST`, `%ACCOUNT`) |
| DATA | Selection criteria — optional |

### Selection Criteria Format

```
SELECTION.FIELD:OPERAND=CRITERIA
```

| Operand | Meaning |
|---------|---------|
| `EQ` | Equal |
| `NE` | Not equal |
| `GE` | Greater than or equal |
| `GT` | Greater than |
| `LE` | Less than or equal |
| `LT` | Less than |
| `LK` | Like (pattern match) |
| `UL` | Unlike |
| `NR` | Not required |

### Enquiry Examples

```
* Run a named enquiry without criteria
ENQUIRY.SELECT,,TEST.USER/654321,CURRENCY-LIST

* Run with a LIKE filter
ENQUIRY.SELECT,,TEST.USER/654321,CURRENCY-LIST,@ID:LK=C...

* Run with equality filter
ENQUIRY.SELECT,,INPUTT/123456,ACCT.BAL.TODAY,ACCOUNT.NUMBER:EQ=29987

* Run a % enquiry (list all accounts)
ENQUIRY.SELECT,,INPUTT/123456,%ACCOUNT

* Run with criteria
ENQUIRY.SELECT,,INPUTT/123456,%ACCOUNT,ACCOUNT.NUMBER:EQ=118737
```

### Enquiry Response Format

```
HEADER.CAPTION.DETAILS,COLUMN.DETAILS,RESPONSE.DATA
```

Example:

```
,@ID::Key/CCY.NAME::Name,"CAD"  "CANADIAN DOLLAR","CHF" "SWISS FRANCS"
```

- **Header Caption Details**: `Identifier=Text/Identifier=Text` — repeated series delimited by `/`
- **Column Details**: `Identifier:FormatType:Label/...` — format types include `DATE` and `AMOUNT`
- **Response Data**: columns delimited by TAB (ASCII 9), rows delimited by `,`

> **Note**: `ENQUIRY.SELECT` cannot be used inside the bulk/local OFS queue (`ofs.addLocalRequest`).

---

## Common OFS Patterns

### Create a FUNDS.TRANSFER

```basic
SUBROUTINE MY.OFS.FT.ROUTINE

    $INSERT I_COMMON
    $INSERT I_EQUATE

    GOSUB INIT
    GOSUB BUILD.FT
    GOSUB SUBMIT.OFS

INIT:
    OFS.SOURCE.ID = 'OFS.LOAD'
    OFS.MSG       = ''
    RETURN

BUILD.FT:
    OFS.MSG  = 'FUNDS.TRANSFER,CUSTOMER.TRANSFER//'
    OFS.MSG := 'DEBIT.ACCT.NO:::' : DEBIT.ACCOUNT : '/'
    OFS.MSG := 'CREDIT.ACCT.NO:::' : CREDIT.ACCOUNT : '/'
    OFS.MSG := 'DEBIT.AMOUNT:::' : AMOUNT : '/'
    OFS.MSG := 'DEBIT.CURRENCY:::' : CURRENCY : '/'
    OFS.MSG := 'DEBIT.VALUE.DATE:::' : VALUE.DATE : '/'
    OFS.MSG := 'PAYMENT.DETAILS:1:::' : NARRATIVE : '/'
    RETURN

SUBMIT.OFS:
    CALL OFS.GLOBUS.MANAGER(OFS.SOURCE.ID, OFS.MSG)

    OFS.STAT = FIELD(FIELD(OFS.MSG,'/',3),',',1)
    IF OFS.STAT EQ 1 THEN
        TXN.ID = FIELD(OFS.MSG,'/',1)
    END ELSE
        ERR.TEXT = FIELD(OFS.MSG,'/',4)
    END
    RETURN
END
```

### Authorise a Record

```basic
* Authorise an existing INAU record
OFS.MSG  = 'FUNDS.TRANSFER,OFS.AUTH/A//' : FT.ID : '/'
CALL OFS.GLOBUS.MANAGER(OFS.SOURCE.ID, OFS.MSG)
```

### Reverse a FUNDS.TRANSFER

```basic
* Build OFS reverse message
OFS.MSG  = 'FUNDS.TRANSFER,PK.REV/R/PROCESS,/' : FT.ID
CALL OFS.GLOBUS.MANAGER(OFS.SOURCE.ID, OFS.MSG)

OFS.STAT = FIELD(FIELD(OFS.MSG,'/',3),',',1)
IF OFS.STAT EQ 1 THEN
    CRT 'Reversed: ' : FT.ID
END
```

### Create an AA Arrangement via OFS

```basic
OFS.MSG  = 'AA.ARRANGEMENT.ACTIVITY,LENDING.NEW//'
OFS.MSG := 'PRODUCT:::' : PRODUCT.ID : '/'
OFS.MSG := 'CUSTOMER:1:::' : CUST.NO : '/'
OFS.MSG := 'CURRENCY:::' : CURRENCY : '/'
OFS.MSG := 'EFFECTIVE.DATE:::' : TODAY : '/'
OFS.MSG := 'TERM:::12M/'
CALL OFS.GLOBUS.MANAGER('OFS.LOAD', OFS.MSG)
```

### Create CUSTOMER via OFS

```basic
OFS.MSG  = 'CUSTOMER,CUSTOMER.OPEN//'
OFS.MSG := 'SHORT.NAME:1:::' : CUST.NAME : '/'
OFS.MSG := 'NAME.1:::' : FULL.NAME : '/'
OFS.MSG := 'SECTOR:::1001/'
OFS.MSG := 'NATIONALITY:::US/'
CALL OFS.GLOBUS.MANAGER('OFS.LOAD', OFS.MSG)
CUST.NO = FIELD(OFS.MSG,'/',1)
```

### Remove a Multi-Value

To remove a multi-value or sub-value, enter a minus sign (`-`) in the field data for the first field of the set:

```basic
* Remove the 2nd multi-value of RELATION.CODE
OFS.MSG = 'CUSTOMER,/I/PROCESS//0,INPUTT/123456,100424,RELATION.CODE:2:1=-'
```

> Use `NULL` to blank a non-multi-value field entirely, but never to remove multi-value entries.

---

## OFS.SOURCE Application

The OFS source controls security and transaction routing. Common sources:

| Source ID | Purpose |
|-----------|---------|
| `OFS.LOAD` | Standard internal OFS — bypasses some validations |
| `CHGOFS` | Batch/system OFS source |
| `REST.API` | REST-triggered OFS (auto-configured) |
| `TELLER` | Teller-originated OFS |
| `TELNET` | TELNET mode OFS — backend classic mode (`tRun tSS TELNET`) |
| `GENERIC.OFS.PROCESS` | Generic OFS processing source |

### Key OFS.SOURCE Fields

| Field | Purpose |
|-------|---------|
| `@ID` | Unique source identifier |
| `DESCRIPTION` | Human-readable description |
| `SOURCE.TYPE` | `BATCH`, `TELNET`, `GLOBUS`, or `SESSION` |
| `LOGIN.ID` | Unix/NT login for automatic communication initiation |
| `EB.PHANT.ID` | `EB.PHANTOM` record for batch processing |
| `MAX.CONNECTIONS` | Maximum concurrent OFS connections |
| `LOG.FILE.DIR` | Directory for OFS log files |
| `LOG.DETAIL.LEVEL` | Logging verbosity — does not affect processing |
| `IN.QUEUE.DIR` | Input directory for batch OFS files |
| `SYNTAX.TYPE` | Message syntax: `GTS` or `OFS` |
| `GENERIC.USER` | T24 user for external access; must have `EB.PHANTOM.PH` authority |
| `IB.USER.CHECK` | Whether to validate external user sign-on; leave null for batch |
| `MAINT.MSG.DET` | Set to `Y` to enable `OFS.REQUEST.DETAIL` message auditing |
| `DET.PREFIX` | Prefix for `OFS.REQUEST.DETAIL` records |
| `AUTO.AUTHORISE` | YES/NO |
| `SUPPRESS.VALIDATION` | Fields to skip validation on |

### Source Types

| Source Type | Processing Mode |
|------------|----------------|
| `BATCH` | Batch mode — directory-based input files |
| `GLOBUS` | Inter-application processing |
| `TELNET` | Online processing via TELNET |
| `SESSION` | Online processing via T24 browser session |

### Blocking an Application from OFS

Add `NOFS` to the `ADDITIONAL.INFO` field of the `PGM.FILE` record for the application to prevent it from being accessed via OFS.

---

## Error Handling Patterns

### Check Status and Log Errors

```basic
CALL OFS.GLOBUS.MANAGER(OFS.SOURCE.ID, OFS.MSG)

OFS.STAT = FIELD(FIELD(OFS.MSG, '/', 3), ',', 1)
BEGIN CASE
    CASE OFS.STAT EQ 1
        * Success
        TXN.ID = FIELD(OFS.MSG, '/', 1)
    CASE OFS.STAT EQ 3
        * Override required — resubmit with override flag
        OFS.OVRD.MSG = OFS.MSG
        * Add override acknowledgement and re-call
    CASE 1
        * Error
        ERR.TEXT = FIELD(OFS.MSG, '-', 2)
        CALL EB.STORE.ERROR(ERR.TEXT, '', '')
END CASE
```

### Retry with Override

```basic
* Append override acknowledgement and resubmit
OFS.MSG = OFS.MSG : 'OVERRIDE:::YES/'
CALL OFS.GLOBUS.MANAGER(OFS.SOURCE.ID, OFS.MSG)
```

### Debugging OFS Issues

When opening an OFS support issue, collect:
- Method of process used: `OFS.POST.MESSAGE`, `OFS.CONNECTION.MANAGER`, `tSS`, `OFS.GLOBUS.MANAGER`, or phantom process
- Error recorded in any `OFSLOG` files
- Application and sample OFS string
- Relevant `OFS.SOURCE` and `EB.PHANTOM` records
- Any local routine involved in creating OFS messages
- Corresponding `OFS.REQUEST.DETAIL` record (enable via `MAINT.MSG.DET=Y` and `DET.PREFIX` in OFS.SOURCE)

---

## Special Characters in OFS

OFS field values containing `:::` or `/` must be escaped. The safest approach is to avoid those characters in field values, or use OFSML for complex data.

| Character | Significance |
|-----------|-------------|
| `/` | Field separator |
| `:::` | Field name/value separator (jBC format) |
| `=` | Field name/value separator (batch/GTS format) |
| `,` | Application/version separator in first token; data field delimiter |
| `:n:` | Multi-value position indicator |
| `:n:m:` | Sub-value position indicator |
| `_` | Leg separator for FX swap transactions (between leg 1 and leg 2) |

### Reserved Characters (Replacement Characters)

These characters are **reserved** in OFS and cannot be used directly in message data:

| Reserved Char | Replacement / Converted To | Notes |
|--------------|---------------------------|-------|
| `?` | `,` (comma) | Use `?` in data where a comma is needed |
| `\|` (pipe) | `"` (double quote) | Use `\|` in data where a double quote is needed |
| `^` (caret) | `/` (forward slash) | Use `^` in data where a forward slash is needed |

Also, do not use `,`, `"`, `/`, `_`, or `//` directly in OFS message data — these have structural meaning.

### Message Wrapping with Tags

To clearly delimit messages (useful for large-batch processing), wrap messages with XML-style tags:

```
<MSG1>ABBREVIATION,INPUTT/******,SEC,ORIGINAL.TEXT=SECTOR</MSG1>
```

The confirmation message returned will also be prefixed and suffixed with the same tags.

---

## Other OFS Request Types

### Clearing Request

```
CLEARING,,TEST.USER/654321,AC.ENTRY.PARAM.ID,DATA
```

- Operation: `CLEARING` — invokes `OFS.CLEARING.MANAGER`
- Options: Optional company code
- ID Information: Key to the `AC.ENTRY.PARAM` record (defines data layout)
- Data: Each entry field separated by the `FIELD.DELIM` from `AC.ENTRY.PARAM`; entries separated by `_`

Example:
```
CLEARING,,TEST.USER/654321,OFS.DEMO,TXNREF1,33537,USD,10000,C,SALARY_TXNREF2,32549,USD,8000,C,SALARY
```

Clearing does not return a response on success; an error response is returned if processing fails.

### XML Report Request

```
XML.REPORT,XML,TEST.USER/654321,REPORT.CONTROL.ID
XML.REPORT,ID,TEST.USER/654321,REPORT.CONTROL.ID
```

- Options: `XML` returns the XML result inline; `ID` returns the `HOLD.CONTROL` key for async retrieval
- Configured via `ENQUIRY.REPORT` with `OUTPUT.FORMAT=XML` and `FORM.NAME=HOLD` in `REPORT.CONTROL`
- Response: `REPORT.ID/MESSAGE.REFERENCE/SUCCESS.INDICATOR/RESPONSE.DATA`

### TEC OFS Interface

```
TEC.OFS.INTERFACE,,TEST.USER/654321,,ITEM.ID,MY.KEY,MY.DETAIL,MY.VALUE
TEC.OFS.INTERFACE,,TEST.USER/654321,,FLUSH
```

Data format: `ITEM.ID,MY.KEY,MY.DETAIL,MY.VALUE` (comma-delimited)

Response: `1,ITEM.ID=API.RESPONSE,KEY=MY.API,DETAIL=VERSION ROUTINE,VALUE=1234`

---

## OFSML — XML Interface

OFSML (OFS Markup Language) is the Temenos XML API for OFS. It is the public XML interface of Temenos Transact for online messaging, supported through the Temenos Open Connectivity Framework (TOCF) components — Temenos Transact Connector or Application Gateway.

OFSML is compliant with W3C XML Schema 1.0. It supports full schema (XSD) validation of both inbound (request) and outbound (response) messages.

### OFSML Namespace

```xml
xmlns="http://www.temenos.com/T24/OFSML/150"
xsi:schemaLocation="http://www.temenos.com/T24/OFSML/150 ofsml15.xsd"
```

### Supported Request Types (OFSML 1.5)

| Category | Request Element | Description |
|----------|----------------|-------------|
| OFSEnquiry | `ofsExtendedEnquiry` | Denormalised OFSML enquiry request |
| OFSEnquiry | `ofsStandardEnquiry` | Standard OFSML enquiry request |
| OFSRoutine | `ofsStandardRoutine` | Request to a standard jBC routine (string output) |
| OFSRoutine | `ofsXMLRoutine` | Request to a routine that accepts/returns XML |
| OFSTransaction | `ofsTransactionInput` | Create or edit a record |
| OFSTransaction | `ofsTransactionAuthorise` | Authorise an unauthorised record |
| OFSTransaction | `ofsTransactionReverse` | Reverse an authorised record |
| OFSTransaction | `ofsTransactionDelete` | Delete an unauthorised record |
| OFSTransaction | `ofsTransactionSee` | View an existing record |
| OFSTransaction | `ofsTransactionHistoryRestore` | Restore a reversed record (new in OFSML 1.5) |

### OFSML Request Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<T24 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="http://www.temenos.com/T24/OFSML/150 ofsml15.xsd"
     xmlns="http://www.temenos.com/T24/OFSML/150">
  <requestProcessing>
    <signatureHandling>NONE</signatureHandling>
    <fireAndForget>NEVER</fireAndForget>
  </requestProcessing>
  <serviceRequest>
    <securityContext encrypt="false">
      <userName>INPUTT</userName>
      <password>654321</password>
    </securityContext>
    <ofsTransactionInput operation="PROCESS" version="" application="ACCOUNT">
      <field name="CUSTOMER">100100</field>
      <field name="CURRENCY">USD</field>
      <field name="CATEGORY">1001</field>
    </ofsTransactionInput>
  </serviceRequest>
</T24>
```

### OFSML Enquiry Request

```xml
<ofsStandardEnquiry name="CURRENCY-LIST"/>
```

### OFSML Response Types

| Category | Response Element | Description |
|----------|-----------------|-------------|
| OFSEnquiryResponse | `ofsExtendedEnquiry` | Denormalised enquiry response |
| OFSEnquiryResponse | `ofsStandardEnquiry` | Standard enquiry response |
| OFSRoutineResponse | `ofsStandardRoutine` | String output from a standard routine |
| OFSRoutineResponse | `ofsXMLRoutine` | XML output from a routine |
| OFSTransactionResponse | `ofsTransactionProcessed` | Processed transaction (check `processingStatus` attribute) |
| OFSTransactionResponse | `ofsTransactionFailed` | Business validation failure — original request + error fields returned |
| OFSTransactionResponse | `ofsTransactionOffline` | Rejected — T24 is in Close of Business cycle |
| OFSTransactionResponse | `ofsTransactionQueued` | Queued for next business cycle |
| OFSTransactionResponse | `ofsTransactions` | List of processed transaction responses |
| OFSFaultResponse | `ofsFault` | Technical error — not a business error |

### OFSML Transaction Response Example

Field values in the response carry `mv` and `sv` attributes:

```xml
<field mv="1" name="RECORD.STATUS" sv="1">INAU</field>
```

### History Restore (OFSML 1.5 Feature)

OFSML 1.5 added support for restoring reversed records:

1. Reverse the live record (`ofsTransactionReverse`) → `processingStatus="NOT-AUTHORISED"`, `RECORD.STATUS=RNAU`
2. Authorise the reversal (`ofsTransactionAuthorise`) → `processingStatus="REVERSED"`, `RECORD.STATUS=REVE`
3. Restore the history (`ofsTransactionHistoryRestore`) → `processingStatus="OK"`, `RECORD.STATUS=HNAU`
4. Authorise the restore (`ofsTransactionAuthorise`) → `processingStatus="OK"`

---

## Other Features

### Multi-Company Processing

OFS supports processing transactions in any company the user has access to. Specify the company in the USER INFORMATION section:

```
TEST.USER/654321/GB0010001
```

### Message Logging

Configurable via `OFS.SOURCE` (`LOG.DETAIL.LEVEL` field). Can log:
- All messages
- Exception messages only
- Communication start and end only
- No messages

Full history stored in `OFS.REQUEST.DETAIL` if message auditing is enabled (`MAINT.MSG.DET=Y`).

### API Hooks

Configured in `OFS.SOURCE`. User routines can be attached at:
- **Communication Start and End** — operations at the start/end of the communication process
- **Individual message receipt and return** — manipulate the message immediately after receipt and before/after return to the calling application
- **Individual message pre and post process** — manipulate the message before processing and on return from processing

### Offline / Store and Forward

If T24 is offline when `OFS.ONLINE.MANAGER` is invoked:
- Enquiry requests return data from the offline cache
- Update requests are stored in a forward queue (`OFS.OFFLINE.QUEUE`)
- `OFS.QUEUE.MANAGER` phantom processes the queue when T24 returns online
- Results written to the outward queue

### Batch Processing

`OFS.QUEUE.MANAGER` runs as a phantom at intervals defined in `EB.PHANTOM`. It reads from the directory set in `IN.QUEUE.DIR` on the `OFS.SOURCE` record. Processing per file:
1. Extract individual messages
2. Call pre-processor routine (if configured)
3. Pass to `OFS.REQUEST.MANAGER`
4. Call post-update routine (if configured)
5. Write output to the output directory

---

## Java Integration — OFS from L3 Java

From Java (RecordLifecycle or ActivityLifecycle), trigger OFS via TransactionData rather than direct OFS call:

```java
// In updateRecord or postCoreTableUpdate:
com.temenos.t24.api.complex.eb.templatehook.TransactionData txnData =
    new com.temenos.t24.api.complex.eb.templatehook.TransactionData();
txnData.setVersionId("FUNDS.TRANSFER,CUSTOMER.TRANSFER");
txnData.setFunction("I");
txnData.setNumberOfAuthoriser("0");
txnData.setTransactionId("");   // leave blank for auto-ID
transactionData.add(txnData);

FundsTransferRecord ftRec = new FundsTransferRecord();
ftRec.setDebitAcctNo(debitAccount);
ftRec.setCreditAcctNo(creditAccount);
currentRecords.add(ftRec.toStructure());
```
