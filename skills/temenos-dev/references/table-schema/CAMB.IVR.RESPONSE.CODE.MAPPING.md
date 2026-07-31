# CAMB.IVR.RESPONSE.CODE.MAPPING — Table Schema

> Source: `INSERTS/I_F.CAMB.IVR.RESPONSE.CODE.MAPPING` in `CATELS_TelephoneBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IVR.RES.ERR.CODE.MAP` | `CambIvrResponseCodeMapping_ErrCodeMap` | TField | Yes | This is a mandatory field based on which IVR response error will be displayed as Error Codes or meaningful error description defined in this parameter Error.Code: Error codes will be displayed in the IVR response if this value is chosen Error.Msg: Error messages will be displayed from this parameter In case the flag is not configured then, error codes will be displayed |
| 2 | `IVR.RES.ERROR.MESSAGE` | `CambIvrResponseCodeMapping_ErrorMessage` |  |  |  |
| 3 | `IVR.RES.DISPLAY.MSG` | `CambIvrResponseCodeMapping_DisplayMsg` |  |  |  |
| 4 | `IVR.RES.OTHER.ERROR.MSG` | `CambIvrResponseCodeMapping_OtherErrorMsg` |  |  |  |
| 5 | `IVR.RES.OTHER.ERROR.CODE` | `CambIvrResponseCodeMapping_OtherErrorCode` |  |  |  |
| 6 | `IVR.RES.DEFAULT.ERROR` | `CambIvrResponseCodeMapping_DefaultError` | TField |  | This field can be defined for both "Error.Msg" and "Error.Code" If set as "Error.Msg" then the message description defined here will be displayed in case an Error is not defined in the field "ERROR.MESSAGE" If set as "Error.Code" then the Error code defined here will be displayed in case an Error is not defined in the field "OTHER.ERROR.MSG" If the field value is left blank then the error from OFS response will be displayed |
| 7 | `IVR.RES.RESERVED.10` | `CambIvrResponseCodeMapping_Reserved10` | TField |  |  |
| 8 | `IVR.RES.RESERVED.9` | `CambIvrResponseCodeMapping_Reserved9` | TField |  |  |
| 9 | `IVR.RES.RESERVED.8` | `CambIvrResponseCodeMapping_Reserved8` | TField |  |  |
| 10 | `IVR.RES.RESERVED.7` | `CambIvrResponseCodeMapping_Reserved7` | TField |  |  |
| 11 | `IVR.RES.RESERVED.6` | `CambIvrResponseCodeMapping_Reserved6` | TField |  |  |
| 12 | `IVR.RES.RESERVED.5` | `CambIvrResponseCodeMapping_Reserved5` | TField |  |  |
| 13 | `IVR.RES.RESERVED.4` | `CambIvrResponseCodeMapping_Reserved4` | TField |  |  |
| 14 | `IVR.RES.RESERVED.3` | `CambIvrResponseCodeMapping_Reserved3` | TField |  |  |
| 15 | `IVR.RES.RESERVED.2` | `CambIvrResponseCodeMapping_Reserved2` | TField |  |  |
| 16 | `IVR.RES.RESERVED.1` | `CambIvrResponseCodeMapping_Reserved1` | TField |  |  |
| 17 | `IVR.RES.LOCAL.REF` | `CambIvrResponseCodeMapping_LocalRef` |  |  |  |
| 18 | `IVR.RES.OVERRIDE` | `CambIvrResponseCodeMapping_Override` |  |  |  |
| 19 | `IVR.RES.RECORD.STATUS` | `CambIvrResponseCodeMapping_RecordStatus` | String |  |  |
| 20 | `IVR.RES.CURR.NO` | `CambIvrResponseCodeMapping_CurrNo` | String |  |  |
| 21 | `IVR.RES.INPUTTER` | `CambIvrResponseCodeMapping_Inputter` |  |  |  |
| 22 | `IVR.RES.DATE.TIME` | `CambIvrResponseCodeMapping_DateTime` |  |  |  |
| 23 | `IVR.RES.AUTHORISER` | `CambIvrResponseCodeMapping_Authoriser` | String |  |  |
| 24 | `IVR.RES.CO.CODE` | `CambIvrResponseCodeMapping_CoCode` | String |  |  |
| 25 | `IVR.RES.DEPT.CODE` | `CambIvrResponseCodeMapping_DeptCode` | String |  |  |
| 26 | `IVR.RES.AUDITOR.CODE` | `CambIvrResponseCodeMapping_AuditorCode` | String |  |  |
| 27 | `IVR.RES.AUDIT.DATE.TIME` | `CambIvrResponseCodeMapping_AuditDateTime` | String |  |  |
