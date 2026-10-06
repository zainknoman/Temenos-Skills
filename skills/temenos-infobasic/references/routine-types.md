# Infobasic Routine Types and Templates

## Routine Type Quick Reference

| Prefix pattern | Type | Called when |
|----------------|------|-------------|
| `VVR.*` | Version Validate Record | Every field change on a T24 version |
| `VIR.*` | Version Input Record | On INPUT or CHANGE of a record |
| `VAR.*` | Version Authorise Record | On AUTHORISE of a record |
| `VCRR.*` | Version Create Record | After a record is committed |
| `*.E.NOFILE.*` | NoFile Enquiry | An enquiry with no backing file |
| `*.DE.CONV.*` | DE (Delivery Engine) Conversion | A delivery advice field value is converted before the message is formatted |
| `*.CALC.*`, `*.GET.*`, `*.CHECK.*` | AA Subroutine | Called by AA framework |
| `*.ARR.TC.*`, `*.PRD.CAT.TC.*` | Property Template | AA property definition |
| `*.S.*` | Service Routine | Background service / batch |
| `PROGRAM` | Batch Program | Standalone jBASE batch |
| `E.*.BUILD` (ENQUIRY `BUILD.ROUTINE`) | Enquiry build routine | Before selection — adds/changes selection criteria (§13) |
| `E.*.CONV` (ENQUIRY `CONVERSION` `@routine`) | Enquiry conversion | Per field value — transforms `O.DATA` (§14) |
| `<JOB>.LOAD` / `.SELECT` / `<JOB>` / `.POST` | Multi-threaded COB job | See `references/cob-services-and-extracts.md` |
| `<APP>` + `<APP>.FIELDS` (+ `.ID`, `.VALIDATE` …) | Local template table | See `references/local-templates.md` |

---

## 1. VVR - Version Validate Record (field-level)

Called on every keystroke/field change. Key COMMON variables in scope via `$INSERT I_COMMON`:

| Variable | Meaning |
|----------|---------|
| `AF` | Field number that triggered this call |
| `AV` | Multi-value position within that field |
| `COMI` | New value being committed to the field |
| `R.NEW(field)` | Current new value of any field |
| `R.OLD(field)` | Authorised (previous) value of any field |
| `R.NEW.LAST(field)` | Last saved value (pre-current-session) |
| `V$FUNCTION` | `"I"` Input, `"C"` Change, `"A"` Auth, `"D"` Delete, `"R"` Reverse |
| `PGM.VERSION` | Version suffix (e.g. `,CC`) |

```basic
* @ValidationCode : N/A
* @ValidationInfo : Timestamp         : 01 Jan 2024 00:00:00
* @ValidationInfo : User Name         : developer
* @ValidationInfo : Nb tests success  : 0
* @ValidationInfo : Nb tests failure  : 0
* @ValidationInfo : Rating            : N/A
* @ValidationInfo : Coverage          : N/A
* @ValidationInfo : Strict flag       : true
* @ValidationInfo : Bypass GateKeeper : false
* <Rating>100</Rating>
SUBROUTINE XX.VVR.MY.APPLICATION
*-----------------------------------------------------------------------------
* Validates MY.APPLICATION on field change
*-----------------------------------------------------------------------------
* Modification History :
* 01/01/24 - Task : T-12345
*             Description of change
*-----------------------------------------------------------------------------
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.MY.APPLICATION
*-----------------------------------------------------------------------------
    IF V$FUNCTION EQ "A" OR V$FUNCTION EQ "D" THEN RETURN
    BEGIN CASE
        CASE AF EQ MY.APP.CREDIT.AMT
            GOSUB VALIDATE.CREDIT.AMT
        CASE AF EQ MY.APP.ACCOUNT.NO
            GOSUB VALIDATE.ACCOUNT
        CASE 1
            ;* no action for other fields
    END CASE
RETURN
*-----------------------------------------------------------------------------
VALIDATE.CREDIT.AMT:
    IF COMI GT 500000 THEN
        ETEXT = 'AMOUNT.EXCEEDS.LIMIT'
        CALL STORE.END.ERROR
    END
RETURN
*-----------------------------------------------------------------------------
VALIDATE.ACCOUNT:
    IF NOT(COMI) THEN RETURN
    CALL F.READ(FN.ACCOUNT, COMI, R.ACCOUNT, F.ACCOUNT, E.ACCOUNT)
    IF E.ACCOUNT THEN
        ETEXT = 'INVALID.ACCOUNT.NUMBER'
        CALL STORE.END.ERROR
    END
RETURN
*-----------------------------------------------------------------------------
END
```

