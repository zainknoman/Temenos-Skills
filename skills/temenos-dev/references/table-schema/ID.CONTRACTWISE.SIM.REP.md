# ID.CONTRACTWISE.SIM.REP — Table Schema

> Source: `INSERTS/I_F.ID.CONTRACTWISE.SIM.REP` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.ICR.LOCAL.PATH` | `IdContractwiseSimRep_LocalPath` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `ID.ICR.RECORD.STATUS` | `IdContractwiseSimRep_RecordStatus` | String |  |  |
| 3 | `ID.ICR.CURR.NO` | `IdContractwiseSimRep_CurrNo` | String |  |  |
| 4 | `ID.ICR.INPUTTER` | `IdContractwiseSimRep_Inputter` |  |  |  |
| 5 | `ID.ICR.DATE.TIME` | `IdContractwiseSimRep_DateTime` |  |  |  |
| 6 | `ID.ICR.AUTHORISER` | `IdContractwiseSimRep_Authoriser` | String |  |  |
| 7 | `ID.ICR.CO.CODE` | `IdContractwiseSimRep_CoCode` | String |  |  |
| 8 | `ID.ICR.DEPT.CODE` | `IdContractwiseSimRep_DeptCode` | String |  |  |
| 9 | `ID.ICR.AUDITOR.CODE` | `IdContractwiseSimRep_AuditorCode` | String |  |  |
| 10 | `ID.ICR.AUDIT.DATE.TIME` | `IdContractwiseSimRep_AuditDateTime` | String |  |  |
