# FS.AGENT.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.AGENT.GROUP` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.AGENT.GROUP.DESCRIPTION` | `FsAgentGroup_Description` |  |  |  |
| 2 | `FS.AGENT.GROUP.FILTER.KEY` | `FsAgentGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.AGENT.GROUP.RECORD.ID` | `FsAgentGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.AGENT.GROUP.RESERVED10` | `FsAgentGroup_Reserved10` | TField |  |  |
| 5 | `FS.AGENT.GROUP.RESERVED9` | `FsAgentGroup_Reserved9` | TField |  |  |
| 6 | `FS.AGENT.GROUP.RESERVED8` | `FsAgentGroup_Reserved8` | TField |  |  |
| 7 | `FS.AGENT.GROUP.RESERVED7` | `FsAgentGroup_Reserved7` | TField |  |  |
| 8 | `FS.AGENT.GROUP.RESERVED6` | `FsAgentGroup_Reserved6` | TField |  |  |
| 9 | `FS.AGENT.GROUP.RESERVED5` | `FsAgentGroup_Reserved5` | TField |  |  |
| 10 | `FS.AGENT.GROUP.RESERVED4` | `FsAgentGroup_Reserved4` | TField |  |  |
| 11 | `FS.AGENT.GROUP.RESERVED3` | `FsAgentGroup_Reserved3` | TField |  |  |
| 12 | `FS.AGENT.GROUP.RESERVED2` | `FsAgentGroup_Reserved2` | TField |  |  |
| 13 | `FS.AGENT.GROUP.RESERVED1` | `FsAgentGroup_Reserved1` | TField |  |  |
| 14 | `FS.AGENT.GROUP.LOCAL.REF` | `FsAgentGroup_LocalRef` |  |  |  |
| 15 | `FS.AGENT.GROUP.OVERRIDE` | `FsAgentGroup_Override` |  |  |  |
| 16 | `FS.AGENT.GROUP.RECORD.STATUS` | `FsAgentGroup_RecordStatus` | String |  |  |
| 17 | `FS.AGENT.GROUP.CURR.NO` | `FsAgentGroup_CurrNo` | String |  |  |
| 18 | `FS.AGENT.GROUP.INPUTTER` | `FsAgentGroup_Inputter` |  |  |  |
| 19 | `FS.AGENT.GROUP.DATE.TIME` | `FsAgentGroup_DateTime` |  |  |  |
| 20 | `FS.AGENT.GROUP.AUTHORISER` | `FsAgentGroup_Authoriser` | String |  |  |
| 21 | `FS.AGENT.GROUP.CO.CODE` | `FsAgentGroup_CoCode` | String |  |  |
| 22 | `FS.AGENT.GROUP.DEPT.CODE` | `FsAgentGroup_DeptCode` | String |  |  |
| 23 | `FS.AGENT.GROUP.AUDITOR.CODE` | `FsAgentGroup_AuditorCode` | String |  |  |
| 24 | `FS.AGENT.GROUP.AUDIT.DATE.TIME` | `FsAgentGroup_AuditDateTime` | String |  |  |
