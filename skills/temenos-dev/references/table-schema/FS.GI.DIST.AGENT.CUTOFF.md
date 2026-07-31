# FS.GI.DIST.AGENT.CUTOFF — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.CUTOFF` in `FS_AgentStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.CUTOFF.PARENT.REF.ID` | `FsGiDistAgentCutoff_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.CUTOFF.ORA.ROWID` | `FsGiDistAgentCutoff_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.CUTOFF.AGENT.ID` | `FsGiDistAgentCutoff_AgentId` | TField |  | Agent Internal Id. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.DIST.AGENT.CUTOFF.TA.FUND.ID` | `FsGiDistAgentCutoff_TaFundId` | TField |  | Fund linked to the agent for which the cut off delay is applicable. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.DIST.AGENT.CUTOFF.SHARE.CLASS.CODE` | `FsGiDistAgentCutoff_ShareClassCode` | TField |  | Fund share class code for which the cut off delay is applicable. Multifonds DB Column is TPART. |
| 6 | `FS.GI.DIST.AGENT.CUTOFF.OPERATION.CODE` | `FsGiDistAgentCutoff_OperationCode` | TField |  | Operation code for which the cut off delay is applicable. Multifonds DB Column is COPERATION. |
| 7 | `FS.GI.DIST.AGENT.CUTOFF.DELAY.HOURS` | `FsGiDistAgentCutoff_DelayHours` | TField |  | Cut-off time delay in hours. It is allowed up to 99 hours. Multifonds DB Column is DELAY. |
| 8 | `FS.GI.DIST.AGENT.CUTOFF.AGENT.DELAY.ID` | `FsGiDistAgentCutoff_AgentDelayId` | TField |  | Unique internal identifier for agent exceptional order cut-off record. Multifonds DB Column is INTERNAL_ID. |
| 9 | `FS.GI.DIST.AGENT.CUTOFF.FUND.ID` | `FsGiDistAgentCutoff_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 10 | `FS.GI.DIST.AGENT.CUTOFF.CLASS.CURRENCY` | `FsGiDistAgentCutoff_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 11 | `FS.GI.DIST.AGENT.CUTOFF.RESERVED10` | `FsGiDistAgentCutoff_Reserved10` | TField |  |  |
| 12 | `FS.GI.DIST.AGENT.CUTOFF.RESERVED9` | `FsGiDistAgentCutoff_Reserved9` | TField |  |  |
| 13 | `FS.GI.DIST.AGENT.CUTOFF.RESERVED8` | `FsGiDistAgentCutoff_Reserved8` | TField |  |  |
| 14 | `FS.GI.DIST.AGENT.CUTOFF.RESERVED7` | `FsGiDistAgentCutoff_Reserved7` | TField |  |  |
| 15 | `FS.GI.DIST.AGENT.CUTOFF.RESERVED6` | `FsGiDistAgentCutoff_Reserved6` | TField |  |  |
| 16 | `FS.GI.DIST.AGENT.CUTOFF.RESERVED5` | `FsGiDistAgentCutoff_Reserved5` | TField |  |  |
| 17 | `FS.GI.DIST.AGENT.CUTOFF.RESERVED4` | `FsGiDistAgentCutoff_Reserved4` | TField |  |  |
| 18 | `FS.GI.DIST.AGENT.CUTOFF.RESERVED3` | `FsGiDistAgentCutoff_Reserved3` | TField |  |  |
| 19 | `FS.GI.DIST.AGENT.CUTOFF.RESERVED2` | `FsGiDistAgentCutoff_Reserved2` | TField |  |  |
| 20 | `FS.GI.DIST.AGENT.CUTOFF.RESERVED1` | `FsGiDistAgentCutoff_Reserved1` | TField |  |  |
| 21 | `FS.GI.DIST.AGENT.CUTOFF.LOCAL.REF` | `FsGiDistAgentCutoff_LocalRef` |  |  |  |
| 22 | `FS.GI.DIST.AGENT.CUTOFF.OVERRIDE` | `FsGiDistAgentCutoff_Override` |  |  |  |
| 23 | `FS.GI.DIST.AGENT.CUTOFF.RECORD.STATUS` | `FsGiDistAgentCutoff_RecordStatus` | String |  |  |
| 24 | `FS.GI.DIST.AGENT.CUTOFF.CURR.NO` | `FsGiDistAgentCutoff_CurrNo` | String |  |  |
| 25 | `FS.GI.DIST.AGENT.CUTOFF.INPUTTER` | `FsGiDistAgentCutoff_Inputter` |  |  |  |
| 26 | `FS.GI.DIST.AGENT.CUTOFF.DATE.TIME` | `FsGiDistAgentCutoff_DateTime` |  |  |  |
| 27 | `FS.GI.DIST.AGENT.CUTOFF.AUTHORISER` | `FsGiDistAgentCutoff_Authoriser` | String |  |  |
| 28 | `FS.GI.DIST.AGENT.CUTOFF.CO.CODE` | `FsGiDistAgentCutoff_CoCode` | String |  |  |
| 29 | `FS.GI.DIST.AGENT.CUTOFF.DEPT.CODE` | `FsGiDistAgentCutoff_DeptCode` | String |  |  |
| 30 | `FS.GI.DIST.AGENT.CUTOFF.AUDITOR.CODE` | `FsGiDistAgentCutoff_AuditorCode` | String |  |  |
| 31 | `FS.GI.DIST.AGENT.CUTOFF.AUDIT.DATE.TIME` | `FsGiDistAgentCutoff_AuditDateTime` | String |  |  |
