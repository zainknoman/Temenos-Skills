# CRS.XML.REQUEST — Table Schema

> Source: `INSERTS/I_F.CRS.XML.REQUEST` in `CE_CrsReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CE.CX.YEAR` | `CrsXmlRequest_Year` | TField | Yes | Mandatory field. Allowed Options: Valid Year or Valid Date. YEAR: The latest dated record in CRS.REPORT.BASE will be picked for XML report generation. When there is no CRS.REPORT.BASE records for the year , no XML will be generated. DATE: When the CRS.REPORT.BASE of a specific date is to be used for report generation, then the date can be specified here. When there is no CRS.REPORT.BASE records for the date, no XML will be generated. Validation rules: A valid year or Date |
| 2 | `CE.CX.ACTION` | `CrsXmlRequest_Action` | TField |  | The possible values are as follows. NEW - To generate new report CORRECTION - To generate correction report at file level, i.e., all the Accounts will be displayed in the report CORRECTION-ACCOUNT - To generate correction report with only corrected accounts. In case of Account level correction, only the Accounts that are corrected will be produced in the report. No XML file will be created when there are no corrected accounts to be reported. When Account info is alone corrected, Report type must be OECD0. Acct Report type or Filter condition must be specified when this Action is selected. CORRECTION-REPORTING.FI - To generate correction report with only corrected ReportingFI details. When ReportingFI is corrected, Report type must be OECD2. The default value will be NEW which means the message is being generated for the first time. Validation rules: NEW or CORRECTION or CORRECTION-ACCOUNT or CORRECTION-REPORTING.FI |
| 3 | `CE.CX.REPORT.TYPE` | `CrsXmlRequest_ReportType` | TField |  |  |
| 4 | `CE.CX.FILTER.COND` | `CrsXmlRequest_FilterCond` | TField |  | Defined filter conditions if any, to be added at the time of selecting CRS.REPORT.BASE table (or COUNTRY.TABLE) for XML generation. Validation rules: The filter conditions will be applied to the table defined in CRS.REPORTING.PARAMETER>COUNTRY.TABLE field. If it is not configured, it will filter CRS.REPORT.BASE records. The operands that can be used are EQ,NE,LK,UL,GE,LE,GT,LT For example to select Luxembourg specific Report base records whose record ID starts with the Luxembourg country code, the filter condition @ID LK LU... can be used. |
| 5 | `CE.CX.FINAL.SUBMISSION` | `CrsXmlRequest_FinalSubmission` | TField |  | Field to specify if the report is generated for final submission to the tax authority. Corrected Reference IDs will be updated in CRS.REPORT.BASE only during Final submission. Validation rules: YES or NO field |
| 6 | `CE.CX.ACCT.REPORT.TYPE` | `CrsXmlRequest_AcctReportType` | TField |  | Specifies the type of Accounts that are to be included in the Correction Report. Input allowed only when Action is CORRECTION-ACCOUNT. OECD1 - New Accounts OECD2 - Corrected Accounts OECD3 - Deleted Accounts ALL - All Accounts that are newly added, corrected or deleted with Correction Status as CORRECTED. |
| 7 | `CE.CX.RESERVED.7` | `CrsXmlRequest_Reserved7` | TField |  |  |
| 8 | `CE.CX.RESERVED.6` | `CrsXmlRequest_Reserved6` | TField |  |  |
| 9 | `CE.CX.RESERVED.5` | `CrsXmlRequest_Reserved5` | TField |  |  |
| 10 | `CE.CX.RESERVED.4` | `CrsXmlRequest_Reserved4` | TField |  |  |
| 11 | `CE.CX.RESERVED.3` | `CrsXmlRequest_Reserved3` | TField |  |  |
| 12 | `CE.CX.RESERVED.2` | `CrsXmlRequest_Reserved2` | TField |  |  |
| 13 | `CE.CX.RESERVED.1` | `CrsXmlRequest_Reserved1` | TField |  |  |
| 14 | `CE.CX.LOCAL.REF` | `CrsXmlRequest_LocalRef` |  |  |  |
| 15 | `CE.CX.OVERRIDE` | `CrsXmlRequest_Override` |  |  |  |
| 16 | `CE.CX.RECORD.STATUS` | `CrsXmlRequest_RecordStatus` | String |  |  |
| 17 | `CE.CX.CURR.NO` | `CrsXmlRequest_CurrNo` | String |  |  |
| 18 | `CE.CX.INPUTTER` | `CrsXmlRequest_Inputter` |  |  |  |
| 19 | `CE.CX.DATE.TIME` | `CrsXmlRequest_DateTime` |  |  |  |
| 20 | `CE.CX.AUTHORISER` | `CrsXmlRequest_Authoriser` | String |  |  |
| 21 | `CE.CX.CO.CODE` | `CrsXmlRequest_CoCode` | String |  |  |
| 22 | `CE.CX.DEPT.CODE` | `CrsXmlRequest_DeptCode` | String |  |  |
| 23 | `CE.CX.AUDITOR.CODE` | `CrsXmlRequest_AuditorCode` | String |  |  |
| 24 | `CE.CX.AUDIT.DATE.TIME` | `CrsXmlRequest_AuditDateTime` | String |  |  |
