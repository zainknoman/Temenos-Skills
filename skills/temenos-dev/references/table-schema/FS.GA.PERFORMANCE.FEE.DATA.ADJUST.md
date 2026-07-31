# FS.GA.PERFORMANCE.FEE.DATA.ADJUST — Table Schema

> Source: `INSERTS/I_F.FS.GA.PERFORMANCE.FEE.DATA.ADJUST` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.FUND.ID` | `FsGaPerformanceFeeDataAdjust_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.DATE.OF.NAV` | `FsGaPerformanceFeeDataAdjust_DateOfNav` | TField |  | Date of the NAV Multifonds DB Column is DATE_NAV. |
| 3 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.SHARE.CLASS.CODE` | `FsGaPerformanceFeeDataAdjust_ShareClassCode` | TField |  | Share class code Multifonds DB Column is TPART. |
| 4 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.CUMUL.DIV.ADJT.ON.NAV` | `FsGaPerformanceFeeDataAdjust_CumulDivAdjtOnNav` | TField |  | Cumulative dividend adjustment on Net asset value (NAV) Multifonds DB Column is CUM_DIV_PER_SHARE_ADJ. |
| 5 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.SUBSCRIPTION.ADJUSTMENT` | `FsGaPerformanceFeeDataAdjust_SubscriptionAdjustment` | TField |  | Subscription amount adjustment for performance fee Multifonds DB Column is SUBS_ADJ. |
| 6 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.REDEMPTION.ADJUSTMENT` | `FsGaPerformanceFeeDataAdjust_RedemptionAdjustment` | TField |  | Redemption amount adjustment for performance fee Multifonds DB Column is REDS_ADJ. |
| 7 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.HURDLE` | `FsGaPerformanceFeeDataAdjust_Hurdle` | TField |  | Hurdle amount adjustment for performance fee Multifonds DB Column is HURDLE_ADJ_HWM_ADJ. |
| 8 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.CUML.DIV.LAST.RESET.FOR.HURDLE` | `FsGaPerformanceFeeDataAdjust_CumlDivLastResetForHurdle` | TField |  | Cumulative dividend since last reset for hurdle Multifonds DB Column is CUM_DIV_HUR_ADJ. |
| 9 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.CUMULATIVE.DIV.ADJT.FOR.HURDLE` | `FsGaPerformanceFeeDataAdjust_CumulativeDivAdjtForHurdle` | TField |  | Cumulative dividend adjustment for hurdle Multifonds DB Column is CUM_DIV_ADJ_HUR_ADJ. |
| 10 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.TOTAL.HWM` | `FsGaPerformanceFeeDataAdjust_TotalHwm` | TField |  | Total high water mark (HWM) basis for adjustment Multifonds DB Column is HWM_BASIS_ADJ. |
| 11 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.CUMUL.DIV.LAST.RESET.FOR.HWM` | `FsGaPerformanceFeeDataAdjust_CumulDivLastResetForHwm` | TField |  | Cumulative dividend since last reset for high water mark (HWM) Multifonds DB Column is CUM_DIV_HWM_ADJ. |
| 12 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.CUMULATIVE.DIV.ADJT.FOR.HWM` | `FsGaPerformanceFeeDataAdjust_CumulativeDivAdjtForHwm` | TField |  | Cumulative dividend adjustment for high water mark (HWM) Multifonds DB Column is CUM_DIV_ADJ_HWM_ADJ. |
| 13 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.CAPPING.AMOUNT` | `FsGaPerformanceFeeDataAdjust_CappingAmount` | TField |  | Maximum amount of adjustment Multifonds DB Column is MAX_AMOUNT_ADJ. |
| 14 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.FINAL.PERFORMANCE.FEES.ADJT` | `FsGaPerformanceFeeDataAdjust_FinalPerformanceFeesAdjt` | TField |  | Final performance fees adjustment Multifonds DB Column is PF_ACCRUAL_ADJ. |
| 15 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.FINAL.CUMULATIVE.ADJUSTMENT` | `FsGaPerformanceFeeDataAdjust_FinalCumulativeAdjustment` | TField |  | Final cumulative adjustment Multifonds DB Column is FINAL_CUMUL_ADJ. |
| 16 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.REMARKS` | `FsGaPerformanceFeeDataAdjust_Remarks` | TField |  | To include remarks/add file under free text field Multifonds DB Column is FREE_TEXT. |
| 17 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.CRYSTALLISATION` | `FsGaPerformanceFeeDataAdjust_Crystallisation` | TField |  | Crystallisation amount for performance fee Multifonds DB Column is CRYSTALLISATION. |
| 18 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.CUMULATIVE.SHARE.TOTAL` | `FsGaPerformanceFeeDataAdjust_CumulativeShareTotal` | TField |  | Cumulative Share Total Multifonds DB Column is CUM_SHARE_TOT. |
| 19 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.PERIOD.END.NAV.PRICE` | `FsGaPerformanceFeeDataAdjust_PeriodEndNavPrice` | TField |  | Period End NAV Price Multifonds DB Column is PERIOD_END_PRICE. |
| 20 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.OPENING.BENCHMARK.VALUE` | `FsGaPerformanceFeeDataAdjust_OpeningBenchmarkValue` | TField |  | Opening Benchmark Value Multifonds DB Column is OPEN_BMK. |
| 21 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RESERVED10` | `FsGaPerformanceFeeDataAdjust_Reserved10` | TField |  |  |
| 22 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RESERVED9` | `FsGaPerformanceFeeDataAdjust_Reserved9` | TField |  |  |
| 23 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RESERVED8` | `FsGaPerformanceFeeDataAdjust_Reserved8` | TField |  |  |
| 24 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RESERVED7` | `FsGaPerformanceFeeDataAdjust_Reserved7` | TField |  |  |
| 25 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RESERVED6` | `FsGaPerformanceFeeDataAdjust_Reserved6` | TField |  |  |
| 26 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RESERVED5` | `FsGaPerformanceFeeDataAdjust_Reserved5` | TField |  |  |
| 27 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RESERVED4` | `FsGaPerformanceFeeDataAdjust_Reserved4` | TField |  |  |
| 28 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RESERVED3` | `FsGaPerformanceFeeDataAdjust_Reserved3` | TField |  |  |
| 29 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RESERVED2` | `FsGaPerformanceFeeDataAdjust_Reserved2` | TField |  |  |
| 30 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RESERVED1` | `FsGaPerformanceFeeDataAdjust_Reserved1` | TField |  |  |
| 31 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.RECORD.STATUS` | `FsGaPerformanceFeeDataAdjust_RecordStatus` | String |  |  |
| 32 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.CURR.NO` | `FsGaPerformanceFeeDataAdjust_CurrNo` | String |  |  |
| 33 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.INPUTTER` | `FsGaPerformanceFeeDataAdjust_Inputter` |  |  |  |
| 34 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.DATE.TIME` | `FsGaPerformanceFeeDataAdjust_DateTime` |  |  |  |
| 35 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.AUTHORISER` | `FsGaPerformanceFeeDataAdjust_Authoriser` | String |  |  |
| 36 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.CO.CODE` | `FsGaPerformanceFeeDataAdjust_CoCode` | String |  |  |
| 37 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.DEPT.CODE` | `FsGaPerformanceFeeDataAdjust_DeptCode` | String |  |  |
| 38 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.AUDITOR.CODE` | `FsGaPerformanceFeeDataAdjust_AuditorCode` | String |  |  |
| 39 | `FS.GA.PERFORMANCE.FEE.DATA.ADJUST.AUDIT.DATE.TIME` | `FsGaPerformanceFeeDataAdjust_AuditDateTime` | String |  |  |
