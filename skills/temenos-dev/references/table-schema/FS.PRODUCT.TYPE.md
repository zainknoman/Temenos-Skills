# FS.PRODUCT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.PRODUCT.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.PRODUCT.TYPE.DESCRIPTION` | `FsProductType_Description` |  |  |  |
| 2 | `FS.PRODUCT.TYPE.FILTER.KEY` | `FsProductType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.PRODUCT.TYPE.RECORD.ID` | `FsProductType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.PRODUCT.TYPE.RESERVED10` | `FsProductType_Reserved10` | TField |  |  |
| 5 | `FS.PRODUCT.TYPE.RESERVED9` | `FsProductType_Reserved9` | TField |  |  |
| 6 | `FS.PRODUCT.TYPE.RESERVED8` | `FsProductType_Reserved8` | TField |  |  |
| 7 | `FS.PRODUCT.TYPE.RESERVED7` | `FsProductType_Reserved7` | TField |  |  |
| 8 | `FS.PRODUCT.TYPE.RESERVED6` | `FsProductType_Reserved6` | TField |  |  |
| 9 | `FS.PRODUCT.TYPE.RESERVED5` | `FsProductType_Reserved5` | TField |  |  |
| 10 | `FS.PRODUCT.TYPE.RESERVED4` | `FsProductType_Reserved4` | TField |  |  |
| 11 | `FS.PRODUCT.TYPE.RESERVED3` | `FsProductType_Reserved3` | TField |  |  |
| 12 | `FS.PRODUCT.TYPE.RESERVED2` | `FsProductType_Reserved2` | TField |  |  |
| 13 | `FS.PRODUCT.TYPE.RESERVED1` | `FsProductType_Reserved1` | TField |  |  |
| 14 | `FS.PRODUCT.TYPE.LOCAL.REF` | `FsProductType_LocalRef` |  |  |  |
| 15 | `FS.PRODUCT.TYPE.OVERRIDE` | `FsProductType_Override` |  |  |  |
| 16 | `FS.PRODUCT.TYPE.RECORD.STATUS` | `FsProductType_RecordStatus` | String |  |  |
| 17 | `FS.PRODUCT.TYPE.CURR.NO` | `FsProductType_CurrNo` | String |  |  |
| 18 | `FS.PRODUCT.TYPE.INPUTTER` | `FsProductType_Inputter` |  |  |  |
| 19 | `FS.PRODUCT.TYPE.DATE.TIME` | `FsProductType_DateTime` |  |  |  |
| 20 | `FS.PRODUCT.TYPE.AUTHORISER` | `FsProductType_Authoriser` | String |  |  |
| 21 | `FS.PRODUCT.TYPE.CO.CODE` | `FsProductType_CoCode` | String |  |  |
| 22 | `FS.PRODUCT.TYPE.DEPT.CODE` | `FsProductType_DeptCode` | String |  |  |
| 23 | `FS.PRODUCT.TYPE.AUDITOR.CODE` | `FsProductType_AuditorCode` | String |  |  |
| 24 | `FS.PRODUCT.TYPE.AUDIT.DATE.TIME` | `FsProductType_AuditDateTime` | String |  |  |
