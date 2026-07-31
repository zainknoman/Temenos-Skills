# AA.STANDARD.FIELDS.CONVERSION — Table Schema

> Source: `INSERTS/I_F.AA.STANDARD.FIELDS.CONVERSION` in `AF_ClassFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SFC.DESCRIPTION` | `AaStandardFieldsConversion_Description` | TField | Yes | This field should contain a description of the conversion program and is displayed on the screen whenever the conversion is run. Validation Rules: Mandatory field which accepts 100 alphanumeric characters |
| 2 | `AA.SFC.CLASS.TYPE` | `AaStandardFieldsConversion_ClassType` | TField | Yes | It should be a valid AA.CLASS.TYPE record wherein the changed standard fields are used in the system. Validation Rules: This is a mandatory field Should be a valid record in AA.CLASS.TYPE |
| 3 | `AA.SFC.STANDARD.FIELD.TYPE` | `AaStandardFieldsConversion_StandardFieldType` | TField | Yes | This field should contain a valid standard field type from the class type mentioned in the field CLASS.TYPE This would ideally be the changed standard field type, Validation Rules: 1. This is a mandatory field 2. Should be a valid standard field type of the class type mentioned in CLASS.TYPE field |
| 4 | `AA.SFC.CONVERSION.TYPE` | `AaStandardFieldsConversion_ConversionType` |  |  |  |
| 5 | `AA.SFC.NEIGHBOUR.FIELD` | `AaStandardFieldsConversion_NeighbourField` |  |  |  |
| 6 | `AA.SFC.RESERVED.12` | `AaStandardFieldsConversion_Reserved12` |  |  |  |
| 7 | `AA.SFC.RESERVED.11` | `AaStandardFieldsConversion_Reserved11` |  |  |  |
| 8 | `AA.SFC.NEW.FIELD` | `AaStandardFieldsConversion_NewField` |  |  |  |
| 9 | `AA.SFC.NEW.FLD.ASSOC.CODE` | `AaStandardFieldsConversion_NewFldAssocCode` |  |  |  |
| 10 | `AA.SFC.RESERVED.9` | `AaStandardFieldsConversion_Reserved9` | TField |  |  |
| 11 | `AA.SFC.RESERVED.8` | `AaStandardFieldsConversion_Reserved8` | TField |  |  |
| 12 | `AA.SFC.OLD.FIELD.NAME` | `AaStandardFieldsConversion_OldFieldName` |  |  |  |
| 13 | `AA.SFC.NEW.FIELD.NAME` | `AaStandardFieldsConversion_NewFieldName` |  |  |  |
| 14 | `AA.SFC.RENAME.FLD.ASSOC.CODE` | `AaStandardFieldsConversion_RenameFldAssocCode` |  |  |  |
| 15 | `AA.SFC.RESERVED.6` | `AaStandardFieldsConversion_Reserved6` | TField |  |  |
| 16 | `AA.SFC.T24.RELEASE` | `AaStandardFieldsConversion_T24Release` | TField |  | Holds the release information of the AA.STANDARD.FIELDS.CONVERSION record. Validation Rules: 1. Allows up to three characters. 2. The RELEASE must be in &quot;Rnn&quot; (e.g. R18) |
| 17 | `AA.SFC.VERIFIED` | `AaStandardFieldsConversion_Verified` | TField |  | System maintained field. It will be auto populated with YES after verifying the record. |
| 18 | `AA.SFC.REBUILD.FIELD` | `AaStandardFieldsConversion_RebuildField` |  |  |  |
| 19 | `AA.SFC.RESERVED.4` | `AaStandardFieldsConversion_Reserved4` | TField |  |  |
| 20 | `AA.SFC.RESERVED.3` | `AaStandardFieldsConversion_Reserved3` | TField |  |  |
| 21 | `AA.SFC.RESERVED.2` | `AaStandardFieldsConversion_Reserved2` | TField |  |  |
| 22 | `AA.SFC.RESERVED.1` | `AaStandardFieldsConversion_Reserved1` | TField |  |  |
| 23 | `AA.SFC.RECORD.STATUS` | `AaStandardFieldsConversion_RecordStatus` | String |  |  |
| 24 | `AA.SFC.CURR.NO` | `AaStandardFieldsConversion_CurrNo` | String |  |  |
| 25 | `AA.SFC.INPUTTER` | `AaStandardFieldsConversion_Inputter` |  |  |  |
| 26 | `AA.SFC.DATE.TIME` | `AaStandardFieldsConversion_DateTime` |  |  |  |
| 27 | `AA.SFC.AUTHORISER` | `AaStandardFieldsConversion_Authoriser` | String |  |  |
| 28 | `AA.SFC.CO.CODE` | `AaStandardFieldsConversion_CoCode` | String |  |  |
| 29 | `AA.SFC.DEPT.CODE` | `AaStandardFieldsConversion_DeptCode` | String |  |  |
| 30 | `AA.SFC.AUDITOR.CODE` | `AaStandardFieldsConversion_AuditorCode` | String |  |  |
| 31 | `AA.SFC.AUDIT.DATE.TIME` | `AaStandardFieldsConversion_AuditDateTime` | String |  |  |
