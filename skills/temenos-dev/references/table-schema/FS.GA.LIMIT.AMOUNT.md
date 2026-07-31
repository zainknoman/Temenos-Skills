# FS.GA.LIMIT.AMOUNT — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.AMOUNT` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.AMOUNT.GROUP.LIMIT` | `FsGaLimitAmount_GroupLimit` | TField |  | Group Limit Multifonds DB Column is CLEGIS. |
| 2 | `FS.GA.LIMIT.AMOUNT.INVESTMENT.RESTRICTION.LAW` | `FsGaLimitAmount_InvestmentRestrictionLaw` | TField |  | Select investment restriction law code as predefined. This is specifically created to support various investment restriction or limits. Used in new limits module. Multifonds DB Column is CLAW. |
| 3 | `FS.GA.LIMIT.AMOUNT.LIMIT.LEVEL` | `FsGaLimitAmount_LimitLevel` | TField |  | It specifies the limit levels Multifonds DB Column is CLEVEL. |
| 4 | `FS.GA.LIMIT.AMOUNT.APPLY.ON` | `FsGaLimitAmount_ApplyOn` | TField |  | Field to be set while setting up parameters of new limits. Multifonds DB Column is CAPPLIC. |
| 5 | `FS.GA.LIMIT.AMOUNT.LIMITS.VALUE` | `FsGaLimitAmount_LimitsValue` | TField |  | Specify the values as per the selected operators while defining limits or investment restrictions. To be asset type code, security identifier, amount or any value depending on the operators selected. Multifonds DB Column is CVALUE. |
| 6 | `FS.GA.LIMIT.AMOUNT.CHART.OF.ACCOUNTS.CODE` | `FsGaLimitAmount_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 7 | `FS.GA.LIMIT.AMOUNT.CT.AMOUNT` | `FsGaLimitAmount_CtAmount` | TField |  | CT Amount Multifonds DB Column is CTMNT. |
| 8 | `FS.GA.LIMIT.AMOUNT.RESERVED10` | `FsGaLimitAmount_Reserved10` | TField |  |  |
| 9 | `FS.GA.LIMIT.AMOUNT.RESERVED9` | `FsGaLimitAmount_Reserved9` | TField |  |  |
| 10 | `FS.GA.LIMIT.AMOUNT.RESERVED8` | `FsGaLimitAmount_Reserved8` | TField |  |  |
| 11 | `FS.GA.LIMIT.AMOUNT.RESERVED7` | `FsGaLimitAmount_Reserved7` | TField |  |  |
| 12 | `FS.GA.LIMIT.AMOUNT.RESERVED6` | `FsGaLimitAmount_Reserved6` | TField |  |  |
| 13 | `FS.GA.LIMIT.AMOUNT.RESERVED5` | `FsGaLimitAmount_Reserved5` | TField |  |  |
| 14 | `FS.GA.LIMIT.AMOUNT.RESERVED4` | `FsGaLimitAmount_Reserved4` | TField |  |  |
| 15 | `FS.GA.LIMIT.AMOUNT.RESERVED3` | `FsGaLimitAmount_Reserved3` | TField |  |  |
| 16 | `FS.GA.LIMIT.AMOUNT.RESERVED2` | `FsGaLimitAmount_Reserved2` | TField |  |  |
| 17 | `FS.GA.LIMIT.AMOUNT.RESERVED1` | `FsGaLimitAmount_Reserved1` | TField |  |  |
| 18 | `FS.GA.LIMIT.AMOUNT.RECORD.STATUS` | `FsGaLimitAmount_RecordStatus` | String |  |  |
| 19 | `FS.GA.LIMIT.AMOUNT.CURR.NO` | `FsGaLimitAmount_CurrNo` | String |  |  |
| 20 | `FS.GA.LIMIT.AMOUNT.INPUTTER` | `FsGaLimitAmount_Inputter` |  |  |  |
| 21 | `FS.GA.LIMIT.AMOUNT.DATE.TIME` | `FsGaLimitAmount_DateTime` |  |  |  |
| 22 | `FS.GA.LIMIT.AMOUNT.AUTHORISER` | `FsGaLimitAmount_Authoriser` | String |  |  |
| 23 | `FS.GA.LIMIT.AMOUNT.CO.CODE` | `FsGaLimitAmount_CoCode` | String |  |  |
| 24 | `FS.GA.LIMIT.AMOUNT.DEPT.CODE` | `FsGaLimitAmount_DeptCode` | String |  |  |
| 25 | `FS.GA.LIMIT.AMOUNT.AUDITOR.CODE` | `FsGaLimitAmount_AuditorCode` | String |  |  |
| 26 | `FS.GA.LIMIT.AMOUNT.AUDIT.DATE.TIME` | `FsGaLimitAmount_AuditDateTime` | String |  |  |
