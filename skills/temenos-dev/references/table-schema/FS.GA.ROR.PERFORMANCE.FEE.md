# FS.GA.ROR.PERFORMANCE.FEE — Table Schema

> Source: `INSERTS/I_F.FS.GA.ROR.PERFORMANCE.FEE` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ROR.PERFORMANCE.FEE.ROR.ID` | `FsGaRorPerformanceFee_RorId` | TField |  | ROR ID Multifonds DB Column is RORID. |
| 2 | `FS.GA.ROR.PERFORMANCE.FEE.ROR.CODE` | `FsGaRorPerformanceFee_RorCode` | TField |  | ROR code is required for user to define the ROR and management fee rate parameter Multifonds DB Column is CROR. |
| 3 | `FS.GA.ROR.PERFORMANCE.FEE.INTERNAL.SECURITY.ID` | `FsGaRorPerformanceFee_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 4 | `FS.GA.ROR.PERFORMANCE.FEE.ROR.METHOD` | `FsGaRorPerformanceFee_RorMethod` | TField |  | Rate of Return (ROR) Method Multifonds DB Column is RMETHODE. |
| 5 | `FS.GA.ROR.PERFORMANCE.FEE.FUND.STOCK.ID` | `FsGaRorPerformanceFee_FundStockId` | TField |  | Fund Stock ID Multifonds DB Column is FUND_STOCKID. |
| 6 | `FS.GA.ROR.PERFORMANCE.FEE.GREATER.THAN` | `FsGaRorPerformanceFee_GreaterThan` | TField |  | ROR Fund vs User ">" (larger than) Multifonds DB Column is FUND_USER_GR. |
| 7 | `FS.GA.ROR.PERFORMANCE.FEE.LESS.THAN.OR.EQUAL.TO` | `FsGaRorPerformanceFee_LessThanOrEqualTo` | TField |  | ROR Fund vs Use less than or equal Multifonds DB Column is FUND_USER_LS. |
| 8 | `FS.GA.ROR.PERFORMANCE.FEE.GREATER.THAN.OR.EQUAL.TO` | `FsGaRorPerformanceFee_GreaterThanOrEqualTo` | TField |  | Fund vs Accumulated Targeted ROR ">" (larger than) Multifonds DB Column is FUND_ACC_TROR_GR. |
| 9 | `FS.GA.ROR.PERFORMANCE.FEE.LESS.THAN` | `FsGaRorPerformanceFee_LessThan` | TField |  | Fund vs Accumulated Targeted ROR and less than or equal Multifonds DB Column is FUND_ACC_TROR_LS. |
| 10 | `FS.GA.ROR.PERFORMANCE.FEE.FEE.RATE` | `FsGaRorPerformanceFee_FeeRate` | TField |  | Fee Rate Multifonds DB Column is FEE_RATE. |
| 11 | `FS.GA.ROR.PERFORMANCE.FEE.RESERVED10` | `FsGaRorPerformanceFee_Reserved10` | TField |  |  |
| 12 | `FS.GA.ROR.PERFORMANCE.FEE.RESERVED9` | `FsGaRorPerformanceFee_Reserved9` | TField |  |  |
| 13 | `FS.GA.ROR.PERFORMANCE.FEE.RESERVED8` | `FsGaRorPerformanceFee_Reserved8` | TField |  |  |
| 14 | `FS.GA.ROR.PERFORMANCE.FEE.RESERVED7` | `FsGaRorPerformanceFee_Reserved7` | TField |  |  |
| 15 | `FS.GA.ROR.PERFORMANCE.FEE.RESERVED6` | `FsGaRorPerformanceFee_Reserved6` | TField |  |  |
| 16 | `FS.GA.ROR.PERFORMANCE.FEE.RESERVED5` | `FsGaRorPerformanceFee_Reserved5` | TField |  |  |
| 17 | `FS.GA.ROR.PERFORMANCE.FEE.RESERVED4` | `FsGaRorPerformanceFee_Reserved4` | TField |  |  |
| 18 | `FS.GA.ROR.PERFORMANCE.FEE.RESERVED3` | `FsGaRorPerformanceFee_Reserved3` | TField |  |  |
| 19 | `FS.GA.ROR.PERFORMANCE.FEE.RESERVED2` | `FsGaRorPerformanceFee_Reserved2` | TField |  |  |
| 20 | `FS.GA.ROR.PERFORMANCE.FEE.RESERVED1` | `FsGaRorPerformanceFee_Reserved1` | TField |  |  |
| 21 | `FS.GA.ROR.PERFORMANCE.FEE.RECORD.STATUS` | `FsGaRorPerformanceFee_RecordStatus` | String |  |  |
| 22 | `FS.GA.ROR.PERFORMANCE.FEE.CURR.NO` | `FsGaRorPerformanceFee_CurrNo` | String |  |  |
| 23 | `FS.GA.ROR.PERFORMANCE.FEE.INPUTTER` | `FsGaRorPerformanceFee_Inputter` |  |  |  |
| 24 | `FS.GA.ROR.PERFORMANCE.FEE.DATE.TIME` | `FsGaRorPerformanceFee_DateTime` |  |  |  |
| 25 | `FS.GA.ROR.PERFORMANCE.FEE.AUTHORISER` | `FsGaRorPerformanceFee_Authoriser` | String |  |  |
| 26 | `FS.GA.ROR.PERFORMANCE.FEE.CO.CODE` | `FsGaRorPerformanceFee_CoCode` | String |  |  |
| 27 | `FS.GA.ROR.PERFORMANCE.FEE.DEPT.CODE` | `FsGaRorPerformanceFee_DeptCode` | String |  |  |
| 28 | `FS.GA.ROR.PERFORMANCE.FEE.AUDITOR.CODE` | `FsGaRorPerformanceFee_AuditorCode` | String |  |  |
| 29 | `FS.GA.ROR.PERFORMANCE.FEE.AUDIT.DATE.TIME` | `FsGaRorPerformanceFee_AuditDateTime` | String |  |  |
