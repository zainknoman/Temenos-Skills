# FS.GI.DIST.RELATIONSHIP — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.RELATIONSHIP` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.RELATIONSHIP.PARENT.REF.ID` | `FsGiDistRelationship_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.RELATIONSHIP.ORA.ROWID` | `FsGiDistRelationship_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.RELATIONSHIP.REGISTER.ID` | `FsGiDistRelationship_RegisterId` | TField |  | Register internal ID Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.RELATIONSHIP.ACTIVE.FLAG` | `FsGiDistRelationship_ActiveFlag` | TField |  | Flag to identify whether the link of register with a related party is still active or not. Multifonds DB Column is FLG_RELATION_PARTY. |
| 5 | `FS.GI.DIST.RELATIONSHIP.PROXY.ID` | `FsGiDistRelationship_ProxyId` | TField |  | Proxy entity internal ID related to the register. Multifonds DB Column is PROXY. |
| 6 | `FS.GI.DIST.RELATIONSHIP.RELATION.TYPE` | `FsGiDistRelationship_RelationType` | TField |  | Type of the relation between proxy and register. Multifonds DB Column is CRELATION. |
| 7 | `FS.GI.DIST.RELATIONSHIP.REASON` | `FsGiDistRelationship_Reason` | TField |  | Reason code for granting the Power of Attorney. Multifonds DB Column is REASON. |
| 8 | `FS.GI.DIST.RELATIONSHIP.FULL.POWER.FLAG` | `FsGiDistRelationship_FullPowerFlag` | TField |  | Flag allows to enable full power for the proxy on all transactions. Otherwise, rights needs to be defined individually. Multifonds DB Column is POWER. |
| 9 | `FS.GI.DIST.RELATIONSHIP.INSTRUCTION.TEXT` | `FsGiDistRelationship_InstructionText` | TField |  | Free text that allows upto 80 alpha numerical characters for proxy entity relationship instructions. Multifonds DB Column is INSTRUCTION. |
| 10 | `FS.GI.DIST.RELATIONSHIP.START.DATE` | `FsGiDistRelationship_StartDate` | TField |  | The date from which on the &apos;Power of Attorney&apos; is granted. Multifonds DB Column is STDATE. |
| 11 | `FS.GI.DIST.RELATIONSHIP.END.DATE` | `FsGiDistRelationship_EndDate` | TField |  | The date on which the &apos;Power of Attorney&apos; ended or will end. Multifonds DB Column is ENDDATE. |
| 12 | `FS.GI.DIST.RELATIONSHIP.INVESTOR.REGISTER.FLAG` | `FsGiDistRelationship_InvestorRegisterFlag` | TField |  | Indicates whether the proxy entity is a Client (C) or a Register (R ). Multifonds DB Column is FLG_CLI_REG. |
| 13 | `FS.GI.DIST.RELATIONSHIP.RELATIONSHIP.ID` | `FsGiDistRelationship_RelationshipId` | TField |  | Unique internal identifier for register proxy relationship record. Multifonds DB Column is INTERNAL_ID. |
| 14 | `FS.GI.DIST.RELATIONSHIP.RESERVED10` | `FsGiDistRelationship_Reserved10` | TField |  |  |
| 15 | `FS.GI.DIST.RELATIONSHIP.RESERVED9` | `FsGiDistRelationship_Reserved9` | TField |  |  |
| 16 | `FS.GI.DIST.RELATIONSHIP.RESERVED8` | `FsGiDistRelationship_Reserved8` | TField |  |  |
| 17 | `FS.GI.DIST.RELATIONSHIP.RESERVED7` | `FsGiDistRelationship_Reserved7` | TField |  |  |
| 18 | `FS.GI.DIST.RELATIONSHIP.RESERVED6` | `FsGiDistRelationship_Reserved6` | TField |  |  |
| 19 | `FS.GI.DIST.RELATIONSHIP.RESERVED5` | `FsGiDistRelationship_Reserved5` | TField |  |  |
| 20 | `FS.GI.DIST.RELATIONSHIP.RESERVED4` | `FsGiDistRelationship_Reserved4` | TField |  |  |
| 21 | `FS.GI.DIST.RELATIONSHIP.RESERVED3` | `FsGiDistRelationship_Reserved3` | TField |  |  |
| 22 | `FS.GI.DIST.RELATIONSHIP.RESERVED2` | `FsGiDistRelationship_Reserved2` | TField |  |  |
| 23 | `FS.GI.DIST.RELATIONSHIP.RESERVED1` | `FsGiDistRelationship_Reserved1` | TField |  |  |
| 24 | `FS.GI.DIST.RELATIONSHIP.LOCAL.REF` | `FsGiDistRelationship_LocalRef` |  |  |  |
| 25 | `FS.GI.DIST.RELATIONSHIP.OVERRIDE` | `FsGiDistRelationship_Override` |  |  |  |
| 26 | `FS.GI.DIST.RELATIONSHIP.RECORD.STATUS` | `FsGiDistRelationship_RecordStatus` | String |  |  |
| 27 | `FS.GI.DIST.RELATIONSHIP.CURR.NO` | `FsGiDistRelationship_CurrNo` | String |  |  |
| 28 | `FS.GI.DIST.RELATIONSHIP.INPUTTER` | `FsGiDistRelationship_Inputter` |  |  |  |
| 29 | `FS.GI.DIST.RELATIONSHIP.DATE.TIME` | `FsGiDistRelationship_DateTime` |  |  |  |
| 30 | `FS.GI.DIST.RELATIONSHIP.AUTHORISER` | `FsGiDistRelationship_Authoriser` | String |  |  |
| 31 | `FS.GI.DIST.RELATIONSHIP.CO.CODE` | `FsGiDistRelationship_CoCode` | String |  |  |
| 32 | `FS.GI.DIST.RELATIONSHIP.DEPT.CODE` | `FsGiDistRelationship_DeptCode` | String |  |  |
| 33 | `FS.GI.DIST.RELATIONSHIP.AUDITOR.CODE` | `FsGiDistRelationship_AuditorCode` | String |  |  |
| 34 | `FS.GI.DIST.RELATIONSHIP.AUDIT.DATE.TIME` | `FsGiDistRelationship_AuditDateTime` | String |  |  |
