# WR.REPORT.BOOK — Table Schema

> Source: `INSERTS/I_F.WR.REPORT.BOOK` in `WR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `WR.RB.DESCRIPTION` | `WrReportBook_Description` |  |  |  |
| 2 | `WR.RB.PRINTING.DATE` | `WrReportBook_PrintingDate` | TField |  | Defines the printing date for reports attached to the portfolios or groups that are linked to the report book. Validation Rules: Disallows dates less than TODAY. If the field ONLINE.OR.COB is �ONLINE� the PRITING.DATE allows only TODAY�s date. If the field PRINTING.DATE is null and ONLINE.OR.COB is �ONLINE�, while commiting, the value TODAY�s date is defaulted to the PRINTING.DATE field. |
| 3 | `WR.RB.STMT.FREQ` | `WrReportBook_StmtFreq` | TField | Yes | Specifies the frequency to generate next transaction period. Validations Mandatory field. |
| 4 | `WR.RB.STMT.START.DATE` | `WrReportBook_StmtStartDate` | TField | Yes | Specifies the start date for the list of transactions that are printed in the statement. Validations Mandatory field. |
| 5 | `WR.RB.STMT.END.DATE` | `WrReportBook_StmtEndDate` | TField | Yes | Specifies the end date for the list of transactions that are printed in the statement. Validations Mandatory field. |
| 6 | `WR.RB.PRINT.TYPE` | `WrReportBook_PrintType` | TField |  | Specifies the type of print to choose for printing. Validations Options allowed are: None or Draft Final - updates the field SCHEDULE, PRITING.DATE, PRITING.TYPE, and LAST.RPTD.PRD NEXT.PRD.START to next printing cycle in WR.KYR.INFO |
| 7 | `WR.RB.ONLINE.OR.COB` | `WrReportBook_OnlineOrCob` | TField |  | Specifies whether the report needs to be printed online or during COB. Validations Options allowed are COB/ONLINE. If it is online, PRITING.DATE must be todays date. &#160; &#160; |
| 8 | `WR.RB.RESERVED.05` | `WrReportBook_Reserved05` | TField |  |  |
| 9 | `WR.RB.RESERVED.04` | `WrReportBook_Reserved04` | TField |  |  |
| 10 | `WR.RB.RESERVED.03` | `WrReportBook_Reserved03` | TField |  |  |
| 11 | `WR.RB.RESERVED.02` | `WrReportBook_Reserved02` | TField |  |  |
| 12 | `WR.RB.RESERVED.01` | `WrReportBook_Reserved01` | TField |  |  |
| 13 | `WR.RB.LOCAL.REF` | `WrReportBook_LocalRef` |  |  |  |
| 14 | `WR.RB.RECORD.STATUS` | `WrReportBook_RecordStatus` | String |  |  |
| 15 | `WR.RB.CURR.NO` | `WrReportBook_CurrNo` | String |  |  |
| 16 | `WR.RB.INPUTTER` | `WrReportBook_Inputter` |  |  |  |
| 17 | `WR.RB.DATE.TIME` | `WrReportBook_DateTime` |  |  |  |
| 18 | `WR.RB.AUTHORISER` | `WrReportBook_Authoriser` | String |  |  |
| 19 | `WR.RB.CO.CODE` | `WrReportBook_CoCode` | String |  |  |
| 20 | `WR.RB.DEPT.CODE` | `WrReportBook_DeptCode` | String |  |  |
| 21 | `WR.RB.AUDITOR.CODE` | `WrReportBook_AuditorCode` | String |  |  |
| 22 | `WR.RB.AUDIT.DATE.TIME` | `WrReportBook_AuditDateTime` | String |  |  |
