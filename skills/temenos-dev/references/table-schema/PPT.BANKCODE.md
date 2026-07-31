# PPT.BANKCODE — Table Schema

> Source: `INSERTS/I_F.PPT.BANKCODE` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBCD.BankCodeID` | `PptBankcode_Bankcodeid` | TField |  | Unique Identifier, system generated |
| 2 | `PPBCD.CompanyID` | `PptBankcode_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 The value links to the field �CompanyID� in PP.COMPANY.PROPERTIES.CONCAT |
| 3 | `PPBCD.CountryCode` | `PptBankcode_Countrycode` | TField |  | Denotes the country for which the National ID is defined |
| 4 | `PPBCD.NationalID` | `PptBankcode_Nationalid` | TField |  | The National identifier of the institution/branch otherwise called NCC(National Clearing Code) |
| 5 | `PPBCD.StartDateBankCode` | `PptBankcode_Startdatebankcode` | TField |  | Specifies the date on which the record is to be considered active by the payments hub. |
| 6 | `PPBCD.BICCode` | `PptBankcode_Biccode` | TField |  | Holds the unique BIC of the institution from the BIC directory. Can be maximum of 11 characters. BIC comprises of Institution code (4 characters) Country code (2 characters) Location code (2 characters) Branch code (3 characters � XXX denotes main or head office) |
| 7 | `PPBCD.FinancialInstitutionName` | `PptBankcode_Financialinstitutionname` | TField |  | Name of the financial institution or bank |
| 8 | `PPBCD.ZIPCode` | `PptBankcode_Zipcode` | TField |  | Post code of the institution/branch. |
| 9 | `PPBCD.CityName` | `PptBankcode_Cityname` | TField |  | Name of the city where the institution/branch is located. |
| 10 | `PPBCD.CheckDigitMethod` | `PptBankcode_Checkdigitmethod` | TField |  | This is applicable only for EMZ clearing. Every BLZ has a logic for validating the account number. This field stores the method for validating that BLZ code. |
| 11 | `PPBCD.OverrideThroughUpload` | `PptBankcode_Overridethroughupload` | TField |  | Specifies whether this specific record can be overwritten when uploaded from a file. To prevent data upload to overwrite this record, set this field to 'N'. Else, set it to 'Y'. |
| 12 | `PPBCD.SourceKey` | `PptBankcode_Sourcekey` | TField |  | This attribute links to the SourceKey in BICTable. |
| 13 | `PPBCD.OriginatingSource` | `PptBankcode_Originatingsource` | TField |  | The source from which details of bank code was updated. |
| 14 | `PPBCD.IBANBIC` | `PptBankcode_Ibanbic` | TField |  | Contains the BIC-11 issued together with the IBANs for the institution�s clients. Institution code (4 characters) Country code (2 characters) Location code (2 characters) Branch code (3 characters � XXX to denote head or main office) |
| 15 | `PPBCD.IBANCountryCode` | `PptBankcode_Ibancountrycode` | TField |  | Country code in the IBAN. This follows ISO 3166-1, contains only alphabets and is 2 character long. Under certain circumstances this can be different from the country indicated in field Country Name |
| 16 | `PPBCD.IBANNationalID` | `PptBankcode_Ibannationalid` | TField |  | The National ID which is as part of the IBAN. |
| 17 | `PPBCD.EndDateBankCode` | `PptBankcode_Enddatebankcode` | TField |  | Specifies the date on which the record is to be considered inactive by the payments hub. |
| 18 | `PPBCD.RACBankCode` | `PptBankcode_Racbankcode` | TField |  | Record Activation Code generated for the record by the payment's hub. Possible values: N - Not active A - Active H - History F - Future C - Not active future |
| 19 | `PPBCD.RSCBankCode` | `PptBankcode_Rscbankcode` | TField |  | Record Status Code generated for the record by the payments hub. Possible values: L - Live U - Unapproved R - Reversed |
| 20 | `PPBCD.EntryUserID` | `PptBankcode_Entryuserid` | TField |  | User ID of the record creator |
| 21 | `PPBCD.EntryDateTime` | `PptBankcode_Entrydatetime` | TField |  | Date and Time when the record was created in DD MON YYYY HH:MM:SS.MMM format |
| 22 | `PPBCD.ApproverUserID` | `PptBankcode_Approveruserid` | TField |  | User ID of the record approver |
| 23 | `PPBCD.ApprovedDateTime` | `PptBankcode_Approveddatetime` | TField |  | Date and Time when the record was approved in DD MON 2015 HH:MM:SS.MMM format |
| 24 | `PPBCD.OfficeType` | `PptBankcode_Officetype` | TField |  |  |
| 25 | `PPBCD.GroupType` | `PptBankcode_Grouptype` | TField |  |  |
