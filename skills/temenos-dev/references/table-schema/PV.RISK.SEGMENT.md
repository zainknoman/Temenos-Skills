# PV.RISK.SEGMENT — Table Schema

> Source: `INSERTS/I_F.PV.RISK.SEGMENT` in `PV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVRS.DESCRIPTION` | `PvRiskSegment_Description` |  |  |  |
| 2 | `PVRS.LOCAL.REF` | `PvRiskSegment_LocalRef` |  |  |  |
| 3 | `PVRS.RECORD.STATUS` | `PvRiskSegment_RecordStatus` | String |  |  |
| 4 | `PVRS.CURR.NO` | `PvRiskSegment_CurrNo` | String |  |  |
| 5 | `PVRS.INPUTTER` | `PvRiskSegment_Inputter` |  |  |  |
| 6 | `PVRS.DATE.TIME` | `PvRiskSegment_DateTime` |  |  |  |
| 7 | `PVRS.AUTHORISER` | `PvRiskSegment_Authoriser` | String |  |  |
| 8 | `PVRS.CO.CODE` | `PvRiskSegment_CoCode` | String |  |  |
| 9 | `PVRS.DEPT.CODE` | `PvRiskSegment_DeptCode` | String |  |  |
| 10 | `PVRS.AUDITOR.CODE` | `PvRiskSegment_AuditorCode` | String |  |  |
| 11 | `PVRS.AUDIT.DATE.TIME` | `PvRiskSegment_AuditDateTime` | String |  |  |
