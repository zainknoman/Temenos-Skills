# FS.GA.LIMIT.VALUE — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.VALUE` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.VALUE.GROUP.LIMIT` | `FsGaLimitValue_GroupLimit` | TField |  | Group Limit Multifonds DB Column is CLEGIS. |
| 2 | `FS.GA.LIMIT.VALUE.INVESTMENT.RESTRICTION.LAW` | `FsGaLimitValue_InvestmentRestrictionLaw` | TField |  | Select investment restriction law code as predefined. This is specifically created to support various investment restriction or limits. Used in new limits module. Multifonds DB Column is CLAW. |
| 3 | `FS.GA.LIMIT.VALUE.LIMIT.LEVEL` | `FsGaLimitValue_LimitLevel` | TField |  | It specifies the limit levels Multifonds DB Column is CLEVEL. |
| 4 | `FS.GA.LIMIT.VALUE.APPLY.ON` | `FsGaLimitValue_ApplyOn` | TField |  | Field to be set while setting up parameters of new limits. Multifonds DB Column is CAPPLIC. |
| 5 | `FS.GA.LIMIT.VALUE.LIMITS.VALUE` | `FsGaLimitValue_LimitsValue` | TField |  | Specify the values as per the selected operators while defining limits or investment restrictions. To be asset type code, security identifier, amount or any value depending on the operators selected. Multifonds DB Column is CVALUE. |
| 6 | `FS.GA.LIMIT.VALUE.CHART.OF.ACCOUNTS.CODE` | `FsGaLimitValue_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 7 | `FS.GA.LIMIT.VALUE.RESERVED10` | `FsGaLimitValue_Reserved10` | TField |  |  |
| 8 | `FS.GA.LIMIT.VALUE.RESERVED9` | `FsGaLimitValue_Reserved9` | TField |  |  |
| 9 | `FS.GA.LIMIT.VALUE.RESERVED8` | `FsGaLimitValue_Reserved8` | TField |  |  |
| 10 | `FS.GA.LIMIT.VALUE.RESERVED7` | `FsGaLimitValue_Reserved7` | TField |  |  |
| 11 | `FS.GA.LIMIT.VALUE.RESERVED6` | `FsGaLimitValue_Reserved6` | TField |  |  |
| 12 | `FS.GA.LIMIT.VALUE.RESERVED5` | `FsGaLimitValue_Reserved5` | TField |  |  |
| 13 | `FS.GA.LIMIT.VALUE.RESERVED4` | `FsGaLimitValue_Reserved4` | TField |  |  |
| 14 | `FS.GA.LIMIT.VALUE.RESERVED3` | `FsGaLimitValue_Reserved3` | TField |  |  |
| 15 | `FS.GA.LIMIT.VALUE.RESERVED2` | `FsGaLimitValue_Reserved2` | TField |  |  |
| 16 | `FS.GA.LIMIT.VALUE.RESERVED1` | `FsGaLimitValue_Reserved1` | TField |  |  |
| 17 | `FS.GA.LIMIT.VALUE.RECORD.STATUS` | `FsGaLimitValue_RecordStatus` | String |  |  |
| 18 | `FS.GA.LIMIT.VALUE.CURR.NO` | `FsGaLimitValue_CurrNo` | String |  |  |
| 19 | `FS.GA.LIMIT.VALUE.INPUTTER` | `FsGaLimitValue_Inputter` |  |  |  |
| 20 | `FS.GA.LIMIT.VALUE.DATE.TIME` | `FsGaLimitValue_DateTime` |  |  |  |
| 21 | `FS.GA.LIMIT.VALUE.AUTHORISER` | `FsGaLimitValue_Authoriser` | String |  |  |
| 22 | `FS.GA.LIMIT.VALUE.CO.CODE` | `FsGaLimitValue_CoCode` | String |  |  |
| 23 | `FS.GA.LIMIT.VALUE.DEPT.CODE` | `FsGaLimitValue_DeptCode` | String |  |  |
| 24 | `FS.GA.LIMIT.VALUE.AUDITOR.CODE` | `FsGaLimitValue_AuditorCode` | String |  |  |
| 25 | `FS.GA.LIMIT.VALUE.AUDIT.DATE.TIME` | `FsGaLimitValue_AuditDateTime` | String |  |  |
