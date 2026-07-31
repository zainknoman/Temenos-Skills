# WR.KYR.INFO — Table Schema

> Source: `INSERTS/I_F.WR.KYR.INFO` in `WR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `WR.KYR.NAME` | `WrKyrInfo_Name` |  |  |  |
| 2 | `WR.KYR.DESCRIPTION` | `WrKyrInfo_Description` |  |  |  |
| 3 | `WR.KYR.ID.REPORT` | `WrKyrInfo_IdReport` |  |  |  |
| 4 | `WR.KYR.ID.CONF.ITEM` | `WrKyrInfo_IdConfItem` |  |  |  |
| 5 | `WR.KYR.ID.ENQ` | `WrKyrInfo_IdEnq` |  |  |  |
| 6 | `WR.KYR.SCHEDULE` | `WrKyrInfo_Schedule` |  |  |  |
| 7 | `WR.KYR.ADDRESS` | `WrKyrInfo_Address` |  |  |  |
| 8 | `WR.KYR.NO.OF.COPIES` | `WrKyrInfo_NoOfCopies` |  |  |  |
| 9 | `WR.KYR.LAST.RPTD.PRD` | `WrKyrInfo_LastRptdPrd` |  |  |  |
| 10 | `WR.KYR.NEXT.PRD.START` | `WrKyrInfo_NextPrdStart` |  |  |  |
| 11 | `WR.KYR.RESERVED.10` | `WrKyrInfo_Reserved10` |  |  |  |
| 12 | `WR.KYR.RESERVED.09` | `WrKyrInfo_Reserved09` |  |  |  |
| 13 | `WR.KYR.RESERVED.08` | `WrKyrInfo_Reserved08` |  |  |  |
| 14 | `WR.KYR.RESERVED.07` | `WrKyrInfo_Reserved07` |  |  |  |
| 15 | `WR.KYR.RESERVED.06` | `WrKyrInfo_Reserved06` |  |  |  |
| 16 | `WR.KYR.ONLINE` | `WrKyrInfo_Online` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 17 | `WR.KYR.RECEIVER.CUSTOMER` | `WrKyrInfo_ReceiverCustomer` |  |  |  |
| 18 | `WR.KYR.RECEIVER.ADDRESS` | `WrKyrInfo_ReceiverAddress` |  |  |  |
| 19 | `WR.KYR.RECEIVER.HLD.EMAIL` | `WrKyrInfo_ReceiverHldEmail` |  |  |  |
| 20 | `WR.KYR.LOCKING.DATE` | `WrKyrInfo_LockingDate` | TField |  | Holds the locking date. Any back-date contract made prior to locking date does not affect the valuation and performance details until this date. Instead, the effect of the back dated contract reflects from next working day after the locking date. |
| 21 | `WR.KYR.REPORT.BOOK` | `WrKyrInfo_ReportBook` | TField | No | Populates the dates and printing parameters from WR.REPORT.BOOK Validations Optional field &#160; |
| 22 | `WR.KYR.PRINTING.DATE` | `WrKyrInfo_PrintingDate` | TField |  | Description Specifies the printing date. Validations Populated from WR.REQUEST.REPORT or WR.REPORT.BOOK No validation. |
| 23 | `WR.KYR.PRINT.TYPE` | `WrKyrInfo_PrintType` | TField |  | Specifies the type of print to choose for printing. Validations Options allowed are: None or Draft Final - updates the fields SCHEDULE, PRITING.DATE, PRITING.TYPE, and LAST.RPTD.PRD NEXT.PRD.START to next printing cycle in WR.KYR.INFO |
| 24 | `WR.KYR.PRINT.CATEGORY` | `WrKyrInfo_PrintCategory` | TField |  | Specifies the print category either discretionary or managed client. Validations Options allowed are ADHOC/BOOK Populated from WR.REQUEST.REPORT or WR.REPORT.BOOK |
| 25 | `WR.KYR.RESERVED.05` | `WrKyrInfo_Reserved05` | TField |  |  |
| 26 | `WR.KYR.RESERVED.04` | `WrKyrInfo_Reserved04` | TField |  |  |
| 27 | `WR.KYR.RESERVED.03` | `WrKyrInfo_Reserved03` | TField |  |  |
| 28 | `WR.KYR.RESERVED.02` | `WrKyrInfo_Reserved02` | TField |  |  |
| 29 | `WR.KYR.RESERVED.01` | `WrKyrInfo_Reserved01` | TField |  |  |
| 30 | `WR.KYR.LOCAL.REF` | `WrKyrInfo_LocalRef` |  |  |  |
| 31 | `WR.KYR.RECORD.STATUS` | `WrKyrInfo_RecordStatus` | String |  |  |
| 32 | `WR.KYR.CURR.NO` | `WrKyrInfo_CurrNo` | String |  |  |
| 33 | `WR.KYR.INPUTTER` | `WrKyrInfo_Inputter` |  |  |  |
| 34 | `WR.KYR.DATE.TIME` | `WrKyrInfo_DateTime` |  |  |  |
| 35 | `WR.KYR.AUTHORISER` | `WrKyrInfo_Authoriser` | String |  |  |
| 36 | `WR.KYR.CO.CODE` | `WrKyrInfo_CoCode` | String |  |  |
| 37 | `WR.KYR.DEPT.CODE` | `WrKyrInfo_DeptCode` | String |  |  |
| 38 | `WR.KYR.AUDITOR.CODE` | `WrKyrInfo_AuditorCode` | String |  |  |
| 39 | `WR.KYR.AUDIT.DATE.TIME` | `WrKyrInfo_AuditDateTime` | String |  |  |
