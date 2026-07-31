# FS.GI.DIVIDEND.TRADING.DESK — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIVIDEND.TRADING.DESK` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.DIV.TRADING.DESK.FUND.ID` | `FsGiDividendTradingDesk_FundId` |  |  |  |
| 2 | `GI.DIV.TRADING.DESK.SHARE.CLASS.CODE` | `FsGiDividendTradingDesk_ShareClassCode` |  |  |  |
| 3 | `GI.DIV.TRADING.DESK.SEQUENCE.NUMBER` | `FsGiDividendTradingDesk_SequenceNumber` |  |  |  |
| 4 | `GI.DIV.TRADING.DESK.PROCESSING.DATE` | `FsGiDividendTradingDesk_ProcessingDate` |  |  |  |
| 5 | `GI.DIV.TRADING.DESK.EXECUTION.DATE` | `FsGiDividendTradingDesk_ExecutionDate` |  |  |  |
| 6 | `GI.DIV.TRADING.DESK.VALUE.DATE` | `FsGiDividendTradingDesk_ValueDate` |  |  |  |
| 7 | `GI.DIV.TRADING.DESK.SETTLEMENT.AMOUNT` | `FsGiDividendTradingDesk_SettlementAmount` |  |  |  |
| 8 | `GI.DIV.TRADING.DESK.FUND.MASTER.CCY` | `FsGiDividendTradingDesk_FundMasterCcy` |  |  |  |
| 9 | `GI.DIV.TRADING.DESK.PAYMENT.CURRENCY` | `FsGiDividendTradingDesk_PaymentCurrency` |  |  |  |
| 10 | `GI.DIV.TRADING.DESK.FX.RATE` | `FsGiDividendTradingDesk_FxRate` |  |  |  |
| 11 | `GI.DIV.TRADING.DESK.DIVIDE.FLAG` | `FsGiDividendTradingDesk_DivideFlag` |  |  |  |
| 12 | `GI.DIV.TRADING.DESK.FX.REFERENCE.NUMBER` | `FsGiDividendTradingDesk_FxReferenceNumber` |  |  |  |
| 13 | `GI.DIV.TRADING.DESK.FX.PROVIDER` | `FsGiDividendTradingDesk_FxProvider` |  |  |  |
| 14 | `GI.DIV.TRADING.DESK.DIV.INVESTOR.SYSTEM.SOURCE.ID` | `FsGiDividendTradingDesk_DivInvestorSystemSourceId` |  |  |  |
| 15 | `GI.DIV.TRADING.DESK.DIV.INVESTOR.CUST.NUMBER` | `FsGiDividendTradingDesk_DivInvestorCustNumber` |  |  |  |
| 16 | `GI.DIV.TRADING.DESK.BRANCH.CODE` | `FsGiDividendTradingDesk_BranchCode` |  |  |  |
| 17 | `GI.DIV.TRADING.DESK.TREASURY.CONTACT.REF` | `FsGiDividendTradingDesk_TreasuryContactRef` |  |  |  |
| 18 | `GI.DIV.TRADING.DESK.OUTBOUND.FLAG` | `FsGiDividendTradingDesk_OutboundFlag` |  |  |  |
| 19 | `GI.DIV.TRADING.DESK.OUTBOUND.TIME` | `FsGiDividendTradingDesk_OutboundTime` |  |  |  |
| 20 | `GI.DIV.TRADING.DESK.HAND.SHAKE.CODE` | `FsGiDividendTradingDesk_HandShakeCode` |  |  |  |
| 21 | `GI.DIV.TRADING.DESK.INBOUND.INTERFACE.DATE` | `FsGiDividendTradingDesk_InboundInterfaceDate` |  |  |  |
| 22 | `GI.DIV.TRADING.DESK.RECEIVED.TIME` | `FsGiDividendTradingDesk_ReceivedTime` |  |  |  |
| 23 | `GI.DIV.TRADING.DESK.REJECT.REASON` | `FsGiDividendTradingDesk_RejectReason` |  |  |  |
| 24 | `GI.DIV.TRADING.DESK.TRADE.DATE` | `FsGiDividendTradingDesk_TradeDate` |  |  |  |
| 25 | `GI.DIV.TRADING.DESK.DIVIDEND.REINV.PAYMENT.FLAG` | `FsGiDividendTradingDesk_DividendReinvPaymentFlag` |  |  |  |
| 26 | `GI.DIV.TRADING.DESK.LEGAL.ENTITY.ID` | `FsGiDividendTradingDesk_LegalEntityId` |  |  |  |
| 27 | `GI.DIV.TRADING.DESK.MF.FUND.ID` | `FsGiDividendTradingDesk_MfFundId` |  |  |  |
| 28 | `GI.DIV.TRADING.DESK.RECORD.DATE` | `FsGiDividendTradingDesk_RecordDate` |  |  |  |
| 29 | `GI.DIV.TRADING.DESK.REMARKS` | `FsGiDividendTradingDesk_Remarks` |  |  |  |
| 30 | `GI.DIV.TRADING.DESK.FX.STATUS` | `FsGiDividendTradingDesk_FxStatus` |  |  |  |
| 31 | `GI.DIV.TRADING.DESK.FX.RECORD.TYPE` | `FsGiDividendTradingDesk_FxRecordType` |  |  |  |
| 32 | `GI.DIV.TRADING.DESK.DIV.FUND.SOURCE.SYSTEM.ID` | `FsGiDividendTradingDesk_DivFundSourceSystemId` |  |  |  |
| 33 | `GI.DIV.TRADING.DESK.SECURITY.ACCOUNT.NUMBER` | `FsGiDividendTradingDesk_SecurityAccountNumber` |  |  |  |
| 34 | `GI.DIV.TRADING.DESK.HAND.SHAKE.CODE.INTERFACE` | `FsGiDividendTradingDesk_HandShakeCodeInterface` |  |  |  |
| 35 | `GI.DIV.TRADING.DESK.INBOUND.REJECT.REASON` | `FsGiDividendTradingDesk_InboundRejectReason` |  |  |  |
| 36 | `GI.DIV.TRADING.DESK.FUND.INVESTOR.CUST.NUMBER` | `FsGiDividendTradingDesk_FundInvestorCustNumber` |  |  |  |
| 37 | `GI.DIV.TRADING.DESK.GROUP.ID` | `FsGiDividendTradingDesk_GroupId` |  |  |  |
| 38 | `GI.DIV.TRADING.DESK.SELL.REFERENCE.CURRENCY` | `FsGiDividendTradingDesk_SellReferenceCurrency` |  |  |  |
| 39 | `GI.DIV.TRADING.DESK.BUY.QUOTATION.CURRENCY` | `FsGiDividendTradingDesk_BuyQuotationCurrency` |  |  |  |
| 40 | `GI.DIV.TRADING.DESK.BUY.QUOTATION.CURRENCY.AMOUNT` | `FsGiDividendTradingDesk_BuyQuotationCurrencyAmount` |  |  |  |
| 41 | `GI.DIV.TRADING.DESK.AMOUNT` | `FsGiDividendTradingDesk_Amount` |  |  |  |
| 42 | `GI.DIV.TRADING.DESK.REGISTER.ID` | `FsGiDividendTradingDesk_RegisterId` |  |  |  |
| 43 | `GI.DIV.TRADING.DESK.RECEIVED.DATE` | `FsGiDividendTradingDesk_ReceivedDate` |  |  |  |
| 44 | `GI.DIV.TRADING.DESK.TEMPLATE.ID` | `FsGiDividendTradingDesk_TemplateId` |  |  |  |
| 45 | `GI.DIV.TRADING.DESK.RESERVED10` | `FsGiDividendTradingDesk_Reserved10` |  |  |  |
| 46 | `GI.DIV.TRADING.DESK.RESERVED9` | `FsGiDividendTradingDesk_Reserved9` |  |  |  |
| 47 | `GI.DIV.TRADING.DESK.RESERVED8` | `FsGiDividendTradingDesk_Reserved8` |  |  |  |
| 48 | `GI.DIV.TRADING.DESK.RESERVED7` | `FsGiDividendTradingDesk_Reserved7` |  |  |  |
| 49 | `GI.DIV.TRADING.DESK.RESERVED6` | `FsGiDividendTradingDesk_Reserved6` |  |  |  |
| 50 | `GI.DIV.TRADING.DESK.RESERVED5` | `FsGiDividendTradingDesk_Reserved5` |  |  |  |
| 51 | `GI.DIV.TRADING.DESK.RESERVED4` | `FsGiDividendTradingDesk_Reserved4` |  |  |  |
| 52 | `GI.DIV.TRADING.DESK.RESERVED3` | `FsGiDividendTradingDesk_Reserved3` |  |  |  |
| 53 | `GI.DIV.TRADING.DESK.RESERVED2` | `FsGiDividendTradingDesk_Reserved2` |  |  |  |
| 54 | `GI.DIV.TRADING.DESK.RESERVED1` | `FsGiDividendTradingDesk_Reserved1` |  |  |  |
| 55 | `GI.DIV.TRADING.DESK.LOCAL.REF` | `FsGiDividendTradingDesk_LocalRef` |  |  |  |
| 56 | `GI.DIV.TRADING.DESK.OVERRIDE` | `FsGiDividendTradingDesk_Override` |  |  |  |
| 57 | `GI.DIV.TRADING.DESK.RECORD.STATUS` | `FsGiDividendTradingDesk_RecordStatus` |  |  |  |
| 58 | `GI.DIV.TRADING.DESK.CURR.NO` | `FsGiDividendTradingDesk_CurrNo` |  |  |  |
| 59 | `GI.DIV.TRADING.DESK.INPUTTER` | `FsGiDividendTradingDesk_Inputter` |  |  |  |
| 60 | `GI.DIV.TRADING.DESK.DATE.TIME` | `FsGiDividendTradingDesk_DateTime` |  |  |  |
| 61 | `GI.DIV.TRADING.DESK.AUTHORISER` | `FsGiDividendTradingDesk_Authoriser` |  |  |  |
| 62 | `GI.DIV.TRADING.DESK.CO.CODE` | `FsGiDividendTradingDesk_CoCode` |  |  |  |
| 63 | `GI.DIV.TRADING.DESK.DEPT.CODE` | `FsGiDividendTradingDesk_DeptCode` |  |  |  |
| 64 | `GI.DIV.TRADING.DESK.AUDITOR.CODE` | `FsGiDividendTradingDesk_AuditorCode` |  |  |  |
| 65 | `GI.DIV.TRADING.DESK.AUDIT.DATE.TIME` | `FsGiDividendTradingDesk_AuditDateTime` |  |  |  |
