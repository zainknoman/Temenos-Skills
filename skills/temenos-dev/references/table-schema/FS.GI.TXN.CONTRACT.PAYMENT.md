# FS.GI.TXN.CONTRACT.PAYMENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.CONTRACT.PAYMENT` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.CONTRACT.PAYMENT.PARENT.REF.ID` | `FsGiTxnContractPayment_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.CONTRACT.PAYMENT.ORA.ROWID` | `FsGiTxnContractPayment_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.CONTRACT.PAYMENT.ORDER.ID` | `FsGiTxnContractPayment_OrderId` | TField |  | Order identification number. Multifonds DB Column is NORDER. |
| 4 | `FS.GI.TXN.CONTRACT.PAYMENT.AGENT.ID` | `FsGiTxnContractPayment_AgentId` | TField |  | Agent internal ID. Multifonds DB Column is NOUTLET. |
| 5 | `FS.GI.TXN.CONTRACT.PAYMENT.DEAL.REFERENCE` | `FsGiTxnContractPayment_DealReference` | TField |  | Unique internal reference that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF. |
| 6 | `FS.GI.TXN.CONTRACT.PAYMENT.PARTIAL.SETTLEMENT.ID` | `FsGiTxnContractPayment_PartialSettlementId` | TField |  | Partial settlement ID applied to the child deal. Multifonds DB Column is PART_SETT_ID. |
| 7 | `FS.GI.TXN.CONTRACT.PAYMENT.PAYMENT.DATE` | `FsGiTxnContractPayment_PaymentDate` | TField |  | Payment date of the settlement Multifonds DB Column is DATE_PAY. |
| 8 | `FS.GI.TXN.CONTRACT.PAYMENT.TRADE.DATE` | `FsGiTxnContractPayment_TradeDate` | TField |  | Trade date on which NAV is applied for the order. Multifonds DB Column is DOPER. |
| 9 | `FS.GI.TXN.CONTRACT.PAYMENT.VALUE.DATE` | `FsGiTxnContractPayment_ValueDate` | TField |  | Value date of the order. Multifonds DB Column is DVALEUR. |
| 10 | `FS.GI.TXN.CONTRACT.PAYMENT.EFFECTIVE.AMOUNT` | `FsGiTxnContractPayment_EffectiveAmount` | TField |  | Effective amount paid by the investor if this one is different from the original amount in the order. System will then update the field &quot;Amount&quot; in the order screen. Multifonds DB Column is MNT_EFFECTIVE. |
| 11 | `FS.GI.TXN.CONTRACT.PAYMENT.SETTLEMENT.MONEY.CODE` | `FsGiTxnContractPayment_SettlementMoneyCode` | TField |  | Settlement money option defined at Agent commission structure leve. It will be updateable only for the main payment record. Once specified, it will be copied to the subsequent payments and will not be updateable by the user. Multifonds DB Column is CSETTLE_MONEY. |
| 12 | `FS.GI.TXN.CONTRACT.PAYMENT.IN.DEAL.REFERENCE` | `FsGiTxnContractPayment_InDealReference` | TField |  | Unique internal reference for two-leg orders that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF_IN. |
| 13 | `FS.GI.TXN.CONTRACT.PAYMENT.PAYMENT.TYPE` | `FsGiTxnContractPayment_PaymentType` | TField |  | Payment Type of the payment instruction. For example, Appro Payment Type (Internal Fund Movement) and Expro Payment Type (External Fund Movement). Multifonds DB Column is PAY_TYPE. |
| 14 | `FS.GI.TXN.CONTRACT.PAYMENT.GLOBAL.REGISTER.ID` | `FsGiTxnContractPayment_GlobalRegisterId` | TField |  | Global register internal ID. Multifonds DB Column is NREGISTER_GLOBAL. |
| 15 | `FS.GI.TXN.CONTRACT.PAYMENT.REGISTER.ID` | `FsGiTxnContractPayment_RegisterId` | TField |  | Register internal ID. Multifonds DB Column is NREGISTER. |
| 16 | `FS.GI.TXN.CONTRACT.PAYMENT.EXCHANGE.GROUP` | `FsGiTxnContractPayment_ExchangeGroup` | TField |  | The exchange rate group code used for the cash flow forecast report at the simulation level, fund exchange forex and for the swift EOD level. Multifonds DB Column is CGROUPE_COURS. |
| 17 | `FS.GI.TXN.CONTRACT.PAYMENT.FUND.PROMOTER.ID` | `FsGiTxnContractPayment_FundPromoterId` | TField |  | Fund Promoter internal ID. Multifonds DB Column is NPROMOTER. |
| 18 | `FS.GI.TXN.CONTRACT.PAYMENT.LEGAL.ENTITY.ID` | `FsGiTxnContractPayment_LegalEntityId` | TField |  | Legal entity internal ID. Multifonds DB Column is NTFC. |
| 19 | `FS.GI.TXN.CONTRACT.PAYMENT.PRODUCT.CODE` | `FsGiTxnContractPayment_ProductCode` | TField |  | Product internal ID. Multifonds DB Column is NPROD. |
| 20 | `FS.GI.TXN.CONTRACT.PAYMENT.TA.FUND.ID` | `FsGiTxnContractPayment_TaFundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 21 | `FS.GI.TXN.CONTRACT.PAYMENT.SHARE.CLASS.CODE` | `FsGiTxnContractPayment_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 22 | `FS.GI.TXN.CONTRACT.PAYMENT.OPERATION.CODE` | `FsGiTxnContractPayment_OperationCode` | TField |  | Type of operation performed such as subscription, redemption, switch, transfer etc. Multifonds DB Column is COPERATION. |
| 23 | `FS.GI.TXN.CONTRACT.PAYMENT.CONTRACT.ID` | `FsGiTxnContractPayment_ContractId` | TField |  | Unique contract number generated by system. Multifonds DB Column is NCONTRACT. |
| 24 | `FS.GI.TXN.CONTRACT.PAYMENT.PAYMENT.STATUS` | `FsGiTxnContractPayment_PaymentStatus` | TField |  | Payment status. Multifonds DB Column is STATUS_PAY. |
| 25 | `FS.GI.TXN.CONTRACT.PAYMENT.CONTRACT.STATUS` | `FsGiTxnContractPayment_ContractStatus` | TField |  | Contract status. Multifonds DB Column is STATUS_CONTRACT. |
| 26 | `FS.GI.TXN.CONTRACT.PAYMENT.DB.CR` | `FsGiTxnContractPayment_DbCr` | TField |  | Credit or Debit transaction type. Multifonds DB Column is CSENS. |
| 27 | `FS.GI.TXN.CONTRACT.PAYMENT.ORDER.TRADE.DATE` | `FsGiTxnContractPayment_OrderTradeDate` | TField |  | Order trade date. Multifonds DB Column is ORDER_DOPER. |
| 28 | `FS.GI.TXN.CONTRACT.PAYMENT.ORDER.VALUE.DATE` | `FsGiTxnContractPayment_OrderValueDate` | TField |  | Order value date. Multifonds DB Column is ORDER_DVALEUR. |
| 29 | `FS.GI.TXN.CONTRACT.PAYMENT.PAYMENT.DATE.AND.TIME` | `FsGiTxnContractPayment_PaymentDateAndTime` | TField |  | Date and time when payment is processed. Multifonds DB Column is PAY_DATE_TIME. |
| 30 | `FS.GI.TXN.CONTRACT.PAYMENT.CONTRACT.CURRENCY` | `FsGiTxnContractPayment_ContractCurrency` | TField |  | Contract currency code. Multifonds DB Column is CMON_CONTRACT. |
| 31 | `FS.GI.TXN.CONTRACT.PAYMENT.CONTRACT.AMOUNT` | `FsGiTxnContractPayment_ContractAmount` | TField |  | Contract amount. Multifonds DB Column is MNT_CONTRACT. |
| 32 | `FS.GI.TXN.CONTRACT.PAYMENT.LATE.PAYMENT.INTEREST` | `FsGiTxnContractPayment_LatePaymentInterest` | TField |  | Late payment interest from the a Late payment interesta field in the contract note. Updated after batching of the order. Multifonds DB Column is LATE_PYMT_INT. |
| 33 | `FS.GI.TXN.CONTRACT.PAYMENT.AMOUNT.DROPPED` | `FsGiTxnContractPayment_AmountDropped` | TField |  | Populated in case the difference between the outstanding amount and the received amount is less than the defined threshold for TA Fund. Multifonds DB Column is MNT_DROPPED. |
| 34 | `FS.GI.TXN.CONTRACT.PAYMENT.LEG.LINK` | `FsGiTxnContractPayment_LegLink` | TField |  | Automatically populated leg link ID for switch / transfer orders. Multifonds DB Column is LEG_LINK. |
| 35 | `FS.GI.TXN.CONTRACT.PAYMENT.RECEIPT.FLAG` | `FsGiTxnContractPayment_ReceiptFlag` | TField |  | Flag to indicate the deal is linked/matched in the cash matching module. Multifonds DB Column is FLG_RECEIPT. |
| 36 | `FS.GI.TXN.CONTRACT.PAYMENT.DEAL.TYPE` | `FsGiTxnContractPayment_DealType` | TField |  | Deal type code for cash handling. Multifonds DB Column is TYPE_DEAL. |
| 37 | `FS.GI.TXN.CONTRACT.PAYMENT.OUTSTANDING.AMOUNT` | `FsGiTxnContractPayment_OutstandingAmount` | TField |  | Outstanding amount. Multifonds DB Column is OUTSTANDING_AMT. |
| 38 | `FS.GI.TXN.CONTRACT.PAYMENT.CHILD.RECEIPT.MATCH.GROUP.ID` | `FsGiTxnContractPayment_ChildReceiptMatchGroupId` | TField |  | Match group ID generated when a child receipt is matched. Multifonds DB Column is CHILD_MATCH_GROUP_ID. |
| 39 | `FS.GI.TXN.CONTRACT.PAYMENT.CHILD.RECEIPT.AMOUNT` | `FsGiTxnContractPayment_ChildReceiptAmount` | TField |  | Amount of child receipt created. Multifonds DB Column is CHILD_RECP_AMT. |
| 40 | `FS.GI.TXN.CONTRACT.PAYMENT.PREVIOUS.MATCH.ID` | `FsGiTxnContractPayment_PreviousMatchId` | TField |  | Previous receipts match group ID. Multifonds DB Column is PREVIOUS_MATCH_ID. |
| 41 | `FS.GI.TXN.CONTRACT.PAYMENT.COLLECTION.ACCOUNT.GROUP` | `FsGiTxnContractPayment_CollectionAccountGroup` | TField |  | Collection account group code used to group deals and receipts that can be matched together. Multifonds DB Column is COLL_ACC_GRP. |
| 42 | `FS.GI.TXN.CONTRACT.PAYMENT.MATCH.GROUP.ID` | `FsGiTxnContractPayment_MatchGroupId` | TField |  | Receipts match group ID. Multifonds DB Column is MATCH_GROUP_ID. |
| 43 | `FS.GI.TXN.CONTRACT.PAYMENT.EFFECTIVE.AMOUNT.QUOT.CCY` | `FsGiTxnContractPayment_EffectiveAmountQuotCcy` | TField |  | Effective amount in quotation currency. Multifonds DB Column is MNT_EFFECTIVE_QUOT. |
| 44 | `FS.GI.TXN.CONTRACT.PAYMENT.INVESTOR.AMOUNT.PAY.CCY` | `FsGiTxnContractPayment_InvestorAmountPayCcy` | TField |  | Net amount as shown in the settlement currency. Multifonds DB Column is MNT_PAY. |
| 45 | `FS.GI.TXN.CONTRACT.PAYMENT.SEQUENCE.NUMBER` | `FsGiTxnContractPayment_SequenceNumber` | TField |  | Sequence number assigned by system. Multifonds DB Column is SEQUENCE_NUMBER. |
| 46 | `FS.GI.TXN.CONTRACT.PAYMENT.SETTLED.QUANTITY` | `FsGiTxnContractPayment_SettledQuantity` | TField |  | Settled quantity of the order. Multifonds DB Column is QTY_SETTLED. |
| 47 | `FS.GI.TXN.CONTRACT.PAYMENT.PAYMENT.ID.INTERNAL` | `FsGiTxnContractPayment_PaymentIdInternal` | TField |  | Internal payment id. Multifonds DB Column is NPAY. |
| 48 | `FS.GI.TXN.CONTRACT.PAYMENT.ORDER.AMOUNT.MATCH` | `FsGiTxnContractPayment_OrderAmountMatch` | TField |  | Type of set up for order amount matching. Multifonds DB Column is ORDER_AMT_MATCH. |
| 49 | `FS.GI.TXN.CONTRACT.PAYMENT.MEMO` | `FsGiTxnContractPayment_Memo` | TField |  | Free text to enter message. Multifonds DB Column is MEMO. |
| 50 | `FS.GI.TXN.CONTRACT.PAYMENT.MIGRATED.FLAG` | `FsGiTxnContractPayment_MigratedFlag` | TField |  | Migrated flag to indiciate the dividend payment has been imported into payment management for the processing. Multifonds DB Column is MIG_FLAG. |
| 51 | `FS.GI.TXN.CONTRACT.PAYMENT.AMOUNT.IN.APP.CCY` | `FsGiTxnContractPayment_AmountInAppCcy` | TField |  | Amount in application currency. Multifonds DB Column is AMOUNT_APP_CCY. |
| 52 | `FS.GI.TXN.CONTRACT.PAYMENT.APPLICATION.CURRENCY` | `FsGiTxnContractPayment_ApplicationCurrency` | TField |  | Application currency. Multifonds DB Column is APP_CCY. |
| 53 | `FS.GI.TXN.CONTRACT.PAYMENT.NOTIONAL.FX` | `FsGiTxnContractPayment_NotionalFx` | TField |  | Notional FX rate. Multifonds DB Column is NOTIONAL_FX. |
| 54 | `FS.GI.TXN.CONTRACT.PAYMENT.FINAL.AMOUNT` | `FsGiTxnContractPayment_FinalAmount` | TField |  | Final amount. Multifonds DB Column is FINAL_AMOUNT. |
| 55 | `FS.GI.TXN.CONTRACT.PAYMENT.FINAL.PAYMENT.ID` | `FsGiTxnContractPayment_FinalPaymentId` | TField |  | Final payment ID. Multifonds DB Column is FINAL_PAYM_ID. |
| 56 | `FS.GI.TXN.CONTRACT.PAYMENT.FUND.ID` | `FsGiTxnContractPayment_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 57 | `FS.GI.TXN.CONTRACT.PAYMENT.CLASS.CURRENCY` | `FsGiTxnContractPayment_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 58 | `FS.GI.TXN.CONTRACT.PAYMENT.RESERVED10` | `FsGiTxnContractPayment_Reserved10` | TField |  |  |
| 59 | `FS.GI.TXN.CONTRACT.PAYMENT.RESERVED9` | `FsGiTxnContractPayment_Reserved9` | TField |  |  |
| 60 | `FS.GI.TXN.CONTRACT.PAYMENT.RESERVED8` | `FsGiTxnContractPayment_Reserved8` | TField |  |  |
| 61 | `FS.GI.TXN.CONTRACT.PAYMENT.RESERVED7` | `FsGiTxnContractPayment_Reserved7` | TField |  |  |
| 62 | `FS.GI.TXN.CONTRACT.PAYMENT.RESERVED6` | `FsGiTxnContractPayment_Reserved6` | TField |  |  |
| 63 | `FS.GI.TXN.CONTRACT.PAYMENT.RESERVED5` | `FsGiTxnContractPayment_Reserved5` | TField |  |  |
| 64 | `FS.GI.TXN.CONTRACT.PAYMENT.RESERVED4` | `FsGiTxnContractPayment_Reserved4` | TField |  |  |
| 65 | `FS.GI.TXN.CONTRACT.PAYMENT.RESERVED3` | `FsGiTxnContractPayment_Reserved3` | TField |  |  |
| 66 | `FS.GI.TXN.CONTRACT.PAYMENT.RESERVED2` | `FsGiTxnContractPayment_Reserved2` | TField |  |  |
| 67 | `FS.GI.TXN.CONTRACT.PAYMENT.RESERVED1` | `FsGiTxnContractPayment_Reserved1` | TField |  |  |
| 68 | `FS.GI.TXN.CONTRACT.PAYMENT.LOCAL.REF` | `FsGiTxnContractPayment_LocalRef` |  |  |  |
| 69 | `FS.GI.TXN.CONTRACT.PAYMENT.OVERRIDE` | `FsGiTxnContractPayment_Override` |  |  |  |
| 70 | `FS.GI.TXN.CONTRACT.PAYMENT.RECORD.STATUS` | `FsGiTxnContractPayment_RecordStatus` | String |  |  |
| 71 | `FS.GI.TXN.CONTRACT.PAYMENT.CURR.NO` | `FsGiTxnContractPayment_CurrNo` | String |  |  |
| 72 | `FS.GI.TXN.CONTRACT.PAYMENT.INPUTTER` | `FsGiTxnContractPayment_Inputter` |  |  |  |
| 73 | `FS.GI.TXN.CONTRACT.PAYMENT.DATE.TIME` | `FsGiTxnContractPayment_DateTime` |  |  |  |
| 74 | `FS.GI.TXN.CONTRACT.PAYMENT.AUTHORISER` | `FsGiTxnContractPayment_Authoriser` | String |  |  |
| 75 | `FS.GI.TXN.CONTRACT.PAYMENT.CO.CODE` | `FsGiTxnContractPayment_CoCode` | String |  |  |
| 76 | `FS.GI.TXN.CONTRACT.PAYMENT.DEPT.CODE` | `FsGiTxnContractPayment_DeptCode` | String |  |  |
| 77 | `FS.GI.TXN.CONTRACT.PAYMENT.AUDITOR.CODE` | `FsGiTxnContractPayment_AuditorCode` | String |  |  |
| 78 | `FS.GI.TXN.CONTRACT.PAYMENT.AUDIT.DATE.TIME` | `FsGiTxnContractPayment_AuditDateTime` | String |  |  |
