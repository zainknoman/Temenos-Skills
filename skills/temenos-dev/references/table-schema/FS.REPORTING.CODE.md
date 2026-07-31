# FS.REPORTING.CODE — Table Schema

> Source: `INSERTS/I_F.FS.REPORTING.CODE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.REPORTING.CODE.DESCRIPTION` | `FsReportingCode_Description` |  |  |  |
| 2 | `FS.REPORTING.CODE.FILTER.KEY` | `FsReportingCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.REPORTING.CODE.RECORD.ID` | `FsReportingCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.REPORTING.CODE.RESERVED10` | `FsReportingCode_Reserved10` | TField |  |  |
| 5 | `FS.REPORTING.CODE.RESERVED9` | `FsReportingCode_Reserved9` | TField |  |  |
| 6 | `FS.REPORTING.CODE.RESERVED8` | `FsReportingCode_Reserved8` | TField |  |  |
| 7 | `FS.REPORTING.CODE.RESERVED7` | `FsReportingCode_Reserved7` | TField |  |  |
| 8 | `FS.REPORTING.CODE.RESERVED6` | `FsReportingCode_Reserved6` | TField |  |  |
| 9 | `FS.REPORTING.CODE.RESERVED5` | `FsReportingCode_Reserved5` | TField |  |  |
| 10 | `FS.REPORTING.CODE.RESERVED4` | `FsReportingCode_Reserved4` | TField |  |  |
| 11 | `FS.REPORTING.CODE.RESERVED3` | `FsReportingCode_Reserved3` | TField |  |  |
| 12 | `FS.REPORTING.CODE.RESERVED2` | `FsReportingCode_Reserved2` | TField |  |  |
| 13 | `FS.REPORTING.CODE.RESERVED1` | `FsReportingCode_Reserved1` | TField |  |  |
| 14 | `FS.REPORTING.CODE.LOCAL.REF` | `FsReportingCode_LocalRef` |  |  |  |
| 15 | `FS.REPORTING.CODE.OVERRIDE` | `FsReportingCode_Override` |  |  |  |
| 16 | `FS.REPORTING.CODE.RECORD.STATUS` | `FsReportingCode_RecordStatus` | String |  |  |
| 17 | `FS.REPORTING.CODE.CURR.NO` | `FsReportingCode_CurrNo` | String |  |  |
| 18 | `FS.REPORTING.CODE.INPUTTER` | `FsReportingCode_Inputter` |  |  |  |
| 19 | `FS.REPORTING.CODE.DATE.TIME` | `FsReportingCode_DateTime` |  |  |  |
| 20 | `FS.REPORTING.CODE.AUTHORISER` | `FsReportingCode_Authoriser` | String |  |  |
| 21 | `FS.REPORTING.CODE.CO.CODE` | `FsReportingCode_CoCode` | String |  |  |
| 22 | `FS.REPORTING.CODE.DEPT.CODE` | `FsReportingCode_DeptCode` | String |  |  |
| 23 | `FS.REPORTING.CODE.AUDITOR.CODE` | `FsReportingCode_AuditorCode` | String |  |  |
| 24 | `FS.REPORTING.CODE.AUDIT.DATE.TIME` | `FsReportingCode_AuditDateTime` | String |  |  |
