# FS.GA.LIMIT.RULE.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.RULE.DETAIL` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.RULE.DETAIL.GROUP.LIMIT` | `FsGaLimitRuleDetail_GroupLimit` | TField |  | Group Limit Multifonds DB Column is CLEGIS. |
| 2 | `FS.GA.LIMIT.RULE.DETAIL.INVESTMENT.RESTRICTION.LAW` | `FsGaLimitRuleDetail_InvestmentRestrictionLaw` | TField |  | Select investment restriction law code as predefined. This is specifically created to support various investment restriction or limits. Used in new limits module. Multifonds DB Column is CLAW. |
| 3 | `FS.GA.LIMIT.RULE.DETAIL.LANGUAGE` | `FsGaLimitRuleDetail_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 4 | `FS.GA.LIMIT.RULE.DETAIL.LONG.DESC` | `FsGaLimitRuleDetail_LongDesc` | TField |  | This represents description of a report, export type, language name etc Multifonds DB Column is LIBELLE. |
| 5 | `FS.GA.LIMIT.RULE.DETAIL.RESERVED10` | `FsGaLimitRuleDetail_Reserved10` | TField |  |  |
| 6 | `FS.GA.LIMIT.RULE.DETAIL.RESERVED9` | `FsGaLimitRuleDetail_Reserved9` | TField |  |  |
| 7 | `FS.GA.LIMIT.RULE.DETAIL.RESERVED8` | `FsGaLimitRuleDetail_Reserved8` | TField |  |  |
| 8 | `FS.GA.LIMIT.RULE.DETAIL.RESERVED7` | `FsGaLimitRuleDetail_Reserved7` | TField |  |  |
| 9 | `FS.GA.LIMIT.RULE.DETAIL.RESERVED6` | `FsGaLimitRuleDetail_Reserved6` | TField |  |  |
| 10 | `FS.GA.LIMIT.RULE.DETAIL.RESERVED5` | `FsGaLimitRuleDetail_Reserved5` | TField |  |  |
| 11 | `FS.GA.LIMIT.RULE.DETAIL.RESERVED4` | `FsGaLimitRuleDetail_Reserved4` | TField |  |  |
| 12 | `FS.GA.LIMIT.RULE.DETAIL.RESERVED3` | `FsGaLimitRuleDetail_Reserved3` | TField |  |  |
| 13 | `FS.GA.LIMIT.RULE.DETAIL.RESERVED2` | `FsGaLimitRuleDetail_Reserved2` | TField |  |  |
| 14 | `FS.GA.LIMIT.RULE.DETAIL.RESERVED1` | `FsGaLimitRuleDetail_Reserved1` | TField |  |  |
| 15 | `FS.GA.LIMIT.RULE.DETAIL.RECORD.STATUS` | `FsGaLimitRuleDetail_RecordStatus` | String |  |  |
| 16 | `FS.GA.LIMIT.RULE.DETAIL.CURR.NO` | `FsGaLimitRuleDetail_CurrNo` | String |  |  |
| 17 | `FS.GA.LIMIT.RULE.DETAIL.INPUTTER` | `FsGaLimitRuleDetail_Inputter` |  |  |  |
| 18 | `FS.GA.LIMIT.RULE.DETAIL.DATE.TIME` | `FsGaLimitRuleDetail_DateTime` |  |  |  |
| 19 | `FS.GA.LIMIT.RULE.DETAIL.AUTHORISER` | `FsGaLimitRuleDetail_Authoriser` | String |  |  |
| 20 | `FS.GA.LIMIT.RULE.DETAIL.CO.CODE` | `FsGaLimitRuleDetail_CoCode` | String |  |  |
| 21 | `FS.GA.LIMIT.RULE.DETAIL.DEPT.CODE` | `FsGaLimitRuleDetail_DeptCode` | String |  |  |
| 22 | `FS.GA.LIMIT.RULE.DETAIL.AUDITOR.CODE` | `FsGaLimitRuleDetail_AuditorCode` | String |  |  |
| 23 | `FS.GA.LIMIT.RULE.DETAIL.AUDIT.DATE.TIME` | `FsGaLimitRuleDetail_AuditDateTime` | String |  |  |
