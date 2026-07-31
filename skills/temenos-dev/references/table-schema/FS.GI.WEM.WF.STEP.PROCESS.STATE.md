# FS.GI.WEM.WF.STEP.PROCESS.STATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.WF.STEP.PROCESS.STATE` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.WORKFLOW.STEP.PROCESS.STATE.ID` | `FsGiWemWfStepProcessState_WorkflowStepProcessStateId` | TField |  | Unique process state ID. Multifonds DB Column is WORKFLOW.STEP.PROCESS.STATE.ID. |
| 2 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.WORKFLOW.STEP.STATE` | `FsGiWemWfStepProcessState_WorkflowStepState` | TField |  | Workflow occurrence. Multifonds DB Column is WORKFLOW.STEP.STATE. |
| 3 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.PROCESS` | `FsGiWemWfStepProcessState_Process` |  |  |  |
| 4 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.PROCESS.SEQUENCE` | `FsGiWemWfStepProcessState_ProcessSequence` |  |  |  |
| 5 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.PROCESS.START` | `FsGiWemWfStepProcessState_ProcessStart` |  |  |  |
| 6 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.PROCESS.COMPLETION` | `FsGiWemWfStepProcessState_ProcessCompletion` |  |  |  |
| 7 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.PROCESS.STATUS` | `FsGiWemWfStepProcessState_ProcessStatus` |  |  |  |
| 8 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.PROCESS.MESSAGE` | `FsGiWemWfStepProcessState_ProcessMessage` |  |  |  |
| 9 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.PROCESS.CODE` | `FsGiWemWfStepProcessState_ProcessCode` |  |  |  |
| 10 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.FUND.GROUP` | `FsGiWemWfStepProcessState_FundGroup` |  |  |  |
| 11 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.FUND.ID` | `FsGiWemWfStepProcessState_FundId` |  |  |  |
| 12 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.RECORD.STATUS` | `FsGiWemWfStepProcessState_RecordStatus` | String |  |  |
| 13 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.CURR.NO` | `FsGiWemWfStepProcessState_CurrNo` | String |  |  |
| 14 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.INPUTTER` | `FsGiWemWfStepProcessState_Inputter` |  |  |  |
| 15 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.DATE.TIME` | `FsGiWemWfStepProcessState_DateTime` |  |  |  |
| 16 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.AUTHORISER` | `FsGiWemWfStepProcessState_Authoriser` | String |  |  |
| 17 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.CO.CODE` | `FsGiWemWfStepProcessState_CoCode` | String |  |  |
| 18 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.DEPT.CODE` | `FsGiWemWfStepProcessState_DeptCode` | String |  |  |
| 19 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.AUDITOR.CODE` | `FsGiWemWfStepProcessState_AuditorCode` | String |  |  |
| 20 | `FS.GI.WEM.WF.STEP.PROCESS.STATE.AUDIT.DATE.TIME` | `FsGiWemWfStepProcessState_AuditDateTime` | String |  |  |
