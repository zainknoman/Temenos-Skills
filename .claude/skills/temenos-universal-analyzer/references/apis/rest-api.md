# T24 REST API Catalog

> Generated 2026-06-20 — 0 REST endpoint classes detected in analysed JARs.
> This file documents REST API patterns, annotation standards, and known service endpoints.

---

## Why Zero Endpoints Were Detected

T24/Transact REST APIs are implemented through two separate mechanisms:

1. **Temenos Microservices (Transact APIs)** — deployed as standalone services (Spring Boot), not embedded in product JARs. These expose OpenAPI/Swagger endpoints and are not present in the T24 product JAR bytecode.

2. **jBC REST Components** — T24 jBC components annotated with `@GET`/`@POST`/`@Path` expose REST endpoints through the TAFJ runtime servlet. These are jBC FUNCTION routines, not Java classes, so they do not appear in JAR analysis.

---

## REST Architecture in T24/Transact

```
Client (TCIB, Mobile, External)
       |
       | HTTP/JSON
       v
Temenos API Layer (API Gateway / Infinity)
       |
       | Route to appropriate service
       v
   Transact APIs         OR        jBC REST Components
   (Spring Boot)                   (TAFJ servlet)
       |                                   |
       v                                   v
T24 Core (via OFS / DataAccess)     T24 Core (direct jBC call)
```

---

## Transact REST API Services (Microservices)

Key REST services available as separate Transact microservice JARs:

| Service | Base Path | Description |
|---------|-----------|-------------|
| Customer Service | `/customers` | Create, read, update customers |
| Account Service | `/accounts` | Account operations |
| Payment Order | `/paymentOrders` | Payment initiation (TPH) |
| Arrangements | `/arrangements` | AA arrangement operations |
| Holdings | `/holdings` | Portfolio and position data |
| Deposits | `/deposits` | Term deposit operations |
| Lending | `/lending` | Loan lifecycle operations |
| Limits | `/limits` | Credit limit management |
| Party | `/party` | Party/customer data (ISO 20022 aligned) |
| Transactions | `/transactions` | Transaction history |

> Swagger/OpenAPI definitions are in `E:\Learning\API-Collections\bundles\`.

---

## jBC REST Component Pattern

jBC components expose REST endpoints using JAX-RS-style annotations processed by the TAFJ componentization framework.

### GET Endpoint

```basic
$PACKAGE MYBANK.RestApi

FUNCTION MYBANK.REST.GET.ACCOUNT.BALANCE

    $USING EB.API
    $USING EB.SystemTables

*-----------------------------------------------------------------------------
*** <region name= Description>
*** <desc>REST GET endpoint: returns account balance by account number.</desc>
*   Path:    /mybank/account/{accountNumber}/balance
*   Method:  GET
*   Returns: JSON with balance information
*** </region>
*-----------------------------------------------------------------------------
    @GET
    @Path("/mybank/account/{accountNumber}/balance")
    @Produces("application/json")

    ACCOUNT.NO = @PathParam("accountNumber")

    GOSUB GET.BALANCE

    RESPONSE = '{"accountNumber":"' : ACCOUNT.NO : '",'
    RESPONSE := '"balance":"' : BALANCE : '",'
    RESPONSE := '"currency":"' : CURRENCY : '"}'

    MYBANK.REST.GET.ACCOUNT.BALANCE = RESPONSE
    RETURN

GET.BALANCE:
    FN.ACC = 'F.ACCOUNT'
    F.ACC  = ''
    CALL OPF(FN.ACC, F.ACC)
    CALL F.READ(FN.ACC, ACCOUNT.NO, R.ACC, F.ACC, ERR)
    IF NOT(ERR) THEN
        BALANCE  = R.ACC<F.ACCOUNT.WORKING.BALANCE>
        CURRENCY = R.ACC<F.ACCOUNT.CURRENCY>
    END ELSE
        BALANCE  = '0'
        CURRENCY = ''
    END
    RETURN
END
```

### POST Endpoint

```basic
$PACKAGE MYBANK.RestApi

