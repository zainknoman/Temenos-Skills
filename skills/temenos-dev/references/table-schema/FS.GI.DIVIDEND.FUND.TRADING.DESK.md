# FS.GI.DIVIDEND.FUND.TRADING.DESK — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIVIDEND.FUND.TRADING.DESK` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.DIV.FUND.TRADING.DESK.DIVIDEND.REINV.PAYMENT.FLAG` | `FsGiDividendFundTradingDesk_DividendReinvPaymentFlag` |  |  |  |
| 2 | `GI.DIV.FUND.TRADING.DESK.LEGAL.ENTITY.ID` | `FsGiDividendFundTradingDesk_LegalEntityId` |  |  |  |
| 3 | `GI.DIV.FUND.TRADING.DESK.EXECUTION.DATE` | `FsGiDividendFundTradingDesk_ExecutionDate` |  |  |  |
| 4 | `GI.DIV.FUND.TRADING.DESK.MF.FUND.ID` | `FsGiDividendFundTradingDesk_MfFundId` |  |  |  |
| 5 | `GI.DIV.FUND.TRADING.DESK.FX.STATUS` | `FsGiDividendFundTradingDesk_FxStatus` |  |  |  |
| 6 | `GI.DIV.FUND.TRADING.DESK.GROUP.ID` | `FsGiDividendFundTradingDesk_GroupId` |  |  |  |
| 7 | `GI.DIV.FUND.TRADING.DESK.SEQUENCE.NUMBER` | `FsGiDividendFundTradingDesk_SequenceNumber` |  |  |  |
| 8 | `GI.DIV.FUND.TRADING.DESK.FX.REFERENCE.NUMBER` | `FsGiDividendFundTradingDesk_FxReferenceNumber` |  |  |  |
| 9 | `GI.DIV.FUND.TRADING.DESK.RECORD.DATE` | `FsGiDividendFundTradingDesk_RecordDate` |  |  |  |
| 10 | `GI.DIV.FUND.TRADING.DESK.INCLUDE.FLAG` | `FsGiDividendFundTradingDesk_IncludeFlag` |  |  |  |
| 11 | `GI.DIV.FUND.TRADING.DESK.VALUE.DATE` | `FsGiDividendFundTradingDesk_ValueDate` |  |  |  |
| 12 | `GI.DIV.FUND.TRADING.DESK.REMARKS` | `FsGiDividendFundTradingDesk_Remarks` |  |  |  |
| 13 | `GI.DIV.FUND.TRADING.DESK.FUND.ID` | `FsGiDividendFundTradingDesk_FundId` |  |  |  |
| 14 | `GI.DIV.FUND.TRADING.DESK.SHARE.CLASS.CODE` | `FsGiDividendFundTradingDesk_ShareClassCode` |  |  |  |
| 15 | `GI.DIV.FUND.TRADING.DESK.SELL.REFERENCE.CURRENCY` | `FsGiDividendFundTradingDesk_SellReferenceCurrency` |  |  |  |
| 16 | `GI.DIV.FUND.TRADING.DESK.BUY.QUOTATION.CURRENCY` | `FsGiDividendFundTradingDesk_BuyQuotationCurrency` |  |  |  |
| 17 | `GI.DIV.FUND.TRADING.DESK.BUY.QUOTATION.CURRENCY.AMOUNT` | `FsGiDividendFundTradingDesk_BuyQuotationCurrencyAmount` |  |  |  |
| 18 | `GI.DIV.FUND.TRADING.DESK.FX.RECORD.TYPE` | `FsGiDividendFundTradingDesk_FxRecordType` |  |  |  |
| 19 | `GI.DIV.FUND.TRADING.DESK.DIV.FUND.SOURCE.SYSTEM.ID` | `FsGiDividendFundTradingDesk_DivFundSourceSystemId` |  |  |  |
| 20 | `GI.DIV.FUND.TRADING.DESK.FUND.INVESTOR.CUST.NUMBER` | `FsGiDividendFundTradingDesk_FundInvestorCustNumber` |  |  |  |
| 21 | `GI.DIV.FUND.TRADING.DESK.PROCESSED.BY` | `FsGiDividendFundTradingDesk_ProcessedBy` |  |  |  |
| 22 | `GI.DIV.FUND.TRADING.DESK.EDIT.FLAG` | `FsGiDividendFundTradingDesk_EditFlag` |  |  |  |
| 23 | `GI.DIV.FUND.TRADING.DESK.FX.PROVIDER` | `FsGiDividendFundTradingDesk_FxProvider` |  |  |  |
| 24 | `GI.DIV.FUND.TRADING.DESK.SECURITY.ACCOUNT.NUMBER` | `FsGiDividendFundTradingDesk_SecurityAccountNumber` |  |  |  |
| 25 | `GI.DIV.FUND.TRADING.DESK.SAVE.FLAG` | `FsGiDividendFundTradingDesk_SaveFlag` |  |  |  |
| 26 | `GI.DIV.FUND.TRADING.DESK.TEMPLATE.ID` | `FsGiDividendFundTradingDesk_TemplateId` |  |  |  |
| 27 | `GI.DIV.FUND.TRADING.DESK.RESERVED10` | `FsGiDividendFundTradingDesk_Reserved10` |  |  |  |
| 28 | `GI.DIV.FUND.TRADING.DESK.RESERVED9` | `FsGiDividendFundTradingDesk_Reserved9` |  |  |  |
| 29 | `GI.DIV.FUND.TRADING.DESK.RESERVED8` | `FsGiDividendFundTradingDesk_Reserved8` |  |  |  |
| 30 | `GI.DIV.FUND.TRADING.DESK.RESERVED7` | `FsGiDividendFundTradingDesk_Reserved7` |  |  |  |
| 31 | `GI.DIV.FUND.TRADING.DESK.RESERVED6` | `FsGiDividendFundTradingDesk_Reserved6` |  |  |  |
| 32 | `GI.DIV.FUND.TRADING.DESK.RESERVED5` | `FsGiDividendFundTradingDesk_Reserved5` |  |  |  |
| 33 | `GI.DIV.FUND.TRADING.DESK.RESERVED4` | `FsGiDividendFundTradingDesk_Reserved4` |  |  |  |
| 34 | `GI.DIV.FUND.TRADING.DESK.RESERVED3` | `FsGiDividendFundTradingDesk_Reserved3` |  |  |  |
| 35 | `GI.DIV.FUND.TRADING.DESK.RESERVED2` | `FsGiDividendFundTradingDesk_Reserved2` |  |  |  |
| 36 | `GI.DIV.FUND.TRADING.DESK.RESERVED1` | `FsGiDividendFundTradingDesk_Reserved1` |  |  |  |
| 37 | `GI.DIV.FUND.TRADING.DESK.LOCAL.REF` | `FsGiDividendFundTradingDesk_LocalRef` |  |  |  |
| 38 | `GI.DIV.FUND.TRADING.DESK.OVERRIDE` | `FsGiDividendFundTradingDesk_Override` |  |  |  |
| 39 | `GI.DIV.FUND.TRADING.DESK.RECORD.STATUS` | `FsGiDividendFundTradingDesk_RecordStatus` |  |  |  |
| 40 | `GI.DIV.FUND.TRADING.DESK.CURR.NO` | `FsGiDividendFundTradingDesk_CurrNo` |  |  |  |
| 41 | `GI.DIV.FUND.TRADING.DESK.INPUTTER` | `FsGiDividendFundTradingDesk_Inputter` |  |  |  |
| 42 | `GI.DIV.FUND.TRADING.DESK.DATE.TIME` | `FsGiDividendFundTradingDesk_DateTime` |  |  |  |
| 43 | `GI.DIV.FUND.TRADING.DESK.AUTHORISER` | `FsGiDividendFundTradingDesk_Authoriser` |  |  |  |
| 44 | `GI.DIV.FUND.TRADING.DESK.CO.CODE` | `FsGiDividendFundTradingDesk_CoCode` |  |  |  |
| 45 | `GI.DIV.FUND.TRADING.DESK.DEPT.CODE` | `FsGiDividendFundTradingDesk_DeptCode` |  |  |  |
| 46 | `GI.DIV.FUND.TRADING.DESK.AUDITOR.CODE` | `FsGiDividendFundTradingDesk_AuditorCode` |  |  |  |
| 47 | `GI.DIV.FUND.TRADING.DESK.AUDIT.DATE.TIME` | `FsGiDividendFundTradingDesk_AuditDateTime` |  |  |  |
