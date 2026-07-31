# LENREN.AUTOREN.SUPPRESS.PARAM — Table Schema

> Source: `INSERTS/I_F.LENREN.AUTOREN.SUPPRESS.PARAM` in `LENREN_Renewal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUTO.RENEW.SUP.AUTO.REN.RSN` | `LenrenAutorenSuppressParam_SupAutoRenRsn` |  |  |  |
| 2 | `AUTO.RENEW.RESERVED.16` | `LenrenAutorenSuppressParam_Reserved16` |  |  |  |
| 3 | `AUTO.RENEW.RESERVED.15` | `LenrenAutorenSuppressParam_Reserved15` |  |  |  |
| 4 | `AUTO.RENEW.RESERVED.14` | `LenrenAutorenSuppressParam_Reserved14` |  |  |  |
| 5 | `AUTO.RENEW.UPDATE.LOAN.COND` | `LenrenAutorenSuppressParam_UpdateLoanCond` |  |  |  |
| 6 | `AUTO.RENEW.RESERVED.13` | `LenrenAutorenSuppressParam_Reserved13` |  |  |  |
| 7 | `AUTO.RENEW.RESERVED.12` | `LenrenAutorenSuppressParam_Reserved12` |  |  |  |
| 8 | `AUTO.RENEW.RESERVED.11` | `LenrenAutorenSuppressParam_Reserved11` |  |  |  |
| 9 | `AUTO.RENEW.DATE.TO.APPLY` | `LenrenAutorenSuppressParam_DateToApply` |  |  |  |
| 10 | `AUTO.RENEW.OFS.SOURCE` | `LenrenAutorenSuppressParam_OfsSource` | TField |  | Field to store the OFS id to trigger the activity defined in the field OFS.ACTIVITY for suppress the loan renewals.Validation - record of OFS.SOURCEExample- LEND.RENEW |
| 11 | `AUTO.RENEW.OFS.VERSION` | `LenrenAutorenSuppressParam_OfsVersion` | TField |  | Field to store the version through which the activity to be triggered via OFS.Valid record of VERSION application.Example - AA.ARRANGEMENT.ACTIVITY,AA |
| 12 | `AUTO.RENEW.OFS.ACTIVITY` | `LenrenAutorenSuppressParam_OfsActivity` | TField |  | Field is used to indicate the activity which will be triggered to suppress the loan renewals as per the conditions defined in LENREN.RENEWAL.REJECTS.PARAM with id suffixed with UPDATE.Valid records of AA.ACTIVITYExample - LENDING-RENEGOTIATE-ARRANGEMENT |
| 13 | `AUTO.RENEW.RESERVED.10` | `LenrenAutorenSuppressParam_Reserved10` | TField |  |  |
| 14 | `AUTO.RENEW.RESERVED.9` | `LenrenAutorenSuppressParam_Reserved9` | TField |  |  |
| 15 | `AUTO.RENEW.RESERVED.8` | `LenrenAutorenSuppressParam_Reserved8` | TField |  |  |
| 16 | `AUTO.RENEW.RESERVED.7` | `LenrenAutorenSuppressParam_Reserved7` | TField |  |  |
| 17 | `AUTO.RENEW.RESERVED.6` | `LenrenAutorenSuppressParam_Reserved6` | TField |  |  |
| 18 | `AUTO.RENEW.RESERVED.5` | `LenrenAutorenSuppressParam_Reserved5` | TField |  |  |
| 19 | `AUTO.RENEW.RESERVED.4` | `LenrenAutorenSuppressParam_Reserved4` | TField |  |  |
| 20 | `AUTO.RENEW.RESERVED.3` | `LenrenAutorenSuppressParam_Reserved3` | TField |  |  |
| 21 | `AUTO.RENEW.RESERVED.2` | `LenrenAutorenSuppressParam_Reserved2` | TField |  |  |
| 22 | `AUTO.RENEW.RESERVED.1` | `LenrenAutorenSuppressParam_Reserved1` | TField |  |  |
| 23 | `AUTO.RENEW.LOCAL.REF` | `LenrenAutorenSuppressParam_LocalRef` |  |  |  |
| 24 | `AUTO.RENEW.OVERRIDE` | `LenrenAutorenSuppressParam_Override` |  |  |  |
| 25 | `AUTO.RENEW.RECORD.STATUS` | `LenrenAutorenSuppressParam_RecordStatus` | String |  |  |
| 26 | `AUTO.RENEW.CURR.NO` | `LenrenAutorenSuppressParam_CurrNo` | String |  |  |
| 27 | `AUTO.RENEW.INPUTTER` | `LenrenAutorenSuppressParam_Inputter` |  |  |  |
| 28 | `AUTO.RENEW.DATE.TIME` | `LenrenAutorenSuppressParam_DateTime` |  |  |  |
| 29 | `AUTO.RENEW.AUTHORISER` | `LenrenAutorenSuppressParam_Authoriser` | String |  |  |
| 30 | `AUTO.RENEW.CO.CODE` | `LenrenAutorenSuppressParam_CoCode` | String |  |  |
| 31 | `AUTO.RENEW.DEPT.CODE` | `LenrenAutorenSuppressParam_DeptCode` | String |  |  |
| 32 | `AUTO.RENEW.AUDITOR.CODE` | `LenrenAutorenSuppressParam_AuditorCode` | String |  |  |
| 33 | `AUTO.RENEW.AUDIT.DATE.TIME` | `LenrenAutorenSuppressParam_AuditDateTime` | String |  |  |
