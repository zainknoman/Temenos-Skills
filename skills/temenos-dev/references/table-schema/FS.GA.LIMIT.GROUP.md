# FS.GA.LIMIT.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.GROUP` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.GROUP.GROUP.LIMIT` | `FsGaLimitGroup_GroupLimit` | TField |  | Group Limit Multifonds DB Column is CLEGIS. |
| 2 | `FS.GA.LIMIT.GROUP.INVESTMENT.RESTRICTION.LAW` | `FsGaLimitGroup_InvestmentRestrictionLaw` | TField |  | Select investment restriction law code as predefined. This is specifically created to support various investment restriction or limits. Used in new limits module. Multifonds DB Column is CLAW. |
| 3 | `FS.GA.LIMIT.GROUP.LIMIT.LEVEL` | `FsGaLimitGroup_LimitLevel` | TField |  | It specifies the limit levels Multifonds DB Column is CLEVEL. |
| 4 | `FS.GA.LIMIT.GROUP.GTI.CODE` | `FsGaLimitGroup_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 5 | `FS.GA.LIMIT.GROUP.RESERVED10` | `FsGaLimitGroup_Reserved10` | TField |  |  |
| 6 | `FS.GA.LIMIT.GROUP.RESERVED9` | `FsGaLimitGroup_Reserved9` | TField |  |  |
| 7 | `FS.GA.LIMIT.GROUP.RESERVED8` | `FsGaLimitGroup_Reserved8` | TField |  |  |
| 8 | `FS.GA.LIMIT.GROUP.RESERVED7` | `FsGaLimitGroup_Reserved7` | TField |  |  |
| 9 | `FS.GA.LIMIT.GROUP.RESERVED6` | `FsGaLimitGroup_Reserved6` | TField |  |  |
| 10 | `FS.GA.LIMIT.GROUP.RESERVED5` | `FsGaLimitGroup_Reserved5` | TField |  |  |
| 11 | `FS.GA.LIMIT.GROUP.RESERVED4` | `FsGaLimitGroup_Reserved4` | TField |  |  |
| 12 | `FS.GA.LIMIT.GROUP.RESERVED3` | `FsGaLimitGroup_Reserved3` | TField |  |  |
| 13 | `FS.GA.LIMIT.GROUP.RESERVED2` | `FsGaLimitGroup_Reserved2` | TField |  |  |
| 14 | `FS.GA.LIMIT.GROUP.RESERVED1` | `FsGaLimitGroup_Reserved1` | TField |  |  |
| 15 | `FS.GA.LIMIT.GROUP.RECORD.STATUS` | `FsGaLimitGroup_RecordStatus` | String |  |  |
| 16 | `FS.GA.LIMIT.GROUP.CURR.NO` | `FsGaLimitGroup_CurrNo` | String |  |  |
| 17 | `FS.GA.LIMIT.GROUP.INPUTTER` | `FsGaLimitGroup_Inputter` |  |  |  |
| 18 | `FS.GA.LIMIT.GROUP.DATE.TIME` | `FsGaLimitGroup_DateTime` |  |  |  |
| 19 | `FS.GA.LIMIT.GROUP.AUTHORISER` | `FsGaLimitGroup_Authoriser` | String |  |  |
| 20 | `FS.GA.LIMIT.GROUP.CO.CODE` | `FsGaLimitGroup_CoCode` | String |  |  |
| 21 | `FS.GA.LIMIT.GROUP.DEPT.CODE` | `FsGaLimitGroup_DeptCode` | String |  |  |
| 22 | `FS.GA.LIMIT.GROUP.AUDITOR.CODE` | `FsGaLimitGroup_AuditorCode` | String |  |  |
| 23 | `FS.GA.LIMIT.GROUP.AUDIT.DATE.TIME` | `FsGaLimitGroup_AuditDateTime` | String |  |  |
