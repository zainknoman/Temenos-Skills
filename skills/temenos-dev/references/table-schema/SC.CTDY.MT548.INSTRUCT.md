# SC.CTDY.MT548.INSTRUCT — Table Schema

> Source: `INSERTS/I_F.SC.CTDY.MT548.INSTRUCT` in `SC_STP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CTDY.INTR.CUSTOMER` | `ScCtdyMt548Instruct_Customer` | TField |  | Holds the Customer To whom MT548 needs to Sent Validation Rules: This is NOINPUT Field |
| 2 | `SC.CTDY.INTR.EAM.ID` | `ScCtdyMt548Instruct_EamId` | TField |  | This Field has EAM.ID To whom MT548 needs to be sent Validation Rules: This is NOINPUT Field |
| 3 | `SC.CTDY.INTR.STATUS` | `ScCtdyMt548Instruct_Status` |  |  |  |
| 4 | `SC.CTDY.INTR.HIGH.LVL.STAT` | `ScCtdyMt548Instruct_HighLvlStat` |  |  |  |
| 5 | `SC.CTDY.INTR.ACTION.REQUIRED` | `ScCtdyMt548Instruct_ActionRequired` |  |  |  |
| 6 | `SC.CTDY.INTR.REASON.CODE` | `ScCtdyMt548Instruct_ReasonCode` |  |  |  |
| 7 | `SC.CTDY.INTR.REASON.NARRATIVE` | `ScCtdyMt548Instruct_ReasonNarrative` |  |  |  |
| 8 | `SC.CTDY.INTR.SEME.REF` | `ScCtdyMt548Instruct_SemeRef` | TField |  | This field holds SEC.TRADE or SECURITY.TRANSFER id which was created through 540-543 This will be Sent in 20C Tag of Outgoing MT548 |
| 9 | `SC.CTDY.INTR.RELA` | `ScCtdyMt548Instruct_Rela` | TField |  | This Field will have Seme Reference of Incoming Message(540-543) or 548 This will be Forwarded in 20C Tag Under Link Block of Outgoing MT548 |
| 10 | `SC.CTDY.INTR.CUSTOMER.TRANS.REF` | `ScCtdyMt548Instruct_CustomerTransRef` | TField |  | The field will have Seme Reference of Incoming Message which was used to Create Transactions |
| 11 | `SC.CTDY.INTR.SENDER.BIC` | `ScCtdyMt548Instruct_SenderBic` | TField |  | Address of Sender who sent 540 -543 Message to create Transaction |
| 12 | `SC.CTDY.INTR.SAFEKEEP.ACCOUNT` | `ScCtdyMt548Instruct_SafekeepAccount` | TField |  | This field will hold the Customer�s Safe keeping account with the bank and will be updated from the incoming MT 540-3 This will be sent in 97A Tag in Outgoing MT548 |
| 13 | `SC.CTDY.INTR.SECURITY` | `ScCtdyMt548Instruct_Security` | TField |  | This field will hold the instrument identifier This will be mapped to Tag 35B in Outgoing MT548 Message |
| 14 | `SC.CTDY.INTR.FUNCTION` | `ScCtdyMt548Instruct_Function` | TField |  | This field will be mapped to tag 23G:// of MT 548 |
| 15 | `SC.CTDY.INTR.MSG.IN.DATE.TIME` | `ScCtdyMt548Instruct_MsgInDateTime` |  |  |  |
| 16 | `SC.CTDY.INTR.MSG.OUT.DATE.TIME` | `ScCtdyMt548Instruct_MsgOutDateTime` |  |  |  |
| 17 | `SC.CTDY.INTR.NO.NOMINAL` | `ScCtdyMt548Instruct_NoNominal` | TField |  | This field holds Nominal of Underlying Security in Transaction |
| 18 | `SC.CTDY.INTR.TRADE.DATE` | `ScCtdyMt548Instruct_TradeDate` | TField |  | Trade Date of Security Transaction |
| 19 | `SC.CTDY.INTR.SETTLEMENT.DATE` | `ScCtdyMt548Instruct_SettlementDate` | TField |  | Value Date of Security Transaction |
| 20 | `SC.CTDY.INTR.GEN.MT548` | `ScCtdyMt548Instruct_GenMt548` | TField |  | GEN.MT548 should be "Yes" if 548 is Manually Triggered GEN.MT548 should be "NO" if 548 is Triggered through Transactions |
| 21 | `SC.CTDY.INTR.DELIVERY.INW.REF` | `ScCtdyMt548Instruct_DeliveryInwRef` | TField |  | This field hold Delivery Reference of Incoming Message (540-543) or 548 This field is Defaulted from Inward Delivery Reference Field in Transactions(SEC.TRADE/SECURITY.TRANSFER) |
| 22 | `SC.CTDY.INTR.DELIVERY.OUT.REF` | `ScCtdyMt548Instruct_DeliveryOutRef` |  |  |  |
| 23 | `SC.CTDY.INTR.SETTLEMENT.AMT` | `ScCtdyMt548Instruct_SettlementAmt` | TField |  | This field will have Settlement Amount of Transaction This will be forwarded in 19A Tag of outgoing MT548 Message |
| 24 | `SC.CTDY.INTR.MOVEMENT.TYPE` | `ScCtdyMt548Instruct_MovementType` | TField |  | This field indicates whether the financial instrument has to be debited from (DELE) / credited to (RECE) the safekeeping account It will be mapped to tag 22H in Outgoing Message Validation Rules: This should be 'REDE//RECE' if SECURITY is Credited This should be 'REDE//DELI' if SECURITY is Debited |
| 25 | `SC.CTDY.INTR.PAYMENT` | `ScCtdyMt548Instruct_Payment` | TField |  | This field indicates whether the instruction is free or against payment. The available options are Against Payment (APMT) or FREE It will be mapped to tag 22H in Outgoing Message Validation Rules: This should be 'PAYM//FREE' if SECURITY.TRANSFER This should be 'PAYM//APMT' if SEC.TRADE |
| 26 | `SC.CTDY.INTR.BUYR` | `ScCtdyMt548Instruct_Buyr` | TField |  | This field will be Defaulted from BIC.CODE of Broker Agent if DEBIT Transaction |
| 27 | `SC.CTDY.INTR.DEAG` | `ScCtdyMt548Instruct_Deag` | TField |  | This field will be Defaulted from BIC.CODE of Broker Agent if CREDIT Transaction |
| 28 | `SC.CTDY.INTR.DECU` | `ScCtdyMt548Instruct_Decu` | TField |  |  |
| 29 | `SC.CTDY.INTR.PSET` | `ScCtdyMt548Instruct_Pset` | TField |  | This field will be Defaulted from PSET Value of TRANSACTION(SEC.TRADE/SECURITY.TRANSFER) |
| 30 | `SC.CTDY.INTR.REAG` | `ScCtdyMt548Instruct_Reag` | TField |  | This field will be Defaulted from Broker Agent if DEBIT Transaction |
| 31 | `SC.CTDY.INTR.RECU` | `ScCtdyMt548Instruct_Recu` | TField |  |  |
| 32 | `SC.CTDY.INTR.SELL` | `ScCtdyMt548Instruct_Sell` | TField |  | This field will be Defaulted from BIC.CODE of Broker Agent if CREDIT Transaction |
| 33 | `SC.CTDY.INTR.LATEST.STATUS` | `ScCtdyMt548Instruct_LatestStatus` |  |  |  |
| 34 | `SC.CTDY.INTR.LATEST.HIGH.LVL.STAT` | `ScCtdyMt548Instruct_LatestHighLvlStat` |  |  |  |
| 35 | `SC.CTDY.INTR.LATEST.ACTION.REQ` | `ScCtdyMt548Instruct_LatestActionReq` |  |  |  |
| 36 | `SC.CTDY.INTR.PREVIOUS.STATUS` | `ScCtdyMt548Instruct_PreviousStatus` |  |  |  |
| 37 | `SC.CTDY.INTR.SAVE.STATUS` | `ScCtdyMt548Instruct_SaveStatus` |  |  |  |
| 38 | `SC.CTDY.INTR.SAVE.HIGH.LVL.STAT` | `ScCtdyMt548Instruct_SaveHighLvlStat` |  |  |  |
| 39 | `SC.CTDY.INTR.SAVE.ACTION.REQUIRED` | `ScCtdyMt548Instruct_SaveActionRequired` |  |  |  |
| 40 | `SC.CTDY.INTR.SAVE.REASON.CODE` | `ScCtdyMt548Instruct_SaveReasonCode` |  |  |  |
| 41 | `SC.CTDY.INTR.SAVE.REASON.NARRATIVE` | `ScCtdyMt548Instruct_SaveReasonNarrative` |  |  |  |
| 42 | `SC.CTDY.INTR.SAVE.SEME.REF` | `ScCtdyMt548Instruct_SaveSemeRef` |  |  |  |
| 43 | `SC.CTDY.INTR.SAVE.RELA` | `ScCtdyMt548Instruct_SaveRela` |  |  |  |
| 44 | `SC.CTDY.INTR.SAVE.CUSTOMER.TRANS.REF` | `ScCtdyMt548Instruct_SaveCustomerTransRef` |  |  |  |
| 45 | `SC.CTDY.INTR.SAVE.SENDER.BIC` | `ScCtdyMt548Instruct_SaveSenderBic` |  |  |  |
| 46 | `SC.CTDY.INTR.SAVE.SAFEKEEP.ACCOUNT` | `ScCtdyMt548Instruct_SaveSafekeepAccount` |  |  |  |
| 47 | `SC.CTDY.INTR.SAVE.SECURITY` | `ScCtdyMt548Instruct_SaveSecurity` |  |  |  |
| 48 | `SC.CTDY.INTR.SAVE.FUNCTION` | `ScCtdyMt548Instruct_SaveFunction` |  |  |  |
| 49 | `SC.CTDY.INTR.SAVE.MSG.IN.DATE.TIME` | `ScCtdyMt548Instruct_SaveMsgInDateTime` |  |  |  |
| 50 | `SC.CTDY.INTR.SAVE.MSG.OUT.DATE.TIME` | `ScCtdyMt548Instruct_SaveMsgOutDateTime` |  |  |  |
| 51 | `SC.CTDY.INTR.SAVE.NO.NOMINAL` | `ScCtdyMt548Instruct_SaveNoNominal` |  |  |  |
| 52 | `SC.CTDY.INTR.SAVE.TRADE.DATE` | `ScCtdyMt548Instruct_SaveTradeDate` |  |  |  |
| 53 | `SC.CTDY.INTR.SAVE.SETTLEMENT.DATE` | `ScCtdyMt548Instruct_SaveSettlementDate` |  |  |  |
| 54 | `SC.CTDY.INTR.SAVE.GEN.MT548` | `ScCtdyMt548Instruct_SaveGenMt548` |  |  |  |
| 55 | `SC.CTDY.INTR.SAVE.DELIVERY.INW.REF` | `ScCtdyMt548Instruct_SaveDeliveryInwRef` |  |  |  |
| 56 | `SC.CTDY.INTR.SAVE.DELIVERY.OUT.REF` | `ScCtdyMt548Instruct_SaveDeliveryOutRef` |  |  |  |
| 57 | `SC.CTDY.INTR.SAVE.SETTLEMENT.AMT` | `ScCtdyMt548Instruct_SaveSettlementAmt` |  |  |  |
| 58 | `SC.CTDY.INTR.SAVE.MOVEMENT.TYPE` | `ScCtdyMt548Instruct_SaveMovementType` |  |  |  |
| 59 | `SC.CTDY.INTR.SAVE.PAYMENT` | `ScCtdyMt548Instruct_SavePayment` |  |  |  |
| 60 | `SC.CTDY.INTR.SAVE.BUYR` | `ScCtdyMt548Instruct_SaveBuyr` |  |  |  |
| 61 | `SC.CTDY.INTR.SAVE.DEAG` | `ScCtdyMt548Instruct_SaveDeag` |  |  |  |
| 62 | `SC.CTDY.INTR.SAVE.DECU` | `ScCtdyMt548Instruct_SaveDecu` |  |  |  |
| 63 | `SC.CTDY.INTR.SAVE.PSET` | `ScCtdyMt548Instruct_SavePset` |  |  |  |
| 64 | `SC.CTDY.INTR.SAVE.REAG` | `ScCtdyMt548Instruct_SaveReag` |  |  |  |
| 65 | `SC.CTDY.INTR.SAVE.RECU` | `ScCtdyMt548Instruct_SaveRecu` |  |  |  |
| 66 | `SC.CTDY.INTR.SAVE.SELL` | `ScCtdyMt548Instruct_SaveSell` |  |  |  |
| 67 | `SC.CTDY.INTR.LATEST.DELIVERY.INW.REF` | `ScCtdyMt548Instruct_LatestDeliveryInwRef` | TField |  |  |
| 68 | `SC.CTDY.INTR.RESERVED2` | `ScCtdyMt548Instruct_Reserved2` | TField |  |  |
| 69 | `SC.CTDY.INTR.RESERVED3` | `ScCtdyMt548Instruct_Reserved3` | TField |  |  |
| 70 | `SC.CTDY.INTR.RESERVED4` | `ScCtdyMt548Instruct_Reserved4` | TField |  |  |
| 71 | `SC.CTDY.INTR.RESERVED5` | `ScCtdyMt548Instruct_Reserved5` | TField |  |  |
| 72 | `SC.CTDY.INTR.RESERVED6` | `ScCtdyMt548Instruct_Reserved6` | TField |  |  |
| 73 | `SC.CTDY.INTR.RESERVED7` | `ScCtdyMt548Instruct_Reserved7` | TField |  |  |
| 74 | `SC.CTDY.INTR.RESERVED8` | `ScCtdyMt548Instruct_Reserved8` | TField |  |  |
| 75 | `SC.CTDY.INTR.RESERVED9` | `ScCtdyMt548Instruct_Reserved9` | TField |  |  |
| 76 | `SC.CTDY.INTR.RESERVED10` | `ScCtdyMt548Instruct_Reserved10` | TField |  |  |
| 77 | `SC.CTDY.INTR.RESERVED11` | `ScCtdyMt548Instruct_Reserved11` | TField |  |  |
| 78 | `SC.CTDY.INTR.RESERVED12` | `ScCtdyMt548Instruct_Reserved12` | TField |  |  |
| 79 | `SC.CTDY.INTR.RESERVED13` | `ScCtdyMt548Instruct_Reserved13` | TField |  |  |
| 80 | `SC.CTDY.INTR.RESERVED14` | `ScCtdyMt548Instruct_Reserved14` | TField |  |  |
| 81 | `SC.CTDY.INTR.RESERVED15` | `ScCtdyMt548Instruct_Reserved15` | TField |  |  |
| 82 | `SC.CTDY.INTR.RESERVED16` | `ScCtdyMt548Instruct_Reserved16` | TField |  |  |
| 83 | `SC.CTDY.INTR.RESERVED17` | `ScCtdyMt548Instruct_Reserved17` | TField |  |  |
| 84 | `SC.CTDY.INTR.RESERVED18` | `ScCtdyMt548Instruct_Reserved18` | TField |  |  |
| 85 | `SC.CTDY.INTR.RESERVED19` | `ScCtdyMt548Instruct_Reserved19` | TField |  |  |
| 86 | `SC.CTDY.INTR.RESERVED20` | `ScCtdyMt548Instruct_Reserved20` | TField |  |  |
| 87 | `SC.CTDY.INTR.LOCAL.REF` | `ScCtdyMt548Instruct_LocalRef` |  |  |  |
| 88 | `SC.CTDY.INTR.STMT.NOS` | `ScCtdyMt548Instruct_StmtNos` |  |  |  |
| 89 | `SC.CTDY.INTR.OVERRIDE` | `ScCtdyMt548Instruct_Override` |  |  |  |
| 90 | `SC.CTDY.INTR.RECORD.STATUS` | `ScCtdyMt548Instruct_RecordStatus` | String |  |  |
| 91 | `SC.CTDY.INTR.CURR.NO` | `ScCtdyMt548Instruct_CurrNo` | String |  |  |
| 92 | `SC.CTDY.INTR.INPUTTER` | `ScCtdyMt548Instruct_Inputter` |  |  |  |
| 93 | `SC.CTDY.INTR.DATE.TIME` | `ScCtdyMt548Instruct_DateTime` |  |  |  |
| 94 | `SC.CTDY.INTR.AUTHORISER` | `ScCtdyMt548Instruct_Authoriser` | String |  |  |
| 95 | `SC.CTDY.INTR.CO.CODE` | `ScCtdyMt548Instruct_CoCode` | String |  |  |
| 96 | `SC.CTDY.INTR.DEPT.CODE` | `ScCtdyMt548Instruct_DeptCode` | String |  |  |
| 97 | `SC.CTDY.INTR.AUDITOR.CODE` | `ScCtdyMt548Instruct_AuditorCode` | String |  |  |
| 98 | `SC.CTDY.INTR.AUDIT.DATE.TIME` | `ScCtdyMt548Instruct_AuditDateTime` | String |  |  |
