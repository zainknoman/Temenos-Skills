# FS.GI.WEM.MANUAL.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.MANUAL.PROCESS` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.MANUAL.PROCESS.PROCESS.ID` | `FsGiWemManualProcess_ProcessId` | TField |  | Process ID Multifonds DB Column is PROCESS.ID. |
| 2 | `FS.GI.WEM.MANUAL.PROCESS.PROCESS.NAME` | `FsGiWemManualProcess_ProcessName` | TField |  | Process Name Multifonds DB Column is PROCESS.NAME. |
| 3 | `FS.GI.WEM.MANUAL.PROCESS.CONTROL.OR.REPORT.ID` | `FsGiWemManualProcess_ControlOrReportId` | TField |  | Control or Report ID (Usefulm only if the Process is Control or Report) Multifonds DB Column is CONTROL.OR.REPORT.ID. |
| 4 | `FS.GI.WEM.MANUAL.PROCESS.ENTITY.TYPE` | `FsGiWemManualProcess_EntityType` | TField |  | Entity type Multifonds DB Column is ENTITY.TYPE. |
| 5 | `FS.GI.WEM.MANUAL.PROCESS.ENTITY.ID` | `FsGiWemManualProcess_EntityId` | TField |  | Entity ID from core Multifonds DB Column is ENTITY.ID. |
| 6 | `FS.GI.WEM.MANUAL.PROCESS.DATE` | `FsGiWemManualProcess_Date` | TField |  | Process Execution Date Multifonds DB Column is DATE. |
| 7 | `FS.GI.WEM.MANUAL.PROCESS.PROCESS.START` | `FsGiWemManualProcess_ProcessStart` | TField |  | Start Time Multifonds DB Column is PROCESS.START. |
| 8 | `FS.GI.WEM.MANUAL.PROCESS.PROCESS.COMPLETION` | `FsGiWemManualProcess_ProcessCompletion` | TField |  | End Time Multifonds DB Column is PROCESS.COMPLETION. |
| 9 | `FS.GI.WEM.MANUAL.PROCESS.PROCESS.STATUS` | `FsGiWemManualProcess_ProcessStatus` | TField |  | Process Status Multifonds DB Column is PROCESS.STATUS. |
| 10 | `FS.GI.WEM.MANUAL.PROCESS.PROCESS.MESSAGE` | `FsGiWemManualProcess_ProcessMessage` | TField |  | Process Message Multifonds DB Column is PROCESS.MESSAGE. |
| 11 | `FS.GI.WEM.MANUAL.PROCESS.PROCESS.CODE` | `FsGiWemManualProcess_ProcessCode` | TField |  | Process Code Multifonds DB Column is PROCESS.CODE. |
| 12 | `FS.GI.WEM.MANUAL.PROCESS.FUND.GROUP` | `FsGiWemManualProcess_FundGroup` | TField |  | Fund Group Multifonds DB Column is FUND.GROUP. |
| 13 | `FS.GI.WEM.MANUAL.PROCESS.FUND.ID` | `FsGiWemManualProcess_FundId` | TField |  | Fund Id Multifonds DB Column is FUND.ID. |
| 14 | `FS.GI.WEM.MANUAL.PROCESS.RESERVED10` | `FsGiWemManualProcess_Reserved10` | TField |  |  |
| 15 | `FS.GI.WEM.MANUAL.PROCESS.RESERVED9` | `FsGiWemManualProcess_Reserved9` | TField |  |  |
| 16 | `FS.GI.WEM.MANUAL.PROCESS.RESERVED8` | `FsGiWemManualProcess_Reserved8` | TField |  |  |
| 17 | `FS.GI.WEM.MANUAL.PROCESS.RESERVED7` | `FsGiWemManualProcess_Reserved7` | TField |  |  |
| 18 | `FS.GI.WEM.MANUAL.PROCESS.RESERVED6` | `FsGiWemManualProcess_Reserved6` | TField |  |  |
| 19 | `FS.GI.WEM.MANUAL.PROCESS.RESERVED5` | `FsGiWemManualProcess_Reserved5` | TField |  |  |
| 20 | `FS.GI.WEM.MANUAL.PROCESS.RESERVED4` | `FsGiWemManualProcess_Reserved4` | TField |  |  |
| 21 | `FS.GI.WEM.MANUAL.PROCESS.RESERVED3` | `FsGiWemManualProcess_Reserved3` | TField |  |  |
| 22 | `FS.GI.WEM.MANUAL.PROCESS.RESERVED2` | `FsGiWemManualProcess_Reserved2` | TField |  |  |
| 23 | `FS.GI.WEM.MANUAL.PROCESS.RESERVED1` | `FsGiWemManualProcess_Reserved1` | TField |  |  |
| 24 | `FS.GI.WEM.MANUAL.PROCESS.LOCAL.REF` | `FsGiWemManualProcess_LocalRef` |  |  |  |
| 25 | `FS.GI.WEM.MANUAL.PROCESS.OVERRIDE` | `FsGiWemManualProcess_Override` |  |  |  |
| 26 | `FS.GI.WEM.MANUAL.PROCESS.RECORD.STATUS` | `FsGiWemManualProcess_RecordStatus` | String |  |  |
| 27 | `FS.GI.WEM.MANUAL.PROCESS.CURR.NO` | `FsGiWemManualProcess_CurrNo` | String |  |  |
| 28 | `FS.GI.WEM.MANUAL.PROCESS.INPUTTER` | `FsGiWemManualProcess_Inputter` |  |  |  |
| 29 | `FS.GI.WEM.MANUAL.PROCESS.DATE.TIME` | `FsGiWemManualProcess_DateTime` |  |  |  |
| 30 | `FS.GI.WEM.MANUAL.PROCESS.AUTHORISER` | `FsGiWemManualProcess_Authoriser` | String |  |  |
| 31 | `FS.GI.WEM.MANUAL.PROCESS.CO.CODE` | `FsGiWemManualProcess_CoCode` | String |  |  |
| 32 | `FS.GI.WEM.MANUAL.PROCESS.DEPT.CODE` | `FsGiWemManualProcess_DeptCode` | String |  |  |
| 33 | `FS.GI.WEM.MANUAL.PROCESS.AUDITOR.CODE` | `FsGiWemManualProcess_AuditorCode` | String |  |  |
| 34 | `FS.GI.WEM.MANUAL.PROCESS.AUDIT.DATE.TIME` | `FsGiWemManualProcess_AuditDateTime` | String |  |  |
