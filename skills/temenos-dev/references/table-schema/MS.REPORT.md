# MS.REPORT — Table Schema

> Source: `INSERTS/I_F.MS.REPORT` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MS.REP.FROM.CHECK.POINT` | `MsReport_FromCheckPoint` |  |  |  |
| 2 | `MS.REP.TO.CHECK.POINT` | `MsReport_ToCheckPoint` |  |  |  |
| 3 | `MS.REP.FROM.CP.TIMESTAMP` | `MsReport_FromCpTimestamp` |  |  |  |
| 4 | `MS.REP.TO.CP.TIMESTAMP` | `MsReport_ToCpTimestamp` |  |  |  |
| 5 | `MS.REP.SERVER.NAME` | `MsReport_ServerName` |  |  |  |
| 6 | `MS.REP.AGENTS` | `MsReport_Agents` |  |  |  |
| 7 | `MS.REP.RECORDS.PER.SERVER` | `MsReport_RecordsPerServer` |  |  |  |
| 8 | `MS.REP.THROUGHPUT.PER.SERVER` | `MsReport_ThroughputPerServer` |  |  |  |
| 9 | `MS.REP.TIME.ELAPSED.IN.SECS` | `MsReport_TimeElapsedInSecs` |  |  |  |
| 10 | `MS.REP.TOTAL.RECORDS` | `MsReport_TotalRecords` |  |  |  |
| 11 | `MS.REP.SYSTEM.THROUGHPUT` | `MsReport_SystemThroughput` |  |  |  |
| 12 | `MS.REP.RESERVED.09` | `MsReport_Reserved09` | TField |  |  |
| 13 | `MS.REP.RESERVED.08` | `MsReport_Reserved08` | TField |  |  |
| 14 | `MS.REP.RESERVED.07` | `MsReport_Reserved07` | TField |  |  |
| 15 | `MS.REP.RESERVED.06` | `MsReport_Reserved06` | TField |  |  |
| 16 | `MS.REP.RESERVED.05` | `MsReport_Reserved05` | TField |  |  |
| 17 | `MS.REP.RESERVED.04` | `MsReport_Reserved04` | TField |  |  |
| 18 | `MS.REP.RESERVED.03` | `MsReport_Reserved03` | TField |  |  |
| 19 | `MS.REP.RESERVED.02` | `MsReport_Reserved02` | TField |  |  |
| 20 | `MS.REP.RESERVED.01` | `MsReport_Reserved01` | TField |  |  |
