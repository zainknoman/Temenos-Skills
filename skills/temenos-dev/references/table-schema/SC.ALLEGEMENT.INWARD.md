# SC.ALLEGEMENT.INWARD — Table Schema

> Source: `INSERTS/I_F.SC.ALLEGEMENT.INWARD` in `SC_STP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.AL.SENDER.BIC` | `ScAllegementInward_SenderBic` | TField |  | This field holds the BIC Address of Sender from message. Mapped with value from FROM.ADDRESS in DE.I.HEADER |
| 2 | `SC.AL.SENDER.CUSTOMER` | `ScAllegementInward_SenderCustomer` | TField |  | T24 Customer reference of Sender from the incoming message. This field holds the T24 Customer ID of the Sender of the Message. Mapped with value from CUSTOMER.NO in DE.I.HEADER Validation Rules: Valid CUSTOMER record |
| 3 | `SC.AL.SENDER.REF` | `ScAllegementInward_SenderRef` | TField |  | Sender Message Reference from the incoming message. For MT578, Mapping is done from Sequence A - GENL as 20C:SEME tag |
| 4 | `SC.AL.IN.DELIVERY.REF` | `ScAllegementInward_InDeliveryRef` |  |  |  |
| 5 | `SC.AL.FUNCTION` | `ScAllegementInward_Function` |  |  |  |
| 6 | `SC.AL.PREP.DATE` | `ScAllegementInward_PrepDate` | TField |  | This field holds the date of preparation of the contract. Mapping is done from Sequence A - GENL as 98a:PREP tag Validation Rules: Standard Date Field |
| 7 | `SC.AL.PREP.TIME` | `ScAllegementInward_PrepTime` | TField |  | This field holds the time of preparation of the contract. Mapping is done from Sequence A - GENL as 98a:PREP tag Validation Rules: Standard Time Field |
| 8 | `SC.AL.PREV.MSG.REF` | `ScAllegementInward_PrevMsgRef` | TField |  | This field holds the message reference of the linked message which was previously received. For MT578, Mapping is done from Sequence A1 - LINK as 20C::RELA tag |
| 9 | `SC.AL.COMM.REF` | `ScAllegementInward_CommRef` | TField |  | This field holds the unique reference agreed upon by the two trade counterparties. Mapping is done from Sequence A1 - LINK as 20C::COMM tag |
| 10 | `SC.AL.MARKET.INFRA.REF` | `ScAllegementInward_MarketInfraRef` | TField |  | This field holds the Identification of a transaction assigned by a market infrastructure other than a centralsecurities depository. Mapping is done from Sequence A1 - LINK as 20C::MITI tag |
| 11 | `SC.AL.VALUE.DATE` | `ScAllegementInward_ValueDate` | TField |  | Settlement Date in the incoming message. Mapping is done from Sequence B - TRADDET with 98A:SETT tag Validation Rules: Standard Date Field Value Date cannot be less than Trade Date |
| 12 | `SC.AL.TRADE.DATE` | `ScAllegementInward_TradeDate` | TField |  | Trade Date in the incoming message. Mapping is done from Sequence B - TRADDET with 98A:TRAD tag Validation Rules: Standard Date Field Trade date cannot be greater than today (T24 System Date) |
| 13 | `SC.AL.ISIN` | `ScAllegementInward_Isin` | TField |  | ISIN in the incoming message. Mapping is done from Sequence B - TRADDET as 35B:ISIN tag |
| 14 | `SC.AL.PLIS` | `ScAllegementInward_Plis` | TField |  | This field holds the Place of Listing or MIC code in the incoming message. Mapping is done from B1 - FIA as 94B::PLIS tag |
| 15 | `SC.AL.STOCK.EXCHANGE` | `ScAllegementInward_StockExchange` | TField |  | This field holds the valid Stock Exchange record retreived from Security master based on the MIC code in PLISfield |
| 16 | `SC.AL.SEC.CURRENCY` | `ScAllegementInward_SecCurrency` | TField |  |  |
| 17 | `SC.AL.SECURITY.NUMBER` | `ScAllegementInward_SecurityNumber` | TField |  | This field holds the security master ID. System would populate this field based on the ISIN. When ALT.INDEX.CHECK is set in SM.PARAMETER where multipleSECURITY.MASTER record can have same ISIN, system will identify the most appropriate SECURITY.MASTER based on theCURRENCY and/OR STOCK.EXCHANGE combination. Validation Rules: Valid SECURITY.MASTER record |
| 18 | `SC.AL.PAY.INSTR` | `ScAllegementInward_PayInstr` | TField |  | This field holds the payment indicator, against payment or free of payment. Mapping is done from Sequence B - TRADDET as 22H:PAYM tag Validation Rules: Allowed Values: APMT, FREE |
| 19 | `SC.AL.TRANS.INSTR` | `ScAllegementInward_TransInstr` | TField |  | This field holds whether the counterparty's instruction is a receipt or delivery of financial instruments. Mapping is done from Sequence B - TRADDET as 22H:REDE tag Validation Rules: Allowed Values: DELI, RECE |
| 20 | `SC.AL.NOMINAL` | `ScAllegementInward_Nominal` | TField |  | Quantity of Security in message. Mapping is done from Sequence C - FIAC 36B:SETT tag |
| 21 | `SC.AL.DEAL.CURRENCY` | `ScAllegementInward_DealCurrency` | TField |  | Currency in which price is associated in message. Mapping is done from Sequence B - TRADDET 90B:DEAL tag |
| 22 | `SC.AL.DEAL.PRICE` | `ScAllegementInward_DealPrice` | TField |  | Price in message. Mapping is done from Sequence B - TRADDET 90B tag |
| 23 | `SC.AL.ACC.OWN` | `ScAllegementInward_AccOwn` | TField |  | This field holds the account owner details. Mapping is done from Sequence C - FIAC as 95P::ACOW tag |
| 24 | `SC.AL.CU.SAFE.ACC` | `ScAllegementInward_CuSafeAcc` | TField |  | This field holds the safe account of the Customer. Mapping is done from Sequence C - FIAC as 97A::SAFE//(Account number) OR 97B::SAFE//(Data Source Scheme)/(Accounttype)/Account number) tag |
| 25 | `SC.AL.CU.SAFE.ACC.DSS` | `ScAllegementInward_CuSafeAccDss` | TField |  | This field holds the data source scheme mentioned in the message. Mapping is done from Sequence C - FIAC as 97B::SAFE// (Data Source Scheme)/(Account type)/Account number tag |
| 26 | `SC.AL.CU.SAFE.ACC.TYPE` | `ScAllegementInward_CuSafeAccType` | TField |  | This field holds the account type mentioned in the message. Mapping is done from Sequence C - FIAC as 97B::SAFE// (Data Source Scheme)/(Account type)/Account number tag |
| 27 | `SC.AL.SETT.TRANS.INDI` | `ScAllegementInward_SettTransIndi` | TField |  | This field contains the settlement transaction indicator, whether it is a internal account transfer or externalaccount transfer. Mapping is done from Sequence E - SETDET as 22F::SETR tag |
| 28 | `SC.AL.SETT.TRANS.COND.INDI` | `ScAllegementInward_SettTransCondIndi` | TField |  | This field contains the settlement transaction condition indicator, whether partial settlement is allowed or not. Mapping is done from Sequence E - SETDET as 22F::STCO tag |
| 29 | `SC.AL.DELIV.AGENT` | `ScAllegementInward_DelivAgent` |  |  |  |
| 30 | `SC.AL.DELIV.AGENT.ACC` | `ScAllegementInward_DelivAgentAcc` |  |  |  |
| 31 | `SC.AL.DELIV.AGENT.ACC.DSS` | `ScAllegementInward_DelivAgentAccDss` |  |  |  |
| 32 | `SC.AL.DELIV.AGENT.ACC.TYPE` | `ScAllegementInward_DelivAgentAccType` |  |  |  |
| 33 | `SC.AL.SELLER` | `ScAllegementInward_Seller` | TField |  | This field holds the Seller details. Mapping is done from Sequence E - SETDET as 95P::SELL tag |
| 34 | `SC.AL.SELLER.ACC` | `ScAllegementInward_SellerAcc` | TField |  | This field holds the safe account of the Seller. Mapping is done from Sequence E - SETDET as 97A::SAFE// (Account number) OR 97B::SAFE// (Data SourceScheme)/(Account type)/(Account number) tag |
| 35 | `SC.AL.SELLER.ACC.DSS` | `ScAllegementInward_SellerAccDss` | TField |  | This field holds the data source scheme mentioned in the message. Mapping is done from Sequence C - FIAC as 97B::SAFE// (Data Source Scheme)/(Account type)/Account number tag |
| 36 | `SC.AL.SELLER.ACC.TYPE` | `ScAllegementInward_SellerAccType` | TField |  | This field holds the account type mentioned in the message. Mapping is done from Sequence C - FIAC as 97B::SAFE// (Data Source Scheme)/(Account type)/Account number tag |
| 37 | `SC.AL.RECIEVE.AGENT` | `ScAllegementInward_RecieveAgent` |  |  |  |
| 38 | `SC.AL.RECIEVE.AGENT.ACC` | `ScAllegementInward_RecieveAgentAcc` |  |  |  |
| 39 | `SC.AL.RECIEVE.AGENT.ACC.DSS` | `ScAllegementInward_RecieveAgentAccDss` |  |  |  |
| 40 | `SC.AL.RECIEVE.AGENT.ACC.TYPE` | `ScAllegementInward_RecieveAgentAccType` |  |  |  |
| 41 | `SC.AL.BUYER` | `ScAllegementInward_Buyer` | TField |  | This field holds the Buyer details. Mapping is done from Sequence E - SETDET as 95P::BUYR tag |
| 42 | `SC.AL.BUYER.ACC` | `ScAllegementInward_BuyerAcc` | TField |  | This field holds the safe account of the Buyer. Mapping is done from Sequence E - SETDET as 97A::SAFE// (Account number) OR 97B::SAFE// (Data SourceScheme)/(Account type)/(Account number) tag |
| 43 | `SC.AL.BUYER.ACC.DSS` | `ScAllegementInward_BuyerAccDss` | TField |  | This field holds the data source scheme mentioned in the message. Mapping is done from Sequence C - FIAC as 97B::SAFE// (Data Source Scheme)/(Account type)/(Account number) tag |
| 44 | `SC.AL.BUYER.ACC.TYPE` | `ScAllegementInward_BuyerAccType` | TField |  | This field holds the account type mentioned in the message. Mapping is done from Sequence C - FIAC as 97B::SAFE// (Data Source Scheme)/(Account type)/(Account number) tag |
| 45 | `SC.AL.BROKER.NO` | `ScAllegementInward_BrokerNo` | TField |  | This field holds Broker id. System will identify the appropriate broker based on the below logic: i)When TRANS.INSTR is DELI, system will compare the SELLER.ACC with SELL.AC in SC.SETT.INSTRUCT and identify thecustomer ID of the Broker.ii)When TRANS.INSTR is RECE, system will compare the BUYER.ACC with BUYR.AC inSC.SETT.INSTRUCT and identify thecustomer ID of the Broker. Validation Rules: Valid CUSTOMER record |
| 46 | `SC.AL.PORTFOLIO.ID` | `ScAllegementInward_PortfolioId` | TField |  | This field holds Portfolio for which SECURITY.TRANSFER will be created. System will identify the appropriate Portfolio based on the below logic: i)When the TRANS.INSTR is DELI, system will identify the portfolio by comparing the BUYER.ACC with theSUB.ACC.EXT.ID in SEC.ACC.MASTERii)When the TRANS.INSTR is RECE,System will identify the portfolio by comparing theSELLER.ACC with the SUB.ACC.EXT.ID in SEC.ACC.MASTER Validation Rules: Valid SEC.ACC.MASTER record |
| 47 | `SC.AL.STATUS` | `ScAllegementInward_Status` | TField | Yes | The below values are possible in this field: 1) RECEIVED - When all mandatory fields required to create a transaction in the system are available from theMT578 Incoming message 2) CANCELLED - If message with function CANC or REMO is received, status will be marked as CANCELLED providedSECURITY.TRANSFER record is not available. 3) ERROR - If any of the mandatory fields are missing or cannot be identified without doubt, the status will bemarked as ERROR. Status will also move to Error if Cancellation inward is received after ACCEPTEDstatus(SECURITY.TRANSFER record available). 4) ACCCEPTED - When user changes from RECEIVED to ACCEPTED, the system will create a new SECURITY.TRANSFERrecord in INAU and its ID reference will be stored in the field SECURITY.TRANSFER.REF 5) REJECTED - If the user after investigation, decides to Reject the allegement, the user will have to changethe STATUS as 'REJECTED'. User can also record the Reason for Rejection. 6) TRFR.CANCELLED - When generated Security Transfer is deleted or reversed, the system will update the Statusas TRFR.CANCELLED Validation Rules: Allowed values : RECEIVED,ERROR,ACCEPTED,REJECTED,CANCELLED,TRFR.CANCELLED When Error reason is present, then Status cannot be changed to RECEIVED, ACCEPTED or TRFR.CANCELLED |
| 48 | `SC.AL.ERROR.REASON` | `ScAllegementInward_ErrorReason` |  |  |  |
| 49 | `SC.AL.REJECT.REASON` | `ScAllegementInward_RejectReason` |  |  |  |
| 50 | `SC.AL.SECURITY.TRANSFER.REF` | `ScAllegementInward_SecurityTransferRef` | TField |  | This field holds the SECURITY.TRANSFER id which has been created through SC.ALLEGATION.INWARD record. When the SECURITY.TRANSFER is deleted or reversed, this field will be made NULL allowing the user toreject or Cancel the Allegement When the generated Security Transfer is deleted or reversed, the Status is updated as TRFR.CANCELLED Validation Rules: Noinput Field. Updated by the System |
| 51 | `SC.AL.ACTION.STATUS` | `ScAllegementInward_ActionStatus` | TField |  | The alert, escalations and potential failure enquiries will show the transactions as long as this field is not Actioned. Allowed values are 'Actioned' or blank. |
| 52 | `SC.AL.RESERVED.9` | `ScAllegementInward_Reserved9` | TField |  |  |
| 53 | `SC.AL.RESERVED.8` | `ScAllegementInward_Reserved8` | TField |  |  |
| 54 | `SC.AL.RESERVED.7` | `ScAllegementInward_Reserved7` | TField |  |  |
| 55 | `SC.AL.RESERVED.6` | `ScAllegementInward_Reserved6` | TField |  |  |
| 56 | `SC.AL.RESERVED.5` | `ScAllegementInward_Reserved5` | TField |  |  |
| 57 | `SC.AL.RESERVED.4` | `ScAllegementInward_Reserved4` | TField |  |  |
| 58 | `SC.AL.RESERVED.3` | `ScAllegementInward_Reserved3` | TField |  |  |
| 59 | `SC.AL.RESERVED.2` | `ScAllegementInward_Reserved2` | TField |  |  |
| 60 | `SC.AL.RESERVED.1` | `ScAllegementInward_Reserved1` | TField |  |  |
| 61 | `SC.AL.LOCAL.REF` | `ScAllegementInward_LocalRef` |  |  |  |
| 62 | `SC.AL.OVERRIDE` | `ScAllegementInward_Override` |  |  |  |
| 63 | `SC.AL.RECORD.STATUS` | `ScAllegementInward_RecordStatus` | String |  |  |
| 64 | `SC.AL.CURR.NO` | `ScAllegementInward_CurrNo` | String |  |  |
| 65 | `SC.AL.INPUTTER` | `ScAllegementInward_Inputter` |  |  |  |
| 66 | `SC.AL.DATE.TIME` | `ScAllegementInward_DateTime` |  |  |  |
| 67 | `SC.AL.AUTHORISER` | `ScAllegementInward_Authoriser` | String |  |  |
| 68 | `SC.AL.CO.CODE` | `ScAllegementInward_CoCode` | String |  |  |
| 69 | `SC.AL.DEPT.CODE` | `ScAllegementInward_DeptCode` | String |  |  |
| 70 | `SC.AL.AUDITOR.CODE` | `ScAllegementInward_AuditorCode` | String |  |  |
| 71 | `SC.AL.AUDIT.DATE.TIME` | `ScAllegementInward_AuditDateTime` | String |  |  |
