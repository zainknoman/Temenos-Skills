# FS.GA.LIMIT.CASH — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.CASH` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.CASH.GROUP.LIMIT` | `FsGaLimitCash_GroupLimit` | TField |  | Group Limit Multifonds DB Column is CLEGIS. |
| 2 | `FS.GA.LIMIT.CASH.INVESTMENT.RESTRICTION.LAW` | `FsGaLimitCash_InvestmentRestrictionLaw` | TField |  | Select investment restriction law code as predefined. This is specifically created to support various investment restriction or limits. Used in new limits module. Multifonds DB Column is CLAW. |
| 3 | `FS.GA.LIMIT.CASH.LIMIT.LEVEL` | `FsGaLimitCash_LimitLevel` | TField |  | It specifies the limit levels Multifonds DB Column is CLEVEL. |
| 4 | `FS.GA.LIMIT.CASH.APPLY.ON` | `FsGaLimitCash_ApplyOn` | TField |  | Field to be set while setting up parameters of new limits. Multifonds DB Column is CAPPLIC. |
| 5 | `FS.GA.LIMIT.CASH.OPERATION.CODE` | `FsGaLimitCash_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 6 | `FS.GA.LIMIT.CASH.RESERVED10` | `FsGaLimitCash_Reserved10` | TField |  |  |
| 7 | `FS.GA.LIMIT.CASH.RESERVED9` | `FsGaLimitCash_Reserved9` | TField |  |  |
| 8 | `FS.GA.LIMIT.CASH.RESERVED8` | `FsGaLimitCash_Reserved8` | TField |  |  |
| 9 | `FS.GA.LIMIT.CASH.RESERVED7` | `FsGaLimitCash_Reserved7` | TField |  |  |
| 10 | `FS.GA.LIMIT.CASH.RESERVED6` | `FsGaLimitCash_Reserved6` | TField |  |  |
| 11 | `FS.GA.LIMIT.CASH.RESERVED5` | `FsGaLimitCash_Reserved5` | TField |  |  |
| 12 | `FS.GA.LIMIT.CASH.RESERVED4` | `FsGaLimitCash_Reserved4` | TField |  |  |
| 13 | `FS.GA.LIMIT.CASH.RESERVED3` | `FsGaLimitCash_Reserved3` | TField |  |  |
| 14 | `FS.GA.LIMIT.CASH.RESERVED2` | `FsGaLimitCash_Reserved2` | TField |  |  |
| 15 | `FS.GA.LIMIT.CASH.RESERVED1` | `FsGaLimitCash_Reserved1` | TField |  |  |
| 16 | `FS.GA.LIMIT.CASH.RECORD.STATUS` | `FsGaLimitCash_RecordStatus` | String |  |  |
| 17 | `FS.GA.LIMIT.CASH.CURR.NO` | `FsGaLimitCash_CurrNo` | String |  |  |
| 18 | `FS.GA.LIMIT.CASH.INPUTTER` | `FsGaLimitCash_Inputter` |  |  |  |
| 19 | `FS.GA.LIMIT.CASH.DATE.TIME` | `FsGaLimitCash_DateTime` |  |  |  |
| 20 | `FS.GA.LIMIT.CASH.AUTHORISER` | `FsGaLimitCash_Authoriser` | String |  |  |
| 21 | `FS.GA.LIMIT.CASH.CO.CODE` | `FsGaLimitCash_CoCode` | String |  |  |
| 22 | `FS.GA.LIMIT.CASH.DEPT.CODE` | `FsGaLimitCash_DeptCode` | String |  |  |
| 23 | `FS.GA.LIMIT.CASH.AUDITOR.CODE` | `FsGaLimitCash_AuditorCode` | String |  |  |
| 24 | `FS.GA.LIMIT.CASH.AUDIT.DATE.TIME` | `FsGaLimitCash_AuditDateTime` | String |  |  |
