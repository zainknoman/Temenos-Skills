# FS.GA.LIMIT.LEGISLATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.LEGISLATION.PARAMETER` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.GROUP.LIMIT` | `FsGaLimitLegislationParameter_GroupLimit` | TField |  | Group Limit Multifonds DB Column is CLEGIS. |
| 2 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.INVESTMENT.RESTRICTION.LAW` | `FsGaLimitLegislationParameter_InvestmentRestrictionLaw` | TField |  | Select investment restriction law code as predefined. This is specifically created to support various investment restriction or limits. Used in new limits module. Multifonds DB Column is CLAW. |
| 3 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.LIMIT.LEVEL` | `FsGaLimitLegislationParameter_LimitLevel` | TField |  | It specifies the limit levels Multifonds DB Column is CLEVEL. |
| 4 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.EXIT` | `FsGaLimitLegislationParameter_Exit` | TField |  | Exit Multifonds DB Column is CEXIT. |
| 5 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.APPLY.ON` | `FsGaLimitLegislationParameter_ApplyOn` | TField |  | Field to be set while setting up parameters of new limits. Multifonds DB Column is CAPPLIC. |
| 6 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.LIMIT.GROUP` | `FsGaLimitLegislationParameter_LimitGroup` | TField |  | Limit Group. Multifonds DB Column is CGROUP. |
| 7 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.LIMIT.TYPE` | `FsGaLimitLegislationParameter_LimitType` | TField |  | It specifies the type of limit. Example Amount, Percent etc Multifonds DB Column is TYP_LIM. |
| 8 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.AMOUNT.TYPE` | `FsGaLimitLegislationParameter_AmountType` | TField |  | The type of amount (ex. Average Nav, Nav after P/L allocation etc.) can be defined as the amount used as basis for further calculation ex. Nav Charges. Multifonds DB Column is TYP_MNT. |
| 9 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.CURRENCY.LIMITS` | `FsGaLimitLegislationParameter_CurrencyLimits` | TField |  | To set a Currency for Limits Multifonds DB Column is CMON_LIM. |
| 10 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.LIMIT.MINIMUM.PERCENT` | `FsGaLimitLegislationParameter_LimitMinimumPercent` | TField |  | It specidfies the minimum percent of limit to be applied Multifonds DB Column is PC_MIN_LIM. |
| 11 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.LIMIT.MINIMUM.AMOUNT` | `FsGaLimitLegislationParameter_LimitMinimumAmount` | TField |  | It specifies the minimum amount of limit to be applied Multifonds DB Column is MNT_MIN_LIM. |
| 12 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.LIMIT.MAXIMUM.PERCENT` | `FsGaLimitLegislationParameter_LimitMaximumPercent` | TField |  | It specidfies the maximum percent of limit to be applied Multifonds DB Column is PC_MAX_LIM. |
| 13 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.MAXIMUM.LIMIT.AMOUNT` | `FsGaLimitLegislationParameter_MaximumLimitAmount` | TField |  | It specifies the maximum amount of limit to be applied. Multifonds DB Column is MNT_MAX_LIM. |
| 14 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.LIMIT.DURATION.PERCENT` | `FsGaLimitLegislationParameter_LimitDurationPercent` | TField |  | It specifies the duration percent of limit to be applied Multifonds DB Column is PC_DUREE. |
| 15 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.LIMIT.IMPORTANCE.LEVEL` | `FsGaLimitLegislationParameter_LimitImportanceLevel` | TField |  | It specidies the importance level of the group limit which is applied Multifonds DB Column is CIMPORTANCE. |
| 16 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.AGGREGATE` | `FsGaLimitLegislationParameter_Aggregate` | TField |  | Possible consolidation of some limits for a management company. Multifonds DB Column is CAGR. |
| 17 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RESERVED10` | `FsGaLimitLegislationParameter_Reserved10` | TField |  |  |
| 18 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RESERVED9` | `FsGaLimitLegislationParameter_Reserved9` | TField |  |  |
| 19 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RESERVED8` | `FsGaLimitLegislationParameter_Reserved8` | TField |  |  |
| 20 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RESERVED7` | `FsGaLimitLegislationParameter_Reserved7` | TField |  |  |
| 21 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RESERVED6` | `FsGaLimitLegislationParameter_Reserved6` | TField |  |  |
| 22 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RESERVED5` | `FsGaLimitLegislationParameter_Reserved5` | TField |  |  |
| 23 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RESERVED4` | `FsGaLimitLegislationParameter_Reserved4` | TField |  |  |
| 24 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RESERVED3` | `FsGaLimitLegislationParameter_Reserved3` | TField |  |  |
| 25 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RESERVED2` | `FsGaLimitLegislationParameter_Reserved2` | TField |  |  |
| 26 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RESERVED1` | `FsGaLimitLegislationParameter_Reserved1` | TField |  |  |
| 27 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.RECORD.STATUS` | `FsGaLimitLegislationParameter_RecordStatus` | String |  |  |
| 28 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.CURR.NO` | `FsGaLimitLegislationParameter_CurrNo` | String |  |  |
| 29 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.INPUTTER` | `FsGaLimitLegislationParameter_Inputter` |  |  |  |
| 30 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.DATE.TIME` | `FsGaLimitLegislationParameter_DateTime` |  |  |  |
| 31 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.AUTHORISER` | `FsGaLimitLegislationParameter_Authoriser` | String |  |  |
| 32 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.CO.CODE` | `FsGaLimitLegislationParameter_CoCode` | String |  |  |
| 33 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.DEPT.CODE` | `FsGaLimitLegislationParameter_DeptCode` | String |  |  |
| 34 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.AUDITOR.CODE` | `FsGaLimitLegislationParameter_AuditorCode` | String |  |  |
| 35 | `FS.GA.LIMIT.LEGISLATION.PARAMETER.AUDIT.DATE.TIME` | `FsGaLimitLegislationParameter_AuditDateTime` | String |  |  |
