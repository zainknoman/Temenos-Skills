# FS.PROVIDER — Table Schema

> Source: `INSERTS/I_F.FS.PROVIDER` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.PROVIDER.DESCRIPTION` | `FsProvider_Description` |  |  |  |
| 2 | `FS.PROVIDER.FILTER.KEY` | `FsProvider_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.PROVIDER.RECORD.ID` | `FsProvider_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.PROVIDER.RESERVED10` | `FsProvider_Reserved10` | TField |  |  |
| 5 | `FS.PROVIDER.RESERVED9` | `FsProvider_Reserved9` | TField |  |  |
| 6 | `FS.PROVIDER.RESERVED8` | `FsProvider_Reserved8` | TField |  |  |
| 7 | `FS.PROVIDER.RESERVED7` | `FsProvider_Reserved7` | TField |  |  |
| 8 | `FS.PROVIDER.RESERVED6` | `FsProvider_Reserved6` | TField |  |  |
| 9 | `FS.PROVIDER.RESERVED5` | `FsProvider_Reserved5` | TField |  |  |
| 10 | `FS.PROVIDER.RESERVED4` | `FsProvider_Reserved4` | TField |  |  |
| 11 | `FS.PROVIDER.RESERVED3` | `FsProvider_Reserved3` | TField |  |  |
| 12 | `FS.PROVIDER.RESERVED2` | `FsProvider_Reserved2` | TField |  |  |
| 13 | `FS.PROVIDER.RESERVED1` | `FsProvider_Reserved1` | TField |  |  |
| 14 | `FS.PROVIDER.LOCAL.REF` | `FsProvider_LocalRef` |  |  |  |
| 15 | `FS.PROVIDER.OVERRIDE` | `FsProvider_Override` |  |  |  |
| 16 | `FS.PROVIDER.RECORD.STATUS` | `FsProvider_RecordStatus` | String |  |  |
| 17 | `FS.PROVIDER.CURR.NO` | `FsProvider_CurrNo` | String |  |  |
| 18 | `FS.PROVIDER.INPUTTER` | `FsProvider_Inputter` |  |  |  |
| 19 | `FS.PROVIDER.DATE.TIME` | `FsProvider_DateTime` |  |  |  |
| 20 | `FS.PROVIDER.AUTHORISER` | `FsProvider_Authoriser` | String |  |  |
| 21 | `FS.PROVIDER.CO.CODE` | `FsProvider_CoCode` | String |  |  |
| 22 | `FS.PROVIDER.DEPT.CODE` | `FsProvider_DeptCode` | String |  |  |
| 23 | `FS.PROVIDER.AUDITOR.CODE` | `FsProvider_AuditorCode` | String |  |  |
| 24 | `FS.PROVIDER.AUDIT.DATE.TIME` | `FsProvider_AuditDateTime` | String |  |  |
