# SE.MAPPING.DEFINITIONS — Table Schema

> Source: `INSERTS/I_F.SE.MAPPING.DEFINITIONS` in `SE_SeatHeatMap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.MD.DESCRIPTION` | `SeMappingDefinitions_Description` |  |  |  |
| 2 | `SE.MD.BUSINESS.LEVEL` | `SeMappingDefinitions_BusinessLevel` | TField |  |  |
| 3 | `SE.MD.MAP.APPLICATION` | `SeMappingDefinitions_MapApplication` |  |  |  |
| 4 | `SE.MD.MAP.LEVEL` | `SeMappingDefinitions_MapLevel` |  |  |  |
| 5 | `SE.MD.RESERVED.5` | `SeMappingDefinitions_Reserved5` | TField |  |  |
| 6 | `SE.MD.RESERVED.4` | `SeMappingDefinitions_Reserved4` | TField |  |  |
| 7 | `SE.MD.RESERVED.3` | `SeMappingDefinitions_Reserved3` | TField |  |  |
| 8 | `SE.MD.RESERVED.2` | `SeMappingDefinitions_Reserved2` | TField |  |  |
| 9 | `SE.MD.RESERVED.1` | `SeMappingDefinitions_Reserved1` | TField |  |  |
| 10 | `SE.MD.RECORD.STATUS` | `SeMappingDefinitions_RecordStatus` | String |  |  |
| 11 | `SE.MD.CURR.NO` | `SeMappingDefinitions_CurrNo` | String |  |  |
| 12 | `SE.MD.INPUTTER` | `SeMappingDefinitions_Inputter` |  |  |  |
| 13 | `SE.MD.DATE.TIME` | `SeMappingDefinitions_DateTime` |  |  |  |
| 14 | `SE.MD.AUTHORISER` | `SeMappingDefinitions_Authoriser` | String |  |  |
| 15 | `SE.MD.CO.CODE` | `SeMappingDefinitions_CoCode` | String |  |  |
| 16 | `SE.MD.DEPT.CODE` | `SeMappingDefinitions_DeptCode` | String |  |  |
| 17 | `SE.MD.AUDITOR.CODE` | `SeMappingDefinitions_AuditorCode` | String |  |  |
| 18 | `SE.MD.AUDIT.DATE.TIME` | `SeMappingDefinitions_AuditDateTime` | String |  |  |
