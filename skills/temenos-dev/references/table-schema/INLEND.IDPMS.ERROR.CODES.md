# INLEND.IDPMS.ERROR.CODES — Table Schema

> Source: `INSERTS/I_F.INLEND.IDPMS.ERROR.CODES` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IDPMS.ERRCD.ERROR.CODE.DESCRIPTION` | `InlendIdpmsErrorCodes_ErrorCodeDescription` |  |  |  |
| 2 | `IDPMS.ERRCD.PROCESS.MODULE` | `InlendIdpmsErrorCodes_ProcessModule` |  |  |  |
| 3 | `IDPMS.ERRCD.RESERVED.10` | `InlendIdpmsErrorCodes_Reserved10` | TField |  |  |
| 4 | `IDPMS.ERRCD.RESERVED.9` | `InlendIdpmsErrorCodes_Reserved9` | TField |  |  |
| 5 | `IDPMS.ERRCD.RESERVED.8` | `InlendIdpmsErrorCodes_Reserved8` | TField |  |  |
| 6 | `IDPMS.ERRCD.RESERVED.7` | `InlendIdpmsErrorCodes_Reserved7` | TField |  |  |
| 7 | `IDPMS.ERRCD.RESERVED.6` | `InlendIdpmsErrorCodes_Reserved6` | TField |  |  |
| 8 | `IDPMS.ERRCD.RESERVED.5` | `InlendIdpmsErrorCodes_Reserved5` | TField |  |  |
| 9 | `IDPMS.ERRCD.RESERVED.4` | `InlendIdpmsErrorCodes_Reserved4` | TField |  |  |
| 10 | `IDPMS.ERRCD.RESERVED.3` | `InlendIdpmsErrorCodes_Reserved3` | TField |  |  |
| 11 | `IDPMS.ERRCD.RESERVED.2` | `InlendIdpmsErrorCodes_Reserved2` | TField |  |  |
| 12 | `IDPMS.ERRCD.RESERVED.1` | `InlendIdpmsErrorCodes_Reserved1` | TField |  |  |
| 13 | `IDPMS.ERRCD.LOCAL.REF` | `InlendIdpmsErrorCodes_LocalRef` |  |  |  |
| 14 | `IDPMS.ERRCD.OVERRIDE` | `InlendIdpmsErrorCodes_Override` |  |  |  |
| 15 | `IDPMS.ERRCD.RECORD.STATUS` | `InlendIdpmsErrorCodes_RecordStatus` | String |  |  |
| 16 | `IDPMS.ERRCD.CURR.NO` | `InlendIdpmsErrorCodes_CurrNo` | String |  |  |
| 17 | `IDPMS.ERRCD.INPUTTER` | `InlendIdpmsErrorCodes_Inputter` |  |  |  |
| 18 | `IDPMS.ERRCD.DATE.TIME` | `InlendIdpmsErrorCodes_DateTime` |  |  |  |
| 19 | `IDPMS.ERRCD.AUTHORISER` | `InlendIdpmsErrorCodes_Authoriser` | String |  |  |
| 20 | `IDPMS.ERRCD.CO.CODE` | `InlendIdpmsErrorCodes_CoCode` | String |  |  |
| 21 | `IDPMS.ERRCD.DEPT.CODE` | `InlendIdpmsErrorCodes_DeptCode` | String |  |  |
| 22 | `IDPMS.ERRCD.AUDITOR.CODE` | `InlendIdpmsErrorCodes_AuditorCode` | String |  |  |
| 23 | `IDPMS.ERRCD.AUDIT.DATE.TIME` | `InlendIdpmsErrorCodes_AuditDateTime` | String |  |  |
