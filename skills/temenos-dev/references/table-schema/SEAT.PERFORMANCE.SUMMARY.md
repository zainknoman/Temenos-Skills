# SEAT.PERFORMANCE.SUMMARY — Table Schema

> Source: `INSERTS/I_F.SEAT.PERFORMANCE.SUMMARY` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.PS.SUMMARY.TYPE` | `SeatPerformanceSummary_SummaryType` |  |  |  |
| 2 | `SE.PS.RECORD.STATUS` | `SeatPerformanceSummary_RecordStatus` |  |  |  |
| 3 | `SE.PS.CURR.NO` | `SeatPerformanceSummary_CurrNo` |  |  |  |
| 4 | `SE.PS.INPUTTER` | `SeatPerformanceSummary_Inputter` |  |  |  |
| 5 | `SE.PS.DATE.TIME` | `SeatPerformanceSummary_DateTime` |  |  |  |
| 6 | `SE.PS.AUTHORISER` | `SeatPerformanceSummary_Authoriser` |  |  |  |
| 7 | `SE.PS.CO.CODE` | `SeatPerformanceSummary_CoCode` |  |  |  |
| 8 | `SE.PS.DEPT.CODE` | `SeatPerformanceSummary_DeptCode` |  |  |  |
| 9 | `SE.PS.AUDITOR.CODE` | `SeatPerformanceSummary_AuditorCode` |  |  |  |
| 10 | `SE.PS.AUDIT.DATE.TIME` | `SeatPerformanceSummary_AuditDateTime` |  |  |  |
