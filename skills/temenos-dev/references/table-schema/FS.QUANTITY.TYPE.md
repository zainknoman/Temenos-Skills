# FS.QUANTITY.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.QUANTITY.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.QUANTITY.TYPE.DESCRIPTION` | `FsQuantityType_Description` |  |  |  |
| 2 | `FS.QUANTITY.TYPE.FILTER.KEY` | `FsQuantityType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.QUANTITY.TYPE.RECORD.ID` | `FsQuantityType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.QUANTITY.TYPE.RESERVED10` | `FsQuantityType_Reserved10` | TField |  |  |
| 5 | `FS.QUANTITY.TYPE.RESERVED9` | `FsQuantityType_Reserved9` | TField |  |  |
| 6 | `FS.QUANTITY.TYPE.RESERVED8` | `FsQuantityType_Reserved8` | TField |  |  |
| 7 | `FS.QUANTITY.TYPE.RESERVED7` | `FsQuantityType_Reserved7` | TField |  |  |
| 8 | `FS.QUANTITY.TYPE.RESERVED6` | `FsQuantityType_Reserved6` | TField |  |  |
| 9 | `FS.QUANTITY.TYPE.RESERVED5` | `FsQuantityType_Reserved5` | TField |  |  |
| 10 | `FS.QUANTITY.TYPE.RESERVED4` | `FsQuantityType_Reserved4` | TField |  |  |
| 11 | `FS.QUANTITY.TYPE.RESERVED3` | `FsQuantityType_Reserved3` | TField |  |  |
| 12 | `FS.QUANTITY.TYPE.RESERVED2` | `FsQuantityType_Reserved2` | TField |  |  |
| 13 | `FS.QUANTITY.TYPE.RESERVED1` | `FsQuantityType_Reserved1` | TField |  |  |
| 14 | `FS.QUANTITY.TYPE.LOCAL.REF` | `FsQuantityType_LocalRef` |  |  |  |
| 15 | `FS.QUANTITY.TYPE.OVERRIDE` | `FsQuantityType_Override` |  |  |  |
| 16 | `FS.QUANTITY.TYPE.RECORD.STATUS` | `FsQuantityType_RecordStatus` | String |  |  |
| 17 | `FS.QUANTITY.TYPE.CURR.NO` | `FsQuantityType_CurrNo` | String |  |  |
| 18 | `FS.QUANTITY.TYPE.INPUTTER` | `FsQuantityType_Inputter` |  |  |  |
| 19 | `FS.QUANTITY.TYPE.DATE.TIME` | `FsQuantityType_DateTime` |  |  |  |
| 20 | `FS.QUANTITY.TYPE.AUTHORISER` | `FsQuantityType_Authoriser` | String |  |  |
| 21 | `FS.QUANTITY.TYPE.CO.CODE` | `FsQuantityType_CoCode` | String |  |  |
| 22 | `FS.QUANTITY.TYPE.DEPT.CODE` | `FsQuantityType_DeptCode` | String |  |  |
| 23 | `FS.QUANTITY.TYPE.AUDITOR.CODE` | `FsQuantityType_AuditorCode` | String |  |  |
| 24 | `FS.QUANTITY.TYPE.AUDIT.DATE.TIME` | `FsQuantityType_AuditDateTime` | String |  |  |
