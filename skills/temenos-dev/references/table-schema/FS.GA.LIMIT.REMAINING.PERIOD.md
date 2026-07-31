# FS.GA.LIMIT.REMAINING.PERIOD — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.REMAINING.PERIOD` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.REMAINING.PERIOD.GROUP.LIMIT` | `FsGaLimitRemainingPeriod_GroupLimit` | TField |  | Group Limit Multifonds DB Column is CLEGIS. |
| 2 | `FS.GA.LIMIT.REMAINING.PERIOD.INVESTMENT.RESTRICTION.LAW` | `FsGaLimitRemainingPeriod_InvestmentRestrictionLaw` | TField |  | Select investment restriction law code as predefined. This is specifically created to support various investment restriction or limits. Used in new limits module. Multifonds DB Column is CLAW. |
| 3 | `FS.GA.LIMIT.REMAINING.PERIOD.GRP.FOR.POSITIVE.AMT.VAL.MOD` | `FsGaLimitRemainingPeriod_GrpForPositiveAmtValMod` | TField |  | A group ID as defined under CMESS table 'GR' to which GTI codes or Reporting codes should be linked Multifonds DB Column is NGROUP. |
| 4 | `FS.GA.LIMIT.REMAINING.PERIOD.GL.ACCOUNT` | `FsGaLimitRemainingPeriod_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.LIMIT.REMAINING.PERIOD.OPERATION.CODE` | `FsGaLimitRemainingPeriod_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 6 | `FS.GA.LIMIT.REMAINING.PERIOD.GTI.CODE` | `FsGaLimitRemainingPeriod_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 7 | `FS.GA.LIMIT.REMAINING.PERIOD.INCOME.TYPE` | `FsGaLimitRemainingPeriod_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 8 | `FS.GA.LIMIT.REMAINING.PERIOD.REPORTING.CODE` | `FsGaLimitRemainingPeriod_ReportingCode` | TField |  | This is the reporting code tagged to an account. Multifonds DB Column is CODE_RAPPORT. |
| 9 | `FS.GA.LIMIT.REMAINING.PERIOD.REVERSE.REPO` | `FsGaLimitRemainingPeriod_ReverseRepo` | TField |  | This field displays the reverse repo code for the given valuation group Multifonds DB Column is CODE_RAPPORT_REV. |
| 10 | `FS.GA.LIMIT.REMAINING.PERIOD.DAYS.TO.MATURITY.CODE` | `FsGaLimitRemainingPeriod_DaysToMaturityCode` | TField |  | This field displays the basis of calculation for days to maturity Multifonds DB Column is DTM_CODE. |
| 11 | `FS.GA.LIMIT.REMAINING.PERIOD.NUMERATOR.CODE` | `FsGaLimitRemainingPeriod_NumeratorCode` | TField |  | This shows different options of numerator codes thats available while defining limit law restrictions. Specifically used in new limits module. Multifonds DB Column is CNUM_CODE. |
| 12 | `FS.GA.LIMIT.REMAINING.PERIOD.AMOUNT.TYPE.VARIABLE` | `FsGaLimitRemainingPeriod_AmountTypeVariable` | TField |  | This field displays the Select the basis used for Remaining period calculation. Options available are elements defined under CMESS table LIB-LIM-Short LP1 Multifonds DB Column is AMT_TYPE. |
| 13 | `FS.GA.LIMIT.REMAINING.PERIOD.COLLATERAL.SECURITY.FLAG` | `FsGaLimitRemainingPeriod_CollateralSecurityFlag` | TField |  | This field displays whether the collateral security flag is ticked or not. When flagged, it uses underlying security information for remaining period calculation Multifonds DB Column is FLG_COLL_SECURITY. |
| 14 | `FS.GA.LIMIT.REMAINING.PERIOD.RESERVED10` | `FsGaLimitRemainingPeriod_Reserved10` | TField |  |  |
| 15 | `FS.GA.LIMIT.REMAINING.PERIOD.RESERVED9` | `FsGaLimitRemainingPeriod_Reserved9` | TField |  |  |
| 16 | `FS.GA.LIMIT.REMAINING.PERIOD.RESERVED8` | `FsGaLimitRemainingPeriod_Reserved8` | TField |  |  |
| 17 | `FS.GA.LIMIT.REMAINING.PERIOD.RESERVED7` | `FsGaLimitRemainingPeriod_Reserved7` | TField |  |  |
| 18 | `FS.GA.LIMIT.REMAINING.PERIOD.RESERVED6` | `FsGaLimitRemainingPeriod_Reserved6` | TField |  |  |
| 19 | `FS.GA.LIMIT.REMAINING.PERIOD.RESERVED5` | `FsGaLimitRemainingPeriod_Reserved5` | TField |  |  |
| 20 | `FS.GA.LIMIT.REMAINING.PERIOD.RESERVED4` | `FsGaLimitRemainingPeriod_Reserved4` | TField |  |  |
| 21 | `FS.GA.LIMIT.REMAINING.PERIOD.RESERVED3` | `FsGaLimitRemainingPeriod_Reserved3` | TField |  |  |
| 22 | `FS.GA.LIMIT.REMAINING.PERIOD.RESERVED2` | `FsGaLimitRemainingPeriod_Reserved2` | TField |  |  |
| 23 | `FS.GA.LIMIT.REMAINING.PERIOD.RESERVED1` | `FsGaLimitRemainingPeriod_Reserved1` | TField |  |  |
| 24 | `FS.GA.LIMIT.REMAINING.PERIOD.RECORD.STATUS` | `FsGaLimitRemainingPeriod_RecordStatus` | String |  |  |
| 25 | `FS.GA.LIMIT.REMAINING.PERIOD.CURR.NO` | `FsGaLimitRemainingPeriod_CurrNo` | String |  |  |
| 26 | `FS.GA.LIMIT.REMAINING.PERIOD.INPUTTER` | `FsGaLimitRemainingPeriod_Inputter` |  |  |  |
| 27 | `FS.GA.LIMIT.REMAINING.PERIOD.DATE.TIME` | `FsGaLimitRemainingPeriod_DateTime` |  |  |  |
| 28 | `FS.GA.LIMIT.REMAINING.PERIOD.AUTHORISER` | `FsGaLimitRemainingPeriod_Authoriser` | String |  |  |
| 29 | `FS.GA.LIMIT.REMAINING.PERIOD.CO.CODE` | `FsGaLimitRemainingPeriod_CoCode` | String |  |  |
| 30 | `FS.GA.LIMIT.REMAINING.PERIOD.DEPT.CODE` | `FsGaLimitRemainingPeriod_DeptCode` | String |  |  |
| 31 | `FS.GA.LIMIT.REMAINING.PERIOD.AUDITOR.CODE` | `FsGaLimitRemainingPeriod_AuditorCode` | String |  |  |
| 32 | `FS.GA.LIMIT.REMAINING.PERIOD.AUDIT.DATE.TIME` | `FsGaLimitRemainingPeriod_AuditDateTime` | String |  |  |