**Key notes:**
- `ETEXT` = error message key (looked up in EB.ERROR table) or literal text
- `CALL STORE.END.ERROR` posts the error and stops field processing
- Check `V$FUNCTION` at entry to skip irrelevant stages
- Modifying `COMI` changes what gets written to the field

---

## 2. VIR - Version Input/Change Record

Runs once per input or change (not per keystroke).

```basic
SUBROUTINE XX.VIR.MY.APPLICATION
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.MY.APPLICATION
*-----------------------------------------------------------------------------
    IF V$FUNCTION EQ "A" OR V$FUNCTION EQ "D" OR V$FUNCTION EQ "R" THEN RETURN
    GOSUB INITIALISE
    GOSUB VALIDATE
RETURN
*-----------------------------------------------------------------------------
INITIALISE:
    FN.ACCOUNT = 'F.ACCOUNT'
    F.ACCOUNT = ''
    CALL OPF(FN.ACCOUNT, F.ACCOUNT)
RETURN
*-----------------------------------------------------------------------------
VALIDATE:
    CREDIT.ACCT = R.NEW(MY.APP.CREDIT.ACCT)
    IF NOT(CREDIT.ACCT) THEN RETURN
    CALL F.READ(FN.ACCOUNT, CREDIT.ACCT, R.ACCOUNT, F.ACCOUNT, E.ACCOUNT)
    IF E.ACCOUNT THEN
        ETEXT = 'INVALID.DEBIT.ACCOUNT'
        AF = MY.APP.CREDIT.ACCT
        CALL STORE.END.ERROR
    END
RETURN
*-----------------------------------------------------------------------------
END
```

**Key note:** Set `AF` before `CALL STORE.END.ERROR` to highlight the specific field in error.

---

## 3. VAR - Version Authorise Record

Runs on authorisation.

```basic
SUBROUTINE XX.VAR.MY.APPLICATION
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.MY.APPLICATION
*-----------------------------------------------------------------------------
    GOSUB INITIALISE
    GOSUB PROCESS
RETURN
*-----------------------------------------------------------------------------
INITIALISE:
    Y.ERR = ''
RETURN
*-----------------------------------------------------------------------------
PROCESS:
    ;* On VAR, use V$ERROR / E / MESSAGE for errors (not STORE.END.ERROR)
    IF R.NEW(MY.APP.STATUS) NE 'CONFIRMED' THEN
        E = 'STATUS.MUST.BE.CONFIRMED'
        MESSAGE = "ERROR"
        V$ERROR = 1
    END
RETURN
*-----------------------------------------------------------------------------
END
```

**Error mechanism on VAR**: use `E = 'msg'`, `V$ERROR = 1` instead of `CALL STORE.END.ERROR`.

---

## 4. VCRR - Version Create Record

Runs after the record is committed. Used for side effects (posting to other applications, etc.).

```basic
SUBROUTINE XX.VCRR.MY.APPLICATION(Y.STAGE)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.MY.APPLICATION
*-----------------------------------------------------------------------------
    IF Y.STAGE NE 'VCRR' THEN RETURN
    GOSUB POST.SIDE.EFFECTS
RETURN
*-----------------------------------------------------------------------------
POST.SIDE.EFFECTS:
    ;* build and send OFS message, update linked tables, etc.
RETURN
*-----------------------------------------------------------------------------
END
```