FUNCTION MYBANK.REST.POST.PAYMENT

    $USING EB.API

    @POST
    @Path("/mybank/payments")
    @Consumes("application/json")
    @Produces("application/json")

    * Request body is available via @RequestBody
    REQUEST.BODY = @RequestBody

    * Parse JSON fields
    DEBIT.ACC  = FIELD(FIELD(REQUEST.BODY, '"debitAccount":"', 2), '"', 1)
    CREDIT.ACC = FIELD(FIELD(REQUEST.BODY, '"creditAccount":"', 2), '"', 1)
    AMOUNT     = FIELD(FIELD(REQUEST.BODY, '"amount":"', 2), '"', 1)

    GOSUB SUBMIT.PAYMENT

    MYBANK.REST.POST.PAYMENT = '{"status":"' : STATUS : '","txnId":"' : TXN.ID : '"}'
    RETURN

SUBMIT.PAYMENT:
    OFS.MSG  = 'FUNDS.TRANSFER,CUSTOMER.TRANSFER//'
    OFS.MSG := 'DEBIT.ACCT.NO:::' : DEBIT.ACC : '/'
    OFS.MSG := 'CREDIT.ACCT.NO:::' : CREDIT.ACC : '/'
    OFS.MSG := 'DEBIT.AMOUNT:::' : AMOUNT : '/'
    CALL OFS.GLOBUS.MANAGER('OFS.LOAD', OFS.MSG)

    OFS.STAT = FIELD(FIELD(OFS.MSG,'/',3),',',1)
    IF OFS.STAT EQ 1 THEN
        STATUS = 'SUCCESS'
        TXN.ID = FIELD(OFS.MSG,'/',1)
    END ELSE
        STATUS = 'ERROR'
        TXN.ID = ''
    END
    RETURN
