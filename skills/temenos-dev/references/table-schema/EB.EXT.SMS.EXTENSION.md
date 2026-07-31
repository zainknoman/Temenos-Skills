# EB.EXT.SMS.EXTENSION — Table Schema

> Source: `INSERTS/I_F.EB.EXT.SMS.EXTENSION` in `EB_Security.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.EXT.EXT.ATTR.NAME` | `EbExtSmsExtension_ExtAttrName` |  |  |  |
| 2 | `EB.EXT.SOURCE.APPL.FIELD` | `EbExtSmsExtension_SourceApplField` |  |  |  |
| 3 | `EB.EXT.LINK.APPLICATION` | `EbExtSmsExtension_LinkApplication` |  |  |  |
| 4 | `EB.EXT.LINK.APPL.FIELD` | `EbExtSmsExtension_LinkApplField` |  |  |  |
| 5 | `EB.EXT.LINK.DATA.API` | `EbExtSmsExtension_LinkDataApi` |  |  |  |
| 6 | `EB.EXT.LINK.RESERVED.5` | `EbExtSmsExtension_LinkReserved5` |  |  |  |
| 7 | `EB.EXT.LINK.RESERVED.4` | `EbExtSmsExtension_LinkReserved4` |  |  |  |
| 8 | `EB.EXT.LINK.RESERVED.3` | `EbExtSmsExtension_LinkReserved3` |  |  |  |
| 9 | `EB.EXT.LINK.RESERVED.2` | `EbExtSmsExtension_LinkReserved2` |  |  |  |
| 10 | `EB.EXT.LINK.RESERVED.1` | `EbExtSmsExtension_LinkReserved1` |  |  |  |
| 11 | `EB.EXT.CUSTOM.DATA.API` | `EbExtSmsExtension_CustomDataApi` | TField |  | API support to provide content - both attribute names and values as key-value pairs Validation Rules: Should be a valid EB.API record When CUSTOM.DATA.API is specified, other fields cannot hold a value as this API will provide data for the ID application |
| 12 | `EB.EXT.EXTERNAL.VARIABLE` | `EbExtSmsExtension_ExtExternalVariable` |  |  |  |
| 13 | `EB.EXT.MULTI.VALUE` | `EbExtSmsExtension_ExtMultiValue` |  |  |  |
| 14 | `EB.EXT.DATA.TYPE` | `EbExtSmsExtension_ExtDataType` |  |  |  |
| 15 | `EB.EXT.RESERVED7` | `EbExtSmsExtension_Reserved7` | TField |  |  |
| 16 | `EB.EXT.RESERVED6` | `EbExtSmsExtension_Reserved6` | TField |  |  |
| 17 | `EB.EXT.RESERVED5` | `EbExtSmsExtension_Reserved5` | TField |  |  |
| 18 | `EB.EXT.RESERVED4` | `EbExtSmsExtension_Reserved4` | TField |  |  |
| 19 | `EB.EXT.RESERVED3` | `EbExtSmsExtension_Reserved3` | TField |  |  |
| 20 | `EB.EXT.RESERVED2` | `EbExtSmsExtension_Reserved2` | TField |  |  |
| 21 | `EB.EXT.RESERVED1` | `EbExtSmsExtension_Reserved1` | TField |  |  |
| 22 | `EB.EXT.OVERRIDE` | `EbExtSmsExtension_Override` |  |  |  |
| 23 | `EB.EXT.RECORD.STATUS` | `EbExtSmsExtension_RecordStatus` | String |  |  |
| 24 | `EB.EXT.CURR.NO` | `EbExtSmsExtension_CurrNo` | String |  |  |
| 25 | `EB.EXT.INPUTTER` | `EbExtSmsExtension_Inputter` |  |  |  |
| 26 | `EB.EXT.DATE.TIME` | `EbExtSmsExtension_DateTime` |  |  |  |
| 27 | `EB.EXT.AUTHORISER` | `EbExtSmsExtension_Authoriser` | String |  |  |
| 28 | `EB.EXT.CO.CODE` | `EbExtSmsExtension_CoCode` | String |  |  |
| 29 | `EB.EXT.DEPT.CODE` | `EbExtSmsExtension_DeptCode` | String |  |  |
| 30 | `EB.EXT.AUDITOR.CODE` | `EbExtSmsExtension_AuditorCode` | String |  |  |
| 31 | `EB.EXT.AUDIT.DATE.TIME` | `EbExtSmsExtension_AuditDateTime` | String |  |  |
