# SC.ORD.INSTR.LOG — Table Schema

> Source: `INSERTS/I_F.SC.ORD.INSTR.LOG` in `SC_SctOrderCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.OIL.CUST.OUT.REFERENCE` | `ScOrdInstrLog_CustOutReference` | TField |  | This field holds the OrderReference from incoming messages (SETR.004 and SETR.010) and the same reference is used in all the outgoing messages to the customer (Say, SETR.006/SETR.012/ SETR.016 and SETR.017) |
| 2 | `SC.OIL.CUSTOMER.ID` | `ScOrdInstrLog_CustomerId` | TField |  | This field holds the Customer Id identified by the system |
| 3 | `SC.OIL.ORDER.TYPE` | `ScOrdInstrLog_OrderType` | TField |  | This fields holds the type of Order |
| 4 | `SC.OIL.ORDER.QUANTITY` | `ScOrdInstrLog_OrderQuantity` | TField |  | This fields holds the quantity of Order |
| 5 | `SC.OIL.SECURITY.NO` | `ScOrdInstrLog_SecurityNo` | TField |  | This fields holds the SecurityNo identified by the System using ISIN from incoming message |
| 6 | `SC.OIL.CURRENCY` | `ScOrdInstrLog_Currency` | TField |  | This fields holds trade currency of the order |
| 7 | `SC.OIL.MSG.TYPE` | `ScOrdInstrLog_MsgType` |  |  |  |
| 8 | `SC.OIL.MSG.IN.OUT` | `ScOrdInstrLog_MsgInOut` |  |  |  |
| 9 | `SC.OIL.MSG.FUNC` | `ScOrdInstrLog_MsgFunc` |  |  |  |
| 10 | `SC.OIL.MSG.QTY` | `ScOrdInstrLog_MsgQty` |  |  |  |
| 11 | `SC.OIL.MSG.PRICE` | `ScOrdInstrLog_MsgPrice` |  |  |  |
| 12 | `SC.OIL.ORD.STATUS.OUT` | `ScOrdInstrLog_OrdStatusOut` |  |  |  |
| 13 | `SC.OIL.PROCESS.STATUS` | `ScOrdInstrLog_ProcessStatus` |  |  |  |
| 14 | `SC.OIL.ERR.REASON` | `ScOrdInstrLog_ErrReason` |  |  |  |
| 15 | `SC.OIL.REASON.NARRATIVE` | `ScOrdInstrLog_ReasonNarrative` |  |  |  |
| 16 | `SC.OIL.DELIVERY.REF` | `ScOrdInstrLog_DeliveryRef` |  |  |  |
| 17 | `SC.OIL.REPLACED.ORDER.ID` | `ScOrdInstrLog_ReplacedOrderId` | TField |  |  |
| 18 | `SC.OIL.LOCAL.REF` | `ScOrdInstrLog_LocalRef` |  |  |  |
| 19 | `SC.OIL.OVERRIDE` | `ScOrdInstrLog_Override` |  |  |  |
| 20 | `SC.OIL.RECORD.STATUS` | `ScOrdInstrLog_RecordStatus` | String |  |  |
| 21 | `SC.OIL.CURR.NO` | `ScOrdInstrLog_CurrNo` | String |  |  |
| 22 | `SC.OIL.INPUTTER` | `ScOrdInstrLog_Inputter` |  |  |  |
| 23 | `SC.OIL.DATE.TIME` | `ScOrdInstrLog_DateTime` |  |  |  |
| 24 | `SC.OIL.AUTHORISER` | `ScOrdInstrLog_Authoriser` | String |  |  |
| 25 | `SC.OIL.CO.CODE` | `ScOrdInstrLog_CoCode` | String |  |  |
| 26 | `SC.OIL.DEPT.CODE` | `ScOrdInstrLog_DeptCode` | String |  |  |
| 27 | `SC.OIL.AUDITOR.CODE` | `ScOrdInstrLog_AuditorCode` | String |  |  |
| 28 | `SC.OIL.AUDIT.DATE.TIME` | `ScOrdInstrLog_AuditDateTime` | String |  |  |
| 29 | `SC.OIL.CTDY.PORT.ACCT` | `ScOrdInstrLog_CtdyPortAcct` | TField |  | This fields custody Portfolio Acocunt from incoming message |
| 30 | `SC.OIL.SENDER.BIC` | `ScOrdInstrLog_SenderBic` | TField |  | This fields holds the BIC address of Sender from incoming message |
| 31 | `SC.OIL.SETT.IBAN.NO` | `ScOrdInstrLog_SettIbanNo` | TField |  | This fields holds the settlement IBAN number from incoming message |
| 32 | `SC.OIL.LATEST.MSG.TYPE` | `ScOrdInstrLog_LatestMsgType` | TField |  | This field will holds the latest message type processed |
| 33 | `SC.OIL.LATEST.MSG.IN.OUT` | `ScOrdInstrLog_LatestMsgInOut` | TField |  | This field indicates the the latest message is inward or outward |
| 34 | `SC.OIL.LATEST.MSG.FUNC` | `ScOrdInstrLog_LatestMsgFunc` | TField |  | This field holds the latest processed function of the message |
| 35 | `SC.OIL.LATEST.MSG.QTY` | `ScOrdInstrLog_LatestMsgQty` | TField |  | This field holds the order quantity of the latest message processed |
| 36 | `SC.OIL.LATEST.MSG.PRICE` | `ScOrdInstrLog_LatestMsgPrice` | TField |  | This field holds the price of the latest message processed |
| 37 | `SC.OIL.LATEST.ORD.STATUS` | `ScOrdInstrLog_LatestOrdStatus` | TField |  | This field holds the order status of the latest processed message |
| 38 | `SC.OIL.LATEST.PROC.STATUS` | `ScOrdInstrLog_LatestProcStatus` | TField |  | This field holds the status of latest processed message |
| 39 | `SC.OIL.LATEST.ERR.REASON` | `ScOrdInstrLog_LatestErrReason` |  |  |  |
| 40 | `SC.OIL.LATEST.REASON.NARR` | `ScOrdInstrLog_LatestReasonNarr` |  |  |  |
| 41 | `SC.OIL.LATEST.DELIVERY.REF` | `ScOrdInstrLog_LatestDeliveryRef` | TField |  | This field holds the delivery reference of the latest message processed |
| 42 | `SC.OIL.TRIGGER.STATUS` | `ScOrdInstrLog_TriggerStatus` | TField |  |  |
| 43 | `SC.OIL.ISIN` | `ScOrdInstrLog_Isin` | TField |  | This will hold the ISIN in the message. |
| 44 | `SC.OIL.BROKER.ID` | `ScOrdInstrLog_BrokerId` | TField |  |  |
| 45 | `SC.OIL.BROKER.BIC` | `ScOrdInstrLog_BrokerBic` | TField |  | This will hold the BROKER.BIC in the message. |
| 46 | `SC.OIL.CONF.CANC.RECD` | `ScOrdInstrLog_ConfCancRecd` |  |  |  |
| 47 | `SC.OIL.CONF.CANC.IN.OUT` | `ScOrdInstrLog_ConfCancInOut` |  |  |  |
| 48 | `SC.OIL.BR.EXE.ADV.REF` | `ScOrdInstrLog_BrExeAdvRef` |  |  |  |
| 49 | `SC.OIL.AMEND.EXPECTED` | `ScOrdInstrLog_AmendExpected` |  |  |  |
| 50 | `SC.OIL.ORDER.STAGE` | `ScOrdInstrLog_OrderStage` |  |  |  |
| 51 | `SC.OIL.CONF.CANC.STATUS` | `ScOrdInstrLog_ConfCancStatus` |  |  |  |
| 52 | `SC.OIL.CONF.CANC.NARR` | `ScOrdInstrLog_ConfCancNarr` |  |  |  |
| 53 | `SC.OIL.CONF.DELIVERY.REF` | `ScOrdInstrLog_ConfDeliveryRef` |  |  |  |
| 54 | `SC.OIL.SEND.CONF.CANC.MSG` | `ScOrdInstrLog_SendConfCancMsg` |  |  |  |
| 55 | `SC.OIL.ORDER.ID` | `ScOrdInstrLog_OrderId` | TField |  | This field holds the SEC.OPEN.ORDER id in cases where the system is unable to map the correct id in the field ID. |
| 56 | `SC.OIL.CONF.ERR.REASON` | `ScOrdInstrLog_ConfErrReason` |  |  |  |
| 57 | `SC.OIL.LATEST.CONF.RECD` | `ScOrdInstrLog_LatestConfRecd` | TField |  |  |
| 58 | `SC.OIL.LATEST.CONF.STATUS` | `ScOrdInstrLog_LatestConfStatus` | TField |  | This field will hold the status of latest confirmation cancellation message that is processed. |
| 59 | `SC.OIL.LATEST.CONF.ORD.STAGE` | `ScOrdInstrLog_LatestConfOrdStage` | TField |  | This field will hold the order stage of latest confirmation cancellation message that is processed. |
| 60 | `SC.OIL.ORIG.TRADE.ID` | `ScOrdInstrLog_OrigTradeId` |  |  |  |
| 61 | `SC.OIL.REPLACED.TRADE.ID` | `ScOrdInstrLog_ReplacedTradeId` |  |  |  |
| 62 | `SC.OIL.SEND.CONF.MSG` | `ScOrdInstrLog_SendConfMsg` |  |  |  |
| 63 | `SC.OIL.MANUAL.CONF.CANC` | `ScOrdInstrLog_ManualConfCanc` |  |  |  |
| 64 | `SC.OIL.MANUAL.CONF.CANC.NARR` | `ScOrdInstrLog_ManualConfCancNarr` |  |  |  |
