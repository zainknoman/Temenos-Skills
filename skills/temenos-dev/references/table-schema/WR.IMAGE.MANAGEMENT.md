# WR.IMAGE.MANAGEMENT — Table Schema

> Source: `INSERTS/I_F.WR.IMAGE.MANAGEMENT` in `WR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `WR.IMN.REPORT.DESCRIPTION` | `WrImageManagement_ReportDescription` | TField |  | Description of the report.This will be used to populate the field 'Description' on IM.DOCUMENT.IMAGE. |
| 2 | `WR.IMN.REPORT.SHORT.NAME` | `WrImageManagement_ReportShortName` | TField |  | Short Name of the report.This will be used to populate the field 'Short Description' on IM.DOCUMENT.IMAGE. |
| 3 | `WR.IMN.REPORT.TYPE` | `WrImageManagement_ReportType` | TField |  | Type of report i.e. the entity the report is based around.Report types can be CUSTOMER, PORTFOLIO or ACCOUNT. |
| 4 | `WR.IMN.REPORT.INSTANCE` | `WrImageManagement_ReportInstance` | TField |  | This is either the customer, portfolio or account to which the .pdf report relates. |
| 5 | `WR.IMN.REPORT.KEY` | `WrImageManagement_ReportKey` | TField |  | This is the file name for the .pdf report to which this Image Management record relates. |
| 6 | `WR.IMN.UPDATE.IMAGE` | `WrImageManagement_UpdateImage` | TField |  | This flag is set to 'YES' when Image Management tables are to be updated. On authorisation, the system creates WR.IMAGE.MANAGEMENT and a WR.IMAGE.UPLOAD record based on the information in this record. This can only happen once per record. |
| 7 | `WR.IMN.STATUS` | `WrImageManagement_Status` | TField |  | This is the status of the report - for information only. |
| 8 | `WR.IMN.FROM.DATE` | `WrImageManagement_FromDate` | TField |  | This is the start date of the report - for information only. |
| 9 | `WR.IMN.TO.DATE` | `WrImageManagement_ToDate` | TField |  | This is the end date of the report - for information only. |
| 10 | `WR.IMN.REQUESTOR` | `WrImageManagement_Requestor` | TField |  | The original requestor of the report.If the reports have been kicked off via a COB process, this will be the user record attached to the COB process itself.If the reports have been run via an adhoc process by a user, this will be the user id for that particular user.This field is only inputtable on the first instance of the record i.e. through OFS from the calling process. |
| 11 | `WR.IMN.FUND.MANAGER` | `WrImageManagement_FundManager` | TField |  | Fund manager for this customer, portfolio or account - free text field. |
| 12 | `WR.IMN.ACCOUNT.OFFICER` | `WrImageManagement_AccountOfficer` | TField |  | This is the account officer for the customer, portfolio or account defined in the Report Instance field. The account officer is defaulted from the CUSTOMER, SEC.ACC.MASTER or ACCOUNT record, but can be overridden here if the user decides to do so. |
| 13 | `WR.IMN.IM.DOCUMENT.UPLOAD` | `WrImageManagement_ImDocumentUpload` | TField |  | Document upload key. This is the IM.DOCUMENT.UPLOAD record created when 'Update Image' flag was set to YES and the record authorised. Once set, this cannot be changed.System-generated field only. |
| 14 | `WR.IMN.REPORT.COMPANY` | `WrImageManagement_ReportCompany` | TField |  |  |
| 15 | `WR.IMN.RESERVED.19` | `WrImageManagement_Reserved19` | TField |  |  |
| 16 | `WR.IMN.RESERVED.18` | `WrImageManagement_Reserved18` | TField |  |  |
| 17 | `WR.IMN.RESERVED.17` | `WrImageManagement_Reserved17` | TField |  |  |
| 18 | `WR.IMN.RESERVED.16` | `WrImageManagement_Reserved16` | TField |  |  |
| 19 | `WR.IMN.RESERVED.15` | `WrImageManagement_Reserved15` | TField |  |  |
| 20 | `WR.IMN.RESERVED.14` | `WrImageManagement_Reserved14` | TField |  |  |
| 21 | `WR.IMN.RESERVED.13` | `WrImageManagement_Reserved13` | TField |  |  |
| 22 | `WR.IMN.RESERVED.12` | `WrImageManagement_Reserved12` | TField |  |  |
| 23 | `WR.IMN.RESERVED.11` | `WrImageManagement_Reserved11` | TField |  |  |
| 24 | `WR.IMN.RESERVED.10` | `WrImageManagement_Reserved10` | TField |  |  |
| 25 | `WR.IMN.RESERVED.09` | `WrImageManagement_Reserved09` | TField |  |  |
| 26 | `WR.IMN.RESERVED.08` | `WrImageManagement_Reserved08` | TField |  |  |
| 27 | `WR.IMN.RESERVED.07` | `WrImageManagement_Reserved07` | TField |  |  |
| 28 | `WR.IMN.RESERVED.06` | `WrImageManagement_Reserved06` | TField |  |  |
| 29 | `WR.IMN.RESERVED.05` | `WrImageManagement_Reserved05` | TField |  |  |
| 30 | `WR.IMN.RESERVED.04` | `WrImageManagement_Reserved04` | TField |  |  |
| 31 | `WR.IMN.RESERVED.03` | `WrImageManagement_Reserved03` | TField |  |  |
| 32 | `WR.IMN.RESERVED.02` | `WrImageManagement_Reserved02` | TField |  |  |
| 33 | `WR.IMN.RESERVED.01` | `WrImageManagement_Reserved01` | TField |  |  |
| 34 | `WR.IMN.RECORD.STATUS` | `WrImageManagement_RecordStatus` | String |  |  |
| 35 | `WR.IMN.CURR.NO` | `WrImageManagement_CurrNo` | String |  |  |
| 36 | `WR.IMN.INPUTTER` | `WrImageManagement_Inputter` |  |  |  |
| 37 | `WR.IMN.DATE.TIME` | `WrImageManagement_DateTime` |  |  |  |
| 38 | `WR.IMN.AUTHORISER` | `WrImageManagement_Authoriser` | String |  |  |
| 39 | `WR.IMN.CO.CODE` | `WrImageManagement_CoCode` | String |  |  |
| 40 | `WR.IMN.DEPT.CODE` | `WrImageManagement_DeptCode` | String |  |  |
| 41 | `WR.IMN.AUDITOR.CODE` | `WrImageManagement_AuditorCode` | String |  |  |
| 42 | `WR.IMN.AUDIT.DATE.TIME` | `WrImageManagement_AuditDateTime` | String |  |  |
