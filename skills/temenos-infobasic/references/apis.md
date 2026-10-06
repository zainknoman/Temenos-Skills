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

---

## Legacy `CALL` → componentised `$USING` (verified)

Every row below was checked against the component classes in the **R23 JARs** (each
`component_<Mod>_<Name>_*_cl.class` lists each method next to the legacy routine it wraps).
The componentised method keeps the legacy routine's arguments. Never derive a name by CamelCasing
a legacy routine: many are irregular (`EB.ACCOUNTING` → `AC.API.EbAccounting`,
`MULTI.GET.LOC.REF` → `EB.Updates.MultiGetLocRef`, `EB.FORMAT.ID` →
`EB.TransactionControl.FormatId`).

| Legacy | `$USING` form | Legacy | `$USING` form |
|--------|---------------|--------|---------------|
| `OPF` | `EB.DataAccess.Opf` | `STORE.END.ERROR` | `EB.ErrorProcessing.StoreEndError` |
| `F.READ` | `EB.DataAccess.FRead` | `ERR` | `EB.ErrorProcessing.Err` |
| `F.READU` | `EB.DataAccess.FReadu` | `FATAL.ERROR` | `EB.ErrorProcessing.FatalError` |
| `F.READV` | `EB.DataAccess.FReadv` | `EXCEPTION.LOG` | `EB.ErrorProcessing.ExceptionLog` |
| `F.WRITE` | `EB.DataAccess.FWrite` | `STORE.OVERRIDE` | `EB.OverrideProcessing.StoreOverride` |
| `F.DELETE` | `EB.DataAccess.FDelete` | `GET.LOC.REF` | `EB.LocalReferences.GetLocRef` |
| `F.RELEASE` | `EB.DataAccess.FRelease` | `MULTI.GET.LOC.REF` | `EB.Updates.MultiGetLocRef` |
| `F.READ.HISTORY` | `EB.DataAccess.FReadHistory` | `JOURNAL.UPDATE` | `EB.TransactionControl.JournalUpdate` |
| `EB.READ.HISTORY.REC` | `EB.DataAccess.ReadHistoryRec` | `TRANSACTION.ABORT` | `EB.TransactionControl.TransactionAbort` |
| `EB.READLIST` | `EB.DataAccess.Readlist` | `CONCAT.FILE.UPDATE` | `EB.TransactionControl.ConcatFileUpdate` |
| `DAS` | `EB.DataAccess.Das` | `EB.FORMAT.ID` | `EB.TransactionControl.FormatId` |
| `CACHE.READ` | `EB.DataAccess.CacheRead` | `OFS.POST.MESSAGE` | `EB.Interface.OfsPostMessage` |
| `DBR` | `EB.DataAccess.Dbr` | `OFS.CALL.BULK.MANAGER` | `EB.Interface.OfsCallBulkManager` |
| `BATCH.BUILD.LIST` | `EB.Service.BatchBuildList` | `OFS.GLOBUS.MANAGER` | `EB.Interface.OfsGlobusManager` |
| `EB.CLEAR.FILE` | `EB.Service.ClearFile` | `OFS.BUILD.RECORD` | `EB.Foundation.OfsBuildRecord` |
| `LOAD.COMPANY` | `ST.CompanyCreation.LoadCompany` | `EB.MAP.LOCAL.FIELDS` | `EB.Foundation.MapLocalFields` |
| `EB.READ.PARAMETER` | `ST.CompanyCreation.EbReadParameter` | `EB.CURR.CONV` | `EB.Foundation.CurrConv` |
| `EB.ACCOUNTING` | `AC.API.EbAccounting` | `SC.FORMAT.CCY.AMT` | `EB.Foundation.ScFormatCcyAmt` |
| `EB.GET.ACCT.BALANCE` | `AC.API.EbGetAcctBalance` | `EB.ROUND.AMOUNT` | `EB.API.RoundAmount` |
| `EXCHRATE` | `ST.ExchangeRate.Exchrate` | `CDT` / `CDD` | `EB.API.Cdt` / `EB.API.Cdd` |
| `MIDDLE.RATE.CONV.CHECK` | `ST.ExchangeRate.MiddleRateConvCheck` | `JULDATE` | `EB.API.Juldate` |
| `TERMRATE` | `ST.ExchangeRate.Termrate` | `EB.SET.NEW.TASK` | `EB.API.SetNewTask` |
| `DIETER.DATE` | `ST.Config.DieterDate` | `GET.STANDARD.SELECTION.DETS` | `EB.API.GetStandardSelectionDets` |
| `CALENDAR.DAY` | `EB.Utility.CalendarDay` | `FIELD.NAMES.TO.NUMBERS` | `EB.API.FieldNamesToNumbers` |
| `EB.NO.OF.MONTHS` | `EB.Utility.NoOfMonths` | `EB.GET.APPL.FIELD` | `EB.API.GetApplField` |
| `REFRESH.FIELD` | `EB.Display.RefreshField` | `ALLOCATE.UNIQUE.TIME` | `EB.API.AllocateUniqueTime` |
| `REBUILD.SCREEN` | `EB.Display.RebuildScreen` | `CHECK.ROUTINE.EXIST` | `EB.API.CheckRoutineExist` |
| `CALCULATE.CHARGE` | `CG.ChargeConfig.CalculateCharge` | `Product.isInCompany` | `EB.API.ProductIsInCompany` |

