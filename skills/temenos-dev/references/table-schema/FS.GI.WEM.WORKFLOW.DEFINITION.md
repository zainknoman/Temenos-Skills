# FS.GI.WEM.WORKFLOW.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.WORKFLOW.DEFINITION` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.WORKFLOW.DEFINITION.WORKFLOW.ID` | `FsGiWemWorkflowDefinition_WorkflowId` | TField |  | Unique workflow ID. Multifonds DB Column is WORKFLOW.ID. |
| 2 | `FS.GI.WEM.WORKFLOW.DEFINITION.WORKFLOW.TYPE` | `FsGiWemWorkflowDefinition_WorkflowType` | TField |  | Workflow type Multifonds DB Column is WORKFLOW.TYPE. |
| 3 | `FS.GI.WEM.WORKFLOW.DEFINITION.WORKFLOW.NAME` | `FsGiWemWorkflowDefinition_WorkflowName` | TField |  | Name of the Workflow Multifonds DB Column is WORKFLOW.NAME. |
| 4 | `FS.GI.WEM.WORKFLOW.DEFINITION.RESERVED10` | `FsGiWemWorkflowDefinition_Reserved10` | TField |  |  |
| 5 | `FS.GI.WEM.WORKFLOW.DEFINITION.RESERVED9` | `FsGiWemWorkflowDefinition_Reserved9` | TField |  |  |
| 6 | `FS.GI.WEM.WORKFLOW.DEFINITION.RESERVED8` | `FsGiWemWorkflowDefinition_Reserved8` | TField |  |  |
| 7 | `FS.GI.WEM.WORKFLOW.DEFINITION.RESERVED7` | `FsGiWemWorkflowDefinition_Reserved7` | TField |  |  |
| 8 | `FS.GI.WEM.WORKFLOW.DEFINITION.RESERVED6` | `FsGiWemWorkflowDefinition_Reserved6` | TField |  |  |
| 9 | `FS.GI.WEM.WORKFLOW.DEFINITION.RESERVED5` | `FsGiWemWorkflowDefinition_Reserved5` | TField |  |  |
| 10 | `FS.GI.WEM.WORKFLOW.DEFINITION.RESERVED4` | `FsGiWemWorkflowDefinition_Reserved4` | TField |  |  |
| 11 | `FS.GI.WEM.WORKFLOW.DEFINITION.RESERVED3` | `FsGiWemWorkflowDefinition_Reserved3` | TField |  |  |
| 12 | `FS.GI.WEM.WORKFLOW.DEFINITION.RESERVED2` | `FsGiWemWorkflowDefinition_Reserved2` | TField |  |  |
| 13 | `FS.GI.WEM.WORKFLOW.DEFINITION.RESERVED1` | `FsGiWemWorkflowDefinition_Reserved1` | TField |  |  |
| 14 | `FS.GI.WEM.WORKFLOW.DEFINITION.LOCAL.REF` | `FsGiWemWorkflowDefinition_LocalRef` |  |  |  |
| 15 | `FS.GI.WEM.WORKFLOW.DEFINITION.OVERRIDE` | `FsGiWemWorkflowDefinition_Override` |  |  |  |
| 16 | `FS.GI.WEM.WORKFLOW.DEFINITION.RECORD.STATUS` | `FsGiWemWorkflowDefinition_RecordStatus` | String |  |  |
| 17 | `FS.GI.WEM.WORKFLOW.DEFINITION.CURR.NO` | `FsGiWemWorkflowDefinition_CurrNo` | String |  |  |
| 18 | `FS.GI.WEM.WORKFLOW.DEFINITION.INPUTTER` | `FsGiWemWorkflowDefinition_Inputter` |  |  |  |
| 19 | `FS.GI.WEM.WORKFLOW.DEFINITION.DATE.TIME` | `FsGiWemWorkflowDefinition_DateTime` |  |  |  |
| 20 | `FS.GI.WEM.WORKFLOW.DEFINITION.AUTHORISER` | `FsGiWemWorkflowDefinition_Authoriser` | String |  |  |
| 21 | `FS.GI.WEM.WORKFLOW.DEFINITION.CO.CODE` | `FsGiWemWorkflowDefinition_CoCode` | String |  |  |
| 22 | `FS.GI.WEM.WORKFLOW.DEFINITION.DEPT.CODE` | `FsGiWemWorkflowDefinition_DeptCode` | String |  |  |
| 23 | `FS.GI.WEM.WORKFLOW.DEFINITION.AUDITOR.CODE` | `FsGiWemWorkflowDefinition_AuditorCode` | String |  |  |
| 24 | `FS.GI.WEM.WORKFLOW.DEFINITION.AUDIT.DATE.TIME` | `FsGiWemWorkflowDefinition_AuditDateTime` | String |  |  |
