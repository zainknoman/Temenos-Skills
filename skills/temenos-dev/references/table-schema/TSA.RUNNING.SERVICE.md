# TSA.RUNNING.SERVICE — Table Schema

> Source: `INSERTS/I_F.TSA.RUNNING.SERVICE` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TSA.RS.TOTAL.AGENT` | `TsaRunningService_TotalAgent` | TField |  |  |
| 2 | `TSA.RS.RUNNING.AGENT` | `TsaRunningService_RunningAgent` | TField |  |  |
| 3 | `TSA.RS.MAX.AGENT` | `TsaRunningService_MaxAgent` | TField |  |  |
| 4 | `TSA.RS.MIN.AGENT` | `TsaRunningService_MinAgent` | TField |  |  |
| 5 | `TSA.RS.LAST.DATE.TIME` | `TsaRunningService_LastDateTime` |  |  |  |
| 6 | `TSA.RS.CURRENT.QUEUE.DEPTH` | `TsaRunningService_CurrentQueueDepth` |  |  |  |
| 7 | `TSA.RS.CURRENT.JOB` | `TsaRunningService_CurrentJob` |  |  |  |
| 8 | `TSA.RS.RUNNING.AGENT.IDS` | `TsaRunningService_RunningAgentIds` |  |  |  |
| 9 | `TSA.RS.ACTIVE.SERVERS` | `TsaRunningService_ActiveServers` |  |  |  |
| 10 | `TSA.RS.RESERVED.5` | `TsaRunningService_Reserved5` | TField |  |  |
| 11 | `TSA.RS.RESERVED.4` | `TsaRunningService_Reserved4` | TField |  |  |
| 12 | `TSA.RS.RESERVED.3` | `TsaRunningService_Reserved3` | TField |  |  |
| 13 | `TSA.RS.RESERVED.2` | `TsaRunningService_Reserved2` | TField |  |  |
| 14 | `TSA.RS.RESERVED.1` | `TsaRunningService_Reserved1` | TField |  |  |
