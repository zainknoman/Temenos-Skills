# FS.APP.TOWN — Table Schema

> Source: `INSERTS/I_F.FS.APP.TOWN` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.APP.TOWN.DESCRIPTION` | `FsAppTown_Description` |  |  |  |
| 2 | `FS.APP.TOWN.FILTER.KEY` | `FsAppTown_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.APP.TOWN.RECORD.ID` | `FsAppTown_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.APP.TOWN.RESERVED10` | `FsAppTown_Reserved10` | TField |  |  |
| 5 | `FS.APP.TOWN.RESERVED9` | `FsAppTown_Reserved9` | TField |  |  |
| 6 | `FS.APP.TOWN.RESERVED8` | `FsAppTown_Reserved8` | TField |  |  |
| 7 | `FS.APP.TOWN.RESERVED7` | `FsAppTown_Reserved7` | TField |  |  |
| 8 | `FS.APP.TOWN.RESERVED6` | `FsAppTown_Reserved6` | TField |  |  |
| 9 | `FS.APP.TOWN.RESERVED5` | `FsAppTown_Reserved5` | TField |  |  |
| 10 | `FS.APP.TOWN.RESERVED4` | `FsAppTown_Reserved4` | TField |  |  |
| 11 | `FS.APP.TOWN.RESERVED3` | `FsAppTown_Reserved3` | TField |  |  |
| 12 | `FS.APP.TOWN.RESERVED2` | `FsAppTown_Reserved2` | TField |  |  |
| 13 | `FS.APP.TOWN.RESERVED1` | `FsAppTown_Reserved1` | TField |  |  |
| 14 | `FS.APP.TOWN.LOCAL.REF` | `FsAppTown_LocalRef` |  |  |  |
| 15 | `FS.APP.TOWN.OVERRIDE` | `FsAppTown_Override` |  |  |  |
| 16 | `FS.APP.TOWN.RECORD.STATUS` | `FsAppTown_RecordStatus` | String |  |  |
| 17 | `FS.APP.TOWN.CURR.NO` | `FsAppTown_CurrNo` | String |  |  |
| 18 | `FS.APP.TOWN.INPUTTER` | `FsAppTown_Inputter` |  |  |  |
| 19 | `FS.APP.TOWN.DATE.TIME` | `FsAppTown_DateTime` |  |  |  |
| 20 | `FS.APP.TOWN.AUTHORISER` | `FsAppTown_Authoriser` | String |  |  |
| 21 | `FS.APP.TOWN.CO.CODE` | `FsAppTown_CoCode` | String |  |  |
| 22 | `FS.APP.TOWN.DEPT.CODE` | `FsAppTown_DeptCode` | String |  |  |
| 23 | `FS.APP.TOWN.AUDITOR.CODE` | `FsAppTown_AuditorCode` | String |  |  |
| 24 | `FS.APP.TOWN.AUDIT.DATE.TIME` | `FsAppTown_AuditDateTime` | String |  |  |
