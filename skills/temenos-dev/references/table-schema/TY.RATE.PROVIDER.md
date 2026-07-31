# TY.RATE.PROVIDER — Table Schema

> Source: `INSERTS/I_F.TY.RATE.PROVIDER` in `TY_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.RP.DESCRIPTION` | `TyRateProvider_Description` |  |  |  |
| 2 | `TY.RP.RESERVED.10` | `TyRateProvider_Reserved10` | TField |  |  |
| 3 | `TY.RP.RESERVED.9` | `TyRateProvider_Reserved9` | TField |  |  |
| 4 | `TY.RP.RESERVED.8` | `TyRateProvider_Reserved8` | TField |  |  |
| 5 | `TY.RP.RESERVED.7` | `TyRateProvider_Reserved7` | TField |  |  |
| 6 | `TY.RP.RESERVED.6` | `TyRateProvider_Reserved6` | TField |  |  |
| 7 | `TY.RP.RESERVED.5` | `TyRateProvider_Reserved5` | TField |  |  |
| 8 | `TY.RP.RESERVED.4` | `TyRateProvider_Reserved4` | TField |  |  |
| 9 | `TY.RP.RESERVED.3` | `TyRateProvider_Reserved3` | TField |  |  |
| 10 | `TY.RP.RESERVED.2` | `TyRateProvider_Reserved2` | TField |  |  |
| 11 | `TY.RP.RESERVED.1` | `TyRateProvider_Reserved1` | TField |  |  |
| 12 | `TY.RP.LOCAL.REF` | `TyRateProvider_LocalRef` |  |  |  |
| 13 | `TY.RP.OVERRIDE` | `TyRateProvider_Override` |  |  |  |
| 14 | `TY.RP.RECORD.STATUS` | `TyRateProvider_RecordStatus` | String |  |  |
| 15 | `TY.RP.CURR.NO` | `TyRateProvider_CurrNo` | String |  |  |
| 16 | `TY.RP.INPUTTER` | `TyRateProvider_Inputter` |  |  |  |
| 17 | `TY.RP.DATE.TIME` | `TyRateProvider_DateTime` |  |  |  |
| 18 | `TY.RP.AUTHORISER` | `TyRateProvider_Authoriser` | String |  |  |
| 19 | `TY.RP.CO.CODE` | `TyRateProvider_CoCode` | String |  |  |
| 20 | `TY.RP.DEPT.CODE` | `TyRateProvider_DeptCode` | String |  |  |
| 21 | `TY.RP.AUDITOR.CODE` | `TyRateProvider_AuditorCode` | String |  |  |
| 22 | `TY.RP.AUDIT.DATE.TIME` | `TyRateProvider_AuditDateTime` | String |  |  |
