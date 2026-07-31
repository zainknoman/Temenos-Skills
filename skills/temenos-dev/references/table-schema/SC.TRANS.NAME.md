# SC.TRANS.NAME — Table Schema

> Source: `INSERTS/I_F.SC.TRANS.NAME` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.TNM.SHORT.NAME` | `ScTransName_ShortName` |  |  |  |
| 2 | `SC.TNM.RECORD.STATUS` | `ScTransName_RecordStatus` | String |  |  |
| 3 | `SC.TNM.CURR.NO` | `ScTransName_CurrNo` | String |  |  |
| 4 | `SC.TNM.INPUTTER` | `ScTransName_Inputter` |  |  |  |
| 5 | `SC.TNM.DATE.TIME` | `ScTransName_DateTime` |  |  |  |
| 6 | `SC.TNM.AUTHORISER` | `ScTransName_Authoriser` | String |  |  |
| 7 | `SC.TNM.CO.CODE` | `ScTransName_CoCode` | String |  |  |
| 8 | `SC.TNM.DEPT.CODE` | `ScTransName_DeptCode` | String |  |  |
| 9 | `SC.TNM.AUDITOR.CODE` | `ScTransName_AuditorCode` | String |  |  |
| 10 | `SC.TNM.AUDIT.DATE.TIME` | `ScTransName_AuditDateTime` | String |  |  |
