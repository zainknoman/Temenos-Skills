# FS.GA.NAVEXP.PROCESS.REPORTS — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAVEXP.PROCESS.REPORTS` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAVEXP.PROCESS.REPORTS.PARENT.REF.ID` | `FsGaNavexpProcessReports_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAVEXP.PROCESS.REPORTS.ORA.ROWID` | `FsGaNavexpProcessReports_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAVEXP.PROCESS.REPORTS.PROCESS.ID` | `FsGaNavexpProcessReports_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 4 | `FS.GA.NAVEXP.PROCESS.REPORTS.REPORT.NAME` | `FsGaNavexpProcessReports_ReportName` | TField |  | Report name linked to Process Multifonds DB Column is REPORT_NAME. |
| 5 | `FS.GA.NAVEXP.PROCESS.REPORTS.RESERVED10` | `FsGaNavexpProcessReports_Reserved10` | TField |  |  |
| 6 | `FS.GA.NAVEXP.PROCESS.REPORTS.RESERVED9` | `FsGaNavexpProcessReports_Reserved9` | TField |  |  |
| 7 | `FS.GA.NAVEXP.PROCESS.REPORTS.RESERVED8` | `FsGaNavexpProcessReports_Reserved8` | TField |  |  |
| 8 | `FS.GA.NAVEXP.PROCESS.REPORTS.RESERVED7` | `FsGaNavexpProcessReports_Reserved7` | TField |  |  |
| 9 | `FS.GA.NAVEXP.PROCESS.REPORTS.RESERVED6` | `FsGaNavexpProcessReports_Reserved6` | TField |  |  |
| 10 | `FS.GA.NAVEXP.PROCESS.REPORTS.RESERVED5` | `FsGaNavexpProcessReports_Reserved5` | TField |  |  |
| 11 | `FS.GA.NAVEXP.PROCESS.REPORTS.RESERVED4` | `FsGaNavexpProcessReports_Reserved4` | TField |  |  |
| 12 | `FS.GA.NAVEXP.PROCESS.REPORTS.RESERVED3` | `FsGaNavexpProcessReports_Reserved3` | TField |  |  |
| 13 | `FS.GA.NAVEXP.PROCESS.REPORTS.RESERVED2` | `FsGaNavexpProcessReports_Reserved2` | TField |  |  |
| 14 | `FS.GA.NAVEXP.PROCESS.REPORTS.RESERVED1` | `FsGaNavexpProcessReports_Reserved1` | TField |  |  |
| 15 | `FS.GA.NAVEXP.PROCESS.REPORTS.LOCAL.REF` | `FsGaNavexpProcessReports_LocalRef` |  |  |  |
| 16 | `FS.GA.NAVEXP.PROCESS.REPORTS.OVERRIDE` | `FsGaNavexpProcessReports_Override` |  |  |  |
| 17 | `FS.GA.NAVEXP.PROCESS.REPORTS.RECORD.STATUS` | `FsGaNavexpProcessReports_RecordStatus` | String |  |  |
| 18 | `FS.GA.NAVEXP.PROCESS.REPORTS.CURR.NO` | `FsGaNavexpProcessReports_CurrNo` | String |  |  |
| 19 | `FS.GA.NAVEXP.PROCESS.REPORTS.INPUTTER` | `FsGaNavexpProcessReports_Inputter` |  |  |  |
| 20 | `FS.GA.NAVEXP.PROCESS.REPORTS.DATE.TIME` | `FsGaNavexpProcessReports_DateTime` |  |  |  |
| 21 | `FS.GA.NAVEXP.PROCESS.REPORTS.AUTHORISER` | `FsGaNavexpProcessReports_Authoriser` | String |  |  |
| 22 | `FS.GA.NAVEXP.PROCESS.REPORTS.CO.CODE` | `FsGaNavexpProcessReports_CoCode` | String |  |  |
| 23 | `FS.GA.NAVEXP.PROCESS.REPORTS.DEPT.CODE` | `FsGaNavexpProcessReports_DeptCode` | String |  |  |
| 24 | `FS.GA.NAVEXP.PROCESS.REPORTS.AUDITOR.CODE` | `FsGaNavexpProcessReports_AuditorCode` | String |  |  |
| 25 | `FS.GA.NAVEXP.PROCESS.REPORTS.AUDIT.DATE.TIME` | `FsGaNavexpProcessReports_AuditDateTime` | String |  |  |
