# DX.MARKET.PRICE.HISTORY — Table Schema

> Source: `INSERTS/I_F.DX.MARKET.PRICE.HISTORY` in `DX_Pricing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.MKTH.PRICE.SET` | `DxMarketPriceHistory_PriceSet` | TField |  | Its gets value from DX.PRICE.SET. CLOSING - END OF EXCHANGE: Prices are updated during the end of exchange processing. CURRENT - ON-LINE: Prices can be updated online using a verify application DX.RV.CHECK.PRICES. If the revaluation occurs during End of Exchange then PRICE.SET holds the value CLOSING. If the revaluation occurs Online then PRICE.SET holds the value CURRENT. |
| 2 | `DX.MKTH.OPTION.TYPE` | `DxMarketPriceHistory_OptionType` |  |  |  |
| 3 | `DX.MKTH.CONTRACT.CODE` | `DxMarketPriceHistory_ContractCode` | TField |  | It is a NOINPUT field. The Contract CODE for the trade, as per the information in DX.CONTRACT.MASTER. Its value should be a valid record in DX.CONTRACT.MASTER. Gets value from DX.TRADE. |
| 4 | `DX.MKTH.TRADE.CCY` | `DxMarketPriceHistory_TradeCcy` | TField |  | It is a NOINPUT field. It is the contract currency of the trade. Its value is populated from DX.TRADE. |
| 5 | `DX.MKTH.MATURITY.DATE` | `DxMarketPriceHistory_MaturityDate` | TField |  | It is NOINPUT field whose value is got from the DX.TRADE. The delivery period or prompt date of the contract transacted. The date must be greater than the Trade Date. |
| 6 | `DX.MKTH.CALL.PUT` | `DxMarketPriceHistory_CallPut` | TField |  | It is NOINPUT field whose value is got from DX.TRADE. It holds single value either CALL or PUT based on the trade. |
| 7 | `DX.MKTH.STRIKE` | `DxMarketPriceHistory_Strike` | TField |  | It is NOINPUT field whose value is got from DX.TRADE. It is the External Strike Price. The price at which an option holder has the right to buy (Call Options) or sell (Put Options) the underlying instrument, or to cash-settle the option if appropriate, to exercise the option. |
| 8 | `DX.MKTH.INT.STRIKE` | `DxMarketPriceHistory_IntStrike` | TField |  | It is a NOINPUT field whose value is got from DX.TRADE. The price is calculated as Internal number of ticks * tick value for strike price. |
| 9 | `DX.MKTH.DELIVERY.CCY` | `DxMarketPriceHistory_DeliveryCcy` | TField |  |  |
| 10 | `DX.MKTH.OPTION.STYLE` | `DxMarketPriceHistory_OptionStyle` | TField |  |  |
| 11 | `DX.MKTH.USR.FLD.NAME` | `DxMarketPriceHistory_UsrFldName` |  |  |  |
| 12 | `DX.MKTH.USR.FLD.VAL` | `DxMarketPriceHistory_UsrFldVal` |  |  |  |
| 13 | `DX.MKTH.USR.FLD.TEXT` | `DxMarketPriceHistory_UsrFldText` |  |  |  |
| 14 | `DX.MKTH.USR.FLD.PRICE` | `DxMarketPriceHistory_UsrFldPrice` |  |  |  |
| 15 | `DX.MKTH.RESERVED30` | `DxMarketPriceHistory_Reserved30` |  |  |  |
| 16 | `DX.MKTH.RESERVED29` | `DxMarketPriceHistory_Reserved29` |  |  |  |
| 17 | `DX.MKTH.RESERVED28` | `DxMarketPriceHistory_Reserved28` | TField |  |  |
| 18 | `DX.MKTH.RESERVED27` | `DxMarketPriceHistory_Reserved27` | TField |  |  |
| 19 | `DX.MKTH.CONTRACT.TYPE` | `DxMarketPriceHistory_ContractType` | TField |  | It is a NOINPUT field whose value is got from DX.TRADE. It accepts three values namely : FUTURE,OPTION,STOCK. |
| 20 | `DX.MKTH.PRICE.UNITS` | `DxMarketPriceHistory_PriceUnits` | TField |  | It is a NOINPUT field whose value is got from DX.CONTRACT.MASTER whose contract is traded. The unit of measure relative to which the price is quoted. It is used for price related description. |
| 21 | `DX.MKTH.PRICE.CCY` | `DxMarketPriceHistory_PriceCcy` | TField |  | It is a NOINPUT field whose value is got from the DX.CONTRACT.MASTER. It is the contract specification currency as set by the relative exchange. This is the user-defined alpha currency code. |
| 22 | `DX.MKTH.PRICE.DPS` | `DxMarketPriceHistory_PriceDps` | TField |  | It is NOINPUT field whose value is got from the DX.CONTRACT.MASTER. The number of decimal places for the price quote. This also changes the number of decimal places in the multi-value set of Price Band. |
| 23 | `DX.MKTH.PRICE` | `DxMarketPriceHistory_Price` | TField |  | It is a NOINPUT field. It holds the quote currency price in which revaluation should be done. |
| 24 | `DX.MKTH.INT.PRICE` | `DxMarketPriceHistory_IntPrice` | TField |  | It is a NOINPUT field whose value is got from DX.TRADE. It is the internal price in standard T24 price format. Its value is calculated as INT.PRICE = Internal number of ticks * tick value for Futures price or Option premium. |
| 25 | `DX.MKTH.RISK.TYPE.IND` | `DxMarketPriceHistory_RiskTypeInd` |  |  |  |
| 26 | `DX.MKTH.REG.RISK.LEVEL` | `DxMarketPriceHistory_RegRiskLevel` |  |  |  |
| 27 | `DX.MKTH.QUOTE.CCY` | `DxMarketPriceHistory_QuoteCcy` | TField |  | The currency of the quoted price in which valuation should be done. If QUOTE.CCY is Null then it takes the PRICE.CCY whose value is defined in the DX.CONTRACT.MASTER. |
| 28 | `DX.MKTH.QUOTE.PRICE` | `DxMarketPriceHistory_QuotePrice` | TField |  | The new price in which revaluation should be done. This is used internally as the price as which to calculate the internal price. |
| 29 | `DX.MKTH.QUOTE.EXC` | `DxMarketPriceHistory_QuoteExc` | TField |  | It is a NOINPUT field. The rate of exchange between the price currency and the quote currency. |
| 30 | `DX.MKTH.PRIIP.KIID.LINK` | `DxMarketPriceHistory_PriipKiidLink` | TField |  | This field holds the KIID(Key Investor Information Document) link URL for PRIIP KIID PRIIP stands for Packaged Retail Investment and Insurance Based Products It accepts Alpha-numeric input such as URL link |
| 31 | `DX.MKTH.UCITS.KIID.LINK` | `DxMarketPriceHistory_UcitsKiidLink` | TField |  | This field holds the KIID(Key Investor Information Document) link for UCITS KIID UCITS stands for Undertakings for the Collective Investment in Transferable Securities and is regulatory framework of the European Commission It accepts Alpha-numeric input such as URL link |
| 32 | `DX.MKTH.PRICE.SOURCE` | `DxMarketPriceHistory_PriceSource` | TField |  | Price source describes the type of pricing model to be used for revaluation. Its value should be a valid record in DX.PRICE.SOURCE. The price source is also setup in DX.CONTRACT.MASTER. |
| 33 | `DX.MKTH.PRICE.DATE` | `DxMarketPriceHistory_PriceDate` | TField |  | The current system date. |
| 34 | `DX.MKTH.PRICE.TIME` | `DxMarketPriceHistory_PriceTime` | TField |  | The current system time. |
| 35 | `DX.MKTH.RESERVED22` | `DxMarketPriceHistory_Reserved22` | TField |  |  |
| 36 | `DX.MKTH.RESERVED21` | `DxMarketPriceHistory_Reserved21` | TField |  |  |
| 37 | `DX.MKTH.TIME.TO.EXPIRY` | `DxMarketPriceHistory_TimeToExpiry` | TField |  | It is a NOINPUT field. It denotes the time to mature the contract. |
| 38 | `DX.MKTH.RESERVED20` | `DxMarketPriceHistory_Reserved20` | TField |  |  |
| 39 | `DX.MKTH.RESERVED19` | `DxMarketPriceHistory_Reserved19` | TField |  |  |
| 40 | `DX.MKTH.INT.RATE` | `DxMarketPriceHistory_IntRate` | TField |  | The internal rate for the primary customer. Indicates whether the contract is a interest rate contract. |
| 41 | `DX.MKTH.SEC.INT.RATE` | `DxMarketPriceHistory_SecIntRate` | TField |  | The secondary internal rate for the secondary customer. |
| 42 | `DX.MKTH.INTEREST.BASIS` | `DxMarketPriceHistory_InterestBasis` | TField |  | Denotes the method for interest calculation. Should be a valid record in INTEREST.BASIS. |
| 43 | `DX.MKTH.RESERVED18` | `DxMarketPriceHistory_Reserved18` | TField |  |  |
| 44 | `DX.MKTH.RESERVED17` | `DxMarketPriceHistory_Reserved17` | TField |  |  |
| 45 | `DX.MKTH.ALT.IND.NAME` | `DxMarketPriceHistory_AltIndName` |  |  |  |
| 46 | `DX.MKTH.ALT.IND.ID` | `DxMarketPriceHistory_AltIndId` |  |  |  |
| 47 | `DX.MKTH.RESERVED16` | `DxMarketPriceHistory_Reserved16` |  |  |  |
| 48 | `DX.MKTH.RESERVED15` | `DxMarketPriceHistory_Reserved15` |  |  |  |
| 49 | `DX.MKTH.RESERVED14` | `DxMarketPriceHistory_Reserved14` | TField |  |  |
| 50 | `DX.MKTH.RESERVED13` | `DxMarketPriceHistory_Reserved13` | TField |  |  |
| 51 | `DX.MKTH.DELTA` | `DxMarketPriceHistory_Delta` | TField |  | This represents the rate of change of the option price with respect to the underlying asset. Greek value generated as part of the option pricing. |
| 52 | `DX.MKTH.GAMMA` | `DxMarketPriceHistory_Gamma` | TField |  | This represents the rate of change of the delta with respect to the underlying asset. Greek value generated as part of the option pricing. |
| 53 | `DX.MKTH.VEGA` | `DxMarketPriceHistory_Vega` | TField |  | This represents the rate of change of the value with respect to the volatility of the underlying asset. Greek value generated as part of the option pricing. |
| 54 | `DX.MKTH.RHO` | `DxMarketPriceHistory_Rho` | TField |  | The rate at which the price of a derivative changes relative to a change in the risk-free rate of interest. Rho measures the sensitivity of an option or options portfolio to a change in interest rate. Values are available for both Call and Put options. Greek value generated as part of the option pricing. |
| 55 | `DX.MKTH.THETA` | `DxMarketPriceHistory_Theta` | TField |  | A measure of the rate of decline in the value of an option due to the passage of time. Theta can also be referred to as the time decay on the value of an option. Theta is part of the group of measures known as the "Greeks" which is used in options pricing. Values are available for both Call and Put options. |
| 56 | `DX.MKTH.RESERVED11` | `DxMarketPriceHistory_Reserved11` | TField |  |  |
| 57 | `DX.MKTH.VOLATILITY` | `DxMarketPriceHistory_Volatility` | TField |  | A variable in option pricing formulas showing the extent to which the return of the underlying asset will fluctuate between now and the option's expiration. Values are available for both Call and Put options. Used to input the volatilities to be used by the option pricing models. |
| 58 | `DX.MKTH.VOLATILITY.KEY` | `DxMarketPriceHistory_VolatilityKey` | TField |  | Key to DX.VOLATALITY. The key for this file is CONTRACT.CODE-MATURITY. |
| 59 | `DX.MKTH.RESERVED10` | `DxMarketPriceHistory_Reserved10` | TField |  |  |
| 60 | `DX.MKTH.RESERVED9` | `DxMarketPriceHistory_Reserved9` | TField |  |  |
| 61 | `DX.MKTH.SOURCE.APP` | `DxMarketPriceHistory_SourceApp` | TField |  | It is a NOINPUT field. It specifies the source application. |
| 62 | `DX.MKTH.SOURCE.KEY` | `DxMarketPriceHistory_SourceKey` | TField |  | It is a NOINPUT field. Record id of the transaction being priced. |
| 63 | `DX.MKTH.RESERVED8` | `DxMarketPriceHistory_Reserved8` | TField |  |  |
| 64 | `DX.MKTH.RESERVED7` | `DxMarketPriceHistory_Reserved7` | TField |  |  |
| 65 | `DX.MKTH.GEN.DATA.NAME` | `DxMarketPriceHistory_GenDataName` |  |  |  |
| 66 | `DX.MKTH.GEN.DATA.CODE` | `DxMarketPriceHistory_GenDataCode` |  |  |  |
| 67 | `DX.MKTH.GEN.DATA.LIMIT` | `DxMarketPriceHistory_GenDataLimit` |  |  |  |
| 68 | `DX.MKTH.RESERVED6` | `DxMarketPriceHistory_Reserved6` |  |  |  |
| 69 | `DX.MKTH.RESERVED5` | `DxMarketPriceHistory_Reserved5` |  |  |  |
| 70 | `DX.MKTH.RESERVED4` | `DxMarketPriceHistory_Reserved4` | TField |  |  |
| 71 | `DX.MKTH.RESERVED3` | `DxMarketPriceHistory_Reserved3` | TField |  |  |
| 72 | `DX.MKTH.UND.PRICE` | `DxMarketPriceHistory_UndPrice` | TField |  | Underlying Price / Exchange price of the two currencies. It is a NOINPUT field. |
| 73 | `DX.MKTH.UND.INT.PRICE` | `DxMarketPriceHistory_UndIntPrice` | TField |  | This is the Underlying Internal Price. It is a NOINPUT field. |
| 74 | `DX.MKTH.RESERVED2` | `DxMarketPriceHistory_Reserved2` |  |  |  |
| 75 | `DX.MKTH.RESERVED1` | `DxMarketPriceHistory_Reserved1` | TField |  |  |
| 76 | `DX.MKTH.LOCAL.REF` | `DxMarketPriceHistory_LocalRef` |  |  |  |
| 77 | `DX.MKTH.OVERRIDE` | `DxMarketPriceHistory_Override` |  |  |  |
| 78 | `DX.MKTH.RECORD.STATUS` | `DxMarketPriceHistory_RecordStatus` | String |  |  |
| 79 | `DX.MKTH.CURR.NO` | `DxMarketPriceHistory_CurrNo` | String |  |  |
| 80 | `DX.MKTH.INPUTTER` | `DxMarketPriceHistory_Inputter` |  |  |  |
| 81 | `DX.MKTH.DATE.TIME` | `DxMarketPriceHistory_DateTime` |  |  |  |
| 82 | `DX.MKTH.AUTHORISER` | `DxMarketPriceHistory_Authoriser` | String |  |  |
| 83 | `DX.MKTH.CO.CODE` | `DxMarketPriceHistory_CoCode` | String |  |  |
| 84 | `DX.MKTH.DEPT.CODE` | `DxMarketPriceHistory_DeptCode` | String |  |  |
| 85 | `DX.MKTH.AUDITOR.CODE` | `DxMarketPriceHistory_AuditorCode` | String |  |  |
| 86 | `DX.MKTH.AUDIT.DATE.TIME` | `DxMarketPriceHistory_AuditDateTime` | String |  |  |
