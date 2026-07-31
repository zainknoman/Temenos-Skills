# FS.GI.FUND.DIV.DIST.CALC.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.DIV.DIST.CALC.DETAILS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.PARENT.REF.ID` | `FsGiFundDivDistCalcDetails_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.ORA.ROWID` | `FsGiFundDivDistCalcDetails_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.TA.FUND.ID` | `FsGiFundDivDistCalcDetails_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.SHARE.CLASS.CODE` | `FsGiFundDivDistCalcDetails_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 5 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.PERIOD.END` | `FsGiFundDivDistCalcDetails_PeriodEnd` | TField |  | Period end for dividend distribution process. Multifonds DB Column is PERIOD_END. |
| 6 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.DIV.DISTRIBUTION.DAYS` | `FsGiFundDivDistCalcDetails_DivDistributionDays` | TField |  | Number of days for dividend distribution process. Multifonds DB Column is DAYS. |
| 7 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.SEPARATE.RATES.FLAG` | `FsGiFundDivDistCalcDetails_SeparateRatesFlag` | TField |  | Flag to allow accrual calculation for each calendar days. It will be caluclated for Saturday and Sunday on Friday available rates together and legal holiday as well. Multifonds DB Column is FLG_SEPARATE_RATES. |
| 8 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.TRUE.PERIOD.END.FLAG` | `FsGiFundDivDistCalcDetails_TruePeriodEndFlag` | TField |  | Flag to indicate the distribution amount calculation. Currently it follows the same setup of separate rates flag. If separate rates are flagged, True period end will be flagged automatically. Multifonds DB Column is FLG_TRUE_PERIOD_END. |
| 9 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.REINV.AT.END.OF.PERIOD.FLAG` | `FsGiFundDivDistCalcDetails_ReinvAtEndOfPeriodFlag` | TField |  | Flag to indicate that the reinvestment will be made on same working day or next working day when distributing positive amount of accruals. Multifonds DB Column is FLG_REINV_EOP. |
| 10 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RED.AT.END.OF.PERIOD.FLAG` | `FsGiFundDivDistCalcDetails_RedAtEndOfPeriodFlag` | TField |  | Flag to indicate that the redemption will be made on same working day or next working day when distributing negative A amount of accruals. Multifonds DB Column is FLG_RED_EOP. |
| 11 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.FUND.ID` | `FsGiFundDivDistCalcDetails_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 12 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.CLASS.CURRENCY` | `FsGiFundDivDistCalcDetails_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 13 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RESERVED10` | `FsGiFundDivDistCalcDetails_Reserved10` | TField |  |  |
| 14 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RESERVED9` | `FsGiFundDivDistCalcDetails_Reserved9` | TField |  |  |
| 15 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RESERVED8` | `FsGiFundDivDistCalcDetails_Reserved8` | TField |  |  |
| 16 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RESERVED7` | `FsGiFundDivDistCalcDetails_Reserved7` | TField |  |  |
| 17 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RESERVED6` | `FsGiFundDivDistCalcDetails_Reserved6` | TField |  |  |
| 18 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RESERVED5` | `FsGiFundDivDistCalcDetails_Reserved5` | TField |  |  |
| 19 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RESERVED4` | `FsGiFundDivDistCalcDetails_Reserved4` | TField |  |  |
| 20 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RESERVED3` | `FsGiFundDivDistCalcDetails_Reserved3` | TField |  |  |
| 21 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RESERVED2` | `FsGiFundDivDistCalcDetails_Reserved2` | TField |  |  |
| 22 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RESERVED1` | `FsGiFundDivDistCalcDetails_Reserved1` | TField |  |  |
| 23 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.LOCAL.REF` | `FsGiFundDivDistCalcDetails_LocalRef` |  |  |  |
| 24 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.OVERRIDE` | `FsGiFundDivDistCalcDetails_Override` |  |  |  |
| 25 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.RECORD.STATUS` | `FsGiFundDivDistCalcDetails_RecordStatus` | String |  |  |
| 26 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.CURR.NO` | `FsGiFundDivDistCalcDetails_CurrNo` | String |  |  |
| 27 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.INPUTTER` | `FsGiFundDivDistCalcDetails_Inputter` |  |  |  |
| 28 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.DATE.TIME` | `FsGiFundDivDistCalcDetails_DateTime` |  |  |  |
| 29 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.AUTHORISER` | `FsGiFundDivDistCalcDetails_Authoriser` | String |  |  |
| 30 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.CO.CODE` | `FsGiFundDivDistCalcDetails_CoCode` | String |  |  |
| 31 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.DEPT.CODE` | `FsGiFundDivDistCalcDetails_DeptCode` | String |  |  |
| 32 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.AUDITOR.CODE` | `FsGiFundDivDistCalcDetails_AuditorCode` | String |  |  |
| 33 | `FS.GI.FUND.DIV.DIST.CALC.DETAILS.AUDIT.DATE.TIME` | `FsGiFundDivDistCalcDetails_AuditDateTime` | String |  |  |
