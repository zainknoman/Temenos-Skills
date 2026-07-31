# PP.HEAVYWEIGHTPRODUCTCOND.PDS — Table Schema

> Source: `INSERTS/I_F.PP.HEAVYWEIGHTPRODUCTCOND.PDS` in `PP_ProductDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.HPC.CompanyID` | `PpHeavyweightproductcondPds_Companyid` |  |  |  |
| 2 | `PP.HPC.CTRBTRIndicator` | `PpHeavyweightproductcondPds_Ctrbtrindicator` |  |  |  |
| 3 | `PP.HPC.PaymentDirection` | `PpHeavyweightproductcondPds_Paymentdirection` |  |  |  |
| 4 | `PP.HPC.DomesticInternational` | `PpHeavyweightproductcondPds_Domesticinternational` |  |  |  |
| 5 | `PP.HPC.MessagePriority` | `PpHeavyweightproductcondPds_Messagepriority` |  |  |  |
| 6 | `PP.HPC.SingleBatchClearing` | `PpHeavyweightproductcondPds_Singlebatchclearing` |  |  |  |
| 7 | `PP.HPC.OriginatingSource` | `PpHeavyweightproductcondPds_Originatingsource` |  |  |  |
| 8 | `PP.HPC.ReturnTrigger` | `PpHeavyweightproductcondPds_Returntrigger` |  |  |  |
| 9 | `PP.HPC.Currency` | `PpHeavyweightproductcondPds_Currency` |  |  |  |
| 10 | `PP.HPC.ChargeType` | `PpHeavyweightproductcondPds_Chargetype` |  |  |  |
| 11 | `PP.HPC.OrderingInstitutionBICPresent` | `PpHeavyweightproductcondPds_Orderinginstitutionbicpresent` |  |  |  |
| 12 | `PP.HPC.BeneficiaryBICPresent` | `PpHeavyweightproductcondPds_Beneficiarybicpresent` |  |  |  |
| 13 | `PP.HPC.OrderingPartyIBANPresent` | `PpHeavyweightproductcondPds_Orderingpartyibanpresent` |  |  |  |
| 14 | `PP.HPC.BeneficiaryPartyIBANPresent` | `PpHeavyweightproductcondPds_Beneficiarypartyibanpresent` |  |  |  |
| 15 | `PP.HPC.BeneficiaryBICRepaired` | `PpHeavyweightproductcondPds_Beneficiarybicrepaired` |  |  |  |
| 16 | `PP.HPC.FinalCodeWord` | `PpHeavyweightproductcondPds_Finalcodeword` |  |  |  |
| 17 | `PP.HPC.CodeWordText` | `PpHeavyweightproductcondPds_Codewordtext` |  |  |  |
| 18 | `PP.HPC.IntraCompanyPayment` | `PpHeavyweightproductcondPds_Intracompanypayment` |  |  |  |
| 19 | `PP.HPC.BankingPriority` | `PpHeavyweightproductcondPds_Bankingpriority` |  |  |  |
| 20 | `PP.HPC.OriginatingDebitPartyCountry` | `PpHeavyweightproductcondPds_Originatingdebitpartycountry` |  |  |  |
| 21 | `PP.HPC.OrderingPartyIBANCountry` | `PpHeavyweightproductcondPds_Orderingpartyibancountry` |  |  |  |
| 22 | `PP.HPC.SenderCountry` | `PpHeavyweightproductcondPds_Sendercountry` |  |  |  |
| 23 | `PP.HPC.OrderingPartyResidency` | `PpHeavyweightproductcondPds_Orderingpartyresidency` |  |  |  |
| 24 | `PP.HPC.BeneficiaryCountry` | `PpHeavyweightproductcondPds_Beneficiarycountry` |  |  |  |
| 25 | `PP.HPC.BeneficiaryPartyIBANCountry` | `PpHeavyweightproductcondPds_Beneficiarypartyibancountry` |  |  |  |
| 26 | `PP.HPC.ReceiverCountry` | `PpHeavyweightproductcondPds_Receivercountry` |  |  |  |
| 27 | `PP.HPC.DebitAccountType` | `PpHeavyweightproductcondPds_Debitaccounttype` |  |  |  |
| 28 | `PP.HPC.SenderBIC` | `PpHeavyweightproductcondPds_Senderbic` |  |  |  |
| 29 | `PP.HPC.ReceiverBIC` | `PpHeavyweightproductcondPds_Receiverbic` |  |  |  |
| 30 | `PP.HPC.IncomingMessageType` | `PpHeavyweightproductcondPds_Incomingmessagetype` |  |  |  |
| 31 | `PP.HPC.ValidationFlag` | `PpHeavyweightproductcondPds_Validationflag` |  |  |  |
| 32 | `PP.HPC.StartDate` | `PpHeavyweightproductcondPds_Startdate` |  |  |  |
| 33 | `PP.HPC.EndDate` | `PpHeavyweightproductcondPds_Enddate` |  |  |  |
| 34 | `PP.HPC.FromAmount` | `PpHeavyweightproductcondPds_Fromamount` |  |  |  |
| 35 | `PP.HPC.ToAmount` | `PpHeavyweightproductcondPds_Toamount` |  |  |  |
| 36 | `PP.HPC.ClientConditionProduct` | `PpHeavyweightproductcondPds_Clientconditionproduct` |  |  |  |
| 37 | `PP.HPC.SourceIndicator` | `PpHeavyweightproductcondPds_Sourceindicator` |  |  |  |
| 38 | `PP.HPC.RoutingProduct` | `PpHeavyweightproductcondPds_Routingproduct` |  |  |  |
| 39 | `PP.HPC.ImposeRoutingFlag` | `PpHeavyweightproductcondPds_Imposeroutingflag` |  |  |  |
| 40 | `PP.HPC.FeeProduct` | `PpHeavyweightproductcondPds_Feeproduct` |  |  |  |
| 41 | `PP.HPC.PostingProduct` | `PpHeavyweightproductcondPds_Postingproduct` |  |  |  |
| 42 | `PP.HPC.LedgerProductCode` | `PpHeavyweightproductcondPds_Ledgerproductcode` |  |  |  |
| 43 | `PP.HPC.DebitBookCode` | `PpHeavyweightproductcondPds_Debitbookcode` |  |  |  |
| 44 | `PP.HPC.CreditBookCode` | `PpHeavyweightproductcondPds_Creditbookcode` |  |  |  |
| 45 | `PP.HPC.DebitChargeBookCode` | `PpHeavyweightproductcondPds_Debitchargebookcode` |  |  |  |
| 46 | `PP.HPC.CreditChargeBookCode` | `PpHeavyweightproductcondPds_Creditchargebookcode` |  |  |  |
| 47 | `PP.HPC.DebitVATBookCode` | `PpHeavyweightproductcondPds_Debitvatbookcode` |  |  |  |
| 48 | `PP.HPC.CreditVATBookCode` | `PpHeavyweightproductcondPds_Creditvatbookcode` |  |  |  |
| 49 | `PP.HPC.RegulatoryReportingIndic` | `PpHeavyweightproductcondPds_Regulatoryreportingindic` |  |  |  |
| 50 | `PP.HPC.NewPriority` | `PpHeavyweightproductcondPds_Newpriority` |  |  |  |
| 51 | `PP.HPC.NonSTPIndicator` | `PpHeavyweightproductcondPds_Nonstpindicator` |  |  |  |
| 52 | `PP.HPC.PSDCompliantIndicator` | `PpHeavyweightproductcondPds_Psdcompliantindicator` |  |  |  |
| 53 | `PP.HPC.ECCompliantIndicator` | `PpHeavyweightproductcondPds_Eccompliantindicator` |  |  |  |
| 54 | `PP.HPC.FilterProduct` | `PpHeavyweightproductcondPds_Filterproduct` |  |  |  |
| 55 | `PP.HPC.ForwardEntryFlag` | `PpHeavyweightproductcondPds_Forwardentryflag` |  |  |  |
| 56 | `PP.HPC.STPFlagForPO` | `PpHeavyweightproductcondPds_Stpflagforpo` |  |  |  |
| 57 | `PP.HPC.CurrencyMarket` | `PpHeavyweightproductcondPds_Currencymarket` |  |  |  |
| 58 | `PP.HPC.DuplicateType` | `PpHeavyweightproductcondPds_Duplicatetype` |  |  |  |
| 59 | `PP.HPC.RateFixing` | `PpHeavyweightproductcondPds_Ratefixing` |  |  |  |
| 60 | `PP.HPC.TxnStopMapRule` | `PpHeavyweightproductcondPds_Txnstopmaprule` |  |  |  |
| 61 | `PP.HPC.RESERVED.2` | `PpHeavyweightproductcondPds_Reserved2` |  |  |  |
| 62 | `PP.HPC.RESERVED.1` | `PpHeavyweightproductcondPds_Reserved1` |  |  |  |
| 63 | `PP.HPC.LOCAL.REF` | `PpHeavyweightproductcondPds_LocalRef` |  |  |  |
| 64 | `PP.HPC.LinkID` | `PpHeavyweightproductcondPds_Linkid` |  |  |  |
| 65 | `PP.HPC.OVERRIDE` | `PpHeavyweightproductcondPds_Override` |  |  |  |
