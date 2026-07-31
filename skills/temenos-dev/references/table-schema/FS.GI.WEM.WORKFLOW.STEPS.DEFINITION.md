# FS.GI.WEM.WORKFLOW.STEPS.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.WORKFLOW.STEPS.DEFINITION` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.WORKFLOW.ID` | `FsGiWemWorkflowStepsDefinition_WorkflowId` | TField |  | Linked workflow ID Multifonds DB Column is WORKFLOW.ID. |
| 2 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.STEP.ID` | `FsGiWemWorkflowStepsDefinition_StepId` |  |  |  |
| 3 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.STEP.SEQUENCE` | `FsGiWemWorkflowStepsDefinition_StepSequence` |  |  |  |
| 4 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.SCOPE` | `FsGiWemWorkflowStepsDefinition_Scope` |  |  |  |
| 5 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.DATE.BASIS` | `FsGiWemWorkflowStepsDefinition_DateBasis` |  |  |  |
| 6 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.TRIGGER` | `FsGiWemWorkflowStepsDefinition_Trigger` |  |  |  |
| 7 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.STEP.START` | `FsGiWemWorkflowStepsDefinition_StepStart` |  |  |  |
| 8 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.STEP.COMPLETION` | `FsGiWemWorkflowStepsDefinition_StepCompletion` |  |  |  |
| 9 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.STEP.CUTOFF` | `FsGiWemWorkflowStepsDefinition_StepCutoff` |  |  |  |
| 10 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.INTERVAL` | `FsGiWemWorkflowStepsDefinition_Interval` |  |  |  |
| 11 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.COOLING.OFF` | `FsGiWemWorkflowStepsDefinition_CoolingOff` |  |  |  |
| 12 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.VALIDATION.FLAG` | `FsGiWemWorkflowStepsDefinition_ValidationFlag` |  |  |  |
| 13 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.ROLLBACK.ALLOWED.FLAG` | `FsGiWemWorkflowStepsDefinition_RollbackAllowedFlag` |  |  |  |
| 14 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.REVERSE.PROCESSING.FLAG` | `FsGiWemWorkflowStepsDefinition_ReverseProcessingFlag` |  |  |  |
| 15 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.USER.LINK.1` | `FsGiWemWorkflowStepsDefinition_UserLink1` |  |  |  |
| 16 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.USER.LINK.2` | `FsGiWemWorkflowStepsDefinition_UserLink2` |  |  |  |
| 17 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.STEP.INFO` | `FsGiWemWorkflowStepsDefinition_StepInfo` |  |  |  |
| 18 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RESERVED10` | `FsGiWemWorkflowStepsDefinition_Reserved10` | TField |  |  |
| 19 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RESERVED9` | `FsGiWemWorkflowStepsDefinition_Reserved9` | TField |  |  |
| 20 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RESERVED8` | `FsGiWemWorkflowStepsDefinition_Reserved8` | TField |  |  |
| 21 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RESERVED7` | `FsGiWemWorkflowStepsDefinition_Reserved7` | TField |  |  |
| 22 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RESERVED6` | `FsGiWemWorkflowStepsDefinition_Reserved6` | TField |  |  |
| 23 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RESERVED5` | `FsGiWemWorkflowStepsDefinition_Reserved5` | TField |  |  |
| 24 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RESERVED4` | `FsGiWemWorkflowStepsDefinition_Reserved4` | TField |  |  |
| 25 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RESERVED3` | `FsGiWemWorkflowStepsDefinition_Reserved3` | TField |  |  |
| 26 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RESERVED2` | `FsGiWemWorkflowStepsDefinition_Reserved2` | TField |  |  |
| 27 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RESERVED1` | `FsGiWemWorkflowStepsDefinition_Reserved1` | TField |  |  |
| 28 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.LOCAL.REF` | `FsGiWemWorkflowStepsDefinition_LocalRef` |  |  |  |
| 29 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.OVERRIDE` | `FsGiWemWorkflowStepsDefinition_Override` |  |  |  |
| 30 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.RECORD.STATUS` | `FsGiWemWorkflowStepsDefinition_RecordStatus` | String |  |  |
| 31 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.CURR.NO` | `FsGiWemWorkflowStepsDefinition_CurrNo` | String |  |  |
| 32 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.INPUTTER` | `FsGiWemWorkflowStepsDefinition_Inputter` |  |  |  |
| 33 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.DATE.TIME` | `FsGiWemWorkflowStepsDefinition_DateTime` |  |  |  |
| 34 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.AUTHORISER` | `FsGiWemWorkflowStepsDefinition_Authoriser` | String |  |  |
| 35 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.CO.CODE` | `FsGiWemWorkflowStepsDefinition_CoCode` | String |  |  |
| 36 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.DEPT.CODE` | `FsGiWemWorkflowStepsDefinition_DeptCode` | String |  |  |
| 37 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.AUDITOR.CODE` | `FsGiWemWorkflowStepsDefinition_AuditorCode` | String |  |  |
| 38 | `FS.GI.WEM.WORKFLOW.STEPS.DEFINITION.AUDIT.DATE.TIME` | `FsGiWemWorkflowStepsDefinition_AuditDateTime` | String |  |  |
