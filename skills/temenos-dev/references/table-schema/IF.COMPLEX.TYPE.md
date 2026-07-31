# IF.COMPLEX.TYPE — Table Schema

> Source: `INSERTS/I_F.IF.COMPLEX.TYPE` in `IF_FlowCatalog.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IF.API.COMP.FIELD.NAME` | `IfComplexType_FieldName` |  |  |  |
| 2 | `IF.API.COMP.FIELD.TYPE` | `IfComplexType_FieldType` |  |  |  |
| 3 | `IF.API.COMP.DATA.TYPE` | `IfComplexType_DataType` |  |  |  |
| 4 | `IF.API.COMP.RESERVED.1` | `IfComplexType_Reserved1` |  |  |  |
| 5 | `IF.API.COMP.RESERVED.2` | `IfComplexType_Reserved2` |  |  |  |
| 6 | `IF.API.COMP.RESERVED.3` | `IfComplexType_Reserved3` |  |  |  |
| 7 | `IF.API.COMP.RESERVED.4` | `IfComplexType_Reserved4` |  |  |  |
| 8 | `IF.API.COMP.RESERVED.5` | `IfComplexType_Reserved5` |  |  |  |
| 9 | `IF.API.COMP.RESERVED.6` | `IfComplexType_Reserved6` |  |  |  |
| 10 | `IF.API.COMP.RESERVED.7` | `IfComplexType_Reserved7` |  |  |  |
| 11 | `IF.API.COMP.RESERVED.8` | `IfComplexType_Reserved8` |  |  |  |
| 12 | `IF.API.COMP.RESERVED.9` | `IfComplexType_Reserved9` |  |  |  |
| 13 | `IF.API.COMP.RESERVED.10` | `IfComplexType_Reserved10` |  |  |  |
| 14 | `IF.API.COMP.HAS.SUBVALUE` | `IfComplexType_HasSubvalue` | TField |  | Overview This is a non-editable field with the field values as YES (Y) or NO (N). Select Y, if any of the field type is defined with the field type XX&lt; Validation Rules This is a no-input field |
| 15 | `IF.API.COMP.TYPE.STRUCTURE` | `IfComplexType_TypeStructure` | TField |  | Overview This field used to store the structure of the complex type as dynamic array. Validation Rules This is a no-input field |
| 16 | `IF.API.COMP.TYPE.SCHEMA` | `IfComplexType_TypeSchema` | TField |  | Overview This field used to store the structure of the complex type as dynamic schema. Validation Rules This is a no-input field |
| 17 | `IF.API.COMP.RESERVED.11` | `IfComplexType_Reserved11` | TField |  |  |
| 18 | `IF.API.COMP.RESERVED.12` | `IfComplexType_Reserved12` | TField |  |  |
| 19 | `IF.API.COMP.RESERVED.13` | `IfComplexType_Reserved13` | TField |  |  |
| 20 | `IF.API.COMP.RESERVED.14` | `IfComplexType_Reserved14` | TField |  |  |
| 21 | `IF.API.COMP.RESERVED.15` | `IfComplexType_Reserved15` | TField |  |  |
| 22 | `IF.API.COMP.RESERVED.16` | `IfComplexType_Reserved16` | TField |  |  |
| 23 | `IF.API.COMP.RESERVED.17` | `IfComplexType_Reserved17` | TField |  |  |
| 24 | `IF.API.COMP.RESERVED.18` | `IfComplexType_Reserved18` | TField |  |  |
| 25 | `IF.API.COMP.RESERVED.19` | `IfComplexType_Reserved19` | TField |  |  |
| 26 | `IF.API.COMP.RESERVED.20` | `IfComplexType_Reserved20` | TField |  |  |
| 27 | `IF.API.COMP.OVERRIDE` | `IfComplexType_Override` |  |  |  |
| 28 | `IF.API.COMP.RECORD.STATUS` | `IfComplexType_RecordStatus` | String |  |  |
| 29 | `IF.API.COMP.CURR.NO` | `IfComplexType_CurrNo` | String |  |  |
| 30 | `IF.API.COMP.INPUTTER` | `IfComplexType_Inputter` |  |  |  |
| 31 | `IF.API.COMP.DATE.TIME` | `IfComplexType_DateTime` |  |  |  |
| 32 | `IF.API.COMP.AUTHORISER` | `IfComplexType_Authoriser` | String |  |  |
| 33 | `IF.API.COMP.CO.CODE` | `IfComplexType_CoCode` | String |  |  |
| 34 | `IF.API.COMP.DEPT.CODE` | `IfComplexType_DeptCode` | String |  |  |
| 35 | `IF.API.COMP.AUDITOR.CODE` | `IfComplexType_AuditorCode` | String |  |  |
| 36 | `IF.API.COMP.AUDIT.DATE.TIME` | `IfComplexType_AuditDateTime` | String |  |  |
