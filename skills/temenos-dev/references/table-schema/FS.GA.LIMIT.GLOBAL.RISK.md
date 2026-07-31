# FS.GA.LIMIT.GLOBAL.RISK — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.GLOBAL.RISK` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.GLOBAL.RISK.CORRESPONDENT.CATEGORY` | `FsGaLimitGlobalRisk_CorrespondentCategory` | TField |  | Category of correspondent Multifonds DB Column is CAT_EMET. |
| 2 | `FS.GA.LIMIT.GLOBAL.RISK.GROUP.RATING` | `FsGaLimitGlobalRisk_GroupRating` | TField |  | Group Rating Multifonds DB Column is CGROUPE_RATING. |
| 3 | `FS.GA.LIMIT.GLOBAL.RISK.FUNDS.LEVEL` | `FsGaLimitGlobalRisk_FundsLevel` |  |  |  |
| 4 | `FS.GA.LIMIT.GLOBAL.RISK.LIMIT.TYPE` | `FsGaLimitGlobalRisk_LimitType` | TField |  | It specifies the type of limit. Example Amount, Percent etc Multifonds DB Column is TYP_LIM. |
| 5 | `FS.GA.LIMIT.GLOBAL.RISK.AMOUNT.TYPE` | `FsGaLimitGlobalRisk_AmountType` | TField |  | The type of amount (ex. Average Nav, Nav after P/L allocation etc.) can be defined as the amount used as basis for further calculation ex. Nav Charges. Multifonds DB Column is TYP_MNT. |
| 6 | `FS.GA.LIMIT.GLOBAL.RISK.CURRENCY.LIMITS` | `FsGaLimitGlobalRisk_CurrencyLimits` | TField |  | To set a Currency for Limits Multifonds DB Column is CMON_LIM. |
| 7 | `FS.GA.LIMIT.GLOBAL.RISK.LIMIT.MINIMUM.PERCENT` | `FsGaLimitGlobalRisk_LimitMinimumPercent` | TField |  | It specidfies the minimum percent of limit to be applied Multifonds DB Column is PC_MIN_LIM. |
| 8 | `FS.GA.LIMIT.GLOBAL.RISK.LIMIT.MINIMUM.AMOUNT` | `FsGaLimitGlobalRisk_LimitMinimumAmount` | TField |  | It specifies the minimum amount of limit to be applied Multifonds DB Column is MNT_MIN_LIM. |
| 9 | `FS.GA.LIMIT.GLOBAL.RISK.LIMIT.MAXIMUM.PERCENT` | `FsGaLimitGlobalRisk_LimitMaximumPercent` | TField |  | It specidfies the maximum percent of limit to be applied Multifonds DB Column is PC_MAX_LIM. |
| 10 | `FS.GA.LIMIT.GLOBAL.RISK.MAXIMUM.LIMIT.AMOUNT` | `FsGaLimitGlobalRisk_MaximumLimitAmount` | TField |  | It specifies the maximum amount of limit to be applied. Multifonds DB Column is MNT_MAX_LIM. |
| 11 | `FS.GA.LIMIT.GLOBAL.RISK.RESERVED10` | `FsGaLimitGlobalRisk_Reserved10` | TField |  |  |
| 12 | `FS.GA.LIMIT.GLOBAL.RISK.RESERVED9` | `FsGaLimitGlobalRisk_Reserved9` | TField |  |  |
| 13 | `FS.GA.LIMIT.GLOBAL.RISK.RESERVED8` | `FsGaLimitGlobalRisk_Reserved8` | TField |  |  |
| 14 | `FS.GA.LIMIT.GLOBAL.RISK.RESERVED7` | `FsGaLimitGlobalRisk_Reserved7` | TField |  |  |
| 15 | `FS.GA.LIMIT.GLOBAL.RISK.RESERVED6` | `FsGaLimitGlobalRisk_Reserved6` | TField |  |  |
| 16 | `FS.GA.LIMIT.GLOBAL.RISK.RESERVED5` | `FsGaLimitGlobalRisk_Reserved5` | TField |  |  |
| 17 | `FS.GA.LIMIT.GLOBAL.RISK.RESERVED4` | `FsGaLimitGlobalRisk_Reserved4` | TField |  |  |
| 18 | `FS.GA.LIMIT.GLOBAL.RISK.RESERVED3` | `FsGaLimitGlobalRisk_Reserved3` | TField |  |  |
| 19 | `FS.GA.LIMIT.GLOBAL.RISK.RESERVED2` | `FsGaLimitGlobalRisk_Reserved2` | TField |  |  |
| 20 | `FS.GA.LIMIT.GLOBAL.RISK.RESERVED1` | `FsGaLimitGlobalRisk_Reserved1` | TField |  |  |
| 21 | `FS.GA.LIMIT.GLOBAL.RISK.RECORD.STATUS` | `FsGaLimitGlobalRisk_RecordStatus` | String |  |  |
| 22 | `FS.GA.LIMIT.GLOBAL.RISK.CURR.NO` | `FsGaLimitGlobalRisk_CurrNo` | String |  |  |
| 23 | `FS.GA.LIMIT.GLOBAL.RISK.INPUTTER` | `FsGaLimitGlobalRisk_Inputter` |  |  |  |
| 24 | `FS.GA.LIMIT.GLOBAL.RISK.DATE.TIME` | `FsGaLimitGlobalRisk_DateTime` |  |  |  |
| 25 | `FS.GA.LIMIT.GLOBAL.RISK.AUTHORISER` | `FsGaLimitGlobalRisk_Authoriser` | String |  |  |
| 26 | `FS.GA.LIMIT.GLOBAL.RISK.CO.CODE` | `FsGaLimitGlobalRisk_CoCode` | String |  |  |
| 27 | `FS.GA.LIMIT.GLOBAL.RISK.DEPT.CODE` | `FsGaLimitGlobalRisk_DeptCode` | String |  |  |
| 28 | `FS.GA.LIMIT.GLOBAL.RISK.AUDITOR.CODE` | `FsGaLimitGlobalRisk_AuditorCode` | String |  |  |
| 29 | `FS.GA.LIMIT.GLOBAL.RISK.AUDIT.DATE.TIME` | `FsGaLimitGlobalRisk_AuditDateTime` | String |  |  |
