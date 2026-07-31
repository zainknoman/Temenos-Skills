# CAMB.H.GARNISHMENT.FILE — Table Schema

> Source: `INSERTS/I_F.CAMB.H.GARNISHMENT.FILE` in `CABASE_AMLInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.GF.GIVEN.NAMES` | `CambHGarnishmentFile_GivenNames` | TField |  |  |
| 2 | `CAMB.GF.FAMILY.NAME` | `CambHGarnishmentFile_FamilyName` | TField |  | Field is used to store the customer's Family name.Validation: This field is used to compare with the family name field in Customer application for matching Garnishments. |
| 3 | `CAMB.GF.SHORT.NAME` | `CambHGarnishmentFile_ShortName` | TField |  | Field is used to store the customer's short name.Validation:This field is used to compare with the short name field in Customer application for matching Garnishments. |
| 4 | `CAMB.GF.BUSINESS.NAME` | `CambHGarnishmentFile_BusinessName` |  |  |  |
| 5 | `CAMB.GF.TRADE.NAME` | `CambHGarnishmentFile_TradeName` |  |  |  |
| 6 | `CAMB.GF.ALIAS.NAME` | `CambHGarnishmentFile_AliasName` |  |  |  |
| 7 | `CAMB.GF.BIRTH.DATE` | `CambHGarnishmentFile_BirthDate` | TField |  |  |
| 8 | `CAMB.GF.SIN.NO` | `CambHGarnishmentFile_SinNo` | TField |  |  |
| 9 | `CAMB.GF.ADDRESS.1` | `CambHGarnishmentFile_Address1` | TField |  | Field is used to store the customer's address.Validation: This field is used to compare with the address field in Customer application for matching Garnishments. |
| 10 | `CAMB.GF.ADDRESS.2` | `CambHGarnishmentFile_Address2` | TField |  | Field is used to store the customer's address.Validation: This field is used to compare with the Street field in Customer application for matching Garnishments. |
| 11 | `CAMB.GF.CITY` | `CambHGarnishmentFile_City` | TField |  | Field is used to store the customer's address.Validation: This field is used to compare with the city field in Customer application for matching Garnishments. |
| 12 | `CAMB.GF.STATE.PROV` | `CambHGarnishmentFile_StateProv` | TField |  | Field is used to store the customer's address.Validation: This field is used to compare with the State field in Customer application for matching Garnishments. |
| 13 | `CAMB.GF.COUNTRY` | `CambHGarnishmentFile_Country` | TField |  | Field is used to store the customer's address.Validation: This field is used to compare with the Add country ID field in Customer application for matching Garnishments. |
| 14 | `CAMB.GF.POSTAL.CODE` | `CambHGarnishmentFile_PostalCode` | TField |  | Field is used to store the customer's postal code residence.Validation: This field is used to compare with the postal code field in Customer application for matching Garnishments. |
| 15 | `CAMB.GF.EXPIRY.DATE` | `CambHGarnishmentFile_ExpiryDate` | TField |  | Field is used to store the expiry date of the garnishee record. Date on which the details of the garnishment gets invalid.Date format field.Eg 12 Dec 2018. On reaching this date, the Garnishment check for the customer will not be validated against this file. |
| 16 | `CAMB.GF.COMMENTS` | `CambHGarnishmentFile_Comments` |  |  |  |
| 17 | `CAMB.GF.CUSTOMER` | `CambHGarnishmentFile_Customer` |  |  |  |
| 18 | `CAMB.GF.VERSION.NAME` | `CambHGarnishmentFile_VersionName` | TField |  | Field to store the valid Version name to flag the granishment flag to Yes, in case CUSTOMER ID is input during Creation of granishment record.Validation: record from VERSION application |
| 19 | `CAMB.GF.CORP.NO` | `CambHGarnishmentFile_CorpNo` | TField |  | Field is used to store customer's corporation number, in case the ID customer is a Corporate. |
| 20 | `CAMB.GF.RESERVED.2` | `CambHGarnishmentFile_Reserved2` | TField |  |  |
| 21 | `CAMB.GF.RESERVED.3` | `CambHGarnishmentFile_Reserved3` | TField |  |  |
| 22 | `CAMB.GF.RESERVED.4` | `CambHGarnishmentFile_Reserved4` | TField |  |  |
| 23 | `CAMB.GF.RESERVED.5` | `CambHGarnishmentFile_Reserved5` | TField |  |  |
| 24 | `CAMB.GF.RESERVED.6` | `CambHGarnishmentFile_Reserved6` | TField |  |  |
| 25 | `CAMB.GF.RESERVED.7` | `CambHGarnishmentFile_Reserved7` | TField |  |  |
| 26 | `CAMB.GF.RESERVED.8` | `CambHGarnishmentFile_Reserved8` | TField |  |  |
| 27 | `CAMB.GF.RESERVED.9` | `CambHGarnishmentFile_Reserved9` | TField |  |  |
| 28 | `CAMB.GF.RESERVED.10` | `CambHGarnishmentFile_Reserved10` | TField |  |  |
| 29 | `CAMB.GF.LOCAL.REF` | `CambHGarnishmentFile_LocalRef` |  |  |  |
| 30 | `CAMB.GF.RECORD.STATUS` | `CambHGarnishmentFile_RecordStatus` | String |  |  |
| 31 | `CAMB.GF.CURR.NO` | `CambHGarnishmentFile_CurrNo` | String |  |  |
| 32 | `CAMB.GF.INPUTTER` | `CambHGarnishmentFile_Inputter` |  |  |  |
| 33 | `CAMB.GF.DATE.TIME` | `CambHGarnishmentFile_DateTime` |  |  |  |
| 34 | `CAMB.GF.AUTHORISER` | `CambHGarnishmentFile_Authoriser` | String |  |  |
| 35 | `CAMB.GF.CO.CODE` | `CambHGarnishmentFile_CoCode` | String |  |  |
| 36 | `CAMB.GF.DEPT.CODE` | `CambHGarnishmentFile_DeptCode` | String |  |  |
| 37 | `CAMB.GF.AUDITOR.CODE` | `CambHGarnishmentFile_AuditorCode` | String |  |  |
| 38 | `CAMB.GF.AUDIT.DATE.TIME` | `CambHGarnishmentFile_AuditDateTime` | String |  |  |
