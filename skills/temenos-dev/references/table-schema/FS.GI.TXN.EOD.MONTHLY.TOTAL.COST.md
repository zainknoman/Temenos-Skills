# FS.GI.TXN.EOD.MONTHLY.TOTAL.COST — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.EOD.MONTHLY.TOTAL.COST` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.FUND.ID` | `FsGiTxnEodMonthlyTotalCost_FundId` | TField |  | Fund ID for which montly total cost is calculated. Multifonds DB Column is NPTF. |
| 2 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.MONTH.YEAR` | `FsGiTxnEodMonthlyTotalCost_MonthYear` | TField |  | Month and year of the Total cost record in DD/YYYY format. Multifonds DB Column is DMONTH_END. |
| 3 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.SHARE.CLASS.CODE` | `FsGiTxnEodMonthlyTotalCost_ShareClassCode` | TField |  | Share class of the TA fund for which montly total cost is calculated. Multifonds DB Column is TPART. |
| 4 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.REGISTER.ID` | `FsGiTxnEodMonthlyTotalCost_RegisterId` | TField |  | Register ID for which the costs have been calculated. Multifonds DB Column is NREGISTER. |
| 5 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.FUND.MASTER.CCY` | `FsGiTxnEodMonthlyTotalCost_FundMasterCcy` | TField |  | TA Fund quotation currency. Multifonds DB Column is CMONREF. |
| 6 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.TOTAL.MONTHLY.COST` | `FsGiTxnEodMonthlyTotalCost_TotalMonthlyCost` | TField |  | Calculated Monthly total cost up to 2 decimals for the month and year, fund, share class and register. Multifonds DB Column is TOTAL_DLY_COST. |
| 7 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.TOTAL.OTHER.COST` | `FsGiTxnEodMonthlyTotalCost_TotalOtherCost` | TField |  | Calculated Monthly other fees upto 2 decimals at each month end, fund, share class and register. Multifonds DB Column is TOTAL_OTHER_COST. |
| 8 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.ACCRUED.TOTAL.COST` | `FsGiTxnEodMonthlyTotalCost_AccruedTotalCost` | TField |  | Calculated Accrued total cost upto 2 decimals at each month end, fund, share class and Register. Multifonds DB Column is REG_DLY_COST_ACCRUAL. |
| 9 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RESERVED10` | `FsGiTxnEodMonthlyTotalCost_Reserved10` | TField |  |  |
| 10 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RESERVED9` | `FsGiTxnEodMonthlyTotalCost_Reserved9` | TField |  |  |
| 11 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RESERVED8` | `FsGiTxnEodMonthlyTotalCost_Reserved8` | TField |  |  |
| 12 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RESERVED7` | `FsGiTxnEodMonthlyTotalCost_Reserved7` | TField |  |  |
| 13 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RESERVED6` | `FsGiTxnEodMonthlyTotalCost_Reserved6` | TField |  |  |
| 14 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RESERVED5` | `FsGiTxnEodMonthlyTotalCost_Reserved5` | TField |  |  |
| 15 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RESERVED4` | `FsGiTxnEodMonthlyTotalCost_Reserved4` | TField |  |  |
| 16 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RESERVED3` | `FsGiTxnEodMonthlyTotalCost_Reserved3` | TField |  |  |
| 17 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RESERVED2` | `FsGiTxnEodMonthlyTotalCost_Reserved2` | TField |  |  |
| 18 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RESERVED1` | `FsGiTxnEodMonthlyTotalCost_Reserved1` | TField |  |  |
| 19 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.LOCAL.REF` | `FsGiTxnEodMonthlyTotalCost_LocalRef` |  |  |  |
| 20 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.OVERRIDE` | `FsGiTxnEodMonthlyTotalCost_Override` |  |  |  |
| 21 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.RECORD.STATUS` | `FsGiTxnEodMonthlyTotalCost_RecordStatus` | String |  |  |
| 22 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.CURR.NO` | `FsGiTxnEodMonthlyTotalCost_CurrNo` | String |  |  |
| 23 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.INPUTTER` | `FsGiTxnEodMonthlyTotalCost_Inputter` |  |  |  |
| 24 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.DATE.TIME` | `FsGiTxnEodMonthlyTotalCost_DateTime` |  |  |  |
| 25 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.AUTHORISER` | `FsGiTxnEodMonthlyTotalCost_Authoriser` | String |  |  |
| 26 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.CO.CODE` | `FsGiTxnEodMonthlyTotalCost_CoCode` | String |  |  |
| 27 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.DEPT.CODE` | `FsGiTxnEodMonthlyTotalCost_DeptCode` | String |  |  |
| 28 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.AUDITOR.CODE` | `FsGiTxnEodMonthlyTotalCost_AuditorCode` | String |  |  |
| 29 | `FS.GI.TXN.EOD.MONTHLY.TOTAL.COST.AUDIT.DATE.TIME` | `FsGiTxnEodMonthlyTotalCost_AuditDateTime` | String |  |  |
