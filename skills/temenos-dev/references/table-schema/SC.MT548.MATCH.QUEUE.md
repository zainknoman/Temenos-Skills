# SC.MT548.MATCH.QUEUE — Table Schema

> Source: `INSERTS/I_F.SC.MT548.MATCH.QUEUE` in `SC_STP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.MQE.MATCH.CODE` | `ScMt548MatchQueue_MatchCode` |  |  |  |
| 2 | `SC.MQE.REASON.CODE` | `ScMt548MatchQueue_ReasonCode` |  |  |  |
| 3 | `SC.MQE.REASON.NARRATIVE` | `ScMt548MatchQueue_ReasonNarrative` |  |  |  |
| 4 | `SC.MQE.MSG.DATE.TIME` | `ScMt548MatchQueue_MsgDateTime` |  |  |  |
| 5 | `SC.MQE.NO.NOMINAL` | `ScMt548MatchQueue_NoNominal` | TField |  | This field is updated by the system with the value in the tag 36B while processing MT548 message. Validation Rules: Single value field. Maximum allowed character is 1-18 numeric characters. |
| 6 | `SC.MQE.AMOUNT` | `ScMt548MatchQueue_Amount` | TField |  | This field is updated by the system with the value in the tag 19A while processing Mt548 message. Validation Rules: Single value field. Maximum allowed character is 1-18 numeric characters. |
| 7 | `SC.MQE.DELIVERY.REF` | `ScMt548MatchQueue_DeliveryRef` |  |  |  |
| 8 | `SC.MQE.SERVICER.TXN.REF` | `ScMt548MatchQueue_ServicerTxnRef` | TField |  | This field will hold the Account Servicer�s Transaction Reference Validation Rules: Single value field. Maximum allowed character is 35. |
| 9 | `SC.MQE.MARKET.TXN.REF` | `ScMt548MatchQueue_MarketTxnRef` | TField |  | This field will hold the Transaction Reference by a market infrastructure Eg:Target2-Securities Validation Rules: Single value field. Maximum allowed character is 35. |
| 10 | `SC.MQE.TRADE.DATE` | `ScMt548MatchQueue_TradeDate` | TField |  | This field will hold the Trade date as in the message Validation Rules: Single value field. Standard T24 Date format. |
| 11 | `SC.MQE.SETTLEMENT.DATE` | `ScMt548MatchQueue_SettlementDate` | TField |  | This field will hold the Settlement date as in the message Validation Rules: Single value field. Standard T24 Date format. |
| 12 | `SC.MQE.MOVEMENT.TYPE` | `ScMt548MatchQueue_MovementType` | TField |  | This field will specify if the movement on a securities account results from a deliver(DELI) or a receive(RECE) instruction Validation Rules: Single value field. Maximum allowed character is 10. |
| 13 | `SC.MQE.PAYMENT` | `ScMt548MatchQueue_Payment` | TField |  | This field will specify how the transaction is to be settled(FREE/APYMT) Validation Rules: Single value field. Maximum allowed character is 10. |
| 14 | `SC.MQE.SAFEKEEP.ACCOUNT` | `ScMt548MatchQueue_SafekeepAccount` | TField |  | This field will hold the account to or from which a securities entry is made Validation Rules: Single value field. Maximum allowed character is 35. |
| 15 | `SC.MQE.SECURITY` | `ScMt548MatchQueue_Security` | TField |  | This field will hold the Instrument Identifier. If ISIN, then ISIN, else any one identifier, else Description. Validation Rules: Single value field. Maximum allowed character is 12. |
| 16 | `SC.MQE.MESSAGE.TYPE` | `ScMt548MatchQueue_MessageType` | TField |  | This field will hold the DE.MESSAGE ID corresponding to the inward message that has updated the record. Eg. SESE024,SESE027 Validation Rules: Single value field. Maximum allowed character is 10. |
| 17 | `SC.MQE.MESSAGE.FUNC` | `ScMt548MatchQueue_MessageFunc` | TField |  | This field will denote the function of the message. This field is updated by the system with the value in the tag 23G while processing MT548 message. Validation Rules: Single value field. Alphanumeric upto 10 characters. |
| 18 | `SC.MQE.SETT.TXN.TYPE` | `ScMt548MatchQueue_SettTxnType` | TField |  |  |
| 19 | `SC.MQE.SPLIT.REFERENCE` | `ScMt548MatchQueue_SplitReference` |  |  |  |
| 20 | `SC.MQE.SPLIT.AMOUNT` | `ScMt548MatchQueue_SplitAmount` |  |  |  |
| 21 | `SC.MQE.LOCAL.REF` | `ScMt548MatchQueue_LocalRef` |  |  |  |
| 22 | `SC.MQE.OVERRIDE` | `ScMt548MatchQueue_Override` |  |  |  |
| 23 | `SC.MQE.RECORD.STATUS` | `ScMt548MatchQueue_RecordStatus` | String |  |  |
| 24 | `SC.MQE.CURR.NO` | `ScMt548MatchQueue_CurrNo` | String |  |  |
| 25 | `SC.MQE.INPUTTER` | `ScMt548MatchQueue_Inputter` |  |  |  |
| 26 | `SC.MQE.DATE.TIME` | `ScMt548MatchQueue_DateTime` |  |  |  |
| 27 | `SC.MQE.AUTHORISER` | `ScMt548MatchQueue_Authoriser` | String |  |  |
| 28 | `SC.MQE.CO.CODE` | `ScMt548MatchQueue_CoCode` | String |  |  |
| 29 | `SC.MQE.DEPT.CODE` | `ScMt548MatchQueue_DeptCode` | String |  |  |
| 30 | `SC.MQE.AUDITOR.CODE` | `ScMt548MatchQueue_AuditorCode` | String |  |  |
| 31 | `SC.MQE.AUDIT.DATE.TIME` | `ScMt548MatchQueue_AuditDateTime` | String |  |  |
| 32 | `SC.MQE.SPLIT.NOMINAL` | `ScMt548MatchQueue_SplitNominal` |  |  |  |
| 33 | `SC.MQE.ACTION.STATUS` | `ScMt548MatchQueue_ActionStatus` | TField |  | The alert, escalations and potential failure enquiries will show the transactions as long as this field is not Actioned. Allowed values are 'Actioned' or blank. |
