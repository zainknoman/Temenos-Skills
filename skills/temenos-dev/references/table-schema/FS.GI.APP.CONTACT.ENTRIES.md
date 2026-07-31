# FS.GI.APP.CONTACT.ENTRIES — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.CONTACT.ENTRIES` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.CONTACT.ENTRIES.PARENT.REF.ID` | `FsGiAppContactEntries_ParentRefId` |  |  |  |
| 2 | `FS.GI.APP.CONTACT.ENTRIES.ORA.ROWID` | `FsGiAppContactEntries_OraRowid` |  |  |  |
| 3 | `FS.GI.APP.CONTACT.ENTRIES.CONTACT.ID` | `FsGiAppContactEntries_ContactId` |  |  |  |
| 4 | `FS.GI.APP.CONTACT.ENTRIES.GDPR.PROCESSED.FLAG` | `FsGiAppContactEntries_GdprProcessedFlag` |  |  |  |
| 5 | `FS.GI.APP.CONTACT.ENTRIES.NAME` | `FsGiAppContactEntries_Name` |  |  |  |
| 6 | `FS.GI.APP.CONTACT.ENTRIES.FIRSTNAME` | `FsGiAppContactEntries_Firstname` |  |  |  |
| 7 | `FS.GI.APP.CONTACT.ENTRIES.TITLE` | `FsGiAppContactEntries_Title` |  |  |  |
| 8 | `FS.GI.APP.CONTACT.ENTRIES.LANGUAGE.CODE` | `FsGiAppContactEntries_LanguageCode` |  |  |  |
| 9 | `FS.GI.APP.CONTACT.ENTRIES.COMMUNICATION.CHANNEL` | `FsGiAppContactEntries_CommunicationChannel` |  |  |  |
| 10 | `FS.GI.APP.CONTACT.ENTRIES.PARENT.TYPE` | `FsGiAppContactEntries_ParentType` |  |  |  |
| 11 | `FS.GI.APP.CONTACT.ENTRIES.PARENT.ID.TYPE` | `FsGiAppContactEntries_ParentIdType` |  |  |  |
| 12 | `FS.GI.APP.CONTACT.ENTRIES.ADDRESS` | `FsGiAppContactEntries_Address` |  |  |  |
| 13 | `FS.GI.APP.CONTACT.ENTRIES.PGP.KEY` | `FsGiAppContactEntries_PgpKey` |  |  |  |
| 14 | `FS.GI.APP.CONTACT.ENTRIES.GDPR.INFORM.DATE` | `FsGiAppContactEntries_GdprInformDate` |  |  |  |
| 15 | `FS.GI.APP.CONTACT.ENTRIES.KEY.REFERENCE` | `FsGiAppContactEntries_KeyReference` |  |  |  |
| 16 | `FS.GI.APP.CONTACT.ENTRIES.KEY.SENDING.CHANNEL` | `FsGiAppContactEntries_KeySendingChannel` |  |  |  |
| 17 | `FS.GI.APP.CONTACT.ENTRIES.FOR.ATTENTION.OF` | `FsGiAppContactEntries_ForAttentionOf` |  |  |  |
| 18 | `FS.GI.APP.CONTACT.ENTRIES.KEY.FAX` | `FsGiAppContactEntries_KeyFax` |  |  |  |
| 19 | `FS.GI.APP.CONTACT.ENTRIES.KEY.ADDRESS.1` | `FsGiAppContactEntries_KeyAddress1` |  |  |  |
| 20 | `FS.GI.APP.CONTACT.ENTRIES.KEY.ADDRESS.2` | `FsGiAppContactEntries_KeyAddress2` |  |  |  |
| 21 | `FS.GI.APP.CONTACT.ENTRIES.KEY.ADDRESS.3` | `FsGiAppContactEntries_KeyAddress3` |  |  |  |
| 22 | `FS.GI.APP.CONTACT.ENTRIES.KEY.ADDRESS.4` | `FsGiAppContactEntries_KeyAddress4` |  |  |  |
| 23 | `FS.GI.APP.CONTACT.ENTRIES.KEY.ADDRESS.5` | `FsGiAppContactEntries_KeyAddress5` |  |  |  |
| 24 | `FS.GI.APP.CONTACT.ENTRIES.KEY.ADDRESS.6` | `FsGiAppContactEntries_KeyAddress6` |  |  |  |
| 25 | `FS.GI.APP.CONTACT.ENTRIES.ENCRYPTED.FILE.EXTENSION` | `FsGiAppContactEntries_EncryptedFileExtension` |  |  |  |
| 26 | `FS.GI.APP.CONTACT.ENTRIES.COMPRESSION.FILE.EXTENSION` | `FsGiAppContactEntries_CompressionFileExtension` |  |  |  |
| 27 | `FS.GI.APP.CONTACT.ENTRIES.FLAG.EMAIL.NOTIFICATION` | `FsGiAppContactEntries_FlagEmailNotification` |  |  |  |
| 28 | `FS.GI.APP.CONTACT.ENTRIES.EMAIL.ADDRESS` | `FsGiAppContactEntries_EmailAddress` |  |  |  |
| 29 | `FS.GI.APP.CONTACT.ENTRIES.RIGHT.TYPE` | `FsGiAppContactEntries_RightType` |  |  |  |
| 30 | `FS.GI.APP.CONTACT.ENTRIES.PII.DISCLOSURE` | `FsGiAppContactEntries_PiiDisclosure` |  |  |  |
| 31 | `FS.GI.APP.CONTACT.ENTRIES.RESERVED10` | `FsGiAppContactEntries_Reserved10` |  |  |  |
| 32 | `FS.GI.APP.CONTACT.ENTRIES.RESERVED9` | `FsGiAppContactEntries_Reserved9` |  |  |  |
| 33 | `FS.GI.APP.CONTACT.ENTRIES.RESERVED8` | `FsGiAppContactEntries_Reserved8` |  |  |  |
| 34 | `FS.GI.APP.CONTACT.ENTRIES.RESERVED7` | `FsGiAppContactEntries_Reserved7` |  |  |  |
| 35 | `FS.GI.APP.CONTACT.ENTRIES.RESERVED6` | `FsGiAppContactEntries_Reserved6` |  |  |  |
| 36 | `FS.GI.APP.CONTACT.ENTRIES.RESERVED5` | `FsGiAppContactEntries_Reserved5` |  |  |  |
| 37 | `FS.GI.APP.CONTACT.ENTRIES.RESERVED4` | `FsGiAppContactEntries_Reserved4` |  |  |  |
| 38 | `FS.GI.APP.CONTACT.ENTRIES.RESERVED3` | `FsGiAppContactEntries_Reserved3` |  |  |  |
| 39 | `FS.GI.APP.CONTACT.ENTRIES.RESERVED2` | `FsGiAppContactEntries_Reserved2` |  |  |  |
| 40 | `FS.GI.APP.CONTACT.ENTRIES.RESERVED1` | `FsGiAppContactEntries_Reserved1` |  |  |  |
| 41 | `FS.GI.APP.CONTACT.ENTRIES.LOCAL.REF` | `FsGiAppContactEntries_LocalRef` |  |  |  |
| 42 | `FS.GI.APP.CONTACT.ENTRIES.OVERRIDE` | `FsGiAppContactEntries_Override` |  |  |  |
| 43 | `FS.GI.APP.CONTACT.ENTRIES.RECORD.STATUS` | `FsGiAppContactEntries_RecordStatus` |  |  |  |
| 44 | `FS.GI.APP.CONTACT.ENTRIES.CURR.NO` | `FsGiAppContactEntries_CurrNo` |  |  |  |
| 45 | `FS.GI.APP.CONTACT.ENTRIES.INPUTTER` | `FsGiAppContactEntries_Inputter` |  |  |  |
| 46 | `FS.GI.APP.CONTACT.ENTRIES.DATE.TIME` | `FsGiAppContactEntries_DateTime` |  |  |  |
| 47 | `FS.GI.APP.CONTACT.ENTRIES.AUTHORISER` | `FsGiAppContactEntries_Authoriser` |  |  |  |
| 48 | `FS.GI.APP.CONTACT.ENTRIES.CO.CODE` | `FsGiAppContactEntries_CoCode` |  |  |  |
| 49 | `FS.GI.APP.CONTACT.ENTRIES.DEPT.CODE` | `FsGiAppContactEntries_DeptCode` |  |  |  |
| 50 | `FS.GI.APP.CONTACT.ENTRIES.AUDITOR.CODE` | `FsGiAppContactEntries_AuditorCode` |  |  |  |
| 51 | `FS.GI.APP.CONTACT.ENTRIES.AUDIT.DATE.TIME` | `FsGiAppContactEntries_AuditDateTime` |  |  |  |
