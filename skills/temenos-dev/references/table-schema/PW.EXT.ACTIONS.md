# PW.EXT.ACTIONS — Table Schema

> Source: `INSERTS/I_F.PW.EXT.ACTIONS` in `PW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PW.EXT.ACT.ACTION` | `PwExtActions_Action` | TField |  | PW.EXT.ACTIONS ACTION This option allows user to do the following actions on the task Action,Reassign,Acquire,Release,Suspend,Resume,Skip |
| 2 | `PW.EXT.ACT.ASSIGN.TO` | `PwExtActions_AssignTo` | TField |  | PW.EXT.ACTIONS ASSIGN.TO The particular task can be assigned to any valid t24 user |
| 3 | `PW.EXT.ACT.ASSIGN.REASON` | `PwExtActions_AssignReason` | TField |  | PW.EXT.ACTIONS ASSIGN.REASON The description or the reason for reassigning the particular task to another user Validation Rules Standard T24 alphanumeric field. Free text Maximum of 35 characters |
| 4 | `PW.EXT.ACT.ASSIGN.DATE` | `PwExtActions_AssignDate` | TField |  | PW.EXT.ACTIONS ASSIGN.DATE System date on which the task is reassigned to another user. System Maintained. No-input. |
| 5 | `PW.EXT.ACT.ASSIGN.TIME` | `PwExtActions_AssignTime` | TField |  | PW.EXT.ACTIONS ASSIGN.TIME System time on which the action was initiated System Maintained. No-input. |
| 6 | `PW.EXT.ACT.OPERATOR` | `PwExtActions_Operator` | TField |  | PW.EXT.ACTIONS OPERATOR The field holds the operator or user name for whom the record is created. Validation Rules Standard T24 alphanumeric field. Noinput field Maximum of 35 characters |
| 7 | `PW.EXT.ACT.NOTES` | `PwExtActions_Notes` |  |  |  |
| 8 | `PW.EXT.ACT.LOCAL.REF` | `PwExtActions_LocalRef` |  |  |  |
| 9 | `PW.EXT.ACT.RESERVED.8` | `PwExtActions_Reserved8` | TField |  |  |
| 10 | `PW.EXT.ACT.RESERVED.7` | `PwExtActions_Reserved7` | TField |  |  |
| 11 | `PW.EXT.ACT.RESERVED.6` | `PwExtActions_Reserved6` | TField |  |  |
| 12 | `PW.EXT.ACT.RESERVED.5` | `PwExtActions_Reserved5` | TField |  |  |
| 13 | `PW.EXT.ACT.RESERVED.4` | `PwExtActions_Reserved4` | TField |  |  |
| 14 | `PW.EXT.ACT.RESERVED.3` | `PwExtActions_Reserved3` | TField |  |  |
| 15 | `PW.EXT.ACT.RESERVED.2` | `PwExtActions_Reserved2` | TField |  |  |
| 16 | `PW.EXT.ACT.RESERVED.1` | `PwExtActions_Reserved1` | TField |  |  |
| 17 | `PW.EXT.ACT.RECORD.STATUS` | `PwExtActions_RecordStatus` | String |  |  |
| 18 | `PW.EXT.ACT.CURR.NO` | `PwExtActions_CurrNo` | String |  |  |
| 19 | `PW.EXT.ACT.INPUTTER` | `PwExtActions_Inputter` |  |  |  |
| 20 | `PW.EXT.ACT.DATE.TIME` | `PwExtActions_DateTime` |  |  |  |
| 21 | `PW.EXT.ACT.AUTHORISER` | `PwExtActions_Authoriser` | String |  |  |
| 22 | `PW.EXT.ACT.CO.CODE` | `PwExtActions_CoCode` | String |  |  |
| 23 | `PW.EXT.ACT.DEPT.CODE` | `PwExtActions_DeptCode` | String |  |  |
| 24 | `PW.EXT.ACT.AUDITOR.CODE` | `PwExtActions_AuditorCode` | String |  |  |
| 25 | `PW.EXT.ACT.AUDIT.DATE.TIME` | `PwExtActions_AuditDateTime` | String |  |  |
