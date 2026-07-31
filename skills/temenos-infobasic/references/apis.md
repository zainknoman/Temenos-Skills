# Infobasic T24 API Reference

## API Style: $INSERT (legacy) vs $USING (modern)

| Style | Release | How to call |
|-------|---------|------------|
| `$INSERT I_COMMON` + `CALL SUBROUTINE(...)` | Pre-R20 / TAFJ classic | `CALL F.READ(...)`, `CALL OPF(...)` |
| `$USING Package` + dot-notation | R20+ DS Packager / TAFJ modern | `AA.Framework.GetArrangement(...)` |

Both styles may coexist. The `$USING` style uses no `CALL` keyword.

---

## Legacy CALL APIs

### File Operations

```basic
CALL OPF(FN.FILE, F.FILE)
;* Opens FN.FILE into handle F.FILE. FN.FILE = 'F.ACCOUNT', F.FILE must be '' first.

CALL F.READ(FN.FILE, ID, R.REC, F.FILE, E.REC)
;* Reads ID from FN.FILE -> R.REC. E.REC = '' if found, error string if not.

CALL CACHE.READ('F.PARAM.TABLE', TABLE.ID, R.REC, READ.FAILED)
;* Cached read for reference/parameter tables. READ.FAILED = 1 if not found.

CALL F.WRITE(FN.FILE, ID, R.REC)
;* Writes R.REC to FN.FILE at key ID.

CALL EB.READLIST(SELECT.STMT, LIST, LIST.NAME, TOTAL, ERR)
;* Executes SELECT and returns LIST of IDs. TOTAL = count. LIST = FM-separated IDs.
```

### Date APIs

```basic
CALL CDT('PK', DATE.VAR, '+30')   ;* Add 30 calendar days to DATE.VAR (modifies in place)
CALL CDT('PK', DATE.VAR, '-7')    ;* Subtract 7 days
CALL CDD('PK', DATE1, DATE2, DAYS);* DAYS = 'C' + day count between DATE1 and DATE2
CALL JULDATE(GREGORIAN, JULIAN)   ;* Convert YYYYMMDD -> Julian
```

### Validation Error APIs

```basic
CALL STORE.END.ERROR
;* Posts ETEXT as error on field AF (MV position AV). Stops processing.
;* Always set ETEXT (and optionally AF, AV) before calling.

CALL STORE.OVERRIDE(CURR.NO)
;* Posts TEXT as an override warning. CURR.NO = current override count.

CALL REFRESH.GUI.OBJECTS
;* Refreshes the GUI screen (use in VVR to update displayed fields after modifying COMI).
```

### Exchange Rate

```basic
CALL EXCHRATE(Y.CCY.MKT, Y.DR.CCY, Y.DR.AMT, Y.CR.CCY, Y.CR.AMT, '', Y.EX.RATE, '', '', Y.RT.CODE)
;* CCY.MKT=1 (spot), DR.CCY=debit currency, DR.AMT=debit amount, CR.CCY=credit currency
;* Returns CR.AMT converted amount, EX.RATE=exchange rate used
```

### Enquiry Execution

```basic
CALL OFS.ENQUIRY.MANAGER('ENQUIRY.NAME', '', RESULT, '')
;* Runs an EB enquiry. RESULT = FM-separated list of matching record IDs.

CALL MULTI.GET.LOC.REF('APPLICATION.NAME', FIELD.NAMES, LREF.POS)
;* Gets field positions for FIELD.NAMES (VM-separated) in APPLICATION.NAME.
;* LREF.POS<1,N> = field number of Nth field name.

CALL GET.STANDARD.SELECTION.DETS(APP.NAME, SS.REC)
;* Gets the SS record for APP.NAME.

CALL FIELD.NAMES.TO.NUMBERS(FIELD.NAME, SS.REC, FIELD.NO, YAF, YAV, YAS, DATA.TYPE, ERR.MSG)
;* Converts FIELD.NAME to its numeric field position in SS.REC.
```

### OFS Messaging

```basic
CALL OFS.CALL.BULK.MANAGER('GCS', OFS.MSG, RESPONSE, txnCommitted)
;* Submits OFS message. RESPONSE = OFS response string. txnCommitted = 1 if OK.
```

