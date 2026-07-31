# FS.GI.DIST.INVESTOR.RELATION — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.INVESTOR.RELATION` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.INVESTOR.RELATION.PARENT.REF.ID` | `FsGiDistInvestorRelation_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.INVESTOR.RELATION.ORA.ROWID` | `FsGiDistInvestorRelation_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.INVESTOR.RELATION.INVESTOR.ID` | `FsGiDistInvestorRelation_InvestorId` | TField |  | Investor internal ID linked to the relationship entity. Multifonds DB Column is NCLIENT. |
| 4 | `FS.GI.DIST.INVESTOR.RELATION.PROXY.ID` | `FsGiDistInvestorRelation_ProxyId` | TField |  | Proxy ID related to the investor. Multifonds DB Column is PROXY. |
| 5 | `FS.GI.DIST.INVESTOR.RELATION.RELATION.TYPE` | `FsGiDistInvestorRelation_RelationType` | TField |  | Type of the relation between proxy and the investor Multifonds DB Column is CRELATION. |
| 6 | `FS.GI.DIST.INVESTOR.RELATION.REASON` | `FsGiDistInvestorRelation_Reason` | TField |  | Reason code for granting the Power of Attorney. Multifonds DB Column is REASON. |
| 7 | `FS.GI.DIST.INVESTOR.RELATION.FULL.POWER.FLAG` | `FsGiDistInvestorRelation_FullPowerFlag` | TField |  | Flag allows to enable full power for the proxy on all transactions. Otherwise, rights needs to be defined individually. Multifonds DB Column is POWER. |
| 8 | `FS.GI.DIST.INVESTOR.RELATION.INSTRUCTION.TEXT` | `FsGiDistInvestorRelation_InstructionText` | TField |  | Free text that allows upto 50 alpha numerical characters for user definable proxy instructions. Multifonds DB Column is INSTRUCTION. |
| 9 | `FS.GI.DIST.INVESTOR.RELATION.START.DATE` | `FsGiDistInvestorRelation_StartDate` | TField |  | The date from which the &apos;Power of Attorney&apos; will commence. Multifonds DB Column is STDATE. |
| 10 | `FS.GI.DIST.INVESTOR.RELATION.END.DATE` | `FsGiDistInvestorRelation_EndDate` | TField |  | The date on which the &apos;Power of Attorney&apos; will end. Multifonds DB Column is ENDDATE. |
| 11 | `FS.GI.DIST.INVESTOR.RELATION.INVESTOR.REGISTER.FLAG` | `FsGiDistInvestorRelation_InvestorRegisterFlag` | TField |  | Field to identify whether the proxy entity is an Investor (C) or a Register(R). Multifonds DB Column is FLG_CLI_REG. |
| 12 | `FS.GI.DIST.INVESTOR.RELATION.ACTIVE.FLAG` | `FsGiDistInvestorRelation_ActiveFlag` | TField |  | Flag to Identify whether the link of investor with a related party is still active or not. Multifonds DB Column is FLG_RELATION_PARTY. |
| 13 | `FS.GI.DIST.INVESTOR.RELATION.CLI.RELATION.ID` | `FsGiDistInvestorRelation_CliRelationId` | TField |  | Unique internal investor relation identifier. Multifonds DB Column is INTERNAL_ID. |
| 14 | `FS.GI.DIST.INVESTOR.RELATION.RESERVED10` | `FsGiDistInvestorRelation_Reserved10` | TField |  |  |
| 15 | `FS.GI.DIST.INVESTOR.RELATION.RESERVED9` | `FsGiDistInvestorRelation_Reserved9` | TField |  |  |
| 16 | `FS.GI.DIST.INVESTOR.RELATION.RESERVED8` | `FsGiDistInvestorRelation_Reserved8` | TField |  |  |
| 17 | `FS.GI.DIST.INVESTOR.RELATION.RESERVED7` | `FsGiDistInvestorRelation_Reserved7` | TField |  |  |
| 18 | `FS.GI.DIST.INVESTOR.RELATION.RESERVED6` | `FsGiDistInvestorRelation_Reserved6` | TField |  |  |
| 19 | `FS.GI.DIST.INVESTOR.RELATION.RESERVED5` | `FsGiDistInvestorRelation_Reserved5` | TField |  |  |
| 20 | `FS.GI.DIST.INVESTOR.RELATION.RESERVED4` | `FsGiDistInvestorRelation_Reserved4` | TField |  |  |
| 21 | `FS.GI.DIST.INVESTOR.RELATION.RESERVED3` | `FsGiDistInvestorRelation_Reserved3` | TField |  |  |
| 22 | `FS.GI.DIST.INVESTOR.RELATION.RESERVED2` | `FsGiDistInvestorRelation_Reserved2` | TField |  |  |
| 23 | `FS.GI.DIST.INVESTOR.RELATION.RESERVED1` | `FsGiDistInvestorRelation_Reserved1` | TField |  |  |
| 24 | `FS.GI.DIST.INVESTOR.RELATION.LOCAL.REF` | `FsGiDistInvestorRelation_LocalRef` |  |  |  |
| 25 | `FS.GI.DIST.INVESTOR.RELATION.OVERRIDE` | `FsGiDistInvestorRelation_Override` |  |  |  |
| 26 | `FS.GI.DIST.INVESTOR.RELATION.RECORD.STATUS` | `FsGiDistInvestorRelation_RecordStatus` | String |  |  |
| 27 | `FS.GI.DIST.INVESTOR.RELATION.CURR.NO` | `FsGiDistInvestorRelation_CurrNo` | String |  |  |
| 28 | `FS.GI.DIST.INVESTOR.RELATION.INPUTTER` | `FsGiDistInvestorRelation_Inputter` |  |  |  |
| 29 | `FS.GI.DIST.INVESTOR.RELATION.DATE.TIME` | `FsGiDistInvestorRelation_DateTime` |  |  |  |
| 30 | `FS.GI.DIST.INVESTOR.RELATION.AUTHORISER` | `FsGiDistInvestorRelation_Authoriser` | String |  |  |
| 31 | `FS.GI.DIST.INVESTOR.RELATION.CO.CODE` | `FsGiDistInvestorRelation_CoCode` | String |  |  |
| 32 | `FS.GI.DIST.INVESTOR.RELATION.DEPT.CODE` | `FsGiDistInvestorRelation_DeptCode` | String |  |  |
| 33 | `FS.GI.DIST.INVESTOR.RELATION.AUDITOR.CODE` | `FsGiDistInvestorRelation_AuditorCode` | String |  |  |
| 34 | `FS.GI.DIST.INVESTOR.RELATION.AUDIT.DATE.TIME` | `FsGiDistInvestorRelation_AuditDateTime` | String |  |  |
