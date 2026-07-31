# RC.CAPTURE — Table Schema

> Source: `INSERTS/I_F.RC.CAPTURE` in `RC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.CAP.DESCRIPTION` | `RcCapture_Description` |  |  |  |
| 2 | `RC.CAP.DEF.BLOCK.FUNDS` | `RcCapture_DefBlockFunds` | TField | No | This field is maintained at the product level to decide if AC.LOCKED.EVENTS record has to be created, when cycler captures a debit transaction for retry at a later date. This feature is not supported for AA Bills recovered using RC YES/NO field When 'YES', AC.LOCKED.EVENTS would be created during capture process for the locked amount as failed amount, from.date=transaction.date and to.date as retry end.date of RC.DETAIL When this field is set to 'NO' AC.LOCKED.EVENTS would not be created during capture process Optional |
| 3 | `RC.CAP.RESERVED.09` | `RcCapture_Reserved09` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 4 | `RC.CAP.PROD.CAT.START` | `RcCapture_ProdCatStart` |  |  |  |
| 5 | `RC.CAP.RESERVED.08` | `RcCapture_Reserved08` |  |  |  |
| 6 | `RC.CAP.RESERVED.07` | `RcCapture_Reserved07` |  |  |  |
| 7 | `RC.CAP.PROD.CAT.END` | `RcCapture_ProdCatEnd` |  |  |  |
| 8 | `RC.CAP.DEF.RC.CONDITION` | `RcCapture_DefRcCondition` | TField |  | Valid record id from RC.CONDITION table to define retry related information If SYSTEM.ID specific RC.CONDITION is not defined, then this default id will be used |
| 9 | `RC.CAP.DEF.RC.TYPE` | `RcCapture_DefRcType` | TField |  | Valid RC.TYPE id to define APIs If SYSTEM.ID specific RC.TYPE is not defined, then this default id will be used. |
| 10 | `RC.CAP.SYSTEM.ID` | `RcCapture_SystemId` |  |  |  |
| 11 | `RC.CAP.RC.TYPE` | `RcCapture_RcType` |  |  |  |
| 12 | `RC.CAP.RC.CONDITION` | `RcCapture_RcCondition` |  |  |  |
| 13 | `RC.CAP.BLOCK.FUNDS` | `RcCapture_BlockFunds` |  |  |  |
| 14 | `RC.CAP.TXN.CODE` | `RcCapture_TxnCode` |  |  |  |
| 15 | `RC.CAP.PROCESSING.STAGE` | `RcCapture_ProcessingStage` |  |  |  |
| 16 | `RC.CAP.EXCL.FUT.PEN.TXNS` | `RcCapture_ExclFutPenTxns` |  |  |  |
| 17 | `RC.CAP.SUPENSE.CATEGORY` | `RcCapture_SupenseCategory` |  |  |  |
| 18 | `RC.CAP.LOCAL.REF` | `RcCapture_LocalRef` |  |  |  |
| 19 | `RC.CAP.DEF.PROCESSING.STAGE` | `RcCapture_DefProcessingStage` |  |  |  |
| 20 | `RC.CAP.DEF.EXCL.FUT.PEN.TXNS` | `RcCapture_DefExclFutPenTxns` | TField | No | This field indicates whether Future Pending Transaction needs to be Processed or not This functionality is only applicable when the retry transaction is processed during online service. Option YES - Indicates that Future Pending Transactions are not processed Option NO/NULL - Indicates that Future Pending Transactions will be processed Validation Rules: Optional Field |
| 21 | `RC.CAP.RESERVED.04` | `RcCapture_Reserved04` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 22 | `RC.CAP.RESERVED.03` | `RcCapture_Reserved03` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 23 | `RC.CAP.RESERVED.02` | `RcCapture_Reserved02` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 24 | `RC.CAP.OVERRIDE` | `RcCapture_Override` |  |  |  |
| 25 | `RC.CAP.RECORD.STATUS` | `RcCapture_RecordStatus` | String |  |  |
| 26 | `RC.CAP.CURR.NO` | `RcCapture_CurrNo` | String |  |  |
| 27 | `RC.CAP.INPUTTER` | `RcCapture_Inputter` |  |  |  |
| 28 | `RC.CAP.DATE.TIME` | `RcCapture_DateTime` |  |  |  |
| 29 | `RC.CAP.AUTHORISER` | `RcCapture_Authoriser` | String |  |  |
| 30 | `RC.CAP.CO.CODE` | `RcCapture_CoCode` | String |  |  |
| 31 | `RC.CAP.DEPT.CODE` | `RcCapture_DeptCode` | String |  |  |
| 32 | `RC.CAP.AUDITOR.CODE` | `RcCapture_AuditorCode` | String |  |  |
| 33 | `RC.CAP.AUDIT.DATE.TIME` | `RcCapture_AuditDateTime` | String |  |  |