---

## 5. DS Packager Style (R20+ modern validation, no parameters)

Used when developing with Design Studio Packager. No `$INSERT` — uses `$USING` and dot-notation APIs.

```basic
$PACKAGE XX.Sample
SUBROUTINE XX.V.FT.VALIDATION
*-----------------------------------------------------------------------------
* Validates FT credit amount via DS Packager framework
*-----------------------------------------------------------------------------
    $USING EB.SystemTables
    $USING ST.Customer
*-----------------------------------------------------------------------------
    creditAmount = EB.SystemTables.getRNew(ST.Customer.Customer.EbCusLegalId)
    IF creditAmount GT 500 THEN
        EB.SystemTables.setE('Amount greater than 500')
    END
RETURN
*-----------------------------------------------------------------------------
END
```

**Key DS Packager APIs:**
- `EB.SystemTables.getRNew(FIELD.CONST)` — read R.NEW field value
- `EB.SystemTables.getRNew(field)<1,mvPos>` — read MV value
- `EB.SystemTables.setE('error text')` — set error message
- `EB.SystemTables.getToday()` — get TODAY date
- `EB.SystemTables.getApplication()` / `setApplication()` — get/set app name
- `EB.SystemTables.getDynArrayFromRNew()` — get full R.NEW as dynamic array

---

## 6. AA Calculation Subroutine (DS Packager style)

```basic
$PACKAGE AA.PaymentSchedule
SUBROUTINE AA.CALC.CUSTOM.PROFIT(ARRANGEMENT.ID, INT.PROPERTY.ID, INTEREST.RECORD, INT.PROPERTY.DATE, TOTAL.PROFIT, CALC.ERR)
*-----------------------------------------------------------------------------
*** <region name= Description>
*** <desc>Calculate total profit for an arrangement</desc>
* This routine calculates the total profit by accumulating interest accruals
* across billing periods.
*** </region>
*-----------------------------------------------------------------------------
* Modification History :
* 01/01/24 - Task : T-12345
*             Calculate custom profit for Islamic finance product
*-----------------------------------------------------------------------------
*** <region name= Inserts>
    $USING AA.Framework
    $USING AA.Interest
    $USING AA.PaymentSchedule
    $USING AC.Fees
    $USING EB.API
*** </region>
*-----------------------------------------------------------------------------
*** <region name= Main control>
    GOSUB Initialise
    IF NOT(CALC.ERR) THEN
        GOSUB ValidateInputs
    END
    IF NOT(CALC.ERR) THEN
        GOSUB CalcProfit
    END
RETURN
*-----------------------------------------------------------------------------
*** <region name= Initialise>
Initialise:
    TOTAL.PROFIT = 0
    CALC.ERR = ""
    CURRENCY = AA.Framework.getArrCurrency()
    R.ACCOUNT.DETAILS = AA.Framework.getAccountDetails()
RETURN
*** </region>
*-----------------------------------------------------------------------------
*** <region name= ValidateInputs>
ValidateInputs:
    BEGIN CASE
        CASE NOT(ARRANGEMENT.ID)
            CALC.ERR = 1
        CASE NOT(INT.PROPERTY.ID)
            CALC.ERR = 1
        CASE INTEREST.RECORD EQ ""
            CALC.ERR = 1
    END CASE
RETURN
*** </region>
*-----------------------------------------------------------------------------
*** <region name= CalcProfit>
CalcProfit:
    AA.Interest.GetInterestAccruals("VAL", ARRANGEMENT.ID, INT.PROPERTY.ID, "", "", R.ACCRUAL.DETAILS, "", "")
    ;* Process accruals and accumulate TOTAL.PROFIT
    TOTAL.PROFIT = 0
    ;* ... calculation logic ...
    EB.API.RoundAmount(CURRENCY, TOTAL.PROFIT, '', '')
RETURN
*** </region>
*-----------------------------------------------------------------------------
END
```

