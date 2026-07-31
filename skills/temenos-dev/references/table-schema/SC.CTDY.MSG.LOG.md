# SC.CTDY.MSG.LOG — Table Schema

> Source: `INSERTS/I_F.SC.CTDY.MSG.LOG` in `SC_STP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CTDY.LOG.MESSAGE.TYPE` | `ScCtdyMsgLog_MessageType` | TField |  | Message type from the incoming message. Mapped with value from MESSAGE.TYPE in DE.I.HEADER Validation Rules: Valid DE.MESSAGE record |
| 2 | `SC.CTDY.LOG.SENDER.ADDRESS` | `ScCtdyMsgLog_SenderAddress` | TField |  | BIC Address of Sender from the incoming message. Mapped with value from FROM.ADDRESS in DE.I.HEADER |
| 3 | `SC.CTDY.LOG.SENDER` | `ScCtdyMsgLog_Sender` | TField |  | T24 Customer reference of Sender from the incoming message. This will hold the T24 Customer ID of the Sender of the Message. Mapped with value from CUSTOMER.NO in DE.I.HEADER Validation Rules: Valid CUSTOMER record |
| 4 | `SC.CTDY.LOG.SEME.REFERENCE` | `ScCtdyMsgLog_SemeReference` | TField |  | Sender Message Reference from the incoming message. For MT540-MT543 , Mapping is done from Sequence A - GENL as 20C:SEME tag |
| 5 | `SC.CTDY.LOG.IN.DELIVERY.REF` | `ScCtdyMsgLog_InDeliveryRef` |  |  |  |
| 6 | `SC.CTDY.LOG.FUNCTION` | `ScCtdyMsgLog_Function` |  |  |  |
| 7 | `SC.CTDY.LOG.STATUS` | `ScCtdyMsgLog_Status` | TField |  | The below values are possible in this field: 1. Input: The trade or the transfer transaction is input and not authorized. 2. Hold: The trade will be created in IHLD 3. Deleted : The unauthorised trade is deleted 4. Authorised: The inputted trade is authorized either manually or automatically. 5. Cancellation Req: Authorised trade is cancelled through MT 540 to MT543 CANC message 6. Reverse: The authorized trade is manually reversed Validation Rules: Allowed values : INPUT, HOLD, DELETED, AUTHORISED, REVERSED, CANC.REQUESTED |
| 8 | `SC.CTDY.LOG.STP.FAIL.REASON` | `ScCtdyMsgLog_StpFailReason` |  |  |  |
| 9 | `SC.CTDY.LOG.LINKED.TXN` | `ScCtdyMsgLog_LinkedTxn` | TField |  | This field will hold ID of the linked SECURITY.TRANSFER generated for Transferring IN securities , which is part of Internal Transfer. |
| 10 | `SC.CTDY.LOG.SECURITY.NO` | `ScCtdyMsgLog_SecurityNo` | TField |  | ISIN in the incoming message. For MT540-MT543, mapping is done from Sequence B - TRADDET with 35B:ISIN tag. |
| 11 | `SC.CTDY.LOG.TRADE.DATE` | `ScCtdyMsgLog_TradeDate` | TField |  | Trade Date in the incoming message. For MT540-MT543, mapping is done from Sequence B - TRADDET with 98A:TRAD tag |
| 12 | `SC.CTDY.LOG.SETTLEMENT.DATE` | `ScCtdyMsgLog_SettlementDate` | TField |  | Settlement Date in the incoming message.For MT540-MT543, mapping is done from Sequence B - TRADDET with 98A:SETTtag |
| 13 | `SC.CTDY.LOG.CUSTODY.PORT.NO.1` | `ScCtdyMsgLog_CustodyPortNo1` | TField |  | Safekeeping account of the customer in message . For MT540-MT543, mapping is done from Sequence C - FIAC with97A:SAFE tag |
| 14 | `SC.CTDY.LOG.CASH.ACCOUNT.1` | `ScCtdyMsgLog_CashAccount1` | TField |  | Cash account ( in IBAN format ) of the customer in message.For MT540-MT543 , Mapping is done from Sequence E2 -CSHPRTY as 97E:CASH |
| 15 | `SC.CTDY.LOG.CUSTODY.PORT.NO.2` | `ScCtdyMsgLog_CustodyPortNo2` | TField |  | Opposite party in the transaction for Internal Transfer.Mapped with value from For MT542 , Sequence E1 - SETPRTYas 97A::BUYR |
| 16 | `SC.CTDY.LOG.BROKER.DET` | `ScCtdyMsgLog_BrokerDet` | TField |  | Broker Address in the message. Mapped with value from For MT540/MT541 , Sequence E1 - SETPRTY as 95P::SELLFor MT542/MT543 , Sequence E1 -SETPRTY as 95P::BUYR |
| 17 | `SC.CTDY.LOG.BROKER.FEE` | `ScCtdyMsgLog_BrokerFee` | TField |  | Broker fee in the message. For MT540-MT543 , mapping is done from AMT - :19A::EXEC |
| 18 | `SC.CTDY.LOG.SETPRTY.TYPE` | `ScCtdyMsgLog_SetprtyType` |  |  |  |
| 19 | `SC.CTDY.LOG.SETPRTY.IDENT.CODE` | `ScCtdyMsgLog_SetprtyIdentCode` |  |  |  |
| 20 | `SC.CTDY.LOG.NOMINAL` | `ScCtdyMsgLog_Nominal` | TField |  | Quantity of Security in message. For MT540-MT543, mapping is done from Sequence C - FIAC 36B tag |
| 21 | `SC.CTDY.LOG.DEAL.CURRENCY` | `ScCtdyMsgLog_DealCurrency` | TField |  | Currency in which price is associated in message. For MT540-MT543, mapping is done from Sequence B - TRADDET 90Btag |
| 22 | `SC.CTDY.LOG.DEAL.PRICE` | `ScCtdyMsgLog_DealPrice` | TField |  | Price in message. For MT540-MT543, mapping is done from Sequence B - TRADDET 90B tag |
| 23 | `SC.CTDY.LOG.SETTLEMENT.CCY` | `ScCtdyMsgLog_SettlementCcy` | TField |  | Currency in which Settlement amount is associated in message. For MT540-MT543, mapping is done from Sequence E3 -AMT 19A tag |
| 24 | `SC.CTDY.LOG.SETTLEMENT.AMT` | `ScCtdyMsgLog_SettlementAmt` | TField |  | Settlement amount in message. For MT540-MT543, mapping is done from Sequence E3 - AMT 19A tag |
| 25 | `SC.CTDY.LOG.SECURITY.CCY` | `ScCtdyMsgLog_SecurityCcy` | TField |  | Currency in which security number is retrieved. For MT540-MT543, mapping is done from Sequence B1 -FIA 11A tag |
| 26 | `SC.CTDY.LOG.INTEREST.AMT` | `ScCtdyMsgLog_InterestAmt` | TField |  |  |
| 27 | `SC.CTDY.LOG.HOLD.REASON` | `ScCtdyMsgLog_HoldReason` |  |  |  |
| 28 | `SC.CTDY.LOG.AMOUNT.QUAL` | `ScCtdyMsgLog_AmountQual` |  |  |  |
| 29 | `SC.CTDY.LOG.AMOUNT.VAL` | `ScCtdyMsgLog_AmountVal` |  |  |  |
| 30 | `SC.CTDY.LOG.SETPRTY.ACC` | `ScCtdyMsgLog_SetprtyAcc` |  |  |  |
| 31 | `SC.CTDY.LOG.TRANSACTION.ERR` | `ScCtdyMsgLog_TransactionErr` |  |  |  |
| 32 | `SC.CTDY.LOG.STOCK.EXCHANGE` | `ScCtdyMsgLog_StockExchange` | TField |  |  |
