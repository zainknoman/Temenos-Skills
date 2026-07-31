# PP.CLEARING.RETURNCODE — Table Schema

> Source: `INSERTS/I_F.PP.CLEARING.RETURNCODE` in `PP_DirectDebitChequeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CGR.CompanyID` | `PpClearingReturncode_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.CGR.ClearingID` | `PpClearingReturncode_Clearingid` | TField |  | Specifies the name of the clearing in the payments hub. It is NOINPUT field. On click of validate button, ClearingID gets autopopulated from ID. |
| 3 | `PP.CGR.ClearingReturnCode` | `PpClearingReturncode_Clearingreturncode` | TField |  | Indicates the Return Code (reason) for rejection Clearing. It is NOINPUT field. On click of validate button, ClearingReturnCode gets autopopulated from ID. |
| 4 | `PP.CGR.ReturnCodeLevel` | `PpClearingReturncode_Returncodelevel` |  |  |  |
| 5 | `PP.CGR.RouteToException` | `PpClearingReturncode_Routetoexception` |  |  |  |
| 6 | `PP.CGR.ReturnCodeDescription` | `PpClearingReturncode_Returncodedescription` |  |  |  |
| 7 | `PP.CGR.ClearingTransactionType` | `PpClearingReturncode_Clearingtransactiontype` |  |  |  |
| 8 | `PP.CGR.ClearingNatureCode` | `PpClearingReturncode_Clearingnaturecode` |  |  |  |
| 9 | `PP.CGR.ReturnAllowedDays` | `PpClearingReturncode_Returnalloweddays` |  |  |  |
| 10 | `PP.CGR.Type` | `PpClearingReturncode_Type` |  |  |  |
| 11 | `PP.CGR.ReasonCodeType` | `PpClearingReturncode_Reasoncodetype` |  |  |  |
| 12 | `PP.CGR.BankCustInitiated` | `PpClearingReturncode_Bankcustinitiated` |  |  |  |
| 13 | `PP.CGR.AddInfo` | `PpClearingReturncode_Addinfo` | TField |  | This field is used to store Tag name that causing error and returning the incoming transaction, e.g a MT103 message Validation Rules:This field is applicable only for SWIFT Based RTGS systems, not to be configured for other type of clearing. |
| 14 | `PP.CGR.LOCAL.REF` | `PpClearingReturncode_LocalRef` |  |  |  |
| 15 | `PP.CGR.OVERRIDE` | `PpClearingReturncode_Override` |  |  |  |
| 16 | `PP.CGR.RECORD.STATUS` | `PpClearingReturncode_RecordStatus` | String |  |  |
| 17 | `PP.CGR.CURR.NO` | `PpClearingReturncode_CurrNo` | String |  |  |
| 18 | `PP.CGR.INPUTTER` | `PpClearingReturncode_Inputter` |  |  |  |
| 19 | `PP.CGR.DATE.TIME` | `PpClearingReturncode_DateTime` |  |  |  |
| 20 | `PP.CGR.AUTHORISER` | `PpClearingReturncode_Authoriser` | String |  |  |
| 21 | `PP.CGR.CO.CODE` | `PpClearingReturncode_CoCode` | String |  |  |
| 22 | `PP.CGR.DEPT.CODE` | `PpClearingReturncode_DeptCode` | String |  |  |
| 23 | `PP.CGR.AUDITOR.CODE` | `PpClearingReturncode_AuditorCode` | String |  |  |
| 24 | `PP.CGR.AUDIT.DATE.TIME` | `PpClearingReturncode_AuditDateTime` | String |  |  |
