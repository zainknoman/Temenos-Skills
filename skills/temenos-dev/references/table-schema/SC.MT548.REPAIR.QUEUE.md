# SC.MT548.REPAIR.QUEUE — Table Schema

> Source: `INSERTS/I_F.SC.MT548.REPAIR.QUEUE` in `SC_STP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.RQE.TRANS.REF` | `ScMt548RepairQueue_TransRef` | TField |  | The TRANS.REF field is updated by the system with the transaction reference specified in the tag 20C while processing MT548 message. Validation Rules: Single value field. Maximum allowed character is 16 and is prefixed with SCTRSC or SECTSC |
| 2 | `SC.RQE.MATCH.CODE` | `ScMt548RepairQueue_MatchCode` |  |  |  |
| 3 | `SC.RQE.REASON.CODE` | `ScMt548RepairQueue_ReasonCode` |  |  |  |
| 4 | `SC.RQE.REASON.NARRATIVE` | `ScMt548RepairQueue_ReasonNarrative` |  |  |  |
| 5 | `SC.RQE.MSG.DATE.TIME` | `ScMt548RepairQueue_MsgDateTime` |  |  |  |
| 6 | `SC.RQE.NO.NOMINAL` | `ScMt548RepairQueue_NoNominal` | TField |  | This field is updated by the system with the value in the tag 36B while processing MT548 message. Validation Rules: Single value field. Maximum allowed character is 1-18 numeric characters. |
| 7 | `SC.RQE.AMOUNT` | `ScMt548RepairQueue_Amount` | TField |  | This field is updated by the system with the value in the tag 19A while processing Mt548 message. Validation Rules: Single value field. Maximum allowed character is 1-18 numeric characters. |
| 8 | `SC.RQE.REJECT.REASON` | `ScMt548RepairQueue_RejectReason` |  |  |  |
| 9 | `SC.RQE.DELIVERY.REF` | `ScMt548RepairQueue_DeliveryRef` |  |  |  |
| 10 | `SC.RQE.SERVICER.TXN.REF` | `ScMt548RepairQueue_ServicerTxnRef` | TField |  | This field will hold the Account Servicer�s Transaction Reference Validation Rules: Single value field. Maximum allowed character is 35. |
| 11 | `SC.RQE.MARKET.TXN.REF` | `ScMt548RepairQueue_MarketTxnRef` | TField |  | This field will hold the Transaction Reference by a market infrastructure Eg:Target2-Securities Validation Rules: Single value field. Maximum allowed character is 35. |
| 12 | `SC.RQE.TRADE.DATE` | `ScMt548RepairQueue_TradeDate` | TField |  | This field will hold the Trade date as in the message Validation Rules: Single value field. Standard T24 Date format. |
| 13 | `SC.RQE.SETTLEMENT.DATE` | `ScMt548RepairQueue_SettlementDate` | TField |  | This field will hold the Settlement date as in the message Validation Rules: Single value field. Standard T24 Date format. |
| 14 | `SC.RQE.MOVEMENT.TYPE` | `ScMt548RepairQueue_MovementType` | TField |  | This field will specify if the movement on a securities account results from a deliver(DELI) or a receive(RECE) instruction Validation Rules: Single value field. Maximum allowed character is 10. |
| 15 | `SC.RQE.PAYMENT` | `ScMt548RepairQueue_Payment` | TField |  | This field will specify how the transaction is to be settled(FREE/APYMT) Validation Rules: Single value field. Maximum allowed character is 10. |
| 16 | `SC.RQE.SAFEKEEP.ACCOUNT` | `ScMt548RepairQueue_SafekeepAccount` | TField |  | This field will hold the account to or from which a securities entry is made Validation Rules: Single value field. Maximum allowed character is 35. |
| 17 | `SC.RQE.SECURITY` | `ScMt548RepairQueue_Security` | TField |  | This field will hold the Instrument Identifier. If ISIN, then ISIN, else any one identifier, else Description. Validation Rules: Single value field. Maximum allowed character is 12. |
| 18 | `SC.RQE.UNMATCH.IN.T24` | `ScMt548RepairQueue_UnmatchInT24` |  |  |  |
| 19 | `SC.RQE.MANUAL.RECON.ID` | `ScMt548RepairQueue_ManualReconId` | TField |  | This will be a free format text field. If User is able to manually identify the T24 Transaction, the Transaction ID can be input here. Validation Rules: Single value field. Maximum allowed character is 35. |
| 20 | `SC.RQE.MESSAGE.TYPE` | `ScMt548RepairQueue_MessageType` | TField |  | This field will hold the DE.MESSAGE ID corresponding to the inward message that has updated the record. Eg. SESE024,SESE027 Validation Rules: Single value field. Maximum allowed character is 10. |
| 21 | `SC.RQE.MESSAGE.FUNC` | `ScMt548RepairQueue_MessageFunc` | TField |  | This field will denote the function of the message. This field is updated by the system with the value in the tag 23G while processing MT548 message. Validation Rules: Single value field. Alphanumeric upto 10 characters. |
| 22 | `SC.RQE.SETT.TXN.TYPE` | `ScMt548RepairQueue_SettTxnType` | TField |  |  |
| 23 | `SC.RQE.ACTION.STATUS` | `ScMt548RepairQueue_ActionStatus` | TField |  | The alert, escalations and potential failure enquiries will show the transactions as long as this field is not Actioned. Allowed values are 'Actioned' or blank. |
| 24 | `SC.RQE.RESERVED.1` | `ScMt548RepairQueue_Reserved1` | TField |  |  |
| 25 | `SC.RQE.LOCAL.REF` | `ScMt548RepairQueue_LocalRef` |  |  |  |
| 26 | `SC.RQE.OVERRIDE` | `ScMt548RepairQueue_Override` |  |  |  |
| 27 | `SC.RQE.RECORD.STATUS` | `ScMt548RepairQueue_RecordStatus` | String |  |  |
| 28 | `SC.RQE.CURR.NO` | `ScMt548RepairQueue_CurrNo` | String |  |  |
| 29 | `SC.RQE.INPUTTER` | `ScMt548RepairQueue_Inputter` |  |  |  |
| 30 | `SC.RQE.DATE.TIME` | `ScMt548RepairQueue_DateTime` |  |  |  |
| 31 | `SC.RQE.AUTHORISER` | `ScMt548RepairQueue_Authoriser` | String |  |  |
| 32 | `SC.RQE.CO.CODE` | `ScMt548RepairQueue_CoCode` | String |  |  |
| 33 | `SC.RQE.DEPT.CODE` | `ScMt548RepairQueue_DeptCode` | String |  |  |
| 34 | `SC.RQE.AUDITOR.CODE` | `ScMt548RepairQueue_AuditorCode` | String |  |  |
| 35 | `SC.RQE.AUDIT.DATE.TIME` | `ScMt548RepairQueue_AuditDateTime` | String |  |  |
