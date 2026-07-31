# USCORE.BALANCE.THRESHOLDS — Table Schema

> Source: `INSERTS/I_F.USCORE.BALANCE.THRESHOLDS` in `USCORE_CDBalReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.BAL.THRES.DESCRIPTION` | `UscoreBalanceThresholds_Description` |  |  |  |
| 2 | `US.BAL.THRES.ALLOWED.CATEGORY` | `UscoreBalanceThresholds_AllowedCategory` |  |  |  |
| 3 | `US.BAL.THRES.EXCLUDED.CATEGORY` | `UscoreBalanceThresholds_ExcludedCategory` |  |  |  |
| 4 | `US.BAL.THRES.RESERVED.20` | `UscoreBalanceThresholds_Reserved20` |  |  |  |
| 5 | `US.BAL.THRES.RESERVED.19` | `UscoreBalanceThresholds_Reserved19` |  |  |  |
| 6 | `US.BAL.THRES.RESERVED.18` | `UscoreBalanceThresholds_Reserved18` |  |  |  |
| 7 | `US.BAL.THRES.RESERVED.17` | `UscoreBalanceThresholds_Reserved17` |  |  |  |
| 8 | `US.BAL.THRES.RESERVED.16` | `UscoreBalanceThresholds_Reserved16` |  |  |  |
| 9 | `US.BAL.THRES.TIER.CODE` | `UscoreBalanceThresholds_TierCode` |  |  |  |
| 10 | `US.BAL.THRES.RESERVED.15` | `UscoreBalanceThresholds_Reserved15` |  |  |  |
| 11 | `US.BAL.THRES.RESERVED.14` | `UscoreBalanceThresholds_Reserved14` |  |  |  |
| 12 | `US.BAL.THRES.RESERVED.13` | `UscoreBalanceThresholds_Reserved13` |  |  |  |
| 13 | `US.BAL.THRES.RESERVED.12` | `UscoreBalanceThresholds_Reserved12` |  |  |  |
| 14 | `US.BAL.THRES.RESERVED.11` | `UscoreBalanceThresholds_Reserved11` |  |  |  |
| 15 | `US.BAL.THRES.UPPER.LIMIT.AMOUNT` | `UscoreBalanceThresholds_UpperLimitAmount` |  |  |  |
| 16 | `US.BAL.THRES.LOCAL.REF` | `UscoreBalanceThresholds_LocalRef` |  |  |  |
| 17 | `US.BAL.THRES.RESERVED.10` | `UscoreBalanceThresholds_Reserved10` | TField |  |  |
| 18 | `US.BAL.THRES.RESERVED.9` | `UscoreBalanceThresholds_Reserved9` | TField |  |  |
| 19 | `US.BAL.THRES.RESERVED.8` | `UscoreBalanceThresholds_Reserved8` | TField |  |  |
| 20 | `US.BAL.THRES.RESERVED.7` | `UscoreBalanceThresholds_Reserved7` | TField |  |  |
| 21 | `US.BAL.THRES.RESERVED.6` | `UscoreBalanceThresholds_Reserved6` | TField |  |  |
| 22 | `US.BAL.THRES.RESERVED.5` | `UscoreBalanceThresholds_Reserved5` | TField |  |  |
| 23 | `US.BAL.THRES.RESERVED.4` | `UscoreBalanceThresholds_Reserved4` | TField |  |  |
| 24 | `US.BAL.THRES.RESERVED.3` | `UscoreBalanceThresholds_Reserved3` | TField |  |  |
| 25 | `US.BAL.THRES.RESERVED.2` | `UscoreBalanceThresholds_Reserved2` | TField |  |  |
| 26 | `US.BAL.THRES.RESERVED.1` | `UscoreBalanceThresholds_Reserved1` | TField |  |  |
| 27 | `US.BAL.THRES.RECORD.STATUS` | `UscoreBalanceThresholds_RecordStatus` | String |  |  |
| 28 | `US.BAL.THRES.CURR.NO` | `UscoreBalanceThresholds_CurrNo` | String |  |  |
| 29 | `US.BAL.THRES.INPUTTER` | `UscoreBalanceThresholds_Inputter` |  |  |  |
| 30 | `US.BAL.THRES.DATE.TIME` | `UscoreBalanceThresholds_DateTime` |  |  |  |
| 31 | `US.BAL.THRES.AUTHORISER` | `UscoreBalanceThresholds_Authoriser` | String |  |  |
| 32 | `US.BAL.THRES.CO.CODE` | `UscoreBalanceThresholds_CoCode` | String |  |  |
| 33 | `US.BAL.THRES.DEPT.CODE` | `UscoreBalanceThresholds_DeptCode` | String |  |  |
| 34 | `US.BAL.THRES.AUDITOR.CODE` | `UscoreBalanceThresholds_AuditorCode` | String |  |  |
| 35 | `US.BAL.THRES.AUDIT.DATE.TIME` | `UscoreBalanceThresholds_AuditDateTime` | String |  |  |
