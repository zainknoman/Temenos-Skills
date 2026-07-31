# FS.GI.TXN.PRE.ORDER — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.PRE.ORDER` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.PRE.ORDER.PARENT.REF.ID` | `FsGiTxnPreOrder_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.PRE.ORDER.ORA.ROWID` | `FsGiTxnPreOrder_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.PRE.ORDER.ORIG.EXTERNAL.ORDER.ID` | `FsGiTxnPreOrder_OrigExternalOrderId` | TField |  | Original external order reference filled in case the original order reference flag is ticked at application level and the original order reference is displayed in the order interface. Multifonds DB Column is ORIGINAL_NORDER_EXTERN. |
| 4 | `FS.GI.TXN.PRE.ORDER.ORDER.EXTERNAL.ID` | `FsGiTxnPreOrder_OrderExternalId` | TField |  | External order ID. Multifonds DB Column is NORDER_EXTERN. |
| 5 | `FS.GI.TXN.PRE.ORDER.PRE.ORDER.FLAG` | `FsGiTxnPreOrder_PreOrderFlag` | TField |  | Flag to specify that the order is pre-order. Multifonds DB Column is PRE_ORDER. |
| 6 | `FS.GI.TXN.PRE.ORDER.CORRECTION.FLAG` | `FsGiTxnPreOrder_CorrectionFlag` | TField |  | Flag to specify this order is a correction deal. Multifonds DB Column is FLG_CORR. |
| 7 | `FS.GI.TXN.PRE.ORDER.NO.CASH.FLAG` | `FsGiTxnPreOrder_NoCashFlag` | TField |  | Flag to specify that there is no cash movements associated with the order. Multifonds DB Column is FLG_NO_CASH. |
| 8 | `FS.GI.TXN.PRE.ORDER.INTERNAL.CASH.FLAG` | `FsGiTxnPreOrder_InternalCashFlag` | TField |  | Flag to specify there is internal cash movement related to this transaction. Multifonds DB Column is FLG_INT_CASH. |
| 9 | `FS.GI.TXN.PRE.ORDER.RECEPTION.DATE.TIME` | `FsGiTxnPreOrder_ReceptionDateTime` |  |  |  |
| 10 | `FS.GI.TXN.PRE.ORDER.DEALING.REGISTER.ID` | `FsGiTxnPreOrder_DealingRegisterId` | TField |  | Dealing register ID. If the main register is a global register, dealing register will be a bearer register dealing for the global register. Multifonds DB Column is NREGISTER_DEAL. |
| 11 | `FS.GI.TXN.PRE.ORDER.REGISTER.ID` | `FsGiTxnPreOrder_RegisterId` | TField |  | Register for which the pre-order is placed. Multifonds DB Column is NREGISTER. |
| 12 | `FS.GI.TXN.PRE.ORDER.AGENT.ID` | `FsGiTxnPreOrder_AgentId` | TField |  | AgentA linked to the pre-order. Multifonds DB Column is NOUTLET. |
| 13 | `FS.GI.TXN.PRE.ORDER.OPERATION.CODE` | `FsGiTxnPreOrder_OperationCode` | TField |  | Type of operation performed such as subscription, redemption, switch, transfer etc. Multifonds DB Column is COPERATION. |
| 14 | `FS.GI.TXN.PRE.ORDER.FUND.ID` | `FsGiTxnPreOrder_FundId` | TField |  | Fund in which the pre-order is placed. Multifonds DB Column is NPTF. |
| 15 | `FS.GI.TXN.PRE.ORDER.PROVIDER.ID` | `FsGiTxnPreOrder_ProviderId` | TField |  | Organisation supplying the security Id. Multifonds DB Column is PROVID. |
| 16 | `FS.GI.TXN.PRE.ORDER.LEGAL.ENTITY.ID` | `FsGiTxnPreOrder_LegalEntityId` | TField |  | Legal Entity linked to the pre-order. Multifonds DB Column is NTFC. |
| 17 | `FS.GI.TXN.PRE.ORDER.SHARE.CLASS.CODE` | `FsGiTxnPreOrder_ShareClassCode` | TField |  | Fund share class in which the pre-order is placed. Multifonds DB Column is TPART. |
| 18 | `FS.GI.TXN.PRE.ORDER.SOS.CLASS.CODE` | `FsGiTxnPreOrder_SosClassCode` | TField |  | Share class code for series of shares funds. Allowed values are from the list of codes defined in MFGI. Multifonds DB Column is TPART_SOS. |
| 19 | `FS.GI.TXN.PRE.ORDER.IN.FUND.ID` | `FsGiTxnPreOrder_InFundId` | TField |  | Destination Fund ID in a two-leg order. Multifonds DB Column is NPTF2. |
| 20 | `FS.GI.TXN.PRE.ORDER.PROVIDER.ID.2` | `FsGiTxnPreOrder_ProviderId2` | TField |  | Organisation supplying the security Id for two leg transactions. Multifonds DB Column is PROVID2. |
| 21 | `FS.GI.TXN.PRE.ORDER.IN.LEGAL.ENTITY.ID` | `FsGiTxnPreOrder_InLegalEntityId` | TField |  | Destination Legal Entity ID in a two-leg order. Multifonds DB Column is NTFC2. |
| 22 | `FS.GI.TXN.PRE.ORDER.IN.SHARE.CLASS` | `FsGiTxnPreOrder_InShareClass` | TField |  | Destination fund share class in a two-leg order. Multifonds DB Column is TPART2. |
| 23 | `FS.GI.TXN.PRE.ORDER.SOS.IN.CLASS.CODE` | `FsGiTxnPreOrder_SosInClassCode` | TField |  | Share class code for series of shares funds for two-leg transactions. Allowed values are from the list of codes defined in MFGI. Multifonds DB Column is TPART_SOS2. |
| 24 | `FS.GI.TXN.PRE.ORDER.DEALING.REGISTER.ID.2` | `FsGiTxnPreOrder_DealingRegisterId2` | TField |  | Dealing register ID for two leg transactions. If the main register is a global register, dealing register will be a bearer register dealing for the global register. Multifonds DB Column is NREGISTER_DEAL2. |
| 25 | `FS.GI.TXN.PRE.ORDER.IN.REGISTER.ID` | `FsGiTxnPreOrder_InRegisterId` | TField |  | Destination register ID in a two-leg order. Multifonds DB Column is NREGISTER2. |
| 26 | `FS.GI.TXN.PRE.ORDER.FULL.REDEMPTION.FLAG` | `FsGiTxnPreOrder_FullRedemptionFlag` | TField |  | Flag to redeem complete register positions. Multifonds DB Column is FLAG_ALL. |
| 27 | `FS.GI.TXN.PRE.ORDER.REGISTER.TYPE` | `FsGiTxnPreOrder_RegisterType` | TField |  | Register type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_REG. |
| 28 | `FS.GI.TXN.PRE.ORDER.SETTLEMENT.TYPE` | `FsGiTxnPreOrder_SettlementType` | TField |  | Settlement type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_SETTLEMENT. |
| 29 | `FS.GI.TXN.PRE.ORDER.DEAL.TYPE` | `FsGiTxnPreOrder_DealType` | TField |  | Deal type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_DEAL. |
| 30 | `FS.GI.TXN.PRE.ORDER.ORDER.STATUS` | `FsGiTxnPreOrder_OrderStatus` | TField |  | Transaction status indicating whether the pre-order is in initial status, validated, deleted, cancelled etc. Multifonds DB Column is STATUS. |
| 31 | `FS.GI.TXN.PRE.ORDER.DEAL.STATUS` | `FsGiTxnPreOrder_DealStatus` | TField |  | Deal status of the order based on cash handling setup. Multifonds DB Column is DEAL_STATUS. |
| 32 | `FS.GI.TXN.PRE.ORDER.ORDER.TRADE.DATE` | `FsGiTxnPreOrder_OrderTradeDate` | TField |  | Trade Date (in DD/MM/YYYY format) of the pre-order. Multifonds DB Column is DATE_EXE. |
| 33 | `FS.GI.TXN.PRE.ORDER.VALUE.DATE` | `FsGiTxnPreOrder_ValueDate` | TField |  | Fund settlement date for the order. Multifonds DB Column is DVALEUR. |
| 34 | `FS.GI.TXN.PRE.ORDER.SIMULATION.DATE` | `FsGiTxnPreOrder_SimulationDate` | TField |  | Date on which simulation will be processed for the order. Multifonds DB Column is SEND_TFC_DATE. |
| 35 | `FS.GI.TXN.PRE.ORDER.AMOUNT` | `FsGiTxnPreOrder_Amount` | TField | Yes | Pre-order Amount. This field is mandatory if quantity field is left blank. Multifonds DB Column is AMOUNT. |
| 36 | `FS.GI.TXN.PRE.ORDER.QUANTITY` | `FsGiTxnPreOrder_Quantity` | TField | Yes | Pre-order quantity. This field is mandatory if amount field is left blank. Multifonds DB Column is QUANTITY. |
| 37 | `FS.GI.TXN.PRE.ORDER.PAYMENT.CURRENCY` | `FsGiTxnPreOrder_PaymentCurrency` | TField |  | The currency (in 3 letter ISO code, Eg: EUR) in which the payments will be processed for this order. Multifonds DB Column is CMON. |
| 38 | `FS.GI.TXN.PRE.ORDER.PAYMENT.TYPE` | `FsGiTxnPreOrder_PaymentType` | TField |  | Type of payment for the transaction. Multifonds DB Column is TYPE_PAYMENT. |
| 39 | `FS.GI.TXN.PRE.ORDER.CUSTODY.SETTLEMENT` | `FsGiTxnPreOrder_CustodySettlement` | TField |  | Custody settlement type populated based on data defined in the register main screen. Multifonds DB Column is CDEF_DELIV. |
| 40 | `FS.GI.TXN.PRE.ORDER.SWITCH.PCT` | `FsGiTxnPreOrder_SwitchPct` | TField |  | Switch percentage of the order. Multifonds DB Column is SPLIT_PERCENT. |
| 41 | `FS.GI.TXN.PRE.ORDER.INTERNAL.REFERENCE` | `FsGiTxnPreOrder_InternalReference` | TField |  | Unique internal reference for the order. Multifonds DB Column is INTERNAL_REFERENCE. |
| 42 | `FS.GI.TXN.PRE.ORDER.ORDER.TYPE` | `FsGiTxnPreOrder_OrderType` | TField |  | Type of the transaction. For example NAV of the day, backdated, back-value etc. Multifonds DB Column is TYPE_ORDRE. |
| 43 | `FS.GI.TXN.PRE.ORDER.RECEIVED.MODE` | `FsGiTxnPreOrder_ReceivedMode` | TField |  | Mode in which the order instruction is received. Multifonds DB Column is MODE_RECEIVED. |
| 44 | `FS.GI.TXN.PRE.ORDER.INTERFACED.ORDER.FLAG` | `FsGiTxnPreOrder_InterfacedOrderFlag` | TField |  | Flag to specify that the order is loaded through interface. Multifonds DB Column is FLG_INTERFACED_ORDER. |
| 45 | `FS.GI.TXN.PRE.ORDER.CONFIRM.USER` | `FsGiTxnPreOrder_ConfirmUser` | TField |  | User who confirms the order. Multifonds DB Column is USER_CONFIRM. |
| 46 | `FS.GI.TXN.PRE.ORDER.ORDER.ID` | `FsGiTxnPreOrder_OrderId` | TField |  | Pre-order identification number. Multifonds DB Column is NORDER. |
| 47 | `FS.GI.TXN.PRE.ORDER.DEAL.REFERENCE` | `FsGiTxnPreOrder_DealReference` | TField |  | Unique internal reference that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF. |
| 48 | `FS.GI.TXN.PRE.ORDER.IN.DEAL.REFERENCE` | `FsGiTxnPreOrder_InDealReference` | TField |  | Unique internal reference for two-leg orders that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF_IN. |
| 49 | `FS.GI.TXN.PRE.ORDER.LEG.LINK` | `FsGiTxnPreOrder_LegLink` | TField |  | System created ID for switch, transfer, Aller Retour and merge order entries. Multifonds DB Column is LEG_LINK. |
| 50 | `FS.GI.TXN.PRE.ORDER.INSTRUCTION.ID` | `FsGiTxnPreOrder_InstructionId` | TField |  | Pre-order instruction ID. Multifonds DB Column is NINSTRUCTION. |
| 51 | `FS.GI.TXN.PRE.ORDER.LINKED.ORDER.ID` | `FsGiTxnPreOrder_LinkedOrderId` | TField |  | Original order number linked to sub orders created for a single multiple series debit order. Multifonds DB Column is LINKED_NORDER. |
| 52 | `FS.GI.TXN.PRE.ORDER.NAV` | `FsGiTxnPreOrder_Nav` | TField |  | NAV price applicable for the order. Multifonds DB Column is NAV_PRICE. |
| 53 | `FS.GI.TXN.PRE.ORDER.FORCED.PRICE.FLAG` | `FsGiTxnPreOrder_ForcedPriceFlag` | TField |  | Forced NAV price to be applied for the order. Multifonds DB Column is FORCE_PRICE. |
| 54 | `FS.GI.TXN.PRE.ORDER.FORCED.IN.PRICE.FLAG` | `FsGiTxnPreOrder_ForcedInPriceFlag` | TField |  | Forced NAV price to be applied for the two-leg order. Multifonds DB Column is FORCE_PRICE_IN. |
| 55 | `FS.GI.TXN.PRE.ORDER.EST.NAV.FLAG` | `FsGiTxnPreOrder_EstNavFlag` | TField |  | Flag indicates whether the transaction should consider the Estimated NAV during the Partial Client trading desk process. Multifonds DB Column is ESTI_NAV. |
| 56 | `FS.GI.TXN.PRE.ORDER.EST.NAV` | `FsGiTxnPreOrder_EstNav` | TField |  | Estimated NAV price which is picked from the share price historical screen whenever the Estimated NAV flag at the order level is ticked. Multifonds DB Column is ESTI_NAV_PRICE. |
| 57 | `FS.GI.TXN.PRE.ORDER.IN.NAV` | `FsGiTxnPreOrder_InNav` | TField |  | NAV applicable for the two-leg order. Multifonds DB Column is NAV_PRICE_IN. |
| 58 | `FS.GI.TXN.PRE.ORDER.COMM.EXCEPT.PCT` | `FsGiTxnPreOrder_CommExceptPct` | TField |  | Order commission exception percentage. Multifonds DB Column is EXCEPT_PCT. |
| 59 | `FS.GI.TXN.PRE.ORDER.COMM.EXCEPT.AMOUNT` | `FsGiTxnPreOrder_CommExceptAmount` | TField |  | Order commission exception amount. Multifonds DB Column is MNT_COM_EXCEPT. |
| 60 | `FS.GI.TXN.PRE.ORDER.DISTRIB.COMM.PCT` | `FsGiTxnPreOrder_DistribCommPct` | TField |  | Percentage of distributed commission. Multifonds DB Column is PCT_COM_DISTRIB. |
| 61 | `FS.GI.TXN.PRE.ORDER.TA.COMM.PCT` | `FsGiTxnPreOrder_TaCommPct` | TField |  | Transfer agent commission percentage. Multifonds DB Column is TA_PCT. |
| 62 | `FS.GI.TXN.PRE.ORDER.COMMISSION.DISCLOSURE.CODE` | `FsGiTxnPreOrder_CommissionDisclosureCode` | TField |  | Commission disclosure code. Multifonds DB Column is COMM_DISCLOSURE. |
| 63 | `FS.GI.TXN.PRE.ORDER.COMM.ON.TOP.FLAG` | `FsGiTxnPreOrder_CommOnTopFlag` | TField |  | Commission on top flag. Multifonds DB Column is FLG_TOP_COMM. |
| 64 | `FS.GI.TXN.PRE.ORDER.MGMT.COMM` | `FsGiTxnPreOrder_MgmtComm` | TField |  | Management commission amount for the order. Multifonds DB Column is MGMT_COMM. |
| 65 | `FS.GI.TXN.PRE.ORDER.COMM.EXCEPT.IN.PCT` | `FsGiTxnPreOrder_CommExceptInPct` | TField |  | Order commission exception percentage for two-leg order. Multifonds DB Column is EXCEPT_PCT_IN. |
| 66 | `FS.GI.TXN.PRE.ORDER.AMOUNT.EXCEPT.IN.AMT` | `FsGiTxnPreOrder_AmountExceptInAmt` | TField |  | Order commission exception amount for two-leg order. Multifonds DB Column is MNT_COM_EXCEPT_IN. |
| 67 | `FS.GI.TXN.PRE.ORDER.DISTRIB.COMM.IN.PCT` | `FsGiTxnPreOrder_DistribCommInPct` | TField |  | Order distributed commission percentage for two-leg order. Multifonds DB Column is PCT_COM_DISTRIB_IN. |
| 68 | `FS.GI.TXN.PRE.ORDER.TA.COMM.IN.PCT` | `FsGiTxnPreOrder_TaCommInPct` | TField |  | Trasnsfer agent commission percentage for two-leg order. Multifonds DB Column is TA_PCT_IN. |
| 69 | `FS.GI.TXN.PRE.ORDER.AGENT.COMM.DISC.SCALE.CODE` | `FsGiTxnPreOrder_AgentCommDiscScaleCode` | TField |  | Agent commission discount scale code. Multifonds DB Column is CSCALE_NDISCOUNT. |
| 70 | `FS.GI.TXN.PRE.ORDER.WAIVER.COMM.SCALE.CODE` | `FsGiTxnPreOrder_WaiverCommScaleCode` | TField |  | Waiver commission percentage scale used when the commission or penalty type &apos;Dual pricing Method&apos; is chosen. Multifonds DB Column is CSCALE_NCOMM_WAIVER. |
| 71 | `FS.GI.TXN.PRE.ORDER.INIT.CHARGE.PCT` | `FsGiTxnPreOrder_InitChargePct` | TField |  | Order initial charge for two-leg order. Multifonds DB Column is NINIT_CHRG_IN. |
| 72 | `FS.GI.TXN.PRE.ORDER.DISCOUNT.IN.AMT` | `FsGiTxnPreOrder_DiscountInAmt` | TField |  | Order discount for two-leg order. Multifonds DB Column is NDISCOUNT_IN. |
| 73 | `FS.GI.TXN.PRE.ORDER.DISCOUNT.IN.SCALE.CODE` | `FsGiTxnPreOrder_DiscountInScaleCode` | TField |  | Order discount scale for two-leg order. Multifonds DB Column is CSCALE_NDISCOUNT_IN. |
| 74 | `FS.GI.TXN.PRE.ORDER.WAIVER.COMM.IN.PCT` | `FsGiTxnPreOrder_WaiverCommInPct` | TField |  | Order waiver commission rate for in leg. Multifonds DB Column is NCOMM_WAIVER_IN. |
| 75 | `FS.GI.TXN.PRE.ORDER.WAIVER.COMM.IN.SCALE.CODE` | `FsGiTxnPreOrder_WaiverCommInScaleCode` | TField |  | Order waiver commission scale for in leg. Multifonds DB Column is CSCALE_WAIVER_IN. |
| 76 | `FS.GI.TXN.PRE.ORDER.FORCED.COMM.PAY.CCY.FLG` | `FsGiTxnPreOrder_ForcedCommPayCcyFlg` | TField |  | Order forced commission amount in payment currency. Multifonds DB Column is FLG_PAY_CCY_OUT. |
| 77 | `FS.GI.TXN.PRE.ORDER.FORCED.COMM.IN.PAY.CCY.FLG` | `FsGiTxnPreOrder_ForcedCommInPayCcyFlg` | TField |  | Order forced commission amount in payment currency for two-leg order. Multifonds DB Column is FLG_PAY_CCY_IN. |
| 78 | `FS.GI.TXN.PRE.ORDER.COMM.ARRANGEMENT.ID` | `FsGiTxnPreOrder_CommArrangementId` | TField |  | Order commission arrangement identification code. Multifonds DB Column is NARRANGE. |
| 79 | `FS.GI.TXN.PRE.ORDER.INITIAL.CHARGE` | `FsGiTxnPreOrder_InitialCharge` | TField |  | Initial commission charge percentage at Order level. This can not be greater than the maximum % allowed by the fund. Multifonds DB Column is NINIT_CHRG. |
| 80 | `FS.GI.TXN.PRE.ORDER.COMMISSION.WAIVER` | `FsGiTxnPreOrder_CommissionWaiver` | TField |  | Commission Waiver Amount. Multifonds DB Column is NCOMM_WAIVER. |
| 81 | `FS.GI.TXN.PRE.ORDER.COMMISSION.DISCOUNT` | `FsGiTxnPreOrder_CommissionDiscount` | TField |  | Discount percentage agreed by fund for dual pricing functionality. Multifonds DB Column is NDISCOUNT. |
| 82 | `FS.GI.TXN.PRE.ORDER.FX.RATE` | `FsGiTxnPreOrder_FxRate` | TField |  | Derived default FX rate. Multifonds DB Column is TAUX. |
| 83 | `FS.GI.TXN.PRE.ORDER.APPLIED.FX.RATE` | `FsGiTxnPreOrder_AppliedFxRate` | TField |  | FX rate applicable for the pre-order. Multifonds DB Column is TAUX_USER. |
| 84 | `FS.GI.TXN.PRE.ORDER.APPLIED.FX.INDICATOR` | `FsGiTxnPreOrder_AppliedFxIndicator` | TField |  | Field indicating the application of FX rate is to divide or multiply. Multifonds DB Column is RATE_INDICATOR. |
| 85 | `FS.GI.TXN.PRE.ORDER.CANC.FX.PL.AMOUNT` | `FsGiTxnPreOrder_CancFxPlAmount` | TField |  | Profit or loss for amount in share class currency for cancelled orders, calculated during client trading desk procesing. Multifonds DB Column is FX_PL_CALC_CANC. |
| 86 | `FS.GI.TXN.PRE.ORDER.TISR` | `FsGiTxnPreOrder_Tisr` | TField |  | Taxable Income per Share Rate applicable for the order. Multifonds DB Column is TISR. |
| 87 | `FS.GI.TXN.PRE.ORDER.US.TAX.FLAG` | `FsGiTxnPreOrder_UsTaxFlag` | TField |  | Flag to indicaten that US Tax is applicable for the order. Multifonds DB Column is FLG_USTAX. |
| 88 | `FS.GI.TXN.PRE.ORDER.SWEDISH.TAX.FLAG` | `FsGiTxnPreOrder_SwedishTaxFlag` | TField |  | Flag to indicaten that Swedish Tax is applicable for the order. Multifonds DB Column is FLG_SWEDISH_TAX. |
| 89 | `FS.GI.TXN.PRE.ORDER.IE.FINANCE.ACT.TAX` | `FsGiTxnPreOrder_IeFinanceActTax` | TField |  | The flag specifies Irish tax applicable on the order. Multifonds DB Column is IE_FIN_ACT_TAXATION. |
| 90 | `FS.GI.TXN.PRE.ORDER.PARTIAL.SETTLEMENT.PCT` | `FsGiTxnPreOrder_PartialSettlementPct` | TField |  | Partial settlement percentage. Multifonds DB Column is PART_SETT_PCT. |
| 91 | `FS.GI.TXN.PRE.ORDER.PART.SETTLEMENT.DATE` | `FsGiTxnPreOrder_PartSettlementDate` | TField |  | Partial settlement date. Multifonds DB Column is SETT_DATE. |
| 92 | `FS.GI.TXN.PRE.ORDER.HOLD.PAYMENT.FLAG` | `FsGiTxnPreOrder_HoldPaymentFlag` | TField |  | Flag to specify payments related to this order should be kept on hold. Multifonds DB Column is FLG_HOLD_PYM. |
| 93 | `FS.GI.TXN.PRE.ORDER.PARTIAL.PAYMENT.FLAG` | `FsGiTxnPreOrder_PartialPaymentFlag` | TField |  | Flag indicates that the transaction follows the new partial payment functionality at the transaction level. Multifonds DB Column is FLG_PART_PAY. |
| 94 | `FS.GI.TXN.PRE.ORDER.PART.AMT.PAY.CCY` | `FsGiTxnPreOrder_PartAmtPayCcy` | TField |  | Partial payment amount in payment currency. Multifonds DB Column is PART_PAY_AMT. |
| 95 | `FS.GI.TXN.PRE.ORDER.REGISTER.BANK.ID` | `FsGiTxnPreOrder_RegisterBankId` | TField |  | Bank ID of the register. Multifonds DB Column is REG_BANK. |
| 96 | `FS.GI.TXN.PRE.ORDER.REGISTER.BANK.ACCOUNT` | `FsGiTxnPreOrder_RegisterBankAccount` | TField |  | Bank Account number of the register. Multifonds DB Column is REG_BANK_ACCOUNT. |
| 97 | `FS.GI.TXN.PRE.ORDER.REGISTER.BANK.HOLDER` | `FsGiTxnPreOrder_RegisterBankHolder` | TField |  | Name of the bank account holder. Multifonds DB Column is REG_BANK_HOLDER. |
| 98 | `FS.GI.TXN.PRE.ORDER.DB.BANK.ID` | `FsGiTxnPreOrder_DbBankId` | TField |  | Bank ID to be debitted for payments related to this order. Multifonds DB Column is REG_BANK_DB. |
| 99 | `FS.GI.TXN.PRE.ORDER.DB.BANK.ACCOUNT` | `FsGiTxnPreOrder_DbBankAccount` | TField |  | Bank account number to be debitted for payments related to this order. Multifonds DB Column is REG_BANK_DB_ACC. |
| 100 | `FS.GI.TXN.PRE.ORDER.ADL.DEFAULT.RATE` | `FsGiTxnPreOrder_AdlDefaultRate` | TField |  | ADL default rate for the order. Multifonds DB Column is ADL_RATE. |
| 101 | `FS.GI.TXN.PRE.ORDER.ADL.AMOUNT` | `FsGiTxnPreOrder_AdlAmount` | TField |  | ADL amount for the order. Multifonds DB Column is ADL_AMOUNT. |
| 102 | `FS.GI.TXN.PRE.ORDER.EXCL.ADL.FROM.AMT.FLG` | `FsGiTxnPreOrder_ExclAdlFromAmtFlg` | TField |  | Flag to indicate that Anti Dilution Levy (ADL) is excluded from order amount. Multifonds DB Column is FLG_TOP_ADL. |
| 103 | `FS.GI.TXN.PRE.ORDER.DAILY.DIV.PAYMENT.TYPE` | `FsGiTxnPreOrder_DailyDivPaymentType` | TField |  | Dailyn dividend payment method. Multifonds DB Column is DLYDIV_PAYMTHD. |
| 104 | `FS.GI.TXN.PRE.ORDER.ACCRUED.DIV.AMOUNT` | `FsGiTxnPreOrder_AccruedDivAmount` | TField |  | Accrued dividend amount for this order. Multifonds DB Column is ACCRUAL_DIV. |
| 105 | `FS.GI.TXN.PRE.ORDER.TRANSACTION.CHARGE` | `FsGiTxnPreOrder_TransactionCharge` | TField |  | Transaction charge applicable for UK module. Multifonds DB Column is NTRANS_CHARG. |
| 106 | `FS.GI.TXN.PRE.ORDER.BOX.NUMBER` | `FsGiTxnPreOrder_BoxNumber` | TField |  | Box number to which the confirmed orders will be added for Box management. Multifonds DB Column is NBOX. |
| 107 | `FS.GI.TXN.PRE.ORDER.VAL.POINT.CUT.OFF` | `FsGiTxnPreOrder_ValPointCutOff` | TField |  | Valuation point cut-off as parameterized in the MF fund calendar screen. Multifonds DB Column is DVP_CUT. |
| 108 | `FS.GI.TXN.PRE.ORDER.DILUTION.LEVY.PCT` | `FsGiTxnPreOrder_DilutionLevyPct` | TField |  | Dilution levy percentage applicable for the order. Multifonds DB Column is NDIL_LEVY. |
| 109 | `FS.GI.TXN.PRE.ORDER.INTEREST.DUE.AMOUNT` | `FsGiTxnPreOrder_InterestDueAmount` | TField |  | Order interest due amount. Multifonds DB Column is NINT_DUE_AMT. |
| 110 | `FS.GI.TXN.PRE.ORDER.TAX.INT.ADJ.AMOUNT` | `FsGiTxnPreOrder_TaxIntAdjAmount` | TField |  | Tax interest adjustments amount. Multifonds DB Column is NTAX_INT. |
| 111 | `FS.GI.TXN.PRE.ORDER.TAX.CREDIT.ADJ.AMOUNT` | `FsGiTxnPreOrder_TaxCreditAdjAmount` | TField |  | Tax credit adjustments amount. Multifonds DB Column is NTAX_CREDIT. |
| 112 | `FS.GI.TXN.PRE.ORDER.IN.BOX.NUMBER` | `FsGiTxnPreOrder_InBoxNumber` | TField |  | Box number In for two-leg order. Multifonds DB Column is NBOX_IN. |
| 113 | `FS.GI.TXN.PRE.ORDER.INHERIT.G1.G2.FLAG` | `FsGiTxnPreOrder_InheritG1G2Flag` | TField |  | Flag to trigger inheritance of Group 1 and Group 2 Units following a Switch / Conversion. Multifonds DB Column is FLG_INHERIT_G1G2. |
| 114 | `FS.GI.TXN.PRE.ORDER.LOI.AMOUNT` | `FsGiTxnPreOrder_LoiAmount` | TField |  | Lettler of intent amount. Multifonds DB Column is LOI_AMOUNT. |
| 115 | `FS.GI.TXN.PRE.ORDER.MULTI.SERIES.FLAG` | `FsGiTxnPreOrder_MultiSeriesFlag` | TField |  | Flag to activate the option to place a debit order across multiple series. Multifonds DB Column is FLG_MULTI_SERIES. |
| 116 | `FS.GI.TXN.PRE.ORDER.EQ.CR.AMOUNT` | `FsGiTxnPreOrder_EqCrAmount` | TField |  | Order equalisation credit. Multifonds DB Column is EQUAL_CR. |
| 117 | `FS.GI.TXN.PRE.ORDER.EQ.DB.AMOUNT` | `FsGiTxnPreOrder_EqDbAmount` | TField |  | Order equalisation debit. Multifonds DB Column is EQUAL_DB. |
| 118 | `FS.GI.TXN.PRE.ORDER.REVISED.CUMUL.REL.PERF` | `FsGiTxnPreOrder_RevisedCumulRelPerf` | TField |  | Revised cumulative relative performance amount. Multifonds DB Column is REVISED_CRP. |
| 119 | `FS.GI.TXN.PRE.ORDER.REVISED.HWM` | `FsGiTxnPreOrder_RevisedHwm` | TField |  | Revised high water mark value for performance fees calculation. Multifonds DB Column is REVISED_HWM. |
| 120 | `FS.GI.TXN.PRE.ORDER.REVISED.GAV` | `FsGiTxnPreOrder_RevisedGav` | TField |  | Revised Gross Asset Value amount. Multifonds DB Column is REVISED_GAV. |
| 121 | `FS.GI.TXN.PRE.ORDER.NON.CRYST.PF.FLAG` | `FsGiTxnPreOrder_NonCrystPfFlag` | TField |  | Non crystallization perfomance fee flag of the order. Multifonds DB Column is FLG_NC_PF. |
| 122 | `FS.GI.TXN.PRE.ORDER.KIID.FLAG` | `FsGiTxnPreOrder_KiidFlag` | TField |  | Flag to specify TA KIID compliance. Multifonds DB Column is FLG_KIID. |
| 123 | `FS.GI.TXN.PRE.ORDER.GLOBAL.ORDERING.FLAG` | `FsGiTxnPreOrder_GlobalOrderingFlag` | TField |  | Flag to have the order in scope of the global ordering functionality. Multifonds DB Column is FLG_GLOBAL_ORD. |
| 124 | `FS.GI.TXN.PRE.ORDER.TRANSACTION.BULKING.NETTING` | `FsGiTxnPreOrder_TransactionBulkingNetting` | TField |  | Type of bulking or netting applied to this transaction. Multifonds DB Column is TRNS_BULK_NET. |
| 125 | `FS.GI.TXN.PRE.ORDER.EXTERNAL.TA.ID` | `FsGiTxnPreOrder_ExternalTaId` | TField |  | External TA for global ordering. Multifonds DB Column is EXTERNAL_TA. |
| 126 | `FS.GI.TXN.PRE.ORDER.TECHNICAL.REGISTER.ID` | `FsGiTxnPreOrder_TechnicalRegisterId` | TField |  | Cash dividend or reinvestment register from client level. Multifonds DB Column is NREGISTER_TECH. |
| 127 | `FS.GI.TXN.PRE.ORDER.TECHNICAL.IN.REGISTER.ID` | `FsGiTxnPreOrder_TechnicalInRegisterId` | TField |  | Cash dividend or reinvestment register from client level for two-leg order. Multifonds DB Column is NREGISTER_TECH_IN. |
| 128 | `FS.GI.TXN.PRE.ORDER.SENDING.METHOD` | `FsGiTxnPreOrder_SendingMethod` | TField |  | Sending method populated only if the flag a Global orderinga is ticked at order level. Multifonds DB Column is SENDING_MTHD. |
| 129 | `FS.GI.TXN.PRE.ORDER.SENDING.IN.METHOD` | `FsGiTxnPreOrder_SendingInMethod` | TField |  | Sending method for two-leg order populated only if the flag a Global orderinga is ticked at order level. Multifonds DB Column is SENDING_MTHD_IN. |
| 130 | `FS.GI.TXN.PRE.ORDER.CAPITAL.PCT` | `FsGiTxnPreOrder_CapitalPct` | TField |  | Percentage of the capital that the partner wants to withdraw for limited partnerships. Multifonds DB Column is CAPITAL_PCT. |
| 131 | `FS.GI.TXN.PRE.ORDER.CLOSING.FLAG` | `FsGiTxnPreOrder_ClosingFlag` | TField |  | Flag to indicate that the order is a closing order placed at the end of a break period. Multifonds DB Column is FLG_CLOSING. |
| 132 | `FS.GI.TXN.PRE.ORDER.CHANGE.BENEF.OWNER.FLG` | `FsGiTxnPreOrder_ChangeBenefOwnerFlg` | TField |  | Flag to indicate change of beneficial owner. Multifonds DB Column is FLG_CHG_BENEFICIAL. |
| 133 | `FS.GI.TXN.PRE.ORDER.PROCESS.ID` | `FsGiTxnPreOrder_ProcessId` | TField |  | Order process ID. Multifonds DB Column is NPROCESS. |
| 134 | `FS.GI.TXN.PRE.ORDER.PROXY.ID` | `FsGiTxnPreOrder_ProxyId` | TField |  | External proxy ID for joint account registers. Multifonds DB Column is PROXY. |
| 135 | `FS.GI.TXN.PRE.ORDER.ACCOUNT.REFERENCE` | `FsGiTxnPreOrder_AccountReference` | TField |  | Client identification reference, e.g. passport number. Multifonds DB Column is ID_NO. |
| 136 | `FS.GI.TXN.PRE.ORDER.BIRTH.DATE` | `FsGiTxnPreOrder_BirthDate` | TField |  | Date of birth of the Proxy of the register. Multifonds DB Column is DATE_NAIS. |
| 137 | `FS.GI.TXN.PRE.ORDER.DESCRIPTION` | `FsGiTxnPreOrder_Description` | TField |  | Free text to enter an order description. Multifonds DB Column is DESCRIPTION. |
| 138 | `FS.GI.TXN.PRE.ORDER.ORDER.LIMIT.CONDITION` | `FsGiTxnPreOrder_OrderLimitCondition` | TField |  | Order limit Condition ID. Multifonds DB Column is NCONDITION. |
| 139 | `FS.GI.TXN.PRE.ORDER.CHANGED.ALL.POS.FLAG` | `FsGiTxnPreOrder_ChangedAllPosFlag` | TField |  | Flag to indicate that complete register positions will be redeemed. Multifonds DB Column is CHANGED_ALL_POS. |
| 140 | `FS.GI.TXN.PRE.ORDER.TAX.ID.COMMENT` | `FsGiTxnPreOrder_TaxIdComment` | TField |  | Free text field to mention any comments relating to this order. Multifonds DB Column is COMMENTS. |
| 141 | `FS.GI.TXN.PRE.ORDER.PRODUCT.CODE` | `FsGiTxnPreOrder_ProductCode` | TField |  | Retail product ID for the order. Multifonds DB Column is NPROD. |
| 142 | `FS.GI.TXN.PRE.ORDER.REMAINING.QUANTITY` | `FsGiTxnPreOrder_RemainingQuantity` | TField |  | Order remaining quantity. Multifonds DB Column is NREMAIN_QTY. |
| 143 | `FS.GI.TXN.PRE.ORDER.SETTLEMENT.MONEY.CODE` | `FsGiTxnPreOrder_SettlementMoneyCode` | TField |  | Settlement of money for saving plan and/or subscription transaction. Multifonds DB Column is CSETTLE_MONEY. |
| 144 | `FS.GI.TXN.PRE.ORDER.WITH.CASH.ACCT.MNGT.FLG` | `FsGiTxnPreOrder_WithCashAcctMngtFlg` | TField |  | Flag to indicate that order is in scope of cash account management. Multifonds DB Column is FLG_CASH_SEC_ORD. |
| 145 | `FS.GI.TXN.PRE.ORDER.SALESMAN.ID` | `FsGiTxnPreOrder_SalesmanId` | TField |  | Salesman ID. Multifonds DB Column is NOUTLET_SMAN. |
| 146 | `FS.GI.TXN.PRE.ORDER.EST.TOTAL.PAY.AMT` | `FsGiTxnPreOrder_EstTotalPayAmt` | TField |  | Estimated total amount to pay. Multifonds DB Column is EST_TOT_AMT_PAY. |
| 147 | `FS.GI.TXN.PRE.ORDER.QUANTITY.ROUNDING.TYPE` | `FsGiTxnPreOrder_QuantityRoundingType` | TField |  | Quantity rounding method. Multifonds DB Column is TYPE_ARRONDI. |
| 148 | `FS.GI.TXN.PRE.ORDER.QUANTITY.DECIMALS` | `FsGiTxnPreOrder_QuantityDecimals` | TField |  | Decimal points applicable for the quantity. Multifonds DB Column is CODE_ARRONDI_QT. |
| 149 | `FS.GI.TXN.PRE.ORDER.FORWARD.DATE` | `FsGiTxnPreOrder_ForwardDate` | TField |  | Flag to indicate a forward dated order. Multifonds DB Column is FLG_FWD_DT. |
| 150 | `FS.GI.TXN.PRE.ORDER.ERISA.WARN.OVERR.FLG` | `FsGiTxnPreOrder_ErisaWarnOverrFlg` | TField |  | Flag to override ERISA warning on threshold percentage. Multifonds DB Column is FLG_ERISA_OVERRIDE. |
| 151 | `FS.GI.TXN.PRE.ORDER.BLOCK.FOR.SETTLE.REASON.FLG` | `FsGiTxnPreOrder_BlockForSettleReasonFlg` | TField |  | Dividend blocked for settlement reason. Multifonds DB Column is FLG_BLK_FOR_SETT_REASON. |
| 152 | `FS.GI.TXN.PRE.ORDER.CLIENT.TRAD.DESK.CODE` | `FsGiTxnPreOrder_ClientTradDeskCode` | TField |  | Client trading desk code used in this order for FX exporting. Multifonds DB Column is CLIENT_TDSK. |
| 153 | `FS.GI.TXN.PRE.ORDER.IN.TRADE.DATE` | `FsGiTxnPreOrder_InTradeDate` | TField |  | Trade date for two-leg order. Multifonds DB Column is DATE_EXE_IN. |
| 154 | `FS.GI.TXN.PRE.ORDER.IN.VALUE.DATE` | `FsGiTxnPreOrder_InValueDate` | TField |  | Value date for two-leg order. Multifonds DB Column is DVALEUR_IN. |
| 155 | `FS.GI.TXN.PRE.ORDER.DOCUMENT.HANDLING` | `FsGiTxnPreOrder_DocumentHandling` | TField |  | Investor correspondence handling code at order level. Multifonds DB Column is DOC_HANDLING. |
| 156 | `FS.GI.TXN.PRE.ORDER.TRUST.RECEIVED.DATE` | `FsGiTxnPreOrder_TrustReceivedDate` | TField |  | Date and time order is received from trusted STP counterparty source. Multifonds DB Column is CUT_OFF_TS. |
| 157 | `FS.GI.TXN.PRE.ORDER.STP.SENDER` | `FsGiTxnPreOrder_StpSender` | TField |  | STP counterparty address. Multifonds DB Column is SENDER_STP. |
| 158 | `FS.GI.TXN.PRE.ORDER.SWIFT.NARRATIVE` | `FsGiTxnPreOrder_SwiftNarrative` | TField |  | Narrative in SWIFT message. Multifonds DB Column is SWIFT_NARRATIVE. |
| 159 | `FS.GI.TXN.PRE.ORDER.EST.AMOUNT.APPLI.CCY` | `FsGiTxnPreOrder_EstAmountAppliCcy` | TField |  | Estimated amount in application currency. Multifonds DB Column is EST_AMT_APP_CCY. |
| 160 | `FS.GI.TXN.PRE.ORDER.INTRUCTION.PROCESS.ID` | `FsGiTxnPreOrder_IntructionProcessId` | TField |  | Instruction batch process ID. Multifonds DB Column is INST_PROCESS_ID. |
| 161 | `FS.GI.TXN.PRE.ORDER.FUND.TRADING.DESK.PROCESS` | `FsGiTxnPreOrder_FundTradingDeskProcess` | TField |  | Fund trading desk process code. Multifonds DB Column is FUND_TDSK_PROC. |
| 162 | `FS.GI.TXN.PRE.ORDER.REGISTER.ACCOUNT.REF` | `FsGiTxnPreOrder_RegisterAccountRef` | TField |  | Register account reference. Multifonds DB Column is REG_ID_NO. |
| 163 | `FS.GI.TXN.PRE.ORDER.REDEEM.LIFO.FLAG` | `FsGiTxnPreOrder_RedeemLifoFlag` | TField |  | Flag to indicate redempotion is in last in first out method. Multifonds DB Column is FLG_RED_LIFO. |
| 164 | `FS.GI.TXN.PRE.ORDER.TRANSACTION.DATE` | `FsGiTxnPreOrder_TransactionDate` | TField |  | Transaction date auto-populated from application date. Multifonds DB Column is TRANS_DATE. |
| 165 | `FS.GI.TXN.PRE.ORDER.GATING.ORDER.ID` | `FsGiTxnPreOrder_GatingOrderId` | TField |  | Gating order number. Multifonds DB Column is NORDER_GATING. |
| 166 | `FS.GI.TXN.PRE.ORDER.PE.RE.COMMENT` | `FsGiTxnPreOrder_PeReComment` | TField |  | PE/RE comment code. Multifonds DB Column is PE_RE_COMMENT. |
| 167 | `FS.GI.TXN.PRE.ORDER.STRUCTURING.FEES.AMT` | `FsGiTxnPreOrder_StructuringFeesAmt` | TField |  | Structuring fees. Multifonds DB Column is STRUCTURE_FEES_AMT. |
| 168 | `FS.GI.TXN.PRE.ORDER.LATE.PAYMENT.INTEREST` | `FsGiTxnPreOrder_LatePaymentInterest` | TField |  | Late payment interest. Multifonds DB Column is LATE_PYMT_INT. |
| 169 | `FS.GI.TXN.PRE.ORDER.REGISTER.ACCOUNT.REF.2` | `FsGiTxnPreOrder_RegisterAccountRef2` | TField |  | Register account reference 2. Multifonds DB Column is REG_ID_NO2. |
| 170 | `FS.GI.TXN.PRE.ORDER.REDEMPTION.AMOUNT` | `FsGiTxnPreOrder_RedemptionAmount` | TField |  | The amount for debit transaction or switch when order is placed in amount and not quantity. Multifonds DB Column is REDMP_AMOUNT. |
| 171 | `FS.GI.TXN.PRE.ORDER.SUBSCRIPTION.QUANTITY` | `FsGiTxnPreOrder_SubscriptionQuantity` | TField |  | The quantity for credit transaction or switch when order is placed in quantity and not amount. Multifonds DB Column is SUB_QUANTITY. |
| 172 | `FS.GI.TXN.PRE.ORDER.REDEMPTION.CONTRACT.ID` | `FsGiTxnPreOrder_RedemptionContractId` | TField |  | Redemption Contract ID used for the operation code &apos;0022&apos;(Export Parts). Multifonds DB Column is REDEMP_NCONTRACT. |
| 173 | `FS.GI.TXN.PRE.ORDER.ORIGINAL.CASH.FLAG` | `FsGiTxnPreOrder_OriginalCashFlag` | TField |  | Original cash. Multifonds DB Column is MIG_ORG_CASH. |
| 174 | `FS.GI.TXN.PRE.ORDER.ADVISED.TRS.FLAG` | `FsGiTxnPreOrder_AdvisedTrsFlag` | TField |  | Advised transaction. Multifonds DB Column is ADVISED_TRN. |
| 175 | `FS.GI.TXN.PRE.ORDER.EXCLUDE.FROM.NET.FLAG` | `FsGiTxnPreOrder_ExcludeFromNetFlag` | TField |  | Flag to exclude order from Swinging Single Price (SSP) Netting. Multifonds DB Column is FLG_EXCL_NET. |
| 176 | `FS.GI.TXN.PRE.ORDER.EXCL.FROM.NET.MVT.FLAG` | `FsGiTxnPreOrder_ExclFromNetMvtFlag` | TField |  | Flag to exclude two-leg order from Swinging Single Price (SSP) Netting. Multifonds DB Column is FLG_EXCL_NET_IN. |
| 177 | `FS.GI.TXN.PRE.ORDER.ROLLOVER.FLG` | `FsGiTxnPreOrder_RolloverFlg` | TField |  | Flag to indicate that order is a rollover of an existing investment. Multifonds DB Column is FLG_ROLLOVER. |
| 178 | `FS.GI.TXN.PRE.ORDER.REJECTED.DATE` | `FsGiTxnPreOrder_RejectedDate` | TField |  | Rejection timestamp. Multifonds DB Column is DREJECTED. |
| 179 | `FS.GI.TXN.PRE.ORDER.REJECTED.USER` | `FsGiTxnPreOrder_RejectedUser` | TField |  | User who has rejected the record. Multifonds DB Column is REJECTED_BY. |
| 180 | `FS.GI.TXN.PRE.ORDER.RELEASED.DATE` | `FsGiTxnPreOrder_ReleasedDate` | TField |  | Released timestamp. Multifonds DB Column is DRELEASED. |
| 181 | `FS.GI.TXN.PRE.ORDER.RELEASED.USER` | `FsGiTxnPreOrder_ReleasedUser` | TField |  | User who has released the record. Multifonds DB Column is RELEASED_BY. |
| 182 | `FS.GI.TXN.PRE.ORDER.BLOCKED.QUANTITY` | `FsGiTxnPreOrder_BlockedQuantity` | TField |  | Blocked quantity for the register and fund. Multifonds DB Column is BLOCKED_QUANTITY. |
| 183 | `FS.GI.TXN.PRE.ORDER.RECEIVED.AMOUNT` | `FsGiTxnPreOrder_ReceivedAmount` | TField |  | Pre-order received amount. Multifonds DB Column is RECIEVED_AMOUNT. |
| 184 | `FS.GI.TXN.PRE.ORDER.CENTRAL.USER` | `FsGiTxnPreOrder_CentralUser` | TField |  | Pre-order central user. Multifonds DB Column is CENTRAL_USER. |
| 185 | `FS.GI.TXN.PRE.ORDER.OUTLET.USER` | `FsGiTxnPreOrder_OutletUser` | TField |  | Pre-order outlet user. Multifonds DB Column is OUTLET_USER. |
| 186 | `FS.GI.TXN.PRE.ORDER.PRINT.FLAG` | `FsGiTxnPreOrder_PrintFlag` | TField |  | Order Print Flag. Multifonds DB Column is FLAG_PRINT. |
| 187 | `FS.GI.TXN.PRE.ORDER.TRADE.DATE` | `FsGiTxnPreOrder_TradeDate` | TField |  | Trade Date on which NAV is to be applied for the order. Multifonds DB Column is DOPER. |
| 188 | `FS.GI.TXN.PRE.ORDER.PAYMENT.STATUS` | `FsGiTxnPreOrder_PaymentStatus` | TField |  | Status of payments related to this order. Multifonds DB Column is PAY_STATUS. |
| 189 | `FS.GI.TXN.PRE.ORDER.PAYMENT.CONFIRM.USER` | `FsGiTxnPreOrder_PaymentConfirmUser` | TField |  | User who confirms the payment. Multifonds DB Column is PAY_CONFIRM. |
| 190 | `FS.GI.TXN.PRE.ORDER.FEES.FLAG` | `FsGiTxnPreOrder_FeesFlag` | TField |  | Order Fees Flag. Multifonds DB Column is FLG_FEES. |
| 191 | `FS.GI.TXN.PRE.ORDER.POR.ORDER.ID` | `FsGiTxnPreOrder_PorOrderId` | TField |  | POR Order ID. Multifonds DB Column is NORDER_POR. |
| 192 | `FS.GI.TXN.PRE.ORDER.REG.ORDER.ID` | `FsGiTxnPreOrder_RegOrderId` | TField |  | Register Order ID Multifonds DB Column is NORDER_REG. |
| 193 | `FS.GI.TXN.PRE.ORDER.FX.TRADING.DESK.FLAG` | `FsGiTxnPreOrder_FxTradingDeskFlag` | TField |  | Flag to identify an order in scope of FX trading desk processing. Multifonds DB Column is FLG_TRADE_DESK. |
| 194 | `FS.GI.TXN.PRE.ORDER.CONFIRM.DATE` | `FsGiTxnPreOrder_ConfirmDate` | TField |  | Pre-order confirmation date. Multifonds DB Column is DATE_CONFIRM. |
| 195 | `FS.GI.TXN.PRE.ORDER.EST.CALC.QUANTITY` | `FsGiTxnPreOrder_EstCalcQuantity` | TField |  | Estimated quantity calculated when an order is placed in amount. Multifonds DB Column is CAL_QUANTITY. |
| 196 | `FS.GI.TXN.PRE.ORDER.APPLIED.FUND.FX.RATE` | `FsGiTxnPreOrder_AppliedFundFxRate` | TField |  | Fund FX rate applicable for the pre-order. Multifonds DB Column is TAUX_USER_NPTF. |
| 197 | `FS.GI.TXN.PRE.ORDER.FUND.RATE.INDICATOR` | `FsGiTxnPreOrder_FundRateIndicator` | TField |  | Field indicating the application of fund FX rate is to divide or multiply. Multifonds DB Column is RATE_INDICATOR_NPTF. |
| 198 | `FS.GI.TXN.PRE.ORDER.APPLIED.FUND.FX.RATE.2` | `FsGiTxnPreOrder_AppliedFundFxRate2` | TField |  | Fund FX rate applicable for two-leg order. Multifonds DB Column is TAUX_USER_NPTF2. |
| 199 | `FS.GI.TXN.PRE.ORDER.FUND.RATE.INDICATOR.2` | `FsGiTxnPreOrder_FundRateIndicator2` | TField |  | Field indicating the application of fund FX rate is to divide or multiply. Multifonds DB Column is RATE_INDICATOR_NPTF2. |
| 200 | `FS.GI.TXN.PRE.ORDER.REDEMPTION.METHOD` | `FsGiTxnPreOrder_RedemptionMethod` | TField |  | Method to select shares to redeem. Linked to group of redemption methods setup for CDSC. Multifonds DB Column is METHOD. |
| 201 | `FS.GI.TXN.PRE.ORDER.CDSC.FLAG` | `FsGiTxnPreOrder_CdscFlag` | TField |  | Flag to indicate that order use condingent deferred sales charge. Multifonds DB Column is USE_CDSC. |
| 202 | `FS.GI.TXN.PRE.ORDER.CDSC.AGENT.ID` | `FsGiTxnPreOrder_CdscAgentId` | TField |  | Prefinancing agent id for CDSC. Multifonds DB Column is NOUTLET_CDSC. |
| 203 | `FS.GI.TXN.PRE.ORDER.FUND.CAT.REST.MARGIN.PCT` | `FsGiTxnPreOrder_FundCatRestMarginPct` | TField |  | Margin percentage used in the investment restriction functionality based on fund category. Multifonds DB Column is MARGIN_PCT. |
| 204 | `FS.GI.TXN.PRE.ORDER.EXTERNAL.ID` | `FsGiTxnPreOrder_ExternalId` | TField |  | Security identifier code. Multifonds DB Column is SECID. |
| 205 | `FS.GI.TXN.PRE.ORDER.EXTERNAL.ID.2` | `FsGiTxnPreOrder_ExternalId2` | TField |  | Security identifier code for two-leg order. Multifonds DB Column is SECID2. |
| 206 | `FS.GI.TXN.PRE.ORDER.CONF.PLUS.USER.FLG` | `FsGiTxnPreOrder_ConfPlusUserFlg` | TField |  | Flag to specify active confirmation plus user is required. Multifonds DB Column is FLG_USER_CONFIRM_PLUS. |
| 207 | `FS.GI.TXN.PRE.ORDER.CONF.PLUS.USER` | `FsGiTxnPreOrder_ConfPlusUser` | TField |  | Active confirmation plus user. Multifonds DB Column is USER_CONFIRM_PLUS. |
| 208 | `FS.GI.TXN.PRE.ORDER.COMM.AGENT.ID` | `FsGiTxnPreOrder_CommAgentId` | TField |  | Commission percentage rate paid to agent or intermediary. Multifonds DB Column is NOUTLET_COMM. |
| 209 | `FS.GI.TXN.PRE.ORDER.COMM.METHOD` | `FsGiTxnPreOrder_CommMethod` | TField |  | Commission method applicable for the order. Multifonds DB Column is COMM_METHOD. |
| 210 | `FS.GI.TXN.PRE.ORDER.UK.REGISTER.TYPE` | `FsGiTxnPreOrder_UkRegisterType` | TField |  | Secondary reg type for UK register. Multifonds DB Column is CREG_TYPE. |
| 211 | `FS.GI.TXN.PRE.ORDER.MARKET.CODE` | `FsGiTxnPreOrder_MarketCode` | TField |  | Order market code. Multifonds DB Column is CMKT_CODE. |
| 212 | `FS.GI.TXN.PRE.ORDER.INSTRUCTION.ID.2` | `FsGiTxnPreOrder_InstructionId2` | TField |  | Order instruction ID for two-leg order. Multifonds DB Column is NINSTRUCTION2. |
| 213 | `FS.GI.TXN.PRE.ORDER.USE.CLIENT.FLAG` | `FsGiTxnPreOrder_UseClientFlag` | TField |  | Use client flag. Multifonds DB Column is FLG_USE_CLI. |
| 214 | `FS.GI.TXN.PRE.ORDER.BOX.STATUS` | `FsGiTxnPreOrder_BoxStatus` | TField |  | Order Box Status. Multifonds DB Column is CBOX_STATUS. |
| 215 | `FS.GI.TXN.PRE.ORDER.ORDER.ALLOC.FLAG` | `FsGiTxnPreOrder_OrderAllocFlag` | TField |  | Asset allocation flag. Multifonds DB Column is CFLG_ALLOC. |
| 216 | `FS.GI.TXN.PRE.ORDER.NORDER.ORG.ID` | `FsGiTxnPreOrder_NorderOrgId` | TField |  | Original Order Number. Multifonds DB Column is NORDER_ORG. |
| 217 | `FS.GI.TXN.PRE.ORDER.SITE.ID` | `FsGiTxnPreOrder_SiteId` | TField |  | Site ID of the order. Multifonds DB Column is SITE_ID. |
| 218 | `FS.GI.TXN.PRE.ORDER.ADL.AMOUNT.PAY.CCY` | `FsGiTxnPreOrder_AdlAmountPayCcy` | TField |  | ADL Amount expressed in payment currency. Multifonds DB Column is ADL_AMOUNT_PAY. |
| 219 | `FS.GI.TXN.PRE.ORDER.SWITCH.ORDER.ID` | `FsGiTxnPreOrder_SwitchOrderId` | TField |  | Order number for switch transaction. Multifonds DB Column is SWITCH_ORDER. |
| 220 | `FS.GI.TXN.PRE.ORDER.NET.AMOUNT` | `FsGiTxnPreOrder_NetAmount` | TField |  | Net amount of the order. Multifonds DB Column is NET_AMOUNT. |
| 221 | `FS.GI.TXN.PRE.ORDER.FLAT.CHARGE.FLAG` | `FsGiTxnPreOrder_FlatChargeFlag` | TField |  | Flag to specify flat charge is applicable for the order. Multifonds DB Column is FLG_FLAT_CHARGE. |
| 222 | `FS.GI.TXN.PRE.ORDER.EXCEPT.MGMT.COMM` | `FsGiTxnPreOrder_ExceptMgmtComm` | TField |  | Exception management commission of the order. Multifonds DB Column is EXCEPT_MGMT_COMM. |
| 223 | `FS.GI.TXN.PRE.ORDER.SPLIT.MANAGER` | `FsGiTxnPreOrder_SplitManager` | TField |  | Split manager of the order. Multifonds DB Column is SPLIT_MANAGER. |
| 224 | `FS.GI.TXN.PRE.ORDER.SPLIT.PCT` | `FsGiTxnPreOrder_SplitPct` | TField |  | Split percentage of the order. Multifonds DB Column is SPLIT_PCT. |
| 225 | `FS.GI.TXN.PRE.ORDER.SPLIT.AMOUNT` | `FsGiTxnPreOrder_SplitAmount` | TField |  | Split amount of the order. Multifonds DB Column is SPLIT_AMOUNT. |
| 226 | `FS.GI.TXN.PRE.ORDER.ASSIGNMENT.STATUS` | `FsGiTxnPreOrder_AssignmentStatus` | TField |  | Order assignment Status. Multifonds DB Column is ASSIGN_STATUS. |
| 227 | `FS.GI.TXN.PRE.ORDER.PRE.ORDER.COMMENT` | `FsGiTxnPreOrder_PreOrderComment` | TField |  | Order comments added at pre-order stage. Multifonds DB Column is PRE_COMMENTS. |
| 228 | `FS.GI.TXN.PRE.ORDER.INTERNAL.REFERENCE.EXT` | `FsGiTxnPreOrder_InternalReferenceExt` | TField |  | Order internal reference extension. Multifonds DB Column is INT_REF_EXTN. |
| 229 | `FS.GI.TXN.PRE.ORDER.REGISTER.IN.BLOCK.CODE` | `FsGiTxnPreOrder_RegisterInBlockCode` | TField |  | Blocking code for register dor two-leg order. Multifonds DB Column is REG_BLK_CODE_IN. |
| 230 | `FS.GI.TXN.PRE.ORDER.CLIENT.IN.BLOCK.CODE` | `FsGiTxnPreOrder_ClientInBlockCode` | TField |  | Blocking code for client for two-leg order. Multifonds DB Column is CLI_BLK_CODE_IN. |
| 231 | `FS.GI.TXN.PRE.ORDER.REGISTER.OUT.BLOCK.CODE` | `FsGiTxnPreOrder_RegisterOutBlockCode` | TField |  | Blocking code for register. Multifonds DB Column is REG_BLK_CODE_OUT. |
| 232 | `FS.GI.TXN.PRE.ORDER.CLIENT.OUT.BLOCK.CODE` | `FsGiTxnPreOrder_ClientOutBlockCode` | TField |  | Blocking code for client. Multifonds DB Column is CLI_BLK_CODE_OUT. |
| 233 | `FS.GI.TXN.PRE.ORDER.INVESTOR.ID` | `FsGiTxnPreOrder_InvestorId` | TField |  | Client ID populated when client is selected at pre-order stage as part of nominee account processing. Multifonds DB Column is NCLIENT. |
| 234 | `FS.GI.TXN.PRE.ORDER.COMM.TYPE` | `FsGiTxnPreOrder_CommType` | TField |  | Commission type applicable for the order. Multifonds DB Column is TYPE_COMM. |
| 235 | `FS.GI.TXN.PRE.ORDER.COMM.IN.TYPE` | `FsGiTxnPreOrder_CommInType` | TField |  | Commission type applicable for the two-leg order. Multifonds DB Column is TYPE_COMM_IN. |
| 236 | `FS.GI.TXN.PRE.ORDER.ORDER.COMM.AMT` | `FsGiTxnPreOrder_OrderCommAmt` | TField |  | Amount or percentage of commission applicable for the order based on commission type setup. Multifonds DB Column is ORD_COMM. |
| 237 | `FS.GI.TXN.PRE.ORDER.ORDER.COMM.IN.AMT` | `FsGiTxnPreOrder_OrderCommInAmt` | TField |  | Amount or percentage of commission applicable for two-leg order based on commission type setup. Multifonds DB Column is ORD_COMM_IN. |
| 238 | `FS.GI.TXN.PRE.ORDER.ORDER.COMM.CCY` | `FsGiTxnPreOrder_OrderCommCcy` | TField |  | Commission currency for the order. Multifonds DB Column is ORD_COMM_CCY. |
| 239 | `FS.GI.TXN.PRE.ORDER.ORDER.COMM.IN.CCY` | `FsGiTxnPreOrder_OrderCommInCcy` | TField |  | Commission currency for two-leg order. Multifonds DB Column is ORD_COMM_CCY_IN. |
| 240 | `FS.GI.TXN.PRE.ORDER.FORCED.COMM.FLAG` | `FsGiTxnPreOrder_ForcedCommFlag` | TField |  | Flag to indicate commission is forced. Multifonds DB Column is FLG_FORCE_COMM. |
| 241 | `FS.GI.TXN.PRE.ORDER.AGENT.COMM.PCT` | `FsGiTxnPreOrder_AgentCommPct` | TField |  | Agent commission percentage. Multifonds DB Column is OUTLET_TUC_PCT. |
| 242 | `FS.GI.TXN.PRE.ORDER.AGENT.COMM.SCALE.CODE` | `FsGiTxnPreOrder_AgentCommScaleCode` | TField |  | Agent commission scale code required for commission type &apos;Scale&apos;. Multifonds DB Column is CSCALE_OUTLET_COMM. |
| 243 | `FS.GI.TXN.PRE.ORDER.AGENT.COMM.IN.PCT` | `FsGiTxnPreOrder_AgentCommInPct` | TField |  | Agent commission percentage for two-leg oder. Multifonds DB Column is OUTLET_TUC_PCT_IN. |
| 244 | `FS.GI.TXN.PRE.ORDER.AGENT.COMM.IN.SCALE.CODE` | `FsGiTxnPreOrder_AgentCommInScaleCode` | TField |  | Agent commission scale code for two-leg order required for commission type &apos;Scale&apos;. Multifonds DB Column is CSCALE_OUTLET_COMM_IN. |
| 245 | `FS.GI.TXN.PRE.ORDER.SOS.FLAG` | `FsGiTxnPreOrder_SosFlag` | TField |  | Series of shares flag. Multifonds DB Column is FLG_SOS. |
| 246 | `FS.GI.TXN.PRE.ORDER.SELECTED.PRICE` | `FsGiTxnPreOrder_SelectedPrice` | TField |  | Type of price to be used from set up done at &apos;ADL parameter&apos; or &apos;Select price&apos; screen. Multifonds DB Column is SELECT_PRICE. |
| 247 | `FS.GI.TXN.PRE.ORDER.SELECTED.IN.PRICE` | `FsGiTxnPreOrder_SelectedInPrice` | TField |  | Type of price to be used for two-leg order from set up done at &apos;ADL parameter&apos; or &apos;Select price&apos; screen. Multifonds DB Column is SELECT_PRICE_IN. |
| 248 | `FS.GI.TXN.PRE.ORDER.NON.CRYST.SP.FLAG` | `FsGiTxnPreOrder_NonCrystSpFlag` | TField |  | Flag to specifuy that the switch out transaction is processed using the GAV price and not the NAV price. Multifonds DB Column is FLG_NON_CRYST_SP. |
| 249 | `FS.GI.TXN.PRE.ORDER.NEW.POSITION.FLAG` | `FsGiTxnPreOrder_NewPositionFlag` | TField |  | New position flag. Multifonds DB Column is FLG_NEW_POSITION. |
| 250 | `FS.GI.TXN.PRE.ORDER.CR.DEAL.REFERENCE` | `FsGiTxnPreOrder_CrDealReference` | TField |  | Credit deal reference of a contract related to a reinvestment order when non-settlement of the credit deal reference is delaying reinvestment. Multifonds DB Column is DEAL_REF_CR. |
| 251 | `FS.GI.TXN.PRE.ORDER.CR.CONTRACT.ID` | `FsGiTxnPreOrder_CrContractId` | TField |  | Credit contract number of a contract related to a reinvestment order when non-settlement of the credit contract is delaying reinvestment. Multifonds DB Column is NCONTRACT_CR. |
| 252 | `FS.GI.TXN.PRE.ORDER.CR.FUND.ID` | `FsGiTxnPreOrder_CrFundId` | TField |  | Credit Fund ID. Multifonds DB Column is NPTF_CR. |
| 253 | `FS.GI.TXN.PRE.ORDER.CR.SHARE.CLASS.CODE` | `FsGiTxnPreOrder_CrShareClassCode` | TField |  | Credit Share Class ID. Multifonds DB Column is TPART_CR. |
| 254 | `FS.GI.TXN.PRE.ORDER.CLIENT.TRAD.DESK.FLAG` | `FsGiTxnPreOrder_ClientTradDeskFlag` | TField |  | Flag to indicate client FX is required for the order. Multifonds DB Column is FLG_CLIENT_FX. |
| 255 | `FS.GI.TXN.PRE.ORDER.FORCED.CLIENT.FX.FLAG` | `FsGiTxnPreOrder_ForcedClientFxFlag` | TField |  | Flag to indicate that exchange rate is forced at order entry. Multifonds DB Column is FLG_FORCED_FX. |
| 256 | `FS.GI.TXN.PRE.ORDER.CANC.FX.PL.CCY` | `FsGiTxnPreOrder_CancFxPlCcy` | TField |  | Currency in which FX profit/loss is calculated during client trading desk processing. Multifonds DB Column is CMON_FX_PL_CALC_CANC. |
| 257 | `FS.GI.TXN.PRE.ORDER.REV.FX.PL.CALC.DATE` | `FsGiTxnPreOrder_RevFxPlCalcDate` | TField |  | Date of the calculation of profit/loss for reversal order. Multifonds DB Column is DFX_REV_PL_CALC. |
| 258 | `FS.GI.TXN.PRE.ORDER.REV.CLIENT.FX` | `FsGiTxnPreOrder_RevClientFx` | TField |  | Client FX reversal method. Multifonds DB Column is CLI_FX_REV. |
| 259 | `FS.GI.TXN.PRE.ORDER.SWIFT.MSG.SENT.FLAG` | `FsGiTxnPreOrder_SwiftMsgSentFlag` | TField |  | Flag to specify whether swift cancellation message should be sent. Multifonds DB Column is FLG_SWIFT_CAN_MSG_SENT. |
| 260 | `FS.GI.TXN.PRE.ORDER.SWIFT.CANC.REASON.CODE` | `FsGiTxnPreOrder_SwiftCancReasonCode` | TField | Yes | Swift cancellation reason code: Mandatory if the swift cancel message flag is Y. Multifonds DB Column is SWIFT_CAN_MSG_CODE. |
| 261 | `FS.GI.TXN.PRE.ORDER.ERR.CORRECTION.ID` | `FsGiTxnPreOrder_ErrCorrectionId` | TField |  | Error/Correction Identifier for a correction or reversal deal. Multifonds DB Column is ERR_CORR_ID. |
| 262 | `FS.GI.TXN.PRE.ORDER.CORRECTIVE.PAYMENT.FLAG` | `FsGiTxnPreOrder_CorrectivePaymentFlag` | TField |  | Corrective payment indicator for automated correction payment generation. Multifonds DB Column is FLG_CORR_PAY. |
| 263 | `FS.GI.TXN.PRE.ORDER.ACTUAL.TRADE.DATE` | `FsGiTxnPreOrder_ActualTradeDate` | TField |  | Actual trade date for the order used to calculate the P/L correction. Multifonds DB Column is ACT_TD. |
| 264 | `FS.GI.TXN.PRE.ORDER.ACTUAL.VALUE.DATE` | `FsGiTxnPreOrder_ActualValueDate` | TField |  | Actual value date of this order used for payment processing. Multifonds DB Column is ACT_VD. |
| 265 | `FS.GI.TXN.PRE.ORDER.PROFIT.LOSS.METHOD` | `FsGiTxnPreOrder_ProfitLossMethod` | TField |  | Method used for Profit and Loss calculation. This impacts the calculation of the reversal value date. Multifonds DB Column is PL_METHOD. |
| 266 | `FS.GI.TXN.PRE.ORDER.REV.CONTRACT.NOTE.FLG` | `FsGiTxnPreOrder_RevContractNoteFlg` | TField |  | Flag to produce contract note on reversal. Multifonds DB Column is FLG_CONT_NOTE. |
| 267 | `FS.GI.TXN.PRE.ORDER.REV.PAYMENT.MADE.FLAG` | `FsGiTxnPreOrder_RevPaymentMadeFlag` | TField |  | Flag to specify whether payments have been made for this reversal deal. Multifonds DB Column is FLG_PAY_MADE. |
| 268 | `FS.GI.TXN.PRE.ORDER.UNMATCH.RECEIPT.FLAG` | `FsGiTxnPreOrder_UnmatchReceiptFlag` | TField |  | Un-match receipt flag to control display of cleared funds. Multifonds DB Column is FLG_UNMATCH_RECPT. |
| 269 | `FS.GI.TXN.PRE.ORDER.GL.POSTINGS.FLAG` | `FsGiTxnPreOrder_GlPostingsFlag` | TField |  | Flag to decide whether GL posting is required for the order. Multifonds DB Column is GL_POSTINGS. |
| 270 | `FS.GI.TXN.PRE.ORDER.GL.IN.POSTINGS.FLAG` | `FsGiTxnPreOrder_GlInPostingsFlag` | TField |  | Flag to decide whether GL posting is required for the two-leg order. Multifonds DB Column is GL_POSTINGS_IN. |
| 271 | `FS.GI.TXN.PRE.ORDER.SWITCH.IN.CALC.NAV.DATE` | `FsGiTxnPreOrder_SwitchInCalcNavDate` | TField |  | Price date for switch in calculated by applying the hard and soft conditional trade date rules. Multifonds DB Column is PRICE_DATE_IN. |
| 272 | `FS.GI.TXN.PRE.ORDER.SWITCH.OUT.CALC.NAV.DATE` | `FsGiTxnPreOrder_SwitchOutCalcNavDate` | TField |  | Price date for switch out calculated by applying the hard and soft conditional trade date rules. Multifonds DB Column is PRICE_DATE_OUT. |
| 273 | `FS.GI.TXN.PRE.ORDER.LEGAL.ENTITY.SWITCH.TR.DATE` | `FsGiTxnPreOrder_LegalEntitySwitchTrDate` | TField |  | Trade date for switch method for Legal Entity linked to the order. Multifonds DB Column is TFC_SWITCH_TD. |
| 274 | `FS.GI.TXN.PRE.ORDER.FUND.PROMOTER.ID` | `FsGiTxnPreOrder_FundPromoterId` | TField |  | Fund promoter linked to the order. Multifonds DB Column is NPROMOTER. |
| 275 | `FS.GI.TXN.PRE.ORDER.PROMOTER.ID.2` | `FsGiTxnPreOrder_PromoterId2` | TField |  | Fund promoter 2 linked to the order. Multifonds DB Column is NPROMOTER2. |
| 276 | `FS.GI.TXN.PRE.ORDER.THRESHOLD.FLAG` | `FsGiTxnPreOrder_ThresholdFlag` | TField |  | Threshold Flag. Multifonds DB Column is FLG_THRESHOLD. |
| 277 | `FS.GI.TXN.PRE.ORDER.MESSAGE.ID` | `FsGiTxnPreOrder_MessageId` | TField |  | Message ID of the order Multifonds DB Column is MSG_ID. |
| 278 | `FS.GI.TXN.PRE.ORDER.FX.PROCESS.UPDATE.FLAG` | `FsGiTxnPreOrder_FxProcessUpdateFlag` | TField |  | FX Process update flag. Multifonds DB Column is FLG_UPD_FUND_TDSK_PROC. |
| 279 | `FS.GI.TXN.PRE.ORDER.FIRST.SUB.MIN.LIMIT` | `FsGiTxnPreOrder_FirstSubMinLimit` | TField |  | First sub minimum limit. Multifonds DB Column is FIRST_SUB_MIN_LIMIT. |
| 280 | `FS.GI.TXN.PRE.ORDER.FIRST.SUB.MAX.LIMIT` | `FsGiTxnPreOrder_FirstSubMaxLimit` | TField |  | First sub maximum limit. Multifonds DB Column is FIRST_SUB_MAX_LIMIT. |
| 281 | `FS.GI.TXN.PRE.ORDER.TRANS.MIN.LIMIT` | `FsGiTxnPreOrder_TransMinLimit` | TField |  | Transaction minimum limit. Multifonds DB Column is TRANS_MIN_LIMIT. |
| 282 | `FS.GI.TXN.PRE.ORDER.TRANS.MAX.LIMIT` | `FsGiTxnPreOrder_TransMaxLimit` | TField |  | Transaction maximum limit. Multifonds DB Column is TRANS_MAX_LIMIT. |
| 283 | `FS.GI.TXN.PRE.ORDER.HOLDING.LIMIT` | `FsGiTxnPreOrder_HoldingLimit` | TField |  | Holding limit. Multifonds DB Column is HOLDING_LIMIT. |
| 284 | `FS.GI.TXN.PRE.ORDER.PE.EVENT.FLAG` | `FsGiTxnPreOrder_PeEventFlag` | TField |  | Private Equity commitments and capital calls flag to identify whether the order is created through event processing or manual creation. Multifonds DB Column is FLG_PE. |
| 285 | `FS.GI.TXN.PRE.ORDER.ORIGINAL.TRADE.DATE` | `FsGiTxnPreOrder_OriginalTradeDate` | TField |  | Original trade date. Multifonds DB Column is DATE_EXE_ORIG. |
| 286 | `FS.GI.TXN.PRE.ORDER.TRADE.DATE.CHANGE.REASON` | `FsGiTxnPreOrder_TradeDateChangeReason` | TField |  | Trade date change reason. Multifonds DB Column is REASON_DATE_EXE. |
| 287 | `FS.GI.TXN.PRE.ORDER.ORIGINAL.VALUE.DATE` | `FsGiTxnPreOrder_OriginalValueDate` | TField |  | Original value date . Multifonds DB Column is DVALEUR_ORIG. |
| 288 | `FS.GI.TXN.PRE.ORDER.TEMP.ORIG.VALUE.DATE` | `FsGiTxnPreOrder_TempOrigValueDate` | TField |  | Original value date temp. Multifonds DB Column is DVALEUR_ORIG_TEMP. |
| 289 | `FS.GI.TXN.PRE.ORDER.VALUE.DATE.CHANGE.REASON` | `FsGiTxnPreOrder_ValueDateChangeReason` | TField |  | Value date change reason. Multifonds DB Column is REASON_DVALEUR. |
| 290 | `FS.GI.TXN.PRE.ORDER.ORIGINAL.IN.TRADE.DATE` | `FsGiTxnPreOrder_OriginalInTradeDate` | TField |  | Original trade date for two-leg order. Multifonds DB Column is DATE_EXE_IN_ORIG. |
| 291 | `FS.GI.TXN.PRE.ORDER.TRADE.DATE.IN.CHANGE.REASON` | `FsGiTxnPreOrder_TradeDateInChangeReason` | TField |  | Trade date in change reason. Multifonds DB Column is REASON_DATE_EXE_IN. |
| 292 | `FS.GI.TXN.PRE.ORDER.ORIGINAL.IN.VALUE.DATE` | `FsGiTxnPreOrder_OriginalInValueDate` | TField |  | Original value date for two-leg order. Multifonds DB Column is DVALEUR_IN_ORIG. |
| 293 | `FS.GI.TXN.PRE.ORDER.TEMP.ORIG.VALUE.IN.DATE` | `FsGiTxnPreOrder_TempOrigValueInDate` | TField |  | Original value date for two-leg order temp. Multifonds DB Column is DVALEUR_IN_ORIG_TEMP. |
| 294 | `FS.GI.TXN.PRE.ORDER.VALUE.DATE.IN.CHANGE.REASON` | `FsGiTxnPreOrder_ValueDateInChangeReason` | TField |  | Value Date for the two-leg change reason. Multifonds DB Column is REASON_DVALEUR_IN. |
| 295 | `FS.GI.TXN.PRE.ORDER.LARGE.DEAL.IN.THRES.BREACH` | `FsGiTxnPreOrder_LargeDealInThresBreach` | TField |  | Flag to indicate large deal threshold is breached for the two leg order. Multifonds DB Column is FLG_LD_THRESHOLD_BREACH_IN. |
| 296 | `FS.GI.TXN.PRE.ORDER.LARGE.DEAL.IN.ORDER.THRES.AMT` | `FsGiTxnPreOrder_LargeDealInOrderThresAmt` | TField |  | Large Deal Order Threshold Amt for the in Leg Multifonds DB Column is LD_ORDER_THRESHOLD_AMT_IN. |
| 297 | `FS.GI.TXN.PRE.ORDER.LARGE.DEAL.IN.THRES.AMT` | `FsGiTxnPreOrder_LargeDealInThresAmt` | TField |  | Large Deal Threshold Amt for the in Leg Multifonds DB Column is LD_THRESHOLD_AMT_IN. |
| 298 | `FS.GI.TXN.PRE.ORDER.LARGE.DEAL.IN.THRES.CCY` | `FsGiTxnPreOrder_LargeDealInThresCcy` | TField |  | Large deal threshold currency for two-leg order. Multifonds DB Column is LD_THRESHOLD_CCY_IN. |
| 299 | `FS.GI.TXN.PRE.ORDER.LARGE.DEAL.THRES.BREACH.FLG` | `FsGiTxnPreOrder_LargeDealThresBreachFlg` | TField |  | Flag to indicate large deal threshold is breached for order. Multifonds DB Column is FLG_LD_THRESHOLD_BREACH. |
| 300 | `FS.GI.TXN.PRE.ORDER.LARGE.DEAL.ORDER.THRES.AMT` | `FsGiTxnPreOrder_LargeDealOrderThresAmt` | TField |  | Order amount in threshold currency. Multifonds DB Column is LD_ORDER_THRESHOLD_AMT. |
| 301 | `FS.GI.TXN.PRE.ORDER.LARGE.DEAL.THRES.AMT` | `FsGiTxnPreOrder_LargeDealThresAmt` | TField |  | Threshold amount or percentage applied to the deal as per threshold setup at Promoter, or Legal Entity, or Fund, or Share Class level. Multifonds DB Column is LD_THRESHOLD_AMT. |
| 302 | `FS.GI.TXN.PRE.ORDER.LARGE.DEAL.THRES.CCY` | `FsGiTxnPreOrder_LargeDealThresCcy` | TField |  | Large deal threshold currency for the order. Multifonds DB Column is LD_THRESHOLD_CCY. |
| 303 | `FS.GI.TXN.PRE.ORDER.PL.CARRY.FORWARD.AMT` | `FsGiTxnPreOrder_PlCarryForwardAmt` | TField |  | Profit/Loss carry forward. Multifonds DB Column is LP_MIG_PLCF. |
| 304 | `FS.GI.TXN.PRE.ORDER.HURDLE.CARRY.FORWARD.AMT` | `FsGiTxnPreOrder_HurdleCarryForwardAmt` | TField |  | Hurdle carry forward. Multifonds DB Column is LP_MIG_HCF. |
| 305 | `FS.GI.TXN.PRE.ORDER.INSTRUCTION.TYPE` | `FsGiTxnPreOrder_InstructionType` | TField |  | Instruction type. Multifonds DB Column is INSTRUC_TYPE. |
| 306 | `FS.GI.TXN.PRE.ORDER.INSTRUCT.REFERENCE.ID` | `FsGiTxnPreOrder_InstructReferenceId` | TField |  | Instruction reference ID. Multifonds DB Column is INSTRUC_REF. |
| 307 | `FS.GI.TXN.PRE.ORDER.GATINS.STATUS` | `FsGiTxnPreOrder_GatinsStatus` | TField |  | Gating order status. Multifonds DB Column is GATING_STATUS. |
| 308 | `FS.GI.TXN.PRE.ORDER.ORIG.SUB.DATE` | `FsGiTxnPreOrder_OrigSubDate` | TField |  | Original subscription date. Multifonds DB Column is SUB_DATE. |
| 309 | `FS.GI.TXN.PRE.ORDER.LAST.CRYST.DATE` | `FsGiTxnPreOrder_LastCrystDate` | TField |  | Last crystallization date. Multifonds DB Column is LAST_CRYST_DATE. |
| 310 | `FS.GI.TXN.PRE.ORDER.LAST.CRYST.NAV` | `FsGiTxnPreOrder_LastCrystNav` | TField |  | Last crystallization NAV. Multifonds DB Column is LAST_CRYST_NAV. |
| 311 | `FS.GI.TXN.PRE.ORDER.FUND.OF.FUND.ORDER.ID` | `FsGiTxnPreOrder_FundOfFundOrderId` | TField |  | Fund of Funds order ID. Multifonds DB Column is NORDER_FOF. |
| 312 | `FS.GI.TXN.PRE.ORDER.FUND.OF.FUND.AGENT.ID` | `FsGiTxnPreOrder_FundOfFundAgentId` | TField |  | Fund of Funds agent ID. Multifonds DB Column is NOUTLET_FOF. |
| 313 | `FS.GI.TXN.PRE.ORDER.RESERVED10` | `FsGiTxnPreOrder_Reserved10` | TField |  |  |
| 314 | `FS.GI.TXN.PRE.ORDER.RESERVED9` | `FsGiTxnPreOrder_Reserved9` | TField |  |  |
| 315 | `FS.GI.TXN.PRE.ORDER.RESERVED8` | `FsGiTxnPreOrder_Reserved8` | TField |  |  |
| 316 | `FS.GI.TXN.PRE.ORDER.RESERVED7` | `FsGiTxnPreOrder_Reserved7` | TField |  |  |
| 317 | `FS.GI.TXN.PRE.ORDER.RESERVED6` | `FsGiTxnPreOrder_Reserved6` | TField |  |  |
| 318 | `FS.GI.TXN.PRE.ORDER.RESERVED5` | `FsGiTxnPreOrder_Reserved5` | TField |  |  |
| 319 | `FS.GI.TXN.PRE.ORDER.RESERVED4` | `FsGiTxnPreOrder_Reserved4` | TField |  |  |
| 320 | `FS.GI.TXN.PRE.ORDER.RESERVED3` | `FsGiTxnPreOrder_Reserved3` | TField |  |  |
| 321 | `FS.GI.TXN.PRE.ORDER.RESERVED2` | `FsGiTxnPreOrder_Reserved2` | TField |  |  |
| 322 | `FS.GI.TXN.PRE.ORDER.RESERVED1` | `FsGiTxnPreOrder_Reserved1` | TField |  |  |
| 323 | `FS.GI.TXN.PRE.ORDER.LOCAL.REF` | `FsGiTxnPreOrder_LocalRef` |  |  |  |
| 324 | `FS.GI.TXN.PRE.ORDER.OVERRIDE` | `FsGiTxnPreOrder_Override` |  |  |  |
| 325 | `FS.GI.TXN.PRE.ORDER.RECORD.STATUS` | `FsGiTxnPreOrder_RecordStatus` | String |  |  |
| 326 | `FS.GI.TXN.PRE.ORDER.CURR.NO` | `FsGiTxnPreOrder_CurrNo` | String |  |  |
| 327 | `FS.GI.TXN.PRE.ORDER.INPUTTER` | `FsGiTxnPreOrder_Inputter` |  |  |  |
| 328 | `FS.GI.TXN.PRE.ORDER.DATE.TIME` | `FsGiTxnPreOrder_DateTime` |  |  |  |
| 329 | `FS.GI.TXN.PRE.ORDER.AUTHORISER` | `FsGiTxnPreOrder_Authoriser` | String |  |  |
| 330 | `FS.GI.TXN.PRE.ORDER.CO.CODE` | `FsGiTxnPreOrder_CoCode` | String |  |  |
| 331 | `FS.GI.TXN.PRE.ORDER.DEPT.CODE` | `FsGiTxnPreOrder_DeptCode` | String |  |  |
| 332 | `FS.GI.TXN.PRE.ORDER.AUDITOR.CODE` | `FsGiTxnPreOrder_AuditorCode` | String |  |  |
| 333 | `FS.GI.TXN.PRE.ORDER.AUDIT.DATE.TIME` | `FsGiTxnPreOrder_AuditDateTime` | String |  |  |