END
```

---

## jBC REST Annotations

| Annotation | Purpose | Example |
|-----------|---------|---------|
| `@GET` | HTTP GET method | `@GET` |
| `@POST` | HTTP POST method | `@POST` |
| `@PUT` | HTTP PUT method | `@PUT` |
| `@DELETE` | HTTP DELETE method | `@DELETE` |
| `@Path` | URL path (supports `{param}`) | `@Path("/accounts/{id}")` |
| `@PathParam` | Bind URL path variable | `ID = @PathParam("id")` |
| `@QueryParam` | Bind URL query parameter | `PAGE = @QueryParam("page")` |
| `@RequestBody` | Bind request body | `BODY = @RequestBody` |
| `@Produces` | Response content type | `@Produces("application/json")` |
| `@Consumes` | Request content type | `@Consumes("application/json")` |
| `@HeaderParam` | Bind request header | `TOKEN = @HeaderParam("Authorization")` |

---

## API Security

REST APIs in T24 are secured via:

| Mechanism | Description |
|-----------|-------------|
| JWT tokens | Bearer token in Authorization header |
| OAuth 2.0 | Client credentials or auth code flow |
| API Gateway | Rate limiting, IP whitelist, API key |
| T24 User Context | REST calls run under a configured T24 user |

Configure the T24 user for REST calls in `OFS.SOURCE` (for OFS-backed REST) or via TAFJ REST configuration.

---

## Swagger / OpenAPI Files

OpenAPI specs for Transact services are at `E:\Learning\API-Collections\`:

| Bundle Path | Service |
|------------|---------|
| `bundles/accountServices/` | Account services API |
| `bundles/creditLimits/` | Credit limit services API |

---

## Known REST Endpoint Patterns

### Customer API

```
GET    /customers/{customerId}              — Read customer
POST   /customers                          — Create customer
PUT    /customers/{customerId}             — Amend customer
GET    /customers/{customerId}/accounts    — Customer's accounts
GET    /customers/{customerId}/arrangements — Customer's arrangements
```

### Account API

```
GET    /accounts/{accountId}               — Read account
GET    /accounts/{accountId}/balances      — Account balances
GET    /accounts/{accountId}/transactions  — Transaction history
POST   /accounts                           — Open account (AA)
```

### Payment API (TPH)

```
POST   /paymentOrders                      — Initiate payment
GET    /paymentOrders/{orderId}            — Payment status
DELETE /paymentOrders/{orderId}            — Cancel payment
GET    /paymentOrders/{orderId}/messages   — Payment messages
```

### Arrangement API (AA)

```
POST   /arrangements                       — Open arrangement
GET    /arrangements/{arrangementId}       — Read arrangement
PUT    /arrangements/{arrangementId}/activities — Post activity
GET    /arrangements/{arrangementId}/balances   — Balances
GET    /arrangements/{arrangementId}/schedule   — Payment schedule
```

---

## Application Customisation APIs (jBC Hook Points)

These are customisation APIs defined in T24 application parameter records. They allow local jBC subroutines to be invoked at specific processing points.

### VERSION — Field-Level Hook Points

The VERSION application allows user-defined subroutines in four fields:

| Field | Invoked From | When | Purpose |
|-------|-------------|------|---------|
| `AUT.NEW.CONTENT` | `RECORD.READ` with functions I, C, H, V | On record read | Conditional defaulting from related files; modify `R.NEW` before display |
| `VALIDATION.RTN` | `VERSION.VALIDATION` | At field input validation and cross-validation | Field-level validation and defaulting; uses `COMI`, `COMI.ENRI`, `ETEXT` variables |
| `INPUT.ROUTINE` | `UNAUTH.RECORD.WRITE` | After cross-validation, before unauthorised write | Update local files, additional checking; called after `CROSS.VALIDATION` and before `BEFORE.UNAU.WRITE` |
| `AUTH.ROUTINE` | `AUTH.RECORD.WRITE` | After `BEFORE.AUTH.WRITE` | Update local files at authorisation stage; no error handling at this point |

**Key variables in VALIDATION.RTN:**

| Variable | Description |
|----------|-------------|
| `COMI` | Current value of the VALIDATION.FLD — use this, not `R.NEW` |
| `COMI.ENRI` | Enrichment for COMI |
| `DISPLAY` | Formatted version of COMI |
| `ETEXT` | Populate with error message when error found |
| `MESSAGE` | `"VAL"` during cross-validation; null during online field checks |

---

### OVERRIDE.CLASS.DETAILS

The `OVERRIDE.CLASS.DETAILS` application allows a subroutine to manipulate override messages, enabling variable sub-classification (for example, converting a foreign currency overdraft amount to local currency before assigning an override class).

**DATA.DEF field:**

| Item | Detail |
|------|--------|
| Format | `@subroutine name(par1,...parn)` — must be defined in `PGM.FILE` as type V; parameters defined in `ADDITIONAL.INFO` as `.PAR(xx,...xx)` |
| Invoked from | `STORE.OVERRIDE` |
| Arguments | `SCAN.TEXT`, `OVERRIDE.VALUE`, `DATA.DEF` |

- `SCAN.TEXT` — the override message as defined in OVERRIDE.CLASS (e.g. `"ACCOUNT and -UNAUTHORISED OVERDRAFT"`)
- `OVERRIDE.VALUE` — `SCAN.TEXT` plus the variable values; return converted value here
- `DATA.DEF` — the parameter definition; return a derived value for the specified element

---

### EB.API — Registering Local Programs

After writing a local subroutine, register it in the `EB.API` application:

| Field | Value |
|-------|-------|
| ID | Name of the BASIC subroutine |
| Description | Subroutine description |
| Protection Level | Security protection level |
| Source Type | `BASIC` |

**Program (ID) field:** For online applications, the key must match the program name. The `TYPE` field indicates the application type:

| Type | Meaning |
|------|---------|
| H, U, L, T, W | File maintenance applications (standard TEMPLATE type) |
| M | Main-line program with no standard file maintenance (conversion program, report); must contain a `SUBROUTINE` statement |

**BATCH.JOB field:** Defines subroutines or jBase commands executed from `BATCH.CONTROL`:
- Format: `@Subroutine name` or jBase VOC command
- Invoked from: `B.INITIATE.PROCESS`
- Multi-valued — several subroutines/commands may be defined sequentially

**BATCH.CONTROL pre-batch APIs:** API calls that can run at the pre-batch stage:

| Prefix | Type |
|--------|------|
| (none) | Subroutine name — must be defined in VOC |
| `SPT` | Script — must be defined in `F.SCRIPT.DESIGNER` |
| `RPT` | Crystal report — must be defined in `F.REPORT.CONTROL` |
| `ENQ` | Enquiry — must be defined in `F.ENQUIRY` |

---

## Reporting / Enquiry Customisation APIs

### ENQUIRY

The ENQUIRY application provides three areas for local routines:

**Conversion routines** — manipulate extracted data:

| Item | Detail |
|------|--------|
| Format | `@ subroutine name` (space between @ and name) |
| Invoked from | `ENQ.BUILD.PAGE` for each item |
| Insert required | `I_ENQUIRY.COMMON` at start of routine |

Key common variables available in conversion routines:

| Variable | Description |
|----------|-------------|
| `ID` | Current record ID being processed |
| `R.RECORD` | The current record being processed |
| `O.DATA` | Current incoming data being processed (also the returned data) |
| `VC` | Current multi-value number being processed |
| `S` | Current sub-value number |
| `VM.COUNT` | Maximum number of multi-values in the current record |
| `SM.COUNT` | Maximum number of sub-values in the current record |

**BUILD.ROUTINE** — manipulates data prior to selection (e.g. builds a work file):

| Item | Detail |
|------|--------|
| Format | Subroutine name (more than one may be specified) |
| Invoked from | `T.ENQUIRY.SELECT` and `S.ENQUIRY.SELECTION` |
| Argument | `ENQ` dynamic array: `ENQ<1>` = enquiry name; `ENQ<2,x>` = selection field names; `ENQ<3,x>` = operands; `ENQ<4,x,y>` = data list |

**External invocation:**
```basic
CALL ENQUIRY.DISPLAY(QQQ)
* QQQ<1>    Enquiry name
* QQQ<2,x>  Selection field names
* QQQ<3,x>  Selection operands
* QQQ<4,x,y> Selection data
* QQQ<9,z>  Sort requirements
* QQQ<10>   Display mode: OUTPUT / null (screen) / P (print)
```

---

### REPGEN.CREATE

The REPGEN utility provides two hook points:

**FL.DECISION.FR** — custom selection subroutine:

| Item | Detail |
|------|--------|
| Format | Subroutine name (enter `SUB` in `FL.DECISION` to signal subroutine) |
| Invoked from | RGS-generated program |
| Argument | `FILENAME` — full filename to be selected |
| Must be defined | In `PGM.FILE` as type S application |

The routine must return an ACTIVE select list for the supplied FILENAME. `REPGEN.SORT` record is available in `R.NEW` with values in `CONSTANTS` fields.

**Modification** — manipulate extracted data:

| Item | Detail |
|------|--------|
| Format | `@ Subroutine name#n` where `#n` is the argument number |
| Invoked from | RGS-generated program |
| Arguments | Par1 through Parn as defined in `PGM.FILE ADDITIONAL.INFO` as `.PAR(xx,...xx)` |
| Must be defined | In `PGM.FILE` as type R routine |

