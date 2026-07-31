# POR.POSTADVICES — Table Schema

> Source: `INSERTS/I_F.POR.POSTADVICES` in `PP_AutoformService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPAD.PostAdvicetype` | `PorPostadvices_Postadvicetype` |  |  |  |
| 2 | `PPPAD.CompanyID` | `PorPostadvices_Companyid` |  |  |  |
| 3 | `PPPAD.ReportIdentifierCode` | `PorPostadvices_Reportidentifiercode` |  |  |  |
| 4 | `PPPAD.AccountOfficer` | `PorPostadvices_Accountofficer` |  |  |  |
| 5 | `PPPAD.OutputIdentifierCode` | `PorPostadvices_Outputidentifiercode` |  |  |  |
| 6 | `PPPAD.SystemDate` | `PorPostadvices_Systemdate` |  |  |  |
| 7 | `PPPAD.ProcessingDate` | `PorPostadvices_Processingdate` |  |  |  |
| 8 | `PPPAD.FTNumber` | `PorPostadvices_Ftnumber` |  |  |  |
| 9 | `PPPAD.CustomerID` | `PorPostadvices_Customerid` |  |  |  |
| 10 | `PPPAD.CustomerName` | `PorPostadvices_Customername` |  |  |  |
| 11 | `PPPAD.CustomerAddress` | `PorPostadvices_Customeraddress` |  |  |  |
| 12 | `PPPAD.CustomerPostalCode` | `PorPostadvices_Customerpostalcode` |  |  |  |
| 13 | `PPPAD.CustomerCountryCode` | `PorPostadvices_Customercountrycode` |  |  |  |
| 14 | `PPPAD.PaymentDirection` | `PorPostadvices_Paymentdirection` |  |  |  |
| 15 | `PPPAD.OutputChannel` | `PorPostadvices_Outputchannel` |  |  |  |
| 16 | `PPPAD.OriginatingChannel` | `PorPostadvices_Originatingchannel` |  |  |  |
| 17 | `PPPAD.CreditValueDate` | `PorPostadvices_Creditvaluedate` |  |  |  |
| 18 | `PPPAD.CreditPartyFreeLine1` | `PorPostadvices_Creditpartyfreeline1` |  |  |  |
| 19 | `PPPAD.CreditPartyFreeLine2` | `PorPostadvices_Creditpartyfreeline2` |  |  |  |
| 20 | `PPPAD.CreditPartyFreeLine3` | `PorPostadvices_Creditpartyfreeline3` |  |  |  |
| 21 | `PPPAD.CreditPartyFreeLine4` | `PorPostadvices_Creditpartyfreeline4` |  |  |  |
| 22 | `PPPAD.CreditPartyAccountLine` | `PorPostadvices_Creditpartyaccountline` |  |  |  |
| 23 | `PPPAD.DebitPartyFreeLine1` | `PorPostadvices_Debitpartyfreeline1` |  |  |  |
| 24 | `PPPAD.DebitPartyFreeLine2` | `PorPostadvices_Debitpartyfreeline2` |  |  |  |
| 25 | `PPPAD.DebitPartyFreeLine3` | `PorPostadvices_Debitpartyfreeline3` |  |  |  |
| 26 | `PPPAD.DebitPartyFreeLine4` | `PorPostadvices_Debitpartyfreeline4` |  |  |  |
| 27 | `PPPAD.DebitPartyAccountLine` | `PorPostadvices_Debitpartyaccountline` |  |  |  |
| 28 | `PPPAD.CreditPartyFreeLineBank` | `PorPostadvices_Creditpartyfreelinebank` |  |  |  |
| 29 | `PPPAD.CreditPartyIdentifierCodeBank` | `PorPostadvices_Creditpartyidentifiercodebank` |  |  |  |
| 30 | `PPPAD.CreditPartyAccountLineBank` | `PorPostadvices_Creditpartyaccountlinebank` |  |  |  |
| 31 | `PPPAD.AdditionalInfLine1` | `PorPostadvices_Additionalinfline1` |  |  |  |
| 32 | `PPPAD.AdditionalInfLine2` | `PorPostadvices_Additionalinfline2` |  |  |  |
| 33 | `PPPAD.AdditionalInfLine3` | `PorPostadvices_Additionalinfline3` |  |  |  |
| 34 | `PPPAD.AdditionalInfLine4` | `PorPostadvices_Additionalinfline4` |  |  |  |
| 35 | `PPPAD.DebitReference` | `PorPostadvices_Debitreference` |  |  |  |
| 36 | `PPPAD.TransactionReferenceIncoming` | `PorPostadvices_Transactionreferenceincoming` |  |  |  |
| 37 | `PPPAD.DDCreditorName` | `PorPostadvices_Ddcreditorname` |  |  |  |
| 38 | `PPPAD.DDCreditorAccountNumber` | `PorPostadvices_Ddcreditoraccountnumber` |  |  |  |
| 39 | `PPPAD.DDCreditorSortCode` | `PorPostadvices_Ddcreditorsortcode` |  |  |  |
| 40 | `PPPAD.ClearingNatureCodeDescription` | `PorPostadvices_Clearingnaturecodedescription` |  |  |  |
| 41 | `PPPAD.DDMandateReference` | `PorPostadvices_Ddmandatereference` |  |  |  |
| 42 | `PPPAD.TransactionCurrencyCode` | `PorPostadvices_Transactioncurrencycode` |  |  |  |
| 43 | `PPPAD.TransactionAmount` | `PorPostadvices_Transactionamount` |  |  |  |
| 44 | `PPPAD.DebitExchangeRate` | `PorPostadvices_Debitexchangerate` |  |  |  |
| 45 | `PPPAD.CreditExchangeRate` | `PorPostadvices_Creditexchangerate` |  |  |  |
| 46 | `PPPAD.DebitMainAccountCurrencyCode` | `PorPostadvices_Debitmainaccountcurrencycode` |  |  |  |
| 47 | `PPPAD.DebitMainAmount` | `PorPostadvices_Debitmainamount` |  |  |  |
| 48 | `PPPAD.DebitValueDate` | `PorPostadvices_Debitvaluedate` |  |  |  |
| 49 | `PPPAD.CreditMainAccountCurrencyCode` | `PorPostadvices_Creditmainaccountcurrencycode` |  |  |  |
| 50 | `PPPAD.CreditMainAmount` | `PorPostadvices_Creditmainamount` |  |  |  |
| 51 | `PPPAD.ChargeAmountCurrency1` | `PorPostadvices_Chargeamountcurrency1` |  |  |  |
| 52 | `PPPAD.ChargeAmount1` | `PorPostadvices_Chargeamount1` |  |  |  |
| 53 | `PPPAD.FeeDescription1` | `PorPostadvices_Feedescription1` |  |  |  |
| 54 | `PPPAD.ChargeAmountCurrency2` | `PorPostadvices_Chargeamountcurrency2` |  |  |  |
| 55 | `PPPAD.ChargeAmount2` | `PorPostadvices_Chargeamount2` |  |  |  |
| 56 | `PPPAD.FeeDescription2` | `PorPostadvices_Feedescription2` |  |  |  |
| 57 | `PPPAD.ChargeAmountCurrency3` | `PorPostadvices_Chargeamountcurrency3` |  |  |  |
| 58 | `PPPAD.ChargeAmount3` | `PorPostadvices_Chargeamount3` |  |  |  |
| 59 | `PPPAD.FeeDescription3` | `PorPostadvices_Feedescription3` |  |  |  |
| 60 | `PPPAD.ChargeAmountCurrency4` | `PorPostadvices_Chargeamountcurrency4` |  |  |  |
| 61 | `PPPAD.ChargeAmount4` | `PorPostadvices_Chargeamount4` |  |  |  |
| 62 | `PPPAD.FeeDescription4` | `PorPostadvices_Feedescription4` |  |  |  |
| 63 | `PPPAD.ChargeAmountCurrency5` | `PorPostadvices_Chargeamountcurrency5` |  |  |  |
| 64 | `PPPAD.ChargeAmount5` | `PorPostadvices_Chargeamount5` |  |  |  |
| 65 | `PPPAD.FeeDescription5` | `PorPostadvices_Feedescription5` |  |  |  |
| 66 | `PPPAD.DebitChargeAccountCurrencyCode` | `PorPostadvices_Debitchargeaccountcurrencycode` |  |  |  |
| 67 | `PPPAD.DebitChargeAccount` | `PorPostadvices_Debitchargeaccount` |  |  |  |
| 68 | `PPPAD.CreditChargeAccountCcyCode` | `PorPostadvices_Creditchargeaccountccycode` |  |  |  |
| 69 | `PPPAD.CreditChargeAccount` | `PorPostadvices_Creditchargeaccount` |  |  |  |
| 70 | `PPPAD.LanguageID` | `PorPostadvices_Languageid` |  |  |  |
| 71 | `PPPAD.FinantialInstitutionName` | `PorPostadvices_Finantialinstitutionname` |  |  |  |
| 72 | `PPPAD.DebitMainAccount` | `PorPostadvices_Debitmainaccount` |  |  |  |
| 73 | `PPPAD.CreditMainAccount` | `PorPostadvices_Creditmainaccount` |  |  |  |
| 74 | `PPPAD.DebitCurrencyPair` | `PorPostadvices_Debitcurrencypair` |  |  |  |
| 75 | `PPPAD.CreditCurrencyPair` | `PorPostadvices_Creditcurrencypair` |  |  |  |
| 76 | `PPPAD.CalculateDebitAmount` | `PorPostadvices_Calculatedebitamount` |  |  |  |
| 77 | `PPPAD.CalculateCreditAmount` | `PorPostadvices_Calculatecreditamount` |  |  |  |
| 78 | `PPPAD.ShortProductDescription1` | `PorPostadvices_Shortproductdescription1` |  |  |  |
| 79 | `PPPAD.ReversalIndicator` | `PorPostadvices_Reversalindicator` |  |  |  |
