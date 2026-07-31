# DFE.REALTIME.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DFE.REALTIME.PARAMETER` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DFE.INW.DESCRIPTION` | `DfeRealtimeParameter_Description` |  |  |  |
| 2 | `DFE.INW.ROUTINE` | `DfeRealtimeParameter_Routine` | TField |  |  |
| 3 | `DFE.INW.FIELD.DELIMITER` | `DfeRealtimeParameter_FieldDelimiter` | TField |  |  |
| 4 | `DFE.INW.FIELD.POSITION` | `DfeRealtimeParameter_FieldPosition` | TField |  |  |
| 5 | `DFE.INW.FIELD.LENGTH` | `DfeRealtimeParameter_FieldLength` | TField |  |  |
| 6 | `DFE.INW.EXTERNAL.CODE` | `DfeRealtimeParameter_ExternalCode` |  |  |  |
| 7 | `DFE.INW.DFE.PARAM.ID` | `DfeRealtimeParameter_DfeParamId` |  |  |  |
| 8 | `DFE.INW.DEFAULT.PARAM.ID` | `DfeRealtimeParameter_DefaultParamId` | TField |  |  |
| 9 | `DFE.INW.RESERVED.9` | `DfeRealtimeParameter_Reserved9` | TField |  |  |
| 10 | `DFE.INW.RESERVED.8` | `DfeRealtimeParameter_Reserved8` | TField |  |  |
| 11 | `DFE.INW.RESERVED.7` | `DfeRealtimeParameter_Reserved7` | TField |  |  |
| 12 | `DFE.INW.RESERVED.6` | `DfeRealtimeParameter_Reserved6` | TField |  |  |
| 13 | `DFE.INW.RESERVED.5` | `DfeRealtimeParameter_Reserved5` | TField |  |  |
| 14 | `DFE.INW.RESERVED.4` | `DfeRealtimeParameter_Reserved4` | TField |  |  |
| 15 | `DFE.INW.RESERVED.3` | `DfeRealtimeParameter_Reserved3` | TField |  |  |
| 16 | `DFE.INW.RESERVED.2` | `DfeRealtimeParameter_Reserved2` | TField |  |  |
| 17 | `DFE.INW.RESERVED.1` | `DfeRealtimeParameter_Reserved1` | TField |  |  |
| 18 | `DFE.INW.RECORD.STATUS` | `DfeRealtimeParameter_RecordStatus` | String |  |  |
| 19 | `DFE.INW.CURR.NO` | `DfeRealtimeParameter_CurrNo` | String |  |  |
| 20 | `DFE.INW.INPUTTER` | `DfeRealtimeParameter_Inputter` |  |  |  |
| 21 | `DFE.INW.DATE.TIME` | `DfeRealtimeParameter_DateTime` |  |  |  |
| 22 | `DFE.INW.AUTHORISER` | `DfeRealtimeParameter_Authoriser` | String |  |  |
| 23 | `DFE.INW.CO.CODE` | `DfeRealtimeParameter_CoCode` | String |  |  |
| 24 | `DFE.INW.DEPT.CODE` | `DfeRealtimeParameter_DeptCode` | String |  |  |
| 25 | `DFE.INW.AUDITOR.CODE` | `DfeRealtimeParameter_AuditorCode` | String |  |  |
| 26 | `DFE.INW.AUDIT.DATE.TIME` | `DfeRealtimeParameter_AuditDateTime` | String |  |  |
