# RC.CHANGE — Table Schema

> Source: `INSERTS/I_F.RC.CHANGE` in `RC_TransactionCycler.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.CHG.RC.DETAIL.ID` | `RcChange_RcDetailId` |  |  |  |
| 2 | `RC.CHG.RESERVED.01` | `RcChange_Reserved01` |  |  |  |
| 3 | `RC.CHG.RESERVED.02` | `RcChange_Reserved02` |  |  |  |
| 4 | `RC.CHG.CHANGE.TYPE` | `RcChange_ChangeType` |  |  |  |
| 5 | `RC.CHG.CHANGE.VALUE` | `RcChange_ChangeValue` |  |  |  |
| 6 | `RC.CHG.RESERVED.03` | `RcChange_Reserved03` |  |  |  |
| 7 | `RC.CHG.RESERVED.04` | `RcChange_Reserved04` |  |  |  |
| 8 | `RC.CHG.RESERVED.05` | `RcChange_Reserved05` |  |  |  |
| 9 | `RC.CHG.RESERVED.06` | `RcChange_Reserved06` |  |  |  |
| 10 | `RC.CHG.CHANGE.REASON` | `RcChange_ChangeReason` |  |  |  |
| 11 | `RC.CHG.RESERVED.07` | `RcChange_Reserved07` | TField |  |  |
| 12 | `RC.CHG.RESERVED.08` | `RcChange_Reserved08` | TField |  |  |
| 13 | `RC.CHG.RESERVED.09` | `RcChange_Reserved09` | TField |  |  |
| 14 | `RC.CHG.LOCAL.REF` | `RcChange_LocalRef` |  |  |  |
| 15 | `RC.CHG.OVERRIDE` | `RcChange_Override` |  |  |  |
| 16 | `RC.CHG.RECORD.STATUS` | `RcChange_RecordStatus` | String |  |  |
| 17 | `RC.CHG.CURR.NO` | `RcChange_CurrNo` | String |  |  |
| 18 | `RC.CHG.INPUTTER` | `RcChange_Inputter` |  |  |  |
| 19 | `RC.CHG.DATE.TIME` | `RcChange_DateTime` |  |  |  |
| 20 | `RC.CHG.AUTHORISER` | `RcChange_Authoriser` | String |  |  |
| 21 | `RC.CHG.CO.CODE` | `RcChange_CoCode` | String |  |  |
| 22 | `RC.CHG.DEPT.CODE` | `RcChange_DeptCode` | String |  |  |
| 23 | `RC.CHG.AUDITOR.CODE` | `RcChange_AuditorCode` | String |  |  |
| 24 | `RC.CHG.AUDIT.DATE.TIME` | `RcChange_AuditDateTime` | String |  |  |
