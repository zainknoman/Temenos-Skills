# FS.CATEGORY — Table Schema

> Source: `INSERTS/I_F.FS.CATEGORY` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.CATEGORY.DESCRIPTION` | `FsCategory_Description` |  |  |  |
| 2 | `FS.CATEGORY.FILTER.KEY` | `FsCategory_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.CATEGORY.RECORD.ID` | `FsCategory_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.CATEGORY.RESERVED10` | `FsCategory_Reserved10` | TField |  |  |
| 5 | `FS.CATEGORY.RESERVED9` | `FsCategory_Reserved9` | TField |  |  |
| 6 | `FS.CATEGORY.RESERVED8` | `FsCategory_Reserved8` | TField |  |  |
| 7 | `FS.CATEGORY.RESERVED7` | `FsCategory_Reserved7` | TField |  |  |
| 8 | `FS.CATEGORY.RESERVED6` | `FsCategory_Reserved6` | TField |  |  |
| 9 | `FS.CATEGORY.RESERVED5` | `FsCategory_Reserved5` | TField |  |  |
| 10 | `FS.CATEGORY.RESERVED4` | `FsCategory_Reserved4` | TField |  |  |
| 11 | `FS.CATEGORY.RESERVED3` | `FsCategory_Reserved3` | TField |  |  |
| 12 | `FS.CATEGORY.RESERVED2` | `FsCategory_Reserved2` | TField |  |  |
| 13 | `FS.CATEGORY.RESERVED1` | `FsCategory_Reserved1` | TField |  |  |
| 14 | `FS.CATEGORY.LOCAL.REF` | `FsCategory_LocalRef` |  |  |  |
| 15 | `FS.CATEGORY.OVERRIDE` | `FsCategory_Override` |  |  |  |
| 16 | `FS.CATEGORY.RECORD.STATUS` | `FsCategory_RecordStatus` | String |  |  |
| 17 | `FS.CATEGORY.CURR.NO` | `FsCategory_CurrNo` | String |  |  |
| 18 | `FS.CATEGORY.INPUTTER` | `FsCategory_Inputter` |  |  |  |
| 19 | `FS.CATEGORY.DATE.TIME` | `FsCategory_DateTime` |  |  |  |
| 20 | `FS.CATEGORY.AUTHORISER` | `FsCategory_Authoriser` | String |  |  |
| 21 | `FS.CATEGORY.CO.CODE` | `FsCategory_CoCode` | String |  |  |
| 22 | `FS.CATEGORY.DEPT.CODE` | `FsCategory_DeptCode` | String |  |  |
| 23 | `FS.CATEGORY.AUDITOR.CODE` | `FsCategory_AuditorCode` | String |  |  |
| 24 | `FS.CATEGORY.AUDIT.DATE.TIME` | `FsCategory_AuditDateTime` | String |  |  |
