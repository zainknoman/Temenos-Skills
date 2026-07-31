# BPM.TASK.ACTIONS — Table Schema

> Source: `INSERTS/I_F.BPM.TASK.ACTIONS` in `JP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BPM.TASK.ACT.ACTION` | `BpmTaskActions_Action` | TField |  |  |
| 2 | `BPM.TASK.ACT.ASSIGN.TO` | `BpmTaskActions_AssignTo` | TField |  |  |
| 3 | `BPM.TASK.ACT.ASSIGN.REASON` | `BpmTaskActions_AssignReason` | TField |  |  |
| 4 | `BPM.TASK.ACT.ASSIGN.DATE` | `BpmTaskActions_AssignDate` | TField |  |  |
| 5 | `BPM.TASK.ACT.ASSIGN.TIME` | `BpmTaskActions_AssignTime` | TField |  |  |
| 6 | `BPM.TASK.ACT.OPERATOR` | `BpmTaskActions_Operator` | TField |  |  |
| 7 | `BPM.TASK.ACT.NOTES` | `BpmTaskActions_Notes` |  |  |  |
| 8 | `BPM.TASK.ACT.LOCAL.REF` | `BpmTaskActions_LocalRef` |  |  |  |
| 9 | `BPM.TASK.ACT.RESERVED.8` | `BpmTaskActions_Reserved8` | TField |  |  |
| 10 | `BPM.TASK.ACT.RESERVED.7` | `BpmTaskActions_Reserved7` | TField |  |  |
| 11 | `BPM.TASK.ACT.RESERVED.6` | `BpmTaskActions_Reserved6` | TField |  |  |
| 12 | `BPM.TASK.ACT.RESERVED.5` | `BpmTaskActions_Reserved5` | TField |  |  |
| 13 | `BPM.TASK.ACT.RESERVED.4` | `BpmTaskActions_Reserved4` | TField |  |  |
| 14 | `BPM.TASK.ACT.RESERVED.3` | `BpmTaskActions_Reserved3` | TField |  |  |
| 15 | `BPM.TASK.ACT.RESERVED.2` | `BpmTaskActions_Reserved2` | TField |  |  |
| 16 | `BPM.TASK.ACT.RESERVED.1` | `BpmTaskActions_Reserved1` | TField |  |  |
| 17 | `BPM.TASK.ACT.RECORD.STATUS` | `BpmTaskActions_RecordStatus` | String |  |  |
| 18 | `BPM.TASK.ACT.CURR.NO` | `BpmTaskActions_CurrNo` | String |  |  |
| 19 | `BPM.TASK.ACT.INPUTTER` | `BpmTaskActions_Inputter` |  |  |  |
| 20 | `BPM.TASK.ACT.DATE.TIME` | `BpmTaskActions_DateTime` |  |  |  |
| 21 | `BPM.TASK.ACT.AUTHORISER` | `BpmTaskActions_Authoriser` | String |  |  |
| 22 | `BPM.TASK.ACT.CO.CODE` | `BpmTaskActions_CoCode` | String |  |  |
| 23 | `BPM.TASK.ACT.DEPT.CODE` | `BpmTaskActions_DeptCode` | String |  |  |
| 24 | `BPM.TASK.ACT.AUDITOR.CODE` | `BpmTaskActions_AuditorCode` | String |  |  |
| 25 | `BPM.TASK.ACT.AUDIT.DATE.TIME` | `BpmTaskActions_AuditDateTime` | String |  |  |
