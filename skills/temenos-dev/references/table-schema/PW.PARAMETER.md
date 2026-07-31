# PW.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PW.PARAMETER` in `PW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PW.PAR.DESCRIPTION` | `PwParameter_Description` |  |  |  |
| 2 | `PW.PAR.MOV.HIS.DATE` | `PwParameter_MovHisDate` | TField | No | PW.PROCESS and PW.ACTIVITY.TXN records are archived if the COMPLETION.DATE of PW.PROCESS record is older than or equal to this date. Validation: 1. valid T24 date field. 2. 1 - 8 characters 3. Optional input. 4. Mutually exclusive with RETENTION.PERIOD Date on which the PW.PROCESS records should be moved from live to history. |
| 3 | `PW.PAR.RETENTION.PERIOD` | `PwParameter_RetentionPeriod` | TField |  | PW.PROCESS and PW.ACTIVITY.TXN records are archived if the COMPLETION.DATE of PW.PROCESS record is older than or equal to this period. Alternative method of specifying the MOV.HIS.DATE. In the format nnD or nnW or nnM or nnY where nn is a number of either Days or Weeks or Months or Years Validation: 1. Valid T24 period 2. 1-10 type "A" (alphanumeric) characters. 3. Should be in the format nnD (days) or nnW (weeks) or nnM (months) or nnY (years) 4. Mutually exclusive with MOV.HIS.DATE. Number of days the record can stay in live file after PW.PROCESS is completed, monthly,yearly or weekly. |
| 4 | `PW.PAR.USE.WFLOW.PATTERNS` | `PwParameter_UseWflowPatterns` | TField |  | Setting this field to YES enables us to define the pattern construct fields in PW.PROCESS.DEFINITION. The value of NO prevents the user from using the pattern constructs in the process definition. Validation: 1. Value of YES or NO. |
| 5 | `PW.PAR.AUTO.PUBLISH` | `PwParameter_AutoPublish` | TField |  | Describes the publishing methodology of PW.PROCESS.DEFINITION Validation: Either YES or NO When the value selected is YES the PW.PROCESS.DEFINITION is published automatically during commit When the value selected is NO the PW.PROCESS.DEFINITION is published manually via the application PW.DEF.PUBLISHER |
| 6 | `PW.PAR.LOAD.BALANCER` | `PwParameter_LoadBalancer` | TField |  | Describes whether the task allocation follows load balancing technique Validation: Either YES or NO When the value selected is YES the tasks are allocated based on the threshold value and user status |
| 7 | `PW.PAR.ALLOCATE.TO.ADMIN` | `PwParameter_AllocateToAdmin` | TField |  | Describes whether the task should be allocated to the admin during Load Balancing. When the value selected is YES all the tasks are allocated to the first user in the PW.PARTICIPANT Validation: Either YES or NO This field value can be set to YES only when Load Balancer is set to YES |
| 8 | `PW.PAR.SYSTEM.THRESHOLD` | `PwParameter_SystemThreshold` | TField |  |  |
| 9 | `PW.PAR.RESERVED.6` | `PwParameter_Reserved6` |  |  |  |
| 10 | `PW.PAR.RESERVED.5` | `PwParameter_Reserved5` | TField |  |  |
| 11 | `PW.PAR.RESERVED.4` | `PwParameter_Reserved4` | TField |  |  |
| 12 | `PW.PAR.RESERVED.3` | `PwParameter_Reserved3` | TField |  |  |
| 13 | `PW.PAR.RESERVED.2` | `PwParameter_Reserved2` | TField |  |  |
| 14 | `PW.PAR.RESERVED.1` | `PwParameter_Reserved1` | TField |  |  |
| 15 | `PW.PAR.LOCAL.REF` | `PwParameter_LocalRef` |  |  |  |
| 16 | `PW.PAR.OVERRIDE` | `PwParameter_Override` |  |  |  |
| 17 | `PW.PAR.RECORD.STATUS` | `PwParameter_RecordStatus` | String |  |  |
| 18 | `PW.PAR.CURR.NO` | `PwParameter_CurrNo` | String |  |  |
| 19 | `PW.PAR.INPUTTER` | `PwParameter_Inputter` |  |  |  |
| 20 | `PW.PAR.DATE.TIME` | `PwParameter_DateTime` |  |  |  |
| 21 | `PW.PAR.AUTHORISER` | `PwParameter_Authoriser` | String |  |  |
| 22 | `PW.PAR.CO.CODE` | `PwParameter_CoCode` | String |  |  |
| 23 | `PW.PAR.DEPT.CODE` | `PwParameter_DeptCode` | String |  |  |
| 24 | `PW.PAR.AUDITOR.CODE` | `PwParameter_AuditorCode` | String |  |  |
| 25 | `PW.PAR.AUDIT.DATE.TIME` | `PwParameter_AuditDateTime` | String |  |  |
