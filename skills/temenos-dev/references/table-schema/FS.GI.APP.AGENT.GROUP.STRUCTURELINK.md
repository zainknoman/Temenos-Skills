# FS.GI.APP.AGENT.GROUP.STRUCTURELINK — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.AGENT.GROUP.STRUCTURELINK` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.PARENT.REF.ID` | `FsGiAppAgentGroupStructurelink_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.ORA.ROWID` | `FsGiAppAgentGroupStructurelink_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.AGENT.GROUP` | `FsGiAppAgentGroupStructurelink_AgentGroup` | TField |  | Agent group ID to be part of the distribution. Multifonds DB Column is GROUP_COM. |
| 4 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.COMMISSION.GROUP` | `FsGiAppAgentGroupStructurelink_CommissionGroup` | TField |  | Group structure link commission group type. Multifonds DB Column is CGROUP. |
| 5 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.SHARE.CLASS.CODE` | `FsGiAppAgentGroupStructurelink_ShareClassCode` | TField |  | Share class code linked to the group structure link . Multifonds DB Column is TPART. |
| 6 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.OPERATION.CODE` | `FsGiAppAgentGroupStructurelink_OperationCode` | TField |  | Operation for which this commission group structure link is to be used. Multifonds DB Column is COPERATION. |
| 7 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.CONDITION.METHOD` | `FsGiAppAgentGroupStructurelink_ConditionMethod` | TField |  | Condition method required for switch transactions to specify the links between the switched funds. Auto populated for all other transactions. Multifonds DB Column is COND_METHOD. |
| 8 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.COMM.STRUCTURE.ID` | `FsGiAppAgentGroupStructurelink_CommStructureId` | TField |  | Commission structure identification that will apply for that agent, commission group and share class. Multifonds DB Column is STRUCTURE_ID. |
| 9 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.AGENT.GROUP.TYPE` | `FsGiAppAgentGroupStructurelink_AgentGroupType` | TField |  | Agent group commission type. Multifonds DB Column is GROUP_COM_TYPE. |
| 10 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RESERVED10` | `FsGiAppAgentGroupStructurelink_Reserved10` | TField |  |  |
| 11 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RESERVED9` | `FsGiAppAgentGroupStructurelink_Reserved9` | TField |  |  |
| 12 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RESERVED8` | `FsGiAppAgentGroupStructurelink_Reserved8` | TField |  |  |
| 13 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RESERVED7` | `FsGiAppAgentGroupStructurelink_Reserved7` | TField |  |  |
| 14 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RESERVED6` | `FsGiAppAgentGroupStructurelink_Reserved6` | TField |  |  |
| 15 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RESERVED5` | `FsGiAppAgentGroupStructurelink_Reserved5` | TField |  |  |
| 16 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RESERVED4` | `FsGiAppAgentGroupStructurelink_Reserved4` | TField |  |  |
| 17 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RESERVED3` | `FsGiAppAgentGroupStructurelink_Reserved3` | TField |  |  |
| 18 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RESERVED2` | `FsGiAppAgentGroupStructurelink_Reserved2` | TField |  |  |
| 19 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RESERVED1` | `FsGiAppAgentGroupStructurelink_Reserved1` | TField |  |  |
| 20 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.LOCAL.REF` | `FsGiAppAgentGroupStructurelink_LocalRef` |  |  |  |
| 21 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.OVERRIDE` | `FsGiAppAgentGroupStructurelink_Override` |  |  |  |
| 22 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.RECORD.STATUS` | `FsGiAppAgentGroupStructurelink_RecordStatus` | String |  |  |
| 23 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.CURR.NO` | `FsGiAppAgentGroupStructurelink_CurrNo` | String |  |  |
| 24 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.INPUTTER` | `FsGiAppAgentGroupStructurelink_Inputter` |  |  |  |
| 25 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.DATE.TIME` | `FsGiAppAgentGroupStructurelink_DateTime` |  |  |  |
| 26 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.AUTHORISER` | `FsGiAppAgentGroupStructurelink_Authoriser` | String |  |  |
| 27 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.CO.CODE` | `FsGiAppAgentGroupStructurelink_CoCode` | String |  |  |
| 28 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.DEPT.CODE` | `FsGiAppAgentGroupStructurelink_DeptCode` | String |  |  |
| 29 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.AUDITOR.CODE` | `FsGiAppAgentGroupStructurelink_AuditorCode` | String |  |  |
| 30 | `FS.GI.APP.AGENT.GROUP.STRUCTURELINK.AUDIT.DATE.TIME` | `FsGiAppAgentGroupStructurelink_AuditDateTime` | String |  |  |