A single value may be returned.

---

### RE.STAT.REQUEST

Allows an alternative print routine instead of the standard `RE.STAT.PRINT` for CRF reports.

**PRINT.ROUTINE field:**

| Item | Detail |
|------|--------|
| Format | Subroutine name |
| Invoked from | `RE.STAT.REQUEST$RUN` |
| Arguments | Report Params, Output Mode, Lang Code, Base Currency |

- `Report Params` — report name; `*D` = detailed, `*B` = both summary and detail
- `Output Mode` — requested output mode
- `Lang Code` — requested language code
- `Base Currency` — requested base currency

---

### CREATE.FICHE.TAPE

Allows definition of a command or routine to create a fiche file.

**TAPE.CREATE field:**

| Item | Detail |
|------|--------|
| Format | Any jBase command or subroutine (UNIX `cat` command is typical) |
| Invoked from | `EXECUTE.COMMAND` |
| Driven from | `F.FICHE.HOLD.CONTROL` |

The command can pass the ID using `&FICHE.HOLD.CONTROL>@ID&`; the routine extracts it via `@SENTENCE[" ",2,1]`.

---

### PRINTER.ID

Allows definition of a command or routine invoked whenever T24 output is directed to that printer ID.

**Command field:**

| Item | Detail |
|------|--------|
| Format | Any jBase command or subroutine |
| Invoked from | `EXECUTE.COMMAND` |
| Driven from | `F.HOLD.CONTROL` |

Example: `LOCAL.PRINT.LOAD &HOLD.CONTROL>@ID&` — extracts ID via `@SENTENCE[" ",2,1]`.

---

## Delivery System APIs

