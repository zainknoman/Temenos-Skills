# SY.EVENT.ERRORS — Table Schema

> Source: `INSERTS/I_F.SY.EVENT.ERRORS` in `SY_Event.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.EE.EVENT.ID` | `SyEventErrors_EventId` | TField |  | The event that has failed. |
| 2 | `SY.EE.EVENT.DEFINITION` | `SyEventErrors_EventDefinition` | TField |  | The event definition key for this event. |
| 3 | `SY.EE.TRANSACTION` | `SyEventErrors_Transaction` | TField |  | The transaction key for this event. |
| 4 | `SY.EE.COB.PHASE` | `SyEventErrors_CobPhase` | TField |  | The COB phase in which this event failed. |
| 5 | `SY.EE.LAST.RUN.DATE` | `SyEventErrors_LastRunDate` | TField |  | The last time this event ran successfully. |
| 6 | `SY.EE.SYSTEM.DATE` | `SyEventErrors_SystemDate` | TField |  | The system (T24) date at the time the error was generated. Note that this may not be the same as DATE. |
| 7 | `SY.EE.AGENT` | `SyEventErrors_Agent` | TField |  | The agent number which was processing this event. |
| 8 | `SY.EE.COMO` | `SyEventErrors_Como` | TField |  | The key to the output (COMO) file generated for this agent and job. |
| 9 | `SY.EE.DATE` | `SyEventErrors_Date` | TField |  | The actual (server) date on which this error occurred. Note that this may not be the same as SYSTEM.DATE. |
| 10 | `SY.EE.TIME` | `SyEventErrors_Time` | TField |  | The time at which this error occurred. |
| 11 | `SY.EE.ERROR` | `SyEventErrors_Error` |  |  |  |
| 12 | `SY.EE.OFS.REF` | `SyEventErrors_OfsRef` |  |  |  |
| 13 | `SY.EE.RECORD.STATUS` | `SyEventErrors_RecordStatus` | String |  | Not used as this is a live file. |
| 14 | `SY.EE.CURR.NO` | `SyEventErrors_CurrNo` | String |  | Not used as this is a live file. |
| 15 | `SY.EE.INPUTTER` | `SyEventErrors_Inputter` |  |  |  |
| 16 | `SY.EE.DATE.TIME` | `SyEventErrors_DateTime` |  |  |  |
| 17 | `SY.EE.AUTHORISER` | `SyEventErrors_Authoriser` | String |  | Not used as this is a live file. |
| 18 | `SY.EE.CO.CODE` | `SyEventErrors_CoCode` | String |  | Not used as this is a live file. |
| 19 | `SY.EE.DEPT.CODE` | `SyEventErrors_DeptCode` | String |  | Not used as this is a live file. |
| 20 | `SY.EE.AUDITOR.CODE` | `SyEventErrors_AuditorCode` | String |  | Not used as this is a live file. |
| 21 | `SY.EE.AUDIT.DATE.TIME` | `SyEventErrors_AuditDateTime` | String |  | Not used as this is a live file. |
