# CL.QUEUE — Table Schema

> Source: `INSERTS/I_F.CL.QUEUE` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CLQ.DESCRIPTION` | `ClQueue_Description` |  |  |  |
| 2 | `CLQ.SELECTION` | `ClQueue_Selection` | TField |  | User can desire to set flag whether particular queue can active or inactive for a centain period. |
| 3 | `CLQ.QUEUE.TYPE` | `ClQueue_QueueType` | TField |  | Type of the queue. |
| 4 | `CLQ.AGENCY` | `ClQueue_Agency` | TField |  | External Agency who handles the queue. |
| 5 | `CLQ.AGENCY.BRANCH` | `ClQueue_AgencyBranch` | TField |  | Branch of the agency that handles the queue. |
| 6 | `CLQ.PRIORITY` | `ClQueue_Priority` | TField |  | When a queue is based on selection, it is assigned with a priority to be used in case of different queues are sharing same criteria. |
| 7 | `CLQ.ITEM.FIELD` | `ClQueue_ItemField` |  |  |  |
| 8 | `CLQ.OPERATOR` | `ClQueue_Operator` |  |  |  |
| 9 | `CLQ.VALUE.FROM` | `ClQueue_ValueFrom` |  |  |  |
| 10 | `CLQ.VALUE.TO` | `ClQueue_ValueTo` |  |  |  |
| 11 | `CLQ.LOGIC.OPER` | `ClQueue_LogicOper` |  |  |  |
| 12 | `CLQ.INACTIVITY.DAYS` | `ClQueue_InactivityDays` | TField |  | Number of days for any item in this queue without any action to be considered as inactive. |
| 13 | `CLQ.INACTIVITY.OUTCOME` | `ClQueue_InactivityOutcome` | TField |  |  |
| 14 | `CLQ.LOCAL.REF` | `ClQueue_LocalRef` |  |  |  |
| 15 | `CLQ.RESERVED.5` | `ClQueue_Reserved5` | TField |  |  |
| 16 | `CLQ.RESERVED.4` | `ClQueue_Reserved4` | TField |  |  |
| 17 | `CLQ.RESERVED.3` | `ClQueue_Reserved3` | TField |  |  |
| 18 | `CLQ.RESERVED.2` | `ClQueue_Reserved2` | TField |  |  |
| 19 | `CLQ.RESERVED.1` | `ClQueue_Reserved1` | TField |  |  |
| 20 | `CLQ.RECORD.STATUS` | `ClQueue_RecordStatus` | String |  |  |
| 21 | `CLQ.CURR.NO` | `ClQueue_CurrNo` | String |  |  |
| 22 | `CLQ.INPUTTER` | `ClQueue_Inputter` |  |  |  |
| 23 | `CLQ.DATE.TIME` | `ClQueue_DateTime` |  |  |  |
| 24 | `CLQ.AUTHORISER` | `ClQueue_Authoriser` | String |  |  |
| 25 | `CLQ.CO.CODE` | `ClQueue_CoCode` | String |  |  |
| 26 | `CLQ.DEPT.CODE` | `ClQueue_DeptCode` | String |  |  |
| 27 | `CLQ.AUDITOR.CODE` | `ClQueue_AuditorCode` | String |  |  |
| 28 | `CLQ.AUDIT.DATE.TIME` | `ClQueue_AuditDateTime` | String |  |  |