### Other

```basic
CALL EBS.CREATE.FILE(FILE.NAME, '', ERROR.MSG)   ;* Create a new jBASE file
CALL CBA.PROCESS.PRINT.CHARGE(YINPUT, YRESULT)  ;* Bank-specific subroutine call pattern
CALL BAB.GET.PARAM.VAL(PARAM.ID, ATTRIBUTE, VALUE.1, VALUE.2)  ;* Read parameter value
```

---

## Modern Package APIs (dot-notation, no CALL)

### AA.Framework

```basic
;* Getters - retrieve values from AA common memory (no parameters)
R.ARRANGEMENT = AA.Framework.getRArrangement()
ARR.CURRENCY  = AA.Framework.getArrCurrency()
ARR.ID        = AA.Framework.getC_aalocarrid()
EFF.DATE      = AA.Framework.getC_aalocactivityeffdate()
PRODUCT.REC   = AA.Framework.getC_aalocproductrecord()
ACCT.DETAILS  = AA.Framework.getC_aalocaccountdetails()
ACCT.ID       = AA.Framework.getC_aaloclinkedaccount()
IS.NEW.ARR    = AA.Framework.getNewArrangement()
LINKED.ACCT   = AA.Framework.getLinkedAccount()

;* Read arrangement record
AA.Framework.GetArrangement(ARRANGEMENT.ID, R.ARRANGEMENT, '')

;* Read arrangement conditions (property record)
AA.Framework.GetArrangementConditions(ARR.ID, PROP.CLASS, PROP.ID, EFF.DATE, PROP.LIST, PROP.RECORD, RET.ERR)
;* PROP.CLASS = "TERM.AMOUNT" | "INTEREST" | "PAYMENT.SCHEDULE" | "DORMANCY" etc.
;* PROP.RECORD = the condition record as dynamic array
;* Use RAISE(PROP.RECORD) to expand @SM delimiters to @FM for field access

;* Get arrangement product
AA.Framework.GetArrangementProduct(ARR.ID, EFF.DATE, '', PRODUCT.ID, '')

;* Period balances
AA.Framework.GetPeriodBalances(ACCOUNT.ID, BALANCE.NAME, DATE.OPTIONS, CHECK.DATE, "", "", BAL.DETAILS, ERR.MSG)
AA.Framework.GetEppPeriodBalances(ARR.ID, BAL.TYPE, "", START.DATE, END.DATE, "", TOTAL.BAL.DETAILS, ERR.MSG)

;* Get context value from AaaRecord
AA.Framework.GetContextValue(AaaRecord, "TRANSACTION.INITIATION", CurrentTxnInit)

;* Property class list save/restore (for nested calls)
SaveProperty = AA.Framework.getAaPropertyClassList()
AA.Framework.setAaPropertyClassList('')
;* ... nested call ...
AA.Framework.setAaPropertyClassList(SaveProperty)

;* CacheRead for SourceCalcType
SourceCalcTypeRec = AA.Framework.SourceCalcType.CacheRead(ReadSource, RetError)
```

**AA.Framework field constants** (from $USING / auto-generated equates):
```basic
AA.Framework.Arrangement.ArrCurrency         ;* field pos in AA.ARRANGEMENT
AA.Framework.Arrangement.ArrStartDate
AA.Framework.Arrangement.ArrArrStatus
AA.Framework.Arrangement.ArrProductGroup
AA.Framework.Arrangement.ArrSubArrangement
AA.Framework.Arrangement.ArrLinkedApplId
AA.Framework.Arrangement.ArrRemarks
AA.Framework.ArrangementActivity.ArrActCustomer
AA.Framework.ArrangementActivity.ArrActRecordStatus
AA.Framework.ArrangementActivity.ArrActCurrNo
AA.Framework.ArrangementActivity.ArrActAuthoriser
AA.Framework.ArrangementActivity.ArrActCoCode
AA.Framework.ArrangementActivity.ArrActDeptCode
AA.Framework.ArrangementActivity.ArrActInputter
AA.Framework.ArrangementActivity.ArrActDateTime
AA.Framework.ArrangementActivity.ArrActMasterArrangement
AA.Framework.ArrangementActivity.ArrActTxnAmount
AA.Framework.ArrangementActivity.ArrActInitiationType
AA.Framework.SourceCalcType.SrcBalanceType
AA.Framework.Sep                             ;* separator constant "'-'"
AA.Framework.OveSep                          ;* override separator "'|'"
```

