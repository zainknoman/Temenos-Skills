# ARACCT.FX.RESTRICT.PARAM — Table Schema

> Source: `INSERTS/I_F.ARACCT.FX.RESTRICT.PARAM` in `ARACCT_FXBlacklistLimitValidation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARACCT.FXP.PO.PRODUCT` | `AracctFxRestrictParam_PoProduct` |  |  |  |
| 2 | `ARACCT.FXP.AA.ACTIVITY` | `AracctFxRestrictParam_AaActivity` |  |  |  |
| 3 | `ARACCT.FXP.MULTIHOLDER.VALIDATION` | `AracctFxRestrictParam_MultiholderValidation` | TField |  | This field indicate whether the multi holder validation is required or not for FX payments. Possible values can be: - NO (NULL) when multi holder validation is not require - YES when multi holder validation is required |
| 4 | `ARACCT.FXP.DATE.MULTIHOLDER.OFF` | `AracctFxRestrictParam_DateMultiholderOff` | TField |  | This field indicate when the multi holder validation is disabled This is a noinput field that will be automatically updated when changing the multi holder validation from YES to NO Based on the field value, multi holder FX transaction details will be moved from Live to Hist table |
| 5 | `ARACCT.FXP.RESERVED.8` | `AracctFxRestrictParam_Reserved8` | TField |  | Reserved for Future use. |
| 6 | `ARACCT.FXP.RESERVED.7` | `AracctFxRestrictParam_Reserved7` | TField |  | Reserved for Future use. |
| 7 | `ARACCT.FXP.RESERVED.6` | `AracctFxRestrictParam_Reserved6` | TField |  | Reserved for Future use. |
| 8 | `ARACCT.FXP.RESERVED.5` | `AracctFxRestrictParam_Reserved5` | TField |  | Reserved for Future use. |
| 9 | `ARACCT.FXP.RESERVED.4` | `AracctFxRestrictParam_Reserved4` | TField |  | Reserved for Future use. |
| 10 | `ARACCT.FXP.RESERVED.3` | `AracctFxRestrictParam_Reserved3` | TField |  | Reserved for Future use. |
| 11 | `ARACCT.FXP.RESERVED.2` | `AracctFxRestrictParam_Reserved2` | TField |  | Reserved for Future use. |
| 12 | `ARACCT.FXP.RESERVED.1` | `AracctFxRestrictParam_Reserved1` | TField |  | Reserved for Future use. |
| 13 | `ARACCT.FXP.RECORD.STATUS` | `AracctFxRestrictParam_RecordStatus` | String |  |  |
| 14 | `ARACCT.FXP.CURR.NO` | `AracctFxRestrictParam_CurrNo` | String |  |  |
| 15 | `ARACCT.FXP.INPUTTER` | `AracctFxRestrictParam_Inputter` |  |  |  |
| 16 | `ARACCT.FXP.DATE.TIME` | `AracctFxRestrictParam_DateTime` |  |  |  |
| 17 | `ARACCT.FXP.AUTHORISER` | `AracctFxRestrictParam_Authoriser` | String |  |  |
| 18 | `ARACCT.FXP.CO.CODE` | `AracctFxRestrictParam_CoCode` | String |  |  |
| 19 | `ARACCT.FXP.DEPT.CODE` | `AracctFxRestrictParam_DeptCode` | String |  |  |
| 20 | `ARACCT.FXP.AUDITOR.CODE` | `AracctFxRestrictParam_AuditorCode` | String |  |  |
| 21 | `ARACCT.FXP.AUDIT.DATE.TIME` | `AracctFxRestrictParam_AuditDateTime` | String |  |  |
