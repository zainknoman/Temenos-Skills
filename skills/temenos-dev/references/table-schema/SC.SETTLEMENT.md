# SC.SETTLEMENT — Table Schema

> Source: `INSERTS/I_F.SC.SETTLEMENT` in `SC_SctSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SETT.SECURITY.NUMBER` | `ScSettlement_SecurityNumber` | TField |  | Identifies the Security to be settled. Each security involved in the original transaction will have a separate settlement record. Therefore there will be only one settlement record from transactions in SEC.TRADE and SECURITY.TRANSFER that have requested actual settlement. Transactions from DIARY and ENTITLEMENT may create more than one settlement record. Transactions from POSITION.TRANSFER will create two settlement records, one each for the transfer of stock out of one depository and the transfer into another depository. Validation Rules: Internally generated field. Defaulted from the transaction which created this settlement record. |
| 2 | `SC.SETT.DEPOSITORY` | `ScSettlement_Depository` | TField |  | Identifies the Depository that holds or is to receive the Security concerned. In the case of POSITION.TRANSFER, two records are created for each security involved with the depository field differing in the two records as the DEPOSITORY.FROM and the DEPOSITORY.TO from the POSITION.TRANSFER record. Internally generated field. Defaulted from the transaction which created this settlement record. Cannot contain the value 'ALL' for a rights issue. |
| 3 | `SC.SETT.TRADE.DATE` | `ScSettlement_TradeDate` | TField |  | Date of the trade. Deal Date. Tax Point. Internally generated field. Defaulted from the transaction which created this settlement record. |
| 4 | `SC.SETT.VALUE.DATE` | `ScSettlement_ValueDate` | TField |  | Value date of the trade i.e. date after which the transaction can be settled. Internally generated field. Defaulted from the transaction which created this settlement record. |
| 5 | `SC.SETT.TRADE.CCY` | `ScSettlement_TradeCcy` | TField |  | Currency that the trade is to be settled in. Internally generated field. Defaulted from the transaction which created this settlement record. |
| 6 | `SC.SETT.TOTAL.NOMINAL` | `ScSettlement_TotalNominal` | TField |  | Total number of shares for settlement for the security specified in the field Where Multi Client/Multi Broker transactions have been input, the system will calculate the total per broker to be received or delivered and populate the appropriate fields at the time of creation of the settlement record. At this level we are not concerned with the Customer/Broker breakdown, merely the Net amount of stock to be settled. Internally calculated at the time of creation of the record. |
| 7 | `SC.SETT.TOTAL.BROKER.AMT` | `ScSettlement_TotalBrokerAmt` | TField |  | The total amout of cash to be Credited to or Debited from the brokers in this transaction. Validation Rules: Internally calculated at the time of creation of the record. |
| 8 | `SC.SETT.TOTAL.CUST.AMT` | `ScSettlement_TotalCustAmt` | TField |  | Total amount of cash to be Debited from or Credited to the Customers on this transaction. Validation Rules: Internally calculated at the time of creation of the record. |
| 9 | `SC.SETT.TOTAL.NOM.SETTLED` | `ScSettlement_TotalNomSettled` | TField |  | Total number of nominals settled as a result of current input to the Broker side of this transaction. Validation Rules: Internally calculated field. Updated as soon as data is input in |
| 10 | `SC.SETT.TOTAL.NOM.REVERSED` | `ScSettlement_TotalNomReversed` | TField |  | Total number of nominals reversed (unsettled) as a result of the current input to the Broker side on this transaction. Validation Rules: Internally generated field. Updated as soon as data is input at BR.REVERSE.NOM. |
| 11 | `SC.SETT.NOMINAL.TO.SETTLE` | `ScSettlement_NominalToSettle` | TField |  | This field holds the number of nominals yet to be settled on the customer's side. This field will be updated at the same time as The value in this field will start with the value in Validation Rules: Internally calculated field. Updated as soon as data is input at Must be zero at the time of committment. |
| 12 | `SC.SETT.NOMINAL.TO.REVERSE` | `ScSettlement_NominalToReverse` | TField |  | This field holds the number of nominals yet to be reversed on the customer's side. This field will be updated at the same time as The value in this field starts with the value of Validation Rules: Internally generated field. Updated as soon as data is input at Must be zero at the time of committment. |
| 13 | `SC.SETT.BRK.AMT.SETTLED` | `ScSettlement_BrkAmtSettled` | TField |  | This field holds the total amount of cash settled as a result of current input to the Broker side in this transaction. Validation Rules: Internally generated field. Updated as soon as data is input at The value in this field is cleared at authorisation. |
| 14 | `SC.SETT.BRK.AMT.REVERSED` | `ScSettlement_BrkAmtReversed` | TField |  | This is the total amount of cash reversed(unsettled) as a result of the current input to the Broker side in this transaction. Validation Rules: Internally generated field. Updated as soon as data is input at The value in this field is cleared at authorisation. |
| 15 | `SC.SETT.CUS.AMT.SETTLED` | `ScSettlement_CusAmtSettled` | TField |  | This field holds the total amount of cash settled as a result of the current input to the Customer side in this transaction. Validation Rules: Internally generated field. Updated as soon as data is input at The value in this field is cleared at authorisation. |
| 16 | `SC.SETT.CUS.AMT.REVERSED` | `ScSettlement_CusAmtReversed` | TField |  | This field holds the total amount of cash reversed(unsettled) as a result of the current input to the Customer side in this transaction. Validation Rules: Internally generated field. Updated as soon as data is input at The value in this field is cleared at authorisation. |
| 17 | `SC.SETT.BROKER.NO` | `ScSettlement_BrokerNo` |  |  |  |
| 18 | `SC.SETT.BR.DEL.INSTR` | `ScSettlement_BrDelInstr` |  |  |  |
| 19 | `SC.SETT.BR.NOM.SETTLED` | `ScSettlement_BrNomSettled` |  |  |  |
| 20 | `SC.SETT.BR.NOM.OUTSTAND` | `ScSettlement_BrNomOutstand` |  |  |  |
| 21 | `SC.SETT.BR.NOM.RECD.DEL` | `ScSettlement_BrNomRecdDel` |  |  |  |
| 22 | `SC.SETT.BR.REVERSE.NOM` | `ScSettlement_BrReverseNom` |  |  |  |
| 23 | `SC.SETT.BR.NOM.VAL.DATE` | `ScSettlement_BrNomValDate` |  |  |  |
| 24 | `SC.SETT.BR.NOM.DEL.REF` | `ScSettlement_BrNomDelRef` |  |  |  |
| 25 | `SC.SETT.BR.AMT.SETTLED` | `ScSettlement_BrAmtSettled` |  |  |  |
| 26 | `SC.SETT.BR.AMT.OUTSTAND` | `ScSettlement_BrAmtOutstand` |  |  |  |
| 27 | `SC.SETT.BR.AMT.REC.PAID` | `ScSettlement_BrAmtRecPaid` |  |  |  |
| 28 | `SC.SETT.BR.REVERSE.AMT` | `ScSettlement_BrReverseAmt` |  |  |  |
| 29 | `SC.SETT.BR.AMT.VAL.DATE` | `ScSettlement_BrAmtValDate` |  |  |  |
| 30 | `SC.SETT.BR.AMT.DEL.REF` | `ScSettlement_BrAmtDelRef` |  |  |  |
| 31 | `SC.SETT.DEPO.CONF.REF` | `ScSettlement_DepoConfRef` |  |  |  |
| 32 | `SC.SETT.BR.AUTO.SETT` | `ScSettlement_BrAutoSett` |  |  |  |
| 33 | `SC.SETT.BR.EXPOSURE` | `ScSettlement_BrExposure` |  |  |  |
| 34 | `SC.SETT.BR.NARRATIVE` | `ScSettlement_BrNarrative` |  |  |  |
| 35 | `SC.SETT.BR.TOL.AMT` | `ScSettlement_BrTolAmt` |  |  |  |
| 36 | `SC.SETT.SYS.MARKET.FEES` | `ScSettlement_SysMarketFees` |  |  |  |
| 37 | `SC.SETT.DEP.MARKET.FEES` | `ScSettlement_DepMarketFees` |  |  |  |
| 38 | `SC.SETT.BR.RESERVED2` | `ScSettlement_BrReserved2` |  |  |  |
| 39 | `SC.SETT.BR.RESERVED1` | `ScSettlement_BrReserved1` |  |  |  |
| 40 | `SC.SETT.CU.PORTFOLIO` | `ScSettlement_CuPortfolio` |  |  |  |
| 41 | `SC.SETT.CU.NOMINEE` | `ScSettlement_CuNominee` |  |  |  |
| 42 | `SC.SETT.CU.NOM.SETTLED` | `ScSettlement_CuNomSettled` |  |  |  |
| 43 | `SC.SETT.CU.NOM.OUTSTAND` | `ScSettlement_CuNomOutstand` |  |  |  |
| 44 | `SC.SETT.CU.NOM.RECD.DEL` | `ScSettlement_CuNomRecdDel` |  |  |  |
| 45 | `SC.SETT.CU.REVERSE.NOM` | `ScSettlement_CuReverseNom` |  |  |  |
| 46 | `SC.SETT.CU.NOM.VAL.DATE` | `ScSettlement_CuNomValDate` |  |  |  |
| 47 | `SC.SETT.CU.NOM.DEL.REF` | `ScSettlement_CuNomDelRef` |  |  |  |
| 48 | `SC.SETT.CU.AMT.SETTLED` | `ScSettlement_CuAmtSettled` |  |  |  |
| 49 | `SC.SETT.CU.AMT.OUTSTAND` | `ScSettlement_CuAmtOutstand` |  |  |  |
| 50 | `SC.SETT.CU.AMT.REC.PAID` | `ScSettlement_CuAmtRecPaid` |  |  |  |
| 51 | `SC.SETT.CU.REVERSE.AMT` | `ScSettlement_CuReverseAmt` |  |  |  |
| 52 | `SC.SETT.CU.AMT.VAL.DATE` | `ScSettlement_CuAmtValDate` |  |  |  |
| 53 | `SC.SETT.CU.AMT.DEL.REF` | `ScSettlement_CuAmtDelRef` |  |  |  |
| 54 | `SC.SETT.CU.ACC.CCY` | `ScSettlement_CuAccCcy` |  |  |  |
| 55 | `SC.SETT.CU.AMT.ACY` | `ScSettlement_CuAmtAcy` |  |  |  |
| 56 | `SC.SETT.CU.XRATE.ACY` | `ScSettlement_CuXrateAcy` |  |  |  |
| 57 | `SC.SETT.CU.AUTO.SETT` | `ScSettlement_CuAutoSett` |  |  |  |
| 58 | `SC.SETT.CU.NARRATIVE` | `ScSettlement_CuNarrative` |  |  |  |
| 59 | `SC.SETT.CU.MC.RESERVED1` | `ScSettlement_CuMcReserved1` |  |  |  |
| 60 | `SC.SETT.BW.AMT.SETTLED` | `ScSettlement_BwAmtSettled` |  |  |  |
| 61 | `SC.SETT.BW.AMT.OUTSTAND` | `ScSettlement_BwAmtOutstand` |  |  |  |
| 62 | `SC.SETT.BW.AMT.REC.PAID` | `ScSettlement_BwAmtRecPaid` |  |  |  |
| 63 | `SC.SETT.BW.REV.AMT` | `ScSettlement_BwRevAmt` |  |  |  |
| 64 | `SC.SETT.BW.AMT.VAL.DT` | `ScSettlement_BwAmtValDt` |  |  |  |
| 65 | `SC.SETT.LT.AMT.SETTLED` | `ScSettlement_LtAmtSettled` |  |  |  |
| 66 | `SC.SETT.LT.AMT.OUTSTAND` | `ScSettlement_LtAmtOutstand` |  |  |  |
| 67 | `SC.SETT.LT.AMT.REC.PAID` | `ScSettlement_LtAmtRecPaid` |  |  |  |
| 68 | `SC.SETT.LT.AMT.REV` | `ScSettlement_LtAmtRev` |  |  |  |
| 69 | `SC.SETT.LT.AMT.VAL.DT` | `ScSettlement_LtAmtValDt` |  |  |  |
| 70 | `SC.SETT.GEN.SETT.DEL` | `ScSettlement_GenSettDel` |  |  |  |
| 71 | `SC.SETT.CU.DEL.REF` | `ScSettlement_CuDelRef` |  |  |  |
| 72 | `SC.SETT.CU.RESERVED3` | `ScSettlement_CuReserved3` |  |  |  |
| 73 | `SC.SETT.CU.RESERVED2` | `ScSettlement_CuReserved2` |  |  |  |
| 74 | `SC.SETT.CU.RESERVED1` | `ScSettlement_CuReserved1` |  |  |  |
| 75 | `SC.SETT.CPTY.LIMIT` | `ScSettlement_CptyLimit` | TField |  | This field indicates whether or not counterparty limit checking is taking place. If this field is set to "YES", then counterparty limit is associated with the first broker and the BR.AMT.OUTSTAND field will be used to update the counterparty limit. Counterparty limit would work with single broker. Validation Rules: |
| 76 | `SC.SETT.CPTY.LIMIT.REF` | `ScSettlement_CptyLimitRef` | TField |  | Holds the limit reference, if this transaction has updated counterparty limit. Validation Rules: |
| 77 | `SC.SETT.SETTLEMENT.DATE` | `ScSettlement_SettlementDate` | TField |  | Picks up the date when the settlement is completed. Validation Rules: Internally generated field. Updated with today's date when settlement is complete. ie when the outstanding nominals and amounts are zero. |
| 78 | `SC.SETT.TRANS.CODE` | `ScSettlement_TransCode` | TField |  | Holds the SC Transaction code of the Customer side. If the Validation Rules: Internally generated field. Obtained from the transaction which has created the particular Will comprise a valid |
| 79 | `SC.SETT.PARENT.TXN.ID` | `ScSettlement_ParentTxnId` | TField |  | The value to this field is populated from the field PARENT.TXN.ID of SECURITY.TRANSFER record. This field is a no-input field and is updated only for those transaction that come from REPO. Validation Rules: No input, Updated from Security Transfer record |
| 80 | `SC.SETT.THREAD.KEY` | `ScSettlement_ThreadKey` | TField |  | Shows the service agent reference from which the transaction originated. |
| 81 | `SC.SETT.PARENT` | `ScSettlement_Parent` | TField |  |  |
| 82 | `SC.SETT.PARENT.REFERENCE` | `ScSettlement_ParentReference` | TField |  |  |
| 83 | `SC.SETT.FAILED.SETT.DATE` | `ScSettlement_FailedSettDate` |  |  |  |
| 84 | `SC.SETT.EOD.ACCOUNTING` | `ScSettlement_EodAccounting` | TField |  | This field will be used to indicate that the settlement will be done only during End of Day processing. This will be updated if EOD.ACCOUNTING is YES in CUSTOMER.SECURITY/STOCK.EXCHANGE when the transaction was created. No Input field |
| 85 | `SC.SETT.NEW.VALUE.DATE` | `ScSettlement_NewValueDate` | TField |  | This field will hold the next working day whenever settlement is suspended during COB. System updated field which will be cycled further on each settlement suspension and this will continue till the transaction is settled. This field will be used for reports and advices. No Input field |
| 86 | `SC.SETT.SETT.STATUS` | `ScSettlement_SettStatus` |  |  |  |
| 87 | `SC.SETT.SETT.REASON` | `ScSettlement_SettReason` |  |  |  |
| 88 | `SC.SETT.APPLICATION` | `ScSettlement_Application` | TField |  |  |
| 89 | `SC.SETT.EAM.ID` | `ScSettlement_EamId` | TField |  |  |
| 90 | `SC.SETT.GEN.EAM.SETT.DEL` | `ScSettlement_GenEamSettDel` | TField |  | Specifies whether MT544-547 Confirmation advice should be generated for External asset manager. Defaulted from CUSTOMER.SECURITY record, which can be overwritten at transaction level Validation Rules Accepted Values:Yes or Blank |
| 91 | `SC.SETT.EAM.DELIVERY.REF` | `ScSettlement_EamDeliveryRef` | TField |  | Delivery reference for the outgoing MT544 to MT547 messages generated for External Asset Manager |
| 92 | `SC.SETT.PSET` | `ScSettlement_Pset` | TField |  | This field will be defaulted from SEC.TRADE and show the Place of settlement |
| 93 | `SC.SETT.GEN.NARRATIVE` | `ScSettlement_GenNarrative` |  |  |  |
| 94 | `SC.SETT.ADDL.INFO` | `ScSettlement_AddlInfo` |  |  |  |
| 95 | `SC.SETT.LINKED.SETT.REF` | `ScSettlement_LinkedSettRef` | TField |  | Updated when an another application controls the SC.SETTLEMENT . Currently , updated for Settlement records of Trades linked to SP.NET.SETTLEMENT. |
| 96 | `SC.SETT.PARTIAL.SETTLED` | `ScSettlement_PartialSettled` | TField |  | When MT548 with 22F tag value PARS/PAIN is received, this field will be set as YES and shown in Escalations under Partial Settlement heading. When MT548 with 22F tag value PARS/PARC is received, this field will be set as NO.FURTHER.SETTLEMENT and will be shown as potential failure under partial settlement heading. NoInput field |
| 97 | `SC.SETT.RESERVED.09` | `ScSettlement_Reserved09` |  |  |  |
| 98 | `SC.SETT.RESERVED.08` | `ScSettlement_Reserved08` |  |  |  |
| 99 | `SC.SETT.RESERVED.07` | `ScSettlement_Reserved07` |  |  |  |
| 100 | `SC.SETT.RESERVED.06` | `ScSettlement_Reserved06` | TField |  |  |
| 101 | `SC.SETT.RESERVED.05` | `ScSettlement_Reserved05` | TField |  |  |
| 102 | `SC.SETT.RESERVED.04` | `ScSettlement_Reserved04` | TField |  |  |
| 103 | `SC.SETT.RESERVED.03` | `ScSettlement_Reserved03` | TField |  |  |
| 104 | `SC.SETT.RESERVED.02` | `ScSettlement_Reserved02` | TField |  |  |
| 105 | `SC.SETT.RESERVED.01` | `ScSettlement_Reserved01` | TField |  |  |
| 106 | `SC.SETT.LOCAL.REF` | `ScSettlement_LocalRef` |  |  |  |
| 107 | `SC.SETT.STATEMENT.NOS` | `ScSettlement_StatementNos` |  |  |  |
| 108 | `SC.SETT.OVERRIDE` | `ScSettlement_Override` |  |  |  |
| 109 | `SC.SETT.RECORD.STATUS` | `ScSettlement_RecordStatus` | String |  |  |
| 110 | `SC.SETT.CURR.NO` | `ScSettlement_CurrNo` | String |  |  |
| 111 | `SC.SETT.INPUTTER` | `ScSettlement_Inputter` |  |  |  |
| 112 | `SC.SETT.DATE.TIME` | `ScSettlement_DateTime` |  |  |  |
| 113 | `SC.SETT.AUTHORISER` | `ScSettlement_Authoriser` | String |  |  |
| 114 | `SC.SETT.CO.CODE` | `ScSettlement_CoCode` | String |  |  |
| 115 | `SC.SETT.DEPT.CODE` | `ScSettlement_DeptCode` | String |  |  |
| 116 | `SC.SETT.AUDITOR.CODE` | `ScSettlement_AuditorCode` | String |  |  |
| 117 | `SC.SETT.AUDIT.DATE.TIME` | `ScSettlement_AuditDateTime` | String |  |  |
