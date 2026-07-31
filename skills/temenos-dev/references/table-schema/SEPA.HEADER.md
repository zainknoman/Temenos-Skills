# SEPA.HEADER — Table Schema

> Source: `INSERTS/I_F.SEPA.HEADER` in `EP_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.HEA.DESCRIPTION` | `SepaHeader_Description` |  |  |  |
| 2 | `SEP.HEA.FIELD.TAG.ID` | `SepaHeader_FieldTagId` |  |  |  |
| 3 | `SEP.HEA.FIELD.TAG.OCCUR` | `SepaHeader_FieldTagOccur` |  |  |  |
| 4 | `SEP.HEA.FIELD.TAG.ALTER` | `SepaHeader_FieldTagAlter` |  |  |  |
| 5 | `SEP.HEA.FIELD.NAME` | `SepaHeader_FieldName` |  |  |  |
| 6 | `SEP.HEA.FIELD.FORMAT` | `SepaHeader_FieldFormat` |  |  |  |
| 7 | `SEP.HEA.FIELD.DETAIL` | `SepaHeader_FieldDetail` |  |  |  |
| 8 | `SEP.HEA.FIELD.EXTRCT` | `SepaHeader_FieldExtrct` |  |  |  |
| 9 | `SEP.HEA.FILE.TAG.PREFIX` | `SepaHeader_FileTagPrefix` | TField |  |  |
| 10 | `SEP.HEA.FILE.HDR.SUFFIX` | `SepaHeader_FileHdrSuffix` | TField |  |  |
| 11 | `SEP.HEA.FILE.DIRECTION` | `SepaHeader_FileDirection` |  |  |  |
| 12 | `SEP.HEA.ALLOWED.MESSAGE` | `SepaHeader_AllowedMessage` |  |  |  |
| 13 | `SEP.HEA.MSG.TAG.PREFIX` | `SepaHeader_MsgTagPrefix` |  |  |  |
| 14 | `SEP.HEA.MSG.HDR.ALIAS` | `SepaHeader_MsgHdrAlias` |  |  |  |
| 15 | `SEP.HEA.FILE.TYPE` | `SepaHeader_FileType` | TField |  |  |
| 16 | `SEP.HEA.FILE.PRE.HEADER` | `SepaHeader_FilePreHeader` | TField |  |  |
| 17 | `SEP.HEA.FILE.POST.HEADER` | `SepaHeader_FilePostHeader` | TField |  |  |
| 18 | `SEP.HEA.PEACH.ID` | `SepaHeader_PeachId` |  |  |  |
| 19 | `SEP.HEA.PEACH.REJECT` | `SepaHeader_PeachReject` | TField |  |  |
| 20 | `SEP.HEA.INW.VALIDATION.RTN` | `SepaHeader_InwValidationRtn` | TField |  |  |
| 21 | `SEP.HEA.HDR.LOAD.RTN` | `SepaHeader_HdrLoadRtn` | TField |  |  |
| 22 | `SEP.HEA.RESERVED.3` | `SepaHeader_Reserved3` | TField |  |  |
| 23 | `SEP.HEA.RESERVED.2` | `SepaHeader_Reserved2` | TField |  |  |
| 24 | `SEP.HEA.RESERVED.1` | `SepaHeader_Reserved1` | TField |  |  |
| 25 | `SEP.HEA.LOCAL.REF` | `SepaHeader_LocalRef` |  |  |  |
| 26 | `SEP.HEA.OVERRIDE` | `SepaHeader_Override` |  |  |  |
| 27 | `SEP.HEA.RECORD.STATUS` | `SepaHeader_RecordStatus` | String |  |  |
| 28 | `SEP.HEA.CURR.NO` | `SepaHeader_CurrNo` | String |  |  |
| 29 | `SEP.HEA.INPUTTER` | `SepaHeader_Inputter` |  |  |  |
| 30 | `SEP.HEA.DATE.TIME` | `SepaHeader_DateTime` |  |  |  |
| 31 | `SEP.HEA.AUTHORISER` | `SepaHeader_Authoriser` | String |  |  |
| 32 | `SEP.HEA.CO.CODE` | `SepaHeader_CoCode` | String |  |  |
| 33 | `SEP.HEA.DEPT.CODE` | `SepaHeader_DeptCode` | String |  |  |
| 34 | `SEP.HEA.AUDITOR.CODE` | `SepaHeader_AuditorCode` | String |  |  |
| 35 | `SEP.HEA.AUDIT.DATE.TIME` | `SepaHeader_AuditDateTime` | String |  |  |