---

## 7. AA Getter Subroutine

```basic
$PACKAGE AA.Services
SUBROUTINE AA.GET.ACCOUNT.STATUS(ARRANGEMENT.ID, ACCOUNT.STATUS, RET.ERR)
*-----------------------------------------------------------------------------
* Returns the current account status for an AA arrangement
*-----------------------------------------------------------------------------
    $USING AA.Framework
    $USING EB.DataAccess
*-----------------------------------------------------------------------------
    GOSUB Initialise
    GOSUB GetStatus
RETURN
*-----------------------------------------------------------------------------
Initialise:
    ACCOUNT.STATUS = ""
    RET.ERR = ""
RETURN
*-----------------------------------------------------------------------------
GetStatus:
    R.REC = ""
    EB.DataAccess.FRead("F.AA.ARRANGEMENT", ARRANGEMENT.ID, R.REC, "", RET.ERR)
    IF RET.ERR THEN RETURN
    ACCOUNT.STATUS = R.REC<AA.Framework.Arrangement.ArrArrStatus>
RETURN
*-----------------------------------------------------------------------------
END
```

---

## 8. NoFile Enquiry Routine

Populates an enquiry grid from computed/assembled data with no backing file.

```basic
$PACKAGE AA.Services
SUBROUTINE AA.E.NOFILE.MY.ENQUIRY(finalArray)
*-----------------------------------------------------------------------------
* NoFile enquiry - returns arrangement data filtered by selection criteria
*-----------------------------------------------------------------------------
    $USING EB.Reports
    $USING AA.Framework
    $USING EB.DataAccess
*-----------------------------------------------------------------------------
    GOSUB initialise
    GOSUB dasSelection
    GOSUB process
RETURN
*-----------------------------------------------------------------------------
initialise:
    finalArray = ""
    ;* Parse selection criteria from the enquiry definition
    fieldNames        = EB.Reports.getEnqSelection()<2>
    selectionOperands = EB.Reports.getEnqSelection()<3>
    selectionValues   = EB.Reports.getEnqSelection()<4>
    lArrangementId = ""
    lCustomerId    = ""
    countFields = DCOUNT(fieldNames, @VM)
    FOR i = 1 TO countFields
        BEGIN CASE
            CASE fieldNames<1,i> EQ "arrangementId"
                lArrangementId = selectionValues<1,i>
            CASE fieldNames<1,i> EQ "customerId"
                lCustomerId = selectionValues<1,i>
        END CASE
    NEXT i
RETURN
*-----------------------------------------------------------------------------
dasSelection:
    TABLE.NAME = "AA.ARRANGEMENT.ACTIVITY"
    THE.LIST = DAS$STATUS.NAU
    THE.ARGS = ""
    THE.ARGS<1> = lArrangementId
    EB.DataAccess.Das(TABLE.NAME, THE.LIST, THE.ARGS, '$NAU')
RETURN
*-----------------------------------------------------------------------------
process:
    IF NOT(THE.LIST) THEN RETURN
    N = DCOUNT(THE.LIST, @FM)
    FOR cnt = 1 TO N
        recId = THE.LIST<cnt>
        R.REC = ""
        EB.DataAccess.FRead("F.AA.ARRANGEMENT.ACTIVITY", recId, R.REC, "", readErr)
        IF readErr THEN CONTINUE
        ;* Apply filters
        customerId = R.REC<AA.Framework.ArrangementActivity.ArrActCustomer>
        IF lCustomerId NE "" AND lCustomerId NE customerId THEN CONTINUE
        ;* Build output row - fields delimited by "*"
        arrId  = R.REC<AA.Framework.ArrangementActivity.ArrActMasterArrangement>
        status = R.REC<AA.Framework.ArrangementActivity.ArrActRecordStatus>
        finalArray<-1> = arrId:"*":status:"*":customerId
    NEXT cnt
RETURN
*-----------------------------------------------------------------------------
END
```

