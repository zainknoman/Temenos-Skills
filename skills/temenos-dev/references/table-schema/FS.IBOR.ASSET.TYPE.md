# FS.IBOR.ASSET.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.IBOR.ASSET.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.IBOR.ASSET.TYPE.DESCRIPTION` | `FsIborAssetType_Description` |  |  |  |
| 2 | `FS.IBOR.ASSET.TYPE.FILTER.KEY` | `FsIborAssetType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.IBOR.ASSET.TYPE.RECORD.ID` | `FsIborAssetType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.IBOR.ASSET.TYPE.RESERVED10` | `FsIborAssetType_Reserved10` | TField |  |  |
| 5 | `FS.IBOR.ASSET.TYPE.RESERVED9` | `FsIborAssetType_Reserved9` | TField |  |  |
| 6 | `FS.IBOR.ASSET.TYPE.RESERVED8` | `FsIborAssetType_Reserved8` | TField |  |  |
| 7 | `FS.IBOR.ASSET.TYPE.RESERVED7` | `FsIborAssetType_Reserved7` | TField |  |  |
| 8 | `FS.IBOR.ASSET.TYPE.RESERVED6` | `FsIborAssetType_Reserved6` | TField |  |  |
| 9 | `FS.IBOR.ASSET.TYPE.RESERVED5` | `FsIborAssetType_Reserved5` | TField |  |  |
| 10 | `FS.IBOR.ASSET.TYPE.RESERVED4` | `FsIborAssetType_Reserved4` | TField |  |  |
| 11 | `FS.IBOR.ASSET.TYPE.RESERVED3` | `FsIborAssetType_Reserved3` | TField |  |  |
| 12 | `FS.IBOR.ASSET.TYPE.RESERVED2` | `FsIborAssetType_Reserved2` | TField |  |  |
| 13 | `FS.IBOR.ASSET.TYPE.RESERVED1` | `FsIborAssetType_Reserved1` | TField |  |  |
| 14 | `FS.IBOR.ASSET.TYPE.LOCAL.REF` | `FsIborAssetType_LocalRef` |  |  |  |
| 15 | `FS.IBOR.ASSET.TYPE.OVERRIDE` | `FsIborAssetType_Override` |  |  |  |
| 16 | `FS.IBOR.ASSET.TYPE.RECORD.STATUS` | `FsIborAssetType_RecordStatus` | String |  |  |
| 17 | `FS.IBOR.ASSET.TYPE.CURR.NO` | `FsIborAssetType_CurrNo` | String |  |  |
| 18 | `FS.IBOR.ASSET.TYPE.INPUTTER` | `FsIborAssetType_Inputter` |  |  |  |
| 19 | `FS.IBOR.ASSET.TYPE.DATE.TIME` | `FsIborAssetType_DateTime` |  |  |  |
| 20 | `FS.IBOR.ASSET.TYPE.AUTHORISER` | `FsIborAssetType_Authoriser` | String |  |  |
| 21 | `FS.IBOR.ASSET.TYPE.CO.CODE` | `FsIborAssetType_CoCode` | String |  |  |
| 22 | `FS.IBOR.ASSET.TYPE.DEPT.CODE` | `FsIborAssetType_DeptCode` | String |  |  |
| 23 | `FS.IBOR.ASSET.TYPE.AUDITOR.CODE` | `FsIborAssetType_AuditorCode` | String |  |  |
| 24 | `FS.IBOR.ASSET.TYPE.AUDIT.DATE.TIME` | `FsIborAssetType_AuditDateTime` | String |  |  |
