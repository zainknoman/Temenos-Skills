# FS.ASSETCLASS.PRICING.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.ASSETCLASS.PRICING.GROUP` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ASSETCLASS.PRICING.GROUP.DESCRIPTION` | `FsAssetclassPricingGroup_Description` |  |  |  |
| 2 | `FS.ASSETCLASS.PRICING.GROUP.FILTER.KEY` | `FsAssetclassPricingGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ASSETCLASS.PRICING.GROUP.RECORD.ID` | `FsAssetclassPricingGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ASSETCLASS.PRICING.GROUP.RESERVED10` | `FsAssetclassPricingGroup_Reserved10` | TField |  |  |
| 5 | `FS.ASSETCLASS.PRICING.GROUP.RESERVED9` | `FsAssetclassPricingGroup_Reserved9` | TField |  |  |
| 6 | `FS.ASSETCLASS.PRICING.GROUP.RESERVED8` | `FsAssetclassPricingGroup_Reserved8` | TField |  |  |
| 7 | `FS.ASSETCLASS.PRICING.GROUP.RESERVED7` | `FsAssetclassPricingGroup_Reserved7` | TField |  |  |
| 8 | `FS.ASSETCLASS.PRICING.GROUP.RESERVED6` | `FsAssetclassPricingGroup_Reserved6` | TField |  |  |
| 9 | `FS.ASSETCLASS.PRICING.GROUP.RESERVED5` | `FsAssetclassPricingGroup_Reserved5` | TField |  |  |
| 10 | `FS.ASSETCLASS.PRICING.GROUP.RESERVED4` | `FsAssetclassPricingGroup_Reserved4` | TField |  |  |
| 11 | `FS.ASSETCLASS.PRICING.GROUP.RESERVED3` | `FsAssetclassPricingGroup_Reserved3` | TField |  |  |
| 12 | `FS.ASSETCLASS.PRICING.GROUP.RESERVED2` | `FsAssetclassPricingGroup_Reserved2` | TField |  |  |
| 13 | `FS.ASSETCLASS.PRICING.GROUP.RESERVED1` | `FsAssetclassPricingGroup_Reserved1` | TField |  |  |
| 14 | `FS.ASSETCLASS.PRICING.GROUP.LOCAL.REF` | `FsAssetclassPricingGroup_LocalRef` |  |  |  |
| 15 | `FS.ASSETCLASS.PRICING.GROUP.OVERRIDE` | `FsAssetclassPricingGroup_Override` |  |  |  |
| 16 | `FS.ASSETCLASS.PRICING.GROUP.RECORD.STATUS` | `FsAssetclassPricingGroup_RecordStatus` | String |  |  |
| 17 | `FS.ASSETCLASS.PRICING.GROUP.CURR.NO` | `FsAssetclassPricingGroup_CurrNo` | String |  |  |
| 18 | `FS.ASSETCLASS.PRICING.GROUP.INPUTTER` | `FsAssetclassPricingGroup_Inputter` |  |  |  |
| 19 | `FS.ASSETCLASS.PRICING.GROUP.DATE.TIME` | `FsAssetclassPricingGroup_DateTime` |  |  |  |
| 20 | `FS.ASSETCLASS.PRICING.GROUP.AUTHORISER` | `FsAssetclassPricingGroup_Authoriser` | String |  |  |
| 21 | `FS.ASSETCLASS.PRICING.GROUP.CO.CODE` | `FsAssetclassPricingGroup_CoCode` | String |  |  |
| 22 | `FS.ASSETCLASS.PRICING.GROUP.DEPT.CODE` | `FsAssetclassPricingGroup_DeptCode` | String |  |  |
| 23 | `FS.ASSETCLASS.PRICING.GROUP.AUDITOR.CODE` | `FsAssetclassPricingGroup_AuditorCode` | String |  |  |
| 24 | `FS.ASSETCLASS.PRICING.GROUP.AUDIT.DATE.TIME` | `FsAssetclassPricingGroup_AuditDateTime` | String |  |  |
