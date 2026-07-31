# FS.GI.APP.COMMISSION.STRUCTURE.DIST — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.COMMISSION.STRUCTURE.DIST` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.PARENT.REF.ID` | `FsGiAppCommissionStructureDist_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.ORA.ROWID` | `FsGiAppCommissionStructureDist_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.COMM.STRUCTURE.ID` | `FsGiAppCommissionStructureDist_CommStructureId` | TField |  | Commission structure identification code . Multifonds DB Column is STRUCTURE_ID. |
| 4 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.AGENT.ID` | `FsGiAppCommissionStructureDist_AgentId` | TField |  | Structure Comm. Distribution Agent ID. Multifonds DB Column is NOUTLET. |
| 5 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.DEFAULT.COMMISSION.TYPE` | `FsGiAppCommissionStructureDist_DefaultCommissionType` | TField |  | Commission Type Code. Multifonds DB Column is COMM_TYPE. |
| 6 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.PERCENTAGE` | `FsGiAppCommissionStructureDist_Percentage` | TField |  | Percentage to be distributed to the agent. Multifonds DB Column is PCT. |
| 7 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.PAYMENT.AGENT.ID` | `FsGiAppCommissionStructureDist_PaymentAgentId` | TField |  | Specifies which agents will receive the commission payment. Multifonds DB Column is NOUTLET_PAY. |
| 8 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.AML.CHECK.FLAG` | `FsGiAppCommissionStructureDist_AmlCheckFlag` | TField |  | Flag to enable agent AML check. Multifonds DB Column is FLG_AML_CHECKS. |
| 9 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.INVISIBLE.FLAG` | `FsGiAppCommissionStructureDist_InvisibleFlag` | TField |  | Flag to mention the agent should not be considered as an official agent within the agent structure. Multifonds DB Column is FLG_INVISIBLE. |
| 10 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.LEVEL` | `FsGiAppCommissionStructureDist_Level` | TField |  | Agent&apos;s level in the distribution hierarchy of the Distribution Agents. Multifonds DB Column is NIVEAU. |
| 11 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.SPECIFIC.INITIAL.CHARGE.PCT` | `FsGiAppCommissionStructureDist_SpecificInitialChargePct` | TField |  | Maximum commission % allowed for the distribution agreement level for the agent distribution. Multifonds DB Column is PCT_SPE_INT_CRG. |
| 12 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RESERVED10` | `FsGiAppCommissionStructureDist_Reserved10` | TField |  |  |
| 13 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RESERVED9` | `FsGiAppCommissionStructureDist_Reserved9` | TField |  |  |
| 14 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RESERVED8` | `FsGiAppCommissionStructureDist_Reserved8` | TField |  |  |
| 15 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RESERVED7` | `FsGiAppCommissionStructureDist_Reserved7` | TField |  |  |
| 16 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RESERVED6` | `FsGiAppCommissionStructureDist_Reserved6` | TField |  |  |
| 17 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RESERVED5` | `FsGiAppCommissionStructureDist_Reserved5` | TField |  |  |
| 18 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RESERVED4` | `FsGiAppCommissionStructureDist_Reserved4` | TField |  |  |
| 19 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RESERVED3` | `FsGiAppCommissionStructureDist_Reserved3` | TField |  |  |
| 20 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RESERVED2` | `FsGiAppCommissionStructureDist_Reserved2` | TField |  |  |
| 21 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RESERVED1` | `FsGiAppCommissionStructureDist_Reserved1` | TField |  |  |
| 22 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.LOCAL.REF` | `FsGiAppCommissionStructureDist_LocalRef` |  |  |  |
| 23 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.OVERRIDE` | `FsGiAppCommissionStructureDist_Override` |  |  |  |
| 24 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.RECORD.STATUS` | `FsGiAppCommissionStructureDist_RecordStatus` | String |  |  |
| 25 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.CURR.NO` | `FsGiAppCommissionStructureDist_CurrNo` | String |  |  |
| 26 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.INPUTTER` | `FsGiAppCommissionStructureDist_Inputter` |  |  |  |
| 27 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.DATE.TIME` | `FsGiAppCommissionStructureDist_DateTime` |  |  |  |
| 28 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.AUTHORISER` | `FsGiAppCommissionStructureDist_Authoriser` | String |  |  |
| 29 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.CO.CODE` | `FsGiAppCommissionStructureDist_CoCode` | String |  |  |
| 30 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.DEPT.CODE` | `FsGiAppCommissionStructureDist_DeptCode` | String |  |  |
| 31 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.AUDITOR.CODE` | `FsGiAppCommissionStructureDist_AuditorCode` | String |  |  |
| 32 | `FS.GI.APP.COMMISSION.STRUCTURE.DIST.AUDIT.DATE.TIME` | `FsGiAppCommissionStructureDist_AuditDateTime` | String |  |  |
