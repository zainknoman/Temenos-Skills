# WR.REPORT.ENQUIRY — Table Schema

> Source: `INSERTS/I_F.WR.REPORT.ENQUIRY` in `WR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `WR.RE.ENQ.DESCRIPTION` | `WrReportEnquiry_EnqDescription` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `WR.RE.BREAKDOWN.ID` | `WrReportEnquiry_BreakdownId` |  |  |  |
| 3 | `WR.RE.BRKDOWN.COL` | `WrReportEnquiry_BrkdownCol` |  |  |  |
| 4 | `WR.RE.BRKDOWN.COL.DES` | `WrReportEnquiry_BrkdownColDes` |  |  |  |
| 5 | `WR.RE.DESCRIPTION` | `WrReportEnquiry_Description` |  |  |  |
| 6 | `WR.RE.T24column` | `WrReportEnquiry_T24column` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `WR.RE.RESERVED.05` | `WrReportEnquiry_Reserved05` | TField |  |  |
| 8 | `WR.RE.RESERVED.04` | `WrReportEnquiry_Reserved04` | TField |  |  |
| 9 | `WR.RE.RESERVED.03` | `WrReportEnquiry_Reserved03` | TField |  |  |
| 10 | `WR.RE.RESERVED.02` | `WrReportEnquiry_Reserved02` | TField |  |  |
| 11 | `WR.RE.RESERVED.01` | `WrReportEnquiry_Reserved01` | TField |  |  |
| 12 | `WR.RE.RECORD.STATUS` | `WrReportEnquiry_RecordStatus` | String |  |  |
| 13 | `WR.RE.CURR.NO` | `WrReportEnquiry_CurrNo` | String |  |  |
| 14 | `WR.RE.INPUTTER` | `WrReportEnquiry_Inputter` |  |  |  |
| 15 | `WR.RE.DATE.TIME` | `WrReportEnquiry_DateTime` |  |  |  |
| 16 | `WR.RE.AUTHORISER` | `WrReportEnquiry_Authoriser` | String |  |  |
| 17 | `WR.RE.CO.CODE` | `WrReportEnquiry_CoCode` | String |  |  |
| 18 | `WR.RE.DEPT.CODE` | `WrReportEnquiry_DeptCode` | String |  |  |
| 19 | `WR.RE.AUDITOR.CODE` | `WrReportEnquiry_AuditorCode` | String |  |  |
| 20 | `WR.RE.AUDIT.DATE.TIME` | `WrReportEnquiry_AuditDateTime` | String |  |  |
