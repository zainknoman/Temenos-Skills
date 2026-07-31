# RC.PRIORITY — Table Schema

> Source: `INSERTS/I_F.RC.PRIORITY` in `RC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.PRTY.DEF.PREV.SETTLE` | `RcPriority_DefPrevSettle` | TField |  | Value is set at product level YES/NO field When this field is set, if the parent transaction fails then all the descendant txn fails For example consider we have 5 txn A,B,C,D,E prev settle of B = A prev settle of C = B prev settle of D = C prev settle of E = D If txn C fails then all descendant txn D and E also fails PREV.SETTLE field will take priority over this field If system id specific prev settle is left null,only then default prev settle option will be applied |
| 2 | `RC.PRTY.SYSTEM.ID` | `RcPriority_SystemId` |  |  |  |
| 3 | `RC.PRTY.RESERVED.10` | `RcPriority_Reserved10` |  |  |  |
| 4 | `RC.PRTY.PRODUCT.PRIORITY` | `RcPriority_ProductPriority` |  |  |  |
| 5 | `RC.PRTY.RESERVED.08` | `RcPriority_Reserved08` |  |  |  |
| 6 | `RC.PRTY.AA.PRODUCT.GROUP` | `RcPriority_AaProductGroup` |  |  |  |
| 7 | `RC.PRTY.PREV.SETTLE` | `RcPriority_PrevSettle` |  |  |  |
| 8 | `RC.PRTY.LOCAL.REF` | `RcPriority_LocalRef` |  |  |  |
| 9 | `RC.PRTY.PRTY.SORT` | `RcPriority_PrtySort` |  |  |  |
| 10 | `RC.PRTY.LOC.PRTY.SORT` | `RcPriority_LocPrtySort` |  |  |  |
| 11 | `RC.PRTY.RESERVED.05` | `RcPriority_Reserved05` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 12 | `RC.PRTY.RESERVED.04` | `RcPriority_Reserved04` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 13 | `RC.PRTY.RESERVED.03` | `RcPriority_Reserved03` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 14 | `RC.PRTY.RESERVED.02` | `RcPriority_Reserved02` | TField |  | This field is reserved for future use Validation rules No input field Reserved for future use |
| 15 | `RC.PRTY.OVERRIDE` | `RcPriority_Override` |  |  |  |
| 16 | `RC.PRTY.RECORD.STATUS` | `RcPriority_RecordStatus` | String |  |  |
| 17 | `RC.PRTY.CURR.NO` | `RcPriority_CurrNo` | String |  |  |
| 18 | `RC.PRTY.INPUTTER` | `RcPriority_Inputter` |  |  |  |
| 19 | `RC.PRTY.DATE.TIME` | `RcPriority_DateTime` |  |  |  |
| 20 | `RC.PRTY.AUTHORISER` | `RcPriority_Authoriser` | String |  |  |
| 21 | `RC.PRTY.CO.CODE` | `RcPriority_CoCode` | String |  |  |
| 22 | `RC.PRTY.DEPT.CODE` | `RcPriority_DeptCode` | String |  |  |
| 23 | `RC.PRTY.AUDITOR.CODE` | `RcPriority_AuditorCode` | String |  |  |
| 24 | `RC.PRTY.AUDIT.DATE.TIME` | `RcPriority_AuditDateTime` | String |  |  |
