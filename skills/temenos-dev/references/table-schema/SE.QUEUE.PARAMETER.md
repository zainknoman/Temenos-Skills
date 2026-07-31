# SE.QUEUE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SE.QUEUE.PARAMETER` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `QUEUE.PAR.TOTAL.INJECT` | `SeQueueParameter_TotalInject` | TField |  |  |
| 2 | `QUEUE.PAR.TOTAL.CONTROL.LISTS` | `SeQueueParameter_TotalControlLists` | TField |  |  |
| 3 | `QUEUE.PAR.NO.OF.CL.RECS` | `SeQueueParameter_NoOfClRecs` | TField |  |  |
| 4 | `QUEUE.PAR.JOB.TIMES.ID` | `SeQueueParameter_JobTimesId` | TField |  |  |
| 5 | `QUEUE.PAR.LOCK.INJECT.CNT` | `SeQueueParameter_LockInjectCnt` | TField |  |  |
| 6 | `QUEUE.PAR.RESERVED.04` | `SeQueueParameter_Reserved04` |  |  |  |
| 7 | `QUEUE.PAR.RESERVED.03` | `SeQueueParameter_Reserved03` | TField |  |  |
| 8 | `QUEUE.PAR.RESERVED.02` | `SeQueueParameter_Reserved02` | TField |  |  |
| 9 | `QUEUE.PAR.RESERVED.01` | `SeQueueParameter_Reserved01` | TField |  |  |
| 10 | `QUEUE.PAR.RECORD.STATUS` | `SeQueueParameter_RecordStatus` | String |  |  |
| 11 | `QUEUE.PAR.CURR.NO` | `SeQueueParameter_CurrNo` | String |  |  |
| 12 | `QUEUE.PAR.INPUTTER` | `SeQueueParameter_Inputter` |  |  |  |
| 13 | `QUEUE.PAR.DATE.TIME` | `SeQueueParameter_DateTime` |  |  |  |
| 14 | `QUEUE.PAR.AUTHORISER` | `SeQueueParameter_Authoriser` | String |  |  |
| 15 | `QUEUE.PAR.CO.CODE` | `SeQueueParameter_CoCode` | String |  |  |
| 16 | `QUEUE.PAR.DEPT.CODE` | `SeQueueParameter_DeptCode` | String |  |  |
| 17 | `QUEUE.PAR.AUDITOR.CODE` | `SeQueueParameter_AuditorCode` | String |  |  |
| 18 | `QUEUE.PAR.AUDIT.DATE.TIME` | `SeQueueParameter_AuditDateTime` | String |  |  |