The T24 delivery system provides user-defined routines for message mapping, disposition control, SWIFT processing, and interface routines via the Generic Delivery Interface.

### DE.FORMAT.SWIFT

Allows a subroutine to be called for a particular SWIFT field when processing incoming SWIFT messages.

**INWARD.ROUTINE field:**

| Item | Detail |
|------|--------|
| Format | Enter `Y` in field; subroutine must be named `DE.ICONV.nn` where `nn` is the SWIFT field tag (e.g. `DE.ICONV.61`) |
| Invoked from | `DE.I.FORMAT.SWIFT.MESSAGE` |
| Arguments | `FIELD` (data from SWIFT message), `LINE` (decoded message; components separated by `@FM`) |

Use when a SWIFT field has multiple components that need to be separated and/or converted for correct inward processing.

---

### DE.WORDS

Allows a user routine for a given language to translate numbers to words.

| Item | Detail |
|------|--------|
| Format | Subroutine name |
| Invoked from | `DE.O.FORMAT.PRINT.MESSAGE`, `DE.O.FORMAT.TELEXP.MESSAGE`, `PRODUCE.DEAL.SLIP` |
| Arguments | `IN.AMT`, `OUT.AMT`, `LINE.LENGTH`, `NO.OF.LINES`, `ERR.MSG` |

- `IN.AMT` — amount to convert; may be `amount*CCY` format
- `OUT.AMT` — returned alpha character representation
- `LINE.LENGTH` — maximum line length; split into multi-values when exceeded
- `NO.OF.LINES` — format to a specific number of lines; blank lines padded (e.g. `*`) for cheque printing
- `ERR.MSG` — error message on failure

---

### DE.DISP.CONTROL

Allows a user-defined routine for enhanced selection in disposition control.

**FIELD.NAME field:**

| Item | Detail |
|------|--------|
| Format | `@Subroutine name` — must be a VOC entry of type `V` |
| Invoked from | `DE.DISP` and `DE.O.DISPOSITION.CONTROL` |
| Arguments | `DE.O.HEADER` record (arg 1), `OPERAND` (arg 2), `CONDITION` (arg 3), return value (arg 4: `1` = true, `0`/null = false) |

---

### DE.MAPPING

Allows a user subroutine to modify the information passed to `APPLICATION.HANDOFF`, enabling additional data mapping not normally available for the message type.

**Routine field:**

| Item | Detail |
|------|--------|
| Format | `@Subroutine name` — must be a VOC entry of type `V` |
| Invoked from | `APPLICATION.HANDOFF` |
| Arguments | DIMensioned array of nine hand-off records (arg 1), return error message (arg 2) |

If all nine records are blanked by the routine, mapping does not proceed and an error is returned to the calling application.

---

### DE.CARRIER

Contains details of all carriers available in Delivery. The carrier record ID is the carrier name as used in `DE.PRODUCT`.

Key fields:

| Field | Description |
|-------|-------------|
| `Address` | Type of record read from `DE.ADDRESS` (e.g. `SWIFT` → key `company.C-cusno.SWIFT.n`) |
| `Carrier Module` | Formatting module to use (e.g. `SWIFT`, `PRINT`, telex formats); rules in `DE.FORMAT.format-module` |
| `Interface` | Name of interface on `DE.INTERFACE`; `CARRIER.MODULE` must be `GENERIC` for custom interfaces |

Interface files created: `F.DE.O.MSG.format-module`, `F.DE.O.PRI.format-module`, `F.DE.O.MSG.interface`, `F.DE.I.MSG.interface`.

---

### DE.INTERFACE

Contains protocol details for all interfaces using the Generic Delivery Interface. ID is the interface name as defined in `DE.CARRIER.Interface`.

**OUT.IF.ROUTINE** — sends messages to the carrier:

| Item | Detail |
|------|--------|
| Format | Subroutine name (VOC entry required) |
| Invoked from | `DE.CC.GENERIC` |
| Arguments | `MISN` (message sequence number), `MSG` (formatted message) |

The routine only needs to send the message; all delivery file updates are handled by `DE.CC.GENERIC`.

**IN.IF.ROUTINE** — receives messages from the carrier:

