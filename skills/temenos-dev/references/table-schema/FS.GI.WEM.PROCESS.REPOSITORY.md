# FS.GI.WEM.PROCESS.REPOSITORY — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.PROCESS.REPOSITORY` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.PROCESS.REPOSITORY.PROCESS.ID` | `FsGiWemProcessRepository_ProcessId` | TField |  | Unique process ID Multifonds DB Column is PROCESS.ID. |
| 2 | `FS.GI.WEM.PROCESS.REPOSITORY.PROCESS.TYPE` | `FsGiWemProcessRepository_ProcessType` | TField |  | Report, control, process, a Multifonds DB Column is PROCESS.TYPE. |
| 3 | `FS.GI.WEM.PROCESS.REPOSITORY.PROCESS.NAME` | `FsGiWemProcessRepository_ProcessName` | TField |  | Process name Multifonds DB Column is PROCESS.NAME. |
| 4 | `FS.GI.WEM.PROCESS.REPOSITORY.PROCESS.CODE` | `FsGiWemProcessRepository_ProcessCode` | TField |  | MF Process code Multifonds DB Column is PROCESS.CODE. |
| 5 | `FS.GI.WEM.PROCESS.REPOSITORY.PROCESS.URL` | `FsGiWemProcessRepository_ProcessUrl` | TField |  | Specific URL part to be used to trigger the process Multifonds DB Column is PROCESS.URL. |
| 6 | `FS.GI.WEM.PROCESS.REPOSITORY.TECHNICAL.API` | `FsGiWemProcessRepository_TechnicalApi` | TField |  | Technical Api Multifonds DB Column is TECHNICAL.API. |
| 7 | `FS.GI.WEM.PROCESS.REPOSITORY.PARAMETERS` | `FsGiWemProcessRepository_Parameters` | TField |  | List of process parameters and map to WEM variables Multifonds DB Column is PARAMETERS. |
| 8 | `FS.GI.WEM.PROCESS.REPOSITORY.TARGET.SYSTEM` | `FsGiWemProcessRepository_TargetSystem` | TField |  | Target System Multifonds DB Column is TARGET.SYSTEM. |
| 9 | `FS.GI.WEM.PROCESS.REPOSITORY.LOG.SCREEN` | `FsGiWemProcessRepository_LogScreen` | TField |  | Specific URL part to be used to retrieve the process logs Multifonds DB Column is LOG.SCREEN. |
| 10 | `FS.GI.WEM.PROCESS.REPOSITORY.RESERVED10` | `FsGiWemProcessRepository_Reserved10` | TField |  |  |
| 11 | `FS.GI.WEM.PROCESS.REPOSITORY.RESERVED9` | `FsGiWemProcessRepository_Reserved9` | TField |  |  |
| 12 | `FS.GI.WEM.PROCESS.REPOSITORY.RESERVED8` | `FsGiWemProcessRepository_Reserved8` | TField |  |  |
| 13 | `FS.GI.WEM.PROCESS.REPOSITORY.RESERVED7` | `FsGiWemProcessRepository_Reserved7` | TField |  |  |
| 14 | `FS.GI.WEM.PROCESS.REPOSITORY.RESERVED6` | `FsGiWemProcessRepository_Reserved6` | TField |  |  |
| 15 | `FS.GI.WEM.PROCESS.REPOSITORY.RESERVED5` | `FsGiWemProcessRepository_Reserved5` | TField |  |  |
| 16 | `FS.GI.WEM.PROCESS.REPOSITORY.RESERVED4` | `FsGiWemProcessRepository_Reserved4` | TField |  |  |
| 17 | `FS.GI.WEM.PROCESS.REPOSITORY.RESERVED3` | `FsGiWemProcessRepository_Reserved3` | TField |  |  |
| 18 | `FS.GI.WEM.PROCESS.REPOSITORY.RESERVED2` | `FsGiWemProcessRepository_Reserved2` | TField |  |  |
| 19 | `FS.GI.WEM.PROCESS.REPOSITORY.RESERVED1` | `FsGiWemProcessRepository_Reserved1` | TField |  |  |
| 20 | `FS.GI.WEM.PROCESS.REPOSITORY.LOCAL.REF` | `FsGiWemProcessRepository_LocalRef` |  |  |  |
| 21 | `FS.GI.WEM.PROCESS.REPOSITORY.OVERRIDE` | `FsGiWemProcessRepository_Override` |  |  |  |
| 22 | `FS.GI.WEM.PROCESS.REPOSITORY.RECORD.STATUS` | `FsGiWemProcessRepository_RecordStatus` | String |  |  |
| 23 | `FS.GI.WEM.PROCESS.REPOSITORY.CURR.NO` | `FsGiWemProcessRepository_CurrNo` | String |  |  |
| 24 | `FS.GI.WEM.PROCESS.REPOSITORY.INPUTTER` | `FsGiWemProcessRepository_Inputter` |  |  |  |
| 25 | `FS.GI.WEM.PROCESS.REPOSITORY.DATE.TIME` | `FsGiWemProcessRepository_DateTime` |  |  |  |
| 26 | `FS.GI.WEM.PROCESS.REPOSITORY.AUTHORISER` | `FsGiWemProcessRepository_Authoriser` | String |  |  |
| 27 | `FS.GI.WEM.PROCESS.REPOSITORY.CO.CODE` | `FsGiWemProcessRepository_CoCode` | String |  |  |
| 28 | `FS.GI.WEM.PROCESS.REPOSITORY.DEPT.CODE` | `FsGiWemProcessRepository_DeptCode` | String |  |  |
| 29 | `FS.GI.WEM.PROCESS.REPOSITORY.AUDITOR.CODE` | `FsGiWemProcessRepository_AuditorCode` | String |  |  |
| 30 | `FS.GI.WEM.PROCESS.REPOSITORY.AUDIT.DATE.TIME` | `FsGiWemProcessRepository_AuditDateTime` | String |  |  |
