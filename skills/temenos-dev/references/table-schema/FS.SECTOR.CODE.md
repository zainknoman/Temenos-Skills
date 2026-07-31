# FS.SECTOR.CODE — Table Schema

> Source: `INSERTS/I_F.FS.SECTOR.CODE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.SECTOR.CODE.DESCRIPTION` | `FsSectorCode_Description` |  |  |  |
| 2 | `FS.SECTOR.CODE.FILTER.KEY` | `FsSectorCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.SECTOR.CODE.RECORD.ID` | `FsSectorCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.SECTOR.CODE.RESERVED10` | `FsSectorCode_Reserved10` | TField |  |  |
| 5 | `FS.SECTOR.CODE.RESERVED9` | `FsSectorCode_Reserved9` | TField |  |  |
| 6 | `FS.SECTOR.CODE.RESERVED8` | `FsSectorCode_Reserved8` | TField |  |  |
| 7 | `FS.SECTOR.CODE.RESERVED7` | `FsSectorCode_Reserved7` | TField |  |  |
| 8 | `FS.SECTOR.CODE.RESERVED6` | `FsSectorCode_Reserved6` | TField |  |  |
| 9 | `FS.SECTOR.CODE.RESERVED5` | `FsSectorCode_Reserved5` | TField |  |  |
| 10 | `FS.SECTOR.CODE.RESERVED4` | `FsSectorCode_Reserved4` | TField |  |  |
| 11 | `FS.SECTOR.CODE.RESERVED3` | `FsSectorCode_Reserved3` | TField |  |  |
| 12 | `FS.SECTOR.CODE.RESERVED2` | `FsSectorCode_Reserved2` | TField |  |  |
| 13 | `FS.SECTOR.CODE.RESERVED1` | `FsSectorCode_Reserved1` | TField |  |  |
| 14 | `FS.SECTOR.CODE.LOCAL.REF` | `FsSectorCode_LocalRef` |  |  |  |
| 15 | `FS.SECTOR.CODE.OVERRIDE` | `FsSectorCode_Override` |  |  |  |
| 16 | `FS.SECTOR.CODE.RECORD.STATUS` | `FsSectorCode_RecordStatus` | String |  |  |
| 17 | `FS.SECTOR.CODE.CURR.NO` | `FsSectorCode_CurrNo` | String |  |  |
| 18 | `FS.SECTOR.CODE.INPUTTER` | `FsSectorCode_Inputter` |  |  |  |
| 19 | `FS.SECTOR.CODE.DATE.TIME` | `FsSectorCode_DateTime` |  |  |  |
| 20 | `FS.SECTOR.CODE.AUTHORISER` | `FsSectorCode_Authoriser` | String |  |  |
| 21 | `FS.SECTOR.CODE.CO.CODE` | `FsSectorCode_CoCode` | String |  |  |
| 22 | `FS.SECTOR.CODE.DEPT.CODE` | `FsSectorCode_DeptCode` | String |  |  |
| 23 | `FS.SECTOR.CODE.AUDITOR.CODE` | `FsSectorCode_AuditorCode` | String |  |  |
| 24 | `FS.SECTOR.CODE.AUDIT.DATE.TIME` | `FsSectorCode_AuditDateTime` | String |  |  |
