# FS.GI.WEM.WORKFLOW.STATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.WORKFLOW.STATE` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.WORKFLOW.STATE.WORKFLOW.STATE.ID` | `FsGiWemWorkflowState_WorkflowStateId` | TField |  |  |
| 2 | `FS.GI.WEM.WORKFLOW.STATE.WORKFLOW` | `FsGiWemWorkflowState_Workflow` | TField |  |  |
| 3 | `FS.GI.WEM.WORKFLOW.STATE.WORKFLOW.TYPE` | `FsGiWemWorkflowState_WorkflowType` | TField |  |  |
| 4 | `FS.GI.WEM.WORKFLOW.STATE.ENTITY.TYPE` | `FsGiWemWorkflowState_EntityType` | TField |  |  |
| 5 | `FS.GI.WEM.WORKFLOW.STATE.ENTITY.ID` | `FsGiWemWorkflowState_EntityId` | TField |  |  |
| 6 | `FS.GI.WEM.WORKFLOW.STATE.WORKFLOW.DATE` | `FsGiWemWorkflowState_WorkflowDate` | TField |  |  |
| 7 | `FS.GI.WEM.WORKFLOW.STATE.STEP.DATE1` | `FsGiWemWorkflowState_StepDate1` | TField |  |  |
| 8 | `FS.GI.WEM.WORKFLOW.STATE.STEP.DATE2` | `FsGiWemWorkflowState_StepDate2` | TField |  |  |
| 9 | `FS.GI.WEM.WORKFLOW.STATE.WORKFLOW.DATE.TYPE` | `FsGiWemWorkflowState_WorkflowDateType` | TField |  |  |
| 10 | `FS.GI.WEM.WORKFLOW.STATE.RESERVED10` | `FsGiWemWorkflowState_Reserved10` | TField |  |  |
| 11 | `FS.GI.WEM.WORKFLOW.STATE.RESERVED9` | `FsGiWemWorkflowState_Reserved9` | TField |  |  |
| 12 | `FS.GI.WEM.WORKFLOW.STATE.RESERVED8` | `FsGiWemWorkflowState_Reserved8` | TField |  |  |
| 13 | `FS.GI.WEM.WORKFLOW.STATE.RESERVED7` | `FsGiWemWorkflowState_Reserved7` | TField |  |  |
| 14 | `FS.GI.WEM.WORKFLOW.STATE.RESERVED6` | `FsGiWemWorkflowState_Reserved6` | TField |  |  |
| 15 | `FS.GI.WEM.WORKFLOW.STATE.RESERVED5` | `FsGiWemWorkflowState_Reserved5` | TField |  |  |
| 16 | `FS.GI.WEM.WORKFLOW.STATE.RESERVED4` | `FsGiWemWorkflowState_Reserved4` | TField |  |  |
| 17 | `FS.GI.WEM.WORKFLOW.STATE.RESERVED3` | `FsGiWemWorkflowState_Reserved3` | TField |  |  |
| 18 | `FS.GI.WEM.WORKFLOW.STATE.RESERVED2` | `FsGiWemWorkflowState_Reserved2` | TField |  |  |
| 19 | `FS.GI.WEM.WORKFLOW.STATE.RESERVED1` | `FsGiWemWorkflowState_Reserved1` | TField |  |  |
| 20 | `FS.GI.WEM.WORKFLOW.STATE.LOCAL.REF` | `FsGiWemWorkflowState_LocalRef` |  |  |  |
| 21 | `FS.GI.WEM.WORKFLOW.STATE.OVERRIDE` | `FsGiWemWorkflowState_Override` |  |  |  |
| 22 | `FS.GI.WEM.WORKFLOW.STATE.RECORD.STATUS` | `FsGiWemWorkflowState_RecordStatus` | String |  |  |
| 23 | `FS.GI.WEM.WORKFLOW.STATE.CURR.NO` | `FsGiWemWorkflowState_CurrNo` | String |  |  |
| 24 | `FS.GI.WEM.WORKFLOW.STATE.INPUTTER` | `FsGiWemWorkflowState_Inputter` |  |  |  |
| 25 | `FS.GI.WEM.WORKFLOW.STATE.DATE.TIME` | `FsGiWemWorkflowState_DateTime` |  |  |  |
| 26 | `FS.GI.WEM.WORKFLOW.STATE.AUTHORISER` | `FsGiWemWorkflowState_Authoriser` | String |  |  |
| 27 | `FS.GI.WEM.WORKFLOW.STATE.CO.CODE` | `FsGiWemWorkflowState_CoCode` | String |  |  |
| 28 | `FS.GI.WEM.WORKFLOW.STATE.DEPT.CODE` | `FsGiWemWorkflowState_DeptCode` | String |  |  |
| 29 | `FS.GI.WEM.WORKFLOW.STATE.AUDITOR.CODE` | `FsGiWemWorkflowState_AuditorCode` | String |  |  |
| 30 | `FS.GI.WEM.WORKFLOW.STATE.AUDIT.DATE.TIME` | `FsGiWemWorkflowState_AuditDateTime` | String |  |  |
