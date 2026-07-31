# RC.CONTRACT.PRIORITY — Table Schema

> Source: `INSERTS/I_F.RC.CONTRACT.PRIORITY` in `RC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.CONT.DESCRIPTION` | `RcContractPriority_Description` |  |  |  |
| 2 | `RC.CONT.DUE.TYPE` | `RcContractPriority_DueType` |  |  |  |
| 3 | `RC.CONT.DUE.RULE` | `RcContractPriority_DueRule` |  |  |  |
| 4 | `RC.CONT.LOCAL.REF` | `RcContractPriority_LocalRef` |  |  |  |
| 5 | `RC.CONT.RESERVED.10` | `RcContractPriority_Reserved10` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 6 | `RC.CONT.RESERVED.09` | `RcContractPriority_Reserved09` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 7 | `RC.CONT.RESERVED.08` | `RcContractPriority_Reserved08` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 8 | `RC.CONT.RESERVED.07` | `RcContractPriority_Reserved07` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 9 | `RC.CONT.RESERVED.06` | `RcContractPriority_Reserved06` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 10 | `RC.CONT.RESERVED.05` | `RcContractPriority_Reserved05` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 11 | `RC.CONT.RESERVED.04` | `RcContractPriority_Reserved04` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 12 | `RC.CONT.RESERVED.03` | `RcContractPriority_Reserved03` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 13 | `RC.CONT.RESERVED.02` | `RcContractPriority_Reserved02` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 14 | `RC.CONT.OVERRIDE` | `RcContractPriority_Override` |  |  |  |
| 15 | `RC.CONT.RECORD.STATUS` | `RcContractPriority_RecordStatus` | String |  |  |
| 16 | `RC.CONT.CURR.NO` | `RcContractPriority_CurrNo` | String |  |  |
| 17 | `RC.CONT.INPUTTER` | `RcContractPriority_Inputter` |  |  |  |
| 18 | `RC.CONT.DATE.TIME` | `RcContractPriority_DateTime` |  |  |  |
| 19 | `RC.CONT.AUTHORISER` | `RcContractPriority_Authoriser` | String |  |  |
| 20 | `RC.CONT.CO.CODE` | `RcContractPriority_CoCode` | String |  |  |
| 21 | `RC.CONT.DEPT.CODE` | `RcContractPriority_DeptCode` | String |  |  |
| 22 | `RC.CONT.AUDITOR.CODE` | `RcContractPriority_AuditorCode` | String |  |  |
| 23 | `RC.CONT.AUDIT.DATE.TIME` | `RcContractPriority_AuditDateTime` | String |  |  |
| 24 | `RC.CONT.CUSTOM.PRIORITY.RANK` | `RcContractPriority_CustomPriorityRank` |  |  |  |
| 25 | `RC.CONT.PRIORITY.RANK.TYPE` | `RcContractPriority_PriorityRankType` |  |  |  |