| Item | Detail |
|------|--------|
| Format | Subroutine name (VOC entry required) |
| Invoked from | `DE.CC.GENERIC` |
| Arguments | `GLOBUS.REF` (5-digit sequence number), `CODE` (`ACK`/`NAK`/blank), `MSG` (message), `R.HEAD` (delivery header record) |

The delivery header record is passed back from the routine; the interface routine may populate fields recognised in the message.

---

### DE.MESSAGE

Allows a routine to process inward messages and generate Funds Transfers via the OFS module.

**IN.OFS.RTN field:**

| Item | Detail |
|------|--------|
| Format | Subroutine name — must be defined in `PGM.FILE` as type S program |
| Invoked from | `FT.OFS.INWARD.MAPPING`; defined in `IN.DIR.RTN` on `OFS.SOURCE`, called from phantom `OFS.REQUEST.MANAGER` |
| Arguments | `DEI.MSG.FT.IN` key, `R.INWARD`, `R.SWIFT`, `MESSAGE.TYPE`, `R.DE.MESSAGE`, `OFS.KEY` (returned), `OFS.MESSAGE` (returned) |

Default routine `FT.OFS.DEFAULT.MAPPING` is provided for message types 100, 200, 202, and 205.

---

### FT.OFS.DEFAULT.MAPPING

The `R.INWARD` record is mapped from incoming SWIFT messages. Key SWIFT field mapping logic:

| Field | SWIFT Field | Message Types | Logic |
|-------|-------------|---------------|-------|
| Receiver Correspondent | 54 | MT100, 202, 205 | Calls `FIND.CUSTOMERS.ACCOUNT`; sets `FT.DEBIT.ACCOUNT` |
| Sender Correspondent | 53 | MT100, 200, 202, 205 | Called only if no account found from field 54 |
| Mandatory Sender Bank | — | All | Called if no account found from field 53 |
| Intermediary | 56 | MT200, 202, 205 | `TEST.INTERMEDIARY`; sets `FT.CREDIT.ACCOUNT` |
| Account With Bank | 57 | MT100, 200, 202, 205 | `TEST.ACCOUNT.WITH.BK` |
| Beneficiary Bank | 58 | MT202, 205 | `TEST.BENE.BANK` |
| Beneficiary | 59 | MT100 | `TEST.BENEFICIARY` |

Transaction type logic:

| Message | Condition | FT.TRANSACTION.TYPE |
|---------|-----------|---------------------|
| 100 | No account with bank | IT |
| 100 | Account with bank present | OT |
| 200 | Always | OT |
| 202/205 | Account with, no beneficiary bank | DW |
| 202/205 | Otherwise | OT |

---

### FD.ACTIVITY

The Fiduciary application allows subroutines to modify data passed to delivery.

**HANDOFF.ROUTINE field:**

| Item | Detail |
|------|--------|
| Format | Subroutine name — must be defined in `PGM.FILE` as type S program |
| Invoked from | `FD.GENERATE.DELIVERY` |
| Argument | `SPECIAL.REC` — additional data to be passed to delivery |

Available common variables (from `I_FID.COMMON`): `FD$R.ORDER()`, `FD$R.PLACEMENT()`, `FD$R.BALANCES()`.

---

### MG.ACTIVITY

The Mortgage application allows subroutines to modify data passed to delivery.

**HANDOFF.ROUTINE field:**

| Item | Detail |
|------|--------|
| Format | Subroutine name — must be defined in `PGM.FILE` as type S program |
| Invoked from | `MG.DE.HANDOFF` |
| Arguments | `REC1` through `REC9` — the nine delivery hand-off records |

---

## Local Clearing Interface APIs

T24 provides customisation APIs in the Funds Transfer module for local clearing (transaction types BC, BI, BD).

### FT.BC.PARAMETER

Customises field-level validation and provides hooks for BC Funds Transfer processing.

**Subroutine hook fields:**

| Field | Invoked From | Purpose |
|-------|-------------|---------|
| `FT.VALIDATION.RTN` | `FT.CROSSVAL` (after standard cross-validation) | Local BC cross-validation; argument: current override count |
| `FT.DELIVERY.RTN` | Delivery processing | Divert messages to local clearing carrier |
| `STO.VALIDATION.RTN` | Standing order processing | Validate standing orders for local clearing |
| `BULK.STO.VALID.RTN` | Bulk standing order processing | Validate bulk standing orders |
| `ACCOUNT.UPD.RTN` | ACCOUNT application | Local updates triggered from account processing |
| `CUSTOMER.UPD.RTN` | CUSTOMER application | Local updates triggered from customer processing |
| `DIVERSION.RTN` | Delivery system | Divert messages into the local clearing system |

