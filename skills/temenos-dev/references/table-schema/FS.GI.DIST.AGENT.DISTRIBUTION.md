# FS.GI.DIST.AGENT.DISTRIBUTION — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.DISTRIBUTION` in `FS_AgentStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.DISTRIBUTION.PARENT.REF.ID` | `FsGiDistAgentDistribution_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.DISTRIBUTION.ORA.ROWID` | `FsGiDistAgentDistribution_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.DISTRIBUTION.AGENT.ID` | `FsGiDistAgentDistribution_AgentId` | TField |  | Agent internal id for the agent distribution. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.DIST.AGENT.DISTRIBUTION.TA.FUND.ID` | `FsGiDistAgentDistribution_TaFundId` | TField |  | Fund internal id linked to the agent distribution. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.DIST.AGENT.DISTRIBUTION.SHARE.CLASS.CODE` | `FsGiDistAgentDistribution_ShareClassCode` | TField |  | Fund share class linked to the agent distribution. Multifonds DB Column is TPART. |
| 6 | `FS.GI.DIST.AGENT.DISTRIBUTION.OPERATION.CODE` | `FsGiDistAgentDistribution_OperationCode` | TField |  | Operation code linked to the agent distribution. Multifonds DB Column is COPERATION. |
| 7 | `FS.GI.DIST.AGENT.DISTRIBUTION.SUB.AGENT.ID` | `FsGiDistAgentDistribution_SubAgentId` | TField |  | Sub Agent ID linked to the agent distribution. Multifonds DB Column is NOUTLET_SUB. |
| 8 | `FS.GI.DIST.AGENT.DISTRIBUTION.DISTRIB.TYPE` | `FsGiDistAgentDistribution_DistribType` | TField |  | Commission Distribution type code. Multifonds DB Column is TYPE_DISTRIB. |
| 9 | `FS.GI.DIST.AGENT.DISTRIBUTION.PERCENTAGE` | `FsGiDistAgentDistribution_Percentage` | TField |  | Percentage of the commission distribution. Multifonds DB Column is PCT. |
| 10 | `FS.GI.DIST.AGENT.DISTRIBUTION.AGENT.PAYMENT.ID` | `FsGiDistAgentDistribution_AgentPaymentId` | TField |  | Agent ID to which the TA has to pay the defined commission. Multifonds DB Column is NOUTLET_PAY. |
| 11 | `FS.GI.DIST.AGENT.DISTRIBUTION.LEVEL` | `FsGiDistAgentDistribution_Level` | TField |  | Agent Commission Distribution Level linked to the distribution Agents. Multifonds DB Column is NIVEAU. |
| 12 | `FS.GI.DIST.AGENT.DISTRIBUTION.SPECIFIC.INITIAL.CHARGE.PCT` | `FsGiDistAgentDistribution_SpecificInitialChargePct` | TField |  | Maximum commission percentage allowed for the operation code at distribution agreement level for the agent. Multifonds DB Column is PCT_SPE_INT_CRG. |
| 13 | `FS.GI.DIST.AGENT.DISTRIBUTION.DEFAULT.COMMISSION.TYPE` | `FsGiDistAgentDistribution_DefaultCommissionType` | TField |  | It specifies the commission type of the agent distribution. Multifonds DB Column is COMM_TYPE. |
| 14 | `FS.GI.DIST.AGENT.DISTRIBUTION.AGENT.DISTRIBUTION.ID` | `FsGiDistAgentDistribution_AgentDistributionId` | TField |  | Unique internal identifier for agent distribution definition. Multifonds DB Column is INTERNAL_ID. |
| 15 | `FS.GI.DIST.AGENT.DISTRIBUTION.FUND.ID` | `FsGiDistAgentDistribution_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 16 | `FS.GI.DIST.AGENT.DISTRIBUTION.CLASS.CURRENCY` | `FsGiDistAgentDistribution_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 17 | `FS.GI.DIST.AGENT.DISTRIBUTION.RESERVED10` | `FsGiDistAgentDistribution_Reserved10` | TField |  |  |
| 18 | `FS.GI.DIST.AGENT.DISTRIBUTION.RESERVED9` | `FsGiDistAgentDistribution_Reserved9` | TField |  |  |
| 19 | `FS.GI.DIST.AGENT.DISTRIBUTION.RESERVED8` | `FsGiDistAgentDistribution_Reserved8` | TField |  |  |
| 20 | `FS.GI.DIST.AGENT.DISTRIBUTION.RESERVED7` | `FsGiDistAgentDistribution_Reserved7` | TField |  |  |
| 21 | `FS.GI.DIST.AGENT.DISTRIBUTION.RESERVED6` | `FsGiDistAgentDistribution_Reserved6` | TField |  |  |
| 22 | `FS.GI.DIST.AGENT.DISTRIBUTION.RESERVED5` | `FsGiDistAgentDistribution_Reserved5` | TField |  |  |
| 23 | `FS.GI.DIST.AGENT.DISTRIBUTION.RESERVED4` | `FsGiDistAgentDistribution_Reserved4` | TField |  |  |
| 24 | `FS.GI.DIST.AGENT.DISTRIBUTION.RESERVED3` | `FsGiDistAgentDistribution_Reserved3` | TField |  |  |
| 25 | `FS.GI.DIST.AGENT.DISTRIBUTION.RESERVED2` | `FsGiDistAgentDistribution_Reserved2` | TField |  |  |
| 26 | `FS.GI.DIST.AGENT.DISTRIBUTION.RESERVED1` | `FsGiDistAgentDistribution_Reserved1` | TField |  |  |
| 27 | `FS.GI.DIST.AGENT.DISTRIBUTION.LOCAL.REF` | `FsGiDistAgentDistribution_LocalRef` |  |  |  |
| 28 | `FS.GI.DIST.AGENT.DISTRIBUTION.OVERRIDE` | `FsGiDistAgentDistribution_Override` |  |  |  |
| 29 | `FS.GI.DIST.AGENT.DISTRIBUTION.RECORD.STATUS` | `FsGiDistAgentDistribution_RecordStatus` | String |  |  |
| 30 | `FS.GI.DIST.AGENT.DISTRIBUTION.CURR.NO` | `FsGiDistAgentDistribution_CurrNo` | String |  |  |
| 31 | `FS.GI.DIST.AGENT.DISTRIBUTION.INPUTTER` | `FsGiDistAgentDistribution_Inputter` |  |  |  |
| 32 | `FS.GI.DIST.AGENT.DISTRIBUTION.DATE.TIME` | `FsGiDistAgentDistribution_DateTime` |  |  |  |
| 33 | `FS.GI.DIST.AGENT.DISTRIBUTION.AUTHORISER` | `FsGiDistAgentDistribution_Authoriser` | String |  |  |
| 34 | `FS.GI.DIST.AGENT.DISTRIBUTION.CO.CODE` | `FsGiDistAgentDistribution_CoCode` | String |  |  |
| 35 | `FS.GI.DIST.AGENT.DISTRIBUTION.DEPT.CODE` | `FsGiDistAgentDistribution_DeptCode` | String |  |  |
| 36 | `FS.GI.DIST.AGENT.DISTRIBUTION.AUDITOR.CODE` | `FsGiDistAgentDistribution_AuditorCode` | String |  |  |
| 37 | `FS.GI.DIST.AGENT.DISTRIBUTION.AUDIT.DATE.TIME` | `FsGiDistAgentDistribution_AuditDateTime` | String |  |  |
