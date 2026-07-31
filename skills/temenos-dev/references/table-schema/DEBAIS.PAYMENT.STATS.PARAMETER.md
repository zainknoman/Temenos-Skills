# DEBAIS.PAYMENT.STATS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DEBAIS.PAYMENT.STATS.PARAMETER` in `DEBAIS_PaymentStatistics.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEBAIS.STATS.CLASSIFICATION` | `DebaisPaymentStatsParameter_Classification` |  |  |  |
| 2 | `DEBAIS.STATS.CLASSIFICATION.CODE` | `DebaisPaymentStatsParameter_ClassificationCode` |  |  |  |
| 3 | `DEBAIS.STATS.COUNTRY` | `DebaisPaymentStatsParameter_Country` |  |  |  |
| 4 | `DEBAIS.STATS.COUNTRY.CODE` | `DebaisPaymentStatsParameter_CountryCode` |  |  |  |
| 5 | `DEBAIS.STATS.EXTRACT.FROM.DATE` | `DebaisPaymentStatsParameter_ExtractFromDate` | TField |  | Configuration of start date which is needed for extract |
| 6 | `DEBAIS.STATS.EXTRACT.TO.DATE` | `DebaisPaymentStatsParameter_ExtractToDate` | TField |  | Configuration of end date which is needed for extract |
| 7 | `DEBAIS.STATS.RESERVED.10` | `DebaisPaymentStatsParameter_Reserved10` | TField |  | Reserved for Future Use. |
| 8 | `DEBAIS.STATS.RESERVED.9` | `DebaisPaymentStatsParameter_Reserved9` | TField |  | Reserved for Future Use. |
| 9 | `DEBAIS.STATS.RESERVED.8` | `DebaisPaymentStatsParameter_Reserved8` | TField |  | Reserved for Future Use. |
| 10 | `DEBAIS.STATS.RESERVED.7` | `DebaisPaymentStatsParameter_Reserved7` | TField |  | Reserved for Future Use. |
| 11 | `DEBAIS.STATS.RESERVED.6` | `DebaisPaymentStatsParameter_Reserved6` | TField |  | Reserved for Future Use. |
| 12 | `DEBAIS.STATS.RESERVED.5` | `DebaisPaymentStatsParameter_Reserved5` | TField |  | Reserved for Future Use. |
| 13 | `DEBAIS.STATS.RESERVED.4` | `DebaisPaymentStatsParameter_Reserved4` | TField |  | Reserved for Future Use. |
| 14 | `DEBAIS.STATS.RESERVED.3` | `DebaisPaymentStatsParameter_Reserved3` | TField |  | Reserved for Future Use. |
| 15 | `DEBAIS.STATS.RESERVED.2` | `DebaisPaymentStatsParameter_Reserved2` | TField |  | Reserved for Future Use. |
| 16 | `DEBAIS.STATS.RESERVED.1` | `DebaisPaymentStatsParameter_Reserved1` | TField |  | Reserved for Future Use. |
| 17 | `DEBAIS.STATS.LOCAL.REF` | `DebaisPaymentStatsParameter_LocalRef` |  |  |  |
| 18 | `DEBAIS.STATS.OVERRIDE` | `DebaisPaymentStatsParameter_Override` |  |  |  |
| 19 | `DEBAIS.STATS.RECORD.STATUS` | `DebaisPaymentStatsParameter_RecordStatus` | String |  |  |
| 20 | `DEBAIS.STATS.CURR.NO` | `DebaisPaymentStatsParameter_CurrNo` | String |  |  |
| 21 | `DEBAIS.STATS.INPUTTER` | `DebaisPaymentStatsParameter_Inputter` |  |  |  |
| 22 | `DEBAIS.STATS.DATE.TIME` | `DebaisPaymentStatsParameter_DateTime` |  |  |  |
| 23 | `DEBAIS.STATS.AUTHORISER` | `DebaisPaymentStatsParameter_Authoriser` | String |  |  |
| 24 | `DEBAIS.STATS.CO.CODE` | `DebaisPaymentStatsParameter_CoCode` | String |  |  |
| 25 | `DEBAIS.STATS.DEPT.CODE` | `DebaisPaymentStatsParameter_DeptCode` | String |  |  |
| 26 | `DEBAIS.STATS.AUDITOR.CODE` | `DebaisPaymentStatsParameter_AuditorCode` | String |  |  |
| 27 | `DEBAIS.STATS.AUDIT.DATE.TIME` | `DebaisPaymentStatsParameter_AuditDateTime` | String |  |  |
