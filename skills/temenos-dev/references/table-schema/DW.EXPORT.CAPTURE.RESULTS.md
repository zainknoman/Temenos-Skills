# DW.EXPORT.CAPTURE.RESULTS — Table Schema

> Source: `INSERTS/I_F.DW.EXPORT.CAPTURE.RESULTS` in `DW_BiExportFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.ECR.CONTROL.LIST` | `DwExportCaptureResults_ControlList` |  |  |  |
| 2 | `DW.ECR.SELECT.STMT` | `DwExportCaptureResults_SelectStmt` |  |  |  |
| 3 | `DW.ECR.SELECTED.NOS` | `DwExportCaptureResults_SelectedNos` |  |  |  |
| 4 | `DW.ECR.PROCESSED.NOS` | `DwExportCaptureResults_ProcessedNos` |  |  |  |
| 5 | `DW.ECR.FILTERED.NOS` | `DwExportCaptureResults_FilteredNos` |  |  |  |
| 6 | `DW.ECR.EXTENDED.NOS` | `DwExportCaptureResults_ExtendedNos` |  |  |  |
| 7 | `DW.ECR.RESERVED.17` | `DwExportCaptureResults_Reserved17` |  |  |  |
| 8 | `DW.ECR.RESERVED.16` | `DwExportCaptureResults_Reserved16` |  |  |  |
| 9 | `DW.ECR.RESERVED.15` | `DwExportCaptureResults_Reserved15` |  |  |  |
| 10 | `DW.ECR.RESERVED.14` | `DwExportCaptureResults_Reserved14` |  |  |  |
| 11 | `DW.ECR.RESERVED.13` | `DwExportCaptureResults_Reserved13` |  |  |  |
| 12 | `DW.ECR.HASH.FIELD.NAME` | `DwExportCaptureResults_HashFieldName` | TField |  | Hash total field name defined for a particular DW.EXPORT file |
| 13 | `DW.ECR.HASH.FIELD.TOTAL` | `DwExportCaptureResults_HashFieldTotal` | TField |  | The running total of all records extracted for a particular DW.EXPORT file. |
| 14 | `DW.ECR.HASH.TOTAL.REC.NOS` | `DwExportCaptureResults_HashTotalRecNos` | TField |  | The total number of records that are being extracted as per in HASH.TOTAL.csv for a particular DW.EXPORT file |
| 15 | `DW.ECR.EXTRACT.RECON` | `DwExportCaptureResults_ExtractRecon` | TField |  | The difference between the number of records selected and (processed + filtered) records |
| 16 | `DW.ECR.HASH.RECON` | `DwExportCaptureResults_HashRecon` | TField |  | The difference between the number of records extended against the hash total number of records for a particular file as per in HASH.TOTAL.csv |
| 17 | `DW.ECR.CSV.FILE.NAME` | `DwExportCaptureResults_CsvFileName` |  |  |  |
| 18 | `DW.ECR.BOM.MATCHES` | `DwExportCaptureResults_BomMatches` |  |  |  |
| 19 | `DW.ECR.NO.OF.HEADINGS` | `DwExportCaptureResults_NoOfHeadings` |  |  |  |
| 20 | `DW.ECR.MIN.ROW.NOS` | `DwExportCaptureResults_MinRowNos` |  |  |  |
| 21 | `DW.ECR.MAX.ROW.NOS` | `DwExportCaptureResults_MaxRowNos` |  |  |  |
| 22 | `DW.ECR.TXT.NO.OF.FLDS` | `DwExportCaptureResults_TxtNoOfFlds` |  |  |  |
| 23 | `DW.ECR.ROWS.RECON` | `DwExportCaptureResults_RowsRecon` |  |  |  |
| 24 | `DW.ECR.HEAD.ROW.RECON` | `DwExportCaptureResults_HeadRowRecon` |  |  |  |
| 25 | `DW.ECR.TXT.HEAD.RECON` | `DwExportCaptureResults_TxtHeadRecon` |  |  |  |
| 26 | `DW.ECR.RESERVED.12` | `DwExportCaptureResults_Reserved12` |  |  |  |
| 27 | `DW.ECR.RESERVED.11` | `DwExportCaptureResults_Reserved11` |  |  |  |
| 28 | `DW.ECR.RESERVED.10` | `DwExportCaptureResults_Reserved10` |  |  |  |
| 29 | `DW.ECR.RESERVED.9` | `DwExportCaptureResults_Reserved9` |  |  |  |
| 30 | `DW.ECR.RESERVED.8` | `DwExportCaptureResults_Reserved8` |  |  |  |
| 31 | `DW.ECR.FILE.NAME` | `DwExportCaptureResults_FileName` | TField |  |  |
| 32 | `DW.ECR.PARAM.ID` | `DwExportCaptureResults_ParamId` | TField |  |  |
| 33 | `DW.ECR.MIS.DATE` | `DwExportCaptureResults_MisDate` | TField |  |  |
| 34 | `DW.ECR.RESERVED.7` | `DwExportCaptureResults_Reserved7` | TField |  |  |
| 35 | `DW.ECR.RESERVED.6` | `DwExportCaptureResults_Reserved6` | TField |  |  |
| 36 | `DW.ECR.RESERVED.5` | `DwExportCaptureResults_Reserved5` | TField |  |  |
| 37 | `DW.ECR.RESERVED.4` | `DwExportCaptureResults_Reserved4` | TField |  |  |
| 38 | `DW.ECR.RESERVED.3` | `DwExportCaptureResults_Reserved3` | TField |  |  |
| 39 | `DW.ECR.RESERVED.2` | `DwExportCaptureResults_Reserved2` | TField |  |  |
| 40 | `DW.ECR.RESERVED.1` | `DwExportCaptureResults_Reserved1` | TField |  |  |
