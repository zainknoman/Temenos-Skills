# EB.PARTIAL.SIGN.PARAM — Table Schema

> Source: `INSERTS/I_F.EB.PARTIAL.SIGN.PARAM` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.PSP.DESCRIPTION` | `EbPartialSignParam_Description` |  |  |  |
| 2 | `EB.PSP.APPLICATION` | `EbPartialSignParam_Application` | TField | Yes | APPLICATION A valid T24 APPLICATION. The Application for which the set of fields are to be defined for partial signing. Validation Rules: Mandatory Input Must be a valid T24 APPLICATION. |
| 3 | `EB.PSP.FIELDS` | `EbPartialSignParam_Fields` |  |  |  |
| 4 | `EB.PSP.LINKED.APPL` | `EbPartialSignParam_LinkedAppl` |  |  |  |
| 5 | `EB.PSP.LINKED.BY` | `EbPartialSignParam_LinkedBy` |  |  |  |
| 6 | `EB.PSP.LINKED.APP.FIELDS` | `EbPartialSignParam_LinkedAppFields` |  |  |  |
| 7 | `EB.PSP.LINKED.APP.FIELD.CONDFLD` | `EbPartialSignParam_LinkedAppFieldCondFld` |  |  |  |
| 8 | `EB.PSP.LINKED.APP.FIELD.CONDOPR` | `EbPartialSignParam_LinkedAppFieldCondOpr` |  |  |  |
| 9 | `EB.PSP.LINKED.APP.FIELD.CONDVAL` | `EbPartialSignParam_LinkedAppFieldCondVal` |  |  |  |
| 10 | `EB.PSP.RESERVED.7` | `EbPartialSignParam_Reserved7` |  |  |  |
| 11 | `EB.PSP.RESERVED.6` | `EbPartialSignParam_Reserved6` |  |  |  |
| 12 | `EB.PSP.FIELD.DELIM` | `EbPartialSignParam_FieldDelim` | TField |  | This field should be entered with a symbol or a group of characters that needs to be used as a separator between different field data. That particular character will be sent as field delimiter in message request. |
| 13 | `EB.PSP.VM.DELIM` | `EbPartialSignParam_VmDelim` | TField |  | This field should be entered with a symbol or a group of characters that needs to be replaced against VM in field data for multi-value fields. That particular character will sent as VM delimiter in message request. |
| 14 | `EB.PSP.SM.DELIM` | `EbPartialSignParam_SmDelim` | TField |  | This field should be entered with a symbol or a group of characters that needs to be replaced against SM in field data for sub-value fields. That particular character will sent as SM delimiter in message request. |
| 15 | `EB.PSP.RESERVED.5` | `EbPartialSignParam_Reserved5` | TField |  |  |
| 16 | `EB.PSP.RESERVED.4` | `EbPartialSignParam_Reserved4` | TField |  |  |
| 17 | `EB.PSP.RESERVED.3` | `EbPartialSignParam_Reserved3` | TField |  |  |
| 18 | `EB.PSP.RESERVED.2` | `EbPartialSignParam_Reserved2` | TField |  |  |
| 19 | `EB.PSP.RESERVED.1` | `EbPartialSignParam_Reserved1` | TField |  |  |
| 20 | `EB.PSP.OVERRIDE` | `EbPartialSignParam_Override` |  |  |  |
| 21 | `EB.PSP.RECORD.STATUS` | `EbPartialSignParam_RecordStatus` | String |  |  |
| 22 | `EB.PSP.CURR.NO` | `EbPartialSignParam_CurrNo` | String |  |  |
| 23 | `EB.PSP.INPUTTER` | `EbPartialSignParam_Inputter` |  |  |  |
| 24 | `EB.PSP.DATE.TIME` | `EbPartialSignParam_DateTime` |  |  |  |
| 25 | `EB.PSP.AUTHORISER` | `EbPartialSignParam_Authoriser` | String |  |  |
| 26 | `EB.PSP.CO.CODE` | `EbPartialSignParam_CoCode` | String |  |  |
| 27 | `EB.PSP.DEPT.CODE` | `EbPartialSignParam_DeptCode` | String |  |  |
| 28 | `EB.PSP.AUDITOR.CODE` | `EbPartialSignParam_AuditorCode` | String |  |  |
| 29 | `EB.PSP.AUDIT.DATE.TIME` | `EbPartialSignParam_AuditDateTime` | String |  |  |
