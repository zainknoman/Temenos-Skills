# FS.GI.DIST.AGENT.GROUP.DISTRTIB — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.GROUP.DISTRTIB` in `FS_AgentStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.PARENT.REF.ID` | `FsGiDistAgentGroupDistrtib_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.ORA.ROWID` | `FsGiDistAgentGroupDistrtib_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.AGENT.ID` | `FsGiDistAgentGroupDistrtib_AgentId` | TField |  | Agent ID for agent distribution. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.COMMISSION.GROUP` | `FsGiDistAgentGroupDistrtib_CommissionGroup` | TField |  | Fund commission group distribution. Multifonds DB Column is CGROUP. |
| 5 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.SHARE.CLASS.CODE` | `FsGiDistAgentGroupDistrtib_ShareClassCode` | TField |  | Fund share class code linked to the fund commission group distribution. Multifonds DB Column is TPART. |
| 6 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.OPERATION.CODE` | `FsGiDistAgentGroupDistrtib_OperationCode` | TField |  | Operation code for which the group commission distribution is applicable. Multifonds DB Column is COPERATION. |
| 7 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.SUB.AGENT.ID` | `FsGiDistAgentGroupDistrtib_SubAgentId` | TField |  | Sub Agent ID linked to agent distribution. Multifonds DB Column is NOUTLET_SUB. |
| 8 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.DISTRIB.TYPE` | `FsGiDistAgentGroupDistrtib_DistribType` | TField |  | Commission Distribution type code. Multifonds DB Column is TYPE_DISTRIB. |
| 9 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.PERCENTAGE` | `FsGiDistAgentGroupDistrtib_Percentage` | TField |  | Percentage of the commission distribution. Multifonds DB Column is PCT. |
| 10 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.AGENT.PAYMENT.ID` | `FsGiDistAgentGroupDistrtib_AgentPaymentId` | TField |  | Agent to which the TA has to pay the defined commission. Multifonds DB Column is NOUTLET_PAY. |
| 11 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.LEVEL` | `FsGiDistAgentGroupDistrtib_Level` | TField |  | Commission distribution group level linked to the distribution agents. Multifonds DB Column is NIVEAU. |
| 12 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.SPECIFIC.INITIAL.CHARGE.PCT` | `FsGiDistAgentGroupDistrtib_SpecificInitialChargePct` | TField |  | Maximum commission percentage allowed for the operation code at distribution agreement level. Multifonds DB Column is PCT_SPE_INT_CRG. |
| 13 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.DEFAULT.COMMISSION.TYPE` | `FsGiDistAgentGroupDistrtib_DefaultCommissionType` | TField |  | It specifies the commission type of the agent group distribution. Multifonds DB Column is COMM_TYPE. |
| 14 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.AGENT.GROUP.DISTRIBUTION.ID` | `FsGiDistAgentGroupDistrtib_AgentGroupDistributionId` | TField |  | Unique internal identifier for agent group distribution definition. Multifonds DB Column is INTERNAL_ID. |
| 15 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RESERVED10` | `FsGiDistAgentGroupDistrtib_Reserved10` | TField |  |  |
| 16 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RESERVED9` | `FsGiDistAgentGroupDistrtib_Reserved9` | TField |  |  |
| 17 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RESERVED8` | `FsGiDistAgentGroupDistrtib_Reserved8` | TField |  |  |
| 18 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RESERVED7` | `FsGiDistAgentGroupDistrtib_Reserved7` | TField |  |  |
| 19 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RESERVED6` | `FsGiDistAgentGroupDistrtib_Reserved6` | TField |  |  |
| 20 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RESERVED5` | `FsGiDistAgentGroupDistrtib_Reserved5` | TField |  |  |
| 21 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RESERVED4` | `FsGiDistAgentGroupDistrtib_Reserved4` | TField |  |  |
| 22 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RESERVED3` | `FsGiDistAgentGroupDistrtib_Reserved3` | TField |  |  |
| 23 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RESERVED2` | `FsGiDistAgentGroupDistrtib_Reserved2` | TField |  |  |
| 24 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RESERVED1` | `FsGiDistAgentGroupDistrtib_Reserved1` | TField |  |  |
| 25 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.LOCAL.REF` | `FsGiDistAgentGroupDistrtib_LocalRef` |  |  |  |
| 26 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.OVERRIDE` | `FsGiDistAgentGroupDistrtib_Override` |  |  |  |
| 27 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.RECORD.STATUS` | `FsGiDistAgentGroupDistrtib_RecordStatus` | String |  |  |
| 28 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.CURR.NO` | `FsGiDistAgentGroupDistrtib_CurrNo` | String |  |  |
| 29 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.INPUTTER` | `FsGiDistAgentGroupDistrtib_Inputter` |  |  |  |
| 30 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.DATE.TIME` | `FsGiDistAgentGroupDistrtib_DateTime` |  |  |  |
| 31 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.AUTHORISER` | `FsGiDistAgentGroupDistrtib_Authoriser` | String |  |  |
| 32 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.CO.CODE` | `FsGiDistAgentGroupDistrtib_CoCode` | String |  |  |
| 33 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.DEPT.CODE` | `FsGiDistAgentGroupDistrtib_DeptCode` | String |  |  |
| 34 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.AUDITOR.CODE` | `FsGiDistAgentGroupDistrtib_AuditorCode` | String |  |  |
| 35 | `FS.GI.DIST.AGENT.GROUP.DISTRTIB.AUDIT.DATE.TIME` | `FsGiDistAgentGroupDistrtib_AuditDateTime` | String |  |  |