**Enquiry definition** must map columns to positions in the `*`-delimited `finalArray` rows.

---

## 9. Delivery Engine (DE) Conversion Routine

**DE = Delivery Engine**, the T24 subsystem that produces customer advices and messages (print, SWIFT, email). It is not an enquiry or display feature. See `skills/temenos-de/` for the full DE pipeline.

A DE conversion routine converts the value of one field of a **delivery message** before that message is formatted. It works the same way as the built-in conversions (`DATE/F`, `AMT`, …) that are set in the Conversion column of a message's format record (`DE.FORMAT.PRINT` / `DE.FORMAT.SWIFT`; `DE.XML.CONVERSION` on `DE.FORMAT.XML`). The conversion only changes what appears in the advice; the T24 record is not changed. R25 ships 18 of these routines (`AA.DE.CONV.*` in `T24_BP`), for example arrangement start and expiry dates, account short name, and customer SWIFT address.

Not to be confused with:
- **`*.DE.MAP.*`**: DE **mapping** routines, set in `DE.MAPPING` field `DE.MAP.ROUTINE`. These add data to a message type. They receive the nine handoff records plus the mapping key, and return an error message.
- **Enquiry conversions**: an `ENQUIRY` CONVERSION routine (Infobasic) or `Enquiry.setValue` (L3 Java). These format enquiry columns.

```basic
$PACKAGE AA.ModelBank
SUBROUTINE AA.DE.CONV.ARRANGEMENT.START.DATE(InValue, HeaderRec, MvNo, OutValue, ErrorMsg)
*-----------------------------------------------------------------------------
* Delivery Engine (DE) conversion - arrangement start date for the delivery advice
*-----------------------------------------------------------------------------
    $USING DE.Outward
    $USING AA.PaymentSchedule
*-----------------------------------------------------------------------------
    GOSUB Initialise
    GOSUB DoConvert
RETURN
*-----------------------------------------------------------------------------
Initialise:
    OutValue = ''
    ErrorMsg = ''
    ArrangementId = InValue          ;* the message field holds the arrangement id
RETURN
*-----------------------------------------------------------------------------
DoConvert:
    IF ArrangementId EQ '' THEN RETURN
    ;* The outward delivery message being formatted is available if more context is needed:
    ;*   DE.Outward.getFDeOMsg() = F.DE.O.MSG file, DE.Outward.getRKey() = its record key
    AccountDetails = ''
    ReadErr = ''
    AA.PaymentSchedule.ProcessAccountDetails(ArrangementId, "GET", "GET", AccountDetails, ReadErr)
    StartDate = AccountDetails<AA.PaymentSchedule.AccountDetails.AdValueDate>
    OutValue = OCONV(ICONV(StartDate, "D4"), "D4E")   ;* value written into the advice
RETURN
*-----------------------------------------------------------------------------
END
```

Pattern taken from R25 `T24_BP/AA.DE.CONV.ARRANGEMENT.START.DATE.b`. It runs inside the Delivery Engine formatting stage, not inside an enquiry.

**Parameters** (all DE conversion routines share this signature):
- `InValue`: the value of the message field being converted. In the R25 `AA.DE.CONV.*` routines this is the arrangement id, which the routine uses to look up the data it outputs.
- `HeaderRec`: header data of the delivery message, passed in by the Delivery Engine.
- `MvNo`: multi-value position of the field in the message.
- `OutValue`: the converted value that appears in the advice. Only the advice changes; the T24 record is never modified.
- `ErrorMsg`: set it to stop formatting with an error.

---

## 10. AA Term-Condition Property Template

