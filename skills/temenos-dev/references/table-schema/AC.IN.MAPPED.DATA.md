# AC.IN.MAPPED.DATA — Table Schema

> Source: `INSERTS/I_F.AC.IN.MAPPED.DATA` in `INCMMS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.IMD.APPLICATION` | `AcInMappedData_Application` | TField |  | Application name from DE.MESSAGE. |
| 2 | `AC.IMD.FLD.NAMES` | `AcInMappedData_FldNames` | TField |  | Field names from AC.IN.EVENT.DATA. |
| 3 | `AC.IMD.FLD.VALUES` | `AcInMappedData_FldValues` | TField |  | Field names from AC.IN.EVENT.DATA. |
| 4 | `AC.IMD.GENERATED.BY` | `AcInMappedData_GeneratedBy` | TField |  |  |
| 5 | `AC.IMD.RESERVED.10` | `AcInMappedData_Reserved10` | TField |  |  |
| 6 | `AC.IMD.RESERVED.9` | `AcInMappedData_Reserved9` | TField |  |  |
| 7 | `AC.IMD.RESERVED.8` | `AcInMappedData_Reserved8` | TField |  |  |
| 8 | `AC.IMD.RESERVED.7` | `AcInMappedData_Reserved7` | TField |  |  |
| 9 | `AC.IMD.RESERVED.6` | `AcInMappedData_Reserved6` | TField |  |  |
| 10 | `AC.IMD.RESERVED.5` | `AcInMappedData_Reserved5` | TField |  |  |
| 11 | `AC.IMD.RESERVED.4` | `AcInMappedData_Reserved4` | TField |  |  |
| 12 | `AC.IMD.RESERVED.3` | `AcInMappedData_Reserved3` | TField |  |  |
| 13 | `AC.IMD.RESERVED.2` | `AcInMappedData_Reserved2` | TField |  |  |
| 14 | `AC.IMD.RESERVED.1` | `AcInMappedData_Reserved1` | TField |  |  |
| 15 | `AC.IMD.OVERRIDE` | `AcInMappedData_Override` |  |  |  |
| 16 | `AC.IMD.RECORD.STATUS` | `AcInMappedData_RecordStatus` | String |  |  |
| 17 | `AC.IMD.CURR.NO` | `AcInMappedData_CurrNo` | String |  |  |
| 18 | `AC.IMD.INPUTTER` | `AcInMappedData_Inputter` |  |  |  |
| 19 | `AC.IMD.DATE.TIME` | `AcInMappedData_DateTime` |  |  |  |
| 20 | `AC.IMD.AUTHORISER` | `AcInMappedData_Authoriser` | String |  |  |
| 21 | `AC.IMD.CO.CODE` | `AcInMappedData_CoCode` | String |  |  |
| 22 | `AC.IMD.DEPT.CODE` | `AcInMappedData_DeptCode` | String |  |  |
| 23 | `AC.IMD.AUDITOR.CODE` | `AcInMappedData_AuditorCode` | String |  |  |
| 24 | `AC.IMD.AUDIT.DATE.TIME` | `AcInMappedData_AuditDateTime` | String |  |  |
