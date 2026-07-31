# PI.ISO.EXTERNAL.CODE — Table Schema

> Source: `INSERTS/I_F.PI.ISO.EXTERNAL.CODE` in `PI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PI.ISO.CODE` | `PiIsoExternalCode_Code` |  |  |  |
| 2 | `PI.ISO.CODE.NAME` | `PiIsoExternalCode_CodeName` |  |  |  |
| 3 | `PI.ISO.CODE.DEFINITION` | `PiIsoExternalCode_CodeDefinition` |  |  |  |
| 4 | `PI.ISO.REQUESTER` | `PiIsoExternalCode_Requester` |  |  |  |
| 5 | `PI.ISO.STATUS` | `PiIsoExternalCode_Status` |  |  |  |
| 6 | `PI.ISO.LAST.UPDATED` | `PiIsoExternalCode_LastUpdated` |  |  |  |
| 7 | `PI.ISO.CREATION.DATE` | `PiIsoExternalCode_CreationDate` |  |  |  |
| 8 | `PI.ISO.OVERRIDE` | `PiIsoExternalCode_Override` |  |  |  |
| 9 | `PI.ISO.RECORD.STATUS` | `PiIsoExternalCode_RecordStatus` | String |  |  |
| 10 | `PI.ISO.CURR.NO` | `PiIsoExternalCode_CurrNo` | String |  |  |
| 11 | `PI.ISO.INPUTTER` | `PiIsoExternalCode_Inputter` |  |  |  |
| 12 | `PI.ISO.DATE.TIME` | `PiIsoExternalCode_DateTime` |  |  |  |
| 13 | `PI.ISO.AUTHORISER` | `PiIsoExternalCode_Authoriser` | String |  |  |
| 14 | `PI.ISO.CO.CODE` | `PiIsoExternalCode_CoCode` | String |  |  |
| 15 | `PI.ISO.DEPT.CODE` | `PiIsoExternalCode_DeptCode` | String |  |  |
| 16 | `PI.ISO.AUDITOR.CODE` | `PiIsoExternalCode_AuditorCode` | String |  |  |
| 17 | `PI.ISO.AUDIT.DATE.TIME` | `PiIsoExternalCode_AuditDateTime` | String |  |  |
| 18 | `PI.ISO.REPLACED.BY` | `PiIsoExternalCode_ReplacedBy` |  |  |  |
| 19 | `PI.ISO.MAPPING.STANDARDS1` | `PiIsoExternalCode_MappingStandards1` |  |  |  |
| 20 | `PI.ISO.MAPPING.VALUE1` | `PiIsoExternalCode_MappingValue1` |  |  |  |
| 21 | `PI.ISO.MAPPING.STANDARDS2` | `PiIsoExternalCode_MappingStandards2` |  |  |  |
| 22 | `PI.ISO.MAPPING.VALUE2` | `PiIsoExternalCode_MappingValue2` |  |  |  |
| 23 | `PI.ISO.ADDITIONAL.INFORMATION` | `PiIsoExternalCode_AdditionalInformation` |  |  |  |
| 24 | `PI.ISO.RESERVED.1` | `PiIsoExternalCode_Reserved1` |  |  |  |
| 25 | `PI.ISO.RESERVED.2` | `PiIsoExternalCode_Reserved2` |  |  |  |
| 26 | `PI.ISO.RESERVED.3` | `PiIsoExternalCode_Reserved3` |  |  |  |
| 27 | `PI.ISO.RESERVED.4` | `PiIsoExternalCode_Reserved4` | TField |  |  |
| 28 | `PI.ISO.RESERVED.5` | `PiIsoExternalCode_Reserved5` | TField |  |  |
