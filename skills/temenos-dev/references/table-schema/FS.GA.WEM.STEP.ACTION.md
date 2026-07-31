# FS.GA.WEM.STEP.ACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.STEP.ACTION` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.STEP.ACTION.PARENT.REF.ID` | `FsGaWemStepAction_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.STEP.ACTION.ORA.ROWID` | `FsGaWemStepAction_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.STEP.ACTION.STEP.ACTION.ID` | `FsGaWemStepAction_StepActionId` | TField |  | Step Action ID Multifonds DB Column is STEP_ACTION_ID. |
| 4 | `FS.GA.WEM.STEP.ACTION.ACTION.ID` | `FsGaWemStepAction_ActionId` | TField |  | Unique ID for an Action Multifonds DB Column is ACTION_ID. |
| 5 | `FS.GA.WEM.STEP.ACTION.STEP.ID` | `FsGaWemStepAction_StepId` | TField |  | Step ID Multifonds DB Column is STEP_ID. |
| 6 | `FS.GA.WEM.STEP.ACTION.ACTIVITY.POSITION` | `FsGaWemStepAction_ActivityPosition` | TField |  | Indicates position of the activity Multifonds DB Column is POSITION. |
| 7 | `FS.GA.WEM.STEP.ACTION.STEP.ACTION.GROUP.ID` | `FsGaWemStepAction_StepActionGroupId` | TField |  | Action Group Identifier For Step Multifonds DB Column is STEP_ACTION_GROUP_ID. |
| 8 | `FS.GA.WEM.STEP.ACTION.RESERVED10` | `FsGaWemStepAction_Reserved10` | TField |  |  |
| 9 | `FS.GA.WEM.STEP.ACTION.RESERVED9` | `FsGaWemStepAction_Reserved9` | TField |  |  |
| 10 | `FS.GA.WEM.STEP.ACTION.RESERVED8` | `FsGaWemStepAction_Reserved8` | TField |  |  |
| 11 | `FS.GA.WEM.STEP.ACTION.RESERVED7` | `FsGaWemStepAction_Reserved7` | TField |  |  |
| 12 | `FS.GA.WEM.STEP.ACTION.RESERVED6` | `FsGaWemStepAction_Reserved6` | TField |  |  |
| 13 | `FS.GA.WEM.STEP.ACTION.RESERVED5` | `FsGaWemStepAction_Reserved5` | TField |  |  |
| 14 | `FS.GA.WEM.STEP.ACTION.RESERVED4` | `FsGaWemStepAction_Reserved4` | TField |  |  |
| 15 | `FS.GA.WEM.STEP.ACTION.RESERVED3` | `FsGaWemStepAction_Reserved3` | TField |  |  |
| 16 | `FS.GA.WEM.STEP.ACTION.RESERVED2` | `FsGaWemStepAction_Reserved2` | TField |  |  |
| 17 | `FS.GA.WEM.STEP.ACTION.RESERVED1` | `FsGaWemStepAction_Reserved1` | TField |  |  |
| 18 | `FS.GA.WEM.STEP.ACTION.LOCAL.REF` | `FsGaWemStepAction_LocalRef` |  |  |  |
| 19 | `FS.GA.WEM.STEP.ACTION.OVERRIDE` | `FsGaWemStepAction_Override` |  |  |  |
| 20 | `FS.GA.WEM.STEP.ACTION.RECORD.STATUS` | `FsGaWemStepAction_RecordStatus` | String |  |  |
| 21 | `FS.GA.WEM.STEP.ACTION.CURR.NO` | `FsGaWemStepAction_CurrNo` | String |  |  |
| 22 | `FS.GA.WEM.STEP.ACTION.INPUTTER` | `FsGaWemStepAction_Inputter` |  |  |  |
| 23 | `FS.GA.WEM.STEP.ACTION.DATE.TIME` | `FsGaWemStepAction_DateTime` |  |  |  |
| 24 | `FS.GA.WEM.STEP.ACTION.AUTHORISER` | `FsGaWemStepAction_Authoriser` | String |  |  |
| 25 | `FS.GA.WEM.STEP.ACTION.CO.CODE` | `FsGaWemStepAction_CoCode` | String |  |  |
| 26 | `FS.GA.WEM.STEP.ACTION.DEPT.CODE` | `FsGaWemStepAction_DeptCode` | String |  |  |
| 27 | `FS.GA.WEM.STEP.ACTION.AUDITOR.CODE` | `FsGaWemStepAction_AuditorCode` | String |  |  |
| 28 | `FS.GA.WEM.STEP.ACTION.AUDIT.DATE.TIME` | `FsGaWemStepAction_AuditDateTime` | String |  |  |
