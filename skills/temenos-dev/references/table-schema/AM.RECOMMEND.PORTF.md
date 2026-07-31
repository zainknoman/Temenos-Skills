# AM.RECOMMEND.PORTF — Table Schema

> Source: `INSERTS/I_F.AM.RECOMMEND.PORTF` in `AM_Modelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.PORT.POSITION.ID` | `AmRecommendPortf_PositionId` |  |  |  |
| 2 | `AM.PORT.RECORD.STATUS` | `AmRecommendPortf_RecordStatus` | String |  |  |
| 3 | `AM.PORT.CURR.NO` | `AmRecommendPortf_CurrNo` | String |  |  |
| 4 | `AM.PORT.INPUTTER` | `AmRecommendPortf_Inputter` |  |  |  |
| 5 | `AM.PORT.DATE.TIME` | `AmRecommendPortf_DateTime` |  |  |  |
| 6 | `AM.PORT.AUTHORISER` | `AmRecommendPortf_Authoriser` | String |  |  |
| 7 | `AM.PORT.CO.CODE` | `AmRecommendPortf_CoCode` | String |  |  |
| 8 | `AM.PORT.DEPT.CODE` | `AmRecommendPortf_DeptCode` | String |  |  |
| 9 | `AM.PORT.AUDITOR.CODE` | `AmRecommendPortf_AuditorCode` | String |  |  |
| 10 | `AM.PORT.AUDIT.DATE.TIME` | `AmRecommendPortf_AuditDateTime` | String |  |  |
