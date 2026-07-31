# FS.EXPORT.FUNDTYPE — Table Schema

> Source: `INSERTS/I_F.FS.EXPORT.FUNDTYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.EXPORT.FUNDTYPE.DESCRIPTION` | `FsExportFundtype_Description` |  |  |  |
| 2 | `FS.EXPORT.FUNDTYPE.FILTER.KEY` | `FsExportFundtype_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.EXPORT.FUNDTYPE.RECORD.ID` | `FsExportFundtype_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.EXPORT.FUNDTYPE.RESERVED10` | `FsExportFundtype_Reserved10` | TField |  |  |
| 5 | `FS.EXPORT.FUNDTYPE.RESERVED9` | `FsExportFundtype_Reserved9` | TField |  |  |
| 6 | `FS.EXPORT.FUNDTYPE.RESERVED8` | `FsExportFundtype_Reserved8` | TField |  |  |
| 7 | `FS.EXPORT.FUNDTYPE.RESERVED7` | `FsExportFundtype_Reserved7` | TField |  |  |
| 8 | `FS.EXPORT.FUNDTYPE.RESERVED6` | `FsExportFundtype_Reserved6` | TField |  |  |
| 9 | `FS.EXPORT.FUNDTYPE.RESERVED5` | `FsExportFundtype_Reserved5` | TField |  |  |
| 10 | `FS.EXPORT.FUNDTYPE.RESERVED4` | `FsExportFundtype_Reserved4` | TField |  |  |
| 11 | `FS.EXPORT.FUNDTYPE.RESERVED3` | `FsExportFundtype_Reserved3` | TField |  |  |
| 12 | `FS.EXPORT.FUNDTYPE.RESERVED2` | `FsExportFundtype_Reserved2` | TField |  |  |
| 13 | `FS.EXPORT.FUNDTYPE.RESERVED1` | `FsExportFundtype_Reserved1` | TField |  |  |
| 14 | `FS.EXPORT.FUNDTYPE.LOCAL.REF` | `FsExportFundtype_LocalRef` |  |  |  |
| 15 | `FS.EXPORT.FUNDTYPE.OVERRIDE` | `FsExportFundtype_Override` |  |  |  |
| 16 | `FS.EXPORT.FUNDTYPE.RECORD.STATUS` | `FsExportFundtype_RecordStatus` | String |  |  |
| 17 | `FS.EXPORT.FUNDTYPE.CURR.NO` | `FsExportFundtype_CurrNo` | String |  |  |
| 18 | `FS.EXPORT.FUNDTYPE.INPUTTER` | `FsExportFundtype_Inputter` |  |  |  |
| 19 | `FS.EXPORT.FUNDTYPE.DATE.TIME` | `FsExportFundtype_DateTime` |  |  |  |
| 20 | `FS.EXPORT.FUNDTYPE.AUTHORISER` | `FsExportFundtype_Authoriser` | String |  |  |
| 21 | `FS.EXPORT.FUNDTYPE.CO.CODE` | `FsExportFundtype_CoCode` | String |  |  |
| 22 | `FS.EXPORT.FUNDTYPE.DEPT.CODE` | `FsExportFundtype_DeptCode` | String |  |  |
| 23 | `FS.EXPORT.FUNDTYPE.AUDITOR.CODE` | `FsExportFundtype_AuditorCode` | String |  |  |
| 24 | `FS.EXPORT.FUNDTYPE.AUDIT.DATE.TIME` | `FsExportFundtype_AuditDateTime` | String |  |  |
