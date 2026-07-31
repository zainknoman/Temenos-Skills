# FS.GA.IRS.CLOSING — Table Schema

> Source: `INSERTS/I_F.FS.GA.IRS.CLOSING` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.IRS.CLOSING.FUND.ID` | `FsGaIrsClosing_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.IRS.CLOSING.LOT.NUMBER` | `FsGaIrsClosing_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 3 | `FS.GA.IRS.CLOSING.TRANSACTION.NUMBER` | `FsGaIrsClosing_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 4 | `FS.GA.IRS.CLOSING.SETTLE.DATE` | `FsGaIrsClosing_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 5 | `FS.GA.IRS.CLOSING.TRADE.DATE` | `FsGaIrsClosing_TradeDate` | TField |  | Trade date of the trnsaction Multifonds DB Column is DOPER. |
| 6 | `FS.GA.IRS.CLOSING.ACCOUNTING.DATE` | `FsGaIrsClosing_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 7 | `FS.GA.IRS.CLOSING.OPERATION.CODE` | `FsGaIrsClosing_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 8 | `FS.GA.IRS.CLOSING.DEAL.STATUS.CODE` | `FsGaIrsClosing_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 9 | `FS.GA.IRS.CLOSING.SWAP.AMOUNT.BEFORE.CHANGE` | `FsGaIrsClosing_SwapAmountBeforeChange` | TField |  | Represents current amt of swap contract to which partial/full closing amount will be applied (used in case of IR5/IR8/IRU transactions for partial closing/full closing or nominal increase/decrease). Multifonds DB Column is MONTANT_SWAP_BF. |
| 10 | `FS.GA.IRS.CLOSING.SWAP.AMOUNT.POST.CHANGE` | `FsGaIrsClosing_SwapAmountPostChange` | TField |  | Represents new amt of swap contract post partial/full closing amount is processed (used in case of IR5/IR8/IRU transactions for partial closing/full closing or nominal increase/decrease). Multifonds DB Column is MONTANT_SWAP_AF. |
| 11 | `FS.GA.IRS.CLOSING.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaIrsClosing_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 12 | `FS.GA.IRS.CLOSING.SWAP.TERMINATION.FEE.PAYABLE` | `FsGaIrsClosing_SwapTerminationFeePayable` | TField |  | Termination fees payable applicable for the swap closing is accounted using fee code IL. When 'New IRS deal' is ticked these fee code will be balanced by operation code IV1. Multifonds DB Column is MFRAIS_TERM_PAY. |
| 13 | `FS.GA.IRS.CLOSING.SWAP.TERMINATION.FEE.RECEIVABL` | `FsGaIrsClosing_SwapTerminationFeeReceivabl` | TField |  | Termination fees receivable applicable for the swap closing is accounted using fee code IK. When 'New IRS deal' is ticked these fee code will be balanced by operation code IV1. Multifonds DB Column is MFRAIS_TERM_REC. |
| 14 | `FS.GA.IRS.CLOSING.SWAP.NET.PRESENT.VALUE` | `FsGaIrsClosing_SwapNetPresentValue` | TField |  | Net present value amount field gets populated with amount equal to pro-rata upfront amount during auto-maturity.This field gets populated with amt when user enters closing amount (Fee code-IH,II). Multifonds DB Column is MNT_NET_VALUE. |
| 15 | `FS.GA.IRS.CLOSING.SWAP.NPV.RECEIVABLE.OR.PAYABLE` | `FsGaIrsClosing_SwapNpvReceivableOrPayable` | TField |  | If swap contract is booked with upfront amt as receivable "R" then at maturity,NPV is populated with prorata upfront amt &amp; 'R' code; if initial upfront amt is booked with payable "P" then value is P. Multifonds DB Column is FLG_NET_VALUE. |
| 16 | `FS.GA.IRS.CLOSING.STATUS.PENDING` | `FsGaIrsClosing_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 17 | `FS.GA.IRS.CLOSING.EXTERNAL.REFERENCE` | `FsGaIrsClosing_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 18 | `FS.GA.IRS.CLOSING.SWAP.PRO.RATA.INTEREST.PAID` | `FsGaIrsClosing_SwapProRataInterestPaid` | TField |  | Int which is to be paid on counterparty closing nominal amt is accounted using IR6 op code in FDSWI03 post booking partial closing trx.This is populated with int paid amt when user enters closing amt. Multifonds DB Column is MINT_PRO_PAY. |
| 19 | `FS.GA.IRS.CLOSING.SWAP.PRO.RATA.INT.RECEIVED` | `FsGaIrsClosing_SwapProRataIntReceived` | TField |  | Int which is to be received on closing nominal amt is accounted using IR7 op code in FDSWI03 after booking partial closing transaction.This is populated with int rec. amt when user enters closing amt. Multifonds DB Column is MINT_PRO_REC. |
| 20 | `FS.GA.IRS.CLOSING.PRO.RATA.INT.ACCRUED.DEFERRAL` | `FsGaIrsClosing_ProRataIntAccruedDeferral` | TField |  | Accrued int (CDS buy) booked with IRS deal due to irregular pd. is populated in this field on partial closing.Prorata amount of accrued int in ratio of closing nominal is populated in this field. Multifonds DB Column is MINT_PRO_DEFF. |
| 21 | `FS.GA.IRS.CLOSING.PRO.RATA.UPFRONT.ON.SWAP.CLOSE` | `FsGaIrsClosing_ProRataUpfrontOnSwapClose` | TField |  | Populated on swap closing. If amt changed,upfront amt &lt; actual prop. upfront.If manually changed Upfront is diff than prop. upfront then amt is adjusted with bal. upfront &amp; eligible for next closing. Multifonds DB Column is UPFRONT_PRO. |
| 22 | `FS.GA.IRS.CLOSING.FUND.COUPON.DATE.LIST` | `FsGaIrsClosing_FundCouponDateList` | TField |  | Fund Coupon Date List Multifonds DB Column is DLST_COUPON_FUND. |
| 23 | `FS.GA.IRS.CLOSING.CTR.COUPON.DATE.LIST` | `FsGaIrsClosing_CtrCouponDateList` | TField |  | CTR Coupon Date List Multifonds DB Column is DLST_COUPON_CTR. |
| 24 | `FS.GA.IRS.CLOSING.VALUE.DATE.FOR.SWAP.CLOSING` | `FsGaIrsClosing_ValueDateForSwapClosing` | TField |  | This field is applicable to the settlement of termination fees receivable, payable and NPV on swap closing or swap nominal increase/decrease. Multifonds DB Column is MFRAIS_TERM_DVALEUR. |
| 25 | `FS.GA.IRS.CLOSING.SETTLEMENT.CCY.ON.SWAP.CLOSING` | `FsGaIrsClosing_SettlementCcyOnSwapClosing` | TField | Yes | This field is applicable to settlement currency of the termination fees receivable, payable and NPV.Once the value date field is updated, this field is mandatory. Multifonds DB Column is MFRAIS_TERM_CDEV. |
| 26 | `FS.GA.IRS.CLOSING.EXCH.RATE.ON.SWAP.CLOSING` | `FsGaIrsClosing_ExchRateOnSwapClosing` | TField | Yes | This field is applicable to exchange rate to be used for settlement of the termination fees receivable, payable and NPV.Once the value date field is updated, this field is mandatory. Multifonds DB Column is MFRAIS_TERM_TCHG. |
| 27 | `FS.GA.IRS.CLOSING.PRORATA.INT.ACCRUED.FUND.LEG` | `FsGaIrsClosing_ProrataIntAccruedFundLeg` | TField |  | Accrued int (CDS sell) booked with IRS deal due to irregular pd. is populated on partial closing.Prorata amount of accrued int in ratio of closing nominal is populated in this field. Multifonds DB Column is MINT_PRO_DEFF_FUND_LEG. |
| 28 | `FS.GA.IRS.CLOSING.INTEREST.AMOUNT.CLOSED.IN.FUND` | `FsGaIrsClosing_InterestAmountClosedInFund` | TField |  | Interest Amount Closed In Fund Multifonds DB Column is MONTANT_INT. |
| 29 | `FS.GA.IRS.CLOSING.IFRS.TAG` | `FsGaIrsClosing_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 30 | `FS.GA.IRS.CLOSING.CHECKED.BY` | `FsGaIrsClosing_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 31 | `FS.GA.IRS.CLOSING.CHECK.DATE` | `FsGaIrsClosing_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 32 | `FS.GA.IRS.CLOSING.SWAP.CASH.SETTLEMENT.FLAG` | `FsGaIrsClosing_SwapCashSettlementFlag` | TField |  | Op code IRA allows to account cash settl. on swap contract with 'IR9' + 'Swap ID' and 'Perf swap' unchecked (FDSWI02).'Amount to be closed' is not used as there is no change in nominal. Multifonds DB Column is FLG_CASH_SETTLEMENT. |
| 33 | `FS.GA.IRS.CLOSING.SECURITY.FOREX.VCI.SETTLEMENT` | `FsGaIrsClosing_SecurityForexVciSettlement` | TField |  | Security Forex VCI Settlement Multifonds DB Column is SEC_SETTL_FX_VCI. |
| 34 | `FS.GA.IRS.CLOSING.FUND.FOREX.VCI.SECURITY` | `FsGaIrsClosing_FundForexVciSecurity` | TField |  | Fund Forex VCI Security Multifonds DB Column is SEC_PTF_FX_VCI. |
| 35 | `FS.GA.IRS.CLOSING.FUND.FX.SETTLEMENT.VCI` | `FsGaIrsClosing_FundFxSettlementVci` | TField |  | Settl Ptf Fx Vci Multifonds DB Column is SETTL_PTF_FX_VCI. |
| 36 | `FS.GA.IRS.CLOSING.CURRENCY.INT.TO.COR.VCI` | `FsGaIrsClosing_CurrencyIntToCorVci` | TField |  | Currency INT To COR VCI Multifonds DB Column is CMON_INT_TO_CMON_COR_VCI. |
| 37 | `FS.GA.IRS.CLOSING.CURRENCY.INT.TO.NPV.CCY.VCI` | `FsGaIrsClosing_CurrencyIntToNpvCcyVci` | TField |  | Currency INT To NPV Ccy VCI Multifonds DB Column is CMON_INT_TO_CMON_NPV_VCI. |
| 38 | `FS.GA.IRS.CLOSING.CURRENCY.INT.TO.FUND.CCY.VCI` | `FsGaIrsClosing_CurrencyIntToFundCcyVci` | TField |  | Currency INT To Fund Ccy VCI Multifonds DB Column is CMON_INT_TO_FUND_CCY_VCI. |
| 39 | `FS.GA.IRS.CLOSING.CURRENCY.COR.TO.NPV.CCY.VCI` | `FsGaIrsClosing_CurrencyCorToNpvCcyVci` | TField |  | Currency COR To NPV Ccy VCI Multifonds DB Column is CMON_COR_TO_CMON_NPV_VCI. |
| 40 | `FS.GA.IRS.CLOSING.CURRENCY.COR.TO.FUND.CCY.VCI` | `FsGaIrsClosing_CurrencyCorToFundCcyVci` | TField |  | Currency COR TO Fund Ccy VCI Multifonds DB Column is CMON_COR_TO_FUND_CCY_VCI. |
| 41 | `FS.GA.IRS.CLOSING.CURRENCY.NPV.TO.FUND.CCY.VCI` | `FsGaIrsClosing_CurrencyNpvToFundCcyVci` | TField |  | Currency NPV To Fund Ccy VCI Multifonds DB Column is CMON_NPV_TO_FUND_CCY_VCI. |
| 42 | `FS.GA.IRS.CLOSING.IFRS.CATEGORY` | `FsGaIrsClosing_IfrsCategory` | TField |  | IFRS category assigned to a transaction Multifonds DB Column is SUB_TYPE. |
| 43 | `FS.GA.IRS.CLOSING.CURRENT.AMOUNT.FUND.LEG.CCY` | `FsGaIrsClosing_CurrentAmountFundLegCcy` | TField |  | Current Amount Fund Leg Ccy Multifonds DB Column is MONTANT_INT_SWAP_BF. |
| 44 | `FS.GA.IRS.CLOSING.NEW.AMOUNT.FUND.LEG.CCY` | `FsGaIrsClosing_NewAmountFundLegCcy` | TField |  | New Amount Fund Leg Ccy Multifonds DB Column is MONTANT_INT_SWAP_AF. |
| 45 | `FS.GA.IRS.CLOSING.ADJUSTMENT.FUND` | `FsGaIrsClosing_AdjustmentFund` | TField |  | Adjustment Fund Multifonds DB Column is NPTF_ORIGIN. |
| 46 | `FS.GA.IRS.CLOSING.CORRESPONDENT.ADJ.NUMBER` | `FsGaIrsClosing_CorrespondentAdjNumber` | TField |  | Correspondent adj number Multifonds DB Column is NCORRESP_ADJ. |
| 47 | `FS.GA.IRS.CLOSING.INTERPORT.TRADES` | `FsGaIrsClosing_InterportTrades` | TField |  | Interport trades Multifonds DB Column is FLG_INTERPORT_TRADES. |
| 48 | `FS.GA.IRS.CLOSING.RESERVED10` | `FsGaIrsClosing_Reserved10` | TField |  |  |
| 49 | `FS.GA.IRS.CLOSING.RESERVED9` | `FsGaIrsClosing_Reserved9` | TField |  |  |
| 50 | `FS.GA.IRS.CLOSING.RESERVED8` | `FsGaIrsClosing_Reserved8` | TField |  |  |
| 51 | `FS.GA.IRS.CLOSING.RESERVED7` | `FsGaIrsClosing_Reserved7` | TField |  |  |
| 52 | `FS.GA.IRS.CLOSING.RESERVED6` | `FsGaIrsClosing_Reserved6` | TField |  |  |
| 53 | `FS.GA.IRS.CLOSING.RESERVED5` | `FsGaIrsClosing_Reserved5` | TField |  |  |
| 54 | `FS.GA.IRS.CLOSING.RESERVED4` | `FsGaIrsClosing_Reserved4` | TField |  |  |
| 55 | `FS.GA.IRS.CLOSING.RESERVED3` | `FsGaIrsClosing_Reserved3` | TField |  |  |
| 56 | `FS.GA.IRS.CLOSING.RESERVED2` | `FsGaIrsClosing_Reserved2` | TField |  |  |
| 57 | `FS.GA.IRS.CLOSING.RESERVED1` | `FsGaIrsClosing_Reserved1` | TField |  |  |
| 58 | `FS.GA.IRS.CLOSING.LOCAL.REF` | `FsGaIrsClosing_LocalRef` |  |  |  |
| 59 | `FS.GA.IRS.CLOSING.OVERRIDE` | `FsGaIrsClosing_Override` |  |  |  |
| 60 | `FS.GA.IRS.CLOSING.RECORD.STATUS` | `FsGaIrsClosing_RecordStatus` | String |  |  |
| 61 | `FS.GA.IRS.CLOSING.CURR.NO` | `FsGaIrsClosing_CurrNo` | String |  |  |
| 62 | `FS.GA.IRS.CLOSING.INPUTTER` | `FsGaIrsClosing_Inputter` |  |  |  |
| 63 | `FS.GA.IRS.CLOSING.DATE.TIME` | `FsGaIrsClosing_DateTime` |  |  |  |
| 64 | `FS.GA.IRS.CLOSING.AUTHORISER` | `FsGaIrsClosing_Authoriser` | String |  |  |
| 65 | `FS.GA.IRS.CLOSING.CO.CODE` | `FsGaIrsClosing_CoCode` | String |  |  |
| 66 | `FS.GA.IRS.CLOSING.DEPT.CODE` | `FsGaIrsClosing_DeptCode` | String |  |  |
| 67 | `FS.GA.IRS.CLOSING.AUDITOR.CODE` | `FsGaIrsClosing_AuditorCode` | String |  |  |
| 68 | `FS.GA.IRS.CLOSING.AUDIT.DATE.TIME` | `FsGaIrsClosing_AuditDateTime` | String |  |  |
