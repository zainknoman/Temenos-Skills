# FS.GI.APP.AGENT.STRUCTURE.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.AGENT.STRUCTURE.LINK` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.AGENT.STRUCTURE.LINK.PARENT.REF.ID` | `FsGiAppAgentStructureLink_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.AGENT.STRUCTURE.LINK.ORA.ROWID` | `FsGiAppAgentStructureLink_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.AGENT.STRUCTURE.LINK.AGENT.ID` | `FsGiAppAgentStructureLink_AgentId` | TField |  | Agent ID for which structure link is parameterised. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.APP.AGENT.STRUCTURE.LINK.COMMISSION.GROUP` | `FsGiAppAgentStructureLink_CommissionGroup` | TField |  | Agent structure link commission group type. Multifonds DB Column is CGROUP. |
| 5 | `FS.GI.APP.AGENT.STRUCTURE.LINK.SHARE.CLASS.CODE` | `FsGiAppAgentStructureLink_ShareClassCode` | TField |  | Share class code linked to the agent structure link . Multifonds DB Column is TPART. |
| 6 | `FS.GI.APP.AGENT.STRUCTURE.LINK.OPERATION.CODE` | `FsGiAppAgentStructureLink_OperationCode` | TField |  | Operation for which this agent structure link is to be used. Multifonds DB Column is COPERATION. |
| 7 | `FS.GI.APP.AGENT.STRUCTURE.LINK.CONDITION.METHOD` | `FsGiAppAgentStructureLink_ConditionMethod` | TField |  | Condition method required for switch transactions to specify the links between the switched funds. Auto populated for all other transactions. Multifonds DB Column is COND_METHOD. |
| 8 | `FS.GI.APP.AGENT.STRUCTURE.LINK.COMM.STRUCTURE.ID` | `FsGiAppAgentStructureLink_CommStructureId` | TField |  | Commission structure identification that will apply for that agent, commission group and share class. Multifonds DB Column is STRUCTURE_ID. |
| 9 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RESERVED10` | `FsGiAppAgentStructureLink_Reserved10` | TField |  |  |
| 10 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RESERVED9` | `FsGiAppAgentStructureLink_Reserved9` | TField |  |  |
| 11 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RESERVED8` | `FsGiAppAgentStructureLink_Reserved8` | TField |  |  |
| 12 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RESERVED7` | `FsGiAppAgentStructureLink_Reserved7` | TField |  |  |
| 13 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RESERVED6` | `FsGiAppAgentStructureLink_Reserved6` | TField |  |  |
| 14 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RESERVED5` | `FsGiAppAgentStructureLink_Reserved5` | TField |  |  |
| 15 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RESERVED4` | `FsGiAppAgentStructureLink_Reserved4` | TField |  |  |
| 16 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RESERVED3` | `FsGiAppAgentStructureLink_Reserved3` | TField |  |  |
| 17 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RESERVED2` | `FsGiAppAgentStructureLink_Reserved2` | TField |  |  |
| 18 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RESERVED1` | `FsGiAppAgentStructureLink_Reserved1` | TField |  |  |
| 19 | `FS.GI.APP.AGENT.STRUCTURE.LINK.LOCAL.REF` | `FsGiAppAgentStructureLink_LocalRef` |  |  |  |
| 20 | `FS.GI.APP.AGENT.STRUCTURE.LINK.OVERRIDE` | `FsGiAppAgentStructureLink_Override` |  |  |  |
| 21 | `FS.GI.APP.AGENT.STRUCTURE.LINK.RECORD.STATUS` | `FsGiAppAgentStructureLink_RecordStatus` | String |  |  |
| 22 | `FS.GI.APP.AGENT.STRUCTURE.LINK.CURR.NO` | `FsGiAppAgentStructureLink_CurrNo` | String |  |  |
| 23 | `FS.GI.APP.AGENT.STRUCTURE.LINK.INPUTTER` | `FsGiAppAgentStructureLink_Inputter` |  |  |  |
| 24 | `FS.GI.APP.AGENT.STRUCTURE.LINK.DATE.TIME` | `FsGiAppAgentStructureLink_DateTime` |  |  |  |
| 25 | `FS.GI.APP.AGENT.STRUCTURE.LINK.AUTHORISER` | `FsGiAppAgentStructureLink_Authoriser` | String |  |  |
| 26 | `FS.GI.APP.AGENT.STRUCTURE.LINK.CO.CODE` | `FsGiAppAgentStructureLink_CoCode` | String |  |  |
| 27 | `FS.GI.APP.AGENT.STRUCTURE.LINK.DEPT.CODE` | `FsGiAppAgentStructureLink_DeptCode` | String |  |  |
| 28 | `FS.GI.APP.AGENT.STRUCTURE.LINK.AUDITOR.CODE` | `FsGiAppAgentStructureLink_AuditorCode` | String |  |  |
| 29 | `FS.GI.APP.AGENT.STRUCTURE.LINK.AUDIT.DATE.TIME` | `FsGiAppAgentStructureLink_AuditDateTime` | String |  |  |
