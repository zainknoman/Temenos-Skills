# AUTO.LOC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AUTO.LOC.PARAMETER` in `CALOCR_LineOfCredit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ALOC.DESCRIPTION` | `AutoLocParameter_Description` | TField |  | The purpose of this field is used to define the description of the table and the record.Allowed values are 65 alphanumeric characters. |
| 2 | `ALOC.ACTIVITY` | `AutoLocParameter_Activity` |  |  |  |
| 3 | `ALOC.PROPERTY` | `AutoLocParameter_Property` |  |  |  |
| 4 | `ALOC.FIELD.NAME` | `AutoLocParameter_FieldName` |  |  |  |
| 5 | `ALOC.FIELD.VALUE` | `AutoLocParameter_FieldValue` |  |  |  |
| 6 | `ALOC.CONV.RTN` | `AutoLocParameter_ConvRtn` |  |  |  |
| 7 | `ALOC.MAND.PROPERTY` | `AutoLocParameter_MandProperty` |  |  |  |
| 8 | `ALOC.MAND.FIELD` | `AutoLocParameter_MandField` |  |  |  |
| 9 | `ALOC.RESERVED.10` | `AutoLocParameter_Reserved10` | TField |  |  |
| 10 | `ALOC.RESERVED.9` | `AutoLocParameter_Reserved9` | TField |  |  |
| 11 | `ALOC.RESERVED.8` | `AutoLocParameter_Reserved8` | TField |  |  |
| 12 | `ALOC.RESERVED.7` | `AutoLocParameter_Reserved7` | TField |  |  |
| 13 | `ALOC.RESERVED.6` | `AutoLocParameter_Reserved6` | TField |  |  |
| 14 | `ALOC.RESERVED.5` | `AutoLocParameter_Reserved5` | TField |  |  |
| 15 | `ALOC.RESERVED.4` | `AutoLocParameter_Reserved4` | TField |  |  |
| 16 | `ALOC.RESERVED.3` | `AutoLocParameter_Reserved3` | TField |  |  |
| 17 | `ALOC.RESERVED.2` | `AutoLocParameter_Reserved2` | TField |  |  |
| 18 | `ALOC.RESERVED.1` | `AutoLocParameter_Reserved1` | TField |  |  |
| 19 | `ALOC.RECORD.STATUS` | `AutoLocParameter_RecordStatus` | String |  |  |
| 20 | `ALOC.CURR.NO` | `AutoLocParameter_CurrNo` | String |  |  |
| 21 | `ALOC.INPUTTER` | `AutoLocParameter_Inputter` |  |  |  |
| 22 | `ALOC.DATE.TIME` | `AutoLocParameter_DateTime` |  |  |  |
| 23 | `ALOC.AUTHORISER` | `AutoLocParameter_Authoriser` | String |  |  |
| 24 | `ALOC.CO.CODE` | `AutoLocParameter_CoCode` | String |  |  |
| 25 | `ALOC.DEPT.CODE` | `AutoLocParameter_DeptCode` | String |  |  |
| 26 | `ALOC.AUDITOR.CODE` | `AutoLocParameter_AuditorCode` | String |  |  |
| 27 | `ALOC.AUDIT.DATE.TIME` | `AutoLocParameter_AuditDateTime` | String |  |  |
