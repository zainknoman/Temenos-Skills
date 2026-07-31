# FS.GA.OPTION.MARKET.VALUE — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPTION.MARKET.VALUE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPTION.MARKET.VALUE.PARENT.REF.ID` | `FsGaOptionMarketValue_ParentRefId` |  |  |  |
| 2 | `FS.GA.OPTION.MARKET.VALUE.ORA.ROWID` | `FsGaOptionMarketValue_OraRowid` |  |  |  |
| 3 | `FS.GA.OPTION.MARKET.VALUE.OPTION.ID` | `FsGaOptionMarketValue_OptionId` |  |  |  |
| 4 | `FS.GA.OPTION.MARKET.VALUE.QUOTATION.PLACE` | `FsGaOptionMarketValue_QuotationPlace` |  |  |  |
| 5 | `FS.GA.OPTION.MARKET.VALUE.QUOTATION.CURRENCY` | `FsGaOptionMarketValue_QuotationCurrency` |  |  |  |
| 6 | `FS.GA.OPTION.MARKET.VALUE.OPTION.MARKET.VALUE` | `FsGaOptionMarketValue_OptionMarketValue` |  |  |  |
| 7 | `FS.GA.OPTION.MARKET.VALUE.TRADE.OR.VALUE.OR.ACC.DATE` | `FsGaOptionMarketValue_TradeOrValueOrAccDate` |  |  |  |
| 8 | `FS.GA.OPTION.MARKET.VALUE.OPTION.BID.MARKET.VALUE` | `FsGaOptionMarketValue_OptionBidMarketValue` |  |  |  |
| 9 | `FS.GA.OPTION.MARKET.VALUE.OPTION.OFFER.MARKET.VALUE` | `FsGaOptionMarketValue_OptionOfferMarketValue` |  |  |  |
| 10 | `FS.GA.OPTION.MARKET.VALUE.PRICE.SOURCE` | `FsGaOptionMarketValue_PriceSource` |  |  |  |
| 11 | `FS.GA.OPTION.MARKET.VALUE.TYPE.OF.OPTIONS.PRICE` | `FsGaOptionMarketValue_TypeOfOptionsPrice` |  |  |  |
| 12 | `FS.GA.OPTION.MARKET.VALUE.TYPE.OF.OPTIONS.PRICE.BID` | `FsGaOptionMarketValue_TypeOfOptionsPriceBid` |  |  |  |
| 13 | `FS.GA.OPTION.MARKET.VALUE.TYPE.OF.OPTIONS.PRICE.OFFER` | `FsGaOptionMarketValue_TypeOfOptionsPriceOffer` |  |  |  |
| 14 | `FS.GA.OPTION.MARKET.VALUE.PRICING.DATE` | `FsGaOptionMarketValue_PricingDate` |  |  |  |
| 15 | `FS.GA.OPTION.MARKET.VALUE.LEVERAGE` | `FsGaOptionMarketValue_Leverage` |  |  |  |
| 16 | `FS.GA.OPTION.MARKET.VALUE.DELTA` | `FsGaOptionMarketValue_Delta` |  |  |  |
| 17 | `FS.GA.OPTION.MARKET.VALUE.SENSIBILITY` | `FsGaOptionMarketValue_Sensibility` |  |  |  |
| 18 | `FS.GA.OPTION.MARKET.VALUE.DELTA.2` | `FsGaOptionMarketValue_Delta2` |  |  |  |
| 19 | `FS.GA.OPTION.MARKET.VALUE.OPTION.COMPENSATION.PRICE` | `FsGaOptionMarketValue_OptionCompensationPrice` |  |  |  |
| 20 | `FS.GA.OPTION.MARKET.VALUE.MAKER.USER.NAME` | `FsGaOptionMarketValue_MakerUserName` |  |  |  |
| 21 | `FS.GA.OPTION.MARKET.VALUE.MAKER.PROCESSING.DATE` | `FsGaOptionMarketValue_MakerProcessingDate` |  |  |  |
| 22 | `FS.GA.OPTION.MARKET.VALUE.RESERVED10` | `FsGaOptionMarketValue_Reserved10` |  |  |  |
| 23 | `FS.GA.OPTION.MARKET.VALUE.RESERVED9` | `FsGaOptionMarketValue_Reserved9` |  |  |  |
| 24 | `FS.GA.OPTION.MARKET.VALUE.RESERVED8` | `FsGaOptionMarketValue_Reserved8` |  |  |  |
| 25 | `FS.GA.OPTION.MARKET.VALUE.RESERVED7` | `FsGaOptionMarketValue_Reserved7` |  |  |  |
| 26 | `FS.GA.OPTION.MARKET.VALUE.RESERVED6` | `FsGaOptionMarketValue_Reserved6` |  |  |  |
| 27 | `FS.GA.OPTION.MARKET.VALUE.RESERVED5` | `FsGaOptionMarketValue_Reserved5` |  |  |  |
| 28 | `FS.GA.OPTION.MARKET.VALUE.RESERVED4` | `FsGaOptionMarketValue_Reserved4` |  |  |  |
| 29 | `FS.GA.OPTION.MARKET.VALUE.RESERVED3` | `FsGaOptionMarketValue_Reserved3` |  |  |  |
| 30 | `FS.GA.OPTION.MARKET.VALUE.RESERVED2` | `FsGaOptionMarketValue_Reserved2` |  |  |  |
| 31 | `FS.GA.OPTION.MARKET.VALUE.RESERVED1` | `FsGaOptionMarketValue_Reserved1` |  |  |  |
| 32 | `FS.GA.OPTION.MARKET.VALUE.LOCAL.REF` | `FsGaOptionMarketValue_LocalRef` |  |  |  |
| 33 | `FS.GA.OPTION.MARKET.VALUE.OVERRIDE` | `FsGaOptionMarketValue_Override` |  |  |  |
| 34 | `FS.GA.OPTION.MARKET.VALUE.RECORD.STATUS` | `FsGaOptionMarketValue_RecordStatus` |  |  |  |
| 35 | `FS.GA.OPTION.MARKET.VALUE.CURR.NO` | `FsGaOptionMarketValue_CurrNo` |  |  |  |
| 36 | `FS.GA.OPTION.MARKET.VALUE.INPUTTER` | `FsGaOptionMarketValue_Inputter` |  |  |  |
| 37 | `FS.GA.OPTION.MARKET.VALUE.DATE.TIME` | `FsGaOptionMarketValue_DateTime` |  |  |  |
| 38 | `FS.GA.OPTION.MARKET.VALUE.AUTHORISER` | `FsGaOptionMarketValue_Authoriser` |  |  |  |
| 39 | `FS.GA.OPTION.MARKET.VALUE.CO.CODE` | `FsGaOptionMarketValue_CoCode` |  |  |  |
| 40 | `FS.GA.OPTION.MARKET.VALUE.DEPT.CODE` | `FsGaOptionMarketValue_DeptCode` |  |  |  |
| 41 | `FS.GA.OPTION.MARKET.VALUE.AUDITOR.CODE` | `FsGaOptionMarketValue_AuditorCode` |  |  |  |
| 42 | `FS.GA.OPTION.MARKET.VALUE.AUDIT.DATE.TIME` | `FsGaOptionMarketValue_AuditDateTime` |  |  |  |
