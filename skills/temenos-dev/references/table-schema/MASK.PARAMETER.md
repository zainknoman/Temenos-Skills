# MASK.PARAMETER — Table Schema

> Source: `INSERTS/I_F.MASK.PARAMETER` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MASK.PAR.APPLICATION` | `MaskParameter_Application` |  |  |  |
| 2 | `MASK.PAR.APPL.FIELD` | `MaskParameter_ApplField` |  |  |  |
| 3 | `MASK.PAR.RESERVED.15` | `MaskParameter_Reserved15` |  |  |  |
| 4 | `MASK.PAR.RESERVED.14` | `MaskParameter_Reserved14` |  |  |  |
| 5 | `MASK.PAR.RESERVED.13` | `MaskParameter_Reserved13` |  |  |  |
| 6 | `MASK.PAR.RESERVED.12` | `MaskParameter_Reserved12` |  |  |  |
| 7 | `MASK.PAR.RESERVED.11` | `MaskParameter_Reserved11` |  |  |  |
| 8 | `MASK.PAR.USER.GROUP` | `MaskParameter_UserGroup` |  |  |  |
| 9 | `MASK.PAR.MASK.TYPE` | `MaskParameter_MaskType` | TField | Yes | This field shows how the masked field values should be reflected on applications/reports Mandatory Field, Drop down Field Dropdown values are 1 - Only last 4 digits 2 - Disp last 4 digits; Mask preceding 3 - Mask all digits |
| 10 | `MASK.PAR.MASK.CHAR` | `MaskParameter_MaskChar` | TField | Yes | The characters used to masked the data can be defined in this field Mandatory Field, Text Field |
| 11 | `MASK.PAR.RESERVED.10` | `MaskParameter_Reserved10` | TField |  |  |
| 12 | `MASK.PAR.RESERVED.9` | `MaskParameter_Reserved9` | TField |  |  |
| 13 | `MASK.PAR.RESERVED.8` | `MaskParameter_Reserved8` | TField |  |  |
| 14 | `MASK.PAR.RESERVED.7` | `MaskParameter_Reserved7` | TField |  |  |
| 15 | `MASK.PAR.RESERVED.6` | `MaskParameter_Reserved6` | TField |  |  |
| 16 | `MASK.PAR.RESERVED.5` | `MaskParameter_Reserved5` | TField |  |  |
| 17 | `MASK.PAR.RESERVED.4` | `MaskParameter_Reserved4` | TField |  |  |
| 18 | `MASK.PAR.RESERVED.3` | `MaskParameter_Reserved3` | TField |  |  |
| 19 | `MASK.PAR.RESERVED.2` | `MaskParameter_Reserved2` | TField |  |  |
| 20 | `MASK.PAR.RESERVED.1` | `MaskParameter_Reserved1` | TField |  |  |
| 21 | `MASK.PAR.LOCAL.REF` | `MaskParameter_LocalRef` |  |  |  |
| 22 | `MASK.PAR.RECORD.STATUS` | `MaskParameter_RecordStatus` | String |  |  |
| 23 | `MASK.PAR.CURR.NO` | `MaskParameter_CurrNo` | String |  |  |
| 24 | `MASK.PAR.INPUTTER` | `MaskParameter_Inputter` |  |  |  |
| 25 | `MASK.PAR.DATE.TIME` | `MaskParameter_DateTime` |  |  |  |
| 26 | `MASK.PAR.AUTHORISER` | `MaskParameter_Authoriser` | String |  |  |
| 27 | `MASK.PAR.CO.CODE` | `MaskParameter_CoCode` | String |  |  |
| 28 | `MASK.PAR.DEPT.CODE` | `MaskParameter_DeptCode` | String |  |  |
| 29 | `MASK.PAR.AUDITOR.CODE` | `MaskParameter_AuditorCode` | String |  |  |
| 30 | `MASK.PAR.AUDIT.DATE.TIME` | `MaskParameter_AuditDateTime` | String |  |  |
