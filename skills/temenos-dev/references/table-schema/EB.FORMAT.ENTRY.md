# EB.FORMAT.ENTRY — Table Schema

> Source: `INSERTS/I_F.EB.FORMAT.ENTRY` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.FMT.SHORT.DESC` | `EbFormatEntry_ShortDesc` | TField | Yes | A Short Description of the purpose of the format record. Validation Rules: 15 Character Max. Mandatory Onsite changes will be disallowed if the record type is INTERNAL. |
| 2 | `EB.FMT.FMT.DESCRIPTION` | `EbFormatEntry_FmtDescription` |  |  |  |
| 3 | `EB.FMT.DESCRIPTION` | `EbFormatEntry_Description` |  |  |  |
| 4 | `EB.FMT.EXTRACTION` | `EbFormatEntry_Extraction` |  |  |  |
| 5 | `EB.FMT.CONVERSION` | `EbFormatEntry_Conversion` |  |  |  |
| 6 | `EB.FMT.PLACEMENT` | `EbFormatEntry_Placement` |  |  |  |
| 7 | `EB.FMT.RECORD.TYPE` | `EbFormatEntry_RecordType` | TField |  | Is this record a record used internally within the core of a T24 module, or has the record be setup to be used as part of a locally developed routine. Validation Rules: INTERNAL or EXTERNAL Records marked as INTERNAL can only be updated by Temenos&amp;trade; Development. Records marked as EXTERNAL can be updated by anyone. Records can only be set as INTERNAL within Temenos&amp;trade; Development. |
| 8 | `EB.FMT.VALIDATE` | `EbFormatEntry_Validate` | TField |  | YES or NO or can be left NULL If set to YES then check is done to ensure that only valid Application/Field name is entered in Named Placement, Extraction and Link file conversion |
| 9 | `EB.FMT.EXTRACT.TABLE` | `EbFormatEntry_ExtractTable` | TField |  | Allows the user to specify the table of all 'extraction' definitions. If specified, the user can use the new 'context' format for extraction. |
| 10 | `EB.FMT.PLACEMENT.TABLE` | `EbFormatEntry_PlacementTable` | TField |  | Allows the user to specify the table of the 'placement' definitions. If specified, the user can use the new 'context' format for placement |
| 11 | `EB.FMT.MAPPING.DIRECTION` | `EbFormatEntry_MappingDirection` | TField |  | By default (i.e. a null value), mapping is specified as uni-directional and will always go from Extraction to Placement. However this field allows the user to specify the definition as being bi-directional. When this is done, then CONVERSION is not allowed as by definition a conversion specification can only be one way. |
| 12 | `EB.FMT.EXTRACT.ENTITY` | `EbFormatEntry_ExtractEntity` | TField |  | Allows the user to specify the entity of all 'extraction' definitions. If specified, the user can use the new 'context' format for extraction. Validation Rules: This field value is validated against the ENTITY field in EB.MDAL.ENTITIES application |
| 13 | `EB.FMT.RESERVED.05` | `EbFormatEntry_Reserved05` | TField |  | Reserved for future use. Validation Rules: None |
| 14 | `EB.FMT.RESERVED.04` | `EbFormatEntry_Reserved04` | TField |  | Reserved for future use. Validation Rules: None |
| 15 | `EB.FMT.RESERVED.03` | `EbFormatEntry_Reserved03` | TField |  | Reserved for future use. Validation Rules: None |
| 16 | `EB.FMT.RESERVED.02` | `EbFormatEntry_Reserved02` | TField |  | Insert text here Validation Rules: Rule 1 Rule 2 |
| 17 | `EB.FMT.OVERRIDE` | `EbFormatEntry_Override` |  |  |  |
| 18 | `EB.FMT.RECORD.STATUS` | `EbFormatEntry_RecordStatus` | String |  |  |
| 19 | `EB.FMT.CURR.NO` | `EbFormatEntry_CurrNo` | String |  |  |
| 20 | `EB.FMT.INPUTTER` | `EbFormatEntry_Inputter` |  |  |  |
| 21 | `EB.FMT.DATE.TIME` | `EbFormatEntry_DateTime` |  |  |  |
| 22 | `EB.FMT.AUTHORISER` | `EbFormatEntry_Authoriser` | String |  |  |
| 23 | `EB.FMT.CO.CODE` | `EbFormatEntry_CoCode` | String |  |  |
| 24 | `EB.FMT.DEPT.CODE` | `EbFormatEntry_DeptCode` | String |  |  |
| 25 | `EB.FMT.AUDITOR.CODE` | `EbFormatEntry_AuditorCode` | String |  |  |
| 26 | `EB.FMT.AUDIT.DATE.TIME` | `EbFormatEntry_AuditDateTime` | String |  |  |