```basic
$PACKAGE AO.Framework
SUBROUTINE AA.ARR.TC.MY.PROPERTY
*-----------------------------------------------------------------------------
* Properties and methods for the MY.PROPERTY term condition
*-----------------------------------------------------------------------------
    $USING AA.Framework
    $USING EB.SystemTables
    $USING EB.Template
    $USING AF.Framework
*-----------------------------------------------------------------------------
    EB.Template.setCMethods('')
    EB.Template.setCProperties('')
*-----------------------------------------------------------------------------
    tmp = EB.Template.getCProperties()
    tmp<EB.Template.PTitle> = 'My Property Title'
    EB.Template.setCProperties(tmp)
    tmp = EB.Template.getCProperties()
    tmp<EB.Template.PEquatePrefix> = 'AA.TC.MY.PROP'
    EB.Template.setCProperties(tmp)
*-----------------------------------------------------------------------------
    SAVE.APPL = EB.SystemTables.getApplication()
    EB.SystemTables.setApplication('AA.ARR.TC.MY.PROPERTY')
    AF.Framework.PropertyTemplate()
    EB.SystemTables.setApplication(SAVE.APPL)
RETURN
*-----------------------------------------------------------------------------
END
```

---

## 11. Standalone Batch Program

```basic
PROGRAM XX.BATCH.MY.JOB
*-----------------------------------------------------------------------------
* Batch job - processes MY.FILE records
*-----------------------------------------------------------------------------
* Modification History :
* 01/01/24 - Task : T-12345 - Initial implementation
*-----------------------------------------------------------------------------
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.MY.FILE

    GOSUB INITIALISE
    GOSUB OPEN.FILES
    GOSUB PROCESS
RETURN
*-----------------------------------------------------------------------------
INITIALISE:
    FN.MY.FILE = 'F.MY.FILE'
    F.MY.FILE  = ''
    TOTAL.PROCESSED = 0
    TOTAL.ERRORS    = 0
RETURN
*-----------------------------------------------------------------------------
OPEN.FILES:
    CALL OPF(FN.MY.FILE, F.MY.FILE)
RETURN
*-----------------------------------------------------------------------------
PROCESS:
    SELECT.STMT = 'SELECT ' : FN.MY.FILE
    CALL EB.READLIST(SELECT.STMT, REC.LIST, '', TOTAL.RECS, ERR)
    FOR I = 1 TO TOTAL.RECS
        RECORD.ID = REC.LIST<I>
        CALL F.READ(FN.MY.FILE, RECORD.ID, R.REC, F.MY.FILE, E.REC)
        IF E.REC THEN
            TOTAL.ERRORS += 1
            CONTINUE
        END
        GOSUB PROCESS.RECORD
        TOTAL.PROCESSED += 1
    NEXT I
    CRT "Processed: " : TOTAL.PROCESSED : " Errors: " : TOTAL.ERRORS
RETURN
*-----------------------------------------------------------------------------
PROCESS.RECORD:
    ;* Record-level logic here
RETURN
*-----------------------------------------------------------------------------
END
```

---

## 12. Service Routine (EB Service)

```basic
$PACKAGE XX.Services
SUBROUTINE XX.S.MY.SERVICE
*-----------------------------------------------------------------------------
* Service routine - runs as a background EB.SERVICE
*-----------------------------------------------------------------------------
    $USING EB.Service
    $USING EB.DataAccess
*-----------------------------------------------------------------------------
    GOSUB Initialise
    GOSUB ProcessService
RETURN
*-----------------------------------------------------------------------------
Initialise:
    RetErr = ""
RETURN
*-----------------------------------------------------------------------------
ProcessService:
    ;* Service logic - check EB.Service.getStatus() etc.
RETURN
*-----------------------------------------------------------------------------
END
```

---

## 13. Enquiry Build Routine (`BUILD.ROUTINE` on ENQUIRY)

