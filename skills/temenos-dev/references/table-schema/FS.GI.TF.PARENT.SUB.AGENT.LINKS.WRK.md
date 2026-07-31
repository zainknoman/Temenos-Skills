# FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK — Table Schema

> Source: `INSERTS/I_F.FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK` in `FS_Distribution.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.PARENT.REF.ID` | `FsGiTfParentSubAgentLinksWrk_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.ORA.ROWID` | `FsGiTfParentSubAgentLinksWrk_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.AGENT.ID` | `FsGiTfParentSubAgentLinksWrk_AgentId` | TField |  | Agent ID whose hierarchy is defined with the level and linkage dates. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.NAME` | `FsGiTfParentSubAgentLinksWrk_Name` | TField |  | Name of the Agent. Multifonds DB Column is NAME. |
| 5 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.TF.PARENT.AGENT.ID` | `FsGiTfParentSubAgentLinksWrk_TfParentAgentId` | TField |  | Parent agent ID linked to the agent. Multifonds DB Column is NOUTLET_PARENT_TF. |
| 6 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.PARENT.NAME` | `FsGiTfParentSubAgentLinksWrk_ParentName` | TField |  | Parent agent name linked to the agent. Multifonds DB Column is PARENT_NAME. |
| 7 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.DISTRIBUTION.LEVEL` | `FsGiTfParentSubAgentLinksWrk_DistributionLevel` | TField |  | Distribution level of the agent linkage. Multifonds DB Column is DISTRIB_LEVEL. |
| 8 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.DATE.FROM` | `FsGiTfParentSubAgentLinksWrk_DateFrom` | TField |  | Child and parent agent linkage start date. Multifonds DB Column is DATE_FROM. |
| 9 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.DATE.TO` | `FsGiTfParentSubAgentLinksWrk_DateTo` | TField |  | Child and parent agent linkage end date. Multifonds DB Column is DATE_TO. |
| 10 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RESERVED10` | `FsGiTfParentSubAgentLinksWrk_Reserved10` | TField |  |  |
| 11 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RESERVED9` | `FsGiTfParentSubAgentLinksWrk_Reserved9` | TField |  |  |
| 12 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RESERVED8` | `FsGiTfParentSubAgentLinksWrk_Reserved8` | TField |  |  |
| 13 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RESERVED7` | `FsGiTfParentSubAgentLinksWrk_Reserved7` | TField |  |  |
| 14 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RESERVED6` | `FsGiTfParentSubAgentLinksWrk_Reserved6` | TField |  |  |
| 15 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RESERVED5` | `FsGiTfParentSubAgentLinksWrk_Reserved5` | TField |  |  |
| 16 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RESERVED4` | `FsGiTfParentSubAgentLinksWrk_Reserved4` | TField |  |  |
| 17 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RESERVED3` | `FsGiTfParentSubAgentLinksWrk_Reserved3` | TField |  |  |
| 18 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RESERVED2` | `FsGiTfParentSubAgentLinksWrk_Reserved2` | TField |  |  |
| 19 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RESERVED1` | `FsGiTfParentSubAgentLinksWrk_Reserved1` | TField |  |  |
| 20 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.LOCAL.REF` | `FsGiTfParentSubAgentLinksWrk_LocalRef` |  |  |  |
| 21 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.OVERRIDE` | `FsGiTfParentSubAgentLinksWrk_Override` |  |  |  |
| 22 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.RECORD.STATUS` | `FsGiTfParentSubAgentLinksWrk_RecordStatus` | String |  |  |
| 23 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.CURR.NO` | `FsGiTfParentSubAgentLinksWrk_CurrNo` | String |  |  |
| 24 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.INPUTTER` | `FsGiTfParentSubAgentLinksWrk_Inputter` |  |  |  |
| 25 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.DATE.TIME` | `FsGiTfParentSubAgentLinksWrk_DateTime` |  |  |  |
| 26 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.AUTHORISER` | `FsGiTfParentSubAgentLinksWrk_Authoriser` | String |  |  |
| 27 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.CO.CODE` | `FsGiTfParentSubAgentLinksWrk_CoCode` | String |  |  |
| 28 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.DEPT.CODE` | `FsGiTfParentSubAgentLinksWrk_DeptCode` | String |  |  |
| 29 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.AUDITOR.CODE` | `FsGiTfParentSubAgentLinksWrk_AuditorCode` | String |  |  |
| 30 | `FS.GI.TF.PARENT.SUB.AGENT.LINKS.WRK.AUDIT.DATE.TIME` | `FsGiTfParentSubAgentLinksWrk_AuditDateTime` | String |  |  |
