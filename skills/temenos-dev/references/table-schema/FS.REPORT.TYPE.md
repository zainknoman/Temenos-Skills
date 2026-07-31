# FS.REPORT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.REPORT.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.REPORT.TYPE.DESCRIPTION` | `FsReportType_Description` |  |  |  |
| 2 | `FS.REPORT.TYPE.FILTER.KEY` | `FsReportType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.REPORT.TYPE.RECORD.ID` | `FsReportType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.REPORT.TYPE.RESERVED10` | `FsReportType_Reserved10` | TField |  |  |
| 5 | `FS.REPORT.TYPE.RESERVED9` | `FsReportType_Reserved9` | TField |  |  |
| 6 | `FS.REPORT.TYPE.RESERVED8` | `FsReportType_Reserved8` | TField |  |  |
| 7 | `FS.REPORT.TYPE.RESERVED7` | `FsReportType_Reserved7` | TField |  |  |
| 8 | `FS.REPORT.TYPE.RESERVED6` | `FsReportType_Reserved6` | TField |  |  |
| 9 | `FS.REPORT.TYPE.RESERVED5` | `FsReportType_Reserved5` | TField |  |  |
| 10 | `FS.REPORT.TYPE.RESERVED4` | `FsReportType_Reserved4` | TField |  |  |
| 11 | `FS.REPORT.TYPE.RESERVED3` | `FsReportType_Reserved3` | TField |  |  |
| 12 | `FS.REPORT.TYPE.RESERVED2` | `FsReportType_Reserved2` | TField |  |  |
| 13 | `FS.REPORT.TYPE.RESERVED1` | `FsReportType_Reserved1` | TField |  |  |
| 14 | `FS.REPORT.TYPE.LOCAL.REF` | `FsReportType_LocalRef` |  |  |  |
| 15 | `FS.REPORT.TYPE.OVERRIDE` | `FsReportType_Override` |  |  |  |
| 16 | `FS.REPORT.TYPE.RECORD.STATUS` | `FsReportType_RecordStatus` | String |  |  |
| 17 | `FS.REPORT.TYPE.CURR.NO` | `FsReportType_CurrNo` | String |  |  |
| 18 | `FS.REPORT.TYPE.INPUTTER` | `FsReportType_Inputter` |  |  |  |
| 19 | `FS.REPORT.TYPE.DATE.TIME` | `FsReportType_DateTime` |  |  |  |
| 20 | `FS.REPORT.TYPE.AUTHORISER` | `FsReportType_Authoriser` | String |  |  |
| 21 | `FS.REPORT.TYPE.CO.CODE` | `FsReportType_CoCode` | String |  |  |
| 22 | `FS.REPORT.TYPE.DEPT.CODE` | `FsReportType_DeptCode` | String |  |  |
| 23 | `FS.REPORT.TYPE.AUDITOR.CODE` | `FsReportType_AuditorCode` | String |  |  |
| 24 | `FS.REPORT.TYPE.AUDIT.DATE.TIME` | `FsReportType_AuditDateTime` | String |  |  |
