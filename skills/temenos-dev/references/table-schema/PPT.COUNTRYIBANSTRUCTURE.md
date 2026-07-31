# PPT.COUNTRYIBANSTRUCTURE — Table Schema

> Source: `INSERTS/I_F.PPT.COUNTRYIBANSTRUCTURE` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCYI.CountryIBANStructureID` | `PptCountryibanstructure_Countryibanstructureid` | TField |  | Unique Identifier, system generated |
| 2 | `PPCYI.CompanyID` | `PptCountryibanstructure_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 |
| 3 | `PPCYI.CountryCode` | `PptCountryibanstructure_Countrycode` | TField |  | Country Code in ISO format |
| 4 | `PPCYI.StartDateCountryIBANStructure` | `PptCountryibanstructure_Startdatecountryibanstructure` | TField |  | Specifies the date on which the record is to be considered active by the payments hub. |
| 5 | `PPCYI.CountryName` | `PptCountryibanstructure_Countryname` | TField |  | The country name of the institution/branch as indicated in ISO 3166 |
| 6 | `PPCYI.HomeCountryIndicator` | `PptCountryibanstructure_Homecountryindicator` | TField |  | Indicates if the country is a home country of the company. This is used for Companies that have more than one country as a local country. For example, GB covers United Kingdom, Isle of Man, Jersey etc. This plays a key role in identifying of the payment is a domestic or an international payment. Possible values Y - Home country of the company N - Not a home country of the company |
| 7 | `PPCYI.IBANStructure` | `PptCountryibanstructure_Ibanstructure` | TField |  | Structure of the IBAN. A = Alpha value (A-Z) N = numeric value (0-9) X = Alphanumeric (A-Z + 0-9) For example, for an IBAN of NL, the IBAN structure can be stored as follows. AANNAAAANNNNNNNNNN. An NL IBAN is validated against this structure. |
| 8 | `PPCYI.NationalClearingSystemCode` | `PptCountryibanstructure_Nationalclearingsystemcode` | TField |  | Required to derive a BIC from an IBAN |
| 9 | `PPCYI.RACCountryIBANStructure` | `PptCountryibanstructure_Raccountryibanstructure` | TField |  | Record Activation Code generated for the record by the payment's hub. Possible values: N - Not active A - Active H - History F - Future C - Not active future |
| 10 | `PPCYI.RSCCountryIBANStructure` | `PptCountryibanstructure_Rsccountryibanstructure` | TField |  | Record Status Code generated for the record by the payments hub. Possible values: L - Live U - Unapproved R - Reversed |
| 11 | `PPCYI.EntryUserID` | `PptCountryibanstructure_Entryuserid` | TField |  | User ID of the record creator |
| 12 | `PPCYI.EntryDateTime` | `PptCountryibanstructure_Entrydatetime` | TField |  | Date and Time when the record was created in DD MON 2015 HH:MM:SS.MMM format |
| 13 | `PPCYI.ApproverUserID` | `PptCountryibanstructure_Approveruserid` | TField |  | User ID of the record approver |
| 14 | `PPCYI.ApprovedDateTime` | `PptCountryibanstructure_Approveddatetime` | TField |  | Date and Time when the record was approved in DD MON 2015 HH:MM:SS.MMM format |
| 15 | `PPCYI.LocalISOCurrencyCode` | `PptCountryibanstructure_Localisocurrencycode` | TField |  | ISO currency code |
| 16 | `PPCYI.LocalISOCurrencyName` | `PptCountryibanstructure_Localisocurrencyname` | TField |  | ISO currency name |
| 17 | `PPCYI.IBANCountryCode` | `PptCountryibanstructure_Ibancountrycode` | TField |  | ISO country code prefix in the IBAN |
| 18 | `PPCYI.IBANCountryCodePosition` | `PptCountryibanstructure_Ibancountrycodeposition` | TField |  | Start position of the country code in IBAN |
| 19 | `PPCYI.IBANCountryCodeLength` | `PptCountryibanstructure_Ibancountrycodelength` | TField |  | Number of characters of the country code in the IBAN |
| 20 | `PPCYI.IBANCheckDigitsPosition` | `PptCountryibanstructure_Ibancheckdigitsposition` | TField |  | Start position of bank identifier in the IBAN |
| 21 | `PPCYI.IBANCheckDigitsLength` | `PptCountryibanstructure_Ibancheckdigitslength` | TField |  | Number of check digits in the IBAN |
| 22 | `PPCYI.BankIdentifierPosition` | `PptCountryibanstructure_Bankidentifierposition` | TField |  | Start position of bank identifier in the IBAN |
| 23 | `PPCYI.BankIdentifierLength` | `PptCountryibanstructure_Bankidentifierlength` | TField |  | Number of characters of bank identifier in the IBAN |
| 24 | `PPCYI.BankBranchIdentifierPosition` | `PptCountryibanstructure_Bankbranchidentifierposition` | TField |  | Start position of the branch identifier in the IBAN (value is empty if the branch identifier is not applied in the country's IBAN format) |
| 25 | `PPCYI.BankBranchIdentifierLength` | `PptCountryibanstructure_Bankbranchidentifierlength` | TField |  | Start position of the branch identifier in the IBAN (value is empty if the branch identifier is not applied in the country's IBAN format) |
| 26 | `PPCYI.IBANNationalIDLength` | `PptCountryibanstructure_Ibannationalidlength` | TField |  | Number of significant characters of the National ID value that are used by SWIFT to populate the IBAN NATIONAL ID, and that are sufficient to derive the IBAN BIC correctly. This number can be different from (that is, smaller than) the length of the national bank/branch identifier defined in the IBAN Registry. Note that as SWIFT refines its IBAN to BIC translation algorithms, this number may change from release to release. |
| 27 | `PPCYI.AccountNumberPosition` | `PptCountryibanstructure_Accountnumberposition` | TField |  | Start position of the account number in IBAN |
| 28 | `PPCYI.AccountNumberlength` | `PptCountryibanstructure_Accountnumberlength` | TField |  | Number of characters of account number in IBAN |
| 29 | `PPCYI.NationalIDLength` | `PptCountryibanstructure_Nationalidlength` | TField |  | As the IBANNationalID is not the same as the NationalID but the NationalID will be mostly part of the IBANNationalID, NationalIDLength and NationalIDPosition are added to convert the NationalID from the IBANnationaliD and for routing and settlement to find the NationalID from the IBAN. |
| 30 | `PPCYI.NationalIDPosition` | `PptCountryibanstructure_Nationalidposition` | TField |  | Start position of the NationalID Position |
| 31 | `PPCYI.IBANTotalLength` | `PptCountryibanstructure_Ibantotallength` | TField |  | The total number of characters of the IBAN |
| 32 | `PPCYI.IBANMandatoryCountry` | `PptCountryibanstructure_Ibanmandatorycountry` | TField | Yes | Y � IBAN is mandatory for sending messages to this country. N � IBAN is not mandatory for sending messages to this country. |
| 33 | `PPCYI.IBANMandatoryCountryMT103` | `PptCountryibanstructure_Ibanmandatorycountrymt103` | TField | Yes | Y � IBAN is mandatory for sending MT103+ to this country. N � IBAN is not mandatory for sending MT103+ to this country. |
| 34 | `PPCYI.WeekendDay1` | `PptCountryibanstructure_Weekendday1` | TField |  | This field will specify the first non-working day in the week. For example,Saturday. |
| 35 | `PPCYI.WeekendDay2` | `PptCountryibanstructure_Weekendday2` | TField |  | This field will specify the second non-working day (if any) in the week. For example, Sunday |
| 36 | `PPCYI.OverrideThroughUpload` | `PptCountryibanstructure_Overridethroughupload` | TField |  | If this field is �N� then it implies that the data entry will never be updated by the upload process. If set to �Y� then the data can be overridden by the upload process |
| 37 | `PPCYI.EndDateCountryIBANStructure` | `PptCountryibanstructure_Enddatecountryibanstructure` | TField |  | Specifies the date on which the record is to be considered inactive by the payments hub. |
| 38 | `PPCYI.AllowSpecialCharacterSet` | `PptCountryibanstructure_Allowspecialcharacterset` | TField |  | This new indicator will take the following values: Y or blank. �Y� indicates the country supports special character set. Blank is default |
| 39 | `PPCYI.CodePageSet` | `PptCountryibanstructure_Codepageset` | TField |  | This field will specify against which code page the special characters have to be validated The value inputted by the user in this field will be validated against the ASCII.VAL.TABLE STANDARD.SW for LATIN or STANDARD.GR for GREEK |