AA methods present in R23 (argument lists not documented in the sources here, so confirm
them before use): `AA.Framework.GetArrangementConditions`, `AA.Framework.GetPeriodBalances`,
`AA.Framework.GetEcbBalanceAmount`, `AA.Framework.GetArrangementAccountId`,
`AA.Framework.GetArrangement`, `AA.ProductFramework.GetPropertyRecord`,
`AC.CashFlow.AccountserviceGetworkingbalance`.

## Common-variable accessors (componentised code)

With `$USING`, the `I_COMMON` / `I_ENQUIRY.COMMON` variables are read and written through
accessors (all verified in R23 `component_EB_SystemTables` / `component_EB_Reports`):

| Variable | `EB.SystemTables.` read | write |
|----------|------------------------|-------|
| `R.NEW(f)` / `R.OLD(f)` / `R.NEW.LAST(f)` | `getRNew(f)` / `getROld(f)` / `getRNewLast(f)` | `setRNew(f, v)` |
| `COMI` / `COMI.ENRI` | `getComi()` / `getComiEnri()` | `setComi` / `setComiEnri` |
| `ETEXT` / `E` / `TEXT` | `getEtext()` / `getE()` / `getText()` | `setEtext` / `setE` / `setText` |
| `AF` / `AV` / `AS` | `getAf()` / `getAv()` / `getAs()` | `setAf` / `setAv` / `setAs` |
| `ID.NEW` / `ID.COMPANY` | `getIdNew()` / `getIdCompany()` | `setIdNew` |
| `V$FUNCTION` / `MESSAGE` | `getVFunction()` / `getMessage()` | `setVFunction` / `setMessage` |
| `TODAY` / `LCCY` / `LNGG` / `OPERATOR` | `getToday()` / `getLccy()` / `getLngg()` / `getOperator()` | — |
| `APPLICATION` / `PGM.VERSION` | `getApplication()` / `getPgmVersion()` | — |
| `R.COMPANY` / `R.USER` / `R.DATES` | `getRCompany()` / `getRUser()` / `getRDates()` | — |
| `T` / `N` / `F` / `ID.F` / `ID.N` / `ID.T` | `getT()` | `setT` / `setN` / `setF` / `setIdF` / `setIdN` / `setIdT` |

`EB.Reports.`: `getOData`/`setOData`, `getRRecord`/`setRRecord`, `getId`/`setId`,
`getEnqSelection`/`setEnqSelection`, `getDFields`, `getDRangeAndValue`, `getDLogicalOperands`,
`getEnqError`/`setEnqError`, `getVmCount`/`setVmCount`, `setSmCount`, `getVc`, `getS`,
`getREnq`, `getEnqKeys`/`setEnqKeys`.

## Documented call contracts (Temenos PDFs in `docs/`)

**`F.READU` — read with lock** (T2BTT R06 *Infobasic Programming for Developers* pp. 76–77)

```basic
CALL F.READU(FN.FILE, Y.ID, R.REC, F.FILE, Y.ERR, RETRY)
;* RETRY: 'P msg' prompt to retry | 'R nn xx' retry xx times, nn s apart | 'I' ignore the lock
;*        'E' return immediately with an error | '' retry continuously
;* The lock is released by F.WRITE of the record, an explicit release, or routine end.
CALL F.RELEASE(FN.FILE, Y.ID, F.FILE)
```