---

### AA.Interest

```basic
;* Get interest accruals
AA.Interest.GetInterestAccruals(REQUEST.TYPE, ARR.ID, INT.PROPERTY, "", "", R.ACCRUAL.DETAILS, "", "")
;* REQUEST.TYPE = "VAL" (valuation), "CURRENT", etc.
;* R.ACCRUAL.DETAILS = the accrual record

;* Build interest info (rates, keys, spreads, basis)
AA.Interest.BuildInterestInfo(ARR.ID, INT.PROPERTY, "", EFF.DATE, R.INTEREST, INT.DATA, INT.BASIS.DATA, ACCRUAL.RULE, "")
;* INT.DATA field constants: AA.Interest.Interest.IntEffectiveRate, IntRateTierType, IntDayBasis, IntAccrualRule, IntTierPercent, IntTierAmount
```

---

### AA.PaymentSchedule

```basic
AA.PaymentSchedule.BuildPaymentScheduleRecord(SCHEDULE.INFO, ARR.ID, "", "", R.PAYMENT.SCHEDULE, RET.ERROR)

AA.PaymentSchedule.BuildPaymentScheduleSchedules(SCHEDULE.INFO, "", "", "", FUTURE.PAY.DATES, FUTURE.PAY.TYPES, FUTURE.PAY.METHODS, "", FUTURE.PAY.PROPS, FUTURE.PAY.PROP.AMTS, "", "", "", "", "", "", FUTURE.BILL.TYPES, "", RETURN.ERROR)

AA.PaymentSchedule.GetSysBillType(BILL.TYPE.CODE, SYS.BILL.TYPE, TYP.ERR)

AA.PaymentSchedule.GetBillDetails(ARR.ID, BILL.REF, R.BILL.DETAILS, BILL.ERR)
;* Status check: R.BILL.DETAILS<AA.PaymentSchedule.BillDetails.BdBillStatus, 1> EQ "SETTLED"

;* AccountDetails field constants
AA.PaymentSchedule.AccountDetails.AdMaturityDate
AA.PaymentSchedule.AccountDetails.AdValueDate

;* PaymentSchedule field constants
AA.PaymentSchedule.PaymentSchedule.PsProperty
AA.PaymentSchedule.PaymentSchedule.PsIncludePrinAmounts
```

---

### AA.ProductFramework

```basic
AA.ProductFramework.GetPublishedRecord('PRODUCT', '', PRODUCT.ID, '', R.PRODUCT, '')
;* Gets the published (live) product record

AA.ProductFramework.GetPropertyClass(PROPERTY.NAME, PROPERTY.CLASS)
;* Returns the class of a property name (e.g. "INTEREST" -> "AA.INT")

AA.ProductFramework.GetPropertyName(PRODUCT.RECORD, 'TERM.AMOUNT', PROPERTY.NAME)
;* Gets the specific property name for a class from the product record

AA.ProductFramework.GetProductPropertyRecord('PRODUCT', STAGE, PRODUCT.ID, PROP.NAME, '', CURRENCY, '', EFF.DATE, PROP.RECORD, RET.ERR)

AA.ProductFramework.GetProductConditionRecords(PRODUCT, CURRENCY, EFF.DATE, PROP.LIST, PROP.CLASS.LIST, LINK.TYPE, PROP.COND.LIST, RET.ERR)

AA.ProductFramework.GetActivityClass(CURRENT.ACTIVITY, CURRENT.ACTIVITY.CLASS, "")
```

---

### AC.Fees

