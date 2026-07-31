# FS.GA.FUTURE.MARKET.VALUE — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUTURE.MARKET.VALUE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUTURE.MARKET.VALUE.PARENT.REF.ID` | `FsGaFutureMarketValue_ParentRefId` |  |  |  |
| 2 | `FS.GA.FUTURE.MARKET.VALUE.ORA.ROWID` | `FsGaFutureMarketValue_OraRowid` |  |  |  |
| 3 | `FS.GA.FUTURE.MARKET.VALUE.FUTURE.ID.CODE` | `FsGaFutureMarketValue_FutureIdCode` |  |  |  |
| 4 | `FS.GA.FUTURE.MARKET.VALUE.QUOTATION.PLACE` | `FsGaFutureMarketValue_QuotationPlace` |  |  |  |
| 5 | `FS.GA.FUTURE.MARKET.VALUE.QUOTATION.CURRENCY` | `FsGaFutureMarketValue_QuotationCurrency` |  |  |  |
| 6 | `FS.GA.FUTURE.MARKET.VALUE.FUTURE.MARKET.VALUE` | `FsGaFutureMarketValue_FutureMarketValue` |  |  |  |
| 7 | `FS.GA.FUTURE.MARKET.VALUE.TRADE.OR.VALUE.OR.ACC.DATE` | `FsGaFutureMarketValue_TradeOrValueOrAccDate` |  |  |  |
| 8 | `FS.GA.FUTURE.MARKET.VALUE.FUTURE.BID.MARKET.VALUE` | `FsGaFutureMarketValue_FutureBidMarketValue` |  |  |  |
| 9 | `FS.GA.FUTURE.MARKET.VALUE.FUTURE.OFFER.MARKET.VALUE` | `FsGaFutureMarketValue_FutureOfferMarketValue` |  |  |  |
| 10 | `FS.GA.FUTURE.MARKET.VALUE.PRICE.SOURCE` | `FsGaFutureMarketValue_PriceSource` |  |  |  |
| 11 | `FS.GA.FUTURE.MARKET.VALUE.TYPE.OF.FUTURES.PRICE` | `FsGaFutureMarketValue_TypeOfFuturesPrice` |  |  |  |
| 12 | `FS.GA.FUTURE.MARKET.VALUE.TYPE.OF.FUTURES.PRICE.BID` | `FsGaFutureMarketValue_TypeOfFuturesPriceBid` |  |  |  |
| 13 | `FS.GA.FUTURE.MARKET.VALUE.TYPE.OF.FUTURES.PRICE.OFFER` | `FsGaFutureMarketValue_TypeOfFuturesPriceOffer` |  |  |  |
| 14 | `FS.GA.FUTURE.MARKET.VALUE.PRICING.DATE` | `FsGaFutureMarketValue_PricingDate` |  |  |  |
| 15 | `FS.GA.FUTURE.MARKET.VALUE.LEVERAGE` | `FsGaFutureMarketValue_Leverage` |  |  |  |
| 16 | `FS.GA.FUTURE.MARKET.VALUE.SENSIBILITY` | `FsGaFutureMarketValue_Sensibility` |  |  |  |
| 17 | `FS.GA.FUTURE.MARKET.VALUE.FUTURES.COMPENSATION.PRICE` | `FsGaFutureMarketValue_FuturesCompensationPrice` |  |  |  |
| 18 | `FS.GA.FUTURE.MARKET.VALUE.MAKER.USER.NAME` | `FsGaFutureMarketValue_MakerUserName` |  |  |  |
| 19 | `FS.GA.FUTURE.MARKET.VALUE.MAKER.PROCESSING.DATE` | `FsGaFutureMarketValue_MakerProcessingDate` |  |  |  |
| 20 | `FS.GA.FUTURE.MARKET.VALUE.RESERVED10` | `FsGaFutureMarketValue_Reserved10` |  |  |  |
| 21 | `FS.GA.FUTURE.MARKET.VALUE.RESERVED9` | `FsGaFutureMarketValue_Reserved9` |  |  |  |
| 22 | `FS.GA.FUTURE.MARKET.VALUE.RESERVED8` | `FsGaFutureMarketValue_Reserved8` |  |  |  |
| 23 | `FS.GA.FUTURE.MARKET.VALUE.RESERVED7` | `FsGaFutureMarketValue_Reserved7` |  |  |  |
| 24 | `FS.GA.FUTURE.MARKET.VALUE.RESERVED6` | `FsGaFutureMarketValue_Reserved6` |  |  |  |
| 25 | `FS.GA.FUTURE.MARKET.VALUE.RESERVED5` | `FsGaFutureMarketValue_Reserved5` |  |  |  |
| 26 | `FS.GA.FUTURE.MARKET.VALUE.RESERVED4` | `FsGaFutureMarketValue_Reserved4` |  |  |  |
| 27 | `FS.GA.FUTURE.MARKET.VALUE.RESERVED3` | `FsGaFutureMarketValue_Reserved3` |  |  |  |
| 28 | `FS.GA.FUTURE.MARKET.VALUE.RESERVED2` | `FsGaFutureMarketValue_Reserved2` |  |  |  |
| 29 | `FS.GA.FUTURE.MARKET.VALUE.RESERVED1` | `FsGaFutureMarketValue_Reserved1` |  |  |  |
| 30 | `FS.GA.FUTURE.MARKET.VALUE.LOCAL.REF` | `FsGaFutureMarketValue_LocalRef` |  |  |  |
| 31 | `FS.GA.FUTURE.MARKET.VALUE.OVERRIDE` | `FsGaFutureMarketValue_Override` |  |  |  |
| 32 | `FS.GA.FUTURE.MARKET.VALUE.RECORD.STATUS` | `FsGaFutureMarketValue_RecordStatus` |  |  |  |
| 33 | `FS.GA.FUTURE.MARKET.VALUE.CURR.NO` | `FsGaFutureMarketValue_CurrNo` |  |  |  |
| 34 | `FS.GA.FUTURE.MARKET.VALUE.INPUTTER` | `FsGaFutureMarketValue_Inputter` |  |  |  |
| 35 | `FS.GA.FUTURE.MARKET.VALUE.DATE.TIME` | `FsGaFutureMarketValue_DateTime` |  |  |  |
| 36 | `FS.GA.FUTURE.MARKET.VALUE.AUTHORISER` | `FsGaFutureMarketValue_Authoriser` |  |  |  |
| 37 | `FS.GA.FUTURE.MARKET.VALUE.CO.CODE` | `FsGaFutureMarketValue_CoCode` |  |  |  |
| 38 | `FS.GA.FUTURE.MARKET.VALUE.DEPT.CODE` | `FsGaFutureMarketValue_DeptCode` |  |  |  |
| 39 | `FS.GA.FUTURE.MARKET.VALUE.AUDITOR.CODE` | `FsGaFutureMarketValue_AuditorCode` |  |  |  |
| 40 | `FS.GA.FUTURE.MARKET.VALUE.AUDIT.DATE.TIME` | `FsGaFutureMarketValue_AuditDateTime` |  |  |  |
