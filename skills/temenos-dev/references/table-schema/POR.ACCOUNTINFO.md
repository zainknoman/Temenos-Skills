# POR.ACCOUNTINFO — Table Schema

> Source: `INSERTS/I_F.POR.ACCOUNTINFO` in `PP_DebitPartyDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPAC.CompanyID` | `PorAccountinfo_Companyid` |  |  |  |
| 2 | `PPPAC.FTNumber` | `PorAccountinfo_Ftnumber` |  |  |  |
| 3 | `PPPAC.MainOrChargeAccountType` | `PorAccountinfo_Mainorchargeaccounttype` |  |  |  |
| 4 | `PPPAC.AccountCompanyID` | `PorAccountinfo_Accountcompanyid` |  |  |  |
| 5 | `PPPAC.AccountNumber` | `PorAccountinfo_Accountnumber` |  |  |  |
| 6 | `PPPAC.AccountCurrency` | `PorAccountinfo_Accountcurrency` |  |  |  |
| 7 | `PPPAC.AccountType` | `PorAccountinfo_Accounttype` |  |  |  |
| 8 | `PPPAC.AccountStatus` | `PorAccountinfo_Accountstatus` |  |  |  |
| 9 | `PPPAC.DebitPostingRestrictionCode` | `PorAccountinfo_Debitpostingrestrictioncode` |  |  |  |
| 10 | `PPPAC.DebitPostingRestrictionDesc` | `PorAccountinfo_Debitpostingrestrictiondesc` |  |  |  |
| 11 | `PPPAC.CdtPostingRestrictionCode` | `PorAccountinfo_Cdtpostingrestrictioncode` |  |  |  |
| 12 | `PPPAC.CdtPostingRestrictionDesc` | `PorAccountinfo_Cdtpostingrestrictiondesc` |  |  |  |
| 13 | `PPPAC.CustomerID` | `PorAccountinfo_Customerid` |  |  |  |
| 14 | `PPPAC.CustomerName` | `PorAccountinfo_Customername` |  |  |  |
| 15 | `PPPAC.CustomerAddress` | `PorAccountinfo_Customeraddress` |  |  |  |
| 16 | `PPPAC.CustomerPostalCode` | `PorAccountinfo_Customerpostalcode` |  |  |  |
| 17 | `PPPAC.CustomerCountryCode` | `PorAccountinfo_Customercountrycode` |  |  |  |
| 18 | `PPPAC.CustomerResidency` | `PorAccountinfo_Customerresidency` |  |  |  |
| 19 | `PPPAC.CustomerLanguageID` | `PorAccountinfo_Customerlanguageid` |  |  |  |
| 20 | `PPPAC.BusinessLine` | `PorAccountinfo_Businessline` |  |  |  |
| 21 | `PPPAC.SectorCode` | `PorAccountinfo_Sectorcode` |  |  |  |
| 22 | `PPPAC.AccountOfficer` | `PorAccountinfo_Accountofficer` |  |  |  |
| 23 | `PPPAC.RelatedIBAN` | `PorAccountinfo_Relatediban` |  |  |  |
| 24 | `PPPAC.BookCode` | `PorAccountinfo_Bookcode` |  |  |  |
| 25 | `PPPAC.ErrorCode` | `PorAccountinfo_Errorcode` |  |  |  |
| 26 | `PPPAC.CustomerPhoneNumber` | `PorAccountinfo_Customerphonenumber` |  |  |  |
| 27 | `PPPAC.CustomerEmailID` | `PorAccountinfo_Customeremailid` |  |  |  |
| 28 | `PPPAC.IdentifierCode` | `PorAccountinfo_Identifiercode` |  |  |  |
| 29 | `PPPAC.OtherRestrictionType` | `PorAccountinfo_Otherrestrictiontype` |  |  |  |
| 30 | `PPPAC.OtherRestrictionDesc` | `PorAccountinfo_Otherrestrictiondesc` |  |  |  |
| 31 | `PPPAC.CategoryCode` | `PorAccountinfo_Categorycode` |  |  |  |
| 32 | `PPPAC.AccountValidationDate` | `PorAccountinfo_Accountvalidationdate` |  |  |  |
| 33 | `PPPAC.AccountDDASystem` | `PorAccountinfo_Accountddasystem` |  |  |  |
