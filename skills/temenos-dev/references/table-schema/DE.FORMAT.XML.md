# DE.FORMAT.XML — Table Schema

> Source: `INSERTS/I_F.DE.FORMAT.XML` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.XML.DESCRIPTION` | `DeFormatXml_Description` |  |  |  |
| 2 | `DE.XML.DE.MESSAGE.POPN` | `DeFormatXml_DeMessagePopn` | TField | No | When creating a DE.FORMAT.XML record initially, the fields on the record can either be entered manually, populated from DE.MESSAGE or populated from DE.FORMAT.PRINT records. If you wish to populate this record from a DE.MESSAGE record, enter the id of the DE.MESSAGE record in this field. If any fields have been entered already, they will be cleared before being populated with the details from the DE.MESSAGE record. __________________________________________________ (1) Optional input (2) 1-20 type "A" characters (3) Must exist on DE.MESSAGE . |
| 3 | `DE.XML.PRINT.POPN` | `DeFormatXml_PrintPopn` | TField | No | When creating a DE.FORMAT.XML record initially, the fields on the record can either be entered manually, populated from DE.MESSAGE or populated from DE.FORMAT.PRINT records. If you wish to populate this record from a DE.FORMAT.PRINT record, enter the id of the DE.FORMAT.PRINT record in this field. If any fields have been entered already, they will be cleared before being populated with the details from the DE.FORMAT.PRINT record. __________________________________________________ (1) Optional input (2) 1-20 type "A" characters (3) Must exist on DE.FORMAT.PRINT . |
| 4 | `DE.XML.FORM.TYPE` | `DeFormatXml_FormType` | A (alphanumeric) | No | XML form type. __________________________________________________ (1) 1-7 type A (alphanumeric) characters. (Optional input. The system has a 'Default' form type defined on the DE.FORM.TYPE table which is used when this field is left blank.) (2) Must be defined on DE.FORM.TYPE. . |
| 5 | `DE.XML.FIELD.NAME` | `DeFormatXml_FieldName` |  |  |  |
| 6 | `DE.XML.DATA.NAME` | `DeFormatXml_DataName` |  |  |  |
| 7 | `DE.XML.GROUP.END` | `DeFormatXml_GroupEnd` |  |  |  |
| 8 | `DE.XML.TEXT` | `DeFormatXml_Text` |  |  |  |
| 9 | `DE.XML.MULTI` | `DeFormatXml_Multi` |  |  |  |
| 10 | `DE.XML.MULTI.GRP.NAME` | `DeFormatXml_MultiGrpName` |  |  |  |
| 11 | `DE.XML.CONVERSION` | `DeFormatXml_Conversion` |  |  |  |
| 12 | `DE.XML.MASK` | `DeFormatXml_Mask` |  |  |  |
| 13 | `DE.XML.CALCULATION` | `DeFormatXml_Calculation` |  |  |  |
| 14 | `DE.XML.RESERVED.10` | `DeFormatXml_Reserved10` |  |  |  |
| 15 | `DE.XML.RESERVED.9` | `DeFormatXml_Reserved9` |  |  |  |
| 16 | `DE.XML.RESERVED.8` | `DeFormatXml_Reserved8` |  |  |  |
| 17 | `DE.XML.PRODUCE.SCHEMA` | `DeFormatXml_ProduceSchema` | TField | Yes | Schema will be produced when this field is set to YES.When this field is set to YES DATA.NAME is mandatory. Schema produced will be available in file F.DE.XML.SCHEMA. Validations: 1. Can take value YES or NULL. |
| 18 | `DE.XML.RESERVED.6` | `DeFormatXml_Reserved6` | TField |  |  |
| 19 | `DE.XML.RESERVED.5` | `DeFormatXml_Reserved5` | TField |  |  |
| 20 | `DE.XML.RESERVED.4` | `DeFormatXml_Reserved4` | TField |  |  |
| 21 | `DE.XML.RESERVED.3` | `DeFormatXml_Reserved3` | TField |  |  |
| 22 | `DE.XML.LOCAL.REF` | `DeFormatXml_LocalRef` |  |  |  |
| 23 | `DE.XML.OVERRIDE` | `DeFormatXml_Override` |  |  |  |
| 24 | `DE.XML.RECORD.STATUS` | `DeFormatXml_RecordStatus` | String |  |  |
| 25 | `DE.XML.CURR.NO` | `DeFormatXml_CurrNo` | String |  |  |
| 26 | `DE.XML.INPUTTER` | `DeFormatXml_Inputter` |  |  |  |
| 27 | `DE.XML.DATE.TIME` | `DeFormatXml_DateTime` |  |  |  |
| 28 | `DE.XML.AUTHORISER` | `DeFormatXml_Authoriser` | String |  |  |
| 29 | `DE.XML.CO.CODE` | `DeFormatXml_CoCode` | String |  |  |
| 30 | `DE.XML.DEPT.CODE` | `DeFormatXml_DeptCode` | String |  |  |
| 31 | `DE.XML.AUDITOR.CODE` | `DeFormatXml_AuditorCode` | String |  |  |
| 32 | `DE.XML.AUDIT.DATE.TIME` | `DeFormatXml_AuditDateTime` | String |  |  |
