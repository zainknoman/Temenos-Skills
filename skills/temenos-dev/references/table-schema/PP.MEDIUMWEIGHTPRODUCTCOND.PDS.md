# PP.MEDIUMWEIGHTPRODUCTCOND.PDS — Table Schema

> Source: `INSERTS/I_F.PP.MEDIUMWEIGHTPRODUCTCOND.PDS` in `PP_ProductDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.MPC.CompanyID` | `PpMediumweightproductcondPds_Companyid` |  |  |  |
| 2 | `PP.MPC.PaymentDirection` | `PpMediumweightproductcondPds_Paymentdirection` |  |  |  |
| 3 | `PP.MPC.ClearingTransactionType` | `PpMediumweightproductcondPds_Clearingtransactiontype` |  |  |  |
| 4 | `PP.MPC.SingleBatchClearing` | `PpMediumweightproductcondPds_Singlebatchclearing` |  |  |  |
| 5 | `PP.MPC.ChargeType` | `PpMediumweightproductcondPds_Chargetype` |  |  |  |
| 6 | `PP.MPC.Currency` | `PpMediumweightproductcondPds_Currency` |  |  |  |
| 7 | `PP.MPC.OriginatingSource` | `PpMediumweightproductcondPds_Originatingsource` |  |  |  |
| 8 | `PP.MPC.IncomingMessageType` | `PpMediumweightproductcondPds_Incomingmessagetype` |  |  |  |
| 9 | `PP.MPC.ClearingNatureCode` | `PpMediumweightproductcondPds_Clearingnaturecode` |  |  |  |
| 10 | `PP.MPC.BeneficiaryPartyIBANCountry` | `PpMediumweightproductcondPds_Beneficiarypartyibancountry` |  |  |  |
| 11 | `PP.MPC.OrderingPartyIBANCountry` | `PpMediumweightproductcondPds_Orderingpartyibancountry` |  |  |  |
| 12 | `PP.MPC.BeneficiaryPartyIBANPresent` | `PpMediumweightproductcondPds_Beneficiarypartyibanpresent` |  |  |  |
| 13 | `PP.MPC.OrderingPartyIBANPresent` | `PpMediumweightproductcondPds_Orderingpartyibanpresent` |  |  |  |
| 14 | `PP.MPC.BeneficiaryInstitBICPresent` | `PpMediumweightproductcondPds_Beneficiaryinstitbicpresent` |  |  |  |
| 15 | `PP.MPC.OrderingInstitBICPresent` | `PpMediumweightproductcondPds_Orderinginstitbicpresent` |  |  |  |
| 16 | `PP.MPC.OrderingPartyResidency` | `PpMediumweightproductcondPds_Orderingpartyresidency` |  |  |  |
| 17 | `PP.MPC.FinalCodeWord` | `PpMediumweightproductcondPds_Finalcodeword` |  |  |  |
| 18 | `PP.MPC.StartDate` | `PpMediumweightproductcondPds_Startdate` |  |  |  |
| 19 | `PP.MPC.EndDate` | `PpMediumweightproductcondPds_Enddate` |  |  |  |
| 20 | `PP.MPC.FromAmount` | `PpMediumweightproductcondPds_Fromamount` |  |  |  |
| 21 | `PP.MPC.ToAmount` | `PpMediumweightproductcondPds_Toamount` |  |  |  |
| 22 | `PP.MPC.ClientConditionProduct` | `PpMediumweightproductcondPds_Clientconditionproduct` |  |  |  |
| 23 | `PP.MPC.SourceIndicator` | `PpMediumweightproductcondPds_Sourceindicator` |  |  |  |
| 24 | `PP.MPC.RoutingProduct` | `PpMediumweightproductcondPds_Routingproduct` |  |  |  |
| 25 | `PP.MPC.ImposeRoutingFlag` | `PpMediumweightproductcondPds_Imposeroutingflag` |  |  |  |
| 26 | `PP.MPC.FeeProduct` | `PpMediumweightproductcondPds_Feeproduct` |  |  |  |
| 27 | `PP.MPC.PostingProduct` | `PpMediumweightproductcondPds_Postingproduct` |  |  |  |
| 28 | `PP.MPC.FilterProduct` | `PpMediumweightproductcondPds_Filterproduct` |  |  |  |
| 29 | `PP.MPC.LedgerProductCode` | `PpMediumweightproductcondPds_Ledgerproductcode` |  |  |  |
| 30 | `PP.MPC.DebitBookCode` | `PpMediumweightproductcondPds_Debitbookcode` |  |  |  |
| 31 | `PP.MPC.CreditBookCode` | `PpMediumweightproductcondPds_Creditbookcode` |  |  |  |
| 32 | `PP.MPC.DebitChargeBookCode` | `PpMediumweightproductcondPds_Debitchargebookcode` |  |  |  |
| 33 | `PP.MPC.CreditChargeBookCode` | `PpMediumweightproductcondPds_Creditchargebookcode` |  |  |  |
| 34 | `PP.MPC.DebitVATBookCode` | `PpMediumweightproductcondPds_Debitvatbookcode` |  |  |  |
| 35 | `PP.MPC.CreditVATBookCode` | `PpMediumweightproductcondPds_Creditvatbookcode` |  |  |  |
| 36 | `PP.MPC.RegulatoryReportingIndic` | `PpMediumweightproductcondPds_Regulatoryreportingindic` |  |  |  |
| 37 | `PP.MPC.NewPriority` | `PpMediumweightproductcondPds_Newpriority` |  |  |  |
| 38 | `PP.MPC.NonSTPIndicator` | `PpMediumweightproductcondPds_Nonstpindicator` |  |  |  |
| 39 | `PP.MPC.PSDCompliantIndicator` | `PpMediumweightproductcondPds_Psdcompliantindicator` |  |  |  |
| 40 | `PP.MPC.ECCompliantIndicator` | `PpMediumweightproductcondPds_Eccompliantindicator` |  |  |  |
| 41 | `PP.MPC.CurrencyMarket` | `PpMediumweightproductcondPds_Currencymarket` |  |  |  |
| 42 | `PP.MPC.SettlementType` | `PpMediumweightproductcondPds_Settlementtype` |  |  |  |
| 43 | `PP.MPC.ClearingHoliday` | `PpMediumweightproductcondPds_Clearingholiday` |  |  |  |
| 44 | `PP.MPC.DuplicateType` | `PpMediumweightproductcondPds_Duplicatetype` |  |  |  |
| 45 | `PP.MPC.DomesticInternational` | `PpMediumweightproductcondPds_Domesticinternational` |  |  |  |
| 46 | `PP.MPC.RateFixing` | `PpMediumweightproductcondPds_Ratefixing` |  |  |  |
| 47 | `PP.MPC.LOCAL.REF` | `PpMediumweightproductcondPds_LocalRef` |  |  |  |
| 48 | `PP.MPC.LinkID` | `PpMediumweightproductcondPds_Linkid` |  |  |  |
| 49 | `PP.MPC.OVERRIDE` | `PpMediumweightproductcondPds_Override` |  |  |  |
| 50 | `PP.MPC.RECORD.STATUS` | `PpMediumweightproductcondPds_RecordStatus` |  |  |  |
| 51 | `PP.MPC.CURR.NO` | `PpMediumweightproductcondPds_CurrNo` |  |  |  |
| 52 | `PP.MPC.INPUTTER` | `PpMediumweightproductcondPds_Inputter` |  |  |  |
| 53 | `PP.MPC.DATE.TIME` | `PpMediumweightproductcondPds_DateTime` |  |  |  |
| 54 | `PP.MPC.AUTHORISER` | `PpMediumweightproductcondPds_Authoriser` |  |  |  |
| 55 | `PP.MPC.CO.CODE` | `PpMediumweightproductcondPds_CoCode` |  |  |  |
| 56 | `PP.MPC.DEPT.CODE` | `PpMediumweightproductcondPds_DeptCode` |  |  |  |
| 57 | `PP.MPC.AUDITOR.CODE` | `PpMediumweightproductcondPds_AuditorCode` |  |  |  |
| 58 | `PP.MPC.AUDIT.DATE.TIME` | `PpMediumweightproductcondPds_AuditDateTime` |  |  |  |
| 59 | `PP.MPC.TxnStopMapRule` | `PpMediumweightproductcondPds_Txnstopmaprule` |  |  |  |
