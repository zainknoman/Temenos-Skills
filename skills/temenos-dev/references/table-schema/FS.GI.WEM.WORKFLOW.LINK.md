# FS.GI.WEM.WORKFLOW.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.WORKFLOW.LINK` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.WORKFLOW.LINK.WORKFLOW.ID` | `FsGiWemWorkflowLink_WorkflowId` | TField |  | Linked workflow ID Multifonds DB Column is WORKFLOW.ID. |
| 2 | `FS.GI.WEM.WORKFLOW.LINK.ENTITY.TYPE` | `FsGiWemWorkflowLink_EntityType` |  |  |  |
| 3 | `FS.GI.WEM.WORKFLOW.LINK.ENTITY.ID` | `FsGiWemWorkflowLink_EntityId` |  |  |  |
| 4 | `FS.GI.WEM.WORKFLOW.LINK.RESERVED10` | `FsGiWemWorkflowLink_Reserved10` | TField |  |  |
| 5 | `FS.GI.WEM.WORKFLOW.LINK.RESERVED9` | `FsGiWemWorkflowLink_Reserved9` | TField |  |  |
| 6 | `FS.GI.WEM.WORKFLOW.LINK.RESERVED8` | `FsGiWemWorkflowLink_Reserved8` | TField |  |  |
| 7 | `FS.GI.WEM.WORKFLOW.LINK.RESERVED7` | `FsGiWemWorkflowLink_Reserved7` | TField |  |  |
| 8 | `FS.GI.WEM.WORKFLOW.LINK.RESERVED6` | `FsGiWemWorkflowLink_Reserved6` | TField |  |  |
| 9 | `FS.GI.WEM.WORKFLOW.LINK.RESERVED5` | `FsGiWemWorkflowLink_Reserved5` | TField |  |  |
| 10 | `FS.GI.WEM.WORKFLOW.LINK.RESERVED4` | `FsGiWemWorkflowLink_Reserved4` | TField |  |  |
| 11 | `FS.GI.WEM.WORKFLOW.LINK.RESERVED3` | `FsGiWemWorkflowLink_Reserved3` | TField |  |  |
| 12 | `FS.GI.WEM.WORKFLOW.LINK.RESERVED2` | `FsGiWemWorkflowLink_Reserved2` | TField |  |  |
| 13 | `FS.GI.WEM.WORKFLOW.LINK.RESERVED1` | `FsGiWemWorkflowLink_Reserved1` | TField |  |  |
| 14 | `FS.GI.WEM.WORKFLOW.LINK.LOCAL.REF` | `FsGiWemWorkflowLink_LocalRef` |  |  |  |
| 15 | `FS.GI.WEM.WORKFLOW.LINK.OVERRIDE` | `FsGiWemWorkflowLink_Override` |  |  |  |
| 16 | `FS.GI.WEM.WORKFLOW.LINK.RECORD.STATUS` | `FsGiWemWorkflowLink_RecordStatus` | String |  |  |
| 17 | `FS.GI.WEM.WORKFLOW.LINK.CURR.NO` | `FsGiWemWorkflowLink_CurrNo` | String |  |  |
| 18 | `FS.GI.WEM.WORKFLOW.LINK.INPUTTER` | `FsGiWemWorkflowLink_Inputter` |  |  |  |
| 19 | `FS.GI.WEM.WORKFLOW.LINK.DATE.TIME` | `FsGiWemWorkflowLink_DateTime` |  |  |  |
| 20 | `FS.GI.WEM.WORKFLOW.LINK.AUTHORISER` | `FsGiWemWorkflowLink_Authoriser` | String |  |  |
| 21 | `FS.GI.WEM.WORKFLOW.LINK.CO.CODE` | `FsGiWemWorkflowLink_CoCode` | String |  |  |
| 22 | `FS.GI.WEM.WORKFLOW.LINK.DEPT.CODE` | `FsGiWemWorkflowLink_DeptCode` | String |  |  |
| 23 | `FS.GI.WEM.WORKFLOW.LINK.AUDITOR.CODE` | `FsGiWemWorkflowLink_AuditorCode` | String |  |  |
| 24 | `FS.GI.WEM.WORKFLOW.LINK.AUDIT.DATE.TIME` | `FsGiWemWorkflowLink_AuditDateTime` | String |  |  |
