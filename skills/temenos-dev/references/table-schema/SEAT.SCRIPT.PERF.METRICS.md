# SEAT.SCRIPT.PERF.METRICS — Table Schema

> Source: `INSERTS/I_F.SEAT.SCRIPT.PERF.METRICS` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.PERF.TOTAL.READ.EXPECTED` | `SeatScriptPerfMetrics_TotalReadExpected` |  |  |  |
| 2 | `SE.PERF.TOTAL.READ.ACTUAL` | `SeatScriptPerfMetrics_TotalReadActual` |  |  |  |
| 3 | `SE.PERF.TOTAL.WRITE.EXPECTED` | `SeatScriptPerfMetrics_TotalWriteExpected` |  |  |  |
| 4 | `SE.PERF.TOTAL.WRITE.ACTUAL` | `SeatScriptPerfMetrics_TotalWriteActual` |  |  |  |
| 5 | `SE.PERF.TOTAL.DELETE.EXPECTED` | `SeatScriptPerfMetrics_TotalDeleteExpected` |  |  |  |
| 6 | `SE.PERF.TOTAL.DELETE.ACTUAL` | `SeatScriptPerfMetrics_TotalDeleteActual` |  |  |  |
| 7 | `SE.PERF.TOTAL.LOCKS.EXPECTED` | `SeatScriptPerfMetrics_TotalLocksExpected` |  |  |  |
| 8 | `SE.PERF.TOTAL.LOCKS.ACTUAL` | `SeatScriptPerfMetrics_TotalLocksActual` |  |  |  |
| 9 | `SE.PERF.TOTAL.EXECUTE.EXPECTED` | `SeatScriptPerfMetrics_TotalExecuteExpected` |  |  |  |
| 10 | `SE.PERF.TOTAL.EXECUTE.ACTUAL` | `SeatScriptPerfMetrics_TotalExecuteActual` |  |  |  |
| 11 | `SE.PERF.TOTAL.CACHE.READ.EXPECTED` | `SeatScriptPerfMetrics_TotalCacheReadExpected` |  |  |  |
| 12 | `SE.PERF.TOTAL.CACHE.READ.ACTUAL` | `SeatScriptPerfMetrics_TotalCacheReadActual` |  |  |  |
| 13 | `SE.PERF.TOTAL.PATHLENGTH.EXPECTED` | `SeatScriptPerfMetrics_TotalPathlengthExpected` |  |  |  |
| 14 | `SE.PERF.TOTAL.PATHLENGTH.ACTUAL` | `SeatScriptPerfMetrics_TotalPathlengthActual` |  |  |  |
| 15 | `SE.PERF.TOTAL.MESSAGES.EXPECTED` | `SeatScriptPerfMetrics_TotalMessagesExpected` |  |  |  |
| 16 | `SE.PERF.TOTAL.MESSAGES.ACTUAL` | `SeatScriptPerfMetrics_TotalMessagesActual` |  |  |  |
| 17 | `SE.PERF.RESERVED.4` | `SeatScriptPerfMetrics_Reserved4` |  |  |  |
| 18 | `SE.PERF.RESERVED.3` | `SeatScriptPerfMetrics_Reserved3` | TField |  |  |
| 19 | `SE.PERF.RESERVED.2` | `SeatScriptPerfMetrics_Reserved2` | TField |  |  |
| 20 | `SE.PERF.RESERVED.1` | `SeatScriptPerfMetrics_Reserved1` | TField |  |  |
| 21 | `SE.PERF.RECORD.STATUS` | `SeatScriptPerfMetrics_RecordStatus` | String |  |  |
| 22 | `SE.PERF.CURR.NO` | `SeatScriptPerfMetrics_CurrNo` | String |  |  |
| 23 | `SE.PERF.INPUTTER` | `SeatScriptPerfMetrics_Inputter` |  |  |  |
| 24 | `SE.PERF.DATE.TIME` | `SeatScriptPerfMetrics_DateTime` |  |  |  |
| 25 | `SE.PERF.AUTHORISER` | `SeatScriptPerfMetrics_Authoriser` | String |  |  |
| 26 | `SE.PERF.CO.CODE` | `SeatScriptPerfMetrics_CoCode` | String |  |  |
| 27 | `SE.PERF.DEPT.CODE` | `SeatScriptPerfMetrics_DeptCode` | String |  |  |
| 28 | `SE.PERF.AUDITOR.CODE` | `SeatScriptPerfMetrics_AuditorCode` | String |  |  |
| 29 | `SE.PERF.AUDIT.DATE.TIME` | `SeatScriptPerfMetrics_AuditDateTime` | String |  |  |