```basic
;* Interest balance updates
AC.Fees.EbUpdateIntBalances(INT.DATA, ARR.DATE, FLAT.RATE, "", "")
AC.Fees.EbUpdatePrinBalances(PRIN.DATA, BILL.DATE, ADD.AMT)

;* Full accrual calculation
AC.Fees.EbPerformAccrual(R.ACCRUAL.DATA, PRIN.DATA, INT.DATA, CALC.PERIOD, CURRENCY, CONT.CUSTOMER, DAY.BASIS, ACCRUE.TO.DATE, "", "", "", TOTAL.INTEREST)

;* Simple interest calculation
AC.Fees.EbInterestCalc(START.DATE, END.DATE, INTEREST.RATE, BASE.AMOUNT, INT.AMOUNT, ACCR.DAYS, INT.DAY.BASIS, CURRENCY, ROUND.INT.AMOUNT, ROUND.TYPE, CUSTOMER)

;* CALC.PERIOD structure (for EbPerformAccrual)
CALC.PERIOD<AC.Fees.EbAcdRecordStart> = ARR.START.DATE
CALC.PERIOD<AC.Fees.EbAcdAccrStart>   = PERIOD.START.DATE
CALC.PERIOD<AC.Fees.EbAcdAccrEnd>     = PERIOD.END.DATE
CALC.PERIOD<AC.Fees.EbAcdContractId>  = ARRANGEMENT.ID
CALC.PERIOD<AC.Fees.EbAcdAccrualParam> = ACCRUAL.RULE

;* AC.Fees field constants
AC.Fees.EbAcFromDate
AC.Fees.EbAcCompoundYield
AC.Fees.EbAciIntEffDate    ;* effective date in INT.DATA MV
AC.Fees.EbAciIntRate       ;* rate in INT.DATA MV
```

---

### EB.API

```basic
EB.API.RoundAmount(CURRENCY, AMOUNT, '', '')
;* Rounds AMOUNT to the decimal places defined for CURRENCY. Modifies AMOUNT in place.

EB.API.Cdt("", DATE.VAR, "+30C")    ;* Add 30 calendar days
EB.API.Cdt("", DATE.VAR, "-1C")     ;* Subtract 1 calendar day
EB.API.Cdd('', DATE1, DATE2, DAYS)  ;* Date difference, DAYS = 'C' + count

EB.API.Cfq()
;* Calculates next cycle frequency date. Set COMI = StartDate:Frequency before calling.
;* Returns result in COMI (read back with EB.SystemTables.getComi())
```

---

### EB.DataAccess

```basic
EB.DataAccess.FRead("F.FILE.NAME", RECORD.ID, R.REC, "", READ.ERR)
;* READ.ERR = "" if found, error string if not.

EB.DataAccess.Das(TABLE.NAME, THE.LIST, THE.ARGS, TABLE.SUFFIX)
;* DAS selection. THE.LIST receives FM-separated IDs.
;* TABLE.SUFFIX = '$NAU' (unauthorised), '$HIS' (history), '' (live)
;* THE.ARGS<1> = first selection argument (master arrangement etc.)
```

---

### EB.SystemTables

```basic
;* Read/write current transaction fields
EB.SystemTables.getRNew(FIELD.CONST)      ;* equivalent of R.NEW(field)
EB.SystemTables.setE('error message')     ;* set error (DS Packager validation)
EB.SystemTables.getToday()                ;* returns TODAY date
EB.SystemTables.getApplication()          ;* current application name
EB.SystemTables.setApplication('APP.NAME')
EB.SystemTables.getDynArrayFromRNew()     ;* full R.NEW as dynamic array
EB.SystemTables.setComi(VALUE)            ;* set COMI
EB.SystemTables.getComi()                 ;* get COMI
RNew = EB.SystemTables.getRNew(AA.Framework.ArrangementActivity.ArrActInitiationType)
```

---

### EB.Reports (Enquiry)

```basic
;* In NoFile enquiry routines - read selection criteria
fieldNames        = EB.Reports.getEnqSelection()<2>   ;* VM-separated field names
selectionOperands = EB.Reports.getEnqSelection()<3>   ;* VM-separated operands
selectionValues   = EB.Reports.getEnqSelection()<4>   ;* VM-separated values

EB.Reports.getDFields()          ;* enquiry field definitions
EB.Reports.getDRangeAndValue()   ;* range/value filters
```

