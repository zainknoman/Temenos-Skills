# PI.ERROR.REASON.CODE — Table Schema

> Source: `INSERTS/I_F.PI.ERROR.REASON.CODE` in `PI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PIERC.ErrorCode` | `PiErrorReasonCode_Errorcode` |  |  |  |
| 2 | `PIERC.ReasonCode` | `PiErrorReasonCode_Reasoncode` |  |  |  |
| 3 | `PIERC.ReasonCodeDescription` | `PiErrorReasonCode_Reasoncodedescription` |  |  |  |
| 4 | `PIERC.LOCAL.REF` | `PiErrorReasonCode_LocalRef` |  |  |  |
| 5 | `PIERC.RESERVED.5` | `PiErrorReasonCode_Reserved5` | TField |  |  |
| 6 | `PIERC.RESERVED.4` | `PiErrorReasonCode_Reserved4` | TField |  |  |
| 7 | `PIERC.RESERVED.3` | `PiErrorReasonCode_Reserved3` | TField |  |  |
| 8 | `PIERC.RESERVED.2` | `PiErrorReasonCode_Reserved2` | TField |  |  |
| 9 | `PIERC.RESERVED.1` | `PiErrorReasonCode_Reserved1` | TField |  |  |
| 10 | `PIERC.OVERRIDE` | `PiErrorReasonCode_Override` |  |  |  |
| 11 | `PIERC.RECORD.STATUS` | `PiErrorReasonCode_RecordStatus` | String |  |  |
| 12 | `PIERC.CURR.NO` | `PiErrorReasonCode_CurrNo` | String |  |  |
| 13 | `PIERC.INPUTTER` | `PiErrorReasonCode_Inputter` |  |  |  |
| 14 | `PIERC.DATE.TIME` | `PiErrorReasonCode_DateTime` |  |  |  |
| 15 | `PIERC.AUTHORISER` | `PiErrorReasonCode_Authoriser` | String |  |  |
| 16 | `PIERC.CO.CODE` | `PiErrorReasonCode_CoCode` | String |  |  |
| 17 | `PIERC.DEPT.CODE` | `PiErrorReasonCode_DeptCode` | String |  |  |
| 18 | `PIERC.AUDITOR.CODE` | `PiErrorReasonCode_AuditorCode` | String |  |  |
| 19 | `PIERC.AUDIT.DATE.TIME` | `PiErrorReasonCode_AuditDateTime` | String |  |  |
