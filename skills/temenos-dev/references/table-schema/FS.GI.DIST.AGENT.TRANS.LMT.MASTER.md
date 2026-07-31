# FS.GI.DIST.AGENT.TRANS.LMT.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.TRANS.LMT.MASTER` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.PARENT.REF.ID` | `FsGiDistAgentTransLmtMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.ORA.ROWID` | `FsGiDistAgentTransLmtMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.AGENT.ID` | `FsGiDistAgentTransLmtMaster_AgentId` | TField |  | Agent internal ID. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.LIMIT.CURRENCY` | `FsGiDistAgentTransLmtMaster_LimitCurrency` | TField |  | Transaction limit currency code (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CMON. |
| 5 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RESERVED10` | `FsGiDistAgentTransLmtMaster_Reserved10` | TField |  |  |
| 6 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RESERVED9` | `FsGiDistAgentTransLmtMaster_Reserved9` | TField |  |  |
| 7 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RESERVED8` | `FsGiDistAgentTransLmtMaster_Reserved8` | TField |  |  |
| 8 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RESERVED7` | `FsGiDistAgentTransLmtMaster_Reserved7` | TField |  |  |
| 9 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RESERVED6` | `FsGiDistAgentTransLmtMaster_Reserved6` | TField |  |  |
| 10 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RESERVED5` | `FsGiDistAgentTransLmtMaster_Reserved5` | TField |  |  |
| 11 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RESERVED4` | `FsGiDistAgentTransLmtMaster_Reserved4` | TField |  |  |
| 12 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RESERVED3` | `FsGiDistAgentTransLmtMaster_Reserved3` | TField |  |  |
| 13 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RESERVED2` | `FsGiDistAgentTransLmtMaster_Reserved2` | TField |  |  |
| 14 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RESERVED1` | `FsGiDistAgentTransLmtMaster_Reserved1` | TField |  |  |
| 15 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.LOCAL.REF` | `FsGiDistAgentTransLmtMaster_LocalRef` |  |  |  |
| 16 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.OVERRIDE` | `FsGiDistAgentTransLmtMaster_Override` |  |  |  |
| 17 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.RECORD.STATUS` | `FsGiDistAgentTransLmtMaster_RecordStatus` | String |  |  |
| 18 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.CURR.NO` | `FsGiDistAgentTransLmtMaster_CurrNo` | String |  |  |
| 19 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.INPUTTER` | `FsGiDistAgentTransLmtMaster_Inputter` |  |  |  |
| 20 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.DATE.TIME` | `FsGiDistAgentTransLmtMaster_DateTime` |  |  |  |
| 21 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.AUTHORISER` | `FsGiDistAgentTransLmtMaster_Authoriser` | String |  |  |
| 22 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.CO.CODE` | `FsGiDistAgentTransLmtMaster_CoCode` | String |  |  |
| 23 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.DEPT.CODE` | `FsGiDistAgentTransLmtMaster_DeptCode` | String |  |  |
| 24 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.AUDITOR.CODE` | `FsGiDistAgentTransLmtMaster_AuditorCode` | String |  |  |
| 25 | `FS.GI.DIST.AGENT.TRANS.LMT.MASTER.AUDIT.DATE.TIME` | `FsGiDistAgentTransLmtMaster_AuditDateTime` | String |  |  |
