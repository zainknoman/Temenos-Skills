# PP.BANK.CODE — Table Schema

> Source: `INSERTS/I_F.PP.BANK.CODE` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BCD.BankCodeID` | `PpBankCode_Bankcodeid` | TField |  | Unique Identifier, system generated |
| 2 | `PP.BCD.CompanyID` | `PpBankCode_Companyid` | TField | Yes | Indicates the Company to which this record belongs to. Example : BNK,GB1 Validation Rules: Mandatory field 3 alphanumeric characters. The value links to the field �CompanyID� in PP.COMPANY.PROPERTIES.CONCAT |
| 3 | `PP.BCD.CountryCode` | `PpBankCode_Countrycode` | TField |  | Denotes the country for which the National ID is defined. |
| 4 | `PP.BCD.NationalID` | `PpBankCode_Nationalid` | TField |  | The National identifier of the institution/branch otherwise called NCC(National Clearing Code) |
| 5 | `PP.BCD.BICCode` | `PpBankCode_Biccode` | TField |  | HOlds the unique BIC of the institution from the BIC directory. Can be maximum of 11 characters. BIC comprises of Institution code (4 characters) Country code (2 characters) Location code (2 characters) Branch code (3 characters � XXX denotes main or head office) |
| 6 | `PP.BCD.FinancialInstitutionName` | `PpBankCode_Financialinstitutionname` | TField |  | Name of the financial institution or bank |
| 7 | `PP.BCD.ZIPCode` | `PpBankCode_Zipcode` | TField |  | Post code of the institution/branch. |
| 8 | `PP.BCD.CityName` | `PpBankCode_Cityname` | TField |  | Name of the city where the institution/branch is located. |
| 9 | `PP.BCD.CheckDigitMethod` | `PpBankCode_Checkdigitmethod` | TField |  | This is applicable only for EMZ clearing. Every BLZ has a logic for validating the account number. This field stores the method for validating that BLZ code. |
| 10 | `PP.BCD.OverrideThroughUpload` | `PpBankCode_Overridethroughupload` | TField |  | Specifies whether this specific record can be overwritten when uploaded from a file. To prevent data upload to overwrite this record, set this field to 'N'. Else, set it to 'Y'. |
| 11 | `PP.BCD.SourceKey` | `PpBankCode_Sourcekey` | TField |  | This attribute links to the SourceKey in BICTable. |
| 12 | `PP.BCD.OriginatingSource` | `PpBankCode_Originatingsource` | TField |  | The source from which details of bank code was updated. This is a free text field |
| 13 | `PP.BCD.IBANBIC` | `PpBankCode_Ibanbic` | TField |  | Contains the BIC-11 issued together with the IBANs for the institution�s clients. Institution code (4 characters) Country code (2 characters) Location code (2 characters) Branch code (3 characters � XXX to denote head or main office) |
| 14 | `PP.BCD.IBANCountryCode` | `PpBankCode_Ibancountrycode` | TField |  | Country code in the IBAN. This follows ISO 3166-1, contains only alphabets and is 2 character long. Under certain circumstances this can be different from the country indicated in field Country Name |
| 15 | `PP.BCD.IBANNationalID` | `PpBankCode_Ibannationalid` | TField |  | The National ID which is as part of the IBAN. |
| 16 | `PP.BCD.StartDateBankCode` | `PpBankCode_Startdatebankcode` | TField |  | Specifies the date on which the record is to be considered active by the payments hub. |
| 17 | `PP.BCD.EndDateBankCode` | `PpBankCode_Enddatebankcode` | TField |  | Specifies the date on which the record is to be considered inactive by the payments hub. |
| 18 | `PP.BCD.RAC` | `PpBankCode_Rac` | TField |  | Record Activation Code generated for the record by the payment's hub. Possible values: N - Not active A - Active H-YYYYMMDDHHMMSSsss - History. Where: YYYY - year, MM - month, DD - day, HH - hour, MM - minutes, SS - seconds and sss - miliseconds F - Future C - Not active future Validation Rules: 19 alphanumeric characters. The value is not editable by the user. |
| 19 | `PP.BCD.RSC` | `PpBankCode_Rsc` | TField |  | Record Status Code generated for the record by the payments hub. Possible values: L - Live U - Unapproved R - Reversed MF - Modified future Validation Rules: 1 alphanumeric character. The value is not editable by the user. |
| 20 | `PP.BCD.OldID` | `PpBankCode_Oldid` | TField |  | Used for internal purpose.Holds the ID of the current live record of store table PPT.BANKCODE. This field can hold upto 65 alphanumeric characters. No Input field |
| 21 | `PP.BCD.CurrentID` | `PpBankCode_Currentid` | TField |  | Used for internal purpose.Holds the ID of the current live record of store table PPT.BANKCODE. This field can hold upto 65 alphanumeric characters. No Input field |
| 22 | `PP.BCD.Action` | `PpBankCode_Action` | TField |  | Used for internal purpose. Value of this field determines values of fields, 'RAC' and 'RSC' Possible values: N - New M - Modified R - Reverse This field can hold upto 1 alphanumeric character and the value is not editable by the user. |
| 23 | `PP.BCD.OVERRIDE` | `PpBankCode_Override` |  |  |  |
| 24 | `PP.BCD.RECORD.STATUS` | `PpBankCode_RecordStatus` | String |  |  |
| 25 | `PP.BCD.CURR.NO` | `PpBankCode_CurrNo` | String |  |  |
| 26 | `PP.BCD.INPUTTER` | `PpBankCode_Inputter` |  |  |  |
| 27 | `PP.BCD.DATE.TIME` | `PpBankCode_DateTime` |  |  |  |
| 28 | `PP.BCD.AUTHORISER` | `PpBankCode_Authoriser` | String |  |  |
| 29 | `PP.BCD.CO.CODE` | `PpBankCode_CoCode` | String |  |  |
| 30 | `PP.BCD.DEPT.CODE` | `PpBankCode_DeptCode` | String |  |  |
| 31 | `PP.BCD.AUDITOR.CODE` | `PpBankCode_AuditorCode` | String |  |  |
| 32 | `PP.BCD.AUDIT.DATE.TIME` | `PpBankCode_AuditDateTime` | String |  |  |
