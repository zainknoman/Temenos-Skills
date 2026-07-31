# FS.ASSETCLASS — Table Schema

> Source: `INSERTS/I_F.FS.ASSETCLASS` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ASSETCLASS.DESCRIPTION` | `FsAssetclass_Description` |  |  |  |
| 2 | `FS.ASSETCLASS.FILTER.KEY` | `FsAssetclass_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ASSETCLASS.RECORD.ID` | `FsAssetclass_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ASSETCLASS.RESERVED10` | `FsAssetclass_Reserved10` | TField |  |  |
| 5 | `FS.ASSETCLASS.RESERVED9` | `FsAssetclass_Reserved9` | TField |  |  |
| 6 | `FS.ASSETCLASS.RESERVED8` | `FsAssetclass_Reserved8` | TField |  |  |
| 7 | `FS.ASSETCLASS.RESERVED7` | `FsAssetclass_Reserved7` | TField |  |  |
| 8 | `FS.ASSETCLASS.RESERVED6` | `FsAssetclass_Reserved6` | TField |  |  |
| 9 | `FS.ASSETCLASS.RESERVED5` | `FsAssetclass_Reserved5` | TField |  |  |
| 10 | `FS.ASSETCLASS.RESERVED4` | `FsAssetclass_Reserved4` | TField |  |  |
| 11 | `FS.ASSETCLASS.RESERVED3` | `FsAssetclass_Reserved3` | TField |  |  |
| 12 | `FS.ASSETCLASS.RESERVED2` | `FsAssetclass_Reserved2` | TField |  |  |
| 13 | `FS.ASSETCLASS.RESERVED1` | `FsAssetclass_Reserved1` | TField |  |  |
| 14 | `FS.ASSETCLASS.LOCAL.REF` | `FsAssetclass_LocalRef` |  |  |  |
| 15 | `FS.ASSETCLASS.OVERRIDE` | `FsAssetclass_Override` |  |  |  |
| 16 | `FS.ASSETCLASS.RECORD.STATUS` | `FsAssetclass_RecordStatus` | String |  |  |
| 17 | `FS.ASSETCLASS.CURR.NO` | `FsAssetclass_CurrNo` | String |  |  |
| 18 | `FS.ASSETCLASS.INPUTTER` | `FsAssetclass_Inputter` |  |  |  |
| 19 | `FS.ASSETCLASS.DATE.TIME` | `FsAssetclass_DateTime` |  |  |  |
| 20 | `FS.ASSETCLASS.AUTHORISER` | `FsAssetclass_Authoriser` | String |  |  |
| 21 | `FS.ASSETCLASS.CO.CODE` | `FsAssetclass_CoCode` | String |  |  |
| 22 | `FS.ASSETCLASS.DEPT.CODE` | `FsAssetclass_DeptCode` | String |  |  |
| 23 | `FS.ASSETCLASS.AUDITOR.CODE` | `FsAssetclass_AuditorCode` | String |  |  |
| 24 | `FS.ASSETCLASS.AUDIT.DATE.TIME` | `FsAssetclass_AuditDateTime` | String |  |  |
