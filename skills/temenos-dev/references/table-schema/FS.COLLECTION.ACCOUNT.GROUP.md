# FS.COLLECTION.ACCOUNT.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.COLLECTION.ACCOUNT.GROUP` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.COLLECTION.ACCOUNT.GROUP.DESCRIPTION` | `FsCollectionAccountGroup_Description` |  |  |  |
| 2 | `FS.COLLECTION.ACCOUNT.GROUP.FILTER.KEY` | `FsCollectionAccountGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.COLLECTION.ACCOUNT.GROUP.RECORD.ID` | `FsCollectionAccountGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.COLLECTION.ACCOUNT.GROUP.RESERVED10` | `FsCollectionAccountGroup_Reserved10` | TField |  |  |
| 5 | `FS.COLLECTION.ACCOUNT.GROUP.RESERVED9` | `FsCollectionAccountGroup_Reserved9` | TField |  |  |
| 6 | `FS.COLLECTION.ACCOUNT.GROUP.RESERVED8` | `FsCollectionAccountGroup_Reserved8` | TField |  |  |
| 7 | `FS.COLLECTION.ACCOUNT.GROUP.RESERVED7` | `FsCollectionAccountGroup_Reserved7` | TField |  |  |
| 8 | `FS.COLLECTION.ACCOUNT.GROUP.RESERVED6` | `FsCollectionAccountGroup_Reserved6` | TField |  |  |
| 9 | `FS.COLLECTION.ACCOUNT.GROUP.RESERVED5` | `FsCollectionAccountGroup_Reserved5` | TField |  |  |
| 10 | `FS.COLLECTION.ACCOUNT.GROUP.RESERVED4` | `FsCollectionAccountGroup_Reserved4` | TField |  |  |
| 11 | `FS.COLLECTION.ACCOUNT.GROUP.RESERVED3` | `FsCollectionAccountGroup_Reserved3` | TField |  |  |
| 12 | `FS.COLLECTION.ACCOUNT.GROUP.RESERVED2` | `FsCollectionAccountGroup_Reserved2` | TField |  |  |
| 13 | `FS.COLLECTION.ACCOUNT.GROUP.RESERVED1` | `FsCollectionAccountGroup_Reserved1` | TField |  |  |
| 14 | `FS.COLLECTION.ACCOUNT.GROUP.LOCAL.REF` | `FsCollectionAccountGroup_LocalRef` |  |  |  |
| 15 | `FS.COLLECTION.ACCOUNT.GROUP.OVERRIDE` | `FsCollectionAccountGroup_Override` |  |  |  |
| 16 | `FS.COLLECTION.ACCOUNT.GROUP.RECORD.STATUS` | `FsCollectionAccountGroup_RecordStatus` | String |  |  |
| 17 | `FS.COLLECTION.ACCOUNT.GROUP.CURR.NO` | `FsCollectionAccountGroup_CurrNo` | String |  |  |
| 18 | `FS.COLLECTION.ACCOUNT.GROUP.INPUTTER` | `FsCollectionAccountGroup_Inputter` |  |  |  |
| 19 | `FS.COLLECTION.ACCOUNT.GROUP.DATE.TIME` | `FsCollectionAccountGroup_DateTime` |  |  |  |
| 20 | `FS.COLLECTION.ACCOUNT.GROUP.AUTHORISER` | `FsCollectionAccountGroup_Authoriser` | String |  |  |
| 21 | `FS.COLLECTION.ACCOUNT.GROUP.CO.CODE` | `FsCollectionAccountGroup_CoCode` | String |  |  |
| 22 | `FS.COLLECTION.ACCOUNT.GROUP.DEPT.CODE` | `FsCollectionAccountGroup_DeptCode` | String |  |  |
| 23 | `FS.COLLECTION.ACCOUNT.GROUP.AUDITOR.CODE` | `FsCollectionAccountGroup_AuditorCode` | String |  |  |
| 24 | `FS.COLLECTION.ACCOUNT.GROUP.AUDIT.DATE.TIME` | `FsCollectionAccountGroup_AuditDateTime` | String |  |  |
