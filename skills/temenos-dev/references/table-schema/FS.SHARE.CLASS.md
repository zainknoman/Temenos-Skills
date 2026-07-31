# FS.SHARE.CLASS — Table Schema

> Source: `INSERTS/I_F.FS.SHARE.CLASS` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.SHARE.CLASS.DESCRIPTION` | `FsShareClass_Description` |  |  |  |
| 2 | `FS.SHARE.CLASS.FILTER.KEY` | `FsShareClass_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.SHARE.CLASS.RECORD.ID` | `FsShareClass_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.SHARE.CLASS.RESERVED10` | `FsShareClass_Reserved10` | TField |  |  |
| 5 | `FS.SHARE.CLASS.RESERVED9` | `FsShareClass_Reserved9` | TField |  |  |
| 6 | `FS.SHARE.CLASS.RESERVED8` | `FsShareClass_Reserved8` | TField |  |  |
| 7 | `FS.SHARE.CLASS.RESERVED7` | `FsShareClass_Reserved7` | TField |  |  |
| 8 | `FS.SHARE.CLASS.RESERVED6` | `FsShareClass_Reserved6` | TField |  |  |
| 9 | `FS.SHARE.CLASS.RESERVED5` | `FsShareClass_Reserved5` | TField |  |  |
| 10 | `FS.SHARE.CLASS.RESERVED4` | `FsShareClass_Reserved4` | TField |  |  |
| 11 | `FS.SHARE.CLASS.RESERVED3` | `FsShareClass_Reserved3` | TField |  |  |
| 12 | `FS.SHARE.CLASS.RESERVED2` | `FsShareClass_Reserved2` | TField |  |  |
| 13 | `FS.SHARE.CLASS.RESERVED1` | `FsShareClass_Reserved1` | TField |  |  |
| 14 | `FS.SHARE.CLASS.LOCAL.REF` | `FsShareClass_LocalRef` |  |  |  |
| 15 | `FS.SHARE.CLASS.OVERRIDE` | `FsShareClass_Override` |  |  |  |
| 16 | `FS.SHARE.CLASS.RECORD.STATUS` | `FsShareClass_RecordStatus` | String |  |  |
| 17 | `FS.SHARE.CLASS.CURR.NO` | `FsShareClass_CurrNo` | String |  |  |
| 18 | `FS.SHARE.CLASS.INPUTTER` | `FsShareClass_Inputter` |  |  |  |
| 19 | `FS.SHARE.CLASS.DATE.TIME` | `FsShareClass_DateTime` |  |  |  |
| 20 | `FS.SHARE.CLASS.AUTHORISER` | `FsShareClass_Authoriser` | String |  |  |
| 21 | `FS.SHARE.CLASS.CO.CODE` | `FsShareClass_CoCode` | String |  |  |
| 22 | `FS.SHARE.CLASS.DEPT.CODE` | `FsShareClass_DeptCode` | String |  |  |
| 23 | `FS.SHARE.CLASS.AUDITOR.CODE` | `FsShareClass_AuditorCode` | String |  |  |
| 24 | `FS.SHARE.CLASS.AUDIT.DATE.TIME` | `FsShareClass_AuditDateTime` | String |  |  |
