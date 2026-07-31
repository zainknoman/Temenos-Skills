# FS.GA.WEM.STEP.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.STEP.DETAILS` in `FS_WemChecklistConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.STEP.DETAILS.PARENT.REF.ID` | `FsGaWemStepDetails_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.STEP.DETAILS.ORA.ROWID` | `FsGaWemStepDetails_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.STEP.DETAILS.STEP.ID` | `FsGaWemStepDetails_StepId` | TField |  | Step ID Multifonds DB Column is STEP_ID. |
| 4 | `FS.GA.WEM.STEP.DETAILS.MODEL.ID` | `FsGaWemStepDetails_ModelId` | TField |  | ID of the Model Multifonds DB Column is MODEL_ID. |
| 5 | `FS.GA.WEM.STEP.DETAILS.NAME` | `FsGaWemStepDetails_Name` | TField |  | Name Multifonds DB Column is NAME. |
| 6 | `FS.GA.WEM.STEP.DETAILS.DESCRIPTION` | `FsGaWemStepDetails_Description` | TField |  | Field Description Multifonds DB Column is DESCRIPTION. |
| 7 | `FS.GA.WEM.STEP.DETAILS.ACTIVITY.POSITION` | `FsGaWemStepDetails_ActivityPosition` | TField |  | Indicates position of the activity Multifonds DB Column is POSITION. |
| 8 | `FS.GA.WEM.STEP.DETAILS.PROCESS.GROUP` | `FsGaWemStepDetails_ProcessGroup` | TField |  | Process Group to which different processes are attached Multifonds DB Column is CODE_PROCESS. |
| 9 | `FS.GA.WEM.STEP.DETAILS.STEP.CUT.OFF.TIME` | `FsGaWemStepDetails_StepCutOffTime` | TField |  | The cut off time before which the step to be processed Multifonds DB Column is DEADLINE_HOUR. |
| 10 | `FS.GA.WEM.STEP.DETAILS.DEADLINE.DAY` | `FsGaWemStepDetails_DeadlineDay` | TField |  | Deadline day Multifonds DB Column is DEADLINE_DAY. |
| 11 | `FS.GA.WEM.STEP.DETAILS.SHORT.DESCRIPTION` | `FsGaWemStepDetails_ShortDescription` | TField |  | Short description for form or report in drilldown and also indicates short description of a Step Multifonds DB Column is ABREGE. |
| 12 | `FS.GA.WEM.STEP.DETAILS.OPTIONAL.FLAG` | `FsGaWemStepDetails_OptionalFlag` | TField | Conditional | Indicates whether the step is optional or mandatory Multifonds DB Column is OPTIONAL_FLG. |
| 13 | `FS.GA.WEM.STEP.DETAILS.WARNING.EXCEPTION.LEVEL` | `FsGaWemStepDetails_WarningExceptionLevel` | TField |  | Warning Exception Level Multifonds DB Column is WAR_EXCEPTION_ID. |
| 14 | `FS.GA.WEM.STEP.DETAILS.FATAL.EXCEPTION.LEVEL` | `FsGaWemStepDetails_FatalExceptionLevel` | TField |  | Minimum status for Fatal Exception Multifonds DB Column is FAT_EXCEPTION_ID. |
| 15 | `FS.GA.WEM.STEP.DETAILS.STEP.START.TIME` | `FsGaWemStepDetails_StepStartTime` | TField |  | Step Start Time Multifonds DB Column is STEP_START_TIME. |
| 16 | `FS.GA.WEM.STEP.DETAILS.STEP.END.TIME` | `FsGaWemStepDetails_StepEndTime` | TField |  | Step End Time Multifonds DB Column is STEP_END_TIME. |
| 17 | `FS.GA.WEM.STEP.DETAILS.STATUS.IDENT.FOR.STEP.GROUP` | `FsGaWemStepDetails_StatusIdentForStepGroup` | TField |  | Status Identifier For Step Group Multifonds DB Column is STEP_GRP_STATUS. |
| 18 | `FS.GA.WEM.STEP.DETAILS.STEP.MESSAGE` | `FsGaWemStepDetails_StepMessage` | TField |  | Displays message for the current step status Multifonds DB Column is STEP_MESSAGE. |
| 19 | `FS.GA.WEM.STEP.DETAILS.SKIP.IDENTIFIER` | `FsGaWemStepDetails_SkipIdentifier` | TField |  | Skip Identifier For Loader Purpose Multifonds DB Column is SKIP_FLG_LOAD. |
| 20 | `FS.GA.WEM.STEP.DETAILS.CONTROL.NUMBER` | `FsGaWemStepDetails_ControlNumber` | TField |  | Control Number Multifonds DB Column is TYP_CTRL. |
| 21 | `FS.GA.WEM.STEP.DETAILS.SKIP` | `FsGaWemStepDetails_Skip` | TField |  | Skip Identifier Multifonds DB Column is SKIP_FLG. |
| 22 | `FS.GA.WEM.STEP.DETAILS.EMAIL.NOTIFICATION` | `FsGaWemStepDetails_EmailNotification` | TField |  | If set &apos;Y&apos; an Email notification to be sent once the step is completed,. If set &apos;N&apos;, or left blank, no Email notifications to be sent. Multifonds DB Column is BY_GROUP_EMAIL. |
| 23 | `FS.GA.WEM.STEP.DETAILS.FOF.CONTROL` | `FsGaWemStepDetails_FofControl` | TField |  | Used in Fund of Fund scenario Multifonds DB Column is FOF_CONTROL. |
| 24 | `FS.GA.WEM.STEP.DETAILS.PREVIOUS.STEP.FUND.COUNT` | `FsGaWemStepDetails_PreviousStepFundCount` | TField |  | Previous Step Fund Count Multifonds DB Column is PRSTP_FNDCNT. |
| 25 | `FS.GA.WEM.STEP.DETAILS.FUTURE.STEP.FUND.COUNT` | `FsGaWemStepDetails_FutureStepFundCount` | TField |  | Future Step Fund Count Multifonds DB Column is FUTSTP_FNDCNT. |
| 26 | `FS.GA.WEM.STEP.DETAILS.RESULT` | `FsGaWemStepDetails_Result` | TField |  | Displays Results Multifonds DB Column is RESULT. |
| 27 | `FS.GA.WEM.STEP.DETAILS.REOCCURRENCE.TIME` | `FsGaWemStepDetails_ReoccurrenceTime` | TField |  | Reoccurrence time of the step Multifonds DB Column is RE_OCCUR_ITVL. |
| 28 | `FS.GA.WEM.STEP.DETAILS.STREAM.ID` | `FsGaWemStepDetails_StreamId` | TField |  | Stream ID Multifonds DB Column is STREAM_ID. |
| 29 | `FS.GA.WEM.STEP.DETAILS.USER.GROUP.ACCESS.RIGHT` | `FsGaWemStepDetails_UserGroupAccessRight` | TField |  | The user group which has rights to access the particular screen or function. Multifonds DB Column is ACCESS_ROLE. |
| 30 | `FS.GA.WEM.STEP.DETAILS.PREVIOUS.STEP.GROUP.STATUS` | `FsGaWemStepDetails_PreviousStepGroupStatus` | TField |  | Previous Step Group Status Multifonds DB Column is PREV_STEP_GRP_STATUS. |
| 31 | `FS.GA.WEM.STEP.DETAILS.BI.PROCESS.JOB.ID` | `FsGaWemStepDetails_BiProcessJobId` | TField |  | To generate report through a WEM step Multifonds DB Column is BIPUB_JOB. |
| 32 | `FS.GA.WEM.STEP.DETAILS.NAV.DATE.FLAG` | `FsGaWemStepDetails_NavDateFlag` | TField |  | Used in case of Back dated NAV control check Multifonds DB Column is NAV_DATE_FLG. |
| 33 | `FS.GA.WEM.STEP.DETAILS.STANDARD.STEP.IDENTIFIER` | `FsGaWemStepDetails_StandardStepIdentifier` | TField |  | Standard Step Identifier Multifonds DB Column is STANDARD_STEP_ID. |
| 34 | `FS.GA.WEM.STEP.DETAILS.RESERVED10` | `FsGaWemStepDetails_Reserved10` | TField |  |  |
| 35 | `FS.GA.WEM.STEP.DETAILS.RESERVED9` | `FsGaWemStepDetails_Reserved9` | TField |  |  |
| 36 | `FS.GA.WEM.STEP.DETAILS.RESERVED8` | `FsGaWemStepDetails_Reserved8` | TField |  |  |
| 37 | `FS.GA.WEM.STEP.DETAILS.RESERVED7` | `FsGaWemStepDetails_Reserved7` | TField |  |  |
| 38 | `FS.GA.WEM.STEP.DETAILS.RESERVED6` | `FsGaWemStepDetails_Reserved6` | TField |  |  |
| 39 | `FS.GA.WEM.STEP.DETAILS.RESERVED5` | `FsGaWemStepDetails_Reserved5` | TField |  |  |
| 40 | `FS.GA.WEM.STEP.DETAILS.RESERVED4` | `FsGaWemStepDetails_Reserved4` | TField |  |  |
| 41 | `FS.GA.WEM.STEP.DETAILS.RESERVED3` | `FsGaWemStepDetails_Reserved3` | TField |  |  |
| 42 | `FS.GA.WEM.STEP.DETAILS.RESERVED2` | `FsGaWemStepDetails_Reserved2` | TField |  |  |
| 43 | `FS.GA.WEM.STEP.DETAILS.RESERVED1` | `FsGaWemStepDetails_Reserved1` | TField |  |  |
| 44 | `FS.GA.WEM.STEP.DETAILS.LOCAL.REF` | `FsGaWemStepDetails_LocalRef` |  |  |  |
| 45 | `FS.GA.WEM.STEP.DETAILS.OVERRIDE` | `FsGaWemStepDetails_Override` |  |  |  |
| 46 | `FS.GA.WEM.STEP.DETAILS.RECORD.STATUS` | `FsGaWemStepDetails_RecordStatus` | String |  |  |
| 47 | `FS.GA.WEM.STEP.DETAILS.CURR.NO` | `FsGaWemStepDetails_CurrNo` | String |  |  |
| 48 | `FS.GA.WEM.STEP.DETAILS.INPUTTER` | `FsGaWemStepDetails_Inputter` |  |  |  |
| 49 | `FS.GA.WEM.STEP.DETAILS.DATE.TIME` | `FsGaWemStepDetails_DateTime` |  |  |  |
| 50 | `FS.GA.WEM.STEP.DETAILS.AUTHORISER` | `FsGaWemStepDetails_Authoriser` | String |  |  |
| 51 | `FS.GA.WEM.STEP.DETAILS.CO.CODE` | `FsGaWemStepDetails_CoCode` | String |  |  |
| 52 | `FS.GA.WEM.STEP.DETAILS.DEPT.CODE` | `FsGaWemStepDetails_DeptCode` | String |  |  |
| 53 | `FS.GA.WEM.STEP.DETAILS.AUDITOR.CODE` | `FsGaWemStepDetails_AuditorCode` | String |  |  |
| 54 | `FS.GA.WEM.STEP.DETAILS.AUDIT.DATE.TIME` | `FsGaWemStepDetails_AuditDateTime` | String |  |  |