**FT.VALIDATION.RTN key variables** (insert `I_F.FT.LOCAL.COMMON` and `I_F.FTCOM`):

| Variable | Description |
|----------|-------------|
| `FTLC$BC.PARAMS` | FT BC PARAMETER record for the system |
| `FTLC$LOCAL.CLEARING` | FT LOCAL CLEARING record |
| `R.CREDIT.ACCT()` | Credit account record |
| `R.DEBIT.ACCT()` | Debit account record |
| `R.CHARGE.ACCT()` | Charge account record |
| `AUTO.PROCESS` | Set to `Y` when processing during EOD or automatic online |

Error handling: set `ETEXT` and call `STORE.END.ERROR` for manual processing; return directly for automatic processing. Overrides via `TEXT` + `STORE.OVERRIDE` (manual online only).

---

### FT.TAPE.PARAMS

Defines parameters for clearing tape/file processing within the Funds Transfer local clearing interface. Used for batch-mode ingestion of clearing files.

---

### AC.ENTRY.PARAM

Defines accounting entry parameters for local clearing transactions. Controls posting rules for BC-type funds transfers.

---

## APIs in Limited Service Mode (FAMS — Funds Authorisation Microservice)

These APIs are supported by the Funds Authorisation Microservice (FAMS) and operate during Limited Service Mode (LSM).

### System / Status APIs

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/system/fundsAuthorisation/status` | Get FAMS and Transact FA status |
| `PUT` | `/system/fundsAuthorisation/status/{parameterId}` | Set FA status to initiate PREP or SYNC |
| `PUT` | `/system/fundsAuthorisation/replay` | STOP or START replay of sync to Transact |
| `PUT` | `/system/fundsAuthorisation/replay/accounts/{accountId}` | Retry sync for a specific account |
| `DELETE` | `/system/fundsAuthorisation/clean` | Clean up AcLockedEventsDelete entities |

**GET /system/fundsAuthorisation/status** — key parameters:

| Parameter | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| `parameterId` | Query | No | ID of the funds authorization parameter table |
| `accountId` | Query | No | Account ID |
| `company` | Header | Yes | Company/region identifier |

Sample response: `{ "famsStatus": "ONLINE", "transactStatus": "ONLINE", "returnCode": "...", "lsmCycle": "1" }`

**PUT /system/fundsAuthorisation/status/{parameterId}** — valid statuses: `PREP` (prepare), `SYNC` (synchronise).

### Metrics / Queue APIs

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/system/fundsAuthorisation/metrics` | List pending queue requests (filter by status, accountId, lsmCycle) |
| `DELETE` | `/system/fundsAuthorisation/metrics` | Clear pending requests queue (ALL or PROCESSED) |
| `GET` | `/system/fundsAuthorisation/summaryMetrics` | Summary totals of pending queue for all/specific accounts |

