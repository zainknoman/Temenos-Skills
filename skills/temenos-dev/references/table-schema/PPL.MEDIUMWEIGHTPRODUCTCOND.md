# PPL.MEDIUMWEIGHTPRODUCTCOND — Table Schema

> Source: `INSERTS/I_F.PPL.MEDIUMWEIGHTPRODUCTCOND` in `PP_ProductDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPMPC.MediumWeightProductID` | `PplMediumweightproductcond_Mediumweightproductid` |  |  |  |
| 2 | `PPMPC.CompanyID` | `PplMediumweightproductcond_Companyid` |  |  |  |
| 3 | `PPMPC.PaymentDirection` | `PplMediumweightproductcond_Paymentdirection` |  |  |  |
| 4 | `PPMPC.ClearingTransactionType` | `PplMediumweightproductcond_Clearingtransactiontype` |  |  |  |
| 5 | `PPMPC.SingleBatchClearing` | `PplMediumweightproductcond_Singlebatchclearing` |  |  |  |
| 6 | `PPMPC.ChargeType` | `PplMediumweightproductcond_Chargetype` |  |  |  |
| 7 | `PPMPC.Currency` | `PplMediumweightproductcond_Currency` |  |  |  |
| 8 | `PPMPC.FromAmount` | `PplMediumweightproductcond_Fromamount` |  |  |  |
| 9 | `PPMPC.ToAmount` | `PplMediumweightproductcond_Toamount` |  |  |  |
| 10 | `PPMPC.OriginatingSource` | `PplMediumweightproductcond_Originatingsource` |  |  |  |
| 11 | `PPMPC.IncomingMessageType` | `PplMediumweightproductcond_Incomingmessagetype` |  |  |  |
| 12 | `PPMPC.ClearingNatureCode` | `PplMediumweightproductcond_Clearingnaturecode` |  |  |  |
| 13 | `PPMPC.BeneficiaryPartyIBANCountry` | `PplMediumweightproductcond_Beneficiarypartyibancountry` |  |  |  |
| 14 | `PPMPC.OrderingPartyIBANCountry` | `PplMediumweightproductcond_Orderingpartyibancountry` |  |  |  |
| 15 | `PPMPC.BeneficiaryPartyIBANPresent` | `PplMediumweightproductcond_Beneficiarypartyibanpresent` |  |  |  |
| 16 | `PPMPC.OrderingPartyIBANPresent` | `PplMediumweightproductcond_Orderingpartyibanpresent` |  |  |  |
| 17 | `PPMPC.BeneficiaryInstitBICPresent` | `PplMediumweightproductcond_Beneficiaryinstitbicpresent` |  |  |  |
| 18 | `PPMPC.OrderingInstitBICPresent` | `PplMediumweightproductcond_Orderinginstitbicpresent` |  |  |  |
| 19 | `PPMPC.OrderingPartyResidency` | `PplMediumweightproductcond_Orderingpartyresidency` |  |  |  |
| 20 | `PPMPC.FinalCodeWord` | `PplMediumweightproductcond_Finalcodeword` |  |  |  |
| 21 | `PPMPC.StartDateMediumWeightProduct` | `PplMediumweightproductcond_Startdatemediumweightproduct` |  |  |  |
| 22 | `PPMPC.ClientConditionProduct` | `PplMediumweightproductcond_Clientconditionproduct` |  |  |  |
| 23 | `PPMPC.SourceIndicator` | `PplMediumweightproductcond_Sourceindicator` |  |  |  |
| 24 | `PPMPC.RoutingProduct` | `PplMediumweightproductcond_Routingproduct` |  |  |  |
| 25 | `PPMPC.ImposeRoutingFlag` | `PplMediumweightproductcond_Imposeroutingflag` |  |  |  |
| 26 | `PPMPC.FeeProduct` | `PplMediumweightproductcond_Feeproduct` |  |  |  |
| 27 | `PPMPC.PostingProduct` | `PplMediumweightproductcond_Postingproduct` |  |  |  |
| 28 | `PPMPC.FilterProduct` | `PplMediumweightproductcond_Filterproduct` |  |  |  |
| 29 | `PPMPC.LedgerProductCode` | `PplMediumweightproductcond_Ledgerproductcode` |  |  |  |
| 30 | `PPMPC.DebitBookCode` | `PplMediumweightproductcond_Debitbookcode` |  |  |  |
| 31 | `PPMPC.CreditBookCode` | `PplMediumweightproductcond_Creditbookcode` |  |  |  |
| 32 | `PPMPC.DebitChargeBookCode` | `PplMediumweightproductcond_Debitchargebookcode` |  |  |  |
| 33 | `PPMPC.CreditChargeBookCode` | `PplMediumweightproductcond_Creditchargebookcode` |  |  |  |
| 34 | `PPMPC.DebitVATBookCode` | `PplMediumweightproductcond_Debitvatbookcode` |  |  |  |
| 35 | `PPMPC.CreditVATBookCode` | `PplMediumweightproductcond_Creditvatbookcode` |  |  |  |
| 36 | `PPMPC.RegulatoryReportingIndicator` | `PplMediumweightproductcond_Regulatoryreportingindicator` |  |  |  |
| 37 | `PPMPC.NewPriority` | `PplMediumweightproductcond_Newpriority` |  |  |  |
| 38 | `PPMPC.NonSTPIndicator` | `PplMediumweightproductcond_Nonstpindicator` |  |  |  |
| 39 | `PPMPC.PSDCompliantIndicator` | `PplMediumweightproductcond_Psdcompliantindicator` |  |  |  |
| 40 | `PPMPC.ECCompliantIndicator` | `PplMediumweightproductcond_Eccompliantindicator` |  |  |  |
| 41 | `PPMPC.EndDateMediumWeightProduct` | `PplMediumweightproductcond_Enddatemediumweightproduct` |  |  |  |
| 42 | `PPMPC.RACMediumWeightProduct` | `PplMediumweightproductcond_Racmediumweightproduct` |  |  |  |
| 43 | `PPMPC.RSCMediumWeightProduct` | `PplMediumweightproductcond_Rscmediumweightproduct` |  |  |  |
| 44 | `PPMPC.EntryUserID` | `PplMediumweightproductcond_Entryuserid` |  |  |  |
| 45 | `PPMPC.EntryDateTime` | `PplMediumweightproductcond_Entrydatetime` |  |  |  |
| 46 | `PPMPC.ApproverUserID` | `PplMediumweightproductcond_Approveruserid` |  |  |  |
| 47 | `PPMPC.ApprovedDateTime` | `PplMediumweightproductcond_Approveddatetime` |  |  |  |
| 48 | `PPMPC.MWConcat` | `PplMediumweightproductcond_Mwconcat` |  |  |  |
| 49 | `PPMPC.CurrencyMarket` | `PplMediumweightproductcond_Currencymarket` |  |  |  |
