# FS.GA.WEM.STEP.CONTROL.ID.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.STEP.CONTROL.ID.DETAILS` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.PARENT.REF.ID` | `FsGaWemStepControlIdDetails_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.ORA.ROWID` | `FsGaWemStepControlIdDetails_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.STEP.CONTROL.ID` | `FsGaWemStepControlIdDetails_StepControlId` | TField |  | Step Control ID Multifonds DB Column is STEP_CONTROL_ID. |
| 4 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.CONTROL.ID` | `FsGaWemStepControlIdDetails_ControlId` | TField |  | Control ID Multifonds DB Column is CONTROL_ID. |
| 5 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.STEP.ID` | `FsGaWemStepControlIdDetails_StepId` | TField |  | Step ID Multifonds DB Column is STEP_ID. |
| 6 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.ACTIVITY.POSITION` | `FsGaWemStepControlIdDetails_ActivityPosition` | TField |  | Indicates position of the activity Multifonds DB Column is POSITION. |
| 7 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RESERVED10` | `FsGaWemStepControlIdDetails_Reserved10` | TField |  |  |
| 8 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RESERVED9` | `FsGaWemStepControlIdDetails_Reserved9` | TField |  |  |
| 9 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RESERVED8` | `FsGaWemStepControlIdDetails_Reserved8` | TField |  |  |
| 10 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RESERVED7` | `FsGaWemStepControlIdDetails_Reserved7` | TField |  |  |
| 11 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RESERVED6` | `FsGaWemStepControlIdDetails_Reserved6` | TField |  |  |
| 12 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RESERVED5` | `FsGaWemStepControlIdDetails_Reserved5` | TField |  |  |
| 13 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RESERVED4` | `FsGaWemStepControlIdDetails_Reserved4` | TField |  |  |
| 14 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RESERVED3` | `FsGaWemStepControlIdDetails_Reserved3` | TField |  |  |
| 15 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RESERVED2` | `FsGaWemStepControlIdDetails_Reserved2` | TField |  |  |
| 16 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RESERVED1` | `FsGaWemStepControlIdDetails_Reserved1` | TField |  |  |
| 17 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.LOCAL.REF` | `FsGaWemStepControlIdDetails_LocalRef` |  |  |  |
| 18 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.OVERRIDE` | `FsGaWemStepControlIdDetails_Override` |  |  |  |
| 19 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.RECORD.STATUS` | `FsGaWemStepControlIdDetails_RecordStatus` | String |  |  |
| 20 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.CURR.NO` | `FsGaWemStepControlIdDetails_CurrNo` | String |  |  |
| 21 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.INPUTTER` | `FsGaWemStepControlIdDetails_Inputter` |  |  |  |
| 22 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.DATE.TIME` | `FsGaWemStepControlIdDetails_DateTime` |  |  |  |
| 23 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.AUTHORISER` | `FsGaWemStepControlIdDetails_Authoriser` | String |  |  |
| 24 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.CO.CODE` | `FsGaWemStepControlIdDetails_CoCode` | String |  |  |
| 25 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.DEPT.CODE` | `FsGaWemStepControlIdDetails_DeptCode` | String |  |  |
| 26 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.AUDITOR.CODE` | `FsGaWemStepControlIdDetails_AuditorCode` | String |  |  |
| 27 | `FS.GA.WEM.STEP.CONTROL.ID.DETAILS.AUDIT.DATE.TIME` | `FsGaWemStepControlIdDetails_AuditDateTime` | String |  |  |
