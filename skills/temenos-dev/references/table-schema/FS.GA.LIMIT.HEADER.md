# FS.GA.LIMIT.HEADER — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.HEADER` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.HEADER.GROUP.LIMIT` | `FsGaLimitHeader_GroupLimit` | TField |  | Group Limit Multifonds DB Column is CLEGIS. |
| 2 | `FS.GA.LIMIT.HEADER.INVESTMENT.RESTRICTION.LAW` | `FsGaLimitHeader_InvestmentRestrictionLaw` | TField |  | Select investment restriction law code as predefined. This is specifically created to support various investment restriction or limits. Used in new limits module. Multifonds DB Column is CLAW. |
| 3 | `FS.GA.LIMIT.HEADER.LIMIT.GROUP.CODE` | `FsGaLimitHeader_LimitGroupCode` | TField |  | This shows the limit group code while defining investment restrictions. This code is linked in fund to have the investment restrictions laws for the fund. Multifonds DB Column is NSL_NO. |
| 4 | `FS.GA.LIMIT.HEADER.NUMERATOR.CODE` | `FsGaLimitHeader_NumeratorCode` | TField |  | This shows different options of numerator codes that available while defining limit law restrictions. Specifically used in new limits module. Multifonds DB Column is CNUM_CODE. |
| 5 | `FS.GA.LIMIT.HEADER.DENOMINATOR.CODE` | `FsGaLimitHeader_DenominatorCode` | TField |  | Corresponds to the Denominator code to be used for investment restriction rule. Multifonds DB Column is CDENO_CODE. |
| 6 | `FS.GA.LIMIT.HEADER.DEACTIVATE` | `FsGaLimitHeader_Deactivate` | TField |  | Field to control a respective law. Multifonds DB Column is CDEACTIV. |
| 7 | `FS.GA.LIMIT.HEADER.NUMERATOR.SPLIT.BY` | `FsGaLimitHeader_NumeratorSplitBy` | TField |  | For numerator, field that allows to enter a split by condition. Multifonds DB Column is CNUM_GRPBY. |
| 8 | `FS.GA.LIMIT.HEADER.DENOMINATOR.SPLIT.BY` | `FsGaLimitHeader_DenominatorSplitBy` | TField |  | For denominator, field that allows to enter a split by condition. Multifonds DB Column is CDENO_GRPBY. |
| 9 | `FS.GA.LIMIT.HEADER.CONDITION` | `FsGaLimitHeader_Condition` | TField |  | Enables users to define, for the same law code, a next level control. Multifonds DB Column is TYP_CLIMIT. |
| 10 | `FS.GA.LIMIT.HEADER.RESERVED10` | `FsGaLimitHeader_Reserved10` | TField |  |  |
| 11 | `FS.GA.LIMIT.HEADER.RESERVED9` | `FsGaLimitHeader_Reserved9` | TField |  |  |
| 12 | `FS.GA.LIMIT.HEADER.RESERVED8` | `FsGaLimitHeader_Reserved8` | TField |  |  |
| 13 | `FS.GA.LIMIT.HEADER.RESERVED7` | `FsGaLimitHeader_Reserved7` | TField |  |  |
| 14 | `FS.GA.LIMIT.HEADER.RESERVED6` | `FsGaLimitHeader_Reserved6` | TField |  |  |
| 15 | `FS.GA.LIMIT.HEADER.RESERVED5` | `FsGaLimitHeader_Reserved5` | TField |  |  |
| 16 | `FS.GA.LIMIT.HEADER.RESERVED4` | `FsGaLimitHeader_Reserved4` | TField |  |  |
| 17 | `FS.GA.LIMIT.HEADER.RESERVED3` | `FsGaLimitHeader_Reserved3` | TField |  |  |
| 18 | `FS.GA.LIMIT.HEADER.RESERVED2` | `FsGaLimitHeader_Reserved2` | TField |  |  |
| 19 | `FS.GA.LIMIT.HEADER.RESERVED1` | `FsGaLimitHeader_Reserved1` | TField |  |  |
| 20 | `FS.GA.LIMIT.HEADER.RECORD.STATUS` | `FsGaLimitHeader_RecordStatus` | String |  |  |
| 21 | `FS.GA.LIMIT.HEADER.CURR.NO` | `FsGaLimitHeader_CurrNo` | String |  |  |
| 22 | `FS.GA.LIMIT.HEADER.INPUTTER` | `FsGaLimitHeader_Inputter` |  |  |  |
| 23 | `FS.GA.LIMIT.HEADER.DATE.TIME` | `FsGaLimitHeader_DateTime` |  |  |  |
| 24 | `FS.GA.LIMIT.HEADER.AUTHORISER` | `FsGaLimitHeader_Authoriser` | String |  |  |
| 25 | `FS.GA.LIMIT.HEADER.CO.CODE` | `FsGaLimitHeader_CoCode` | String |  |  |
| 26 | `FS.GA.LIMIT.HEADER.DEPT.CODE` | `FsGaLimitHeader_DeptCode` | String |  |  |
| 27 | `FS.GA.LIMIT.HEADER.AUDITOR.CODE` | `FsGaLimitHeader_AuditorCode` | String |  |  |
| 28 | `FS.GA.LIMIT.HEADER.AUDIT.DATE.TIME` | `FsGaLimitHeader_AuditDateTime` | String |  |  |
