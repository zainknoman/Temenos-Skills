# FS.GI.DIST.JOINTACCOUNT.REGISTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.JOINTACCOUNT.REGISTER` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.PARENT.REF.ID` | `FsGiDistJointaccountRegister_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.ORA.ROWID` | `FsGiDistJointaccountRegister_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.REGISTER.ID` | `FsGiDistJointaccountRegister_RegisterId` | TField |  | Register internal ID. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.JOIN.REGISTER.ID` | `FsGiDistJointaccountRegister_JoinRegisterId` | TField |  | Register ID linked as a joint account holder. Multifonds DB Column is NREGISTER_JOIN. |
| 5 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RELATION.TYPE` | `FsGiDistJointaccountRegister_RelationType` | TField |  | Relation type code for the relationship between joint account holder and main register. Multifonds DB Column is CRELATION. |
| 6 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.HOLDING.PCT` | `FsGiDistJointaccountRegister_HoldingPct` | TField |  | Joint account holding percentage. Multifonds DB Column is PCT_HOLDING. |
| 7 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.NO.COPY.FLAG` | `FsGiDistJointaccountRegister_NoCopyFlag` | TField |  | The flag to indicate that there is no additional account statements requried to send for the joint acount holder. Multifonds DB Column is FLG_NO_COPY. |
| 8 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.COUPLE.INTERNAL.ID` | `FsGiDistJointaccountRegister_CoupleInternalId` | TField |  | Unique internal identifier for joint account holder record. Multifonds DB Column is INTERNAL_ID. |
| 9 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RESERVED10` | `FsGiDistJointaccountRegister_Reserved10` | TField |  |  |
| 10 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RESERVED9` | `FsGiDistJointaccountRegister_Reserved9` | TField |  |  |
| 11 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RESERVED8` | `FsGiDistJointaccountRegister_Reserved8` | TField |  |  |
| 12 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RESERVED7` | `FsGiDistJointaccountRegister_Reserved7` | TField |  |  |
| 13 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RESERVED6` | `FsGiDistJointaccountRegister_Reserved6` | TField |  |  |
| 14 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RESERVED5` | `FsGiDistJointaccountRegister_Reserved5` | TField |  |  |
| 15 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RESERVED4` | `FsGiDistJointaccountRegister_Reserved4` | TField |  |  |
| 16 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RESERVED3` | `FsGiDistJointaccountRegister_Reserved3` | TField |  |  |
| 17 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RESERVED2` | `FsGiDistJointaccountRegister_Reserved2` | TField |  |  |
| 18 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RESERVED1` | `FsGiDistJointaccountRegister_Reserved1` | TField |  |  |
| 19 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.LOCAL.REF` | `FsGiDistJointaccountRegister_LocalRef` |  |  |  |
| 20 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.OVERRIDE` | `FsGiDistJointaccountRegister_Override` |  |  |  |
| 21 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.RECORD.STATUS` | `FsGiDistJointaccountRegister_RecordStatus` | String |  |  |
| 22 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.CURR.NO` | `FsGiDistJointaccountRegister_CurrNo` | String |  |  |
| 23 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.INPUTTER` | `FsGiDistJointaccountRegister_Inputter` |  |  |  |
| 24 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.DATE.TIME` | `FsGiDistJointaccountRegister_DateTime` |  |  |  |
| 25 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.AUTHORISER` | `FsGiDistJointaccountRegister_Authoriser` | String |  |  |
| 26 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.CO.CODE` | `FsGiDistJointaccountRegister_CoCode` | String |  |  |
| 27 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.DEPT.CODE` | `FsGiDistJointaccountRegister_DeptCode` | String |  |  |
| 28 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.AUDITOR.CODE` | `FsGiDistJointaccountRegister_AuditorCode` | String |  |  |
| 29 | `FS.GI.DIST.JOINTACCOUNT.REGISTER.AUDIT.DATE.TIME` | `FsGiDistJointaccountRegister_AuditDateTime` | String |  |  |
