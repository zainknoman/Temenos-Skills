# FS.GI.WEM.WORKFLOW.STEPS.STATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.WORKFLOW.STEPS.STATE` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.WORKFLOW.STEPSTATE.ID` | `FsGiWemWorkflowStepsState_WorkflowStepstateId` | TField |  |  |
| 2 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.WORKFLOW.STATE` | `FsGiWemWorkflowStepsState_WorkflowState` |  |  |  |
| 3 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.STEP` | `FsGiWemWorkflowStepsState_Step` |  |  |  |
| 4 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.STEP.NAME` | `FsGiWemWorkflowStepsState_StepName` |  |  |  |
| 5 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.STEP.STATUS` | `FsGiWemWorkflowStepsState_StepStatus` |  |  |  |
| 6 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.STEP.START` | `FsGiWemWorkflowStepsState_StepStart` |  |  |  |
| 7 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.STEP.COMPLETION` | `FsGiWemWorkflowStepsState_StepCompletion` |  |  |  |
| 8 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.STEP.MESSAGE` | `FsGiWemWorkflowStepsState_StepMessage` |  |  |  |
| 9 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.STEP.SEQUENCE` | `FsGiWemWorkflowStepsState_StepSequence` |  |  |  |
| 10 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.SCOPE` | `FsGiWemWorkflowStepsState_Scope` |  |  |  |
| 11 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.DATE.BASIS` | `FsGiWemWorkflowStepsState_DateBasis` |  |  |  |
| 12 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.TRIGGER` | `FsGiWemWorkflowStepsState_Trigger` |  |  |  |
| 13 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.EVENT` | `FsGiWemWorkflowStepsState_Event` |  |  |  |
| 14 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.EVENT.NAME` | `FsGiWemWorkflowStepsState_EventName` |  |  |  |
| 15 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.EVENT.STATUS` | `FsGiWemWorkflowStepsState_EventStatus` |  |  |  |
| 16 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.SUBMIT.STATUS` | `FsGiWemWorkflowStepsState_SubmitStatus` |  |  |  |
| 17 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.CALCULATED.STEP.START` | `FsGiWemWorkflowStepsState_CalculatedStepStart` |  |  |  |
| 18 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.CALCULATED.STEP.COMPLETION` | `FsGiWemWorkflowStepsState_CalculatedStepCompletion` |  |  |  |
| 19 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.CALCULATED.STEP.CUT.OFF` | `FsGiWemWorkflowStepsState_CalculatedStepCutOff` |  |  |  |
| 20 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.INTERVAL` | `FsGiWemWorkflowStepsState_Interval` |  |  |  |
| 21 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.COOLING.OFF` | `FsGiWemWorkflowStepsState_CoolingOff` |  |  |  |
| 22 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.VALIDATION.FLAG` | `FsGiWemWorkflowStepsState_ValidationFlag` |  |  |  |
| 23 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.PAUSE.FLAG` | `FsGiWemWorkflowStepsState_PauseFlag` |  |  |  |
| 24 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.VALIDATION.STATUS` | `FsGiWemWorkflowStepsState_ValidationStatus` |  |  |  |
| 25 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.AUTO.ROLLBACK.EVENT` | `FsGiWemWorkflowStepsState_AutoRollbackEvent` |  |  |  |
| 26 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.ROLLBACK.ALLOWED.FLAGS` | `FsGiWemWorkflowStepsState_RollbackAllowedFlags` |  |  |  |
| 27 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.REVERSE.PROCESSING.FLAG` | `FsGiWemWorkflowStepsState_ReverseProcessingFlag` |  |  |  |
| 28 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.USER.LINK.1` | `FsGiWemWorkflowStepsState_UserLink1` |  |  |  |
| 29 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.USER.LINK.2` | `FsGiWemWorkflowStepsState_UserLink2` |  |  |  |
| 30 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.LOCAL.REF` | `FsGiWemWorkflowStepsState_LocalRef` |  |  |  |
| 31 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.OVERRIDE` | `FsGiWemWorkflowStepsState_Override` |  |  |  |
| 32 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.RECORD.STATUS` | `FsGiWemWorkflowStepsState_RecordStatus` | String |  |  |
| 33 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.CURR.NO` | `FsGiWemWorkflowStepsState_CurrNo` | String |  |  |
| 34 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.INPUTTER` | `FsGiWemWorkflowStepsState_Inputter` |  |  |  |
| 35 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.DATE.TIME` | `FsGiWemWorkflowStepsState_DateTime` |  |  |  |
| 36 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.AUTHORISER` | `FsGiWemWorkflowStepsState_Authoriser` | String |  |  |
| 37 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.CO.CODE` | `FsGiWemWorkflowStepsState_CoCode` | String |  |  |
| 38 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.DEPT.CODE` | `FsGiWemWorkflowStepsState_DeptCode` | String |  |  |
| 39 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.AUDITOR.CODE` | `FsGiWemWorkflowStepsState_AuditorCode` | String |  |  |
| 40 | `FS.GI.WEM.WORKFLOW.STEPS.STATE.AUDIT.DATE.TIME` | `FsGiWemWorkflowStepsState_AuditDateTime` | String |  |  |
