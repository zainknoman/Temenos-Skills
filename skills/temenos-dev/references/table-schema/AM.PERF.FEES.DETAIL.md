# AM.PERF.FEES.DETAIL — Table Schema

> Source: `INSERTS/I_F.AM.PERF.FEES.DETAIL` in `AM_PerformanceFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.PFD.DATE` | `AmPerfFeesDetail_Date` |  |  |  |
| 2 | `AM.PFD.BENCHMARK` | `AmPerfFeesDetail_Benchmark` |  |  |  |
| 3 | `AM.PFD.PORT.PERF` | `AmPerfFeesDetail_PortPerf` |  |  |  |
| 4 | `AM.PFD.BENCH.PERF` | `AmPerfFeesDetail_BenchPerf` |  |  |  |
| 5 | `AM.PFD.CCY.PERF` | `AmPerfFeesDetail_CcyPerf` |  |  |  |
| 6 | `AM.PFD.EXCESS.RETURNS` | `AmPerfFeesDetail_ExcessReturns` |  |  |  |
| 7 | `AM.PFD.RATE` | `AmPerfFeesDetail_Rate` |  |  |  |
| 8 | `AM.PFD.MARKET.VALUE` | `AmPerfFeesDetail_MarketValue` |  |  |  |
| 9 | `AM.PFD.PERF.FEES` | `AmPerfFeesDetail_PerfFees` |  |  |  |
| 10 | `AM.PFD.RESERVED.5` | `AmPerfFeesDetail_Reserved5` |  |  |  |
| 11 | `AM.PFD.RESERVED.4` | `AmPerfFeesDetail_Reserved4` |  |  |  |
| 12 | `AM.PFD.RESERVED.3` | `AmPerfFeesDetail_Reserved3` |  |  |  |
| 13 | `AM.PFD.RESERVED.2` | `AmPerfFeesDetail_Reserved2` |  |  |  |
| 14 | `AM.PFD.RESERVED.1` | `AmPerfFeesDetail_Reserved1` |  |  |  |
| 15 | `AM.PFD.RECORD.STATUS` | `AmPerfFeesDetail_RecordStatus` | String |  |  |
| 16 | `AM.PFD.CURR.NO` | `AmPerfFeesDetail_CurrNo` | String |  |  |
| 17 | `AM.PFD.INPUTTER` | `AmPerfFeesDetail_Inputter` |  |  |  |
| 18 | `AM.PFD.DATE.TIME` | `AmPerfFeesDetail_DateTime` |  |  |  |
| 19 | `AM.PFD.AUTHORISER` | `AmPerfFeesDetail_Authoriser` | String |  |  |
| 20 | `AM.PFD.CO.CODE` | `AmPerfFeesDetail_CoCode` | String |  |  |
| 21 | `AM.PFD.DEPT.CODE` | `AmPerfFeesDetail_DeptCode` | String |  |  |
| 22 | `AM.PFD.AUDITOR.CODE` | `AmPerfFeesDetail_AuditorCode` | String |  |  |
| 23 | `AM.PFD.AUDIT.DATE.TIME` | `AmPerfFeesDetail_AuditDateTime` | String |  |  |
