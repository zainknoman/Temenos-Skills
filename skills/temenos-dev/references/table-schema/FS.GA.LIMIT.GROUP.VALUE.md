# FS.GA.LIMIT.GROUP.VALUE — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.GROUP.VALUE` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.GROUP.VALUE.GROUP.LIMIT` | `FsGaLimitGroupValue_GroupLimit` | TField |  | Group Limit Multifonds DB Column is CLEGIS. |
| 2 | `FS.GA.LIMIT.GROUP.VALUE.INVESTMENT.RESTRICTION.LAW` | `FsGaLimitGroupValue_InvestmentRestrictionLaw` | TField |  | Select investment restriction law code as predefined. This is specifically created to support various investment restriction or limits. Used in new limits module. Multifonds DB Column is CLAW. |
| 3 | `FS.GA.LIMIT.GROUP.VALUE.LIMIT.LEVEL` | `FsGaLimitGroupValue_LimitLevel` | TField |  | It specifies the limit levels Multifonds DB Column is CLEVEL. |
| 4 | `FS.GA.LIMIT.GROUP.VALUE.EXIT` | `FsGaLimitGroupValue_Exit` | TField |  | Exit Multifonds DB Column is CEXIT. |
| 5 | `FS.GA.LIMIT.GROUP.VALUE.APPLY.ON` | `FsGaLimitGroupValue_ApplyOn` | TField |  | Field to be set while setting up parameters of new limits. Multifonds DB Column is CAPPLIC. |
| 6 | `FS.GA.LIMIT.GROUP.VALUE.LIMIT.TYPE` | `FsGaLimitGroupValue_LimitType` | TField |  | It specifies the type of limit. Example Amount, Percent etc Multifonds DB Column is TYP_LIM. |
| 7 | `FS.GA.LIMIT.GROUP.VALUE.AMOUNT.TYPE` | `FsGaLimitGroupValue_AmountType` | TField |  | The type of amount (ex. Average Nav, Nav after P/L allocation etc.) can be defined as the amount used as basis for further calculation ex. Nav Charges. Multifonds DB Column is TYP_MNT. |
| 8 | `FS.GA.LIMIT.GROUP.VALUE.CURRENCY.LIMITS` | `FsGaLimitGroupValue_CurrencyLimits` | TField |  | To set a Currency for Limits Multifonds DB Column is CMON_LIM. |
| 9 | `FS.GA.LIMIT.GROUP.VALUE.LIMIT.MINIMUM.PERCENT` | `FsGaLimitGroupValue_LimitMinimumPercent` | TField |  | It specidfies the minimum percent of limit to be applied Multifonds DB Column is PC_MIN_LIM. |
| 10 | `FS.GA.LIMIT.GROUP.VALUE.LIMIT.MINIMUM.AMOUNT` | `FsGaLimitGroupValue_LimitMinimumAmount` | TField |  | It specifies the minimum amount of limit to be applied Multifonds DB Column is MNT_MIN_LIM. |
| 11 | `FS.GA.LIMIT.GROUP.VALUE.LIMIT.MAXIMUM.PERCENT` | `FsGaLimitGroupValue_LimitMaximumPercent` | TField |  | It specidfies the maximum percent of limit to be applied Multifonds DB Column is PC_MAX_LIM. |
| 12 | `FS.GA.LIMIT.GROUP.VALUE.MAXIMUM.LIMIT.AMOUNT` | `FsGaLimitGroupValue_MaximumLimitAmount` | TField |  | It specifies the maximum amount of limit to be applied. Multifonds DB Column is MNT_MAX_LIM. |
| 13 | `FS.GA.LIMIT.GROUP.VALUE.LIMIT.DURATION.PERCENT` | `FsGaLimitGroupValue_LimitDurationPercent` | TField |  | It specifies the duration percent of limit to be applied Multifonds DB Column is PC_DUREE. |
| 14 | `FS.GA.LIMIT.GROUP.VALUE.LIMIT.IMPORTANCE.LEVEL` | `FsGaLimitGroupValue_LimitImportanceLevel` | TField |  | It specidies the importance level of the group limit which is applied Multifonds DB Column is CIMPORTANCE. |
| 15 | `FS.GA.LIMIT.GROUP.VALUE.RESERVED10` | `FsGaLimitGroupValue_Reserved10` | TField |  |  |
| 16 | `FS.GA.LIMIT.GROUP.VALUE.RESERVED9` | `FsGaLimitGroupValue_Reserved9` | TField |  |  |
| 17 | `FS.GA.LIMIT.GROUP.VALUE.RESERVED8` | `FsGaLimitGroupValue_Reserved8` | TField |  |  |
| 18 | `FS.GA.LIMIT.GROUP.VALUE.RESERVED7` | `FsGaLimitGroupValue_Reserved7` | TField |  |  |
| 19 | `FS.GA.LIMIT.GROUP.VALUE.RESERVED6` | `FsGaLimitGroupValue_Reserved6` | TField |  |  |
| 20 | `FS.GA.LIMIT.GROUP.VALUE.RESERVED5` | `FsGaLimitGroupValue_Reserved5` | TField |  |  |
| 21 | `FS.GA.LIMIT.GROUP.VALUE.RESERVED4` | `FsGaLimitGroupValue_Reserved4` | TField |  |  |
| 22 | `FS.GA.LIMIT.GROUP.VALUE.RESERVED3` | `FsGaLimitGroupValue_Reserved3` | TField |  |  |
| 23 | `FS.GA.LIMIT.GROUP.VALUE.RESERVED2` | `FsGaLimitGroupValue_Reserved2` | TField |  |  |
| 24 | `FS.GA.LIMIT.GROUP.VALUE.RESERVED1` | `FsGaLimitGroupValue_Reserved1` | TField |  |  |
| 25 | `FS.GA.LIMIT.GROUP.VALUE.RECORD.STATUS` | `FsGaLimitGroupValue_RecordStatus` | String |  |  |
| 26 | `FS.GA.LIMIT.GROUP.VALUE.CURR.NO` | `FsGaLimitGroupValue_CurrNo` | String |  |  |
| 27 | `FS.GA.LIMIT.GROUP.VALUE.INPUTTER` | `FsGaLimitGroupValue_Inputter` |  |  |  |
| 28 | `FS.GA.LIMIT.GROUP.VALUE.DATE.TIME` | `FsGaLimitGroupValue_DateTime` |  |  |  |
| 29 | `FS.GA.LIMIT.GROUP.VALUE.AUTHORISER` | `FsGaLimitGroupValue_Authoriser` | String |  |  |
| 30 | `FS.GA.LIMIT.GROUP.VALUE.CO.CODE` | `FsGaLimitGroupValue_CoCode` | String |  |  |
| 31 | `FS.GA.LIMIT.GROUP.VALUE.DEPT.CODE` | `FsGaLimitGroupValue_DeptCode` | String |  |  |
| 32 | `FS.GA.LIMIT.GROUP.VALUE.AUDITOR.CODE` | `FsGaLimitGroupValue_AuditorCode` | String |  |  |
| 33 | `FS.GA.LIMIT.GROUP.VALUE.AUDIT.DATE.TIME` | `FsGaLimitGroupValue_AuditDateTime` | String |  |  |
