# FS.REPORT.NAMES — Table Schema

> Source: `INSERTS/I_F.FS.REPORT.NAMES` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.REPORT.NAMES.DESCRIPTION` | `FsReportNames_Description` |  |  |  |
| 2 | `FS.REPORT.NAMES.FILTER.KEY` | `FsReportNames_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.REPORT.NAMES.RECORD.ID` | `FsReportNames_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.REPORT.NAMES.RESERVED10` | `FsReportNames_Reserved10` | TField |  |  |
| 5 | `FS.REPORT.NAMES.RESERVED9` | `FsReportNames_Reserved9` | TField |  |  |
| 6 | `FS.REPORT.NAMES.RESERVED8` | `FsReportNames_Reserved8` | TField |  |  |
| 7 | `FS.REPORT.NAMES.RESERVED7` | `FsReportNames_Reserved7` | TField |  |  |
| 8 | `FS.REPORT.NAMES.RESERVED6` | `FsReportNames_Reserved6` | TField |  |  |
| 9 | `FS.REPORT.NAMES.RESERVED5` | `FsReportNames_Reserved5` | TField |  |  |
| 10 | `FS.REPORT.NAMES.RESERVED4` | `FsReportNames_Reserved4` | TField |  |  |
| 11 | `FS.REPORT.NAMES.RESERVED3` | `FsReportNames_Reserved3` | TField |  |  |
| 12 | `FS.REPORT.NAMES.RESERVED2` | `FsReportNames_Reserved2` | TField |  |  |
| 13 | `FS.REPORT.NAMES.RESERVED1` | `FsReportNames_Reserved1` | TField |  |  |
| 14 | `FS.REPORT.NAMES.LOCAL.REF` | `FsReportNames_LocalRef` |  |  |  |
| 15 | `FS.REPORT.NAMES.OVERRIDE` | `FsReportNames_Override` |  |  |  |
| 16 | `FS.REPORT.NAMES.RECORD.STATUS` | `FsReportNames_RecordStatus` | String |  |  |
| 17 | `FS.REPORT.NAMES.CURR.NO` | `FsReportNames_CurrNo` | String |  |  |
| 18 | `FS.REPORT.NAMES.INPUTTER` | `FsReportNames_Inputter` |  |  |  |
| 19 | `FS.REPORT.NAMES.DATE.TIME` | `FsReportNames_DateTime` |  |  |  |
| 20 | `FS.REPORT.NAMES.AUTHORISER` | `FsReportNames_Authoriser` | String |  |  |
| 21 | `FS.REPORT.NAMES.CO.CODE` | `FsReportNames_CoCode` | String |  |  |
| 22 | `FS.REPORT.NAMES.DEPT.CODE` | `FsReportNames_DeptCode` | String |  |  |
| 23 | `FS.REPORT.NAMES.AUDITOR.CODE` | `FsReportNames_AuditorCode` | String |  |  |
| 24 | `FS.REPORT.NAMES.AUDIT.DATE.TIME` | `FsReportNames_AuditDateTime` | String |  |  |
