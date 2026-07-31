# FS.GI.FUND.PERFORMANCE.FEE.PARAM — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.PERFORMANCE.FEE.PARAM` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.PARENT.REF.ID` | `FsGiFundPerformanceFeeParam_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.ORA.ROWID` | `FsGiFundPerformanceFeeParam_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.FUND.ID` | `FsGiFundPerformanceFeeParam_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.SHARE.CLASS.CODE` | `FsGiFundPerformanceFeeParam_ShareClassCode` | TField |  | Fund share class for which performance fee parameterisation applies. Multifonds DB Column is TPART. |
| 5 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.PERFORMANCE.FEE.CODE` | `FsGiFundPerformanceFeeParam_PerformanceFeeCode` | TField |  | Performance fee method. Multifonds DB Column is CPERFOR_FEE. |
| 6 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.HWM.APPLICABLE.FLAG` | `FsGiFundPerformanceFeeParam_HwmApplicableFlag` | TField |  | Flag allows to enable HWM (High Water Mark) for performance fee calculation. Multifonds DB Column is FLG_HWM_APPLICABLE. |
| 7 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.HWM.PRINCIPLE` | `FsGiFundPerformanceFeeParam_HwmPrinciple` | TField |  | It specifies the principle to reset the HWM. Multifonds DB Column is HWM_PRIN. |
| 8 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.HWM.PERIOD.IN.MONTHS` | `FsGiFundPerformanceFeeParam_HwmPeriodInMonths` | TField |  | It specifies the observation period for the HWM reset in months. Multifonds DB Column is HWM_PERIOD. |
| 9 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RATE.TYPE` | `FsGiFundPerformanceFeeParam_RateType` | TField |  | Rate type code to calculate the performance fee. Multifonds DB Column is PF_RATE_TYPE. |
| 10 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.PF.PERCENTAGE` | `FsGiFundPerformanceFeeParam_PfPercentage` | TField | Yes | Performance fee rate in percentage. The field is mandatory if &apos;Rate type&apos; is set as &apos;0001&apos;(Rate); otherwise its not updatable. Multifonds DB Column is PCT_PERFOR. |
| 11 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.SCALE.CODE` | `FsGiFundPerformanceFeeParam_ScaleCode` | TField | Yes | The performance fee scale code type.The field is mandatory if &apos;Rate type&apos; is set as &apos;0002&apos;(Scale); otherwise the field is not updatable. Multifonds DB Column is SCALE_CODE. |
| 12 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.DP.FOR.CRP.PF.ACCRUAL` | `FsGiFundPerformanceFeeParam_DpForCrpPfAccrual` | TField |  | Decimal places for CRP/PF accrual. Multifonds DB Column is DEC_CRP_PF. |
| 13 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.DP.FOR.REFERENCE.NAV` | `FsGiFundPerformanceFeeParam_DpForReferenceNav` | TField |  | Decimal places for Reference NAV (HAHWM). Multifonds DB Column is DEC_REF_NAV. |
| 14 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.DP.FOR.GROSS.NAV` | `FsGiFundPerformanceFeeParam_DpForGrossNav` | TField |  | Decimal places for Gross NAV. Multifonds DB Column is DEC_GROSS_NAV. |
| 15 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.REFERENCE.NAV.NET.DIV.FLAG` | `FsGiFundPerformanceFeeParam_ReferenceNavNetDivFlag` | TField |  | Flag to apply the refernece nav decimial setup to the HWM net dividend and HAHWM net dividend price Multifonds DB Column is FLG_NET_DIVIDEND. |
| 16 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.HURDLE.APPLICABLE.FLAG` | `FsGiFundPerformanceFeeParam_HurdleApplicableFlag` | TField |  | Flag to enable hurdle for performance fee calculation. Multifonds DB Column is FLG_HURDLE_APPLICABLE. |
| 17 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.HURDLE.TYPE` | `FsGiFundPerformanceFeeParam_HurdleType` | TField |  | Type of hurdle for performance fee calculation. Multifonds DB Column is HURDLE_TYPE. |
| 18 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.HURDLE.METHOD` | `FsGiFundPerformanceFeeParam_HurdleMethod` | TField |  | Hurdle rate method. Multifonds DB Column is HURDLE_METHOD. |
| 19 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.HURDLE.RATE` | `FsGiFundPerformanceFeeParam_HurdleRate` | TField |  | Hurdle rate in percentage. Multifonds DB Column is HURDLE_RATE. |
| 20 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.CATCH.UP.PERCENTAGE` | `FsGiFundPerformanceFeeParam_CatchUpPercentage` | TField |  | Catch up percentage. Multifonds DB Column is PCT_CATCH_UP. |
| 21 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.DAY.COUNT.METHOD` | `FsGiFundPerformanceFeeParam_DayCountMethod` | TField |  | Method used for days count. For example: &apos;0001&apos;(ACT/ACT), &apos;0005&apos;(ACT/denominator), &apos;0007&apos;(BD/denominator). Multifonds DB Column is DC_METHOD. |
| 22 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.DENOMINATOR` | `FsGiFundPerformanceFeeParam_Denominator` | TField |  | Denominator for the number of days. Multifonds DB Column is DENOMIN. |
| 23 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.HURDLE.RATE.TYPE` | `FsGiFundPerformanceFeeParam_HurdleRateType` | TField |  | Hurdle rate method. Multifonds DB Column is HURDLE_RATE_TYPE. |
| 24 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.COMPOUNDING.BASIS` | `FsGiFundPerformanceFeeParam_CompoundingBasis` | TField |  | It specifies the basis for compounding. Multifonds DB Column is COMPOUND_BASIS. |
| 25 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESET.HURDLE` | `FsGiFundPerformanceFeeParam_ResetHurdle` | TField |  | The method to reset the hurdle. Multifonds DB Column is RESET_HURDLE. |
| 26 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.BENCHMARK.TYPE` | `FsGiFundPerformanceFeeParam_BenchmarkType` | TField |  | Benchmark type code. Multifonds DB Column is BMK_TYPE. |
| 27 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.BENCHMARK.SECURITY.ID` | `FsGiFundPerformanceFeeParam_BenchmarkSecurityId` | TField |  | Benchmark Security ID. Multifonds DB Column is NOVAL_BENCH. |
| 28 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.HURDLE.RATE.ON.TOP.OF.BMK` | `FsGiFundPerformanceFeeParam_HurdleRateOnTopOfBmk` | TField |  | Additional rate for hurdle. The value can be negative or positive. Multifonds DB Column is HURDLE_RATE_ON_BMK. |
| 29 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.HURDLE.RATE.ON.BMK.TYPE` | `FsGiFundPerformanceFeeParam_HurdleRateOnBmkType` | TField |  | It specifies if the Hurdle rate on top of the benchmark is to be considered as a percent value or a percentage to be added to the benchmark. Multifonds DB Column is HURDLE_ON_BMK_TYPE. |
| 30 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.OBSERVATION.PERIOD` | `FsGiFundPerformanceFeeParam_ObservationPeriod` | TField |  | The observation period for the hurdle. Multifonds DB Column is OBSER_PERIOD. |
| 31 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.OBSERVATION.CALENDAR` | `FsGiFundPerformanceFeeParam_ObservationCalendar` | TField |  | Benchmark security observation Calendar. Multifonds DB Column is OBSER_CALENDAR. |
| 32 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.OBS.DATE.FOR.INCEPTION` | `FsGiFundPerformanceFeeParam_ObsDateForInception` | TField |  | Observation date for inception. Multifonds DB Column is OBSER_INCEP_DATE. |
| 33 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.OBS.NEXT.THEORETICAL.DATE` | `FsGiFundPerformanceFeeParam_ObsNextTheoreticalDate` | TField |  | Next theoretical observation date. The field is automatically populated by the system based on the observation period and the observation date. Multifonds DB Column is OBSER_NTOD. |
| 34 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.OBSERVATION.DATE.TYPE` | `FsGiFundPerformanceFeeParam_ObservationDateType` | TField |  | Observation date type. Multifonds DB Column is OBSER_DATE_TYPE. |
| 35 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.OBSERVATION.START.DATE` | `FsGiFundPerformanceFeeParam_ObservationStartDate` | TField | Yes | The observation start date. It is mandatory if the field &apos;Observation period&apos; is setup. Multifonds DB Column is OBSER_START. |
| 36 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.OBSERVATION.DATE.TO.BE.USED` | `FsGiFundPerformanceFeeParam_ObservationDateToBeUsed` | TField |  | Observation date to ne used. Multifonds DB Column is OBSER_DATE_USED. |
| 37 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.OBSERVATION.SYSTEM.DATE` | `FsGiFundPerformanceFeeParam_ObservationSystemDate` | TField |  | Observation system date. Multifonds DB Column is OBSER_NTOD_SYS. |
| 38 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.PF.CALCULATION.STATUS` | `FsGiFundPerformanceFeeParam_PfCalculationStatus` | TField |  | Performance fee calculation status. Multifonds DB Column is PF_CALC_STATUS. |
| 39 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.PF.PARAM.INTERNAL.ID` | `FsGiFundPerformanceFeeParam_PfParamInternalId` | TField |  | Unique internal identifier supplied as a reference to external processes creating new details in the table. Multifonds DB Column is INTERNAL_ID. |
| 40 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESERVED10` | `FsGiFundPerformanceFeeParam_Reserved10` | TField |  |  |
| 41 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESERVED9` | `FsGiFundPerformanceFeeParam_Reserved9` | TField |  |  |
| 42 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESERVED8` | `FsGiFundPerformanceFeeParam_Reserved8` | TField |  |  |
| 43 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESERVED7` | `FsGiFundPerformanceFeeParam_Reserved7` | TField |  |  |
| 44 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESERVED6` | `FsGiFundPerformanceFeeParam_Reserved6` | TField |  |  |
| 45 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESERVED5` | `FsGiFundPerformanceFeeParam_Reserved5` | TField |  |  |
| 46 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESERVED4` | `FsGiFundPerformanceFeeParam_Reserved4` | TField |  |  |
| 47 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESERVED3` | `FsGiFundPerformanceFeeParam_Reserved3` | TField |  |  |
| 48 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESERVED2` | `FsGiFundPerformanceFeeParam_Reserved2` | TField |  |  |
| 49 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RESERVED1` | `FsGiFundPerformanceFeeParam_Reserved1` | TField |  |  |
| 50 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.LOCAL.REF` | `FsGiFundPerformanceFeeParam_LocalRef` |  |  |  |
| 51 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.OVERRIDE` | `FsGiFundPerformanceFeeParam_Override` |  |  |  |
| 52 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.RECORD.STATUS` | `FsGiFundPerformanceFeeParam_RecordStatus` | String |  |  |
| 53 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.CURR.NO` | `FsGiFundPerformanceFeeParam_CurrNo` | String |  |  |
| 54 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.INPUTTER` | `FsGiFundPerformanceFeeParam_Inputter` |  |  |  |
| 55 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.DATE.TIME` | `FsGiFundPerformanceFeeParam_DateTime` |  |  |  |
| 56 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.AUTHORISER` | `FsGiFundPerformanceFeeParam_Authoriser` | String |  |  |
| 57 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.CO.CODE` | `FsGiFundPerformanceFeeParam_CoCode` | String |  |  |
| 58 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.DEPT.CODE` | `FsGiFundPerformanceFeeParam_DeptCode` | String |  |  |
| 59 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.AUDITOR.CODE` | `FsGiFundPerformanceFeeParam_AuditorCode` | String |  |  |
| 60 | `FS.GI.FUND.PERFORMANCE.FEE.PARAM.AUDIT.DATE.TIME` | `FsGiFundPerformanceFeeParam_AuditDateTime` | String |  |  |