Proven skeleton: `tests/golden/infobasic-enquiry-build/`. The routine receives the enquiry
selection array. Positions `<2>`, `<3>` and `<4>` are the parallel VM-lists of selection field
names, operands and values (the Java hook docs call these "fields<2 … 4> from ENQ.SELECTION",
CB3PREFJ Lesson 7). Append to all three together:

```basic
    SUBROUTINE E.MY.BUILD(ENQ.DATA)
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_ENQUIRY.COMMON

    ENQ.DATA<2,-1> = 'SECTOR'          ;* selection field (STANDARD.SELECTION name)
    ENQ.DATA<3,-1> = 'EQ'              ;* operand
    ENQ.DATA<4,-1> = '1001'            ;* value
    RETURN
END
```

To read what the user typed, `LOCATE 'FIELD' IN ENQ.DATA<2,1> SETTING POS` and take
`ENQ.DATA<3,POS>` / `ENQ.DATA<4,POS>`. Java equivalent: `Enquiry.setFilterCriteria`
(`temenos-l3`).

## 14. Enquiry Conversion Routine (`CONVERSION` = `@ROUTINE`)

Proven skeleton: `tests/golden/infobasic-enquiry-conversion/`. Commons from
`I_ENQUIRY.COMMON`: `O.DATA` holds the current value **in and out**, `ID` the current
record id, `R.RECORD` the current record, `VM.COUNT` the number of multi-values to display
(Temenos *Subroutine Guide*, `E.GET.LOCAL.AMT` / `E.GET.STMT.NARRATIVE`).

```basic
    SUBROUTINE E.MY.CONV
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_ENQUIRY.COMMON
    $INSERT I_F.CUSTOMER

    Y.ID = O.DATA
    IF Y.ID EQ '' THEN RETURN
    FN.CUS = 'F.CUSTOMER' ; F.CUS = ''
    CALL OPF(FN.CUS, F.CUS)
    R.CUS = '' ; Y.ERR = ''
    CALL F.READ(FN.CUS, Y.ID, R.CUS, F.CUS, Y.ERR)
    IF Y.ERR EQ '' THEN O.DATA = R.CUS<EB.CUS.SECTOR> ELSE O.DATA = ''
    RETURN
END
```

Componentised: `EB.Reports.getOData()` / `EB.Reports.setOData(v)`, `EB.Reports.getRRecord()`,
`EB.Reports.getId()`. A conversion that returns several lines sets `R.RECORD<n>` to a VM-list and
`VM.COUNT` to its count. A conversion runs once per row, so never `SELECT` inside it. Java
equivalent: `Enquiry.setValue` (`temenos-l3`).

---

## Parameterised Utility Subroutine (Legacy $INSERT style)

```basic
SUBROUTINE XX.VAL.ACCOUNT.NOS(ACCOUNT.ID, CHECK.TYPE, ERR.MSG)
*-----------------------------------------------------------------------------
* Validates account number format and existence
*-----------------------------------------------------------------------------
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.ACCOUNT
*-----------------------------------------------------------------------------
    ERR.MSG = ''
    IF NOT(ACCOUNT.ID) THEN RETURN
    GOSUB CHECK.FORMAT
    IF NOT(ERR.MSG) THEN GOSUB CHECK.EXISTS
RETURN
*-----------------------------------------------------------------------------
CHECK.FORMAT:
    IF LEN(ACCOUNT.ID) NE 10 THEN
        ERR.MSG = 'INVALID.ACCOUNT.FORMAT'
    END
RETURN
*-----------------------------------------------------------------------------
CHECK.EXISTS:
    CALL F.READ(FN.ACCOUNT, ACCOUNT.ID, R.ACCOUNT, F.ACCOUNT, E.ACCOUNT)
    IF E.ACCOUNT THEN
        ERR.MSG = 'ACCOUNT.NOT.FOUND'
    END
RETURN
*-----------------------------------------------------------------------------
END
```
