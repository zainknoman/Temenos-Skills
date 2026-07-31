# FS.GI.DIST.JOINTACCOUNT.INVESTOR — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.JOINTACCOUNT.INVESTOR` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.PARENT.REF.ID` | `FsGiDistJointaccountInvestor_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.ORA.ROWID` | `FsGiDistJointaccountInvestor_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.REGISTER.ID` | `FsGiDistJointaccountInvestor_RegisterId` | TField |  | Register internal ID Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.INVESTOR.ID` | `FsGiDistJointaccountInvestor_InvestorId` | TField |  | Investor ID linked as a joint account holder. Multifonds DB Column is NCLIENT_JOIN. |
| 5 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RELATION.TYPE` | `FsGiDistJointaccountInvestor_RelationType` | TField |  | Relation type code for the relationship between joint account holder and main register. Multifonds DB Column is CRELATION. |
| 6 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.HOLDING.PCT` | `FsGiDistJointaccountInvestor_HoldingPct` | TField |  | Joint account holding percentage. Multifonds DB Column is PCT_HOLDING. |
| 7 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.NO.COPY.FLAG` | `FsGiDistJointaccountInvestor_NoCopyFlag` | TField |  | The flag to indicate that there is no additional account statements requried to send for the joint acount holder. Multifonds DB Column is FLG_NO_COPY. |
| 8 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.COUPLE.INTERNAL.ID` | `FsGiDistJointaccountInvestor_CoupleInternalId` | TField |  | Unique internal identifier for joint account holder record. Multifonds DB Column is INTERNAL_ID. |
| 9 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RESERVED10` | `FsGiDistJointaccountInvestor_Reserved10` | TField |  |  |
| 10 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RESERVED9` | `FsGiDistJointaccountInvestor_Reserved9` | TField |  |  |
| 11 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RESERVED8` | `FsGiDistJointaccountInvestor_Reserved8` | TField |  |  |
| 12 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RESERVED7` | `FsGiDistJointaccountInvestor_Reserved7` | TField |  |  |
| 13 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RESERVED6` | `FsGiDistJointaccountInvestor_Reserved6` | TField |  |  |
| 14 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RESERVED5` | `FsGiDistJointaccountInvestor_Reserved5` | TField |  |  |
| 15 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RESERVED4` | `FsGiDistJointaccountInvestor_Reserved4` | TField |  |  |
| 16 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RESERVED3` | `FsGiDistJointaccountInvestor_Reserved3` | TField |  |  |
| 17 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RESERVED2` | `FsGiDistJointaccountInvestor_Reserved2` | TField |  |  |
| 18 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RESERVED1` | `FsGiDistJointaccountInvestor_Reserved1` | TField |  |  |
| 19 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.LOCAL.REF` | `FsGiDistJointaccountInvestor_LocalRef` |  |  |  |
| 20 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.OVERRIDE` | `FsGiDistJointaccountInvestor_Override` |  |  |  |
| 21 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.RECORD.STATUS` | `FsGiDistJointaccountInvestor_RecordStatus` | String |  |  |
| 22 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.CURR.NO` | `FsGiDistJointaccountInvestor_CurrNo` | String |  |  |
| 23 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.INPUTTER` | `FsGiDistJointaccountInvestor_Inputter` |  |  |  |
| 24 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.DATE.TIME` | `FsGiDistJointaccountInvestor_DateTime` |  |  |  |
| 25 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.AUTHORISER` | `FsGiDistJointaccountInvestor_Authoriser` | String |  |  |
| 26 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.CO.CODE` | `FsGiDistJointaccountInvestor_CoCode` | String |  |  |
| 27 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.DEPT.CODE` | `FsGiDistJointaccountInvestor_DeptCode` | String |  |  |
| 28 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.AUDITOR.CODE` | `FsGiDistJointaccountInvestor_AuditorCode` | String |  |  |
| 29 | `FS.GI.DIST.JOINTACCOUNT.INVESTOR.AUDIT.DATE.TIME` | `FsGiDistJointaccountInvestor_AuditDateTime` | String |  |  |
