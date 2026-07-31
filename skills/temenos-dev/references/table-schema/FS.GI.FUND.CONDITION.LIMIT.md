# FS.GI.FUND.CONDITION.LIMIT — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.CONDITION.LIMIT` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.CONDITION.LIMIT.PARENT.REF.ID` | `FsGiFundConditionLimit_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.CONDITION.LIMIT.ORA.ROWID` | `FsGiFundConditionLimit_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.CONDITION.LIMIT.FUND.ID` | `FsGiFundConditionLimit_FundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.CONDITION.LIMIT.SHARE.CLASS.CODE` | `FsGiFundConditionLimit_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 5 | `FS.GI.FUND.CONDITION.LIMIT.OPERATION.CODE` | `FsGiFundConditionLimit_OperationCode` | TField |  | Transaction type in scope of conditional limit parameterisation . Multifonds DB Column is COPERATION. |
| 6 | `FS.GI.FUND.CONDITION.LIMIT.DEFAULT.CONDITION` | `FsGiFundConditionLimit_DefaultCondition` | TField |  | Default conditional code. Multifonds DB Column is DEFAULT_COND. |
| 7 | `FS.GI.FUND.CONDITION.LIMIT.RESERVED10` | `FsGiFundConditionLimit_Reserved10` | TField |  |  |
| 8 | `FS.GI.FUND.CONDITION.LIMIT.RESERVED9` | `FsGiFundConditionLimit_Reserved9` | TField |  |  |
| 9 | `FS.GI.FUND.CONDITION.LIMIT.RESERVED8` | `FsGiFundConditionLimit_Reserved8` | TField |  |  |
| 10 | `FS.GI.FUND.CONDITION.LIMIT.RESERVED7` | `FsGiFundConditionLimit_Reserved7` | TField |  |  |
| 11 | `FS.GI.FUND.CONDITION.LIMIT.RESERVED6` | `FsGiFundConditionLimit_Reserved6` | TField |  |  |
| 12 | `FS.GI.FUND.CONDITION.LIMIT.RESERVED5` | `FsGiFundConditionLimit_Reserved5` | TField |  |  |
| 13 | `FS.GI.FUND.CONDITION.LIMIT.RESERVED4` | `FsGiFundConditionLimit_Reserved4` | TField |  |  |
| 14 | `FS.GI.FUND.CONDITION.LIMIT.RESERVED3` | `FsGiFundConditionLimit_Reserved3` | TField |  |  |
| 15 | `FS.GI.FUND.CONDITION.LIMIT.RESERVED2` | `FsGiFundConditionLimit_Reserved2` | TField |  |  |
| 16 | `FS.GI.FUND.CONDITION.LIMIT.RESERVED1` | `FsGiFundConditionLimit_Reserved1` | TField |  |  |
| 17 | `FS.GI.FUND.CONDITION.LIMIT.LOCAL.REF` | `FsGiFundConditionLimit_LocalRef` |  |  |  |
| 18 | `FS.GI.FUND.CONDITION.LIMIT.OVERRIDE` | `FsGiFundConditionLimit_Override` |  |  |  |
| 19 | `FS.GI.FUND.CONDITION.LIMIT.RECORD.STATUS` | `FsGiFundConditionLimit_RecordStatus` | String |  |  |
| 20 | `FS.GI.FUND.CONDITION.LIMIT.CURR.NO` | `FsGiFundConditionLimit_CurrNo` | String |  |  |
| 21 | `FS.GI.FUND.CONDITION.LIMIT.INPUTTER` | `FsGiFundConditionLimit_Inputter` |  |  |  |
| 22 | `FS.GI.FUND.CONDITION.LIMIT.DATE.TIME` | `FsGiFundConditionLimit_DateTime` |  |  |  |
| 23 | `FS.GI.FUND.CONDITION.LIMIT.AUTHORISER` | `FsGiFundConditionLimit_Authoriser` | String |  |  |
| 24 | `FS.GI.FUND.CONDITION.LIMIT.CO.CODE` | `FsGiFundConditionLimit_CoCode` | String |  |  |
| 25 | `FS.GI.FUND.CONDITION.LIMIT.DEPT.CODE` | `FsGiFundConditionLimit_DeptCode` | String |  |  |
| 26 | `FS.GI.FUND.CONDITION.LIMIT.AUDITOR.CODE` | `FsGiFundConditionLimit_AuditorCode` | String |  |  |
| 27 | `FS.GI.FUND.CONDITION.LIMIT.AUDIT.DATE.TIME` | `FsGiFundConditionLimit_AuditDateTime` | String |  |  |
