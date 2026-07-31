# PP.CLEARING.COMPANY — Table Schema

> Source: `INSERTS/I_F.PP.CLEARING.COMPANY` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CCM.CompanyID` | `PpClearingCompany_Companyid` | TField | Yes | desc>Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: Mandatory field 3 alphanumeric characters. The value links to the field �CompanyID� in PP.COMPANY.PROPERTIES.CONCAT |
| 2 | `PP.CCM.ClearingName` | `PpClearingCompany_Clearingname` | TField |  | Specifies the name of clearing for which company details are defined. Validation Rules: 128 alphanumeric characters. |
| 3 | `PP.CCM.ClearingID` | `PpClearingCompany_Clearingid` |  |  |  |
| 4 | `PP.CCM.ClearingAccountCompany` | `PpClearingCompany_Clearingaccountcompany` |  |  |  |
| 5 | `PP.CCM.ClearingAccountCurrency` | `PpClearingCompany_Clearingaccountcurrency` |  |  |  |
| 6 | `PP.CCM.ClearingAccountNumber` | `PpClearingCompany_Clearingaccountnumber` |  |  |  |
| 7 | `PP.CCM.AlternateIdentifier` | `PpClearingCompany_Alternateidentifier` |  |  |  |
| 8 | `PP.CCM.LOCAL.REF` | `PpClearingCompany_LocalRef` |  |  |  |
| 9 | `PP.CCM.OVERRIDE` | `PpClearingCompany_Override` |  |  |  |
| 10 | `PP.CCM.RECORD.STATUS` | `PpClearingCompany_RecordStatus` | String |  |  |
| 11 | `PP.CCM.CURR.NO` | `PpClearingCompany_CurrNo` | String |  |  |
| 12 | `PP.CCM.INPUTTER` | `PpClearingCompany_Inputter` |  |  |  |
| 13 | `PP.CCM.DATE.TIME` | `PpClearingCompany_DateTime` |  |  |  |
| 14 | `PP.CCM.AUTHORISER` | `PpClearingCompany_Authoriser` | String |  |  |
| 15 | `PP.CCM.CO.CODE` | `PpClearingCompany_CoCode` | String |  |  |
| 16 | `PP.CCM.DEPT.CODE` | `PpClearingCompany_DeptCode` | String |  |  |
| 17 | `PP.CCM.AUDITOR.CODE` | `PpClearingCompany_AuditorCode` | String |  |  |
| 18 | `PP.CCM.AUDIT.DATE.TIME` | `PpClearingCompany_AuditDateTime` | String |  |  |
| 19 | `PP.CCM.ClearingTransactionType` | `PpClearingCompany_Clearingtransactiontype` |  |  |  |
