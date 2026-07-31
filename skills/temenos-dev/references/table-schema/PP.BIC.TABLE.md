# PP.BIC.TABLE — Table Schema

> Source: `INSERTS/I_F.PP.BIC.TABLE` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.BIC.BICID` | `PpBicTable_Bicid` | TField |  | Unique identifier. System generated |
| 2 | `PP.BIC.CompanyID` | `PpBicTable_Companyid` | TField | Yes | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: Mandatory field 3 alphanumeric characters. The value links to the field �CompanyID� in PP.COMPANY.PROPERTIES.CONCAT |
| 3 | `PP.BIC.BICCode` | `PpBicTable_Biccode` | TField |  | This is the unique BIC related to the institution from the BIC Directory. � institution code (4 char) � country code (2 char) � location code (2 char) � branch code (3 char � XXX for main office) |
| 4 | `PP.BIC.StartDateBICTable` | `PpBicTable_Startdatebictable` | TField |  | Specifies the date on which the record is to be considered active by the payments hub. |
| 5 | `PP.BIC.SourceKey` | `PpBicTable_Sourcekey` | TField |  | System generated number. Not for user input. |
| 6 | `PP.BIC.SubTypeIndicator` | `PpBicTable_Subtypeindicator` | TField |  | Specifies the type of financial institution being defined. System updated. Not for user input Possible Values 1. SUPE 2. NOSU 3. MCFI 4. NSWB 5. NOSU 6. PSPA 7. SSPA 8. SWIF 9. BEID 10.CORP 11.MCCO 12.SMDP 13.TRCO |
| 7 | `PP.BIC.FinancialInstitutionName` | `PpBicTable_Financialinstitutionname` | TField |  | Financial Institution or bank name |
| 8 | `PP.BIC.POBNumber` | `PpBicTable_Pobnumber` | TField |  | POB number of the institution/branch. |
| 9 | `PP.BIC.StreetAddress1` | `PpBicTable_Streetaddress1` | TField |  | Holds the address of the financial institution/bank |
| 10 | `PP.BIC.StreetAddress2` | `PpBicTable_Streetaddress2` | TField |  | Holds the address of the financial institution/bank |
| 11 | `PP.BIC.StreetAddress3` | `PpBicTable_Streetaddress3` | TField |  | Holds the address of the financial institution/bank |
| 12 | `PP.BIC.CityName` | `PpBicTable_Cityname` | TField |  | City in which the financial institution/bank is located |
| 13 | `PP.BIC.CPS` | `PpBicTable_Cps` | TField |  | County, province, state or other administrative regions of the financial institution/bank |
| 14 | `PP.BIC.ZIPCode` | `PpBicTable_Zipcode` | TField |  | Zip code of the institution/branch. |
| 15 | `PP.BIC.CountryName` | `PpBicTable_Countryname` | TField |  | Name of the country in which the financial institution/bank is located. |
| 16 | `PP.BIC.CountryCode` | `PpBicTable_Countrycode` | TField |  | The country in which the financial institution/bank is located. Should be a valid value in PPT.COUNTRY |
| 17 | `PP.BIC.EBAReachability` | `PpBicTable_Ebareachability` | TField |  | Specifies if this BIC can be reached via the EBA clearing house (Euro Banking Association). Y � Reachable by EBA N � Not reachable by EBA |
| 18 | `PP.BIC.NationalID` | `PpBicTable_Nationalid` | TField |  | The National identifier of the institution/branch. |
| 19 | `PP.BIC.CHIPSUID` | `PpBicTable_Chipsuid` | TField |  | This is the CHIPS Universal ID related to the institution |
| 20 | `PP.BIC.OverrideThroughUpload` | `PpBicTable_Overridethroughupload` | TField |  | If this field is �N� then it implies that the data entry will never be updated by the upload process. If set to �Y� then the data can be overridden by the upload process. |
| 21 | `PP.BIC.EndDateBICTable` | `PpBicTable_Enddatebictable` | TField |  | Specifies the date on which the record is to be considered inactive by the payments hub. |
| 22 | `PP.BIC.RAC` | `PpBicTable_Rac` | TField |  | Record Activation Code generated for the record by the payment's hub. Possible values: N - Not active A - Active H-YYYYMMDDHHMMSSsss - History. Where: YYYY - year, MM - month, DD - day, HH - hour, MM - minutes, SS - seconds and sss - miliseconds F - Future C - Not active future Validation Rules: 19 alphanumeric characters. The value is not editable by the user. |
| 23 | `PP.BIC.RSC` | `PpBicTable_Rsc` | TField |  | Record Status Code generated for the record by the payments hub. Possible values: L - Live U - Unapproved R - Reversed MF - Modified future Validation Rules: 1 alphanumeric character. The value is not editable by the user. |
| 24 | `PP.BIC.OldID` | `PpBicTable_Oldid` | TField |  | Used for internal purpose.Holds the ID of the current live record of store table PPT.BICTABLE. This field can hold upto 15 alphanumeric characters. No Input field |
| 25 | `PP.BIC.CurrentID` | `PpBicTable_Currentid` | TField |  | Used for internal purpose.Holds the ID of the current live record of store table PPT.BICTABLE. This field can hold upto 65 alphanumeric characters. No Input field |
| 26 | `PP.BIC.Action` | `PpBicTable_Action` | TField |  | Used for internal purpose. Value of this field determines values of fields, 'RAC' and 'RSC' Possible values: N - New M - Modified R - Reverse This field can hold upto 1 alphanumeric character and the value is not editable by the user. |
| 27 | `PP.BIC.OVERRIDE` | `PpBicTable_Override` |  |  |  |
| 28 | `PP.BIC.RECORD.STATUS` | `PpBicTable_RecordStatus` | String |  |  |
| 29 | `PP.BIC.CURR.NO` | `PpBicTable_CurrNo` | String |  |  |
| 30 | `PP.BIC.INPUTTER` | `PpBicTable_Inputter` |  |  |  |
| 31 | `PP.BIC.DATE.TIME` | `PpBicTable_DateTime` |  |  |  |
| 32 | `PP.BIC.AUTHORISER` | `PpBicTable_Authoriser` | String |  |  |
| 33 | `PP.BIC.CO.CODE` | `PpBicTable_CoCode` | String |  |  |
| 34 | `PP.BIC.DEPT.CODE` | `PpBicTable_DeptCode` | String |  |  |
| 35 | `PP.BIC.AUDITOR.CODE` | `PpBicTable_AuditorCode` | String |  |  |
| 36 | `PP.BIC.AUDIT.DATE.TIME` | `PpBicTable_AuditDateTime` | String |  |  |
