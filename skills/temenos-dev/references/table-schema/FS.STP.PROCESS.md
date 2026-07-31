# FS.STP.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.STP.PROCESS` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.STP.PROCESS.DESCRIPTION` | `FsStpProcess_Description` |  |  |  |
| 2 | `FS.STP.PROCESS.FILTER.KEY` | `FsStpProcess_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.STP.PROCESS.RECORD.ID` | `FsStpProcess_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.STP.PROCESS.RESERVED10` | `FsStpProcess_Reserved10` | TField |  |  |
| 5 | `FS.STP.PROCESS.RESERVED9` | `FsStpProcess_Reserved9` | TField |  |  |
| 6 | `FS.STP.PROCESS.RESERVED8` | `FsStpProcess_Reserved8` | TField |  |  |
| 7 | `FS.STP.PROCESS.RESERVED7` | `FsStpProcess_Reserved7` | TField |  |  |
| 8 | `FS.STP.PROCESS.RESERVED6` | `FsStpProcess_Reserved6` | TField |  |  |
| 9 | `FS.STP.PROCESS.RESERVED5` | `FsStpProcess_Reserved5` | TField |  |  |
| 10 | `FS.STP.PROCESS.RESERVED4` | `FsStpProcess_Reserved4` | TField |  |  |
| 11 | `FS.STP.PROCESS.RESERVED3` | `FsStpProcess_Reserved3` | TField |  |  |
| 12 | `FS.STP.PROCESS.RESERVED2` | `FsStpProcess_Reserved2` | TField |  |  |
| 13 | `FS.STP.PROCESS.RESERVED1` | `FsStpProcess_Reserved1` | TField |  |  |
| 14 | `FS.STP.PROCESS.LOCAL.REF` | `FsStpProcess_LocalRef` |  |  |  |
| 15 | `FS.STP.PROCESS.OVERRIDE` | `FsStpProcess_Override` |  |  |  |
| 16 | `FS.STP.PROCESS.RECORD.STATUS` | `FsStpProcess_RecordStatus` | String |  |  |
| 17 | `FS.STP.PROCESS.CURR.NO` | `FsStpProcess_CurrNo` | String |  |  |
| 18 | `FS.STP.PROCESS.INPUTTER` | `FsStpProcess_Inputter` |  |  |  |
| 19 | `FS.STP.PROCESS.DATE.TIME` | `FsStpProcess_DateTime` |  |  |  |
| 20 | `FS.STP.PROCESS.AUTHORISER` | `FsStpProcess_Authoriser` | String |  |  |
| 21 | `FS.STP.PROCESS.CO.CODE` | `FsStpProcess_CoCode` | String |  |  |
| 22 | `FS.STP.PROCESS.DEPT.CODE` | `FsStpProcess_DeptCode` | String |  |  |
| 23 | `FS.STP.PROCESS.AUDITOR.CODE` | `FsStpProcess_AuditorCode` | String |  |  |
| 24 | `FS.STP.PROCESS.AUDIT.DATE.TIME` | `FsStpProcess_AuditDateTime` | String |  |  |
