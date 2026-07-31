# FS.GI.DIST.AGENT.COMM — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.COMM` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.COMM.PARENT.REF.ID` | `FsGiDistAgentComm_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.COMM.ORA.ROWID` | `FsGiDistAgentComm_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.COMM.AGENT.ID` | `FsGiDistAgentComm_AgentId` | TField |  | Agent internal Id. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.DIST.AGENT.COMM.FEE.TYPE` | `FsGiDistAgentComm_FeeType` | TField |  | It specifies the commission fee type code. Multifonds DB Column is FEE_TYPE. |
| 5 | `FS.GI.DIST.AGENT.COMM.LEGAL.ENTITY.ID` | `FsGiDistAgentComm_LegalEntityId` | TField |  | Legal fund entity internal Id linked to the agent commission setup. Multifonds DB Column is NTFC. |
| 6 | `FS.GI.DIST.AGENT.COMM.FUND.ID` | `FsGiDistAgentComm_FundId` | TField |  | Fund intenral Id linked to the agent commissions setup. Multifonds DB Column is NPTF. |
| 7 | `FS.GI.DIST.AGENT.COMM.SHARE.CLASS.CODE` | `FsGiDistAgentComm_ShareClassCode` | TField |  | Fund share class linked to the agent commission setup. Multifonds DB Column is TPART. |
| 8 | `FS.GI.DIST.AGENT.COMM.FEE.PERIOD.TYPE` | `FsGiDistAgentComm_FeePeriodType` | TField |  | Commission Period fee type applicable. Multifonds DB Column is FEE_PERIOD_TYPE. |
| 9 | `FS.GI.DIST.AGENT.COMM.TOTAL.REGISTER` | `FsGiDistAgentComm_TotalRegister` | TField |  | Total number of registers linked. Multifonds DB Column is TOT_REGISTER. |
| 10 | `FS.GI.DIST.AGENT.COMM.TOTAL.CONTRACTS` | `FsGiDistAgentComm_TotalContracts` | TField |  | Total number of contracts linked. Multifonds DB Column is TOT_CONTRACTS. |
| 11 | `FS.GI.DIST.AGENT.COMM.OPERATION.CODE` | `FsGiDistAgentComm_OperationCode` | TField |  | Operation code for which the fee is applicable. Multifonds DB Column is COPERATION. |
| 12 | `FS.GI.DIST.AGENT.COMM.COMM.CONDITION` | `FsGiDistAgentComm_CommCondition` | TField |  | Commission condition method. Multifonds DB Column is CONDITION. |
| 13 | `FS.GI.DIST.AGENT.COMM.PERCENTAGE` | `FsGiDistAgentComm_Percentage` | TField |  | Commission percentage. Multifonds DB Column is PERCENTAGE. |
| 14 | `FS.GI.DIST.AGENT.COMM.AMOUNT` | `FsGiDistAgentComm_Amount` | TField |  | Commission amount. Multifonds DB Column is AMOUNT. |
| 15 | `FS.GI.DIST.AGENT.COMM.SCALE.CODE` | `FsGiDistAgentComm_ScaleCode` | TField |  | Commission scale applicable. Multifonds DB Column is SCALE_CODE. |
| 16 | `FS.GI.DIST.AGENT.COMM.RESERVED10` | `FsGiDistAgentComm_Reserved10` | TField |  |  |
| 17 | `FS.GI.DIST.AGENT.COMM.RESERVED9` | `FsGiDistAgentComm_Reserved9` | TField |  |  |
| 18 | `FS.GI.DIST.AGENT.COMM.RESERVED8` | `FsGiDistAgentComm_Reserved8` | TField |  |  |
| 19 | `FS.GI.DIST.AGENT.COMM.RESERVED7` | `FsGiDistAgentComm_Reserved7` | TField |  |  |
| 20 | `FS.GI.DIST.AGENT.COMM.RESERVED6` | `FsGiDistAgentComm_Reserved6` | TField |  |  |
| 21 | `FS.GI.DIST.AGENT.COMM.RESERVED5` | `FsGiDistAgentComm_Reserved5` | TField |  |  |
| 22 | `FS.GI.DIST.AGENT.COMM.RESERVED4` | `FsGiDistAgentComm_Reserved4` | TField |  |  |
| 23 | `FS.GI.DIST.AGENT.COMM.RESERVED3` | `FsGiDistAgentComm_Reserved3` | TField |  |  |
| 24 | `FS.GI.DIST.AGENT.COMM.RESERVED2` | `FsGiDistAgentComm_Reserved2` | TField |  |  |
| 25 | `FS.GI.DIST.AGENT.COMM.RESERVED1` | `FsGiDistAgentComm_Reserved1` | TField |  |  |
| 26 | `FS.GI.DIST.AGENT.COMM.LOCAL.REF` | `FsGiDistAgentComm_LocalRef` |  |  |  |
| 27 | `FS.GI.DIST.AGENT.COMM.OVERRIDE` | `FsGiDistAgentComm_Override` |  |  |  |
| 28 | `FS.GI.DIST.AGENT.COMM.RECORD.STATUS` | `FsGiDistAgentComm_RecordStatus` | String |  |  |
| 29 | `FS.GI.DIST.AGENT.COMM.CURR.NO` | `FsGiDistAgentComm_CurrNo` | String |  |  |
| 30 | `FS.GI.DIST.AGENT.COMM.INPUTTER` | `FsGiDistAgentComm_Inputter` |  |  |  |
| 31 | `FS.GI.DIST.AGENT.COMM.DATE.TIME` | `FsGiDistAgentComm_DateTime` |  |  |  |
| 32 | `FS.GI.DIST.AGENT.COMM.AUTHORISER` | `FsGiDistAgentComm_Authoriser` | String |  |  |
| 33 | `FS.GI.DIST.AGENT.COMM.CO.CODE` | `FsGiDistAgentComm_CoCode` | String |  |  |
| 34 | `FS.GI.DIST.AGENT.COMM.DEPT.CODE` | `FsGiDistAgentComm_DeptCode` | String |  |  |
| 35 | `FS.GI.DIST.AGENT.COMM.AUDITOR.CODE` | `FsGiDistAgentComm_AuditorCode` | String |  |  |
| 36 | `FS.GI.DIST.AGENT.COMM.AUDIT.DATE.TIME` | `FsGiDistAgentComm_AuditDateTime` | String |  |  |