### Account / Reservation APIs

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/holdings/accounts/{accountId}/balances` | Account balances and available funds |
| `PUT` | `/holdings/accounts/{accountId}/status` | Set or remove emergency block on account |
| `GET` | `/holdings/accounts/{accountId}/reservations` | All active reservations for account |
| `GET` | `/holdings/accounts/{accountId}/reservations/{reservationId}` | Single active reservation |
| `POST` | `/order/fundsReservation` | Create, validate, or cancel funds reservation |

**POST /order/fundsReservation** — request body fields:

| Field | Mandatory | Valid Values | Description |
|-------|-----------|--------------|-------------|
| `requestType` | Yes | `CSM=RESERVE`, `CSM=COVER`, `CSM=CANCELRES` | Type of reservation operation |
| `acEntryParamId` | Yes | — | Processing rule ID for the clearing request |
| `ofsString` | Yes | — | Full OFS request string |

Sample request:
```json
{
  "requestType": "CSM=COVER",
  "acEntryParamId": "COVER",
  "ofsString": "101,GB62DEMO60161300087122,100,D,USD,213,20190417,REF.ARR3RESKEY1,,NARR.ARR3RESKEY22,,ARR3RESKEY22"
}
```

---

## API Behavior in Various Modes

API results depend on the **System FA Status** and **Account FA Status** in both FAMS and Transact.

### FAMS API Behavior Matrix

**Reservation and ValidationTransaction:**

| System FA Status | Account FA Status | LSM Allowed | Redirected to Transact | Result |
|-----------------|-------------------|-------------|----------------------|--------|
| ONLINE | Blank | — | YES | Success/error per Transact conditions |
| ONLINE | ERROR | — | YES | Success/error per Transact (Force mode or override-specific setup) |
| ONLINE | PREP | — | — | Rejected |
| LIMITED | Blank | LIMITED | YES | Success/error per FAMS account conditions |
| LIMITED | Blank | NO | — | Rejected |
| LIMITED | ERROR | — | — | Rejected |
| SYNC | Blank/ERROR | — | YES | Success/error per Transact conditions |
| SYNC | LIMITED | — | — | Success/error per FAMS account conditions |
| SYNC | SYNC | — | — | Rejected |

**GetAccountBalances:**

| System FA Status | Account FA Status | Result |
|-----------------|-------------------|--------|
| ONLINE | — | Success/error from Transact; redirect only for available funds — other balances from FAMS |
| ONLINE | PREP | Rejected |
| LIMITED | Blank LIMITED / ERROR | Success/error per FAMS account conditions |
| LIMITED | NO | Success/error per FAMS account conditions |
| SYNC | Blank | Redirect for available funds only; other balances from FAMS |
| SYNC | LIMITED | Success/error per FAMS account conditions |

**EmergencyBlock:**

| System FA Status | Account FA Status | Result |
|-----------------|-------------------|--------|
| ONLINE | — | Rejected |
| PREP | — | Rejected |
| LIMITED | Blank LIMITED | Success/error per FAMS account conditions |
| LIMITED | NO / ERROR | Rejected |
| SYNC | Blank/ERROR/SYNC | Rejected |
| SYNC | LIMITED | Success/error per FAMS account conditions |

### Transact API Behavior Matrix

**Reservation and ValidationTransaction:**

| System FA Status | Account FA Status | Result |
|-----------------|-------------------|--------|
| ONLINE | Blank | Success/error per Transact account conditions |
| ONLINE | ERROR | Override; success/error per accounting mode and override conditions |
| ONLINE | PREP | Rejected |
| ONLINE | LIMITED | Rejected |
| SYNC | Blank | Success/error per Transact account conditions |
| SYNC | ERROR | Override; success/error per accounting mode and override conditions |
| SYNC | SYNC | Rejected |

**GetAccountBalances (Transact):**

| System FA Status | Account FA Status | Result |
|-----------------|-------------------|--------|
| ONLINE | Blank/ERROR | Success/error per Transact account conditions |
| ONLINE | PREP/LIMITED | Rejected |
| SYNC | Blank/ERROR | Success/error per Transact account conditions |
| SYNC | SYNC | Rejected |

**EmergencyBlock (Transact):** All statuses — Rejected.

### Transact Processing Behavior (Accounting / OFS Clearing / AC.LOCKED.EVENTS)

| Processing Type | System FA Status | Account FA Status | Result |
|----------------|-----------------|-------------------|--------|
| Accounting (GL entries) | ONLINE | Blank | Success/error per account conditions |
| Accounting (GL entries) | ONLINE | ERROR | Override; success/error per accounting mode |
| Accounting (GL entries) | PREP/LIMITED/SYNC | — | Rejected |
| OFS Clearing (BOOK) | ONLINE | Blank | Success/error per account conditions |
| OFS Clearing (BOOK) | ONLINE | ERROR | Override; success/error per accounting mode |
| OFS Clearing (BOOK) | PREP/LIMITED/SYNC | — | Rejected |
| AC.LOCKED.EVENTS | ONLINE | Blank/ERROR | Success/error per available funds in Transact |
| AC.LOCKED.EVENTS | PREP/LIMITED | — | Rejected |
| AC.LOCKED.EVENTS | SYNC | Blank/ERROR | Success/error per available funds in Transact; only if reservation FA.STATUS is SYNC or ONLINE |
