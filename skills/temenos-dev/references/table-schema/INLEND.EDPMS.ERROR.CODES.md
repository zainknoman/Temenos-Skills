# INLEND.EDPMS.ERROR.CODES — Table Schema

> Source: `INSERTS/I_F.INLEND.EDPMS.ERROR.CODES` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EDPMS.ERRCD.ERROR.CODE.DESCRIPTION` | `InlendEdpmsErrorCodes_ErrorCodeDescription` |  |  |  |
| 2 | `EDPMS.ERRCD.RESERVED.10` | `InlendEdpmsErrorCodes_Reserved10` | TField |  |  |
| 3 | `EDPMS.ERRCD.RESERVED.9` | `InlendEdpmsErrorCodes_Reserved9` | TField |  |  |
| 4 | `EDPMS.ERRCD.RESERVED.8` | `InlendEdpmsErrorCodes_Reserved8` | TField |  |  |
| 5 | `EDPMS.ERRCD.RESERVED.7` | `InlendEdpmsErrorCodes_Reserved7` | TField |  |  |
| 6 | `EDPMS.ERRCD.RESERVED.6` | `InlendEdpmsErrorCodes_Reserved6` | TField |  |  |
| 7 | `EDPMS.ERRCD.RESERVED.5` | `InlendEdpmsErrorCodes_Reserved5` | TField |  |  |
| 8 | `EDPMS.ERRCD.RESERVED.4` | `InlendEdpmsErrorCodes_Reserved4` | TField |  |  |
| 9 | `EDPMS.ERRCD.RESERVED.3` | `InlendEdpmsErrorCodes_Reserved3` | TField |  |  |
| 10 | `EDPMS.ERRCD.RESERVED.2` | `InlendEdpmsErrorCodes_Reserved2` | TField |  |  |
| 11 | `EDPMS.ERRCD.RESERVED.1` | `InlendEdpmsErrorCodes_Reserved1` | TField |  |  |
| 12 | `EDPMS.ERRCD.LOCAL.REF` | `InlendEdpmsErrorCodes_LocalRef` |  |  |  |
| 13 | `EDPMS.ERRCD.OVERRIDE` | `InlendEdpmsErrorCodes_Override` |  |  |  |
| 14 | `EDPMS.ERRCD.RECORD.STATUS` | `InlendEdpmsErrorCodes_RecordStatus` | String |  |  |
| 15 | `EDPMS.ERRCD.CURR.NO` | `InlendEdpmsErrorCodes_CurrNo` | String |  |  |
| 16 | `EDPMS.ERRCD.INPUTTER` | `InlendEdpmsErrorCodes_Inputter` |  |  |  |
| 17 | `EDPMS.ERRCD.DATE.TIME` | `InlendEdpmsErrorCodes_DateTime` |  |  |  |
| 18 | `EDPMS.ERRCD.AUTHORISER` | `InlendEdpmsErrorCodes_Authoriser` | String |  |  |
| 19 | `EDPMS.ERRCD.CO.CODE` | `InlendEdpmsErrorCodes_CoCode` | String |  |  |
| 20 | `EDPMS.ERRCD.DEPT.CODE` | `InlendEdpmsErrorCodes_DeptCode` | String |  |  |
| 21 | `EDPMS.ERRCD.AUDITOR.CODE` | `InlendEdpmsErrorCodes_AuditorCode` | String |  |  |
| 22 | `EDPMS.ERRCD.AUDIT.DATE.TIME` | `InlendEdpmsErrorCodes_AuditDateTime` | String |  |  |
