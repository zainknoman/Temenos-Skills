# DE.ALT.CHARS — Table Schema

> Source: `INSERTS/I_F.DE.ALT.CHARS` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.ALTC.DESCRIPTION` | `DeAltChars_Description` |  |  |  |
| 2 | `DE.ALTC.VALID.ASCII.TABLE` | `DeAltChars_ValidAsciiTable` | TField | Yes | Field to specify valid ASCII.VAL.TABLE. The values entered in field ALTER.CHAR.CODE will be validated to check if its valid entry in ASCII.VAL.TABLE specified here Validation Rules: Valid record in ASCII.VAL.TABLE (Mandatory input.) |
| 3 | `DE.ALTC.FORMATTING.CHECK` | `DeAltChars_FormattingCheck` | TField |  | Specifies whether the string, as a whole is to be checked against ASCII.VAL.TABLE specified in field VALID.ASCII.TABLE. Validation Rules: YES or NO field. Defaulted to 'NO' |
| 4 | `DE.ALTC.LOCAL.CHAR.CODE` | `DeAltChars_LocalCharCode` |  |  |  |
| 5 | `DE.ALTC.ALTER.CHAR.CODE` | `DeAltChars_AlterCharCode` |  |  |  |
| 6 | `DE.ALTC.CHAR.POSITION` | `DeAltChars_CharPosition` |  |  |  |
| 7 | `DE.ALTC.DEF.ALT.CHAR.CODE` | `DeAltChars_DefAltCharCode` | TField |  |  |
| 8 | `DE.ALTC.RESERVED.4` | `DeAltChars_Reserved4` | TField |  | This field is reserved for future use. |
| 9 | `DE.ALTC.RESERVED.3` | `DeAltChars_Reserved3` | TField |  | This field is reserved for future use. |
| 10 | `DE.ALTC.RESERVED.2` | `DeAltChars_Reserved2` | TField |  | This field is reserved for future use. |
| 11 | `DE.ALTC.RESERVED.1` | `DeAltChars_Reserved1` | TField |  | This field is reserved for future use. |
| 12 | `DE.ALTC.LOCAL.REF` | `DeAltChars_LocalRef` |  |  |  |
| 13 | `DE.ALTC.OVERRIDE` | `DeAltChars_Override` |  |  |  |
| 14 | `DE.ALTC.RECORD.STATUS` | `DeAltChars_RecordStatus` | String |  |  |
| 15 | `DE.ALTC.CURR.NO` | `DeAltChars_CurrNo` | String |  |  |
| 16 | `DE.ALTC.INPUTTER` | `DeAltChars_Inputter` |  |  |  |
| 17 | `DE.ALTC.DATE.TIME` | `DeAltChars_DateTime` |  |  |  |
| 18 | `DE.ALTC.AUTHORISER` | `DeAltChars_Authoriser` | String |  |  |
| 19 | `DE.ALTC.CO.CODE` | `DeAltChars_CoCode` | String |  |  |
| 20 | `DE.ALTC.DEPT.CODE` | `DeAltChars_DeptCode` | String |  |  |
| 21 | `DE.ALTC.AUDITOR.CODE` | `DeAltChars_AuditorCode` | String |  |  |
| 22 | `DE.ALTC.AUDIT.DATE.TIME` | `DeAltChars_AuditDateTime` | String |  |  |
