# SP.AGGREGATION — Table Schema

> Source: `INSERTS/I_F.SP.AGGREGATION` in `SP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SP.AGGR.BROKER.NO` | `SpAggregation_BrokerNo` | TField |  | Broker whose MT515 will be aggregated (i.e. Aggregated Broker. Broker is valid only when the fields TRADE.AGGREGATION SETTLE.AGGREGATION in CUSTOMER.SECURITY are set to YES. |
| 2 | `SP.AGGR.SECURITY` | `SpAggregation_Security` | TField |  | This field will hold the Security involved in the SEC.TRADE. |
| 3 | `SP.AGGR.DEPOSITORY` | `SpAggregation_Depository` | TField |  | This field will hold the Depository involved in the SEC.TRADE. |
| 4 | `SP.AGGR.TRADE.CURRENCY` | `SpAggregation_TradeCurrency` | TField |  | This field will hold the trade Currency in SEC.TRADE. |
| 5 | `SP.AGGR.TRADE.DATE` | `SpAggregation_TradeDate` | TField |  | This field will hold the trade date in SEC.TRADE. |
| 6 | `SP.AGGR.VALUE.DATE` | `SpAggregation_ValueDate` | TField |  | This field will hold the value date in SEC.TRADE. |
| 7 | `SP.AGGR.STOCK.EXCHANGE` | `SpAggregation_StockExchange` | TField |  | This field will hold the Stock exchange maintained as per swift codes. |
| 8 | `SP.AGGR.TRANS.CODE` | `SpAggregation_TransCode` | TField |  | This field will hold the Transaction code BUYI or SELL and will be maintained as per swift guidelines. |
| 9 | `SP.AGGR.DELIV.INSTR` | `SpAggregation_DelivInstr` | TField |  | This field will hold the Delivery instruction APMTor FREE and will be maintained as per swift. |
| 10 | `SP.AGGR.LOCAL1` | `SpAggregation_Local1` | TField |  | This field will be updated only in case of parent child processing. For non aggregation, This field will hold unique reference that is common to parent and child transactions in order to group parent and child delivery messages under the unique reference. For aggregation, this field will hold the depository in the parent transactions to group delivery messages of child transactions by parent depository |
| 11 | `SP.AGGR.LOCAL2` | `SpAggregation_Local2` | TField |  | Reserved for future use. |
| 12 | `SP.AGGR.NOMINAL` | `SpAggregation_Nominal` | TField |  | This field will hold the Nominal of trade. |
| 13 | `SP.AGGR.PRICE` | `SpAggregation_Price` | TField |  | This field will hold the Broker price in trade. |
| 14 | `SP.AGGR.GROSS.AMOUNT` | `SpAggregation_GrossAmount` | TField |  | This field will hold the Broker gross amount. |
| 15 | `SP.AGGR.NET.AMOUNT` | `SpAggregation_NetAmount` | TField |  | This field will hold the Broker Net amount. |
| 16 | `SP.AGGR.RECON.KEY` | `SpAggregation_ReconKey` | TField |  | This field will hold the SP.RECONCILIATION reference and is used to find the reconciliation record. |
| 17 | `SP.AGGR.RECON.UPDATE` | `SpAggregation_ReconUpdate` | TField |  | This field will hold the values ADD MODIFY REMOVE If New record is created Value will be ADD If RECON.KEY is changed Value will be MODIFY If RECON.KEY is removed VALUE will be REMOVE |
| 18 | `SP.AGGR.NON.AGGR.BROKER` | `SpAggregation_NonAggrBroker` |  |  |  |
| 19 | `SP.AGGR.NON.AGGR.MT515.REF` | `SpAggregation_NonAggrMt515Ref` |  |  |  |
| 20 | `SP.AGGR.RESERVED.1` | `SpAggregation_Reserved1` |  |  |  |
| 21 | `SP.AGGR.RESERVED.2` | `SpAggregation_Reserved2` |  |  |  |
| 22 | `SP.AGGR.RESERVED.3` | `SpAggregation_Reserved3` |  |  |  |
| 23 | `SP.AGGR.RESERVED.4` | `SpAggregation_Reserved4` |  |  |  |
| 24 | `SP.AGGR.RESERVED.5` | `SpAggregation_Reserved5` |  |  |  |
| 25 | `SP.AGGR.LOCAL.REF` | `SpAggregation_LocalRef` |  |  |  |
| 26 | `SP.AGGR.OVERRIDE` | `SpAggregation_Override` |  |  |  |
| 27 | `SP.AGGR.RECORD.STATUS` | `SpAggregation_RecordStatus` | String |  |  |
| 28 | `SP.AGGR.CURR.NO` | `SpAggregation_CurrNo` | String |  |  |
| 29 | `SP.AGGR.INPUTTER` | `SpAggregation_Inputter` |  |  |  |
| 30 | `SP.AGGR.DATE.TIME` | `SpAggregation_DateTime` |  |  |  |
| 31 | `SP.AGGR.AUTHORISER` | `SpAggregation_Authoriser` | String |  |  |
| 32 | `SP.AGGR.CO.CODE` | `SpAggregation_CoCode` | String |  |  |
| 33 | `SP.AGGR.DEPT.CODE` | `SpAggregation_DeptCode` | String |  |  |
| 34 | `SP.AGGR.AUDITOR.CODE` | `SpAggregation_AuditorCode` | String |  |  |
| 35 | `SP.AGGR.AUDIT.DATE.TIME` | `SpAggregation_AuditDateTime` | String |  |  |
