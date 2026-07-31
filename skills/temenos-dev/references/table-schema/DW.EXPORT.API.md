# DW.EXPORT.API — Table Schema

> Source: `INSERTS/I_F.DW.EXPORT.API` in `DW_BiExportFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.EA.COMMIT.TYPE` | `DwExportApi_CommitType` |  |  |  |
| 2 | `DW.EA.FIELD.NAME` | `DwExportApi_FieldName` |  |  |  |
| 3 | `DW.EA.API` | `DwExportApi_Api` |  |  |  |
| 4 | `DW.EA.RESERVED.6` | `DwExportApi_Reserved6` |  |  |  |
| 5 | `DW.EA.RESERVED.5` | `DwExportApi_Reserved5` |  |  |  |
| 6 | `DW.EA.RESERVED.4` | `DwExportApi_Reserved4` |  |  |  |
| 7 | `DW.EA.RESERVED.3` | `DwExportApi_Reserved3` | TField |  |  |
| 8 | `DW.EA.RESERVED.2` | `DwExportApi_Reserved2` | TField |  |  |
| 9 | `DW.EA.RESERVED.1` | `DwExportApi_Reserved1` | TField |  |  |
| 10 | `DW.EA.RECORD.STATUS` | `DwExportApi_RecordStatus` | String |  |  |
| 11 | `DW.EA.CURR.NO` | `DwExportApi_CurrNo` | String |  |  |
| 12 | `DW.EA.INPUTTER` | `DwExportApi_Inputter` |  |  |  |
| 13 | `DW.EA.DATE.TIME` | `DwExportApi_DateTime` |  |  |  |
| 14 | `DW.EA.AUTHORISER` | `DwExportApi_Authoriser` | String |  |  |
| 15 | `DW.EA.CO.CODE` | `DwExportApi_CoCode` | String |  |  |
| 16 | `DW.EA.DEPT.CODE` | `DwExportApi_DeptCode` | String |  |  |
| 17 | `DW.EA.AUDITOR.CODE` | `DwExportApi_AuditorCode` | String |  |  |
| 18 | `DW.EA.AUDIT.DATE.TIME` | `DwExportApi_AuditDateTime` | String |  |  |
| 19 | `DW.EA.FIELD.DISPLAY.FMT` | `DwExportApi_FieldDisplayFmt` |  |  |  |
| 20 | `DW.EA.FIELD.DATA.TYPE` | `DwExportApi_FieldDataType` |  |  |  |
| 21 | `DW.EA.FIELD.TYPE` | `DwExportApi_FieldType` |  |  |  |
