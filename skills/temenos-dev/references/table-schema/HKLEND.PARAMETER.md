# HKLEND.PARAMETER — Table Schema

> Source: `INSERTS/I_F.HKLEND.PARAMETER` in `HKLEND_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HKLEND.PARAMETER.PRODUCT` | `HklendParameter_Product` |  |  |  |
| 2 | `HKLEND.PARAMETER.PI.INDEX` | `HklendParameter_PiIndex` |  |  |  |
| 3 | `HKLEND.PARAMETER.PI.PROPERTY` | `HklendParameter_PiProperty` | TField |  | This field holds the property to be configured in the Periodic Interest product. |
| 4 | `HKLEND.PARAMETER.LOCAL.REF` | `HklendParameter_LocalRef` |  |  |  |
| 5 | `HKLEND.PARAMETER.OVERRIDE` | `HklendParameter_Override` |  |  |  |
| 6 | `HKLEND.PARAMETER.RECORD.STATUS` | `HklendParameter_RecordStatus` | String |  |  |
| 7 | `HKLEND.PARAMETER.CURR.NO` | `HklendParameter_CurrNo` | String |  |  |
| 8 | `HKLEND.PARAMETER.INPUTTER` | `HklendParameter_Inputter` |  |  |  |
| 9 | `HKLEND.PARAMETER.DATE.TIME` | `HklendParameter_DateTime` |  |  |  |
| 10 | `HKLEND.PARAMETER.AUTHORISER` | `HklendParameter_Authoriser` | String |  |  |
| 11 | `HKLEND.PARAMETER.CO.CODE` | `HklendParameter_CoCode` | String |  |  |
| 12 | `HKLEND.PARAMETER.DEPT.CODE` | `HklendParameter_DeptCode` | String |  |  |
| 13 | `HKLEND.PARAMETER.AUDITOR.CODE` | `HklendParameter_AuditorCode` | String |  |  |
| 14 | `HKLEND.PARAMETER.AUDIT.DATE.TIME` | `HklendParameter_AuditDateTime` | String |  |  |
| 15 | `HKLEND.PARAMETER.NOTICE.PERIOD` | `HklendParameter_NoticePeriod` | TField |  | This field holds the period to be configured for prepayment/payoff. |
| 16 | `HKLEND.PARAMETER.LTV.THRESHOLD` | `HklendParameter_LtvThreshold` | TField |  | LTV threshold set by HKMC. |
| 17 | `HKLEND.PARAMETER.INSURER.ACCT` | `HklendParameter_InsurerAcct` | TField |  | Configure the required internal account to be credited if the insurance policy is external. |
| 18 | `HKLEND.PARAMETER.PREMIUM.PROPERTY` | `HklendParameter_PremiumProperty` | TField |  | Premium charge property. This is used to identify the premium charge to be deactivated when insurance is terminated. |
