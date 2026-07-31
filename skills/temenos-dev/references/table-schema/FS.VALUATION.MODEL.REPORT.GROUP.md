# FS.VALUATION.MODEL.REPORT.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.VALUATION.MODEL.REPORT.GROUP` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.VALUATION.MODEL.REPORT.GROUP.DESCRIPTION` | `FsValuationModelReportGroup_Description` |  |  |  |
| 2 | `FS.VALUATION.MODEL.REPORT.GROUP.FILTER.KEY` | `FsValuationModelReportGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.VALUATION.MODEL.REPORT.GROUP.RECORD.ID` | `FsValuationModelReportGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.VALUATION.MODEL.REPORT.GROUP.RESERVED10` | `FsValuationModelReportGroup_Reserved10` | TField |  |  |
| 5 | `FS.VALUATION.MODEL.REPORT.GROUP.RESERVED9` | `FsValuationModelReportGroup_Reserved9` | TField |  |  |
| 6 | `FS.VALUATION.MODEL.REPORT.GROUP.RESERVED8` | `FsValuationModelReportGroup_Reserved8` | TField |  |  |
| 7 | `FS.VALUATION.MODEL.REPORT.GROUP.RESERVED7` | `FsValuationModelReportGroup_Reserved7` | TField |  |  |
| 8 | `FS.VALUATION.MODEL.REPORT.GROUP.RESERVED6` | `FsValuationModelReportGroup_Reserved6` | TField |  |  |
| 9 | `FS.VALUATION.MODEL.REPORT.GROUP.RESERVED5` | `FsValuationModelReportGroup_Reserved5` | TField |  |  |
| 10 | `FS.VALUATION.MODEL.REPORT.GROUP.RESERVED4` | `FsValuationModelReportGroup_Reserved4` | TField |  |  |
| 11 | `FS.VALUATION.MODEL.REPORT.GROUP.RESERVED3` | `FsValuationModelReportGroup_Reserved3` | TField |  |  |
| 12 | `FS.VALUATION.MODEL.REPORT.GROUP.RESERVED2` | `FsValuationModelReportGroup_Reserved2` | TField |  |  |
| 13 | `FS.VALUATION.MODEL.REPORT.GROUP.RESERVED1` | `FsValuationModelReportGroup_Reserved1` | TField |  |  |
| 14 | `FS.VALUATION.MODEL.REPORT.GROUP.LOCAL.REF` | `FsValuationModelReportGroup_LocalRef` |  |  |  |
| 15 | `FS.VALUATION.MODEL.REPORT.GROUP.OVERRIDE` | `FsValuationModelReportGroup_Override` |  |  |  |
| 16 | `FS.VALUATION.MODEL.REPORT.GROUP.RECORD.STATUS` | `FsValuationModelReportGroup_RecordStatus` | String |  |  |
| 17 | `FS.VALUATION.MODEL.REPORT.GROUP.CURR.NO` | `FsValuationModelReportGroup_CurrNo` | String |  |  |
| 18 | `FS.VALUATION.MODEL.REPORT.GROUP.INPUTTER` | `FsValuationModelReportGroup_Inputter` |  |  |  |
| 19 | `FS.VALUATION.MODEL.REPORT.GROUP.DATE.TIME` | `FsValuationModelReportGroup_DateTime` |  |  |  |
| 20 | `FS.VALUATION.MODEL.REPORT.GROUP.AUTHORISER` | `FsValuationModelReportGroup_Authoriser` | String |  |  |
| 21 | `FS.VALUATION.MODEL.REPORT.GROUP.CO.CODE` | `FsValuationModelReportGroup_CoCode` | String |  |  |
| 22 | `FS.VALUATION.MODEL.REPORT.GROUP.DEPT.CODE` | `FsValuationModelReportGroup_DeptCode` | String |  |  |
| 23 | `FS.VALUATION.MODEL.REPORT.GROUP.AUDITOR.CODE` | `FsValuationModelReportGroup_AuditorCode` | String |  |  |
| 24 | `FS.VALUATION.MODEL.REPORT.GROUP.AUDIT.DATE.TIME` | `FsValuationModelReportGroup_AuditDateTime` | String |  |  |
