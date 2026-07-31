# PPT.BICTABLE — Table Schema

> Source: `INSERTS/I_F.PPT.BICTABLE` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBIC.BICID` | `PptBictable_Bicid` | TField |  | Unique identifier. System generated |
| 2 | `PPBIC.CompanyID` | `PptBictable_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 The value links to the field �CompanyID� in PP.COMPANY.PROPERTIES.CONCAT |
| 3 | `PPBIC.BICCode` | `PptBictable_Biccode` | TField |  | This is the unique BIC related to the institution from the BIC Directory. � institution code (4 char) � country code (2 char) � location code (2 char) � branch code (3 char � XXX for main office) |
| 4 | `PPBIC.StartDateBICTable` | `PptBictable_Startdatebictable` | TField |  | Specifies the date on which the record is to be considered active by the payments hub. |
| 5 | `PPBIC.SourceKey` | `PptBictable_Sourcekey` | TField |  | System generated number. Not for user input. |
| 6 | `PPBIC.SubTypeIndicator` | `PptBictable_Subtypeindicator` | TField |  | Specifies the type of financial institution being defined. System updated. Not for user input Possible Values 1. SUPE 2. NOSU 3. MCFI 4. NSWB 5. NOSU 6. PSPA 7. SSPA 8. SWIF 9. BEID 10.CORP 11.MCCO 12.SMDP 13.TRCO |
| 7 | `PPBIC.FinancialInstitutionName` | `PptBictable_Financialinstitutionname` | TField |  | Financial Institution or bank name |
| 8 | `PPBIC.POBNumber` | `PptBictable_Pobnumber` | TField |  | POB number of the institution/branch. |
| 9 | `PPBIC.StreetAddress1` | `PptBictable_Streetaddress1` | TField |  | Holds the address of the financial institution/bank |
| 10 | `PPBIC.StreetAddress2` | `PptBictable_Streetaddress2` | TField |  | Holds the address of the financial institution/bank |
| 11 | `PPBIC.StreetAddress3` | `PptBictable_Streetaddress3` | TField |  | Holds the address of the financial institution/bank |
| 12 | `PPBIC.CityName` | `PptBictable_Cityname` | TField |  | City in which the financial institution/bank is located |
| 13 | `PPBIC.CPS` | `PptBictable_Cps` | TField |  | County, province, state or other administrative regions of the financial institution/bank |
| 14 | `PPBIC.ZIPCode` | `PptBictable_Zipcode` | TField |  | Zip code of the institution/branch. |
| 15 | `PPBIC.CountryName` | `PptBictable_Countryname` | TField |  | Name of the country in which the financial institution/bank is located. |
| 16 | `PPBIC.CountryCode` | `PptBictable_Countrycode` | TField |  | The country in which the financial institution/bank is located. Links to PPT.COUNTRY |
| 17 | `PPBIC.EBAReachability` | `PptBictable_Ebareachability` | TField |  | Specifies if this BIC can be reached via the EBA clearing house (Euro Banking Association). Y � Reachable by EBA N � Not reachable by EBA |
| 18 | `PPBIC.NationalID` | `PptBictable_Nationalid` | TField |  | The National identifier of the institution/branch. |
| 19 | `PPBIC.CHIPSUID` | `PptBictable_Chipsuid` | TField |  | This is the CHIPS Universal ID related to the institution |
| 20 | `PPBIC.OverrideThroughUpload` | `PptBictable_Overridethroughupload` | TField |  | If this field is �N� then it implies that the data entry will never be updated by the upload process. If set to �Y� then the data can be overridden by the upload process. |
| 21 | `PPBIC.EndDateBICTable` | `PptBictable_Enddatebictable` | TField |  | Specifies the date on which the record is to be considered inactive by the payments hub. |
| 22 | `PPBIC.RACBICTable` | `PptBictable_Racbictable` | TField |  | Record Activation Code generated for the record by the payment's hub. Possible values: N - Not active A - Active H - History F - Future C - Not active future |
| 23 | `PPBIC.RSCBICTable` | `PptBictable_Rscbictable` | TField |  | Record Status Code generated for the record by the payments hub. Possible values: L - Live U - Unapproved R - Reversed |
| 24 | `PPBIC.EntryUserID` | `PptBictable_Entryuserid` | TField |  | User ID of the record creator |
| 25 | `PPBIC.EntryDateTime` | `PptBictable_Entrydatetime` | TField |  | Date and Time when the record was created in DD MON YYYY HH:MM:SS.MMM format |
| 26 | `PPBIC.ApproverUserID` | `PptBictable_Approveruserid` | TField |  | User ID of the record approver |
| 27 | `PPBIC.ApprovedDateTime` | `PptBictable_Approveddatetime` | TField |  | Date and Time when the record was approved in DD MON 2015 HH:MM:SS.MMM format |
