# DESCTX.SECTRAS.ERROR.CODE — Table Schema

> Source: `INSERTS/I_F.DESCTX.SECTRAS.ERROR.CODE` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SECTRAS.ERR.CODE.ERROR.TEXT` | `DesctxSectrasErrorCode_ErrorText` | TField |  | This field contains the Error message. |
| 2 | `SECTRAS.ERR.CODE.ERROR.DESCRIPTION` | `DesctxSectrasErrorCode_ErrorDescription` |  |  |  |
| 3 | `SECTRAS.ERR.CODE.ERROR.TYPE` | `DesctxSectrasErrorCode_ErrorType` | TField |  | This field indicates whether the the error code is to be considered as error or warning. |
| 4 | `SECTRAS.ERR.CODE.LOCAL.REF` | `DesctxSectrasErrorCode_LocalRef` |  |  |  |
| 5 | `SECTRAS.ERR.CODE.RESERVED.8` | `DesctxSectrasErrorCode_Reserved8` | TField |  | This field is reserved for future use. |
| 6 | `SECTRAS.ERR.CODE.RESERVED.7` | `DesctxSectrasErrorCode_Reserved7` | TField |  | This field is reserved for future use. |
| 7 | `SECTRAS.ERR.CODE.RESERVED.6` | `DesctxSectrasErrorCode_Reserved6` | TField |  | This field is reserved for future use. |
| 8 | `SECTRAS.ERR.CODE.RESERVED.5` | `DesctxSectrasErrorCode_Reserved5` | TField |  | This field is reserved for future use. |
| 9 | `SECTRAS.ERR.CODE.RESERVED.4` | `DesctxSectrasErrorCode_Reserved4` | TField |  | This field is reserved for future use. |
| 10 | `SECTRAS.ERR.CODE.RESERVED.3` | `DesctxSectrasErrorCode_Reserved3` | TField |  | This field is reserved for future use. |
| 11 | `SECTRAS.ERR.CODE.RESERVED.2` | `DesctxSectrasErrorCode_Reserved2` | TField |  | This field is reserved for future use. |
| 12 | `SECTRAS.ERR.CODE.RESERVED.1` | `DesctxSectrasErrorCode_Reserved1` | TField |  | This field is reserved for future use. |
| 13 | `SECTRAS.ERR.CODE.OVERRIDE` | `DesctxSectrasErrorCode_Override` |  |  |  |
| 14 | `SECTRAS.ERR.CODE.RECORD.STATUS` | `DesctxSectrasErrorCode_RecordStatus` | String |  |  |
| 15 | `SECTRAS.ERR.CODE.CURR.NO` | `DesctxSectrasErrorCode_CurrNo` | String |  |  |
| 16 | `SECTRAS.ERR.CODE.INPUTTER` | `DesctxSectrasErrorCode_Inputter` |  |  |  |
| 17 | `SECTRAS.ERR.CODE.DATE.TIME` | `DesctxSectrasErrorCode_DateTime` |  |  |  |
| 18 | `SECTRAS.ERR.CODE.AUTHORISER` | `DesctxSectrasErrorCode_Authoriser` | String |  |  |
| 19 | `SECTRAS.ERR.CODE.CO.CODE` | `DesctxSectrasErrorCode_CoCode` | String |  |  |
| 20 | `SECTRAS.ERR.CODE.DEPT.CODE` | `DesctxSectrasErrorCode_DeptCode` | String |  |  |
| 21 | `SECTRAS.ERR.CODE.AUDITOR.CODE` | `DesctxSectrasErrorCode_AuditorCode` | String |  |  |
| 22 | `SECTRAS.ERR.CODE.AUDIT.DATE.TIME` | `DesctxSectrasErrorCode_AuditDateTime` | String |  |  |
