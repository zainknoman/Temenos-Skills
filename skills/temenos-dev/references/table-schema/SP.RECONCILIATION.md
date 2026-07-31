# SP.RECONCILIATION — Table Schema

> Source: `INSERTS/I_F.SP.RECONCILIATION` in `SP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SP.RECN.BROKER.NO` | `SpReconciliation_BrokerNo` | TField |  | This field used is to specify the Broker whose MT515 will be aggregated (i.e. Aggregated Broker |
| 2 | `SP.RECN.SECURITY` | `SpReconciliation_Security` | TField |  | This field used is to specify the Security involved in the trade. |
| 3 | `SP.RECN.DEPOSITORY` | `SpReconciliation_Depository` | TField |  | This field used is to specify the Depository involved in the trade. |
| 4 | `SP.RECN.TRADE.CURRENCY` | `SpReconciliation_TradeCurrency` | TField |  | This field used is to specify the Currency of trade. |
| 5 | `SP.RECN.TRADE.DATE` | `SpReconciliation_TradeDate` | TField |  | This field used is to specify the Trade date. |
| 6 | `SP.RECN.VALUE.DATE` | `SpReconciliation_ValueDate` | TField |  | This field used is to specify the Value date of the trade. |
| 7 | `SP.RECN.STOCK.EXCHANGE` | `SpReconciliation_StockExchange` | TField |  | This field used is to specify the Stock exchange maintained as per swift codes. |
| 8 | `SP.RECN.TRANS.CODE` | `SpReconciliation_TransCode` | TField |  | This field used is to specify the Transaction code BUYI/SELL and is maintained as per swift guidelines. |
| 9 | `SP.RECN.DELIV.INSTR` | `SpReconciliation_DelivInstr` | TField |  | This field used is to specify the Delivery instruction APMT/FREE maintained as per swift. |
| 10 | `SP.RECN.LOCAL1` | `SpReconciliation_Local1` | TField |  | Local values to be used for RECONCILIATION. |
| 11 | `SP.RECN.LOCAL2` | `SpReconciliation_Local2` | TField |  | Local values to be used for RECONCILIATION. |
| 12 | `SP.RECN.NOMINAL` | `SpReconciliation_Nominal` | TField |  | This field will hold the consolidated Nominal of all aggregated trades. |
| 13 | `SP.RECN.PRICE` | `SpReconciliation_Price` | TField |  | This field will hold the consolidated price based on the aggregated trades. |
| 14 | `SP.RECN.GROSS.AMOUNT` | `SpReconciliation_GrossAmount` | TField |  | This field will hold the Consolidated Broker gross amount of all aggregated trades. |
| 15 | `SP.RECN.NET.AMOUNT` | `SpReconciliation_NetAmount` | TField |  | This field will hold the Consolidated Broker Net amount of all aggregated trades. |
| 16 | `SP.RECN.RECON.KEY` | `SpReconciliation_ReconKey` | TField |  | SP.RECONCILIATION.CONCAT reference and NOINPUT field. This field will be automatically updated based on thecomponents involved in aggregation. |
| 17 | `SP.RECN.CONF.REF` | `SpReconciliation_ConfRef` | TField |  | This field will hold the aggregated MT515 reference. |
| 18 | `SP.RECN.SETT.INSTR.REF` | `SpReconciliation_SettInstrRef` |  |  |  |
| 19 | `SP.RECN.SETT.STAT.REF` | `SpReconciliation_SettStatRef` | TField |  | This field will hold the aggregated MT548 reference. |
| 20 | `SP.RECN.DEPO.CONF.REF` | `SpReconciliation_DepoConfRef` | TField |  | This field will hold the aggregated MT545/MT547 reference. |
| 21 | `SP.RECN.CONF.NOMINAL` | `SpReconciliation_ConfNominal` | TField |  | This field will hold the aggregated Nominal received in MT515. |
| 22 | `SP.RECN.CONF.AMOUNT` | `SpReconciliation_ConfAmount` | TField |  | This field will hold the aggregated Amount received in MT515. |
| 23 | `SP.RECN.CONF.STATUS` | `SpReconciliation_ConfStatus` | TField |  | This field will hold the Status of Inward MT515 � Matched/Unmatched/Pending. |
| 24 | `SP.RECN.RECON.NOMINAL` | `SpReconciliation_ReconNominal` | TField |  | This field is used for manual reconciliation without MT515. |
| 25 | `SP.RECN.RECON.AMOUNT` | `SpReconciliation_ReconAmount` | TField |  | This field is used for manual reconciliation without MT515. |
| 26 | `SP.RECN.TOLERANCE.AMOUNT` | `SpReconciliation_ToleranceAmount` | TField |  | This field will hold the tolerance amount calculated using tolerance percentage setup in CUSTOMER.SECURITY recordof broker. |
| 27 | `SP.RECN.STATUS.NARR` | `SpReconciliation_StatusNarr` | TField |  | Records the reason for the rejection/reconciliation failure and any other narrative. The status could be: NOREC: No Matching record found for the group based on details in incoming message DIFFNOM: Quantity varies from the quantity in the incoming message DIFFAMT: The amount varies from the amount in the incoming message MTCHTOL:Status is matched but the amount in incoming message differs from the amount in Recon record but thedifference is within tolerance specified |
| 28 | `SP.RECN.NOM.SETTLED` | `SpReconciliation_NomSettled` | TField |  | This field will hold the Total nominal settled as a part of aggregated MT545 or MT547. |
| 29 | `SP.RECN.NOM.OUTSTAND` | `SpReconciliation_NomOutstand` | TField |  | This field will hold the aggregated nominal outstanding. |
| 30 | `SP.RECN.AMT.SETTLED` | `SpReconciliation_AmtSettled` | TField |  | This field will hold the Total amount settled as a part of aggregated MT545 or MT547. |
| 31 | `SP.RECN.AMT.OUTSTAND` | `SpReconciliation_AmtOutstand` | TField |  | This field will hold the aggregated nominal outstanding. |
| 32 | `SP.RECN.NOM.PERC.SETT.REV` | `SpReconciliation_NomPercSettRev` | TField |  | Percentage of nominal settled/reversed as a part of MT545 or MT547. |
| 33 | `SP.RECN.AMT.PERC.SETT.REV` | `SpReconciliation_AmtPercSettRec` |  |  |  |
| 34 | `SP.RECN.SETTLEMENT.STATUS` | `SpReconciliation_SettlementStatus` | TField |  | The status of settlement. Pending - Before any settlement confirmation is received Partial - After partial settlement Settled After complete settlement |
| 35 | `SP.RECN.SETT.VALUE.DATE` | `SpReconciliation_SettValueDate` | TField |  | Value date of settlement that will be updated into SC.SETTLEMENT. |
| 36 | `SP.RECN.CANCEL.TRADES` | `SpReconciliation_CancelTrades` | TField |  | This field can be used to reverse the underlying trades and aggregation records pertaining to it. Only input ofYES allowed. |
| 37 | `SP.RECN.SEQUENCE` | `SpReconciliation_Sequence` | TField |  |  |
| 38 | `SP.RECN.PARENT` | `SpReconciliation_Parent` | TField |  | Allowed value is YES. This Field is to determine whether the trade is a parent trade. |
| 39 | `SP.RECN.SETT.REFERENCE` | `SpReconciliation_SettReference` | TField |  | System updated Field . Unique Reference for each message sent from Reconciliation transaction is updated bysystem . For Example : If ID of current Reconciliation is SPRECO00335ABCDE . Sett References will be updated as R00001 00335ABCDE when delivery instruction is sent for first time , R00002 00335ABCDE when delivery instruction is sent for second time and so on.The portion in bold is maintained by system and will be based on No of delivery instructions. Validation Rules: NOINPUT Field |
| 40 | `SP.RECN.NET.TRANS.CODE` | `SpReconciliation_NetTransCode` | TField |  | Field indicates the Transaction Code based on Sum of Netted transactions nominal Sum of Netted transactions is Positive , then it will be updated as BUYI Sum of Netted transactions is Negative , then it will be updated as SELL Sum is zero, then no value will be updated in this field Validation Rules: Allowed Options - BUYI or SELL NOINPUT Field |
| 41 | `SP.RECN.LOCAL.REF` | `SpReconciliation_LocalRef` |  |  |  |
| 42 | `SP.RECN.OVERRIDE` | `SpReconciliation_Override` |  |  |  |
| 43 | `SP.RECN.RECORD.STATUS` | `SpReconciliation_RecordStatus` | String |  |  |
| 44 | `SP.RECN.CURR.NO` | `SpReconciliation_CurrNo` | String |  |  |
| 45 | `SP.RECN.INPUTTER` | `SpReconciliation_Inputter` |  |  |  |
| 46 | `SP.RECN.DATE.TIME` | `SpReconciliation_DateTime` |  |  |  |
| 47 | `SP.RECN.AUTHORISER` | `SpReconciliation_Authoriser` | String |  |  |
| 48 | `SP.RECN.CO.CODE` | `SpReconciliation_CoCode` | String |  |  |
| 49 | `SP.RECN.DEPT.CODE` | `SpReconciliation_DeptCode` | String |  |  |
| 50 | `SP.RECN.AUDITOR.CODE` | `SpReconciliation_AuditorCode` | String |  |  |
| 51 | `SP.RECN.AUDIT.DATE.TIME` | `SpReconciliation_AuditDateTime` | String |  |  |
| 52 | `SP.RECN.NET.SETTLEMENT.REF` | `SpReconciliation_NetSettlementRef` | TField |  | ID of SP.NET.SETTLEMENT that has created the current SP.RECONCILIATION record. |
| 53 | `SP.RECN.NEW.TRADE.DATE` | `SpReconciliation_NewTradeDate` | TField |  | TRADE.DATE to be sent in the depository delivery instruction from SP.NET.SETTLEMENT Validation Rules NOINPUT field |
| 54 | `SP.RECN.NEW.VALUE.DATE` | `SpReconciliation_NewValueDate` | TField |  | VALUE.DATE to be sent in the depository delivery instruction from SP.NET.SETTLEMENT Validation Rules NOINPUT field |
