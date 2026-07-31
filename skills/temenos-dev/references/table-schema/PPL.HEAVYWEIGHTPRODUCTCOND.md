# PPL.HEAVYWEIGHTPRODUCTCOND — Table Schema

> Source: `INSERTS/I_F.PPL.HEAVYWEIGHTPRODUCTCOND` in `PP_ProductDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPHPC.HeavyWeightProductID` | `PplHeavyweightproductcond_Heavyweightproductid` |  |  |  |
| 2 | `PPHPC.CompanyID` | `PplHeavyweightproductcond_Companyid` |  |  |  |
| 3 | `PPHPC.CTRBTRIndicator` | `PplHeavyweightproductcond_Ctrbtrindicator` |  |  |  |
| 4 | `PPHPC.PaymentDirection` | `PplHeavyweightproductcond_Paymentdirection` |  |  |  |
| 5 | `PPHPC.DomesticInternational` | `PplHeavyweightproductcond_Domesticinternational` |  |  |  |
| 6 | `PPHPC.MessagePriority` | `PplHeavyweightproductcond_Messagepriority` |  |  |  |
| 7 | `PPHPC.SingleBatchClearing` | `PplHeavyweightproductcond_Singlebatchclearing` |  |  |  |
| 8 | `PPHPC.OriginatingSource` | `PplHeavyweightproductcond_Originatingsource` |  |  |  |
| 9 | `PPHPC.ReturnTrigger` | `PplHeavyweightproductcond_Returntrigger` |  |  |  |
| 10 | `PPHPC.Currency` | `PplHeavyweightproductcond_Currency` |  |  |  |
| 11 | `PPHPC.FromAmount` | `PplHeavyweightproductcond_Fromamount` |  |  |  |
| 12 | `PPHPC.ToAmount` | `PplHeavyweightproductcond_Toamount` |  |  |  |
| 13 | `PPHPC.ChargeType` | `PplHeavyweightproductcond_Chargetype` |  |  |  |
| 14 | `PPHPC.OrderingInstitutionBICPresent` | `PplHeavyweightproductcond_Orderinginstitutionbicpresent` |  |  |  |
| 15 | `PPHPC.BeneficiaryBICPresent` | `PplHeavyweightproductcond_Beneficiarybicpresent` |  |  |  |
| 16 | `PPHPC.OrderingPartyIBANPresent` | `PplHeavyweightproductcond_Orderingpartyibanpresent` |  |  |  |
| 17 | `PPHPC.BeneficiaryPartyIBANPresent` | `PplHeavyweightproductcond_Beneficiarypartyibanpresent` |  |  |  |
| 18 | `PPHPC.BeneficiaryBICRepaired` | `PplHeavyweightproductcond_Beneficiarybicrepaired` |  |  |  |
| 19 | `PPHPC.FinalCodeWord` | `PplHeavyweightproductcond_Finalcodeword` |  |  |  |
| 20 | `PPHPC.CodeWordText` | `PplHeavyweightproductcond_Codewordtext` |  |  |  |
| 21 | `PPHPC.IntraCompanyPayment` | `PplHeavyweightproductcond_Intracompanypayment` |  |  |  |
| 22 | `PPHPC.BankingPriority` | `PplHeavyweightproductcond_Bankingpriority` |  |  |  |
| 23 | `PPHPC.OriginatingDebitPartyCountry` | `PplHeavyweightproductcond_Originatingdebitpartycountry` |  |  |  |
| 24 | `PPHPC.OrderingPartyIBANCountry` | `PplHeavyweightproductcond_Orderingpartyibancountry` |  |  |  |
| 25 | `PPHPC.SenderCountry` | `PplHeavyweightproductcond_Sendercountry` |  |  |  |
| 26 | `PPHPC.OrderingPartyResidency` | `PplHeavyweightproductcond_Orderingpartyresidency` |  |  |  |
| 27 | `PPHPC.BeneficiaryCountry` | `PplHeavyweightproductcond_Beneficiarycountry` |  |  |  |
| 28 | `PPHPC.BeneficiaryPartyIBANCountry` | `PplHeavyweightproductcond_Beneficiarypartyibancountry` |  |  |  |
| 29 | `PPHPC.ReceiverCountry` | `PplHeavyweightproductcond_Receivercountry` |  |  |  |
| 30 | `PPHPC.DebitAccountType` | `PplHeavyweightproductcond_Debitaccounttype` |  |  |  |
| 31 | `PPHPC.SenderBIC` | `PplHeavyweightproductcond_Senderbic` |  |  |  |
| 32 | `PPHPC.ReceiverBIC` | `PplHeavyweightproductcond_Receiverbic` |  |  |  |
| 33 | `PPHPC.IncomingMessageType` | `PplHeavyweightproductcond_Incomingmessagetype` |  |  |  |
| 34 | `PPHPC.ValidationFlag` | `PplHeavyweightproductcond_Validationflag` |  |  |  |
| 35 | `PPHPC.StartDateHeavyWeightProduct` | `PplHeavyweightproductcond_Startdateheavyweightproduct` |  |  |  |
| 36 | `PPHPC.ClientConditionProduct` | `PplHeavyweightproductcond_Clientconditionproduct` |  |  |  |
| 37 | `PPHPC.SourceIndicator` | `PplHeavyweightproductcond_Sourceindicator` |  |  |  |
| 38 | `PPHPC.RoutingProduct` | `PplHeavyweightproductcond_Routingproduct` |  |  |  |
| 39 | `PPHPC.ImposeRoutingFlag` | `PplHeavyweightproductcond_Imposeroutingflag` |  |  |  |
| 40 | `PPHPC.FeeProduct` | `PplHeavyweightproductcond_Feeproduct` |  |  |  |
| 41 | `PPHPC.PostingProduct` | `PplHeavyweightproductcond_Postingproduct` |  |  |  |
| 42 | `PPHPC.LedgerProductCode` | `PplHeavyweightproductcond_Ledgerproductcode` |  |  |  |
| 43 | `PPHPC.DebitBookCode` | `PplHeavyweightproductcond_Debitbookcode` |  |  |  |
| 44 | `PPHPC.CreditBookCode` | `PplHeavyweightproductcond_Creditbookcode` |  |  |  |
| 45 | `PPHPC.DebitChargeBookCode` | `PplHeavyweightproductcond_Debitchargebookcode` |  |  |  |
| 46 | `PPHPC.CreditChargeBookCode` | `PplHeavyweightproductcond_Creditchargebookcode` |  |  |  |
| 47 | `PPHPC.DebitVATBookCode` | `PplHeavyweightproductcond_Debitvatbookcode` |  |  |  |
| 48 | `PPHPC.CreditVATBookCode` | `PplHeavyweightproductcond_Creditvatbookcode` |  |  |  |
| 49 | `PPHPC.RegulatoryReportingIndicator` | `PplHeavyweightproductcond_Regulatoryreportingindicator` |  |  |  |
| 50 | `PPHPC.NewPriority` | `PplHeavyweightproductcond_Newpriority` |  |  |  |
| 51 | `PPHPC.NonSTPIndicator` | `PplHeavyweightproductcond_Nonstpindicator` |  |  |  |
| 52 | `PPHPC.PSDCompliantIndicator` | `PplHeavyweightproductcond_Psdcompliantindicator` |  |  |  |
| 53 | `PPHPC.ECCompliantIndicator` | `PplHeavyweightproductcond_Eccompliantindicator` |  |  |  |
| 54 | `PPHPC.EndDateHeavyWeightProduct` | `PplHeavyweightproductcond_Enddateheavyweightproduct` |  |  |  |
| 55 | `PPHPC.RACHeavyWeightProduct` | `PplHeavyweightproductcond_Racheavyweightproduct` |  |  |  |
| 56 | `PPHPC.RSCHeavyWeightProduct` | `PplHeavyweightproductcond_Rscheavyweightproduct` |  |  |  |
| 57 | `PPHPC.EntryUserID` | `PplHeavyweightproductcond_Entryuserid` |  |  |  |
| 58 | `PPHPC.EntryDateTime` | `PplHeavyweightproductcond_Entrydatetime` |  |  |  |
| 59 | `PPHPC.ApproverUserID` | `PplHeavyweightproductcond_Approveruserid` |  |  |  |
| 60 | `PPHPC.ApprovedDateTime` | `PplHeavyweightproductcond_Approveddatetime` |  |  |  |
| 61 | `PPHPC.HWConcat` | `PplHeavyweightproductcond_Hwconcat` |  |  |  |
| 62 | `PPHPC.FilterProduct` | `PplHeavyweightproductcond_Filterproduct` |  |  |  |
| 63 | `PPHPC.ForwardEntryFlag` | `PplHeavyweightproductcond_Forwardentryflag` |  |  |  |
| 64 | `PPHPC.STPFlagForPO` | `PplHeavyweightproductcond_Stpflagforpo` |  |  |  |
| 65 | `PPHPC.CurrencyMarket` | `PplHeavyweightproductcond_Currencymarket` |  |  |  |
