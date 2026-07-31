# RC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.RC.PARAMETER` in `RC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.PARAM.CREATE.RETRY.TRIGGER` | `RcParameter_CreateRetryTrigger` | TField | Yes | Field to indicate the basis on which the trigger records will be processed when the service is run online The trigger records will be updated on encountering a credit entry irrespective of this setup. Option CREDIT.BALANCE - Indicates that the retry trigger (RC.TRIGGER) will be processed based on the current functionality, i.e. the service will process the trigger only when the account's usable balance is positive (overdraft condition removed) Option ANY.CREDIT - Indicates that the retry trigger will be processed by the service for any credit, having in mind that credit check has been recently enhanced and made soft, and the bank can define various conditions for credit check to determine if there are sufficient funds Validation Rules: Mandatory field |
| 2 | `RC.PARAM.TRACK.BK.CR.TXN` | `RcParameter_TrackBkCrTxn` | TField |  | Field to indicates whether Recycler should repay on the date of payment received rather than considering the system date when funds are received on holidays. Allowed Option: YES - whenever a payment is received on holiday, the retry process will try to repay the dues from the date when the payment is received. |
| 3 | `RC.PARAM.VALIDATE.ACTIVITY.RESTRICTION` | `RcParameter_ValidateActivityRestriction` | TField |  | Field to indicate whether Recycler should perform Arrangement Activity Restriction checks on the settlement account Allowed Option: YES - System performs Activity restriction checks as part of Settlement account pre-validations during the Recycler Job processing |
| 4 | `RC.PARAM.FREQUENCY.CYCLE` | `RcParameter_FrequencyCycle` | TField |  | Field to indicate whether retry requests are cycled based on Batch Holiday or Branch Holiday when BSNSS frequency is used Allowed Options: BATCH.HOLIDAY - Next Retry Date and Retry End Date would be calculated or cycled based on Batch Holiday definition from COMPANY record BRANCH.HOLIDAY - Next Retry Date and Retry End Date would be calculated or cycled based on Branch Holiday definition from COMPANY record Null or Blank - Follows same process as BRANCH.HOLIDAY |
| 5 | `RC.PARAM.RESERVED.03` | `RcParameter_Reserved03` |  |  |  |
| 6 | `RC.PARAM.RESERVED.02` | `RcParameter_Reserved02` |  |  |  |
| 7 | `RC.PARAM.LOCAL.REF` | `RcParameter_LocalRef` |  |  |  |
| 8 | `RC.PARAM.OVERRIDE` | `RcParameter_Override` |  |  |  |
| 9 | `RC.PARAM.RECORD.STATUS` | `RcParameter_RecordStatus` | String |  |  |
| 10 | `RC.PARAM.CURR.NO` | `RcParameter_CurrNo` | String |  |  |
| 11 | `RC.PARAM.INPUTTER` | `RcParameter_Inputter` |  |  |  |
| 12 | `RC.PARAM.DATE.TIME` | `RcParameter_DateTime` |  |  |  |
| 13 | `RC.PARAM.AUTHORISER` | `RcParameter_Authoriser` | String |  |  |
| 14 | `RC.PARAM.CO.CODE` | `RcParameter_CoCode` | String |  |  |
| 15 | `RC.PARAM.DEPT.CODE` | `RcParameter_DeptCode` | String |  |  |
| 16 | `RC.PARAM.AUDITOR.CODE` | `RcParameter_AuditorCode` | String |  |  |
| 17 | `RC.PARAM.AUDIT.DATE.TIME` | `RcParameter_AuditDateTime` | String |  |  |
