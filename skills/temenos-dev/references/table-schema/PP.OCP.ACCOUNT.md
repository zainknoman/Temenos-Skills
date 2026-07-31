# PP.OCP.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.PP.OCP.ACCOUNT` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.OCP.CompanyID` | `PpOcpAccount_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. The value links to the field �CompanyID� in PP.COMPANY.PROPERTIES.CONCAT |
| 2 | `PP.OCP.Currency1` | `PpOcpAccount_Currency1` | TField |  | This field defines Currency 1 of the currency pair for which OCP account is defined. |
| 3 | `PP.OCP.Currency2` | `PpOcpAccount_Currency2` | TField |  | This field defines Currency 2 of the currency pair for which OCP account is defined. |
| 4 | `PP.OCP.AccountType` | `PpOcpAccount_Accounttype` | TField |  | Account Type. Possible Values: C - Client N - Nostro V - Vostro/Loro I - Suspense/Internal PL - P&amp;L Account |
| 5 | `PP.OCP.AccountCompanyID` | `PpOcpAccount_Accountcompanyid` | TField |  | This field defines Company code of the respective account. |
| 6 | `PP.OCP.Account` | `PpOcpAccount_Account` | TField |  | This field defines the Open Currency Position account for the respective currency pair. |
| 7 | `PP.OCP.AccountCurrency` | `PpOcpAccount_Accountcurrency` | TField |  | This field defines Currency of the OCP account. |
| 8 | `PP.OCP.StartDateOCPAccount` | `PpOcpAccount_Startdateocpaccount` | TField |  | Specifies the date from which the record is considered active for payments processing. |
| 9 | `PP.OCP.EndDateOCPAccount` | `PpOcpAccount_Enddateocpaccount` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 10 | `PP.OCP.RAC` | `PpOcpAccount_Rac` | TField |  | Record Activation Code generated for the record by the payment's hub. Possible values: N - Not active A - Active H-YYYYMMDDHHMMSSsss - History. Where: YYYY - year, MM - month, DD - day, HH - hour, MM - minutes, SS - seconds and sss - miliseconds. F - Future C - Not active future Validation Rules: 19 alphanumeric characters. The value is not editable by the user. |
| 11 | `PP.OCP.RSC` | `PpOcpAccount_Rsc` | TField |  | Record Status Code generated for the record by the payments hub. Possible values: L - Live U - Unapproved R - Reversed MF - Modified future Validation Rules: 1 alphanumeric character. The value is not editable by the user. |
| 12 | `PP.OCP.OldID` | `PpOcpAccount_Oldid` | TField |  | Used for internal purpose.Holds the ID of the previous live record of store table. This field can hold upto 65 alphanumeric characters and the value is not editable by the user. |
| 13 | `PP.OCP.CurrentID` | `PpOcpAccount_Currentid` | TField |  | Used for internal purpose.Holds the ID of the current live record of store table. This field can hold upto 65 alphanumeric characters and the value is not editable by the user. |
| 14 | `PP.OCP.Action` | `PpOcpAccount_Action` | TField |  | Used for internal purpose. Value of this field determines values of fields, 'RAC' and 'RSC' Possible values: N - New M - Modified R - Reverse This field can hold upto 1 alphanumeric character and the value is not editable by the user. |
| 15 | `PP.OCP.OVERRIDE` | `PpOcpAccount_Override` |  |  |  |
| 16 | `PP.OCP.RECORD.STATUS` | `PpOcpAccount_RecordStatus` | String |  |  |
| 17 | `PP.OCP.CURR.NO` | `PpOcpAccount_CurrNo` | String |  |  |
| 18 | `PP.OCP.INPUTTER` | `PpOcpAccount_Inputter` |  |  |  |
| 19 | `PP.OCP.DATE.TIME` | `PpOcpAccount_DateTime` |  |  |  |
| 20 | `PP.OCP.AUTHORISER` | `PpOcpAccount_Authoriser` | String |  |  |
| 21 | `PP.OCP.CO.CODE` | `PpOcpAccount_CoCode` | String |  |  |
| 22 | `PP.OCP.DEPT.CODE` | `PpOcpAccount_DeptCode` | String |  |  |
| 23 | `PP.OCP.AUDITOR.CODE` | `PpOcpAccount_AuditorCode` | String |  |  |
| 24 | `PP.OCP.AUDIT.DATE.TIME` | `PpOcpAccount_AuditDateTime` | String |  |  |
