# FS.GI.TXN.ORDER — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.ORDER` in `FS_TransactionEntry.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.ORDER.PARENT.REF.ID` | `FsGiTxnOrder_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.ORDER.ORA.ROWID` | `FsGiTxnOrder_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.ORDER.ORIG.EXTERNAL.ORDER.ID` | `FsGiTxnOrder_OrigExternalOrderId` | TField |  | Original external order reference filled in case the original order reference flag is ticked at application level and the original order reference is displayed in the order interface. Multifonds DB Column is ORIGINAL_NORDER_EXTERN. |
| 4 | `FS.GI.TXN.ORDER.ORDER.EXTERNAL.ID` | `FsGiTxnOrder_OrderExternalId` | TField |  | External order ID. Multifonds DB Column is NORDER_EXTERN. |
| 5 | `FS.GI.TXN.ORDER.PRE.ORDER.FLAG` | `FsGiTxnOrder_PreOrderFlag` | TField |  | Flag to specify that the order is pre-order. Multifonds DB Column is PRE_ORDER. |
| 6 | `FS.GI.TXN.ORDER.CORRECTION.FLAG` | `FsGiTxnOrder_CorrectionFlag` | TField |  | Flag to specify this order is a correction deal. Multifonds DB Column is FLG_CORR. |
| 7 | `FS.GI.TXN.ORDER.NO.CASH.FLAG` | `FsGiTxnOrder_NoCashFlag` | TField |  | Flag to specify that there is no cash movements associated with the order. Multifonds DB Column is FLG_NO_CASH. |
| 8 | `FS.GI.TXN.ORDER.INTERNAL.CASH.FLAG` | `FsGiTxnOrder_InternalCashFlag` | TField |  | Flag to specify there is internal cash movement related to this transaction. Multifonds DB Column is FLG_INT_CASH. |
| 9 | `FS.GI.TXN.ORDER.RECEPTION.DATE.TIME` | `FsGiTxnOrder_ReceptionDateTime` |  |  |  |
| 10 | `FS.GI.TXN.ORDER.DEALING.REGISTER.ID` | `FsGiTxnOrder_DealingRegisterId` | TField |  | Dealing register ID. If the main register is a global register, dealing register will be a bearer register dealing for the global register. Multifonds DB Column is NREGISTER_DEAL. |
| 11 | `FS.GI.TXN.ORDER.REGISTER.ID` | `FsGiTxnOrder_RegisterId` | TField |  | Register for which the order is placed. Multifonds DB Column is NREGISTER. |
| 12 | `FS.GI.TXN.ORDER.AGENT.ID` | `FsGiTxnOrder_AgentId` | TField |  | Agentlinked to the order. Multifonds DB Column is NOUTLET. |
| 13 | `FS.GI.TXN.ORDER.OPERATION.CODE` | `FsGiTxnOrder_OperationCode` | TField |  | Type of operation performed such as subscription, redemption, switch, transfer etc. Multifonds DB Column is COPERATION. |
| 14 | `FS.GI.TXN.ORDER.TA.FUND.ID` | `FsGiTxnOrder_TaFundId` | TField |  | Fund in which the order is placed. Multifonds DB Column is NPTF. |
| 15 | `FS.GI.TXN.ORDER.PROVIDER.ID` | `FsGiTxnOrder_ProviderId` | TField |  | Organisation supplying the security Id. Multifonds DB Column is PROVID. |
| 16 | `FS.GI.TXN.ORDER.LEGAL.ENTITY.ID` | `FsGiTxnOrder_LegalEntityId` | TField |  | Legal Entity linked to the order. Multifonds DB Column is NTFC. |
| 17 | `FS.GI.TXN.ORDER.SHARE.CLASS.CODE` | `FsGiTxnOrder_ShareClassCode` | TField |  | Fund share class in which the order is placed. Multifonds DB Column is TPART. |
| 18 | `FS.GI.TXN.ORDER.SOS.CLASS.CODE` | `FsGiTxnOrder_SosClassCode` | TField |  | Share class code for series of shares funds. Allowed values are from the list of codes defined in MFGI. Multifonds DB Column is TPART_SOS. |
| 19 | `FS.GI.TXN.ORDER.TA.IN.FUND.ID` | `FsGiTxnOrder_TaInFundId` | TField |  | Destination Fund ID in a two-leg order. Multifonds DB Column is NPTF2. |
| 20 | `FS.GI.TXN.ORDER.PROVIDER.ID.2` | `FsGiTxnOrder_ProviderId2` | TField |  | Organisation supplying the security Id for two leg transactions. Multifonds DB Column is PROVID2. |
| 21 | `FS.GI.TXN.ORDER.IN.LEGAL.ENTITY.ID` | `FsGiTxnOrder_InLegalEntityId` | TField |  | Destination Legal Entity ID in a two-leg order. Multifonds DB Column is NTFC2. |
| 22 | `FS.GI.TXN.ORDER.IN.SHARE.CLASS` | `FsGiTxnOrder_InShareClass` | TField |  | Destination fund share class in a two-leg order. Multifonds DB Column is TPART2. |
| 23 | `FS.GI.TXN.ORDER.SOS.IN.CLASS.CODE` | `FsGiTxnOrder_SosInClassCode` | TField |  | Share class code for series of shares funds for two-leg transactions. Allowed values are from the list of codes defined in MFGI. Multifonds DB Column is TPART_SOS2. |
| 24 | `FS.GI.TXN.ORDER.DEALING.REGISTER.ID.2` | `FsGiTxnOrder_DealingRegisterId2` | TField |  | Dealing register ID for two leg transactions. If the main register is a global register, dealing register will be a bearer register dealing for the global register. Multifonds DB Column is NREGISTER_DEAL2. |
| 25 | `FS.GI.TXN.ORDER.IN.REGISTER.ID` | `FsGiTxnOrder_InRegisterId` | TField |  | Destination register ID in a two-leg order. Multifonds DB Column is NREGISTER2. |
| 26 | `FS.GI.TXN.ORDER.FULL.REDEMPTION.FLAG` | `FsGiTxnOrder_FullRedemptionFlag` | TField |  | Flag to redeem complete register positions. Multifonds DB Column is FLAG_ALL. |
| 27 | `FS.GI.TXN.ORDER.REGISTER.TYPE` | `FsGiTxnOrder_RegisterType` | TField |  | Register type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_REG. |
| 28 | `FS.GI.TXN.ORDER.SETTLEMENT.TYPE` | `FsGiTxnOrder_SettlementType` | TField |  | Settlement type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_SETTLEMENT. |
| 29 | `FS.GI.TXN.ORDER.DEAL.TYPE` | `FsGiTxnOrder_DealType` | TField |  | Deal type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_DEAL. |
| 30 | `FS.GI.TXN.ORDER.ORDER.STATUS` | `FsGiTxnOrder_OrderStatus` | TField |  | Transaction status indicating whether the order is in initial status, validated, deleted, cancelled etc. Multifonds DB Column is STATUS. |
| 31 | `FS.GI.TXN.ORDER.DEAL.STATUS` | `FsGiTxnOrder_DealStatus` | TField |  | Deal status of the order based on cash handling setup. Multifonds DB Column is DEAL_STATUS. |
| 32 | `FS.GI.TXN.ORDER.ORDER.TRADE.DATE` | `FsGiTxnOrder_OrderTradeDate` | TField |  | Trade Date (in DD/MM/YYYY format) of the order. Multifonds DB Column is DATE_EXE. |
| 33 | `FS.GI.TXN.ORDER.VALUE.DATE` | `FsGiTxnOrder_ValueDate` | TField |  | Fund settlement date for the order. Multifonds DB Column is DVALEUR. |
| 34 | `FS.GI.TXN.ORDER.SIMULATION.DATE` | `FsGiTxnOrder_SimulationDate` | TField |  | Date on which simulation will be processed for the order. Multifonds DB Column is SEND_TFC_DATE. |
| 35 | `FS.GI.TXN.ORDER.AMOUNT` | `FsGiTxnOrder_Amount` | TField | Yes | Order Amount. This field is mandatory if quantity field is left blank. Multifonds DB Column is AMOUNT. |
| 36 | `FS.GI.TXN.ORDER.QUANTITY` | `FsGiTxnOrder_Quantity` | TField | Yes | Order quantity. This field is mandatory if amount field is left blank. Multifonds DB Column is QUANTITY. |
| 37 | `FS.GI.TXN.ORDER.PAYMENT.CURRENCY` | `FsGiTxnOrder_PaymentCurrency` | TField |  | The currency (in 3 letter ISO code, Eg: EUR) in which the payments will be processed for this order. Multifonds DB Column is CMON. |
| 38 | `FS.GI.TXN.ORDER.PAYMENT.TYPE` | `FsGiTxnOrder_PaymentType` | TField |  | Type of payment for the transaction. Multifonds DB Column is TYPE_PAYMENT. |
| 39 | `FS.GI.TXN.ORDER.CUSTODY.SETTLEMENT` | `FsGiTxnOrder_CustodySettlement` | TField |  | Custody settlement type populated based on data defined in the register main screen. Multifonds DB Column is CDEF_DELIV. |
| 40 | `FS.GI.TXN.ORDER.SWITCH.PCT` | `FsGiTxnOrder_SwitchPct` | TField |  | Switch percentage of the order. Multifonds DB Column is SPLIT_PERCENT. |
| 41 | `FS.GI.TXN.ORDER.INTERNAL.REFERENCE` | `FsGiTxnOrder_InternalReference` | TField |  | Unique internal reference for the order. Multifonds DB Column is INTERNAL_REFERENCE. |
| 42 | `FS.GI.TXN.ORDER.ORDER.TYPE` | `FsGiTxnOrder_OrderType` | TField |  | Type of the transaction. For example NAV of the day, backdated, back-value etc. Multifonds DB Column is TYPE_ORDRE. |
| 43 | `FS.GI.TXN.ORDER.RECEIVED.MODE` | `FsGiTxnOrder_ReceivedMode` | TField |  | Mode in which the order instruction is received. Multifonds DB Column is MODE_RECEIVED. |
| 44 | `FS.GI.TXN.ORDER.INTERFACED.ORDER.FLAG` | `FsGiTxnOrder_InterfacedOrderFlag` | TField |  | Flag to specify that the order is loaded through interface. Multifonds DB Column is FLG_INTERFACED_ORDER. |
| 45 | `FS.GI.TXN.ORDER.CONFIRM.USER` | `FsGiTxnOrder_ConfirmUser` | TField |  | User who confirms the order. Multifonds DB Column is USER_CONFIRM. |
| 46 | `FS.GI.TXN.ORDER.ORDER.ID` | `FsGiTxnOrder_OrderId` | TField |  | Order identification number. Multifonds DB Column is NORDER. |
| 47 | `FS.GI.TXN.ORDER.DEAL.REFERENCE` | `FsGiTxnOrder_DealReference` | TField |  | Unique internal reference that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF. |
| 48 | `FS.GI.TXN.ORDER.IN.DEAL.REFERENCE` | `FsGiTxnOrder_InDealReference` | TField |  | Unique internal reference for two-leg orders that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF_IN. |
| 49 | `FS.GI.TXN.ORDER.LEG.LINK` | `FsGiTxnOrder_LegLink` | TField |  | System created ID for switch, transfer, Aller Retour and merge order entries. Multifonds DB Column is LEG_LINK. |
| 50 | `FS.GI.TXN.ORDER.INSTRUCTION.ID` | `FsGiTxnOrder_InstructionId` | TField |  | Order instruction ID. Multifonds DB Column is NINSTRUCTION. |
| 51 | `FS.GI.TXN.ORDER.LINKED.ORDER.ID` | `FsGiTxnOrder_LinkedOrderId` | TField |  | Original order number linked to sub orders created for a single multiple series debit order. Multifonds DB Column is LINKED_NORDER. |
| 52 | `FS.GI.TXN.ORDER.NAV` | `FsGiTxnOrder_Nav` | TField |  | NAV price applicable for the order. Multifonds DB Column is NAV_PRICE. |
| 53 | `FS.GI.TXN.ORDER.FORCED.PRICE.FLAG` | `FsGiTxnOrder_ForcedPriceFlag` | TField |  | Forced NAV price to be applied for the order. Multifonds DB Column is FORCE_PRICE. |
| 54 | `FS.GI.TXN.ORDER.FORCED.IN.PRICE.FLAG` | `FsGiTxnOrder_ForcedInPriceFlag` | TField |  | Forced NAV price to be applied for the two-leg order. Multifonds DB Column is FORCE_PRICE_IN. |
| 55 | `FS.GI.TXN.ORDER.EST.NAV.FLAG` | `FsGiTxnOrder_EstNavFlag` | TField |  | Flag indicates whether the transaction should consider the Estimated NAV during the Partial Client trading desk process. Multifonds DB Column is ESTI_NAV. |
| 56 | `FS.GI.TXN.ORDER.EST.NAV` | `FsGiTxnOrder_EstNav` | TField |  | Estimated NAV price which is picked from the share price historical screen whenever the Estimated NAV flag at the order level is ticked. Multifonds DB Column is ESTI_NAV_PRICE. |
| 57 | `FS.GI.TXN.ORDER.IN.NAV` | `FsGiTxnOrder_InNav` | TField |  | NAV applicable for the two-leg order. Multifonds DB Column is NAV_PRICE_IN. |
| 58 | `FS.GI.TXN.ORDER.COMM.EXCEPT.PCT` | `FsGiTxnOrder_CommExceptPct` | TField |  | Order commission exception percentage. Multifonds DB Column is EXCEPT_PCT. |
| 59 | `FS.GI.TXN.ORDER.COMM.EXCEPT.AMOUNT` | `FsGiTxnOrder_CommExceptAmount` | TField |  | Order commission exception amount. Multifonds DB Column is MNT_COM_EXCEPT. |
| 60 | `FS.GI.TXN.ORDER.DISTRIB.COMM.PCT` | `FsGiTxnOrder_DistribCommPct` | TField |  | Percentage of distributed commission. Multifonds DB Column is PCT_COM_DISTRIB. |
| 61 | `FS.GI.TXN.ORDER.TA.COMM.PCT` | `FsGiTxnOrder_TaCommPct` | TField |  | Transfer agent commission percentage. Multifonds DB Column is TA_PCT. |
| 62 | `FS.GI.TXN.ORDER.COMMISSION.DISCLOSURE.CODE` | `FsGiTxnOrder_CommissionDisclosureCode` | TField |  | Commission disclosure code. Multifonds DB Column is COMM_DISCLOSURE. |
| 63 | `FS.GI.TXN.ORDER.COMM.ON.TOP.FLAG` | `FsGiTxnOrder_CommOnTopFlag` | TField |  | Commission on top flag. Multifonds DB Column is FLG_TOP_COMM. |
| 64 | `FS.GI.TXN.ORDER.MGMT.COMM` | `FsGiTxnOrder_MgmtComm` | TField |  | Management commission amount for the order. Multifonds DB Column is MGMT_COMM. |
| 65 | `FS.GI.TXN.ORDER.COMM.EXCEPT.IN.PCT` | `FsGiTxnOrder_CommExceptInPct` | TField |  | Order commission exception percentage for two-leg order. Multifonds DB Column is EXCEPT_PCT_IN. |
| 66 | `FS.GI.TXN.ORDER.AMOUNT.EXCEPT.IN.AMT` | `FsGiTxnOrder_AmountExceptInAmt` | TField |  | Order commission exception amount for two-leg order. Multifonds DB Column is MNT_COM_EXCEPT_IN. |
| 67 | `FS.GI.TXN.ORDER.DISTRIB.COMM.IN.PCT` | `FsGiTxnOrder_DistribCommInPct` | TField |  | Order distributed commission percentage for two-leg order. Multifonds DB Column is PCT_COM_DISTRIB_IN. |
| 68 | `FS.GI.TXN.ORDER.TA.COMM.IN.PCT` | `FsGiTxnOrder_TaCommInPct` | TField |  | Trasnsfer agent commission percentage for two-leg order. Multifonds DB Column is TA_PCT_IN. |
| 69 | `FS.GI.TXN.ORDER.AGENT.COMM.DISC.SCALE.CODE` | `FsGiTxnOrder_AgentCommDiscScaleCode` | TField |  | Agent commission discount scale code. Multifonds DB Column is CSCALE_NDISCOUNT. |
| 70 | `FS.GI.TXN.ORDER.WAIVER.COMM.SCALE.CODE` | `FsGiTxnOrder_WaiverCommScaleCode` | TField |  | Waiver commission percentage scale used when the commission or penalty type &apos;Dual pricing Method&apos; is chosen. Multifonds DB Column is CSCALE_NCOMM_WAIVER. |
| 71 | `FS.GI.TXN.ORDER.INIT.CHARGE.PCT` | `FsGiTxnOrder_InitChargePct` | TField |  | Order initial charge for two-leg order. Multifonds DB Column is NINIT_CHRG_IN. |
| 72 | `FS.GI.TXN.ORDER.DISCOUNT.IN.AMT` | `FsGiTxnOrder_DiscountInAmt` | TField |  | Order discount for two-leg order. Multifonds DB Column is NDISCOUNT_IN. |
| 73 | `FS.GI.TXN.ORDER.DISCOUNT.IN.SCALE.CODE` | `FsGiTxnOrder_DiscountInScaleCode` | TField |  | Order discount scale for two-leg order. Multifonds DB Column is CSCALE_NDISCOUNT_IN. |
| 74 | `FS.GI.TXN.ORDER.WAIVER.COMM.IN.PCT` | `FsGiTxnOrder_WaiverCommInPct` | TField |  | Order waiver commission rate for in leg. Multifonds DB Column is NCOMM_WAIVER_IN. |
| 75 | `FS.GI.TXN.ORDER.WAIVER.COMM.IN.SCALE.CODE` | `FsGiTxnOrder_WaiverCommInScaleCode` | TField |  | Order waiver commission scale for in leg. Multifonds DB Column is CSCALE_WAIVER_IN. |
| 76 | `FS.GI.TXN.ORDER.FORCED.COMM.PAY.CCY.FLG` | `FsGiTxnOrder_ForcedCommPayCcyFlg` | TField |  | Order forced commission amount in payment currency. Multifonds DB Column is FLG_PAY_CCY_OUT. |
| 77 | `FS.GI.TXN.ORDER.FORCED.COMM.IN.PAY.CCY.FLG` | `FsGiTxnOrder_ForcedCommInPayCcyFlg` | TField |  | Order forced commission amount in payment currency for two-leg order. Multifonds DB Column is FLG_PAY_CCY_IN. |
| 78 | `FS.GI.TXN.ORDER.COMM.ARRANGEMENT.ID` | `FsGiTxnOrder_CommArrangementId` | TField |  | Order commission arrangement identification code. Multifonds DB Column is NARRANGE. |
| 79 | `FS.GI.TXN.ORDER.INITIAL.CHARGE` | `FsGiTxnOrder_InitialCharge` | TField |  | Initial commission charge percentage at Order level. This can not be greater than the maximum % allowed by the fund. Multifonds DB Column is NINIT_CHRG. |
| 80 | `FS.GI.TXN.ORDER.COMMISSION.WAIVER` | `FsGiTxnOrder_CommissionWaiver` | TField |  | Commission Waiver Amount. Multifonds DB Column is NCOMM_WAIVER. |
| 81 | `FS.GI.TXN.ORDER.COMMISSION.DISCOUNT` | `FsGiTxnOrder_CommissionDiscount` | TField |  | Discount percentage agreed by fund for dual pricing functionality. Multifonds DB Column is NDISCOUNT. |
| 82 | `FS.GI.TXN.ORDER.FX.RATE` | `FsGiTxnOrder_FxRate` | TField |  | Derived default FX rate. Multifonds DB Column is TAUX. |
| 83 | `FS.GI.TXN.ORDER.APPLIED.FX.RATE` | `FsGiTxnOrder_AppliedFxRate` | TField |  | FX rate applicable for the order. Multifonds DB Column is TAUX_USER. |
| 84 | `FS.GI.TXN.ORDER.APPLIED.FX.INDICATOR` | `FsGiTxnOrder_AppliedFxIndicator` | TField |  | Field indicating the application of FX rate is to divide or multiply. Multifonds DB Column is RATE_INDICATOR. |
| 85 | `FS.GI.TXN.ORDER.CANC.FX.PL.AMOUNT` | `FsGiTxnOrder_CancFxPlAmount` | TField |  | Profit or loss for amount in share class currency for cancelled orders, calculated during client trading desk procesing. Multifonds DB Column is FX_PL_CALC_CANC. |
| 86 | `FS.GI.TXN.ORDER.TISR` | `FsGiTxnOrder_Tisr` | TField |  | Taxable Income per Share Rate applicable for the order. Multifonds DB Column is TISR. |
| 87 | `FS.GI.TXN.ORDER.US.TAX.FLAG` | `FsGiTxnOrder_UsTaxFlag` | TField |  | Flag to indicaten that US Tax is applicable for the order. Multifonds DB Column is FLG_USTAX. |
| 88 | `FS.GI.TXN.ORDER.SWEDISH.TAX.FLAG` | `FsGiTxnOrder_SwedishTaxFlag` | TField |  | Flag to indicaten that Swedish Tax is applicable for the order. Multifonds DB Column is FLG_SWEDISH_TAX. |
| 89 | `FS.GI.TXN.ORDER.IE.FINANCE.ACT.TAX` | `FsGiTxnOrder_IeFinanceActTax` | TField |  | The flag specifies Irish tax applicable on the order. Multifonds DB Column is IE_FIN_ACT_TAXATION. |
| 90 | `FS.GI.TXN.ORDER.PARTIAL.SETTLEMENT.PCT` | `FsGiTxnOrder_PartialSettlementPct` | TField |  | Partial settlement percentage. Multifonds DB Column is PART_SETT_PCT. |
| 91 | `FS.GI.TXN.ORDER.PART.SETTLEMENT.DATE` | `FsGiTxnOrder_PartSettlementDate` | TField |  | Partial settlement date. Multifonds DB Column is SETT_DATE. |
| 92 | `FS.GI.TXN.ORDER.HOLD.PAYMENT.FLAG` | `FsGiTxnOrder_HoldPaymentFlag` | TField |  | Flag to specify payments related to this order should be kept on hold. Multifonds DB Column is FLG_HOLD_PYM. |
| 93 | `FS.GI.TXN.ORDER.PARTIAL.PAYMENT.FLAG` | `FsGiTxnOrder_PartialPaymentFlag` | TField |  | Flag indicates that the transaction follows the new partial payment functionality at the transaction level. Multifonds DB Column is FLG_PART_PAY. |
| 94 | `FS.GI.TXN.ORDER.PART.AMT.PAY.CCY` | `FsGiTxnOrder_PartAmtPayCcy` | TField |  | Partial payment amount in payment currency. Multifonds DB Column is PART_PAY_AMT. |
| 95 | `FS.GI.TXN.ORDER.REGISTER.BANK.ID` | `FsGiTxnOrder_RegisterBankId` | TField |  | Bank ID of the register. Multifonds DB Column is REG_BANK. |
| 96 | `FS.GI.TXN.ORDER.REGISTER.BANK.ACCOUNT` | `FsGiTxnOrder_RegisterBankAccount` | TField |  | Bank Account number of the register. Multifonds DB Column is REG_BANK_ACCOUNT. |
| 97 | `FS.GI.TXN.ORDER.REGISTER.BANK.HOLDER` | `FsGiTxnOrder_RegisterBankHolder` | TField |  | Name of the bank account holder. Multifonds DB Column is REG_BANK_HOLDER. |
| 98 | `FS.GI.TXN.ORDER.DB.BANK.ID` | `FsGiTxnOrder_DbBankId` | TField |  | Bank ID to be debitted for payments related to this order. Multifonds DB Column is REG_BANK_DB. |
| 99 | `FS.GI.TXN.ORDER.DB.BANK.ACCOUNT` | `FsGiTxnOrder_DbBankAccount` | TField |  | Bank account number to be debitted for payments related to this order. Multifonds DB Column is REG_BANK_DB_ACC. |
| 100 | `FS.GI.TXN.ORDER.ADL.DEFAULT.RATE` | `FsGiTxnOrder_AdlDefaultRate` | TField |  | ADL default rate for the order. Multifonds DB Column is ADL_RATE. |
| 101 | `FS.GI.TXN.ORDER.ADL.AMOUNT` | `FsGiTxnOrder_AdlAmount` | TField |  | ADL amount for the order. Multifonds DB Column is ADL_AMOUNT. |
| 102 | `FS.GI.TXN.ORDER.EXCL.ADL.FROM.AMT.FLG` | `FsGiTxnOrder_ExclAdlFromAmtFlg` | TField |  | Flag to indicate that Anti Dilution Levy (ADL) is excluded from order amount. Multifonds DB Column is FLG_TOP_ADL. |
| 103 | `FS.GI.TXN.ORDER.DAILY.DIV.PAYMENT.TYPE` | `FsGiTxnOrder_DailyDivPaymentType` | TField |  | Dailyn dividend payment method. Multifonds DB Column is DLYDIV_PAYMTHD. |
| 104 | `FS.GI.TXN.ORDER.ACCRUED.DIV.AMOUNT` | `FsGiTxnOrder_AccruedDivAmount` | TField |  | Accrued dividend amount for this order. Multifonds DB Column is ACCRUAL_DIV. |
| 105 | `FS.GI.TXN.ORDER.TRANSACTION.CHARGE` | `FsGiTxnOrder_TransactionCharge` | TField |  | Transaction charge applicable for UK module. Multifonds DB Column is NTRANS_CHARG. |
| 106 | `FS.GI.TXN.ORDER.BOX.NUMBER` | `FsGiTxnOrder_BoxNumber` | TField |  | Box number to which the confirmed orders will be added for Box management. Multifonds DB Column is NBOX. |
| 107 | `FS.GI.TXN.ORDER.VAL.POINT.CUT.OFF` | `FsGiTxnOrder_ValPointCutOff` | TField |  | Valuation point cut-off as parameterized in the MF fund calendar screen. Multifonds DB Column is DVP_CUT. |
| 108 | `FS.GI.TXN.ORDER.DILUTION.LEVY.PCT` | `FsGiTxnOrder_DilutionLevyPct` | TField |  | Dilution levy percentage applicable for the order. Multifonds DB Column is NDIL_LEVY. |
| 109 | `FS.GI.TXN.ORDER.INTEREST.DUE.AMOUNT` | `FsGiTxnOrder_InterestDueAmount` | TField |  | Order interest due amount. Multifonds DB Column is NINT_DUE_AMT. |
| 110 | `FS.GI.TXN.ORDER.TAX.INT.ADJ.AMOUNT` | `FsGiTxnOrder_TaxIntAdjAmount` | TField |  | Tax interest adjustments amount. Multifonds DB Column is NTAX_INT. |
| 111 | `FS.GI.TXN.ORDER.TAX.CREDIT.ADJ.AMOUNT` | `FsGiTxnOrder_TaxCreditAdjAmount` | TField |  | Tax credit adjustments amount. Multifonds DB Column is NTAX_CREDIT. |
| 112 | `FS.GI.TXN.ORDER.IN.BOX.NUMBER` | `FsGiTxnOrder_InBoxNumber` | TField |  | Box number In for two-leg order. Multifonds DB Column is NBOX_IN. |
| 113 | `FS.GI.TXN.ORDER.INHERIT.G1.G2.FLAG` | `FsGiTxnOrder_InheritG1G2Flag` | TField |  | Flag to trigger inheritance of Group 1 and Group 2 Units following a Switch / Conversion. Multifonds DB Column is FLG_INHERIT_G1G2. |
| 114 | `FS.GI.TXN.ORDER.LOI.AMOUNT` | `FsGiTxnOrder_LoiAmount` | TField |  | Lettler of intent amount. Multifonds DB Column is LOI_AMOUNT. |
| 115 | `FS.GI.TXN.ORDER.MULTI.SERIES.FLAG` | `FsGiTxnOrder_MultiSeriesFlag` | TField |  | Flag to activate the option to place a debit order across multiple series. Multifonds DB Column is FLG_MULTI_SERIES. |
| 116 | `FS.GI.TXN.ORDER.EQ.CR.AMOUNT` | `FsGiTxnOrder_EqCrAmount` | TField |  | Order equalisation credit. Multifonds DB Column is EQUAL_CR. |
| 117 | `FS.GI.TXN.ORDER.EQ.DB.AMOUNT` | `FsGiTxnOrder_EqDbAmount` | TField |  | Order equalisation debit. Multifonds DB Column is EQUAL_DB. |
| 118 | `FS.GI.TXN.ORDER.REVISED.CUMUL.REL.PERF` | `FsGiTxnOrder_RevisedCumulRelPerf` | TField |  | Revised cumulative relative performance amount. Multifonds DB Column is REVISED_CRP. |
| 119 | `FS.GI.TXN.ORDER.REVISED.HWM` | `FsGiTxnOrder_RevisedHwm` | TField |  | Revised high water mark value for performance fees calculation. Multifonds DB Column is REVISED_HWM. |
| 120 | `FS.GI.TXN.ORDER.REVISED.GAV` | `FsGiTxnOrder_RevisedGav` | TField |  | Revised Gross Asset Value amount. Multifonds DB Column is REVISED_GAV. |
| 121 | `FS.GI.TXN.ORDER.NON.CRYST.PF.FLAG` | `FsGiTxnOrder_NonCrystPfFlag` | TField |  | Non crystallization perfomance fee flag of the order. Multifonds DB Column is FLG_NC_PF. |
| 122 | `FS.GI.TXN.ORDER.KIID.FLAG` | `FsGiTxnOrder_KiidFlag` | TField |  | Flag to specify TA KIID compliance. Multifonds DB Column is FLG_KIID. |
| 123 | `FS.GI.TXN.ORDER.GLOBAL.ORDERING.FLAG` | `FsGiTxnOrder_GlobalOrderingFlag` | TField |  | Flag to have the order in scope of the global ordering functionality. Multifonds DB Column is FLG_GLOBAL_ORD. |
| 124 | `FS.GI.TXN.ORDER.TRANSACTION.BULKING.NETTING` | `FsGiTxnOrder_TransactionBulkingNetting` | TField |  | Type of bulking or netting applied to this transaction. Multifonds DB Column is TRNS_BULK_NET. |
| 125 | `FS.GI.TXN.ORDER.EXTERNAL.TA.ID` | `FsGiTxnOrder_ExternalTaId` | TField |  | External TA for global ordering. Multifonds DB Column is EXTERNAL_TA. |
| 126 | `FS.GI.TXN.ORDER.TECHNICAL.REGISTER.ID` | `FsGiTxnOrder_TechnicalRegisterId` | TField |  | Cash dividend or reinvestment register from client level. Multifonds DB Column is NREGISTER_TECH. |
| 127 | `FS.GI.TXN.ORDER.TECHNICAL.IN.REGISTER.ID` | `FsGiTxnOrder_TechnicalInRegisterId` | TField |  | Cash dividend or reinvestment register from client level for two-leg order. Multifonds DB Column is NREGISTER_TECH_IN. |
| 128 | `FS.GI.TXN.ORDER.SENDING.METHOD` | `FsGiTxnOrder_SendingMethod` | TField |  | Sending method populated only if the flag a Global orderinga is ticked at order level. Multifonds DB Column is SENDING_MTHD. |
| 129 | `FS.GI.TXN.ORDER.SENDING.IN.METHOD` | `FsGiTxnOrder_SendingInMethod` | TField |  | Sending method for two-leg order populated only if the flag a Global orderinga is ticked at order level. Multifonds DB Column is SENDING_MTHD_IN. |
| 130 | `FS.GI.TXN.ORDER.CAPITAL.PCT` | `FsGiTxnOrder_CapitalPct` | TField |  | Percentage of the capital that the partner wants to withdraw for limited partnerships. Multifonds DB Column is CAPITAL_PCT. |
| 131 | `FS.GI.TXN.ORDER.CLOSING.FLAG` | `FsGiTxnOrder_ClosingFlag` | TField |  | Flag to indicate that the order is a closing order placed at the end of a break period. Multifonds DB Column is FLG_CLOSING. |
| 132 | `FS.GI.TXN.ORDER.CHANGE.BENEF.OWNER.FLG` | `FsGiTxnOrder_ChangeBenefOwnerFlg` | TField |  | Flag to indicate change of beneficial owner. Multifonds DB Column is FLG_CHG_BENEFICIAL. |
| 133 | `FS.GI.TXN.ORDER.PROCESS.ID` | `FsGiTxnOrder_ProcessId` | TField |  | Order process ID. Multifonds DB Column is NPROCESS. |
| 134 | `FS.GI.TXN.ORDER.PROXY.ID` | `FsGiTxnOrder_ProxyId` | TField |  | External proxy ID for joint account registers. Multifonds DB Column is PROXY. |
| 135 | `FS.GI.TXN.ORDER.ACCOUNT.REFERENCE` | `FsGiTxnOrder_AccountReference` | TField |  | Client identification reference, e.g. passport number. Multifonds DB Column is ID_NO. |
| 136 | `FS.GI.TXN.ORDER.BIRTH.DATE` | `FsGiTxnOrder_BirthDate` | TField |  | Date of birth of the Proxy of the register. Multifonds DB Column is DATE_NAIS. |
| 137 | `FS.GI.TXN.ORDER.DESCRIPTION` | `FsGiTxnOrder_Description` | TField |  | Free text to enter an order description. Multifonds DB Column is DESCRIPTION. |
| 138 | `FS.GI.TXN.ORDER.ORDER.LIMIT.CONDITION` | `FsGiTxnOrder_OrderLimitCondition` | TField |  | Order limit Condition ID. Multifonds DB Column is NCONDITION. |
| 139 | `FS.GI.TXN.ORDER.CHANGED.ALL.POS.FLAG` | `FsGiTxnOrder_ChangedAllPosFlag` | TField |  | Flag to indicate that complete register positions will be redeemed. Multifonds DB Column is CHANGED_ALL_POS. |
| 140 | `FS.GI.TXN.ORDER.TAX.ID.COMMENT` | `FsGiTxnOrder_TaxIdComment` | TField |  | Free text field to mention any comments relating to this order. Multifonds DB Column is COMMENTS. |
| 141 | `FS.GI.TXN.ORDER.PRODUCT.CODE` | `FsGiTxnOrder_ProductCode` | TField |  | Retail product ID for the order. Multifonds DB Column is NPROD. |
| 142 | `FS.GI.TXN.ORDER.REMAINING.QUANTITY` | `FsGiTxnOrder_RemainingQuantity` | TField |  | Order remaining quantity. Multifonds DB Column is NREMAIN_QTY. |
| 143 | `FS.GI.TXN.ORDER.SETTLEMENT.MONEY.CODE` | `FsGiTxnOrder_SettlementMoneyCode` | TField |  | Settlement of money for saving plan and/or subscription transaction. Multifonds DB Column is CSETTLE_MONEY. |
| 144 | `FS.GI.TXN.ORDER.WITH.CASH.ACCT.MNGT.FLG` | `FsGiTxnOrder_WithCashAcctMngtFlg` | TField |  | Flag to indicate that order is in scope of cash account management. Multifonds DB Column is FLG_CASH_SEC_ORD. |
| 145 | `FS.GI.TXN.ORDER.SALESMAN.ID` | `FsGiTxnOrder_SalesmanId` | TField |  | Salesman ID. Multifonds DB Column is NOUTLET_SMAN. |
| 146 | `FS.GI.TXN.ORDER.EST.TOTAL.PAY.AMT` | `FsGiTxnOrder_EstTotalPayAmt` | TField |  | Estimated total amount to pay. Multifonds DB Column is EST_TOT_AMT_PAY. |
| 147 | `FS.GI.TXN.ORDER.QUANTITY.ROUNDING.TYPE` | `FsGiTxnOrder_QuantityRoundingType` | TField |  | Quantity rounding method. Multifonds DB Column is TYPE_ARRONDI. |
| 148 | `FS.GI.TXN.ORDER.QUANTITY.DECIMALS` | `FsGiTxnOrder_QuantityDecimals` | TField |  | Decimal points applicable for the quantity. Multifonds DB Column is CODE_ARRONDI_QT. |
| 149 | `FS.GI.TXN.ORDER.FORWARD.DATE` | `FsGiTxnOrder_ForwardDate` | TField |  | Flag to indicate a forward dated order. Multifonds DB Column is FLG_FWD_DT. |
| 150 | `FS.GI.TXN.ORDER.ERISA.WARN.OVERR.FLG` | `FsGiTxnOrder_ErisaWarnOverrFlg` | TField |  | Flag to override ERISA warning on threshold percentage. Multifonds DB Column is FLG_ERISA_OVERRIDE. |
| 151 | `FS.GI.TXN.ORDER.BLOCK.FOR.SETTLE.REASON.FLG` | `FsGiTxnOrder_BlockForSettleReasonFlg` | TField |  | Dividend blocked for settlement reason. Multifonds DB Column is FLG_BLK_FOR_SETT_REASON. |
| 152 | `FS.GI.TXN.ORDER.CLIENT.TRAD.DESK.CODE` | `FsGiTxnOrder_ClientTradDeskCode` | TField |  | Client trading desk code used in this order for FX exporting. Multifonds DB Column is CLIENT_TDSK. |
| 153 | `FS.GI.TXN.ORDER.IN.TRADE.DATE` | `FsGiTxnOrder_InTradeDate` | TField |  | Trade date for two-leg order. Multifonds DB Column is DATE_EXE_IN. |
| 154 | `FS.GI.TXN.ORDER.IN.VALUE.DATE` | `FsGiTxnOrder_InValueDate` | TField |  | Value date for two-leg order. Multifonds DB Column is DVALEUR_IN. |
| 155 | `FS.GI.TXN.ORDER.DOCUMENT.HANDLING` | `FsGiTxnOrder_DocumentHandling` | TField |  | Investor correspondence handling code at order level. Multifonds DB Column is DOC_HANDLING. |
| 156 | `FS.GI.TXN.ORDER.TRUST.RECEIVED.DATE` | `FsGiTxnOrder_TrustReceivedDate` | TField |  | Date and time order is received from trusted STP counterparty source. Multifonds DB Column is CUT_OFF_TS. |
| 157 | `FS.GI.TXN.ORDER.STP.SENDER` | `FsGiTxnOrder_StpSender` | TField |  | STP counterparty address. Multifonds DB Column is SENDER_STP. |
| 158 | `FS.GI.TXN.ORDER.SWIFT.NARRATIVE` | `FsGiTxnOrder_SwiftNarrative` | TField |  | Narrative in SWIFT message. Multifonds DB Column is SWIFT_NARRATIVE. |
| 159 | `FS.GI.TXN.ORDER.EST.AMOUNT.APPLI.CCY` | `FsGiTxnOrder_EstAmountAppliCcy` | TField |  | Estimated amount in application currency. Multifonds DB Column is EST_AMT_APP_CCY. |
| 160 | `FS.GI.TXN.ORDER.INTRUCTION.PROCESS.ID` | `FsGiTxnOrder_IntructionProcessId` | TField |  | Instruction batch process ID. Multifonds DB Column is INST_PROCESS_ID. |
| 161 | `FS.GI.TXN.ORDER.FUND.TRADING.DESK.PROCESS` | `FsGiTxnOrder_FundTradingDeskProcess` | TField |  | Fund trading desk process code. Multifonds DB Column is FUND_TDSK_PROC. |
| 162 | `FS.GI.TXN.ORDER.REGISTER.ACCOUNT.REF` | `FsGiTxnOrder_RegisterAccountRef` | TField |  | Register account reference. Multifonds DB Column is REG_ID_NO. |
| 163 | `FS.GI.TXN.ORDER.REDEEM.LIFO.FLAG` | `FsGiTxnOrder_RedeemLifoFlag` | TField |  | Flag to indicate redempotion is in last in first out method. Multifonds DB Column is FLG_RED_LIFO. |
| 164 | `FS.GI.TXN.ORDER.TRANSACTION.DATE` | `FsGiTxnOrder_TransactionDate` | TField |  | Transaction date auto-populated from application date. Multifonds DB Column is TRANS_DATE. |
| 165 | `FS.GI.TXN.ORDER.GATING.ORDER.ID` | `FsGiTxnOrder_GatingOrderId` | TField |  | Gating order number. Multifonds DB Column is NORDER_GATING. |
| 166 | `FS.GI.TXN.ORDER.PE.RE.COMMENT` | `FsGiTxnOrder_PeReComment` | TField |  | PE/RE comment code. Multifonds DB Column is PE_RE_COMMENT. |
| 167 | `FS.GI.TXN.ORDER.STRUCTURING.FEES.AMT` | `FsGiTxnOrder_StructuringFeesAmt` | TField |  | Structuring fees. Multifonds DB Column is STRUCTURE_FEES_AMT. |
| 168 | `FS.GI.TXN.ORDER.LATE.PAYMENT.INTEREST` | `FsGiTxnOrder_LatePaymentInterest` | TField |  | Late payment interest. Multifonds DB Column is LATE_PYMT_INT. |
| 169 | `FS.GI.TXN.ORDER.REGISTER.ACCOUNT.REF.2` | `FsGiTxnOrder_RegisterAccountRef2` | TField |  | Register account reference 2. Multifonds DB Column is REG_ID_NO2. |
| 170 | `FS.GI.TXN.ORDER.REDEMPTION.AMOUNT` | `FsGiTxnOrder_RedemptionAmount` | TField |  | The amount for debit transaction or switch when order is placed in amount and not quantity. Multifonds DB Column is REDMP_AMOUNT. |
| 171 | `FS.GI.TXN.ORDER.SUBSCRIPTION.QUANTITY` | `FsGiTxnOrder_SubscriptionQuantity` | TField |  | The quantity for credit transaction or switch when order is placed in quantity and not amount. Multifonds DB Column is SUB_QUANTITY. |
| 172 | `FS.GI.TXN.ORDER.REDEMPTION.CONTRACT.ID` | `FsGiTxnOrder_RedemptionContractId` | TField |  | Redemption Contract ID used for the operation code &apos;0022&apos;(Export Parts). Multifonds DB Column is REDEMP_NCONTRACT. |
| 173 | `FS.GI.TXN.ORDER.ORIGINAL.CASH.FLAG` | `FsGiTxnOrder_OriginalCashFlag` | TField |  | Original cash. Multifonds DB Column is MIG_ORG_CASH. |
| 174 | `FS.GI.TXN.ORDER.ADVISED.TRS.FLAG` | `FsGiTxnOrder_AdvisedTrsFlag` | TField |  | Advised transaction. Multifonds DB Column is ADVISED_TRN. |
| 175 | `FS.GI.TXN.ORDER.EXCLUDE.FROM.NET.FLAG` | `FsGiTxnOrder_ExcludeFromNetFlag` | TField |  | Flag to exclude order from Swinging Single Price (SSP) Netting. Multifonds DB Column is FLG_EXCL_NET. |
| 176 | `FS.GI.TXN.ORDER.EXCL.FROM.NET.MVT.FLAG` | `FsGiTxnOrder_ExclFromNetMvtFlag` | TField |  | Flag to exclude two-leg order from Swinging Single Price (SSP) Netting. Multifonds DB Column is FLG_EXCL_NET_IN. |
| 177 | `FS.GI.TXN.ORDER.ROLLOVER.FLG` | `FsGiTxnOrder_RolloverFlg` | TField |  | Flag to indicate that order is a rollover of an existing investment. Multifonds DB Column is FLG_ROLLOVER. |
| 178 | `FS.GI.TXN.ORDER.REJECTED.DATE` | `FsGiTxnOrder_RejectedDate` | TField |  | Rejection timestamp. Multifonds DB Column is DREJECTED. |
| 179 | `FS.GI.TXN.ORDER.REJECTED.USER` | `FsGiTxnOrder_RejectedUser` | TField |  | User who has rejected the record. Multifonds DB Column is REJECTED_BY. |
| 180 | `FS.GI.TXN.ORDER.RELEASED.DATE` | `FsGiTxnOrder_ReleasedDate` | TField |  | Released timestamp. Multifonds DB Column is DRELEASED. |
| 181 | `FS.GI.TXN.ORDER.RELEASED.USER` | `FsGiTxnOrder_ReleasedUser` | TField |  | User who has released the record. Multifonds DB Column is RELEASED_BY. |
| 182 | `FS.GI.TXN.ORDER.BLOCKED.QUANTITY` | `FsGiTxnOrder_BlockedQuantity` | TField |  | Blocked quantity for the register and fund. Multifonds DB Column is BLOCKED_QUANTITY. |
| 183 | `FS.GI.TXN.ORDER.RECEIVED.AMOUNT` | `FsGiTxnOrder_ReceivedAmount` | TField |  | Order received amount. Multifonds DB Column is RECIEVED_AMOUNT. |
| 184 | `FS.GI.TXN.ORDER.PRINT.FLAG` | `FsGiTxnOrder_PrintFlag` | TField |  | Order Print Flag. Multifonds DB Column is FLAG_PRINT. |
| 185 | `FS.GI.TXN.ORDER.TRADE.DATE` | `FsGiTxnOrder_TradeDate` | TField |  | Trade Date on which NAV is to be applied for the order. Multifonds DB Column is DOPER. |
| 186 | `FS.GI.TXN.ORDER.PAYMENT.STATUS` | `FsGiTxnOrder_PaymentStatus` | TField |  | Status of payments related to this order. Multifonds DB Column is PAY_STATUS. |
| 187 | `FS.GI.TXN.ORDER.PAYMENT.CONFIRM.USER` | `FsGiTxnOrder_PaymentConfirmUser` | TField |  | User who confirms the payment. Multifonds DB Column is PAY_CONFIRM. |
| 188 | `FS.GI.TXN.ORDER.FEES.FLAG` | `FsGiTxnOrder_FeesFlag` | TField |  | Order Fees Flag. Multifonds DB Column is FLG_FEES. |
| 189 | `FS.GI.TXN.ORDER.POR.ORDER.ID` | `FsGiTxnOrder_PorOrderId` | TField |  | POR Order ID. Multifonds DB Column is NORDER_POR. |
| 190 | `FS.GI.TXN.ORDER.REG.ORDER.ID` | `FsGiTxnOrder_RegOrderId` | TField |  | Register Order ID Multifonds DB Column is NORDER_REG. |
| 191 | `FS.GI.TXN.ORDER.FX.TRADING.DESK.FLAG` | `FsGiTxnOrder_FxTradingDeskFlag` | TField |  | Flag to identify an order in scope of FX trading desk processing. Multifonds DB Column is FLG_TRADE_DESK. |
| 192 | `FS.GI.TXN.ORDER.CONFIRM.DATE` | `FsGiTxnOrder_ConfirmDate` | TField |  | Order confirmation date. Multifonds DB Column is DATE_CONFIRM. |
| 193 | `FS.GI.TXN.ORDER.EST.CALC.QUANTITY` | `FsGiTxnOrder_EstCalcQuantity` | TField |  | Estimated quantity calculated when an order is placed in amount. Multifonds DB Column is CAL_QUANTITY. |
| 194 | `FS.GI.TXN.ORDER.APPLIED.FUND.FX.RATE` | `FsGiTxnOrder_AppliedFundFxRate` | TField |  | Fund FX rate applicable for the order. Multifonds DB Column is TAUX_USER_NPTF. |
| 195 | `FS.GI.TXN.ORDER.FUND.RATE.INDICATOR` | `FsGiTxnOrder_FundRateIndicator` | TField |  | Field indicating the application of fund FX rate is to divide or multiply. Multifonds DB Column is RATE_INDICATOR_NPTF. |
| 196 | `FS.GI.TXN.ORDER.APPLIED.FUND.FX.RATE.2` | `FsGiTxnOrder_AppliedFundFxRate2` | TField |  | Fund FX rate applicable for two-leg order. Multifonds DB Column is TAUX_USER_NPTF2. |
| 197 | `FS.GI.TXN.ORDER.FUND.RATE.INDICATOR.2` | `FsGiTxnOrder_FundRateIndicator2` | TField |  | Field indicating the application of fund FX rate is to divide or multiply. Multifonds DB Column is RATE_INDICATOR_NPTF2. |
| 198 | `FS.GI.TXN.ORDER.REDEMPTION.METHOD` | `FsGiTxnOrder_RedemptionMethod` | TField |  | Method to select shares to redeem. Linked to group of redemption methods setup for CDSC. Multifonds DB Column is METHOD. |
| 199 | `FS.GI.TXN.ORDER.CDSC.FLAG` | `FsGiTxnOrder_CdscFlag` | TField |  | Flag to indicate that order use condingent deferred sales charge. Multifonds DB Column is USE_CDSC. |
| 200 | `FS.GI.TXN.ORDER.CDSC.AGENT.ID` | `FsGiTxnOrder_CdscAgentId` | TField |  | Prefinancing agent id for CDSC. Multifonds DB Column is NOUTLET_CDSC. |
| 201 | `FS.GI.TXN.ORDER.FUND.CAT.REST.MARGIN.PCT` | `FsGiTxnOrder_FundCatRestMarginPct` | TField |  | Margin percentage used in the investment restriction functionality based on fund category. Multifonds DB Column is MARGIN_PCT. |
| 202 | `FS.GI.TXN.ORDER.EXTERNAL.ID` | `FsGiTxnOrder_ExternalId` | TField |  | Security identifier code. Multifonds DB Column is SECID. |
| 203 | `FS.GI.TXN.ORDER.EXTERNAL.ID.2` | `FsGiTxnOrder_ExternalId2` | TField |  | Security identifier code for two-leg order. Multifonds DB Column is SECID2. |
| 204 | `FS.GI.TXN.ORDER.CONF.PLUS.USER.FLG` | `FsGiTxnOrder_ConfPlusUserFlg` | TField |  | Flag to specify active confirmation plus user is required. Multifonds DB Column is FLG_USER_CONFIRM_PLUS. |
| 205 | `FS.GI.TXN.ORDER.CONF.PLUS.USER` | `FsGiTxnOrder_ConfPlusUser` | TField |  | Active confirmation plus user. Multifonds DB Column is USER_CONFIRM_PLUS. |
| 206 | `FS.GI.TXN.ORDER.COMM.AGENT.ID` | `FsGiTxnOrder_CommAgentId` | TField |  | Commission percentage rate paid to agent or intermediary. Multifonds DB Column is NOUTLET_COMM. |
| 207 | `FS.GI.TXN.ORDER.COMM.METHOD` | `FsGiTxnOrder_CommMethod` | TField |  | Commission method applicable for the order. Multifonds DB Column is COMM_METHOD. |
| 208 | `FS.GI.TXN.ORDER.UK.REGISTER.TYPE` | `FsGiTxnOrder_UkRegisterType` | TField |  | Secondary reg type for UK register. Multifonds DB Column is CREG_TYPE. |
| 209 | `FS.GI.TXN.ORDER.MARKET.CODE` | `FsGiTxnOrder_MarketCode` | TField |  | Order market code. Multifonds DB Column is CMKT_CODE. |
| 210 | `FS.GI.TXN.ORDER.INSTRUCTION.ID.2` | `FsGiTxnOrder_InstructionId2` | TField |  | Order instruction ID for two-leg order. Multifonds DB Column is NINSTRUCTION2. |
| 211 | `FS.GI.TXN.ORDER.USE.CLIENT.FLAG` | `FsGiTxnOrder_UseClientFlag` | TField |  | Use client flag. Multifonds DB Column is FLG_USE_CLI. |
| 212 | `FS.GI.TXN.ORDER.BOX.STATUS` | `FsGiTxnOrder_BoxStatus` | TField |  | Order Box Status. Multifonds DB Column is CBOX_STATUS. |
| 213 | `FS.GI.TXN.ORDER.ORDER.ALLOC.FLAG` | `FsGiTxnOrder_OrderAllocFlag` | TField |  | Asset allocation flag. Multifonds DB Column is CFLG_ALLOC. |
| 214 | `FS.GI.TXN.ORDER.SITE.ID` | `FsGiTxnOrder_SiteId` | TField |  | Site ID of the order. Multifonds DB Column is SITE_ID. |
| 215 | `FS.GI.TXN.ORDER.ADL.AMOUNT.PAY.CCY` | `FsGiTxnOrder_AdlAmountPayCcy` | TField |  | ADL Amount expressed in payment currency. Multifonds DB Column is ADL_AMOUNT_PAY. |
| 216 | `FS.GI.TXN.ORDER.SWITCH.ORDER.ID` | `FsGiTxnOrder_SwitchOrderId` | TField |  | Order number for switch transaction. Multifonds DB Column is SWITCH_ORDER. |
| 217 | `FS.GI.TXN.ORDER.NET.AMOUNT` | `FsGiTxnOrder_NetAmount` | TField |  | Net amount of the order. Multifonds DB Column is NET_AMOUNT. |
| 218 | `FS.GI.TXN.ORDER.FLAT.CHARGE.FLAG` | `FsGiTxnOrder_FlatChargeFlag` | TField |  | Flag to specify flat charge is applicable for the order. Multifonds DB Column is FLG_FLAT_CHARGE. |
| 219 | `FS.GI.TXN.ORDER.EXCEPT.MGMT.COMM` | `FsGiTxnOrder_ExceptMgmtComm` | TField |  | Exception management commission of the order. Multifonds DB Column is EXCEPT_MGMT_COMM. |
| 220 | `FS.GI.TXN.ORDER.SPLIT.MANAGER` | `FsGiTxnOrder_SplitManager` | TField |  | Split manager of the order. Multifonds DB Column is SPLIT_MANAGER. |
| 221 | `FS.GI.TXN.ORDER.SPLIT.PCT` | `FsGiTxnOrder_SplitPct` | TField |  | Split percentage of the order. Multifonds DB Column is SPLIT_PCT. |
| 222 | `FS.GI.TXN.ORDER.SPLIT.AMOUNT` | `FsGiTxnOrder_SplitAmount` | TField |  | Split amount of the order. Multifonds DB Column is SPLIT_AMOUNT. |
| 223 | `FS.GI.TXN.ORDER.ASSIGNMENT.STATUS` | `FsGiTxnOrder_AssignmentStatus` | TField |  | Order assignment Status. Multifonds DB Column is ASSIGN_STATUS. |
| 224 | `FS.GI.TXN.ORDER.PRE.ORDER.COMMENT` | `FsGiTxnOrder_PreOrderComment` | TField |  | Order comments added at pre-order stage. Multifonds DB Column is PRE_COMMENTS. |
| 225 | `FS.GI.TXN.ORDER.INTERNAL.REFERENCE.EXT` | `FsGiTxnOrder_InternalReferenceExt` | TField |  | Order internal reference extension. Multifonds DB Column is INT_REF_EXTN. |
| 226 | `FS.GI.TXN.ORDER.REGISTER.IN.BLOCK.CODE` | `FsGiTxnOrder_RegisterInBlockCode` | TField |  | Blocking code for register dor two-leg order. Multifonds DB Column is REG_BLK_CODE_IN. |
| 227 | `FS.GI.TXN.ORDER.CLIENT.IN.BLOCK.CODE` | `FsGiTxnOrder_ClientInBlockCode` | TField |  | Blocking code for client for two-leg order. Multifonds DB Column is CLI_BLK_CODE_IN. |
| 228 | `FS.GI.TXN.ORDER.REGISTER.OUT.BLOCK.CODE` | `FsGiTxnOrder_RegisterOutBlockCode` | TField |  | Blocking code for register. Multifonds DB Column is REG_BLK_CODE_OUT. |
| 229 | `FS.GI.TXN.ORDER.CLIENT.OUT.BLOCK.CODE` | `FsGiTxnOrder_ClientOutBlockCode` | TField |  | Blocking code for client. Multifonds DB Column is CLI_BLK_CODE_OUT. |
| 230 | `FS.GI.TXN.ORDER.FUND.OF.FUND.ORDER.ID` | `FsGiTxnOrder_FundOfFundOrderId` | TField |  | Fund of Funds order ID. Multifonds DB Column is NORDER_FOF. |
| 231 | `FS.GI.TXN.ORDER.FUND.OF.FUND.AGENT.ID` | `FsGiTxnOrder_FundOfFundAgentId` | TField |  | Fund of Funds agent ID. Multifonds DB Column is NOUTLET_FOF. |
| 232 | `FS.GI.TXN.ORDER.INVESTOR.ID` | `FsGiTxnOrder_InvestorId` | TField |  | Client ID populated when client is selected at pre-order stage as part of nominee account processing. Multifonds DB Column is NCLIENT. |
| 233 | `FS.GI.TXN.ORDER.SOS.FLAG` | `FsGiTxnOrder_SosFlag` | TField |  | Series of shares flag. Multifonds DB Column is FLG_SOS. |
| 234 | `FS.GI.TXN.ORDER.COMM.TYPE` | `FsGiTxnOrder_CommType` | TField |  | Commission type applicable for the order. Multifonds DB Column is TYPE_COMM. |
| 235 | `FS.GI.TXN.ORDER.COMM.IN.TYPE` | `FsGiTxnOrder_CommInType` | TField |  | Commission type applicable for the two-leg order. Multifonds DB Column is TYPE_COMM_IN. |
| 236 | `FS.GI.TXN.ORDER.ORDER.COMM.AMT` | `FsGiTxnOrder_OrderCommAmt` | TField |  | Amount or percentage of commission applicable for the order based on commission type setup. Multifonds DB Column is ORD_COMM. |
| 237 | `FS.GI.TXN.ORDER.ORDER.COMM.IN.AMT` | `FsGiTxnOrder_OrderCommInAmt` | TField |  | Amount or percentage of commission applicable for two-leg order based on commission type setup. Multifonds DB Column is ORD_COMM_IN. |
| 238 | `FS.GI.TXN.ORDER.ORDER.COMM.CCY` | `FsGiTxnOrder_OrderCommCcy` | TField |  | Commission currency for the order. Multifonds DB Column is ORD_COMM_CCY. |
| 239 | `FS.GI.TXN.ORDER.ORDER.COMM.IN.CCY` | `FsGiTxnOrder_OrderCommInCcy` | TField |  | Commission currency for two-leg order. Multifonds DB Column is ORD_COMM_CCY_IN. |
| 240 | `FS.GI.TXN.ORDER.AGENT.COMM.PCT` | `FsGiTxnOrder_AgentCommPct` | TField |  | Agent commission percentage. Multifonds DB Column is OUTLET_TUC_PCT. |
| 241 | `FS.GI.TXN.ORDER.AGENT.COMM.SCALE.CODE` | `FsGiTxnOrder_AgentCommScaleCode` | TField |  | Agent commission scale code required for commission type &apos;Scale&apos;. Multifonds DB Column is CSCALE_OUTLET_COMM. |
| 242 | `FS.GI.TXN.ORDER.AGENT.COMM.IN.PCT` | `FsGiTxnOrder_AgentCommInPct` | TField |  | Agent commission percentage for two-leg oder. Multifonds DB Column is OUTLET_TUC_PCT_IN. |
| 243 | `FS.GI.TXN.ORDER.AGENT.COMM.IN.SCALE.CODE` | `FsGiTxnOrder_AgentCommInScaleCode` | TField |  | Agent commission scale code for two-leg order required for commission type &apos;Scale&apos;. Multifonds DB Column is CSCALE_OUTLET_COMM_IN. |
| 244 | `FS.GI.TXN.ORDER.FORCED.COMM.FLAG` | `FsGiTxnOrder_ForcedCommFlag` | TField |  | Flag to indicate commission is forced. Multifonds DB Column is FLG_FORCE_COMM. |
| 245 | `FS.GI.TXN.ORDER.AUTO.GENERATED.ORDER.FLG` | `FsGiTxnOrder_AutoGeneratedOrderFlg` | TField |  | Flag to indicate order is auto generated. Multifonds DB Column is FLG_AUTO_ORD. |
| 246 | `FS.GI.TXN.ORDER.SSP.INCLUDE.FLAG` | `FsGiTxnOrder_SspIncludeFlag` | TField |  | Include in Swinging Single Price (SSP). Multifonds DB Column is FLG_SSP_INCLUDE. |
| 247 | `FS.GI.TXN.ORDER.NON.CRYST.SP.FLAG` | `FsGiTxnOrder_NonCrystSpFlag` | TField |  | Flag to specifuy that the switch out transaction is processed using the GAV price and not the NAV price. Multifonds DB Column is FLG_NON_CRYST_SP. |
| 248 | `FS.GI.TXN.ORDER.SELECTED.PRICE` | `FsGiTxnOrder_SelectedPrice` | TField |  | Type of price to be used from set up done at &apos;ADL parameter&apos; or &apos;Select price&apos; screen. Multifonds DB Column is SELECT_PRICE. |
| 249 | `FS.GI.TXN.ORDER.SELECTED.IN.PRICE` | `FsGiTxnOrder_SelectedInPrice` | TField |  | Type of price to be used for two-leg order from set up done at &apos;ADL parameter&apos; or &apos;Select price&apos; screen. Multifonds DB Column is SELECT_PRICE_IN. |
| 250 | `FS.GI.TXN.ORDER.MIGRATED.FLAG` | `FsGiTxnOrder_MigratedFlag` | TField |  | Flag to indicate that the transaction is linked to the payment module. Multifonds DB Column is MIG_FLAG. |
| 251 | `FS.GI.TXN.ORDER.NEW.POSITION.FLAG` | `FsGiTxnOrder_NewPositionFlag` | TField |  | New position flag. Multifonds DB Column is FLG_NEW_POSITION. |
| 252 | `FS.GI.TXN.ORDER.MANUAL.UPDATE.FLAG` | `FsGiTxnOrder_ManualUpdateFlag` | TField |  | Flag to not count orders for pending warning messages if deal status is manually changed. Multifonds DB Column is FLG_MANUAL_UPDATE. |
| 253 | `FS.GI.TXN.ORDER.CR.DEAL.REFERENCE` | `FsGiTxnOrder_CrDealReference` | TField |  | Credit deal reference of a contract related to a reinvestment order when non-settlement of the credit deal reference is delaying reinvestment. Multifonds DB Column is DEAL_REF_CR. |
| 254 | `FS.GI.TXN.ORDER.CR.CONTRACT.ID` | `FsGiTxnOrder_CrContractId` | TField |  | Credit contract number of a contract related to a reinvestment order when non-settlement of the credit contract is delaying reinvestment. Multifonds DB Column is NCONTRACT_CR. |
| 255 | `FS.GI.TXN.ORDER.CR.FUND.ID` | `FsGiTxnOrder_CrFundId` | TField |  | Credit Fund ID. Multifonds DB Column is NPTF_CR. |
| 256 | `FS.GI.TXN.ORDER.CR.SHARE.CLASS.CODE` | `FsGiTxnOrder_CrShareClassCode` | TField |  | Credit Share Class ID. Multifonds DB Column is TPART_CR. |
| 257 | `FS.GI.TXN.ORDER.CLIENT.TRAD.DESK.FLAG` | `FsGiTxnOrder_ClientTradDeskFlag` | TField |  | Flag to indicate client FX is required for the order. Multifonds DB Column is FLG_CLIENT_FX. |
| 258 | `FS.GI.TXN.ORDER.FORCED.CLIENT.FX.FLAG` | `FsGiTxnOrder_ForcedClientFxFlag` | TField |  | Flag to indicate that exchange rate is forced at order entry. Multifonds DB Column is FLG_FORCED_FX. |
| 259 | `FS.GI.TXN.ORDER.CANC.FX.PL.CCY` | `FsGiTxnOrder_CancFxPlCcy` | TField |  | Currency in which FX profit/loss is calculated during client trading desk processing. Multifonds DB Column is CMON_FX_PL_CALC_CANC. |
| 260 | `FS.GI.TXN.ORDER.REV.FX.PL.CALC.DATE` | `FsGiTxnOrder_RevFxPlCalcDate` | TField |  | Date of the calculation of profit/loss for reversal order. Multifonds DB Column is DFX_REV_PL_CALC. |
| 261 | `FS.GI.TXN.ORDER.REV.CLIENT.FX` | `FsGiTxnOrder_RevClientFx` | TField |  | Client FX reversal method. Multifonds DB Column is CLI_FX_REV. |
| 262 | `FS.GI.TXN.ORDER.SWIFT.MSG.SENT.FLAG` | `FsGiTxnOrder_SwiftMsgSentFlag` | TField |  | Flag to specify whether swift cancellation message should be sent. Multifonds DB Column is FLG_SWIFT_CAN_MSG_SENT. |
| 263 | `FS.GI.TXN.ORDER.SWIFT.CANC.REASON.CODE` | `FsGiTxnOrder_SwiftCancReasonCode` | TField | Yes | Swift cancellation reason code: Mandatory if the swift cancel message flag is Y. Multifonds DB Column is SWIFT_CAN_MSG_CODE. |
| 264 | `FS.GI.TXN.ORDER.ERR.CORRECTION.ID` | `FsGiTxnOrder_ErrCorrectionId` | TField |  | Error/Correction Identifier for a correction or reversal deal. Multifonds DB Column is ERR_CORR_ID. |
| 265 | `FS.GI.TXN.ORDER.CORRECTIVE.PAYMENT.FLAG` | `FsGiTxnOrder_CorrectivePaymentFlag` | TField |  | Corrective payment indicator for automated correction payment generation. Multifonds DB Column is FLG_CORR_PAY. |
| 266 | `FS.GI.TXN.ORDER.ACTUAL.TRADE.DATE` | `FsGiTxnOrder_ActualTradeDate` | TField |  | Actual trade date for the order used to calculate the P/L correction. Multifonds DB Column is ACT_TD. |
| 267 | `FS.GI.TXN.ORDER.ACTUAL.VALUE.DATE` | `FsGiTxnOrder_ActualValueDate` | TField |  | Actual value date of this order used for payment processing. Multifonds DB Column is ACT_VD. |
| 268 | `FS.GI.TXN.ORDER.PROFIT.LOSS.METHOD` | `FsGiTxnOrder_ProfitLossMethod` | TField |  | Method used for Profit and Loss calculation. This impacts the calculation of the reversal value date. Multifonds DB Column is PL_METHOD. |
| 269 | `FS.GI.TXN.ORDER.REV.CONTRACT.NOTE.FLG` | `FsGiTxnOrder_RevContractNoteFlg` | TField |  | Flag to produce contract note on reversal. Multifonds DB Column is FLG_CONT_NOTE. |
| 270 | `FS.GI.TXN.ORDER.REV.PAYMENT.MADE.FLAG` | `FsGiTxnOrder_RevPaymentMadeFlag` | TField |  | Flag to specify whether payments have been made for this reversal deal. Multifonds DB Column is FLG_PAY_MADE. |
| 271 | `FS.GI.TXN.ORDER.UNMATCH.RECEIPT.FLAG` | `FsGiTxnOrder_UnmatchReceiptFlag` | TField |  | Un-match receipt flag to control display of cleared funds. Multifonds DB Column is FLG_UNMATCH_RECPT. |
| 272 | `FS.GI.TXN.ORDER.CLIENT.TR.DSK.FORCED.RATE` | `FsGiTxnOrder_ClientTrDskForcedRate` | TField |  | Client trading desk external exchange rate received for order for which the exchange rate was forced during creation. Multifonds DB Column is CTD_EXCH_RATE. |
| 273 | `FS.GI.TXN.ORDER.CLIENT.TR.DSK.FORCED.INDIC` | `FsGiTxnOrder_ClientTrDskForcedIndic` | TField |  | Divide/Multiply for the client trading desk forced external exchange rate . Multifonds DB Column is CTD_RATE_INDICATE. |
| 274 | `FS.GI.TXN.ORDER.GL.POSTINGS.FLAG` | `FsGiTxnOrder_GlPostingsFlag` | TField |  | Flag to decide whether GL posting is required for the order. Multifonds DB Column is GL_POSTINGS. |
| 275 | `FS.GI.TXN.ORDER.GL.IN.POSTINGS.FLAG` | `FsGiTxnOrder_GlInPostingsFlag` | TField |  | Flag to decide whether GL posting is required for the two-leg order. Multifonds DB Column is GL_POSTINGS_IN. |
| 276 | `FS.GI.TXN.ORDER.SWITCH.IN.CALC.NAV.DATE` | `FsGiTxnOrder_SwitchInCalcNavDate` | TField |  | Price date for switch in calculated by applying the hard and soft conditional trade date rules. Multifonds DB Column is PRICE_DATE_IN. |
| 277 | `FS.GI.TXN.ORDER.SWITCH.OUT.CALC.NAV.DATE` | `FsGiTxnOrder_SwitchOutCalcNavDate` | TField |  | Price date for switch out calculated by applying the hard and soft conditional trade date rules. Multifonds DB Column is PRICE_DATE_OUT. |
| 278 | `FS.GI.TXN.ORDER.LEGAL.ENTITY.SWITCH.TR.DATE` | `FsGiTxnOrder_LegalEntitySwitchTrDate` | TField |  | Trade date for switch method for Legal Entity linked to the order. Multifonds DB Column is TFC_SWITCH_TD. |
| 279 | `FS.GI.TXN.ORDER.CANCEL.REVERSE.FLAG` | `FsGiTxnOrder_CancelReverseFlag` | TField |  | Flag to specify order is cancelled or reversed. Multifonds DB Column is MIG_FLG_CAN_REV. |
| 280 | `FS.GI.TXN.ORDER.FUND.PROMOTER.ID` | `FsGiTxnOrder_FundPromoterId` | TField |  | Fund promoter linked to the order. Multifonds DB Column is NPROMOTER. |
| 281 | `FS.GI.TXN.ORDER.THRESHOLD.FLAG` | `FsGiTxnOrder_ThresholdFlag` | TField |  | Threshold Flag. Multifonds DB Column is FLG_THRESHOLD. |
| 282 | `FS.GI.TXN.ORDER.PROMOTER.ID.2` | `FsGiTxnOrder_PromoterId2` | TField |  | Fund promoter 2 linked to the order. Multifonds DB Column is NPROMOTER2. |
| 283 | `FS.GI.TXN.ORDER.FX.PROCESS.UPDATE.FLAG` | `FsGiTxnOrder_FxProcessUpdateFlag` | TField |  | FX Process update flag. Multifonds DB Column is FLG_UPD_FUND_TDSK_PROC. |
| 284 | `FS.GI.TXN.ORDER.FIRST.SUB.MIN.LIMIT` | `FsGiTxnOrder_FirstSubMinLimit` | TField |  | First sub minimum limit. Multifonds DB Column is FIRST_SUB_MIN_LIMIT. |
| 285 | `FS.GI.TXN.ORDER.FIRST.SUB.MAX.LIMIT` | `FsGiTxnOrder_FirstSubMaxLimit` | TField |  | First sub maximum limit. Multifonds DB Column is FIRST_SUB_MAX_LIMIT. |
| 286 | `FS.GI.TXN.ORDER.TRANS.MIN.LIMIT` | `FsGiTxnOrder_TransMinLimit` | TField |  | Transaction minimum limit. Multifonds DB Column is TRANS_MIN_LIMIT. |
| 287 | `FS.GI.TXN.ORDER.TRANS.MAX.LIMIT` | `FsGiTxnOrder_TransMaxLimit` | TField |  | Transaction maximum limit. Multifonds DB Column is TRANS_MAX_LIMIT. |
| 288 | `FS.GI.TXN.ORDER.HOLDING.LIMIT` | `FsGiTxnOrder_HoldingLimit` | TField |  | Holding limit. Multifonds DB Column is HOLDING_LIMIT. |
| 289 | `FS.GI.TXN.ORDER.ORIGINAL.TRADE.DATE` | `FsGiTxnOrder_OriginalTradeDate` | TField |  | Original trade date. Multifonds DB Column is DATE_EXE_ORIG. |
| 290 | `FS.GI.TXN.ORDER.TRADE.DATE.CHANGE.REASON` | `FsGiTxnOrder_TradeDateChangeReason` | TField |  | Trade date change reason. Multifonds DB Column is REASON_DATE_EXE. |
| 291 | `FS.GI.TXN.ORDER.ORIGINAL.VALUE.DATE` | `FsGiTxnOrder_OriginalValueDate` | TField |  | Original value date . Multifonds DB Column is DVALEUR_ORIG. |
| 292 | `FS.GI.TXN.ORDER.TEMP.ORIG.VALUE.DATE` | `FsGiTxnOrder_TempOrigValueDate` | TField |  | Original value date temp. Multifonds DB Column is DVALEUR_ORIG_TEMP. |
| 293 | `FS.GI.TXN.ORDER.VALUE.DATE.CHANGE.REASON` | `FsGiTxnOrder_ValueDateChangeReason` | TField |  | Value date change reason. Multifonds DB Column is REASON_DVALEUR. |
| 294 | `FS.GI.TXN.ORDER.ORIGINAL.IN.TRADE.DATE` | `FsGiTxnOrder_OriginalInTradeDate` | TField |  | Original trade date for two-leg order. Multifonds DB Column is DATE_EXE_IN_ORIG. |
| 295 | `FS.GI.TXN.ORDER.TRADE.DATE.IN.CHANGE.REASON` | `FsGiTxnOrder_TradeDateInChangeReason` | TField |  | Trade date in change reason. Multifonds DB Column is REASON_DATE_EXE_IN. |
| 296 | `FS.GI.TXN.ORDER.ORIGINAL.IN.VALUE.DATE` | `FsGiTxnOrder_OriginalInValueDate` | TField |  | Original value date for two-leg order. Multifonds DB Column is DVALEUR_IN_ORIG. |
| 297 | `FS.GI.TXN.ORDER.TEMP.ORIG.VALUE.IN.DATE` | `FsGiTxnOrder_TempOrigValueInDate` | TField |  | Original value date for two-leg order temp. Multifonds DB Column is DVALEUR_IN_ORIG_TEMP. |
| 298 | `FS.GI.TXN.ORDER.VALUE.DATE.IN.CHANGE.REASON` | `FsGiTxnOrder_ValueDateInChangeReason` | TField |  | Value Date for the two-leg change reason. Multifonds DB Column is REASON_DVALEUR_IN. |
| 299 | `FS.GI.TXN.ORDER.LARGE.DEAL.IN.THRES.BREACH` | `FsGiTxnOrder_LargeDealInThresBreach` | TField |  | Flag to indicate large deal threshold is breached for the two leg order. Multifonds DB Column is FLG_LD_THRESHOLD_BREACH_IN. |
| 300 | `FS.GI.TXN.ORDER.LARGE.DEAL.IN.ORDER.THRES.AMT` | `FsGiTxnOrder_LargeDealInOrderThresAmt` | TField |  | Large Deal Order Threshold Amt for the in Leg Multifonds DB Column is LD_ORDER_THRESHOLD_AMT_IN. |
| 301 | `FS.GI.TXN.ORDER.LARGE.DEAL.IN.THRES.AMT` | `FsGiTxnOrder_LargeDealInThresAmt` | TField |  | Large Deal Threshold Amt for the in Leg Multifonds DB Column is LD_THRESHOLD_AMT_IN. |
| 302 | `FS.GI.TXN.ORDER.LARGE.DEAL.IN.THRES.CCY` | `FsGiTxnOrder_LargeDealInThresCcy` | TField |  | Large deal threshold currency for two-leg order. Multifonds DB Column is LD_THRESHOLD_CCY_IN. |
| 303 | `FS.GI.TXN.ORDER.LARGE.DEAL.THRES.BREACH.FLG` | `FsGiTxnOrder_LargeDealThresBreachFlg` | TField |  | Flag to indicate large deal threshold is breached for order. Multifonds DB Column is FLG_LD_THRESHOLD_BREACH. |
| 304 | `FS.GI.TXN.ORDER.LARGE.DEAL.ORDER.THRES.AMT` | `FsGiTxnOrder_LargeDealOrderThresAmt` | TField |  | Order amount in threshold currency. Multifonds DB Column is LD_ORDER_THRESHOLD_AMT. |
| 305 | `FS.GI.TXN.ORDER.LARGE.DEAL.THRES.AMT` | `FsGiTxnOrder_LargeDealThresAmt` | TField |  | Threshold amount or percentage applied to the deal as per threshold setup at Promoter, or Legal Entity, or Fund, or Share Class level. Multifonds DB Column is LD_THRESHOLD_AMT. |
| 306 | `FS.GI.TXN.ORDER.LARGE.DEAL.THRES.CCY` | `FsGiTxnOrder_LargeDealThresCcy` | TField |  | Large deal threshold currency for the order. Multifonds DB Column is LD_THRESHOLD_CCY. |
| 307 | `FS.GI.TXN.ORDER.PE.EVENT.FLAG` | `FsGiTxnOrder_PeEventFlag` | TField |  | Private Equity commitments and capital calls flag to identify whether the order is created through event processing or manual creation. Multifonds DB Column is FLG_PE. |
| 308 | `FS.GI.TXN.ORDER.PL.CARRY.FORWARD.AMT` | `FsGiTxnOrder_PlCarryForwardAmt` | TField |  | Profit/Loss carry forward. Multifonds DB Column is LP_MIG_PLCF. |
| 309 | `FS.GI.TXN.ORDER.HURDLE.CARRY.FORWARD.AMT` | `FsGiTxnOrder_HurdleCarryForwardAmt` | TField |  | Hurdle carry forward. Multifonds DB Column is LP_MIG_HCF. |
| 310 | `FS.GI.TXN.ORDER.INSTRUCTION.TYPE` | `FsGiTxnOrder_InstructionType` | TField |  | Instruction type. Multifonds DB Column is INSTRUC_TYPE. |
| 311 | `FS.GI.TXN.ORDER.INSTRUCT.REFERENCE.ID` | `FsGiTxnOrder_InstructReferenceId` | TField |  | Instruction reference ID. Multifonds DB Column is INSTRUC_REF. |
| 312 | `FS.GI.TXN.ORDER.ISA.DEAL.PCT` | `FsGiTxnOrder_IsaDealPct` | TField |  | Percentage of value distributed across rapid orders for Individual Savings Account (ISA) operations. Multifonds DB Column is ISA_RDO_PCT. |
| 313 | `FS.GI.TXN.ORDER.RAPID.DEAL.ORDER.FLAG` | `FsGiTxnOrder_RapidDealOrderFlag` | TField |  | Flag to indicate rapid deal order have been updated in the order entry screen. Multifonds DB Column is FLG_RDO_UPD. |
| 314 | `FS.GI.TXN.ORDER.GATINS.STATUS` | `FsGiTxnOrder_GatinsStatus` | TField |  | Gating order status. Multifonds DB Column is GATING_STATUS. |
| 315 | `FS.GI.TXN.ORDER.ORIG.SUB.DATE` | `FsGiTxnOrder_OrigSubDate` | TField |  | Original subscription date. Multifonds DB Column is SUB_DATE. |
| 316 | `FS.GI.TXN.ORDER.LAST.CRYST.DATE` | `FsGiTxnOrder_LastCrystDate` | TField |  | Last crystallization date. Multifonds DB Column is LAST_CRYST_DATE. |
| 317 | `FS.GI.TXN.ORDER.LAST.CRYST.NAV` | `FsGiTxnOrder_LastCrystNav` | TField |  | Last crystallization NAV. Multifonds DB Column is LAST_CRYST_NAV. |
| 318 | `FS.GI.TXN.ORDER.ISIN` | `FsGiTxnOrder_Isin` | TField |  | ISIN identifiter of the fund share Class. Multifonds DB Column is ISIN. |
| 319 | `FS.GI.TXN.ORDER.FUND.CURRENCY` | `FsGiTxnOrder_FundCurrency` | TField |  | Fund Share Class quotation currency. Multifonds DB Column is CMONREF1. |
| 320 | `FS.GI.TXN.ORDER.EST.AMOUNT.QUOTATION.CCY` | `FsGiTxnOrder_EstAmountQuotationCcy` | TField |  | Estimated Amount in the fund share class quotation currency. Multifonds DB Column is EST_AMT_QUOT. |
| 321 | `FS.GI.TXN.ORDER.ORDER.COMMISSION.METHOD` | `FsGiTxnOrder_OrderCommissionMethod` | TField |  | Commission method applied to the transaction. Multifonds DB Column is XPCT_DISP. |
| 322 | `FS.GI.TXN.ORDER.ORDER.COMMISSION.VALUE` | `FsGiTxnOrder_OrderCommissionValue` | TField |  | Commission value applied to the Transaction. Multifonds DB Column is PCT_DISP. |
| 323 | `FS.GI.TXN.ORDER.IN.ISIN` | `FsGiTxnOrder_InIsin` | TField |  | Leg In ISIN identifiter of the fund share Class. Multifonds DB Column is ISIN2. |
| 324 | `FS.GI.TXN.ORDER.IN.FUND.CURRENCY` | `FsGiTxnOrder_InFundCurrency` | TField |  | Leg In Fund Share Class quotation currency. Multifonds DB Column is CMONREF2. |
| 325 | `FS.GI.TXN.ORDER.FUND.CUT.OFF.TIME` | `FsGiTxnOrder_FundCutOffTime` | TField |  | Fund Cut off time applicable to the transaction. Multifonds DB Column is FUND_CUT_OFF. |
| 326 | `FS.GI.TXN.ORDER.AGENT.CUT.OFF` | `FsGiTxnOrder_AgentCutOff` | TField |  | Agent exeption cut-off time appliacble to the transaction. Multifonds DB Column is OUTLET_CUT_OFF. |
| 327 | `FS.GI.TXN.ORDER.GRACE.PERIOD` | `FsGiTxnOrder_GracePeriod` | TField |  | Manual fund grace period cut-off time applicable to the transaction. Multifonds DB Column is MANUAL_GRACE_PERIOD1. |
| 328 | `FS.GI.TXN.ORDER.EXCHANGE.GROUP` | `FsGiTxnOrder_ExchangeGroup` | TField |  | Exchange Group is linked to the fund in which the order is placed. Exchange Group is used to group several funds having same set of parameters for the transaction life cycle. It be used as the parameter for the Cash Flow forecast reporting, forex reporting , Batch process and end of the day process. Multifonds DB Column is CGROUPE_COURS. |
| 329 | `FS.GI.TXN.ORDER.LP.REDEMPTION.METHOD` | `FsGiTxnOrder_LpRedemptionMethod` | TField |  | Withdrawal method for tranche funds. Multifonds DB Column is RED_METHOD. |
| 330 | `FS.GI.TXN.ORDER.TRANSFER.ROR.HISTORY.FLAG` | `FsGiTxnOrder_TransferRorHistoryFlag` | TField |  | Flag to indicate the RoR history to be transferred to the new investor. Multifonds DB Column is FLG_TRANSFER_ROR. |
| 331 | `FS.GI.TXN.ORDER.ABF.CRYST.OPTION` | `FsGiTxnOrder_AbfCrystOption` | TField |  | Crystallization option for asset based fee Multifonds DB Column is CFEE_CRYST_ABF. |
| 332 | `FS.GI.TXN.ORDER.INC.FEE.CRYST.OPTION` | `FsGiTxnOrder_IncFeeCrystOption` | TField |  | Crystallization option for incentive fee Multifonds DB Column is CFEE_CRYST_INC. |
| 333 | `FS.GI.TXN.ORDER.HURDLE.BASE.CARRY.FORWARD` | `FsGiTxnOrder_HurdleBaseCarryForward` | TField |  | Field for migration of hurdle basis on to the system. Multifonds DB Column is LP_MIG_HBCF. |
| 334 | `FS.GI.TXN.ORDER.FUND.ID` | `FsGiTxnOrder_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 335 | `FS.GI.TXN.ORDER.CLASS.CURRENCY` | `FsGiTxnOrder_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 336 | `FS.GI.TXN.ORDER.IN.FUND.ID` | `FsGiTxnOrder_InFundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID2. |
| 337 | `FS.GI.TXN.ORDER.IN.CLASS.CURRENCY` | `FsGiTxnOrder_InClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY2. |
| 338 | `FS.GI.TXN.ORDER.ORDER.COMMISSION.VALUE.IN` | `FsGiTxnOrder_OrderCommissionValueIn` | TField |  | Commission value applied to the in leg transaction. Multifonds DB Column is PCT_DISP_IN. |
| 339 | `FS.GI.TXN.ORDER.ORDER.COMMISSION.METHOD.IN` | `FsGiTxnOrder_OrderCommissionMethodIn` | TField |  | Commission method applied to the in leg transaction. Multifonds DB Column is XPCT_DISP_IN. |
| 340 | `FS.GI.TXN.ORDER.PARTIAL.PAYMENT.TYPE` | `FsGiTxnOrder_PartialPaymentType` | TField |  | Partial payment type. Multifonds DB Column is PART_PAY_TYPE. |
| 341 | `FS.GI.TXN.ORDER.ORIGINAL.DEAL.REF` | `FsGiTxnOrder_OriginalDealRef` | TField |  | Original deal reference. Multifonds DB Column is ORIGINAL_DEAL_REF. |
| 342 | `FS.GI.TXN.ORDER.RESERVED10` | `FsGiTxnOrder_Reserved10` | TField |  |  |
| 343 | `FS.GI.TXN.ORDER.RESERVED9` | `FsGiTxnOrder_Reserved9` | TField |  |  |
| 344 | `FS.GI.TXN.ORDER.RESERVED8` | `FsGiTxnOrder_Reserved8` | TField |  |  |
| 345 | `FS.GI.TXN.ORDER.RESERVED7` | `FsGiTxnOrder_Reserved7` | TField |  |  |
| 346 | `FS.GI.TXN.ORDER.RESERVED6` | `FsGiTxnOrder_Reserved6` | TField |  |  |
| 347 | `FS.GI.TXN.ORDER.RESERVED5` | `FsGiTxnOrder_Reserved5` | TField |  |  |
| 348 | `FS.GI.TXN.ORDER.RESERVED4` | `FsGiTxnOrder_Reserved4` | TField |  |  |
| 349 | `FS.GI.TXN.ORDER.RESERVED3` | `FsGiTxnOrder_Reserved3` | TField |  |  |
| 350 | `FS.GI.TXN.ORDER.RESERVED2` | `FsGiTxnOrder_Reserved2` | TField |  |  |
| 351 | `FS.GI.TXN.ORDER.RESERVED1` | `FsGiTxnOrder_Reserved1` | TField |  |  |
| 352 | `FS.GI.TXN.ORDER.LOCAL.REF` | `FsGiTxnOrder_LocalRef` |  |  |  |
| 353 | `FS.GI.TXN.ORDER.OVERRIDE` | `FsGiTxnOrder_Override` |  |  |  |
| 354 | `FS.GI.TXN.ORDER.RECORD.STATUS` | `FsGiTxnOrder_RecordStatus` | String |  |  |
| 355 | `FS.GI.TXN.ORDER.CURR.NO` | `FsGiTxnOrder_CurrNo` | String |  |  |
| 356 | `FS.GI.TXN.ORDER.INPUTTER` | `FsGiTxnOrder_Inputter` |  |  |  |
| 357 | `FS.GI.TXN.ORDER.DATE.TIME` | `FsGiTxnOrder_DateTime` |  |  |  |
| 358 | `FS.GI.TXN.ORDER.AUTHORISER` | `FsGiTxnOrder_Authoriser` | String |  |  |
| 359 | `FS.GI.TXN.ORDER.CO.CODE` | `FsGiTxnOrder_CoCode` | String |  |  |
| 360 | `FS.GI.TXN.ORDER.DEPT.CODE` | `FsGiTxnOrder_DeptCode` | String |  |  |
| 361 | `FS.GI.TXN.ORDER.AUDITOR.CODE` | `FsGiTxnOrder_AuditorCode` | String |  |  |
| 362 | `FS.GI.TXN.ORDER.AUDIT.DATE.TIME` | `FsGiTxnOrder_AuditDateTime` | String |  |  |
