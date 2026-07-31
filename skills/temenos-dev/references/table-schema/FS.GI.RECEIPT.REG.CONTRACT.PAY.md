# FS.GI.RECEIPT.REG.CONTRACT.PAY — Table Schema

> Source: `INSERTS/I_F.FS.GI.RECEIPT.REG.CONTRACT.PAY` in `FS_Receipt.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.COLLECTION.ACCOUNT.GROUP` | `FsGiReceiptRegContractPay_CollectionAccountGroup` |  |  |  |
| 2 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RECORD.TYPE` | `FsGiReceiptRegContractPay_RecordType` |  |  |  |
| 3 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.VALUE.DATE` | `FsGiReceiptRegContractPay_ValueDate` |  |  |  |
| 4 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.DEAL.REFERENCE` | `FsGiReceiptRegContractPay_DealReference` |  |  |  |
| 5 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.AGENT.ID` | `FsGiReceiptRegContractPay_AgentId` |  |  |  |
| 6 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.FUND.PROMOTER.ID` | `FsGiReceiptRegContractPay_FundPromoterId` |  |  |  |
| 7 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.FUND.ID` | `FsGiReceiptRegContractPay_FundId` |  |  |  |
| 8 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.SHARE.CLASS.CODE` | `FsGiReceiptRegContractPay_ShareClassCode` |  |  |  |
| 9 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.PROCESS.ID` | `FsGiReceiptRegContractPay_ProcessId` |  |  |  |
| 10 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.DEAL.TYPE` | `FsGiReceiptRegContractPay_DealType` |  |  |  |
| 11 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.SETTLEMENT.TYPE` | `FsGiReceiptRegContractPay_SettlementType` |  |  |  |
| 12 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.TYPE.OF.PAYMENT` | `FsGiReceiptRegContractPay_TypeOfPayment` |  |  |  |
| 13 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.REGISTER.ID` | `FsGiReceiptRegContractPay_RegisterId` |  |  |  |
| 14 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.OPERATION.CODE` | `FsGiReceiptRegContractPay_OperationCode` |  |  |  |
| 15 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.SETTLEMENT.MONEY.CODE` | `FsGiReceiptRegContractPay_SettlementMoneyCode` |  |  |  |
| 16 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.FINAL.AMOUNT` | `FsGiReceiptRegContractPay_FinalAmount` |  |  |  |
| 17 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.FINAL.PAYMENT.ID` | `FsGiReceiptRegContractPay_FinalPaymentId` |  |  |  |
| 18 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.MATCH.GROUP.ID` | `FsGiReceiptRegContractPay_MatchGroupId` |  |  |  |
| 19 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.PREVIOUS.MATCH.ID` | `FsGiReceiptRegContractPay_PreviousMatchId` |  |  |  |
| 20 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.CHILD.RECEIPT.MATCH.GROUP.ID` | `FsGiReceiptRegContractPay_ChildReceiptMatchGroupId` |  |  |  |
| 21 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.MEMO` | `FsGiReceiptRegContractPay_Memo` |  |  |  |
| 22 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.PARTIAL.SETTLEMENT.ID` | `FsGiReceiptRegContractPay_PartialSettlementId` |  |  |  |
| 23 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.OUTSTANDING.AMOUNT` | `FsGiReceiptRegContractPay_OutstandingAmount` |  |  |  |
| 24 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.PAY.DATE` | `FsGiReceiptRegContractPay_PayDate` |  |  |  |
| 25 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.ORDER.AMOUNT.MATCH` | `FsGiReceiptRegContractPay_OrderAmountMatch` |  |  |  |
| 26 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.TRADE.DATE` | `FsGiReceiptRegContractPay_TradeDate` |  |  |  |
| 27 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.PAYMENT.TYPE` | `FsGiReceiptRegContractPay_PaymentType` |  |  |  |
| 28 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.CONTRACT.ID` | `FsGiReceiptRegContractPay_ContractId` |  |  |  |
| 29 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RECEIPT.FLAG` | `FsGiReceiptRegContractPay_ReceiptFlag` |  |  |  |
| 30 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.APPLICATION.CURRENCY` | `FsGiReceiptRegContractPay_ApplicationCurrency` |  |  |  |
| 31 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.INSTRUCTION.ID` | `FsGiReceiptRegContractPay_InstructionId` |  |  |  |
| 32 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.PAYMENT.DATE.AND.TIME` | `FsGiReceiptRegContractPay_PaymentDateAndTime` |  |  |  |
| 33 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.IN.DEAL.REFERENCE` | `FsGiReceiptRegContractPay_InDealReference` |  |  |  |
| 34 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.SEQUENCE.NUMBER` | `FsGiReceiptRegContractPay_SequenceNumber` |  |  |  |
| 35 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.SETTLED.QUANTITY` | `FsGiReceiptRegContractPay_SettledQuantity` |  |  |  |
| 36 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.AMOUNT.APPLICATION.CURRENCY` | `FsGiReceiptRegContractPay_AmountApplicationCurrency` |  |  |  |
| 37 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.SEQUENCE.ID` | `FsGiReceiptRegContractPay_SequenceId` |  |  |  |
| 38 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.ORDER.ID` | `FsGiReceiptRegContractPay_OrderId` |  |  |  |
| 39 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.NOTIONAL.FX` | `FsGiReceiptRegContractPay_NotionalFx` |  |  |  |
| 40 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.INVESTOR.AMOUNT.PAY.CCY` | `FsGiReceiptRegContractPay_InvestorAmountPayCcy` |  |  |  |
| 41 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.MIGRATED.FLAG` | `FsGiReceiptRegContractPay_MigratedFlag` |  |  |  |
| 42 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.CHILD.RECEIPT.AMOUNT` | `FsGiReceiptRegContractPay_ChildReceiptAmount` |  |  |  |
| 43 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.DB.CR` | `FsGiReceiptRegContractPay_DbCr` |  |  |  |
| 44 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.AMOUNT.DROPPED` | `FsGiReceiptRegContractPay_AmountDropped` |  |  |  |
| 45 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.EFFECTIVE.AMOUNT` | `FsGiReceiptRegContractPay_EffectiveAmount` |  |  |  |
| 46 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.LEGAL.ENTITY.ID` | `FsGiReceiptRegContractPay_LegalEntityId` |  |  |  |
| 47 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.EXCHANGE.GROUP` | `FsGiReceiptRegContractPay_ExchangeGroup` |  |  |  |
| 48 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.PAYMENT.ID` | `FsGiReceiptRegContractPay_PaymentId` |  |  |  |
| 49 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.PRODUCT.CODE` | `FsGiReceiptRegContractPay_ProductCode` |  |  |  |
| 50 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.LEG.LINK` | `FsGiReceiptRegContractPay_LegLink` |  |  |  |
| 51 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.PAYMENT.STATUS` | `FsGiReceiptRegContractPay_PaymentStatus` |  |  |  |
| 52 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.CONTRACT.STATUS` | `FsGiReceiptRegContractPay_ContractStatus` |  |  |  |
| 53 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.ORDER.VALUE.DATE` | `FsGiReceiptRegContractPay_OrderValueDate` |  |  |  |
| 54 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.ORDER.TRADE.DATE` | `FsGiReceiptRegContractPay_OrderTradeDate` |  |  |  |
| 55 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.GLOBAL.REGISTER.ID` | `FsGiReceiptRegContractPay_GlobalRegisterId` |  |  |  |
| 56 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.CONTRACT.AMOUNT` | `FsGiReceiptRegContractPay_ContractAmount` |  |  |  |
| 57 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.LATE.PAYMENT.INTEREST` | `FsGiReceiptRegContractPay_LatePaymentInterest` |  |  |  |
| 58 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.CONTRACT.CURRENCY` | `FsGiReceiptRegContractPay_ContractCurrency` |  |  |  |
| 59 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RESERVED10` | `FsGiReceiptRegContractPay_Reserved10` |  |  |  |
| 60 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RESERVED9` | `FsGiReceiptRegContractPay_Reserved9` |  |  |  |
| 61 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RESERVED8` | `FsGiReceiptRegContractPay_Reserved8` |  |  |  |
| 62 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RESERVED7` | `FsGiReceiptRegContractPay_Reserved7` |  |  |  |
| 63 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RESERVED6` | `FsGiReceiptRegContractPay_Reserved6` |  |  |  |
| 64 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RESERVED5` | `FsGiReceiptRegContractPay_Reserved5` |  |  |  |
| 65 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RESERVED4` | `FsGiReceiptRegContractPay_Reserved4` |  |  |  |
| 66 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RESERVED3` | `FsGiReceiptRegContractPay_Reserved3` |  |  |  |
| 67 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RESERVED2` | `FsGiReceiptRegContractPay_Reserved2` |  |  |  |
| 68 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RESERVED1` | `FsGiReceiptRegContractPay_Reserved1` |  |  |  |
| 69 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.LOCAL.REF` | `FsGiReceiptRegContractPay_LocalRef` |  |  |  |
| 70 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.OVERRIDE` | `FsGiReceiptRegContractPay_Override` |  |  |  |
| 71 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.RECORD.STATUS` | `FsGiReceiptRegContractPay_RecordStatus` |  |  |  |
| 72 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.CURR.NO` | `FsGiReceiptRegContractPay_CurrNo` |  |  |  |
| 73 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.INPUTTER` | `FsGiReceiptRegContractPay_Inputter` |  |  |  |
| 74 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.DATE.TIME` | `FsGiReceiptRegContractPay_DateTime` |  |  |  |
| 75 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.AUTHORISER` | `FsGiReceiptRegContractPay_Authoriser` |  |  |  |
| 76 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.CO.CODE` | `FsGiReceiptRegContractPay_CoCode` |  |  |  |
| 77 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.DEPT.CODE` | `FsGiReceiptRegContractPay_DeptCode` |  |  |  |
| 78 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.AUDITOR.CODE` | `FsGiReceiptRegContractPay_AuditorCode` |  |  |  |
| 79 | `FS.GI.RECEIPT.REG.CONTRACT.PAY.AUDIT.DATE.TIME` | `FsGiReceiptRegContractPay_AuditDateTime` |  |  |  |
