# SP.NET.SETTLEMENT — Table Schema

> Source: `INSERTS/I_F.SP.NET.SETTLEMENT` in `SP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SP.NETT.SECURITY.NO` | `SpNetSettlement_SecurityNo` | TField |  | Field to accept Security for netting. Transactions netted should have same Security as mentioned in this field. Validation Rules: NOCHANGE Field . Valid Security Master |
| 2 | `SP.NETT.TRADE.CCY` | `SpNetSettlement_TradeCcy` | TField |  | Field to accept Trade Currency for netting. Transactions netted should have same Trade Currency as mentioned in this field. Validation Rules: NOCHANGE Field . Valid Currency Record |
| 3 | `SP.NETT.STOCK.EXCHANGE` | `SpNetSettlement_StockExchange` | TField |  | Field to accept Stock exchange for netting. Transactions netted should have same Stock exchange as mentioned in this field. Validation Rules: NOCHANGE Field . Valid Stock Exchange |
| 4 | `SP.NETT.DELIVERY.INSTR` | `SpNetSettlement_DeliveryInstr` | TField |  | Field to accept Delivery Instruction for netting. Transactions netted should have same Delivery Instruction as mentioned in this field. Validation Rules: NOCHANGE Field |
| 5 | `SP.NETT.BROKER.NO` | `SpNetSettlement_BrokerNo` | TField |  | Field to accept Broker for netting. Transactions netted should have same Broker as mentioned in this field. Validation Rules: NOCHANGE Field . Valid record from CUSTOMER.SECURITY . Cannot be Synthetic Counterparties |
| 6 | `SP.NETT.DEPOSITORY` | `SpNetSettlement_Depository` | TField |  | Field to accept Depository for netting. Transactions netted should have same Depository as mentioned in this field. Validation Rules: NOCHANGE Field . Valid DEPOSITORY from CUSTOMER.SECURITY |
| 7 | `SP.NETT.SUB.ACCOUNT` | `SpNetSettlement_SubAccount` | TField |  | Field to accept Subaccount for netting. Transactions netted should have same Subaccount as mentioned in this field. Validation Rules: NOCHANGE Field . Valid Sub account for the associated depository |
| 8 | `SP.NETT.NEW.TXN.REF` | `SpNetSettlement_NewTxnRef` |  |  |  |
| 9 | `SP.NETT.TXN.REF` | `SpNetSettlement_TxnRef` |  |  |  |
| 10 | `SP.NETT.TXN.TRADE.DATE` | `SpNetSettlement_TxnTradeDate` |  |  |  |
| 11 | `SP.NETT.TXN.VALUE.DATE` | `SpNetSettlement_TxnValueDate` |  |  |  |
| 12 | `SP.NETT.TXN.TRANS.CODE` | `SpNetSettlement_TxnTransCode` |  |  |  |
| 13 | `SP.NETT.TXN.NOMINAL` | `SpNetSettlement_TxnNominal` |  |  |  |
| 14 | `SP.NETT.TXN.PRICE` | `SpNetSettlement_TxnPrice` |  |  |  |
| 15 | `SP.NETT.TXN.DEAL.AMT` | `SpNetSettlement_TxnDealAmt` |  |  |  |
| 16 | `SP.NETT.TXN.SETT.AMT` | `SpNetSettlement_TxnSettAmt` |  |  |  |
| 17 | `SP.NETT.CANC.DELIVERY.REF` | `SpNetSettlement_CancDeliveryRef` |  |  |  |
| 18 | `SP.NETT.MV.RESERVED01` | `SpNetSettlement_MvReserved01` |  |  |  |
| 19 | `SP.NETT.MV.RESERVED02` | `SpNetSettlement_MvReserved02` |  |  |  |
| 20 | `SP.NETT.MV.RESERVED03` | `SpNetSettlement_MvReserved03` |  |  |  |
| 21 | `SP.NETT.MV.RESERVED04` | `SpNetSettlement_MvReserved04` |  |  |  |
| 22 | `SP.NETT.MV.RESERVED05` | `SpNetSettlement_MvReserved05` |  |  |  |
| 23 | `SP.NETT.RECONCILIATION.ID` | `SpNetSettlement_ReconciliationId` | TField |  | ID of SP.RECONCILIATION updated for current netting record. Validation Rules: NOINPUT Field |
| 24 | `SP.NETT.NET.NOMINAL` | `SpNetSettlement_NetNominal` | TField |  | Sum of TXN.NOMINAL considering Customer Transaction code is updated here . Same is defaulted to field : NOMINAL in underlying SP.RECONCILIATION Validation Rules: NOINPUT Field |
| 25 | `SP.NETT.NET.TRANS.IND` | `SpNetSettlement_NetTransInd` | TField |  | If SUM of TXN.NOMINAL is Negative , then defaulted with SELL . If SUM of TXN.NOMINAL is Positive, then defaulted with BUYI . Otherwise, will be blank . For Example.If TXN.NOMINAL for Trade A , Trade B is updated as 30 , 40 resp and TRANS.CODE for Trade A , Trade B is Credit and Debit , then NET.NOMINAL is updated with 10 and NET.TRANS.IND with SELL |
| 26 | `SP.NETT.NET.PRICE` | `SpNetSettlement_NetPrice` | TField |  | Price is defaulted based on NET.DEAL.AMOUNT and NET.NOMINAL . Same is defaulted to field : PRICE in underlying SP.RECONCILIATION |
| 27 | `SP.NETT.NET.DEAL.AMT` | `SpNetSettlement_NetDealAmt` | TField |  | Sum of TXN.DEAL.AMT considering Customer Transaction code is defaulted . Same is defaulted to field : GROSS.AMOUNT in underlying SP.RECONCILIATION |
| 28 | `SP.NETT.NET.SETT.AMT` | `SpNetSettlement_NetSettAmt` | TField |  | Sum of TXN.SETT.AMT considering Customer Transaction code is defaulted . Same is defaulted to field : NET.AMOUNT in underlying SP.RECONCILIATION |
| 29 | `SP.NETT.NET.TRADE.DATE` | `SpNetSettlement_NetTradeDate` | TField |  | Field to input Trade Date for the netted record. System defaults with Latest Trade Date among Netted transactions.Same is defaulted to field : NEW.TRADE.DATE in underlying SP.RECONCILIATION Validation Rules: Date cannot be before Latest Trade Date among Netted Transactions Date cannot be forward dated |
| 30 | `SP.NETT.NET.VALUE.DATE` | `SpNetSettlement_NetValueDate` | TField |  | Field to input Value Date for the netted record.System defaults with Latest Value Date among Netted transaction.Same is defaulted to field : NEW.VALUE.DATE in underlying SP.RECONCILIATION Validation Rules: Date cannot be before Latest Value Date among Netted Transactions Date should be after NET.TRADE.DATE |
| 31 | `SP.NETT.RESERVED01` | `SpNetSettlement_Reserved01` | TField |  |  |
| 32 | `SP.NETT.RESERVED02` | `SpNetSettlement_Reserved02` | TField |  |  |
| 33 | `SP.NETT.RESERVED03` | `SpNetSettlement_Reserved03` | TField |  |  |
| 34 | `SP.NETT.RESERVED04` | `SpNetSettlement_Reserved04` | TField |  |  |
| 35 | `SP.NETT.RESERVED05` | `SpNetSettlement_Reserved05` | TField |  |  |
| 36 | `SP.NETT.LOCAL.REF` | `SpNetSettlement_LocalRef` |  |  |  |
| 37 | `SP.NETT.OVERRIDE` | `SpNetSettlement_Override` |  |  |  |
| 38 | `SP.NETT.RECORD.STATUS` | `SpNetSettlement_RecordStatus` | String |  |  |
| 39 | `SP.NETT.CURR.NO` | `SpNetSettlement_CurrNo` | String |  |  |
| 40 | `SP.NETT.INPUTTER` | `SpNetSettlement_Inputter` |  |  |  |
| 41 | `SP.NETT.DATE.TIME` | `SpNetSettlement_DateTime` |  |  |  |
| 42 | `SP.NETT.AUTHORISER` | `SpNetSettlement_Authoriser` | String |  |  |
| 43 | `SP.NETT.CO.CODE` | `SpNetSettlement_CoCode` | String |  |  |
| 44 | `SP.NETT.DEPT.CODE` | `SpNetSettlement_DeptCode` | String |  |  |
| 45 | `SP.NETT.AUDITOR.CODE` | `SpNetSettlement_AuditorCode` | String |  |  |
| 46 | `SP.NETT.AUDIT.DATE.TIME` | `SpNetSettlement_AuditDateTime` | String |  |  |
