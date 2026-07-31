# FX.GEN.CONDITION — Table Schema

> Source: `INSERTS/I_F.FX.GEN.CONDITION` in `FX_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FX.GE.DESCRIPTION` | `FxGenCondition_Description` |  |  |  |
| 2 | `FX.GE.RECORD.STATUS` | `FxGenCondition_RecordStatus` | String |  |  |
| 3 | `FX.GE.CURR.NO` | `FxGenCondition_CurrNo` | String |  |  |
| 4 | `FX.GE.INPUTTER` | `FxGenCondition_Inputter` |  |  |  |
| 5 | `FX.GE.DATE.TIME` | `FxGenCondition_DateTime` |  |  |  |
| 6 | `FX.GE.AUTHORISER` | `FxGenCondition_Authoriser` | String |  |  |
| 7 | `FX.GE.CO.CODE` | `FxGenCondition_CoCode` | String |  |  |
| 8 | `FX.GE.DEPT.CODE` | `FxGenCondition_DeptCode` | String |  |  |
| 9 | `FX.GE.AUDITOR.CODE` | `FxGenCondition_AuditorCode` | String |  |  |
| 10 | `FX.GE.AUDIT.DATE.TIME` | `FxGenCondition_AuditDateTime` | String |  |  |
