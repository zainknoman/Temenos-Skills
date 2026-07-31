# POR.POSTINGLINE — Table Schema

> Source: `INSERTS/I_F.POR.POSTINGLINE` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPLI.CompanyID` | `PorPostingline_Companyid` |  |  |  |
| 2 | `PPPLI.FTNumber` | `PorPostingline_Ftnumber` |  |  |  |
| 3 | `PPPLI.PostingLineNumber` | `PorPostingline_Postinglinenumber` |  |  |  |
| 4 | `PPPLI.ReservationKey` | `PorPostingline_Reservationkey` |  |  |  |
| 5 | `PPPLI.AccountNumberCompanyID` | `PorPostingline_Accountnumbercompanyid` |  |  |  |
| 6 | `PPPLI.AccountNumber` | `PorPostingline_Accountnumber` |  |  |  |
| 7 | `PPPLI.AccountCurrency` | `PorPostingline_Accountcurrency` |  |  |  |
| 8 | `PPPLI.PostingLineDebitCreditInd` | `PorPostingline_Postinglinedebitcreditind` |  |  |  |
| 9 | `PPPLI.PostingAmount` | `PorPostingline_Postingamount` |  |  |  |
| 10 | `PPPLI.PostingAmountCurrency` | `PorPostingline_Postingamountcurrency` |  |  |  |
| 11 | `PPPLI.PostingAmountLocalCurrency` | `PorPostingline_Postingamountlocalcurrency` |  |  |  |
| 12 | `PPPLI.LocalCurrencyCode` | `PorPostingline_Localcurrencycode` |  |  |  |
| 13 | `PPPLI.BookingDate` | `PorPostingline_Bookingdate` |  |  |  |
| 14 | `PPPLI.ValueDate` | `PorPostingline_Valuedate` |  |  |  |
| 15 | `PPPLI.ExposureDate` | `PorPostingline_Exposuredate` |  |  |  |
| 16 | `PPPLI.BookingCode` | `PorPostingline_Bookingcode` |  |  |  |
| 17 | `PPPLI.PostingTypeFlag` | `PorPostingline_Postingtypeflag` |  |  |  |
| 18 | `PPPLI.OurReference` | `PorPostingline_Ourreference` |  |  |  |
| 19 | `PPPLI.AccountOwnerReference` | `PorPostingline_Accountownerreference` |  |  |  |
| 20 | `PPPLI.SupplementaryDetails` | `PorPostingline_Supplementarydetails` |  |  |  |
| 21 | `PPPLI.DepartmentCode` | `PorPostingline_Departmentcode` |  |  |  |
| 22 | `PPPLI.CurrencyMarket` | `PorPostingline_Currencymarket` |  |  |  |
| 23 | `PPPLI.DealerDesk` | `PorPostingline_Dealerdesk` |  |  |  |
| 24 | `PPPLI.ClientID` | `PorPostingline_Clientid` |  |  |  |
| 25 | `PPPLI.BookCode` | `PorPostingline_Bookcode` |  |  |  |
| 26 | `PPPLI.SWIFTTransactionTypeCode` | `PorPostingline_Swifttransactiontypecode` |  |  |  |
| 27 | `PPPLI.ReversalIndicator` | `PorPostingline_Reversalindicator` |  |  |  |
