# FS.EXPORT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.EXPORT.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.EXPORT.TYPE.DESCRIPTION` | `FsExportType_Description` |  |  |  |
| 2 | `FS.EXPORT.TYPE.FILTER.KEY` | `FsExportType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.EXPORT.TYPE.RECORD.ID` | `FsExportType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.EXPORT.TYPE.RESERVED10` | `FsExportType_Reserved10` | TField |  |  |
| 5 | `FS.EXPORT.TYPE.RESERVED9` | `FsExportType_Reserved9` | TField |  |  |
| 6 | `FS.EXPORT.TYPE.RESERVED8` | `FsExportType_Reserved8` | TField |  |  |
| 7 | `FS.EXPORT.TYPE.RESERVED7` | `FsExportType_Reserved7` | TField |  |  |
| 8 | `FS.EXPORT.TYPE.RESERVED6` | `FsExportType_Reserved6` | TField |  |  |
| 9 | `FS.EXPORT.TYPE.RESERVED5` | `FsExportType_Reserved5` | TField |  |  |
| 10 | `FS.EXPORT.TYPE.RESERVED4` | `FsExportType_Reserved4` | TField |  |  |
| 11 | `FS.EXPORT.TYPE.RESERVED3` | `FsExportType_Reserved3` | TField |  |  |
| 12 | `FS.EXPORT.TYPE.RESERVED2` | `FsExportType_Reserved2` | TField |  |  |
| 13 | `FS.EXPORT.TYPE.RESERVED1` | `FsExportType_Reserved1` | TField |  |  |
| 14 | `FS.EXPORT.TYPE.LOCAL.REF` | `FsExportType_LocalRef` |  |  |  |
| 15 | `FS.EXPORT.TYPE.OVERRIDE` | `FsExportType_Override` |  |  |  |
| 16 | `FS.EXPORT.TYPE.RECORD.STATUS` | `FsExportType_RecordStatus` | String |  |  |
| 17 | `FS.EXPORT.TYPE.CURR.NO` | `FsExportType_CurrNo` | String |  |  |
| 18 | `FS.EXPORT.TYPE.INPUTTER` | `FsExportType_Inputter` |  |  |  |
| 19 | `FS.EXPORT.TYPE.DATE.TIME` | `FsExportType_DateTime` |  |  |  |
| 20 | `FS.EXPORT.TYPE.AUTHORISER` | `FsExportType_Authoriser` | String |  |  |
| 21 | `FS.EXPORT.TYPE.CO.CODE` | `FsExportType_CoCode` | String |  |  |
| 22 | `FS.EXPORT.TYPE.DEPT.CODE` | `FsExportType_DeptCode` | String |  |  |
| 23 | `FS.EXPORT.TYPE.AUDITOR.CODE` | `FsExportType_AuditorCode` | String |  |  |
| 24 | `FS.EXPORT.TYPE.AUDIT.DATE.TIME` | `FsExportType_AuditDateTime` | String |  |  |
