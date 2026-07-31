# FS.TRANSBLOCK.OPERATION — Table Schema

> Source: `INSERTS/I_F.FS.TRANSBLOCK.OPERATION` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.TRANSBLOCK.OPERATION.DESCRIPTION` | `FsTransblockOperation_Description` |  |  |  |
| 2 | `FS.TRANSBLOCK.OPERATION.FILTER.KEY` | `FsTransblockOperation_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.TRANSBLOCK.OPERATION.RECORD.ID` | `FsTransblockOperation_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.TRANSBLOCK.OPERATION.RESERVED10` | `FsTransblockOperation_Reserved10` | TField |  |  |
| 5 | `FS.TRANSBLOCK.OPERATION.RESERVED9` | `FsTransblockOperation_Reserved9` | TField |  |  |
| 6 | `FS.TRANSBLOCK.OPERATION.RESERVED8` | `FsTransblockOperation_Reserved8` | TField |  |  |
| 7 | `FS.TRANSBLOCK.OPERATION.RESERVED7` | `FsTransblockOperation_Reserved7` | TField |  |  |
| 8 | `FS.TRANSBLOCK.OPERATION.RESERVED6` | `FsTransblockOperation_Reserved6` | TField |  |  |
| 9 | `FS.TRANSBLOCK.OPERATION.RESERVED5` | `FsTransblockOperation_Reserved5` | TField |  |  |
| 10 | `FS.TRANSBLOCK.OPERATION.RESERVED4` | `FsTransblockOperation_Reserved4` | TField |  |  |
| 11 | `FS.TRANSBLOCK.OPERATION.RESERVED3` | `FsTransblockOperation_Reserved3` | TField |  |  |
| 12 | `FS.TRANSBLOCK.OPERATION.RESERVED2` | `FsTransblockOperation_Reserved2` | TField |  |  |
| 13 | `FS.TRANSBLOCK.OPERATION.RESERVED1` | `FsTransblockOperation_Reserved1` | TField |  |  |
| 14 | `FS.TRANSBLOCK.OPERATION.LOCAL.REF` | `FsTransblockOperation_LocalRef` |  |  |  |
| 15 | `FS.TRANSBLOCK.OPERATION.OVERRIDE` | `FsTransblockOperation_Override` |  |  |  |
| 16 | `FS.TRANSBLOCK.OPERATION.RECORD.STATUS` | `FsTransblockOperation_RecordStatus` | String |  |  |
| 17 | `FS.TRANSBLOCK.OPERATION.CURR.NO` | `FsTransblockOperation_CurrNo` | String |  |  |
| 18 | `FS.TRANSBLOCK.OPERATION.INPUTTER` | `FsTransblockOperation_Inputter` |  |  |  |
| 19 | `FS.TRANSBLOCK.OPERATION.DATE.TIME` | `FsTransblockOperation_DateTime` |  |  |  |
| 20 | `FS.TRANSBLOCK.OPERATION.AUTHORISER` | `FsTransblockOperation_Authoriser` | String |  |  |
| 21 | `FS.TRANSBLOCK.OPERATION.CO.CODE` | `FsTransblockOperation_CoCode` | String |  |  |
| 22 | `FS.TRANSBLOCK.OPERATION.DEPT.CODE` | `FsTransblockOperation_DeptCode` | String |  |  |
| 23 | `FS.TRANSBLOCK.OPERATION.AUDITOR.CODE` | `FsTransblockOperation_AuditorCode` | String |  |  |
| 24 | `FS.TRANSBLOCK.OPERATION.AUDIT.DATE.TIME` | `FsTransblockOperation_AuditDateTime` | String |  |  |
