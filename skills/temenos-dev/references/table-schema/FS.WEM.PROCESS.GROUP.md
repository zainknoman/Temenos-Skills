# FS.WEM.PROCESS.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.WEM.PROCESS.GROUP` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.WEM.PROCESS.GROUP.DESCRIPTION` | `FsWemProcessGroup_Description` |  |  |  |
| 2 | `FS.WEM.PROCESS.GROUP.FILTER.KEY` | `FsWemProcessGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.WEM.PROCESS.GROUP.RECORD.ID` | `FsWemProcessGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.WEM.PROCESS.GROUP.RESERVED10` | `FsWemProcessGroup_Reserved10` | TField |  |  |
| 5 | `FS.WEM.PROCESS.GROUP.RESERVED9` | `FsWemProcessGroup_Reserved9` | TField |  |  |
| 6 | `FS.WEM.PROCESS.GROUP.RESERVED8` | `FsWemProcessGroup_Reserved8` | TField |  |  |
| 7 | `FS.WEM.PROCESS.GROUP.RESERVED7` | `FsWemProcessGroup_Reserved7` | TField |  |  |
| 8 | `FS.WEM.PROCESS.GROUP.RESERVED6` | `FsWemProcessGroup_Reserved6` | TField |  |  |
| 9 | `FS.WEM.PROCESS.GROUP.RESERVED5` | `FsWemProcessGroup_Reserved5` | TField |  |  |
| 10 | `FS.WEM.PROCESS.GROUP.RESERVED4` | `FsWemProcessGroup_Reserved4` | TField |  |  |
| 11 | `FS.WEM.PROCESS.GROUP.RESERVED3` | `FsWemProcessGroup_Reserved3` | TField |  |  |
| 12 | `FS.WEM.PROCESS.GROUP.RESERVED2` | `FsWemProcessGroup_Reserved2` | TField |  |  |
| 13 | `FS.WEM.PROCESS.GROUP.RESERVED1` | `FsWemProcessGroup_Reserved1` | TField |  |  |
| 14 | `FS.WEM.PROCESS.GROUP.LOCAL.REF` | `FsWemProcessGroup_LocalRef` |  |  |  |
| 15 | `FS.WEM.PROCESS.GROUP.OVERRIDE` | `FsWemProcessGroup_Override` |  |  |  |
| 16 | `FS.WEM.PROCESS.GROUP.RECORD.STATUS` | `FsWemProcessGroup_RecordStatus` | String |  |  |
| 17 | `FS.WEM.PROCESS.GROUP.CURR.NO` | `FsWemProcessGroup_CurrNo` | String |  |  |
| 18 | `FS.WEM.PROCESS.GROUP.INPUTTER` | `FsWemProcessGroup_Inputter` |  |  |  |
| 19 | `FS.WEM.PROCESS.GROUP.DATE.TIME` | `FsWemProcessGroup_DateTime` |  |  |  |
| 20 | `FS.WEM.PROCESS.GROUP.AUTHORISER` | `FsWemProcessGroup_Authoriser` | String |  |  |
| 21 | `FS.WEM.PROCESS.GROUP.CO.CODE` | `FsWemProcessGroup_CoCode` | String |  |  |
| 22 | `FS.WEM.PROCESS.GROUP.DEPT.CODE` | `FsWemProcessGroup_DeptCode` | String |  |  |
| 23 | `FS.WEM.PROCESS.GROUP.AUDITOR.CODE` | `FsWemProcessGroup_AuditorCode` | String |  |  |
| 24 | `FS.WEM.PROCESS.GROUP.AUDIT.DATE.TIME` | `FsWemProcessGroup_AuditDateTime` | String |  |  |
