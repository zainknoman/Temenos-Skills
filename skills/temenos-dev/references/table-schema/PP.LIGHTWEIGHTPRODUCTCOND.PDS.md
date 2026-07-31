# PP.LIGHTWEIGHTPRODUCTCOND.PDS — Table Schema

> Source: `INSERTS/I_F.PP.LIGHTWEIGHTPRODUCTCOND.PDS` in `PP_ProductDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.LPC.CompanyID` | `PpLightweightproductcondPds_Companyid` |  |  |  |
| 2 | `PP.LPC.OriginatingSource` | `PpLightweightproductcondPds_Originatingsource` |  |  |  |
| 3 | `PP.LPC.MessageType` | `PpLightweightproductcondPds_Messagetype` |  |  |  |
| 4 | `PP.LPC.ClearingNatureCode` | `PpLightweightproductcondPds_Clearingnaturecode` |  |  |  |
| 5 | `PP.LPC.SettlementIndicator` | `PpLightweightproductcondPds_Settlementindicator` |  |  |  |
| 6 | `PP.LPC.StartDate` | `PpLightweightproductcondPds_Startdate` |  |  |  |
| 7 | `PP.LPC.EndDate` | `PpLightweightproductcondPds_Enddate` |  |  |  |
| 8 | `PP.LPC.ClientConditionProduct` | `PpLightweightproductcondPds_Clientconditionproduct` |  |  |  |
| 9 | `PP.LPC.SourceProduct` | `PpLightweightproductcondPds_Sourceproduct` |  |  |  |
| 10 | `PP.LPC.RoutingProduct` | `PpLightweightproductcondPds_Routingproduct` |  |  |  |
| 11 | `PP.LPC.ImposeRoutingFlag` | `PpLightweightproductcondPds_Imposeroutingflag` |  |  |  |
| 12 | `PP.LPC.FeeProduct` | `PpLightweightproductcondPds_Feeproduct` |  |  |  |
| 13 | `PP.LPC.PostingProduct` | `PpLightweightproductcondPds_Postingproduct` |  |  |  |
| 14 | `PP.LPC.LedgerProductCode` | `PpLightweightproductcondPds_Ledgerproductcode` |  |  |  |
| 15 | `PP.LPC.DebitBookCode` | `PpLightweightproductcondPds_Debitbookcode` |  |  |  |
| 16 | `PP.LPC.CreditBookCode` | `PpLightweightproductcondPds_Creditbookcode` |  |  |  |
| 17 | `PP.LPC.DebitChargeBookCode` | `PpLightweightproductcondPds_Debitchargebookcode` |  |  |  |
| 18 | `PP.LPC.CreditChargeBookCode` | `PpLightweightproductcondPds_Creditchargebookcode` |  |  |  |
| 19 | `PP.LPC.DebitVATBookCode` | `PpLightweightproductcondPds_Debitvatbookcode` |  |  |  |
| 20 | `PP.LPC.CreditVATBookCode` | `PpLightweightproductcondPds_Creditvatbookcode` |  |  |  |
| 21 | `PP.LPC.RegulatoryReportingIndicator` | `PpLightweightproductcondPds_Regulatoryreportingindicator` |  |  |  |
| 22 | `PP.LPC.NonSTPIndicator` | `PpLightweightproductcondPds_Nonstpindicator` |  |  |  |
| 23 | `PP.LPC.PSDCompliantIndicator` | `PpLightweightproductcondPds_Psdcompliantindicator` |  |  |  |
| 24 | `PP.LPC.ECCompliantIndicator` | `PpLightweightproductcondPds_Eccompliantindicator` |  |  |  |
| 25 | `PP.LPC.FilterProduct` | `PpLightweightproductcondPds_Filterproduct` |  |  |  |
| 26 | `PP.LPC.ForwardEntryFlag` | `PpLightweightproductcondPds_Forwardentryflag` |  |  |  |
| 27 | `PP.LPC.STPFlagForPO` | `PpLightweightproductcondPds_Stpflagforpo` |  |  |  |
| 28 | `PP.LPC.ClearingTransactionType` | `PpLightweightproductcondPds_Clearingtransactiontype` |  |  |  |
| 29 | `PP.LPC.CurrencyMarket` | `PpLightweightproductcondPds_Currencymarket` |  |  |  |
| 30 | `PP.LPC.SettlementType` | `PpLightweightproductcondPds_Settlementtype` |  |  |  |
| 31 | `PP.LPC.ClearingHoliday` | `PpLightweightproductcondPds_Clearingholiday` |  |  |  |
| 32 | `PP.LPC.DomesticInternational` | `PpLightweightproductcondPds_Domesticinternational` |  |  |  |
| 33 | `PP.LPC.DuplicateType` | `PpLightweightproductcondPds_Duplicatetype` |  |  |  |
| 34 | `PP.LPC.RateFixing` | `PpLightweightproductcondPds_Ratefixing` |  |  |  |
| 35 | `PP.LPC.LOCAL.REF` | `PpLightweightproductcondPds_LocalRef` |  |  |  |
| 36 | `PP.LPC.LinkID` | `PpLightweightproductcondPds_Linkid` |  |  |  |
| 37 | `PP.LPC.OVERRIDE` | `PpLightweightproductcondPds_Override` |  |  |  |
| 38 | `PP.LPC.RECORD.STATUS` | `PpLightweightproductcondPds_RecordStatus` |  |  |  |
| 39 | `PP.LPC.CURR.NO` | `PpLightweightproductcondPds_CurrNo` |  |  |  |
| 40 | `PP.LPC.INPUTTER` | `PpLightweightproductcondPds_Inputter` |  |  |  |
| 41 | `PP.LPC.DATE.TIME` | `PpLightweightproductcondPds_DateTime` |  |  |  |
| 42 | `PP.LPC.AUTHORISER` | `PpLightweightproductcondPds_Authoriser` |  |  |  |
| 43 | `PP.LPC.CO.CODE` | `PpLightweightproductcondPds_CoCode` |  |  |  |
| 44 | `PP.LPC.DEPT.CODE` | `PpLightweightproductcondPds_DeptCode` |  |  |  |
| 45 | `PP.LPC.AUDITOR.CODE` | `PpLightweightproductcondPds_AuditorCode` |  |  |  |
| 46 | `PP.LPC.AUDIT.DATE.TIME` | `PpLightweightproductcondPds_AuditDateTime` |  |  |  |
| 47 | `PP.LPC.PaymentDirection` | `PpLightweightproductcondPds_Paymentdirection` |  |  |  |
| 48 | `PP.LPC.TxnStopMapRule` | `PpLightweightproductcondPds_Txnstopmaprule` |  |  |  |
