# RC.CONDITION — Table Schema

> Source: `INSERTS/I_F.RC.CONDITION` in `RC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.COND.DESCRIPTION` | `RcCondition_Description` |  |  |  |
| 2 | `RC.COND.RETRY.FQU` | `RcCondition_RetryFqu` | TField |  | This standard frequency field is used to determine when to attempt a retry. This field is sub-divided into two elements: 1. Date 1-9 type D (date format) characters. 2. Frequency DAILY -Every day BSNSS - Every Business day WEEKLY - Every week or XX number of weeks MONTHLY - Twice Monthly or Monthly every XX months on a specific date DEFINED - (Must exist EB.FREQUENCY) For example; LHFYR -Last day in this Mid Year LQUAT - Last day in this quarter LYEAR-Last day of this year LMNTH - Last day of this month LWEEK - Last day of this week Validation rules Standard T24 frequency |
| 3 | `RC.COND.RETRY.ATTEMPTS` | `RcCondition_RetryAttempts` | TField | No | Defines the number of retry attempts before giving up, it will be the number of days if the frequency is daily Validation rules Up to 5n characters Optional Input No input if retry period is set |
| 4 | `RC.COND.RETRY.PERIOD` | `RcCondition_RetryPeriod` | TField | Yes | Defines a specific period for example to terminate the retry processing based on the date the transaction was added to the recycler, For example M0131 end of this month, M0231 end of next month, M0215 on the 15th of the next month. Validation rules Mandatory if cutoff time is entered No input if retry attempts is set. |
| 5 | `RC.COND.RETRY.OPTIONS` | `RcCondition_RetryOptions` | TField |  |  |
| 6 | `RC.COND.RETENTION.PERIOD` | `RcCondition_RetentionPeriod` | TField | No | Defines the number of days that the RC.DETAIL record will remain after maturity before being deleted or moved to history. Validation rules Optional Input Upto 2N |
| 7 | `RC.COND.WRITE.TO.HISTORY` | `RcCondition_WriteToHistory` | TField | No | This field is to indicate whether RC.DETAIL record will be written to the RC.DETAIL.HIST file. "YES" indicates that the RC.DETAIL record will be written to RC.DETAIL.HIST after the post maturity period "NO" or NULL indicates that the detail record will be deleted at the end of the retention period. Validation rules Optional Input YES NO or Null |
| 8 | `RC.COND.TXN.TYPE` | `RcCondition_TxnType` | TField |  |  |
| 9 | `RC.COND.START.DT.OPTION` | `RcCondition_StartDtOption` | TField |  | This option is to specify a relative date or a specific day of a month as a start date. This would be used to offset the START.DATE of the retry process with base date as capture date Value of this field can either be given as "nn" or "+nn" where 'nn' is a numeric value between 1 to 31, if "+" does not precedes numeric value Or can be set as any numeric value between 1 to 99 when preceded by "+" character |
| 10 | `RC.COND.DATE.CONVENTION` | `RcCondition_DateConvention` | TField |  |  |
| 11 | `RC.COND.CUTOFF.TIME` | `RcCondition_CutoffTime` | TField | No | This field indicates cutoff time factor for the transaction to be processed by the Recycler. Validation rules: Optional field Accept information in time format as HH:MM |
| 12 | `RC.COND.ONLINE.RETRY.ATTEMPTS` | `RcCondition_OnlineRetryAttempts` | TField |  |  |
| 13 | `RC.COND.RESERVED.05` | `RcCondition_Reserved05` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 14 | `RC.COND.RESERVED.04` | `RcCondition_Reserved04` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 15 | `RC.COND.RESERVED.03` | `RcCondition_Reserved03` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 16 | `RC.COND.LOCAL.REF` | `RcCondition_LocalRef` |  |  |  |
| 17 | `RC.COND.OVERRIDE` | `RcCondition_Override` |  |  |  |
| 18 | `RC.COND.RECORD.STATUS` | `RcCondition_RecordStatus` | String |  |  |
| 19 | `RC.COND.CURR.NO` | `RcCondition_CurrNo` | String |  |  |
| 20 | `RC.COND.INPUTTER` | `RcCondition_Inputter` |  |  |  |
| 21 | `RC.COND.DATE.TIME` | `RcCondition_DateTime` |  |  |  |
| 22 | `RC.COND.AUTHORISER` | `RcCondition_Authoriser` | String |  |  |
| 23 | `RC.COND.CO.CODE` | `RcCondition_CoCode` | String |  |  |
| 24 | `RC.COND.DEPT.CODE` | `RcCondition_DeptCode` | String |  |  |
| 25 | `RC.COND.AUDITOR.CODE` | `RcCondition_AuditorCode` | String |  |  |
| 26 | `RC.COND.AUDIT.DATE.TIME` | `RcCondition_AuditDateTime` | String |  |  |
