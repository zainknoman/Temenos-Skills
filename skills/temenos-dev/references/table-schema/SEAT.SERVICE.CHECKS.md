# SEAT.SERVICE.CHECKS — Table Schema

> Source: `INSERTS/I_F.SEAT.SERVICE.CHECKS` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.SERV.CHKS.SCRIPT.GROUP` | `SeatServiceChecks_ScriptGroup` |  |  |  |
| 2 | `SE.SERV.CHKS.ACTIVATION.SERVICE` | `SeatServiceChecks_ActivationService` | TField |  | This field is used to identify if service is an activation service. |
| 3 | `SE.SERV.CHKS.JOBS.TO.CHECK` | `SeatServiceChecks_JobsToCheck` |  |  |  |
| 4 | `SE.SERV.CHKS.FILE.NAME` | `SeatServiceChecks_FileName` |  |  |  |
| 5 | `SE.SERV.CHKS.SELECTION.CRITERIA` | `SeatServiceChecks_SelectionCriteria` |  |  |  |
| 6 | `SE.SERV.CHKS.RESERVED.8` | `SeatServiceChecks_Reserved8` | TField |  |  |
| 7 | `SE.SERV.CHKS.RESERVED.7` | `SeatServiceChecks_Reserved7` | TField |  |  |
| 8 | `SE.SERV.CHKS.RESERVED.6` | `SeatServiceChecks_Reserved6` | TField |  |  |
| 9 | `SE.SERV.CHKS.RESERVED.5` | `SeatServiceChecks_Reserved5` | TField |  |  |
| 10 | `SE.SERV.CHKS.RESERVED.4` | `SeatServiceChecks_Reserved4` | TField |  |  |
| 11 | `SE.SERV.CHKS.RESERVED.3` | `SeatServiceChecks_Reserved3` | TField |  |  |
| 12 | `SE.SERV.CHKS.RESERVED.2` | `SeatServiceChecks_Reserved2` | TField |  |  |
| 13 | `SE.SERV.CHKS.RESERVED.1` | `SeatServiceChecks_Reserved1` | TField |  |  |
| 14 | `SE.SERV.CHKS.LOCAL.REF` | `SeatServiceChecks_LocalRef` |  |  |  |
| 15 | `SE.SERV.CHKS.STMT.NOS` | `SeatServiceChecks_StmtNos` |  |  |  |
| 16 | `SE.SERV.CHKS.OVERRIDE` | `SeatServiceChecks_Override` |  |  |  |
| 17 | `SE.SERV.CHKS.RECORD.STATUS` | `SeatServiceChecks_RecordStatus` | String |  |  |
| 18 | `SE.SERV.CHKS.CURR.NO` | `SeatServiceChecks_CurrNo` | String |  |  |
| 19 | `SE.SERV.CHKS.INPUTTER` | `SeatServiceChecks_Inputter` |  |  |  |
| 20 | `SE.SERV.CHKS.DATE.TIME` | `SeatServiceChecks_DateTime` |  |  |  |
| 21 | `SE.SERV.CHKS.AUTHORISER` | `SeatServiceChecks_Authoriser` | String |  |  |
| 22 | `SE.SERV.CHKS.CO.CODE` | `SeatServiceChecks_CoCode` | String |  |  |
| 23 | `SE.SERV.CHKS.DEPT.CODE` | `SeatServiceChecks_DeptCode` | String |  |  |
| 24 | `SE.SERV.CHKS.AUDITOR.CODE` | `SeatServiceChecks_AuditorCode` | String |  |  |
| 25 | `SE.SERV.CHKS.AUDIT.DATE.TIME` | `SeatServiceChecks_AuditDateTime` | String |  |  |
