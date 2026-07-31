# FS.SCHEDULER.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.SCHEDULER.PROCESS` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.SCHEDULER.PROCESS.DESCRIPTION` | `FsSchedulerProcess_Description` |  |  |  |
| 2 | `FS.SCHEDULER.PROCESS.FILTER.KEY` | `FsSchedulerProcess_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.SCHEDULER.PROCESS.RECORD.ID` | `FsSchedulerProcess_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.SCHEDULER.PROCESS.RESERVED10` | `FsSchedulerProcess_Reserved10` | TField |  |  |
| 5 | `FS.SCHEDULER.PROCESS.RESERVED9` | `FsSchedulerProcess_Reserved9` | TField |  |  |
| 6 | `FS.SCHEDULER.PROCESS.RESERVED8` | `FsSchedulerProcess_Reserved8` | TField |  |  |
| 7 | `FS.SCHEDULER.PROCESS.RESERVED7` | `FsSchedulerProcess_Reserved7` | TField |  |  |
| 8 | `FS.SCHEDULER.PROCESS.RESERVED6` | `FsSchedulerProcess_Reserved6` | TField |  |  |
| 9 | `FS.SCHEDULER.PROCESS.RESERVED5` | `FsSchedulerProcess_Reserved5` | TField |  |  |
| 10 | `FS.SCHEDULER.PROCESS.RESERVED4` | `FsSchedulerProcess_Reserved4` | TField |  |  |
| 11 | `FS.SCHEDULER.PROCESS.RESERVED3` | `FsSchedulerProcess_Reserved3` | TField |  |  |
| 12 | `FS.SCHEDULER.PROCESS.RESERVED2` | `FsSchedulerProcess_Reserved2` | TField |  |  |
| 13 | `FS.SCHEDULER.PROCESS.RESERVED1` | `FsSchedulerProcess_Reserved1` | TField |  |  |
| 14 | `FS.SCHEDULER.PROCESS.LOCAL.REF` | `FsSchedulerProcess_LocalRef` |  |  |  |
| 15 | `FS.SCHEDULER.PROCESS.OVERRIDE` | `FsSchedulerProcess_Override` |  |  |  |
| 16 | `FS.SCHEDULER.PROCESS.RECORD.STATUS` | `FsSchedulerProcess_RecordStatus` | String |  |  |
| 17 | `FS.SCHEDULER.PROCESS.CURR.NO` | `FsSchedulerProcess_CurrNo` | String |  |  |
| 18 | `FS.SCHEDULER.PROCESS.INPUTTER` | `FsSchedulerProcess_Inputter` |  |  |  |
| 19 | `FS.SCHEDULER.PROCESS.DATE.TIME` | `FsSchedulerProcess_DateTime` |  |  |  |
| 20 | `FS.SCHEDULER.PROCESS.AUTHORISER` | `FsSchedulerProcess_Authoriser` | String |  |  |
| 21 | `FS.SCHEDULER.PROCESS.CO.CODE` | `FsSchedulerProcess_CoCode` | String |  |  |
| 22 | `FS.SCHEDULER.PROCESS.DEPT.CODE` | `FsSchedulerProcess_DeptCode` | String |  |  |
| 23 | `FS.SCHEDULER.PROCESS.AUDITOR.CODE` | `FsSchedulerProcess_AuditorCode` | String |  |  |
| 24 | `FS.SCHEDULER.PROCESS.AUDIT.DATE.TIME` | `FsSchedulerProcess_AuditDateTime` | String |  |  |
