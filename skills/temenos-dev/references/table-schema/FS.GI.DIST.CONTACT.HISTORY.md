# FS.GI.DIST.CONTACT.HISTORY — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.CONTACT.HISTORY` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.CONTACT.HISTORY.PARENT.REF.ID` | `FsGiDistContactHistory_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.CONTACT.HISTORY.ORA.ROWID` | `FsGiDistContactHistory_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.CONTACT.HISTORY.PARENT.ID.TYPE` | `FsGiDistContactHistory_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.CONTACT.HISTORY.PARENT.ID` | `FsGiDistContactHistory_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.CONTACT.HISTORY.CONTACT.DATE` | `FsGiDistContactHistory_ContactDate` | TField |  | Date on which the entity has been contacted. Multifonds DB Column is DCONTACT. |
| 6 | `FS.GI.DIST.CONTACT.HISTORY.COMMENTS` | `FsGiDistContactHistory_Comments` | TField |  | Free text field that allows upto 300 alpha numerical characters for contact comments. Multifonds DB Column is COMMENT_DESC. |
| 7 | `FS.GI.DIST.CONTACT.HISTORY.SELECT.FLAG` | `FsGiDistContactHistory_SelectFlag` | TField |  | Flag to indicates the contact history comments are active. A maximum of 3 comments can be selected. Multifonds DB Column is FLG_SELECT. |
| 8 | `FS.GI.DIST.CONTACT.HISTORY.CONTACT.HIST.ID` | `FsGiDistContactHistory_ContactHistId` | TField |  | Unique internal contact hisotry comments identifer. Multifonds DB Column is INTERNAL_ID. |
| 9 | `FS.GI.DIST.CONTACT.HISTORY.RESERVED10` | `FsGiDistContactHistory_Reserved10` | TField |  |  |
| 10 | `FS.GI.DIST.CONTACT.HISTORY.RESERVED9` | `FsGiDistContactHistory_Reserved9` | TField |  |  |
| 11 | `FS.GI.DIST.CONTACT.HISTORY.RESERVED8` | `FsGiDistContactHistory_Reserved8` | TField |  |  |
| 12 | `FS.GI.DIST.CONTACT.HISTORY.RESERVED7` | `FsGiDistContactHistory_Reserved7` | TField |  |  |
| 13 | `FS.GI.DIST.CONTACT.HISTORY.RESERVED6` | `FsGiDistContactHistory_Reserved6` | TField |  |  |
| 14 | `FS.GI.DIST.CONTACT.HISTORY.RESERVED5` | `FsGiDistContactHistory_Reserved5` | TField |  |  |
| 15 | `FS.GI.DIST.CONTACT.HISTORY.RESERVED4` | `FsGiDistContactHistory_Reserved4` | TField |  |  |
| 16 | `FS.GI.DIST.CONTACT.HISTORY.RESERVED3` | `FsGiDistContactHistory_Reserved3` | TField |  |  |
| 17 | `FS.GI.DIST.CONTACT.HISTORY.RESERVED2` | `FsGiDistContactHistory_Reserved2` | TField |  |  |
| 18 | `FS.GI.DIST.CONTACT.HISTORY.RESERVED1` | `FsGiDistContactHistory_Reserved1` | TField |  |  |
| 19 | `FS.GI.DIST.CONTACT.HISTORY.LOCAL.REF` | `FsGiDistContactHistory_LocalRef` |  |  |  |
| 20 | `FS.GI.DIST.CONTACT.HISTORY.OVERRIDE` | `FsGiDistContactHistory_Override` |  |  |  |
| 21 | `FS.GI.DIST.CONTACT.HISTORY.RECORD.STATUS` | `FsGiDistContactHistory_RecordStatus` | String |  |  |
| 22 | `FS.GI.DIST.CONTACT.HISTORY.CURR.NO` | `FsGiDistContactHistory_CurrNo` | String |  |  |
| 23 | `FS.GI.DIST.CONTACT.HISTORY.INPUTTER` | `FsGiDistContactHistory_Inputter` |  |  |  |
| 24 | `FS.GI.DIST.CONTACT.HISTORY.DATE.TIME` | `FsGiDistContactHistory_DateTime` |  |  |  |
| 25 | `FS.GI.DIST.CONTACT.HISTORY.AUTHORISER` | `FsGiDistContactHistory_Authoriser` | String |  |  |
| 26 | `FS.GI.DIST.CONTACT.HISTORY.CO.CODE` | `FsGiDistContactHistory_CoCode` | String |  |  |
| 27 | `FS.GI.DIST.CONTACT.HISTORY.DEPT.CODE` | `FsGiDistContactHistory_DeptCode` | String |  |  |
| 28 | `FS.GI.DIST.CONTACT.HISTORY.AUDITOR.CODE` | `FsGiDistContactHistory_AuditorCode` | String |  |  |
| 29 | `FS.GI.DIST.CONTACT.HISTORY.AUDIT.DATE.TIME` | `FsGiDistContactHistory_AuditDateTime` | String |  |  |
