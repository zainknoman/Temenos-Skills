# FS.MAPPING.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.MAPPING.DETAILS` in `FS_ApplicationFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MAP.DET.API.NAME` | `FsMappingDetails_ApiName` |  |  |  |
| 2 | `MAP.DET.SYS.SINGLE.MULT` | `FsMappingDetails_SysSingleMult` |  |  |  |
| 3 | `MAP.DET.SOURCE` | `FsMappingDetails_Source` |  |  |  |
| 4 | `MAP.DET.TARGET` | `FsMappingDetails_Target` |  |  |  |
| 5 | `MAP.DET.PROCESS.API` | `FsMappingDetails_ProcessApi` | TField |  |  |
| 6 | `MAP.DET.HOT.FIELD.IN.FIELD` | `FsMappingDetails_HotFieldInField` |  |  |  |
| 7 | `MAP.DET.HOT.FIELD.IN.OPERATOR` | `FsMappingDetails_HotFieldInOperator` |  |  |  |
| 8 | `MAP.DET.HOT.FIELD.IN.VALUE` | `FsMappingDetails_HotFieldInValue` |  |  |  |
| 9 | `MAP.DET.HOT.FIELD.OUT.FIELD` | `FsMappingDetails_HotFieldOutField` |  |  |  |
| 10 | `MAP.DET.HOT.FIELD.OUT.VALUE` | `FsMappingDetails_HotFieldOutValue` |  |  |  |
| 11 | `MAP.DET.RESERVED9` | `FsMappingDetails_Reserved9` | TField |  |  |
| 12 | `MAP.DET.RESERVED8` | `FsMappingDetails_Reserved8` | TField |  |  |
| 13 | `MAP.DET.RESERVED7` | `FsMappingDetails_Reserved7` | TField |  |  |
| 14 | `MAP.DET.RESERVED6` | `FsMappingDetails_Reserved6` | TField |  |  |
| 15 | `MAP.DET.RESERVED5` | `FsMappingDetails_Reserved5` | TField |  |  |
| 16 | `MAP.DET.RESERVED4` | `FsMappingDetails_Reserved4` | TField |  |  |
| 17 | `MAP.DET.RESERVED3` | `FsMappingDetails_Reserved3` | TField |  |  |
| 18 | `MAP.DET.RESERVED2` | `FsMappingDetails_Reserved2` | TField |  |  |
| 19 | `MAP.DET.RESERVED1` | `FsMappingDetails_Reserved1` | TField |  |  |
| 20 | `MAP.DET.LOCAL.REF` | `FsMappingDetails_LocalRef` |  |  |  |
| 21 | `MAP.DET.OVERRIDE` | `FsMappingDetails_Override` |  |  |  |
| 22 | `MAP.DET.RECORD.STATUS` | `FsMappingDetails_RecordStatus` | String |  |  |
| 23 | `MAP.DET.CURR.NO` | `FsMappingDetails_CurrNo` | String |  |  |
| 24 | `MAP.DET.INPUTTER` | `FsMappingDetails_Inputter` |  |  |  |
| 25 | `MAP.DET.DATE.TIME` | `FsMappingDetails_DateTime` |  |  |  |
| 26 | `MAP.DET.AUTHORISER` | `FsMappingDetails_Authoriser` | String |  |  |
| 27 | `MAP.DET.CO.CODE` | `FsMappingDetails_CoCode` | String |  |  |
| 28 | `MAP.DET.DEPT.CODE` | `FsMappingDetails_DeptCode` | String |  |  |
| 29 | `MAP.DET.AUDITOR.CODE` | `FsMappingDetails_AuditorCode` | String |  |  |
| 30 | `MAP.DET.AUDIT.DATE.TIME` | `FsMappingDetails_AuditDateTime` | String |  |  |
