# FS.GI.DIST.AGENT.VALUE.DATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.VALUE.DATE` in `FS_AgentStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.VALUE.DATE.PARENT.REF.ID` | `FsGiDistAgentValueDate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.VALUE.DATE.ORA.ROWID` | `FsGiDistAgentValueDate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.VALUE.DATE.AGENT.ID` | `FsGiDistAgentValueDate_AgentId` | TField |  | Agent Internal ID. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.DIST.AGENT.VALUE.DATE.TA.FUND.ID` | `FsGiDistAgentValueDate_TaFundId` | TField |  | Fund internal ID linked to the agent. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.DIST.AGENT.VALUE.DATE.SHARE.CLASS.CODE` | `FsGiDistAgentValueDate_ShareClassCode` | TField |  | Fund share class linked to the agent. Multifonds DB Column is TPART. |
| 6 | `FS.GI.DIST.AGENT.VALUE.DATE.OPERATION.CODE` | `FsGiDistAgentValueDate_OperationCode` | TField |  | Operation code for which valude date setup is applicable. Multifonds DB Column is COPERATION. |
| 7 | `FS.GI.DIST.AGENT.VALUE.DATE.VALUE.DATE.NUMBER.OF.DAYS` | `FsGiDistAgentValueDate_ValueDateNumberOfDays` | TField |  | Number of days to be applied for value date calculation. Multifonds DB Column is NUMBER_DAYS. |
| 8 | `FS.GI.DIST.AGENT.VALUE.DATE.VALUE.DATE.METHOD` | `FsGiDistAgentValueDate_ValueDateMethod` | TField |  | Value date method to be applied for value date calculation. Multifonds DB Column is WORKING_DAY. |
| 9 | `FS.GI.DIST.AGENT.VALUE.DATE.AGENT.VALUE.DATE.ID` | `FsGiDistAgentValueDate_AgentValueDateId` | TField |  | Unique internal identifier for agent value date record. Multifonds DB Column is INTERNAL_ID. |
| 10 | `FS.GI.DIST.AGENT.VALUE.DATE.FUND.ID` | `FsGiDistAgentValueDate_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 11 | `FS.GI.DIST.AGENT.VALUE.DATE.CLASS.CURRENCY` | `FsGiDistAgentValueDate_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 12 | `FS.GI.DIST.AGENT.VALUE.DATE.RESERVED10` | `FsGiDistAgentValueDate_Reserved10` | TField |  |  |
| 13 | `FS.GI.DIST.AGENT.VALUE.DATE.RESERVED9` | `FsGiDistAgentValueDate_Reserved9` | TField |  |  |
| 14 | `FS.GI.DIST.AGENT.VALUE.DATE.RESERVED8` | `FsGiDistAgentValueDate_Reserved8` | TField |  |  |
| 15 | `FS.GI.DIST.AGENT.VALUE.DATE.RESERVED7` | `FsGiDistAgentValueDate_Reserved7` | TField |  |  |
| 16 | `FS.GI.DIST.AGENT.VALUE.DATE.RESERVED6` | `FsGiDistAgentValueDate_Reserved6` | TField |  |  |
| 17 | `FS.GI.DIST.AGENT.VALUE.DATE.RESERVED5` | `FsGiDistAgentValueDate_Reserved5` | TField |  |  |
| 18 | `FS.GI.DIST.AGENT.VALUE.DATE.RESERVED4` | `FsGiDistAgentValueDate_Reserved4` | TField |  |  |
| 19 | `FS.GI.DIST.AGENT.VALUE.DATE.RESERVED3` | `FsGiDistAgentValueDate_Reserved3` | TField |  |  |
| 20 | `FS.GI.DIST.AGENT.VALUE.DATE.RESERVED2` | `FsGiDistAgentValueDate_Reserved2` | TField |  |  |
| 21 | `FS.GI.DIST.AGENT.VALUE.DATE.RESERVED1` | `FsGiDistAgentValueDate_Reserved1` | TField |  |  |
| 22 | `FS.GI.DIST.AGENT.VALUE.DATE.LOCAL.REF` | `FsGiDistAgentValueDate_LocalRef` |  |  |  |
| 23 | `FS.GI.DIST.AGENT.VALUE.DATE.OVERRIDE` | `FsGiDistAgentValueDate_Override` |  |  |  |
| 24 | `FS.GI.DIST.AGENT.VALUE.DATE.RECORD.STATUS` | `FsGiDistAgentValueDate_RecordStatus` | String |  |  |
| 25 | `FS.GI.DIST.AGENT.VALUE.DATE.CURR.NO` | `FsGiDistAgentValueDate_CurrNo` | String |  |  |
| 26 | `FS.GI.DIST.AGENT.VALUE.DATE.INPUTTER` | `FsGiDistAgentValueDate_Inputter` |  |  |  |
| 27 | `FS.GI.DIST.AGENT.VALUE.DATE.DATE.TIME` | `FsGiDistAgentValueDate_DateTime` |  |  |  |
| 28 | `FS.GI.DIST.AGENT.VALUE.DATE.AUTHORISER` | `FsGiDistAgentValueDate_Authoriser` | String |  |  |
| 29 | `FS.GI.DIST.AGENT.VALUE.DATE.CO.CODE` | `FsGiDistAgentValueDate_CoCode` | String |  |  |
| 30 | `FS.GI.DIST.AGENT.VALUE.DATE.DEPT.CODE` | `FsGiDistAgentValueDate_DeptCode` | String |  |  |
| 31 | `FS.GI.DIST.AGENT.VALUE.DATE.AUDITOR.CODE` | `FsGiDistAgentValueDate_AuditorCode` | String |  |  |
| 32 | `FS.GI.DIST.AGENT.VALUE.DATE.AUDIT.DATE.TIME` | `FsGiDistAgentValueDate_AuditDateTime` | String |  |  |
