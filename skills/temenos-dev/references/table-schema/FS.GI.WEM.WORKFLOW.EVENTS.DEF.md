# FS.GI.WEM.WORKFLOW.EVENTS.DEF — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.WORKFLOW.EVENTS.DEF` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.WORKFLOW.ID` | `FsGiWemWorkflowEventsDef_WorkflowId` | TField |  | Linked workflow ID Multifonds DB Column is WORKFLOW.ID. |
| 2 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.STEP.SEQUENCE` | `FsGiWemWorkflowEventsDef_StepSequence` |  |  |  |
| 3 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.ACTION` | `FsGiWemWorkflowEventsDef_Action` |  |  |  |
| 4 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.EVENT.ID` | `FsGiWemWorkflowEventsDef_EventId` |  |  |  |
| 5 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RESERVED10` | `FsGiWemWorkflowEventsDef_Reserved10` | TField |  |  |
| 6 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RESERVED9` | `FsGiWemWorkflowEventsDef_Reserved9` | TField |  |  |
| 7 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RESERVED8` | `FsGiWemWorkflowEventsDef_Reserved8` | TField |  |  |
| 8 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RESERVED7` | `FsGiWemWorkflowEventsDef_Reserved7` | TField |  |  |
| 9 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RESERVED6` | `FsGiWemWorkflowEventsDef_Reserved6` | TField |  |  |
| 10 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RESERVED5` | `FsGiWemWorkflowEventsDef_Reserved5` | TField |  |  |
| 11 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RESERVED4` | `FsGiWemWorkflowEventsDef_Reserved4` | TField |  |  |
| 12 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RESERVED3` | `FsGiWemWorkflowEventsDef_Reserved3` | TField |  |  |
| 13 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RESERVED2` | `FsGiWemWorkflowEventsDef_Reserved2` | TField |  |  |
| 14 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RESERVED1` | `FsGiWemWorkflowEventsDef_Reserved1` | TField |  |  |
| 15 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.LOCAL.REF` | `FsGiWemWorkflowEventsDef_LocalRef` |  |  |  |
| 16 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.OVERRIDE` | `FsGiWemWorkflowEventsDef_Override` |  |  |  |
| 17 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.RECORD.STATUS` | `FsGiWemWorkflowEventsDef_RecordStatus` | String |  |  |
| 18 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.CURR.NO` | `FsGiWemWorkflowEventsDef_CurrNo` | String |  |  |
| 19 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.INPUTTER` | `FsGiWemWorkflowEventsDef_Inputter` |  |  |  |
| 20 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.DATE.TIME` | `FsGiWemWorkflowEventsDef_DateTime` |  |  |  |
| 21 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.AUTHORISER` | `FsGiWemWorkflowEventsDef_Authoriser` | String |  |  |
| 22 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.CO.CODE` | `FsGiWemWorkflowEventsDef_CoCode` | String |  |  |
| 23 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.DEPT.CODE` | `FsGiWemWorkflowEventsDef_DeptCode` | String |  |  |
| 24 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.AUDITOR.CODE` | `FsGiWemWorkflowEventsDef_AuditorCode` | String |  |  |
| 25 | `FS.GI.WEM.WORKFLOW.EVENTS.DEF.AUDIT.DATE.TIME` | `FsGiWemWorkflowEventsDef_AuditDateTime` | String |  |  |
