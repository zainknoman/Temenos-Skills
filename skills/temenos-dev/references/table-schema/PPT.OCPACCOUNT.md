# PPT.OCPACCOUNT — Table Schema

> Source: `INSERTS/I_F.PPT.OCPACCOUNT` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPOCP.CompanyID` | `PptOcpaccount_Companyid` | TField | Yes | Indicates the company ID for which the record is created. identify the Owning Bank. Example : BNK,GB1 Validation Rules: Mandatory field. 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY |
| 2 | `PPOCP.Currency1` | `PptOcpaccount_Currency1` | TField | Yes | This field defines Currency 1 of the currency pair for which OCP account is defined. Validation Rules: Mandatory field. 3 alphanumeric characters.The value links to the field 'CurrencyCode' in PPT.CURRENCY and cannot be the same as field 'Currency2'. |
| 3 | `PPOCP.Currency2` | `PptOcpaccount_Currency2` | TField | Yes | This field defines Currency 2 of the currency pair for which OCP account is defined. Validation Rules: Mandatory field. 3 alphanumeric characters.The value links to the field 'CurrencyCode' in PPT.CURRENCY and cannot be the same as field 'Currency1'. |
| 4 | `PPOCP.StartDateOCPAccount` | `PptOcpaccount_Startdateocpaccount` | TField |  | Specifies the date from which the record is considered active for payments processing. Validation Rules: 11 characters DATE format. |
| 5 | `PPOCP.AccountType` | `PptOcpaccount_Accounttype` | TField |  | Account Type. Possible Values: C - Client N - Nostro V - Vostro/Loro I - Suspense/Internal PL - P&amp;L Account Validation Rules: 20 alphanumeric characters. |
| 6 | `PPOCP.AccountCompanyID` | `PptOcpaccount_Accountcompanyid` | TField |  | This field defines Company code of the respective account. Validation Rules: 3 alphanumeric characters. |
| 7 | `PPOCP.Account` | `PptOcpaccount_Account` | TField |  | This field defines the Open Currency Position account for the respective currency pair. Validation Rules: 35 alphanumeric characters. |
| 8 | `PPOCP.AccountCurrency` | `PptOcpaccount_Accountcurrency` | TField |  | This field defines Currency of the OCP account. Validation Rules: 3 alphanumeric characters. |
| 9 | `PPOCP.EndDateOCPAccount` | `PptOcpaccount_Enddateocpaccount` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. Validation Rules: 11 characters DATE format. |
| 10 | `PPOCP.RACOCPAccount` | `PptOcpaccount_Racocpaccount` | TField |  |  |
| 11 | `PPOCP.RSCOCPAccount` | `PptOcpaccount_Rscocpaccount` | TField |  |  |
| 12 | `PPOCP.EntryUserID` | `PptOcpaccount_Entryuserid` | TField |  | Indicates the user that created or modified the entry. Validation Rules: 30 alphanumeric characters. The value is not editable by the user. |
| 13 | `PPOCP.EntryDateTime` | `PptOcpaccount_Entrydatetime` | TField |  | Indicates the system date and time when the entry was created or modified. Validation Rules: 17 characters Date Time format. It need to be displayed as DD MMM YYYY HH:MM:SS.sss. Example: 12 JAN 2015 12:34:25.123 The value is not editable by the user. |
| 14 | `PPOCP.ApproverUserID` | `PptOcpaccount_Approveruserid` | TField |  | Indicates the name of the user who approved the entry. Validation Rules: 30 alphanumeric characters. The value is not editable by the user. |
| 15 | `PPOCP.ApprovedDateTime` | `PptOcpaccount_Approveddatetime` | TField |  | Indicates the system date and time when the entry was approved. Validation Rules: 17 characters Date Time format. It need to be displayed as DD MMM YYYY HH:MM:SS.sss. Example: 12 JAN 2015 12:34:25.123 The value is not editable by the user. |
