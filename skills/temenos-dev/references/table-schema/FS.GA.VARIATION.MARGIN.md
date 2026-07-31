# FS.GA.VARIATION.MARGIN — Table Schema

> Source: `INSERTS/I_F.FS.GA.VARIATION.MARGIN` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.VARIATION.MARGIN.NAV.GROUP.CODE` | `FsGaVariationMargin_NavGroupCode` |  |  |  |
| 2 | `FS.GA.VARIATION.MARGIN.FUND.ID` | `FsGaVariationMargin_FundId` |  |  |  |
| 3 | `FS.GA.VARIATION.MARGIN.BROKER.FOR.VARIATION.MARGIN` | `FsGaVariationMargin_BrokerForVariationMargin` |  |  |  |
| 4 | `FS.GA.VARIATION.MARGIN.EXTERNAL.SECURITY.ID` | `FsGaVariationMargin_ExternalSecurityId` |  |  |  |
| 5 | `FS.GA.VARIATION.MARGIN.SEC.ID.DESCRIPTION` | `FsGaVariationMargin_SecIdDescription` |  |  |  |
| 6 | `FS.GA.VARIATION.MARGIN.SECURITY.CURRENCY` | `FsGaVariationMargin_SecurityCurrency` |  |  |  |
| 7 | `FS.GA.VARIATION.MARGIN.GTI.CODE` | `FsGaVariationMargin_GtiCode` |  |  |  |
| 8 | `FS.GA.VARIATION.MARGIN.OPERATION.CODE` | `FsGaVariationMargin_OperationCode` |  |  |  |
| 9 | `FS.GA.VARIATION.MARGIN.SETTLE.DATE` | `FsGaVariationMargin_SettleDate` |  |  |  |
| 10 | `FS.GA.VARIATION.MARGIN.SETTLED.DATE.VALEUR` | `FsGaVariationMargin_SettledDateValeur` |  |  |  |
| 11 | `FS.GA.VARIATION.MARGIN.SERVICE.CODE` | `FsGaVariationMargin_ServiceCode` |  |  |  |
| 12 | `FS.GA.VARIATION.MARGIN.MANAGER.CODE` | `FsGaVariationMargin_ManagerCode` |  |  |  |
| 13 | `FS.GA.VARIATION.MARGIN.LOT.NUMBER` | `FsGaVariationMargin_LotNumber` |  |  |  |
| 14 | `FS.GA.VARIATION.MARGIN.FUND.CURRENCY` | `FsGaVariationMargin_FundCurrency` |  |  |  |
| 15 | `FS.GA.VARIATION.MARGIN.SETTLE.CURRENCY` | `FsGaVariationMargin_SettleCurrency` |  |  |  |
| 16 | `FS.GA.VARIATION.MARGIN.QUANTITY` | `FsGaVariationMargin_Quantity` |  |  |  |
| 17 | `FS.GA.VARIATION.MARGIN.LAST.SETTLEMENT.PRICE` | `FsGaVariationMargin_LastSettlementPrice` |  |  |  |
| 18 | `FS.GA.VARIATION.MARGIN.NEW.SETTLEMENT.PRICE` | `FsGaVariationMargin_NewSettlementPrice` |  |  |  |
| 19 | `FS.GA.VARIATION.MARGIN.RATE.OF.EXCHANGE` | `FsGaVariationMargin_RateOfExchange` |  |  |  |
| 20 | `FS.GA.VARIATION.MARGIN.SETTLE.EXCHANGE.RATE` | `FsGaVariationMargin_SettleExchangeRate` |  |  |  |
| 21 | `FS.GA.VARIATION.MARGIN.NET.MARGIN.IN.FUND.CCY` | `FsGaVariationMargin_NetMarginInFundCcy` |  |  |  |
| 22 | `FS.GA.VARIATION.MARGIN.NET.MARGIN.IN.SETTLEMENT.CCY` | `FsGaVariationMargin_NetMarginInSettlementCcy` |  |  |  |
| 23 | `FS.GA.VARIATION.MARGIN.TOTAL.VARIATION.MARGIN` | `FsGaVariationMargin_TotalVariationMargin` |  |  |  |
| 24 | `FS.GA.VARIATION.MARGIN.CONTRACT.SIZE` | `FsGaVariationMargin_ContractSize` |  |  |  |
| 25 | `FS.GA.VARIATION.MARGIN.PROVIDER.ID` | `FsGaVariationMargin_ProviderId` |  |  |  |
| 26 | `FS.GA.VARIATION.MARGIN.PROVIDER.CODE` | `FsGaVariationMargin_ProviderCode` |  |  |  |
| 27 | `FS.GA.VARIATION.MARGIN.TRANSACTION.NUMBER` | `FsGaVariationMargin_TransactionNumber` |  |  |  |
| 28 | `FS.GA.VARIATION.MARGIN.TRANSACTION.ENTRY.NUMBER` | `FsGaVariationMargin_TransactionEntryNumber` |  |  |  |
| 29 | `FS.GA.VARIATION.MARGIN.PTF.TRANSACTION.ENTRY.NUMBER` | `FsGaVariationMargin_PtfTransactionEntryNumber` |  |  |  |
| 30 | `FS.GA.VARIATION.MARGIN.FUTURE.OPTION.TRANSACTION.TYPE` | `FsGaVariationMargin_FutureOptionTransactionType` |  |  |  |
| 31 | `FS.GA.VARIATION.MARGIN.STATUS.CODE` | `FsGaVariationMargin_StatusCode` |  |  |  |
| 32 | `FS.GA.VARIATION.MARGIN.FLAG.SHOW` | `FsGaVariationMargin_FlagShow` |  |  |  |
| 33 | `FS.GA.VARIATION.MARGIN.VARIATION.MARGIN.SQL` | `FsGaVariationMargin_VariationMarginSql` |  |  |  |
| 34 | `FS.GA.VARIATION.MARGIN.PRICE.OUT.DATE` | `FsGaVariationMargin_PriceOutDate` |  |  |  |
| 35 | `FS.GA.VARIATION.MARGIN.CASH.NUMBER` | `FsGaVariationMargin_CashNumber` |  |  |  |
| 36 | `FS.GA.VARIATION.MARGIN.SUFFIX.NUMBER.ON.CASH` | `FsGaVariationMargin_SuffixNumberOnCash` |  |  |  |
| 37 | `FS.GA.VARIATION.MARGIN.VARMARGIN.ACCOUNT.FUTURES` | `FsGaVariationMargin_VarmarginAccountFutures` |  |  |  |
| 38 | `FS.GA.VARIATION.MARGIN.VARIATION.MARGIN.SUFFIX.NUMBER` | `FsGaVariationMargin_VariationMarginSuffixNumber` |  |  |  |
| 39 | `FS.GA.VARIATION.MARGIN.TRANSACTION.TYPE.TRANS` | `FsGaVariationMargin_TransactionTypeTrans` |  |  |  |
| 40 | `FS.GA.VARIATION.MARGIN.DEBIT.CREDIT.INDICATOR` | `FsGaVariationMargin_DebitCreditIndicator` |  |  |  |
| 41 | `FS.GA.VARIATION.MARGIN.MARGIN.AMOUNT` | `FsGaVariationMargin_MarginAmount` |  |  |  |
| 42 | `FS.GA.VARIATION.MARGIN.ADJUSTMENT.MARGIN.CLS` | `FsGaVariationMargin_AdjustmentMarginCls` |  |  |  |
| 43 | `FS.GA.VARIATION.MARGIN.ADJUSTMENT.MARGIN.REV` | `FsGaVariationMargin_AdjustmentMarginRev` |  |  |  |
| 44 | `FS.GA.VARIATION.MARGIN.ADJUSTED.MARGIN` | `FsGaVariationMargin_AdjustedMargin` |  |  |  |
| 45 | `FS.GA.VARIATION.MARGIN.OPTION.AND.FUTURES.SEC.TYPE` | `FsGaVariationMargin_OptionAndFuturesSecType` |  |  |  |
| 46 | `FS.GA.VARIATION.MARGIN.FUND.ACCOUNTING.DATE` | `FsGaVariationMargin_FundAccountingDate` |  |  |  |
| 47 | `FS.GA.VARIATION.MARGIN.TRANSACTION.PRICE` | `FsGaVariationMargin_TransactionPrice` |  |  |  |
| 48 | `FS.GA.VARIATION.MARGIN.MESSAGE.ERROR` | `FsGaVariationMargin_MessageError` |  |  |  |
| 49 | `FS.GA.VARIATION.MARGIN.NEW.SETTLEMENT.DATE` | `FsGaVariationMargin_NewSettlementDate` |  |  |  |
| 50 | `FS.GA.VARIATION.MARGIN.VALUATION.METHOD` | `FsGaVariationMargin_ValuationMethod` |  |  |  |
| 51 | `FS.GA.VARIATION.MARGIN.REASON.CODE` | `FsGaVariationMargin_ReasonCode` |  |  |  |
| 52 | `FS.GA.VARIATION.MARGIN.FLAG.MANUAL` | `FsGaVariationMargin_FlagManual` |  |  |  |
| 53 | `FS.GA.VARIATION.MARGIN.RESERVED10` | `FsGaVariationMargin_Reserved10` |  |  |  |
| 54 | `FS.GA.VARIATION.MARGIN.RESERVED9` | `FsGaVariationMargin_Reserved9` |  |  |  |
| 55 | `FS.GA.VARIATION.MARGIN.RESERVED8` | `FsGaVariationMargin_Reserved8` |  |  |  |
| 56 | `FS.GA.VARIATION.MARGIN.RESERVED7` | `FsGaVariationMargin_Reserved7` |  |  |  |
| 57 | `FS.GA.VARIATION.MARGIN.RESERVED6` | `FsGaVariationMargin_Reserved6` |  |  |  |
| 58 | `FS.GA.VARIATION.MARGIN.RESERVED5` | `FsGaVariationMargin_Reserved5` |  |  |  |
| 59 | `FS.GA.VARIATION.MARGIN.RESERVED4` | `FsGaVariationMargin_Reserved4` |  |  |  |
| 60 | `FS.GA.VARIATION.MARGIN.RESERVED3` | `FsGaVariationMargin_Reserved3` |  |  |  |
| 61 | `FS.GA.VARIATION.MARGIN.RESERVED2` | `FsGaVariationMargin_Reserved2` |  |  |  |
| 62 | `FS.GA.VARIATION.MARGIN.RESERVED1` | `FsGaVariationMargin_Reserved1` |  |  |  |
| 63 | `FS.GA.VARIATION.MARGIN.RECORD.STATUS` | `FsGaVariationMargin_RecordStatus` |  |  |  |
| 64 | `FS.GA.VARIATION.MARGIN.CURR.NO` | `FsGaVariationMargin_CurrNo` |  |  |  |
| 65 | `FS.GA.VARIATION.MARGIN.INPUTTER` | `FsGaVariationMargin_Inputter` |  |  |  |
| 66 | `FS.GA.VARIATION.MARGIN.DATE.TIME` | `FsGaVariationMargin_DateTime` |  |  |  |
| 67 | `FS.GA.VARIATION.MARGIN.AUTHORISER` | `FsGaVariationMargin_Authoriser` |  |  |  |
| 68 | `FS.GA.VARIATION.MARGIN.CO.CODE` | `FsGaVariationMargin_CoCode` |  |  |  |
| 69 | `FS.GA.VARIATION.MARGIN.DEPT.CODE` | `FsGaVariationMargin_DeptCode` |  |  |  |
| 70 | `FS.GA.VARIATION.MARGIN.AUDITOR.CODE` | `FsGaVariationMargin_AuditorCode` |  |  |  |
| 71 | `FS.GA.VARIATION.MARGIN.AUDIT.DATE.TIME` | `FsGaVariationMargin_AuditDateTime` |  |  |  |
