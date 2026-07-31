# FS.GI.TXN.TRADING.DESK.VALIDATION — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.TRADING.DESK.VALIDATION` in `FS_ExchangeRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.TRADING.DESK.VALIDATION.PARENT.REF.ID` | `FsGiTxnTradingDeskValidation_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.TRADING.DESK.VALIDATION.ORA.ROWID` | `FsGiTxnTradingDeskValidation_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.TRADING.DESK.VALIDATION.FX.TRADING.DESK.FLAG` | `FsGiTxnTradingDeskValidation_FxTradingDeskFlag` | TField |  | Flag to identify if the record is Client FX &apos;C&apos; or Fund FX &apos;F&apos;. Multifonds DB Column is FLG_TRADE_DESK. |
| 4 | `FS.GI.TXN.TRADING.DESK.VALIDATION.EXCHANGE.GROUP` | `FsGiTxnTradingDeskValidation_ExchangeGroup` | TField |  | Exchange group of the FX record. Multifonds DB Column is CGROUPE_COURS. |
| 5 | `FS.GI.TXN.TRADING.DESK.VALIDATION.EXCHANGE.GROUP.FX.METHOD` | `FsGiTxnTradingDeskValidation_ExchangeGroupFxMethod` | TField |  | Trading desk exchange group method code for Fund FX. Multifonds DB Column is CTD_MTHD. |
| 6 | `FS.GI.TXN.TRADING.DESK.VALIDATION.ACCOUNTING.DATE.MF` | `FsGiTxnTradingDeskValidation_AccountingDateMf` | TField |  | Date of report generation for FX. Multifonds DB Column is DCTA. |
| 7 | `FS.GI.TXN.TRADING.DESK.VALIDATION.STATUS` | `FsGiTxnTradingDeskValidation_Status` | TField |  | Status of the FX record. Multifonds DB Column is CSTATUS. |
| 8 | `FS.GI.TXN.TRADING.DESK.VALIDATION.DEAL.REFERENCE` | `FsGiTxnTradingDeskValidation_DealReference` | TField |  | Unique deal reference of the order. Multifonds DB Column is DEAL_REF. |
| 9 | `FS.GI.TXN.TRADING.DESK.VALIDATION.TRADE.DATE` | `FsGiTxnTradingDeskValidation_TradeDate` | TField |  | Trade date of the FX deal for both Client FX &amp; Fund FX. Multifonds DB Column is DOPER. |
| 10 | `FS.GI.TXN.TRADING.DESK.VALIDATION.VALUE.DATE` | `FsGiTxnTradingDeskValidation_ValueDate` | TField |  | Value date of FX record same as order value date. Multifonds DB Column is DVALEUR. |
| 11 | `FS.GI.TXN.TRADING.DESK.VALIDATION.SELL.QUOTATION.CCY.AMT` | `FsGiTxnTradingDeskValidation_SellQuotationCcyAmt` | TField |  | Quot ccy. amount to be sold for fund FX for credit transaction. This is either the initial full amount, or the change in amount since the previous FX details for this deal. Signs would be reversed for a Debit transaction. Multifonds DB Column is SELL_QUOT_CCY_AMT. |
| 12 | `FS.GI.TXN.TRADING.DESK.VALIDATION.SELL.QUOTATION.CCY` | `FsGiTxnTradingDeskValidation_SellQuotationCcy` | TField |  | Quot ccy. to be sold for fund FX record for credit transaction. Multifonds DB Column is SELL_QUOT_CCY. |
| 13 | `FS.GI.TXN.TRADING.DESK.VALIDATION.SELL.REFERENCE.CCY` | `FsGiTxnTradingDeskValidation_SellReferenceCcy` | TField |  | Reference (core) currency code for sold currency - populated for: Debit Transactions, Reversal of a credit transaction. Multifonds DB Column is SELL_REF_CCY. |
| 14 | `FS.GI.TXN.TRADING.DESK.VALIDATION.SELL.REFERENCE.CCY.AMT` | `FsGiTxnTradingDeskValidation_SellReferenceCcyAmt` | TField |  | Amount to sell In reference (core) currency - populated for: Debit Transactions, Reversal of a credit transaction. Multifonds DB Column is SELL_REF_CCY_AMT. |
| 15 | `FS.GI.TXN.TRADING.DESK.VALIDATION.BUY.QUOTATION.CCY.AMT` | `FsGiTxnTradingDeskValidation_BuyQuotationCcyAmt` | TField |  | Buy quotation currency Amount: this is either the initial full amount or the change in amount since the previous FX details for this deal. Multifonds DB Column is BUY_QUOT_CCY_AMT. |
| 16 | `FS.GI.TXN.TRADING.DESK.VALIDATION.BUY.QUOTATION.CCY` | `FsGiTxnTradingDeskValidation_BuyQuotationCcy` | TField |  | Quot. ccy to be bought for fund FX record for Debit transaction. Multifonds DB Column is BUY_QUOT_CCY. |
| 17 | `FS.GI.TXN.TRADING.DESK.VALIDATION.BUY.REFERENCE.CCY.AMT` | `FsGiTxnTradingDeskValidation_BuyReferenceCcyAmt` | TField |  | Amount to buy in reference (core) currency - populated for: Credit Transactions, Reversal of a debit transaction. Multifonds DB Column is BUY_REF_CCY_AMT. |
| 18 | `FS.GI.TXN.TRADING.DESK.VALIDATION.BUY.REFERENCE.CCY` | `FsGiTxnTradingDeskValidation_BuyReferenceCcy` | TField |  | Reference (core) currency code for bought currency - populated for: Credit Transactions, Reversal of a debit transaction. Multifonds DB Column is BUY_REF_CCY. |
| 19 | `FS.GI.TXN.TRADING.DESK.VALIDATION.APPLIED.FX.RATE` | `FsGiTxnTradingDeskValidation_AppliedFxRate` | TField |  | Exchange rate for FX records. Multifonds DB Column is TAUX_USER. |
| 20 | `FS.GI.TXN.TRADING.DESK.VALIDATION.APPLIED.FX.INDICATOR` | `FsGiTxnTradingDeskValidation_AppliedFxIndicator` | TField |  | Exchange rate to be multiplied or divided (direct or indirect) for FX. Multifonds DB Column is RATE_INDICATOR. |
| 21 | `FS.GI.TXN.TRADING.DESK.VALIDATION.PARTIAL.RESIDUAL.PAYMENT` | `FsGiTxnTradingDeskValidation_PartialResidualPayment` | TField |  | Indicates whether the FX is linked to Partial or Residual payment transaction. Multifonds DB Column is PAR_RED_INDI. |
| 22 | `FS.GI.TXN.TRADING.DESK.VALIDATION.AMOUNT` | `FsGiTxnTradingDeskValidation_Amount` | TField |  | FX buy or sell amount by which the FX deal is changing at this stage of the deal. Multifonds DB Column is AMOUNT. |
| 23 | `FS.GI.TXN.TRADING.DESK.VALIDATION.REFERENCE.NO` | `FsGiTxnTradingDeskValidation_ReferenceNo` | TField |  | FX reference no. of the deal. Multifonds DB Column is REFERENCE_NO. |
| 24 | `FS.GI.TXN.TRADING.DESK.VALIDATION.FX.PROVIDER` | `FsGiTxnTradingDeskValidation_FxProvider` | TField |  | FX provider for client trading desk and fund trading desk. Multifonds DB Column is FX_PROVIDER. |
| 25 | `FS.GI.TXN.TRADING.DESK.VALIDATION.INVESTOR.SOURCE.SYSTEM.ID` | `FsGiTxnTradingDeskValidation_InvestorSourceSystemId` | TField |  | Source system ID for client FX record. Multifonds DB Column is SRC_SYS_ID_CLNT. |
| 26 | `FS.GI.TXN.TRADING.DESK.VALIDATION.FUND.SOURCE.SYSTEM.ID` | `FsGiTxnTradingDeskValidation_FundSourceSystemId` | TField |  | Source system ID for fund FX record. Multifonds DB Column is SRC_SYS_ID_FND. |
| 27 | `FS.GI.TXN.TRADING.DESK.VALIDATION.INVESTOR.CUSTOMER.NUMBER` | `FsGiTxnTradingDeskValidation_InvestorCustomerNumber` | TField |  | Exchange order customer number for client FX record. Multifonds DB Column is CUST_NO. |
| 28 | `FS.GI.TXN.TRADING.DESK.VALIDATION.FUND.CUSTOMER.NUMBER` | `FsGiTxnTradingDeskValidation_FundCustomerNumber` | TField |  | Exchange order customer number for fund FX record. Multifonds DB Column is CUST_NO_FND. |
| 29 | `FS.GI.TXN.TRADING.DESK.VALIDATION.BRANCH.CODE` | `FsGiTxnTradingDeskValidation_BranchCode` | TField |  | Branch code of the transfer agency branch requesting the FX on behalf of the customer. This is a number that the FX system to which the request is made can recognize. Multifonds DB Column is BRANCH_CODE. |
| 30 | `FS.GI.TXN.TRADING.DESK.VALIDATION.SECURITY.ACCOUNT.NUMBER` | `FsGiTxnTradingDeskValidation_SecurityAccountNumber` | TField |  | Security account no as stored at fund level for FX purposes. Multifonds DB Column is SEC_ACC_NO. |
| 31 | `FS.GI.TXN.TRADING.DESK.VALIDATION.TREASURY.CONTRACT.REFERENCE` | `FsGiTxnTradingDeskValidation_TreasuryContractReference` | TField |  | FX Treasury contract reference received through inbound file. Multifonds DB Column is TRSRY_CONT_REF. |
| 32 | `FS.GI.TXN.TRADING.DESK.VALIDATION.HANDSHAKE.CODE` | `FsGiTxnTradingDeskValidation_HandshakeCode` | TField |  | FX CMPL or NACK received through inbound. Multifonds DB Column is HNDSHK_CD. |
| 33 | `FS.GI.TXN.TRADING.DESK.VALIDATION.REJECT.REASON` | `FsGiTxnTradingDeskValidation_RejectReason` | TField |  | FX rejection reason. Multifonds DB Column is INBND_RJCT_RSN. |
| 34 | `FS.GI.TXN.TRADING.DESK.VALIDATION.OUTBOUND.FLAG` | `FsGiTxnTradingDeskValidation_OutboundFlag` | TField |  | FX flagged by client when FX record details are extracted from this table. Multifonds DB Column is FLG_OUTBND_INT. |
| 35 | `FS.GI.TXN.TRADING.DESK.VALIDATION.OUTBOUND.FILE.DATE` | `FsGiTxnTradingDeskValidation_OutboundFileDate` | TField |  | FX date and time when FX record details are extracted. Multifonds DB Column is OUTBND_INT_DT. |
| 36 | `FS.GI.TXN.TRADING.DESK.VALIDATION.INBOUND.FILE.DATE` | `FsGiTxnTradingDeskValidation_InboundFileDate` | TField |  | FX date received from Inbound file for rejection records. Multifonds DB Column is INBND_INT_DT. |
| 37 | `FS.GI.TXN.TRADING.DESK.VALIDATION.ORDER.TYPE` | `FsGiTxnTradingDeskValidation_OrderType` | TField |  | Type of order if sub/red FX. Multifonds DB Column is TYPE_OPER. |
| 38 | `FS.GI.TXN.TRADING.DESK.VALIDATION.PAYMENT.CURRENCY` | `FsGiTxnTradingDeskValidation_PaymentCurrency` | TField |  | FX deal payment currency. Multifonds DB Column is CMON. |
| 39 | `FS.GI.TXN.TRADING.DESK.VALIDATION.FUND.MASTER.CCY` | `FsGiTxnTradingDeskValidation_FundMasterCcy` | TField |  | FX deal quotation or fund currency. Multifonds DB Column is CMONREF. |
| 40 | `FS.GI.TXN.TRADING.DESK.VALIDATION.GROUP.LEVEL` | `FsGiTxnTradingDeskValidation_GroupLevel` | TField |  | Technical processing data. Multifonds DB Column is GRP_LEVEL. |
| 41 | `FS.GI.TXN.TRADING.DESK.VALIDATION.ORDER.ID` | `FsGiTxnTradingDeskValidation_OrderId` | TField |  | Order number of the deal. Multifonds DB Column is NORDER. |
| 42 | `FS.GI.TXN.TRADING.DESK.VALIDATION.AGENT.ID` | `FsGiTxnTradingDeskValidation_AgentId` | TField |  | Agent for the deal. Multifonds DB Column is NOUTLET. |
| 43 | `FS.GI.TXN.TRADING.DESK.VALIDATION.IN.DEAL.REFERENCE` | `FsGiTxnTradingDeskValidation_InDealReference` | TField |  | Unique deal reference for the in-leg of the contract. Multifonds DB Column is DEAL_REF_IN. |
| 44 | `FS.GI.TXN.TRADING.DESK.VALIDATION.LEG.LINK` | `FsGiTxnTradingDeskValidation_LegLink` | TField |  | Identifier linking multiple parts of the same transaction. Multifonds DB Column is LEG_LINK. |
| 45 | `FS.GI.TXN.TRADING.DESK.VALIDATION.AMOUNT.QUANTITY.FLAG` | `FsGiTxnTradingDeskValidation_AmountQuantityFlag` | TField |  | Amount or quantity flag. Multifonds DB Column is AMT_OR_QTY. |
| 46 | `FS.GI.TXN.TRADING.DESK.VALIDATION.PRE.POST.PRICE.FX` | `FsGiTxnTradingDeskValidation_PrePostPriceFx` | TField |  | Flag to distinguish pre-pricing or post pricing fund FX record. Multifonds DB Column is FLG_PRE_POST_PRICE. |
| 47 | `FS.GI.TXN.TRADING.DESK.VALIDATION.FUND.FX.REMARKS` | `FsGiTxnTradingDeskValidation_FundFxRemarks` | TField |  | Remarks input for fund FX records. Multifonds DB Column is REMARKS. |
| 48 | `FS.GI.TXN.TRADING.DESK.VALIDATION.TA.FUND.ID` | `FsGiTxnTradingDeskValidation_TaFundId` | TField |  | TA fund of fund FX record. Multifonds DB Column is NPTF. |
| 49 | `FS.GI.TXN.TRADING.DESK.VALIDATION.SHARE.CLASS.CODE` | `FsGiTxnTradingDeskValidation_ShareClassCode` | TField |  | Share class of fund FX record. Multifonds DB Column is TPART. |
| 50 | `FS.GI.TXN.TRADING.DESK.VALIDATION.FX.RECORD.TYPE` | `FsGiTxnTradingDeskValidation_FxRecordType` | TField |  | FX record type of Fund FX record for both credit and debit transaction. Multifonds DB Column is FX_REC_TYPE. |
| 51 | `FS.GI.TXN.TRADING.DESK.VALIDATION.OPERATION.CODE` | `FsGiTxnTradingDeskValidation_OperationCode` | TField |  | Transaction operation code. Multifonds DB Column is COPERATION. |
| 52 | `FS.GI.TXN.TRADING.DESK.VALIDATION.DB.CR` | `FsGiTxnTradingDeskValidation_DbCr` | TField |  | FX Debit or Credit direction for this exchange transaction for the order Multifonds DB Column is CSENS. |
| 53 | `FS.GI.TXN.TRADING.DESK.VALIDATION.FUND.ID` | `FsGiTxnTradingDeskValidation_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 54 | `FS.GI.TXN.TRADING.DESK.VALIDATION.CLASS.CURRENCY` | `FsGiTxnTradingDeskValidation_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 55 | `FS.GI.TXN.TRADING.DESK.VALIDATION.EXCHANGE.GROUP.DESC` | `FsGiTxnTradingDeskValidation_ExchangeGroupDesc` | TField |  | Fund Group Name. Multifonds DB Column is CGROUPE_COURS_DESC. |
| 56 | `FS.GI.TXN.TRADING.DESK.VALIDATION.TRADING.DESK.STATUS` | `FsGiTxnTradingDeskValidation_TradingDeskStatus` | TField |  | Trading Desk Status. Multifonds DB Column is MWRK_ORDERS_CSTATUS. |
| 57 | `FS.GI.TXN.TRADING.DESK.VALIDATION.TRADING.DESK.FX.METHOD` | `FsGiTxnTradingDeskValidation_TradingDeskFxMethod` | TField |  | Trading Desk Method. Multifonds DB Column is MWRK_ORDERS_CTD_MTHD. |
| 58 | `FS.GI.TXN.TRADING.DESK.VALIDATION.STATUS.DESC` | `FsGiTxnTradingDeskValidation_StatusDesc` | TField |  | Status Description. Multifonds DB Column is CSTATUS_DESC. |
| 59 | `FS.GI.TXN.TRADING.DESK.VALIDATION.FOREX.ORDER.FLAG` | `FsGiTxnTradingDeskValidation_ForexOrderFlag` | TField |  | Forex by Order. Multifonds DB Column is FLG_FOREX_ORD. |
| 60 | `FS.GI.TXN.TRADING.DESK.VALIDATION.FX.ESTIMATED.AMOUNT` | `FsGiTxnTradingDeskValidation_FxEstimatedAmount` | TField |  | Fx Estimated Amount Multifonds DB Column is EST_AMOUNT. |
| 61 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RESERVED10` | `FsGiTxnTradingDeskValidation_Reserved10` | TField |  |  |
| 62 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RESERVED9` | `FsGiTxnTradingDeskValidation_Reserved9` | TField |  |  |
| 63 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RESERVED8` | `FsGiTxnTradingDeskValidation_Reserved8` | TField |  |  |
| 64 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RESERVED7` | `FsGiTxnTradingDeskValidation_Reserved7` | TField |  |  |
| 65 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RESERVED6` | `FsGiTxnTradingDeskValidation_Reserved6` | TField |  |  |
| 66 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RESERVED5` | `FsGiTxnTradingDeskValidation_Reserved5` | TField |  |  |
| 67 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RESERVED4` | `FsGiTxnTradingDeskValidation_Reserved4` | TField |  |  |
| 68 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RESERVED3` | `FsGiTxnTradingDeskValidation_Reserved3` | TField |  |  |
| 69 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RESERVED2` | `FsGiTxnTradingDeskValidation_Reserved2` | TField |  |  |
| 70 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RESERVED1` | `FsGiTxnTradingDeskValidation_Reserved1` | TField |  |  |
| 71 | `FS.GI.TXN.TRADING.DESK.VALIDATION.LOCAL.REF` | `FsGiTxnTradingDeskValidation_LocalRef` |  |  |  |
| 72 | `FS.GI.TXN.TRADING.DESK.VALIDATION.OVERRIDE` | `FsGiTxnTradingDeskValidation_Override` |  |  |  |
| 73 | `FS.GI.TXN.TRADING.DESK.VALIDATION.RECORD.STATUS` | `FsGiTxnTradingDeskValidation_RecordStatus` | String |  |  |
| 74 | `FS.GI.TXN.TRADING.DESK.VALIDATION.CURR.NO` | `FsGiTxnTradingDeskValidation_CurrNo` | String |  |  |
| 75 | `FS.GI.TXN.TRADING.DESK.VALIDATION.INPUTTER` | `FsGiTxnTradingDeskValidation_Inputter` |  |  |  |
| 76 | `FS.GI.TXN.TRADING.DESK.VALIDATION.DATE.TIME` | `FsGiTxnTradingDeskValidation_DateTime` |  |  |  |
| 77 | `FS.GI.TXN.TRADING.DESK.VALIDATION.AUTHORISER` | `FsGiTxnTradingDeskValidation_Authoriser` | String |  |  |
| 78 | `FS.GI.TXN.TRADING.DESK.VALIDATION.CO.CODE` | `FsGiTxnTradingDeskValidation_CoCode` | String |  |  |
| 79 | `FS.GI.TXN.TRADING.DESK.VALIDATION.DEPT.CODE` | `FsGiTxnTradingDeskValidation_DeptCode` | String |  |  |
| 80 | `FS.GI.TXN.TRADING.DESK.VALIDATION.AUDITOR.CODE` | `FsGiTxnTradingDeskValidation_AuditorCode` | String |  |  |
| 81 | `FS.GI.TXN.TRADING.DESK.VALIDATION.AUDIT.DATE.TIME` | `FsGiTxnTradingDeskValidation_AuditDateTime` | String |  |  |
