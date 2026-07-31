# FS.GI.DIST.CONTACT.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.CONTACT.LINK` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.CONTACT.LINK.PARENT.REF.ID` | `FsGiDistContactLink_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.CONTACT.LINK.ORA.ROWID` | `FsGiDistContactLink_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.CONTACT.LINK.PARENT.ID.TYPE` | `FsGiDistContactLink_ParentIdType` | TField |  | ID of the entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.CONTACT.LINK.PARENT.ID` | `FsGiDistContactLink_ParentId` | TField |  | Type of entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.CONTACT.LINK.CONTACT.ID.TYPE` | `FsGiDistContactLink_ContactIdType` | TField |  | Contact List type of the entity. Multifonds DB Column is NCONT_TYPE. |
| 6 | `FS.GI.DIST.CONTACT.LINK.CONTACT.ID.LIST` | `FsGiDistContactLink_ContactIdList` | TField |  | Contact List Id of the entity. Multifonds DB Column is NCONT_LIST. |
| 7 | `FS.GI.DIST.CONTACT.LINK.LEGAL.ENTITY.ID` | `FsGiDistContactLink_LegalEntityId` | TField |  | Legal Entity ID connected to the Contact link. Multifonds DB Column is NTFC. |
| 8 | `FS.GI.DIST.CONTACT.LINK.RESERVED10` | `FsGiDistContactLink_Reserved10` | TField |  |  |
| 9 | `FS.GI.DIST.CONTACT.LINK.RESERVED9` | `FsGiDistContactLink_Reserved9` | TField |  |  |
| 10 | `FS.GI.DIST.CONTACT.LINK.RESERVED8` | `FsGiDistContactLink_Reserved8` | TField |  |  |
| 11 | `FS.GI.DIST.CONTACT.LINK.RESERVED7` | `FsGiDistContactLink_Reserved7` | TField |  |  |
| 12 | `FS.GI.DIST.CONTACT.LINK.RESERVED6` | `FsGiDistContactLink_Reserved6` | TField |  |  |
| 13 | `FS.GI.DIST.CONTACT.LINK.RESERVED5` | `FsGiDistContactLink_Reserved5` | TField |  |  |
| 14 | `FS.GI.DIST.CONTACT.LINK.RESERVED4` | `FsGiDistContactLink_Reserved4` | TField |  |  |
| 15 | `FS.GI.DIST.CONTACT.LINK.RESERVED3` | `FsGiDistContactLink_Reserved3` | TField |  |  |
| 16 | `FS.GI.DIST.CONTACT.LINK.RESERVED2` | `FsGiDistContactLink_Reserved2` | TField |  |  |
| 17 | `FS.GI.DIST.CONTACT.LINK.RESERVED1` | `FsGiDistContactLink_Reserved1` | TField |  |  |
| 18 | `FS.GI.DIST.CONTACT.LINK.LOCAL.REF` | `FsGiDistContactLink_LocalRef` |  |  |  |
| 19 | `FS.GI.DIST.CONTACT.LINK.OVERRIDE` | `FsGiDistContactLink_Override` |  |  |  |
| 20 | `FS.GI.DIST.CONTACT.LINK.RECORD.STATUS` | `FsGiDistContactLink_RecordStatus` | String |  |  |
| 21 | `FS.GI.DIST.CONTACT.LINK.CURR.NO` | `FsGiDistContactLink_CurrNo` | String |  |  |
| 22 | `FS.GI.DIST.CONTACT.LINK.INPUTTER` | `FsGiDistContactLink_Inputter` |  |  |  |
| 23 | `FS.GI.DIST.CONTACT.LINK.DATE.TIME` | `FsGiDistContactLink_DateTime` |  |  |  |
| 24 | `FS.GI.DIST.CONTACT.LINK.AUTHORISER` | `FsGiDistContactLink_Authoriser` | String |  |  |
| 25 | `FS.GI.DIST.CONTACT.LINK.CO.CODE` | `FsGiDistContactLink_CoCode` | String |  |  |
| 26 | `FS.GI.DIST.CONTACT.LINK.DEPT.CODE` | `FsGiDistContactLink_DeptCode` | String |  |  |
| 27 | `FS.GI.DIST.CONTACT.LINK.AUDITOR.CODE` | `FsGiDistContactLink_AuditorCode` | String |  |  |
| 28 | `FS.GI.DIST.CONTACT.LINK.AUDIT.DATE.TIME` | `FsGiDistContactLink_AuditDateTime` | String |  |  |