---

### AA.Customer

```basic
AA.Customer.GetArrangementCustomer(ARR.ID, "", "", "", "", CONT.CUSTOMER, RET.ERROR)
;* Returns the customer ID linked to the arrangement
```

---

### AA.Dormancy

```basic
AA.Dormancy.CheckDormancyStatus(ARR.ID, PROPERTY.ID, CHECK.DATE, DORMANCY.STATUS, RET.ERR)
```

---

### EB.Template (Property Templates)

```basic
EB.Template.setCMethods('')
EB.Template.setCProperties('')
tmp = EB.Template.getCProperties()
tmp<EB.Template.PTitle> = 'My Property'
EB.Template.setCProperties(tmp)
tmp<EB.Template.PEquatePrefix> = 'AA.TC.MY.PROP'
EB.Template.setCProperties(tmp)
```

---

### AF.Framework

```basic
AF.Framework.PropertyTemplate()          ;* invoke the property template engine
EFF.DATE = AF.Framework.getActivityEffDate()   ;* get current activity effective date
```

---

### AO.Framework field constants

```basic
AO.Framework.TcPrivileges.AaTcPrivService
AO.Framework.TcPrivileges.AaTcPrivServiceActive
AO.Framework.TcPrivileges.AaTcPrivOperation
```

---

### AA.ProductManagement field constants

```basic
AA.ProductManagement.ProductDesigner.PrdCalcProperty   ;* MV list of calc properties
AA.ProductManagement.ProductDesigner.PrdSourceType     ;* corresponding source types
AA.ProductManagement.ProductDesigner.TierSourceType    ;* tier source types
```

---

## Common $INSERT Files (Legacy)

| Insert | Content |
|--------|---------|
| `I_COMMON` | Global variables: TODAY, LCCY, COMI, LNGG, AF, AV, ETEXT, TEXT, V$FUNCTION, R.NEW, R.OLD, R.DATES, etc. |
| `I_EQUATE` | System equates and separator constants |
| `I_ENQUIRY.COMMON` | Enquiry framework variables |
| `I_F.ACCOUNT` | F.ACCOUNT field position constants |
| `I_F.FUNDS.TRANSFER` | FT field position constants |
| `I_F.CUSTOMER` | F.CUSTOMER field position constants |
| `I_F.OVERRIDE` | Override record constants |
| `I_F.USER` | User record constants |
| `I_F.USER.LOCAL.REF` | User local reference position constants |
| `I_F.VERSION` | Version file constants |
| `I_AA.APP.COMMON` | AA application common variables |
| `I_AA.LOCAL.COMMON` | AA local/override common variables |
| `I_DAS.AA.ARRANGEMENT.ACTIVITY` | DAS selection constants (DAS$STATUS.NAU etc.) |

---

## COMMON Area Variables (I_COMMON key variables)

| Variable | Type | Description |
|----------|------|-------------|
| `TODAY` | String | Current date YYYYMMDD |
| `LCCY` | String | Local currency code |
| `COMI` | String | Current field committed value (VVR context) |
| `LNGG` | Number | Current language number |
| `AF` | Number | Field number that triggered VVR |
| `AV` | Number | Multi-value position that triggered VVR |
| `ETEXT` | String | Error text for STORE.END.ERROR |
| `TEXT` | String | Override text for STORE.OVERRIDE |
| `V$FUNCTION` | String | I/C/A/D/R (Input/Change/Auth/Delete/Reverse) |
| `V$ERROR` | Number | Set to 1 to indicate error in VAR |
| `R.NEW` | DynArray | New record being entered (indexed by field const) |
| `R.OLD` | DynArray | Previous authorised record |
| `R.NEW.LAST` | DynArray | Last saved value before current session |
| `PGM.VERSION` | String | Current version suffix (e.g. `,CC`) |
| `COMI` (modify) | String | Assign to change the field value being written |
| `MESSAGE` | String | "ERROR" for VAR error |
| `R.DATES` | DynArray | System DATES record (Julian date, etc.) |