**`CACHE.READ`** (same deck pp. 81–84): `CACHE.READ(FileName, ID, Record, Error)`. FileName
has no mnemonic (`'F.CURRENCY'`) and no `OPF` is needed. Use it for rarely-updated parameter
records. Entries older than `SPF>CACHE.EXPIRY` seconds are re-read. `ID` may also be
`'SelectIDs'`, `'SSelectIDs'` or `'SSelectARs'` to return an id list.

**`EB.READ.HISTORY.REC` — latest `$HIS` copy** (CSD Programming Standards item 23). Prefer it
to hand-building `ID:';n'` keys:

```basic
CALL EB.READ.HISTORY.REC(F.FUNDS.TRANSFER$HIS, Y.FT.ID, R.FT.HIS, Y.HIS.ERR)
```

**`MULTI.GET.LOC.REF`** (CSD / TAM Coding Standards p. 25) — preferred over repeated
`GET.LOC.REF`:

```basic
APPL = 'CUSTOMER'
FLD  = 'CUST.ID':VM:'MFO.CODE'
POS  = ''
CALL MULTI.GET.LOC.REF(APPL, FLD, POS)
CUST.ID.POS = POS<1,1> ; MFO.CODE.POS = POS<1,2>
```

**`EB.GET.ACCT.BALANCE`** (TAM Coding Standards p. 51):
`CALL EB.GET.ACCT.BALANCE(ACCT.ID, ACCT.REC, BALANCE.TYPE, BALANCE.DATE, SYSTEM.DATE, BALANCE, CREDIT.MVMT, DEBIT.MVMT, ERR.MSG)`

**`EB.ACCOUNTING`** (TAM Coding Standards pp. 42–43):

```basic
CALL EB.ACCOUNTING(SYSTEM.ID, TYPE, ENTRY.ARRAY, ACCOUNTING.TYPE)
CALL EB.ACCOUNTING('CLR', 'DEL', '', 0)      ;* delete entries when V$FUNCTION is 'D'
CALL EB.ACCOUNTING('CLR', 'REV', '', '')     ;* reverse on 'R' / RECORD.STATUS 'REVE'
```

`ENTRY.ARRAY` holds the entries, each laid out as a `STMT.ENTRY`/`CATEG.ENTRY` record. Build
them with the `I_F.STMT.ENTRY` equates and verify every field with
`validate_fields.py --app STMT.ENTRY`. Validate the company and category first, and stop with
`FATAL.ERROR` on a setup error. An application that raises entries must have a `STMT.NOS` field
(template guide p. 72). The legal `TYPE` values for raising entries are not listed in the
sources here — ask.

**`STORE.OVERRIDE` with values** (template guide pp. 90–92): `TEXT` holds an `OVERRIDE` id
whose message contains `&` placeholders. The values follow after `FM`, separated by `VM`, in
placeholder order:

```basic
TEXT = 'ACCT.UNAUTH.OD':FM:Y.CCY:VM:Y.AMT:VM:Y.ACCT
CALL STORE.OVERRIDE(CURR.NO)
```

**OFS from a routine** (CSD Programming Standards items 25–26): use `OFS.CALL.BULK.MANAGER`,
not `OFS.BULK.MANAGER`. For bulk OFS transactions use the public API `ofs.addLocalRequest`
(`EB.Interface.OfsAddlocalrequest`). `OFS.POST.MESSAGE` writes to `F.OFS.MESSAGE.QUEUE`, which
`OFS.MESSAGE.SERVICE` processes. The `OFS.SOURCE` id is passed as a parameter (DEL6 *Delivery
Carriers* R11).

**General standards** (CSD Programming Standards; Programming Standards p. 33):
- Use `$INSERT`, not `$INCLUDE`.
- No `OPF` on `STANDARD.SELECTION`; use `GET.STANDARD.SELECTION.DETS`.
- No `DBR` to fetch single fields; read the record once.
- Never re-read a parameter record inside a loop.
- Errors and overrides are `EB.ERROR` / `OVERRIDE` ids, not literal text.
