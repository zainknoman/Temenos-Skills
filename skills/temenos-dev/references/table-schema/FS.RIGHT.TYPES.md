# FS.RIGHT.TYPES — Table Schema

> Source: `INSERTS/I_F.FS.RIGHT.TYPES` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.RIGHT.TYPES.DESCRIPTION` | `FsRightTypes_Description` |  |  |  |
| 2 | `FS.RIGHT.TYPES.FILTER.KEY` | `FsRightTypes_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.RIGHT.TYPES.RECORD.ID` | `FsRightTypes_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.RIGHT.TYPES.RESERVED10` | `FsRightTypes_Reserved10` | TField |  |  |
| 5 | `FS.RIGHT.TYPES.RESERVED9` | `FsRightTypes_Reserved9` | TField |  |  |
| 6 | `FS.RIGHT.TYPES.RESERVED8` | `FsRightTypes_Reserved8` | TField |  |  |
| 7 | `FS.RIGHT.TYPES.RESERVED7` | `FsRightTypes_Reserved7` | TField |  |  |
| 8 | `FS.RIGHT.TYPES.RESERVED6` | `FsRightTypes_Reserved6` | TField |  |  |
| 9 | `FS.RIGHT.TYPES.RESERVED5` | `FsRightTypes_Reserved5` | TField |  |  |
| 10 | `FS.RIGHT.TYPES.RESERVED4` | `FsRightTypes_Reserved4` | TField |  |  |
| 11 | `FS.RIGHT.TYPES.RESERVED3` | `FsRightTypes_Reserved3` | TField |  |  |
| 12 | `FS.RIGHT.TYPES.RESERVED2` | `FsRightTypes_Reserved2` | TField |  |  |
| 13 | `FS.RIGHT.TYPES.RESERVED1` | `FsRightTypes_Reserved1` | TField |  |  |
| 14 | `FS.RIGHT.TYPES.LOCAL.REF` | `FsRightTypes_LocalRef` |  |  |  |
| 15 | `FS.RIGHT.TYPES.OVERRIDE` | `FsRightTypes_Override` |  |  |  |
| 16 | `FS.RIGHT.TYPES.RECORD.STATUS` | `FsRightTypes_RecordStatus` | String |  |  |
| 17 | `FS.RIGHT.TYPES.CURR.NO` | `FsRightTypes_CurrNo` | String |  |  |
| 18 | `FS.RIGHT.TYPES.INPUTTER` | `FsRightTypes_Inputter` |  |  |  |
| 19 | `FS.RIGHT.TYPES.DATE.TIME` | `FsRightTypes_DateTime` |  |  |  |
| 20 | `FS.RIGHT.TYPES.AUTHORISER` | `FsRightTypes_Authoriser` | String |  |  |
| 21 | `FS.RIGHT.TYPES.CO.CODE` | `FsRightTypes_CoCode` | String |  |  |
| 22 | `FS.RIGHT.TYPES.DEPT.CODE` | `FsRightTypes_DeptCode` | String |  |  |
| 23 | `FS.RIGHT.TYPES.AUDITOR.CODE` | `FsRightTypes_AuditorCode` | String |  |  |
| 24 | `FS.RIGHT.TYPES.AUDIT.DATE.TIME` | `FsRightTypes_AuditDateTime` | String |  |  |
