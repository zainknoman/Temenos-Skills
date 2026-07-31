# POR.BACS — Table Schema

> Source: `INSERTS/I_F.POR.BACS` in `PP_LocalClearingBACSService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPARR.CompanyID` | `PorBacs_Companyid` |  |  |  |
| 2 | `PPARR.FTNumber` | `PorBacs_Ftnumber` |  |  |  |
| 3 | `PPARR.FileProductName` | `PorBacs_Fileproductname` |  |  |  |
| 4 | `PPARR.FileReference` | `PorBacs_Filereference` |  |  |  |
| 5 | `PPARR.FileSendersReference` | `PorBacs_Filesendersreference` |  |  |  |
| 6 | `PPARR.ProcessingDate` | `PorBacs_Processingdate` |  |  |  |
| 7 | `PPARR.CurrencyCode` | `PorBacs_Currencycode` |  |  |  |
| 8 | `PPARR.CTBeneficiarySortCode` | `PorBacs_Ctbeneficiarysortcode` |  |  |  |
| 9 | `PPARR.CTBeneficiaryAccountNumber` | `PorBacs_Ctbeneficiaryaccountnumber` |  |  |  |
| 10 | `PPARR.CTAccountType` | `PorBacs_Ctaccounttype` |  |  |  |
| 11 | `PPARR.CTTransactionCode` | `PorBacs_Cttransactioncode` |  |  |  |
| 12 | `PPARR.CTRemittersSortCode` | `PorBacs_Ctremitterssortcode` |  |  |  |
| 13 | `PPARR.CTRemittersAccountNumber` | `PorBacs_Ctremittersaccountnumber` |  |  |  |
| 14 | `PPARR.CTPostingDate` | `PorBacs_Ctpostingdate` |  |  |  |
| 15 | `PPARR.CTTransactionAmount` | `PorBacs_Cttransactionamount` |  |  |  |
| 16 | `PPARR.CTRemitterName` | `PorBacs_Ctremittername` |  |  |  |
| 17 | `PPARR.CTReferenceNumber` | `PorBacs_Ctreferencenumber` |  |  |  |
| 18 | `PPARR.CTBeneficiaryName` | `PorBacs_Ctbeneficiaryname` |  |  |  |
| 19 | `PPARR.DDDebtorSortCode` | `PorBacs_Dddebtorsortcode` |  |  |  |
| 20 | `PPARR.DDDebtorAccountNumber` | `PorBacs_Dddebtoraccountnumber` |  |  |  |
| 21 | `PPARR.DDAccountType` | `PorBacs_Ddaccounttype` |  |  |  |
| 22 | `PPARR.DDTransactionCode` | `PorBacs_Ddtransactioncode` |  |  |  |
| 23 | `PPARR.DDCreditorSortCode` | `PorBacs_Ddcreditorsortcode` |  |  |  |
| 24 | `PPARR.DDCreditorAccountNumber` | `PorBacs_Ddcreditoraccountnumber` |  |  |  |
| 25 | `PPARR.DDPostingDate` | `PorBacs_Ddpostingdate` |  |  |  |
| 26 | `PPARR.DDTransactionAmount` | `PorBacs_Ddtransactionamount` |  |  |  |
| 27 | `PPARR.DDCreditorName` | `PorBacs_Ddcreditorname` |  |  |  |
| 28 | `PPARR.DDMandateReference` | `PorBacs_Ddmandatereference` |  |  |  |
| 29 | `PPARR.DDDebtorAccountName` | `PorBacs_Dddebtoraccountname` |  |  |  |
| 30 | `PPARR.CDProcessingDate` | `PorBacs_Cdprocessingdate` |  |  |  |
| 31 | `PPARR.CDDraweeMemberSortCode` | `PorBacs_Cddraweemembersortcode` |  |  |  |
| 32 | `PPARR.CDDrawerAccountNumber` | `PorBacs_Cddraweraccountnumber` |  |  |  |
| 33 | `PPARR.CDAccountType` | `PorBacs_Cdaccounttype` |  |  |  |
| 34 | `PPARR.CDTransactionCode` | `PorBacs_Cdtransactioncode` |  |  |  |
| 35 | `PPARR.CDCollectingMemberSortCode` | `PorBacs_Cdcollectingmembersortcode` |  |  |  |
| 36 | `PPARR.CDTransactionAmount` | `PorBacs_Cdtransactionamount` |  |  |  |
| 37 | `PPARR.CDReferenceNumber` | `PorBacs_Cdreferencenumber` |  |  |  |
