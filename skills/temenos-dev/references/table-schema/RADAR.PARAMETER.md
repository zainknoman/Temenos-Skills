# RADAR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.RADAR.PARAMETER` in `AM_TimeSeries.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RAD.DESCRIPTION` | `RadarParameter_Description` |  |  |  |
| 2 | `RAD.XML.LEVEL` | `RadarParameter_XmlLevel` |  |  |  |
| 3 | `RAD.XML.LEVEL.NO` | `RadarParameter_XmlLevelNo` |  |  |  |
| 4 | `RAD.GLOBUS.FILE` | `RadarParameter_GlobusFile` |  |  |  |
| 5 | `RAD.XML.LABEL` | `RadarParameter_XmlLabel` |  |  |  |
| 6 | `RAD.GLOBUS.FIELD` | `RadarParameter_GlobusField` |  |  |  |
| 7 | `RAD.RECORD.STATUS` | `RadarParameter_RecordStatus` | String |  |  |
| 8 | `RAD.CURR.NO` | `RadarParameter_CurrNo` | String |  |  |
| 9 | `RAD.INPUTTER` | `RadarParameter_Inputter` |  |  |  |
| 10 | `RAD.DATE.TIME` | `RadarParameter_DateTime` |  |  |  |
| 11 | `RAD.AUTHORISER` | `RadarParameter_Authoriser` | String |  |  |
| 12 | `RAD.CO.CODE` | `RadarParameter_CoCode` | String |  |  |
| 13 | `RAD.DEPT.CODE` | `RadarParameter_DeptCode` | String |  |  |
| 14 | `RAD.AUDITOR.CODE` | `RadarParameter_AuditorCode` | String |  |  |
| 15 | `RAD.AUDIT.DATE.TIME` | `RadarParameter_AuditDateTime` | String |  |  |
