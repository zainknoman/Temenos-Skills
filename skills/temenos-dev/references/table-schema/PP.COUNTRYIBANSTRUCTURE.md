# PP.COUNTRYIBANSTRUCTURE — Table Schema

> Source: `INSERTS/I_F.PP.COUNTRYIBANSTRUCTURE` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CYI.CountryIBANStructureID` | `PpCountryibanstructure_Countryibanstructureid` | TField |  | Unique Identifier, system generated |
| 2 | `PP.CYI.CompanyID` | `PpCountryibanstructure_Companyid` | TField | Yes | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: Mandatory field 3 alphanumeric characters. The value links to the field �CompanyID� in PP.COMPANY.PROPERTIES.CONCAT |
| 3 | `PP.CYI.CountryCode` | `PpCountryibanstructure_Countrycode` | TField |  | Country Code in ISO format |
| 4 | `PP.CYI.CountryName` | `PpCountryibanstructure_Countryname` | TField |  | The country name of the institution/branch as indicated in ISO 3166 |
| 5 | `PP.CYI.HomeCountryIndicator` | `PpCountryibanstructure_Homecountryindicator` | TField |  | Indicates if the country is a home country of the company. This is used for Companies that have more than one country as a local country. For example, GB covers United Kingdom, Isle of Man, Jersey etc. This plays a key role in identifying of the payment is a domestic or an international payment. Possible values Y - Home country of the company N - Not a home country of the company |
| 6 | `PP.CYI.IBANStructure` | `PpCountryibanstructure_Ibanstructure` | TField |  | Structure of the IBAN. A = Alpha value (A-Z) N = numeric value (0-9) X = Alphanumeric (A-Z + 0-9) For example, for an IBAN of NL, the IBAN structure can be stored as follows. AANNAAAANNNNNNNNNN. An NL IBAN is validated against this structure. |
| 7 | `PP.CYI.NationalClearingSystemCode` | `PpCountryibanstructure_Nationalclearingsystemcode` | TField |  | Required to derive a BIC from an IBAN |
| 8 | `PP.CYI.LocalISOCurrencyCode` | `PpCountryibanstructure_Localisocurrencycode` | TField |  | ISO currency code |
| 9 | `PP.CYI.LocalISOCurrencyName` | `PpCountryibanstructure_Localisocurrencyname` | TField |  | ISO currency name |
| 10 | `PP.CYI.IBANCountryCode` | `PpCountryibanstructure_Ibancountrycode` | TField |  | ISO country code prefix in the IBAN |
| 11 | `PP.CYI.IBANCountryCodePosition` | `PpCountryibanstructure_Ibancountrycodeposition` | TField |  | Start position of the country code in IBAN |
| 12 | `PP.CYI.IBANCountryCodeLength` | `PpCountryibanstructure_Ibancountrycodelength` | TField |  | Number of characters of the country code in the IBAN |
| 13 | `PP.CYI.IBANCheckDigitsPosition` | `PpCountryibanstructure_Ibancheckdigitsposition` | TField |  | Start position of bank identifier in the IBAN |
| 14 | `PP.CYI.IBANCheckDigitsLength` | `PpCountryibanstructure_Ibancheckdigitslength` | TField |  | Number of check digits in the IBAN |
| 15 | `PP.CYI.BankIdentifierPosition` | `PpCountryibanstructure_Bankidentifierposition` | TField |  | Start position of bank identifier in the IBAN |
| 16 | `PP.CYI.BankIdentifierLength` | `PpCountryibanstructure_Bankidentifierlength` | TField |  | Number of characters of bank identifier in the IBAN |
| 17 | `PP.CYI.BankBranchIdentifierPosition` | `PpCountryibanstructure_Bankbranchidentifierposition` | TField |  | Start position of the branch identifier in the IBAN (value is empty if the branch identifier is not applied in the country's IBAN format) |
| 18 | `PP.CYI.BankBranchIdentifierLength` | `PpCountryibanstructure_Bankbranchidentifierlength` | TField |  | Start position of the branch identifier in the IBAN (value is empty if the branch identifier is not applied in the country's IBAN format) |
| 19 | `PP.CYI.IBANNationalIDLength` | `PpCountryibanstructure_Ibannationalidlength` | TField |  | Number of significant characters of the National ID value that are used by SWIFT to populate the IBAN NATIONAL ID, and that are sufficient to derive the IBAN BIC correctly. This number can be different from (that is, smaller than) the length of the national bank/branch identifier defined in the IBAN Registry. Note that as SWIFT refines its IBAN to BIC translation algorithms, this number may change from release to release. |
| 20 | `PP.CYI.AccountNumberPosition` | `PpCountryibanstructure_Accountnumberposition` | TField |  | Start position of the account number in IBAN |
| 21 | `PP.CYI.AccountNumberlength` | `PpCountryibanstructure_Accountnumberlength` | TField |  | Number of characters of account number in IBAN |
| 22 | `PP.CYI.NationalIDLength` | `PpCountryibanstructure_Nationalidlength` | TField |  | As the IBANNationalID is not the same as the NationalID but the NationalID will be mostly part of the IBANNationalID, NationalIDLength and NationalIDPosition are added to convert the NationalID from the IBANnationaliD and for routing and settlement to find the NationalID from the IBAN. |
| 23 | `PP.CYI.NationalIDPosition` | `PpCountryibanstructure_Nationalidposition` | TField |  | Start position of the NationalID Position |
| 24 | `PP.CYI.IBANTotalLength` | `PpCountryibanstructure_Ibantotallength` | TField |  | The total number of characters of the IBAN |
| 25 | `PP.CYI.IBANMandatoryCountry` | `PpCountryibanstructure_Ibanmandatorycountry` | TField | Yes | Y � IBAN is mandatory for sending messages to this country. N � IBAN is not mandatory for sending messages to this country. |
| 26 | `PP.CYI.IBANMandatoryCountryMT103` | `PpCountryibanstructure_Ibanmandatorycountrymt103` | TField | Yes | Y � IBAN is mandatory for sending MT103+ to this country. N � IBAN is not mandatory for sending MT103+ to this country. |
| 27 | `PP.CYI.WeekendDay1` | `PpCountryibanstructure_Weekendday1` | TField |  | This field will specify the first non-working day in the week. For example, Saturday. |
| 28 | `PP.CYI.WeekendDay2` | `PpCountryibanstructure_Weekendday2` | TField |  | This field will specify the second non-working day (if any) in the week. For example, Sunday |
| 29 | `PP.CYI.OverrideThroughUpload` | `PpCountryibanstructure_Overridethroughupload` | TField |  | If this field is �N� then it implies that the data entry will never be updated by the upload process. If set to �Y� then the data can be overridden by the upload process. |
| 30 | `PP.CYI.StartDateCountryIBANStructure` | `PpCountryibanstructure_Startdatecountryibanstructure` | TField |  | Specifies the date on which the record is to be considered active by the payments hub. |
| 31 | `PP.CYI.EndDateCountryIBANStructure` | `PpCountryibanstructure_Enddatecountryibanstructure` | TField |  | Specifies the date on which the record is to be considered inactive by the payments hub. |
| 32 | `PP.CYI.AllowSpecialCharacterSet` | `PpCountryibanstructure_Allowspecialcharacterset` | TField |  | This new indicator will take the following values Y or blank. Y indicates the country supports special character set. Blank is default |
| 33 | `PP.CYI.CodePageSet` | `PpCountryibanstructure_Codepageset` | TField |  | This field will specify against which code page the special characters have to be validated The value inputted by the user in this field will be validated against the ASCII.VAL.TABLE STANDARD.SW for LATIN or STANDARD.GR for GREEK |
| 34 | `PP.CYI.RAC` | `PpCountryibanstructure_Rac` | TField |  | Record Activation Code generated for the record by the payment's hub. Possible values: N - Not active A - Active H-YYYYMMDDHHMMSSsss - History. Where: YYYY - year, MM - month, DD - day, HH - hour, MM - minutes, SS - seconds and sss - miliseconds F - Future C - Not active future Validation Rules: 19 alphanumeric characters. The value is not editable by the user. |
| 35 | `PP.CYI.RSC` | `PpCountryibanstructure_Rsc` | TField |  | Record Status Code generated for the record by the payments hub. Possible values: L - Live U - Unapproved R - Reversed MF - Modified future Validation Rules: 1 alphanumeric character. The value is not editable by the user. |
| 36 | `PP.CYI.OldID` | `PpCountryibanstructure_Oldid` | TField |  | Used for internal purpose.Holds the ID of the current live record of store table PPT.COUNTRYIBANSTRUCTURE. This field can hold upto 15 alphanumeric characters. No Input field |
| 37 | `PP.CYI.CurrentID` | `PpCountryibanstructure_Currentid` | TField |  | Used for internal purpose.Holds the ID of the current live record of store table PPT.COUNTRYIBANSTRUCTURE. This field can hold upto 65 alphanumeric characters. No Input field |
| 38 | `PP.CYI.Action` | `PpCountryibanstructure_Action` | TField |  | Used for internal purpose. Value of this field determines values of fields, 'RAC' and 'RSC' Possible values: N - New M - Modified R - Reverse This field can hold upto 1 alphanumeric character and the value is not editable by the user. |
| 39 | `PP.CYI.OVERRIDE` | `PpCountryibanstructure_Override` |  |  |  |
| 40 | `PP.CYI.RECORD.STATUS` | `PpCountryibanstructure_RecordStatus` | String |  |  |
| 41 | `PP.CYI.CURR.NO` | `PpCountryibanstructure_CurrNo` | String |  |  |
| 42 | `PP.CYI.INPUTTER` | `PpCountryibanstructure_Inputter` |  |  |  |
| 43 | `PP.CYI.DATE.TIME` | `PpCountryibanstructure_DateTime` |  |  |  |
| 44 | `PP.CYI.AUTHORISER` | `PpCountryibanstructure_Authoriser` | String |  |  |
| 45 | `PP.CYI.CO.CODE` | `PpCountryibanstructure_CoCode` | String |  |  |
| 46 | `PP.CYI.DEPT.CODE` | `PpCountryibanstructure_DeptCode` | String |  |  |
| 47 | `PP.CYI.AUDITOR.CODE` | `PpCountryibanstructure_AuditorCode` | String |  |  |
| 48 | `PP.CYI.AUDIT.DATE.TIME` | `PpCountryibanstructure_AuditDateTime` | String |  |  |
