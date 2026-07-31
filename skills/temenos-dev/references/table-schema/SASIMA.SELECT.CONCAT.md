# SASIMA.SELECT.CONCAT — Table Schema

> Source: `INSERTS/I_F.SASIMA.SELECT.CONCAT` in `SASIMA_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SS.CT.REPORT.DATE` | `SasimaSelectConcat_ReportDate` | TField |  | Gets updated to TODAY upon authorisation of the activities to which the APIs are attached |
| 2 | `SS.CT.PROCESS.FLAG` | `SasimaSelectConcat_ProcessFlag` | TField |  | Y/N/REV field denotes if the file extract has been processed or not This field is updated to yes ,each time when the CONCAT table is updated Post the extraction this field is updated to N Allowed Values Y/N/REV |
| 3 | `SS.CT.DEFAULT.FLAG` | `SasimaSelectConcat_DefaultFlag` | TField |  | this field denotes the default status of the arrangement allowed values WN/WY This filed will be updated to WY, when the overdue bill exceeds the maximum number of delinq days defined at the parameter level. Post the default extraction this field will be updated to WN |
| 4 | `SS.CT.REPORT.REASON` | `SasimaSelectConcat_ReportReason` | TField |  | Specifies the reason such as Negotiated settled, Fully settled etc. for the default file upload. Not Multi value field. This field gets updated during default file extraction based on the logic defined in logic for outstanding amount |
| 5 | `SS.CT.CUSTOMER` | `SasimaSelectConcat_Customer` |  |  |  |
| 6 | `SS.CT.OUTSTANDING.BALANCE` | `SasimaSelectConcat_OutstandingBalance` | TField |  |  |
| 7 | `SS.CT.REPORT.TIME` | `SasimaSelectConcat_ReportTime` | TField |  | Specifies the date on which the file will be reported Valid T24 date type field. Gets updated to TODAY upon authorisation of the activities to which the APIs are attached |
| 8 | `SS.CT.CURRENT.CYCLE.DATE` | `SasimaSelectConcat_CurrentCycleDate` | TField |  | To store the last cyclic date reported |
| 9 | `SS.CT.LAST.BILL.ID` | `SasimaSelectConcat_LastBillId` | TField |  | To store the last bill id reported |
| 10 | `SS.CT.REVERSAL.RECORD` | `SasimaSelectConcat_ReversalRecord` | TField |  | Field to store the xml file generated when new loan is created |
| 11 | `SS.CT.PRODUCT.NAME` | `SasimaSelectConcat_ProductName` | TField |  | To specify the product of the contract |
| 12 | `SS.CT.REPORT.DATA` | `SasimaSelectConcat_ReportData` | TField |  | To set and retrive the values during file processing |
| 13 | `SS.CT.DUE.DATES` | `SasimaSelectConcat_DueDates` |  |  |  |
| 14 | `SS.CT.DUE.AMTS` | `SasimaSelectConcat_DueAmts` |  |  |  |
| 15 | `SS.CT.OVERDUE.DAYS` | `SasimaSelectConcat_OverdueDays` | TField |  | To store the Arrangement Overdue Days values |
