# FS.IBOR.ASSET.SUBTYPE — Table Schema

> Source: `INSERTS/I_F.FS.IBOR.ASSET.SUBTYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.IBOR.ASSET.SUBTYPE.DESCRIPTION` | `FsIborAssetSubtype_Description` |  |  |  |
| 2 | `FS.IBOR.ASSET.SUBTYPE.FILTER.KEY` | `FsIborAssetSubtype_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.IBOR.ASSET.SUBTYPE.RECORD.ID` | `FsIborAssetSubtype_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.IBOR.ASSET.SUBTYPE.RESERVED10` | `FsIborAssetSubtype_Reserved10` | TField |  |  |
| 5 | `FS.IBOR.ASSET.SUBTYPE.RESERVED9` | `FsIborAssetSubtype_Reserved9` | TField |  |  |
| 6 | `FS.IBOR.ASSET.SUBTYPE.RESERVED8` | `FsIborAssetSubtype_Reserved8` | TField |  |  |
| 7 | `FS.IBOR.ASSET.SUBTYPE.RESERVED7` | `FsIborAssetSubtype_Reserved7` | TField |  |  |
| 8 | `FS.IBOR.ASSET.SUBTYPE.RESERVED6` | `FsIborAssetSubtype_Reserved6` | TField |  |  |
| 9 | `FS.IBOR.ASSET.SUBTYPE.RESERVED5` | `FsIborAssetSubtype_Reserved5` | TField |  |  |
| 10 | `FS.IBOR.ASSET.SUBTYPE.RESERVED4` | `FsIborAssetSubtype_Reserved4` | TField |  |  |
| 11 | `FS.IBOR.ASSET.SUBTYPE.RESERVED3` | `FsIborAssetSubtype_Reserved3` | TField |  |  |
| 12 | `FS.IBOR.ASSET.SUBTYPE.RESERVED2` | `FsIborAssetSubtype_Reserved2` | TField |  |  |
| 13 | `FS.IBOR.ASSET.SUBTYPE.RESERVED1` | `FsIborAssetSubtype_Reserved1` | TField |  |  |
| 14 | `FS.IBOR.ASSET.SUBTYPE.LOCAL.REF` | `FsIborAssetSubtype_LocalRef` |  |  |  |
| 15 | `FS.IBOR.ASSET.SUBTYPE.OVERRIDE` | `FsIborAssetSubtype_Override` |  |  |  |
| 16 | `FS.IBOR.ASSET.SUBTYPE.RECORD.STATUS` | `FsIborAssetSubtype_RecordStatus` | String |  |  |
| 17 | `FS.IBOR.ASSET.SUBTYPE.CURR.NO` | `FsIborAssetSubtype_CurrNo` | String |  |  |
| 18 | `FS.IBOR.ASSET.SUBTYPE.INPUTTER` | `FsIborAssetSubtype_Inputter` |  |  |  |
| 19 | `FS.IBOR.ASSET.SUBTYPE.DATE.TIME` | `FsIborAssetSubtype_DateTime` |  |  |  |
| 20 | `FS.IBOR.ASSET.SUBTYPE.AUTHORISER` | `FsIborAssetSubtype_Authoriser` | String |  |  |
| 21 | `FS.IBOR.ASSET.SUBTYPE.CO.CODE` | `FsIborAssetSubtype_CoCode` | String |  |  |
| 22 | `FS.IBOR.ASSET.SUBTYPE.DEPT.CODE` | `FsIborAssetSubtype_DeptCode` | String |  |  |
| 23 | `FS.IBOR.ASSET.SUBTYPE.AUDITOR.CODE` | `FsIborAssetSubtype_AuditorCode` | String |  |  |
| 24 | `FS.IBOR.ASSET.SUBTYPE.AUDIT.DATE.TIME` | `FsIborAssetSubtype_AuditDateTime` | String |  |  |
