# DX.MARKET.PRICE — Table Schema

> Source: `INSERTS/I_F.DX.MARKET.PRICE` in `DX_Pricing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.MKT.PRICE.SET` | `DxMarketPrice_PriceSet` | TField |  | Its gets value from DX.PRICE.SET. It holds two values CLOSING - END OF EXCHANGE: Prices are updated during the end of exchange processing. CURRENT - ON-LINE: Prices can be updated online using a verify application DX.RV.CHECK.PRICES. If the revaluation occurs during End of Exchange then PRICE.SET holds the value CLOSING. If the revaluation occurs Online then PRICE.SET holds the value CURRENT. |
| 2 | `DX.MKT.OPTION.TYPE` | `DxMarketPrice_OptionType` |  |  |  |
| 3 | `DX.MKT.CONTRACT.CODE` | `DxMarketPrice_ContractCode` | TField |  | It is a NOINPUT field. The Contract CODE for the trade, as per the information in DX.CONTRACT.MASTER. Its value should be a valid record in DX.CONTRACT.MASTER. Gets value from DX.TRADE. |
| 4 | `DX.MKT.TRADE.CCY` | `DxMarketPrice_TradeCcy` | TField |  | It is a NOINPUT field. It is the contract currency of the trade. Its value is populated from DX.TRADE. |
| 5 | `DX.MKT.MATURITY.DATE` | `DxMarketPrice_MaturityDate` | TField |  | It is NOINPUT field whose value is got from the DX.TRADE. The delivery period or prompt date of the contract transacted. The date must be greater than the Trade Date. |
| 6 | `DX.MKT.CALL.PUT` | `DxMarketPrice_CallPut` | TField |  | It is NOINPUT field whose value is got from DX.TRADE. It holds single value either CALL or PUT based on the trade. |
| 7 | `DX.MKT.STRIKE` | `DxMarketPrice_Strike` | TField |  | It is NOINPUT field whose value is got from DX.TRADE. It is the External Strike Price. The price at which an option holder has the right to buy (Call Options) or sell (Put Options) the underlying instrument, or to cash-settle the option if appropriate, to exercise the option. |
| 8 | `DX.MKT.INT.STRIKE` | `DxMarketPrice_IntStrike` | TField |  | It is a NOINPUT field whose value is got from DX.TRADE. The price is calculated as Internal number of ticks * tick value for strike price. |
| 9 | `DX.MKT.DELIVERY.CCY` | `DxMarketPrice_DeliveryCcy` | TField |  | A NOINPUT field whose value is defaulted from delivery currency of DX.TRADE. This is the user-defined alpha currency code. |
| 10 | `DX.MKT.OPTION.STYLE` | `DxMarketPrice_OptionStyle` | TField |  | A NOINPUT field which holds the first character of option style value in DX.TRADE. This will hold the value either 'A' for American, 'E' for European or 'C' for Carribean options |
| 11 | `DX.MKT.USR.FLD.NAME` | `DxMarketPrice_UsrFldName` |  |  |  |
| 12 | `DX.MKT.USR.FLD.VAL` | `DxMarketPrice_UsrFldVal` |  |  |  |
| 13 | `DX.MKT.USR.FLD.TEXT` | `DxMarketPrice_UsrFldText` |  |  |  |
| 14 | `DX.MKT.USR.FLD.PRICE` | `DxMarketPrice_UsrFldPrice` |  |  |  |
| 15 | `DX.MKT.RESERVED30` | `DxMarketPrice_Reserved30` |  |  |  |
| 16 | `DX.MKT.RESERVED29` | `DxMarketPrice_Reserved29` |  |  |  |
| 17 | `DX.MKT.RESERVED28` | `DxMarketPrice_Reserved28` | TField |  |  |
| 18 | `DX.MKT.RESERVED27` | `DxMarketPrice_Reserved27` | TField |  |  |
| 19 | `DX.MKT.CONTRACT.TYPE` | `DxMarketPrice_ContractType` | TField |  | It is a NOINPUT field whose value is got from DX.TRADE. It accepts three values namely : FUTURE,OPTION,STOCK. |
| 20 | `DX.MKT.PRICE.UNITS` | `DxMarketPrice_PriceUnits` | TField |  | It is a NOINPUT field whose value is got from DX.CONTRACT.MASTER whose contract is traded. The unit of measure relative to which the price is quoted. It is used for price related description. |
| 21 | `DX.MKT.PRICE.CCY` | `DxMarketPrice_PriceCcy` | TField |  | It is a NOINPUT field whose value is got from the DX.CONTRACT.MASTER. It is the contract specification currency as set by the relative exchange. This is the user-defined alpha currency code. |
| 22 | `DX.MKT.PRICE.DPS` | `DxMarketPrice_PriceDps` | TField |  | It is NOINPUT field whose value is got from the DX.CONTRACT.MASTER. The number of decimal places for the price quote. This also changes the number of decimal places in the multi-value set of Price Band. |
| 23 | `DX.MKT.PRICE` | `DxMarketPrice_Price` | TField |  | It is a NOINPUT field. It holds the quote currency price in which revaluation should be done. |
| 24 | `DX.MKT.INT.PRICE` | `DxMarketPrice_IntPrice` | TField |  | It is a NOINPUT field whose value is got from DX.TRADE. It is the internal price in standard T24 price format. Its value is calculated as Internal number of ticks * tick value for Futures price or Option premium |
| 25 | `DX.MKT.RISK.TYPE.IND` | `DxMarketPrice_RiskTYpeInd` |  |  |  |
| 26 | `DX.MKT.REG.RISK.LEVEL` | `DxMarketPrice_RegRiskLevel` |  |  |  |
| 27 | `DX.MKT.QUOTE.CCY` | `DxMarketPrice_QuoteCcy` | TField |  | The currency of the quoted price in which valuation should be done. If QUOTE.CCY is Null then it takes the PRICE.CCY whose value is defined in the DX.CONTRACT.MASTER. |
| 28 | `DX.MKT.QUOTE.PRICE` | `DxMarketPrice_QuotePrice` | TField |  | The new price in which revaluation should be done. This is used internally as the price as which to calculate the internal price |
| 29 | `DX.MKT.QUOTE.EXC` | `DxMarketPrice_QuoteExc` | TField |  | It is a NOINPUT field. The rate of exchange between the price currency and the quote currency |
| 30 | `DX.MKT.PRIIP.KIID.LINK` | `DxMarketPrice_PriipKiidLink` | TField |  | This field holds the KIID(Key Investor Information Document) link URL for PRIIP KIID PRIIP stands for Packaged Retail Investment and Insurance Based Products It accepts Alpha-numeric input such as URL link |
| 31 | `DX.MKT.UCITS.KIID.LINK` | `DxMarketPrice_UcitsKiidLink` | TField |  | This field holds the KIID(Key Investor Information Document) link for UCITS KIID UCITS stands for Undertakings for the Collective Investment in Transferable Securities and is regulatory framework of the European Commission It accepts Alpha-numeric input such as URL link |
| 32 | `DX.MKT.PRICE.SOURCE` | `DxMarketPrice_PriceSource` | TField |  | Price source describes the type of pricing model to be used for revaluation. Its value should be a valid record in DX.PRICE.SOURCE. The price source is also setup in DX.CONTRACT.MASTER. |
| 33 | `DX.MKT.PRICE.DATE` | `DxMarketPrice_PriceDate` | TField |  | The current system date. |
| 34 | `DX.MKT.PRICE.TIME` | `DxMarketPrice_PriceTime` | TField |  | The current system time. |
| 35 | `DX.MKT.RESERVED22` | `DxMarketPrice_Reserved22` | TField |  |  |
| 36 | `DX.MKT.RESERVED21` | `DxMarketPrice_Reserved21` | TField |  |  |
| 37 | `DX.MKT.TIME.TO.EXPIRY` | `DxMarketPrice_TimeToExpiry` | TField |  | It is a NOINPUT field. It denotes the time to mature the contract. |
| 38 | `DX.MKT.RESERVED20` | `DxMarketPrice_Reserved20` | TField |  |  |
| 39 | `DX.MKT.RESERVED19` | `DxMarketPrice_Reserved19` | TField |  |  |
| 40 | `DX.MKT.INT.RATE` | `DxMarketPrice_IntRate` | TField |  | The internal rate for the primary customer. Indicates whether the contract is a interest rate contract. |
| 41 | `DX.MKT.SEC.INT.RATE` | `DxMarketPrice_SecIntRate` | TField |  | The secondary internal rate for the secondary customer. |
| 42 | `DX.MKT.INTEREST.BASIS` | `DxMarketPrice_InterestBasis` | TField |  | Denotes the method for interest calculation. Should be a valid record in INTEREST.BASIS. |
| 43 | `DX.MKT.RESERVED18` | `DxMarketPrice_Reserved18` | TField |  |  |
| 44 | `DX.MKT.RESERVED17` | `DxMarketPrice_Reserved17` | TField |  |  |
| 45 | `DX.MKT.ALT.IND.NAME` | `DxMarketPrice_AltIndName` |  |  |  |
| 46 | `DX.MKT.ALT.IND.ID` | `DxMarketPrice_AltIndId` |  |  |  |
| 47 | `DX.MKT.RESERVED16` | `DxMarketPrice_Reserved16` |  |  |  |
| 48 | `DX.MKT.RESERVED15` | `DxMarketPrice_Reserved15` |  |  |  |
| 49 | `DX.MKT.RESERVED14` | `DxMarketPrice_Reserved14` | TField |  |  |
| 50 | `DX.MKT.RESERVED13` | `DxMarketPrice_Reserved13` | TField |  |  |
| 51 | `DX.MKT.DELTA` | `DxMarketPrice_Delta` | TField |  | This represents the rate of change of the option price with respect to the underlying asset. Greek value generated as part of the option pricing. |
| 52 | `DX.MKT.GAMMA` | `DxMarketPrice_Gamma` | TField |  | This represents the rate of change of the delta with respect to the underlying asset. Greek value generated as part of the option pricing. |
| 53 | `DX.MKT.VEGA` | `DxMarketPrice_Vega` | TField |  | This represents the rate of change of the value with respect to the volatility of the underlying asset. Greek value generated as part of the option pricing. |
| 54 | `DX.MKT.RHO` | `DxMarketPrice_Rho` | TField |  | The rate at which the price of a derivative changes relative to a change in the risk-free rate of interest. Rho measures the sensitivity of an option or options portfolio to a change in interest rate. Values are available for both Call and Put options. Greek value generated as part of the option pricing. |
| 55 | `DX.MKT.THETA` | `DxMarketPrice_Theta` | TField |  | A measure of the rate of decline in the value of an option due to the passage of time. Theta can also be referred to as the time decay on the value of an option. Theta is part of the group of measures known as the Greeks which is used in options pricing. Values are available for both Call and Put options. |
| 56 | `DX.MKT.RESERVED11` | `DxMarketPrice_Reserved11` | TField |  |  |
| 57 | `DX.MKT.VOLATILITY` | `DxMarketPrice_Volatility` | TField |  | A variable in option pricing formulas showing the extent to which the return of the underlying asset will fluctuate between now and the option's expiration. Values are available for both Call and Put options. Used to input the volatilities to be used by the option pricing models. |
| 58 | `DX.MKT.VOLATILITY.KEY` | `DxMarketPrice_VolatilityKey` | TField |  | Key to DX.VOLATALITY. The key for this file is CONTRACT.CODE-MATURITY. |
| 59 | `DX.MKT.RESERVED10` | `DxMarketPrice_Reserved10` | TField |  |  |
| 60 | `DX.MKT.RESERVED9` | `DxMarketPrice_Reserved9` | TField |  |  |
| 61 | `DX.MKT.SOURCE.APP` | `DxMarketPrice_SourceApp` | TField |  | It is a NOINPUT field. It specifies the source application. |
| 62 | `DX.MKT.SOURCE.KEY` | `DxMarketPrice_SourceKey` | TField |  | It is a NOINPUT field. Record id of the transaction being priced. |
| 63 | `DX.MKT.RESERVED8` | `DxMarketPrice_Reserved8` | TField |  |  |
| 64 | `DX.MKT.RESERVED7` | `DxMarketPrice_Reserved7` | TField |  |  |
| 65 | `DX.MKT.GEN.DATA.NAME` | `DxMarketPrice_GenDataName` |  |  |  |
| 66 | `DX.MKT.GEN.DATA.CODE` | `DxMarketPrice_GenDataCode` |  |  |  |
| 67 | `DX.MKT.GEN.DATA.LIMIT` | `DxMarketPrice_GenDataLimit` |  |  |  |
| 68 | `DX.MKT.RESERVED6` | `DxMarketPrice_Reserved6` |  |  |  |
| 69 | `DX.MKT.RESERVED5` | `DxMarketPrice_Reserved5` |  |  |  |
| 70 | `DX.MKT.RESERVED4` | `DxMarketPrice_Reserved4` | TField |  |  |
| 71 | `DX.MKT.RESERVED3` | `DxMarketPrice_Reserved3` | TField |  |  |
| 72 | `DX.MKT.UND.PRICE` | `DxMarketPrice_UndPrice` | TField |  | Underlying Price / Exchange price of the two currencies It is a NOINPUT field. |
| 73 | `DX.MKT.UND.INT.PRICE` | `DxMarketPrice_UndIntPrice` | TField |  | This is the Underlying Internal Price. It is a NOINPUT field. |
| 74 | `DX.MKT.RESERVED2` | `DxMarketPrice_Reserved2` |  |  |  |
| 75 | `DX.MKT.RESERVED1` | `DxMarketPrice_Reserved1` | TField |  |  |
| 76 | `DX.MKT.LOCAL.REF` | `DxMarketPrice_LocalRef` |  |  |  |
| 77 | `DX.MKT.OVERRIDE` | `DxMarketPrice_Override` |  |  |  |
| 78 | `DX.MKT.RECORD.STATUS` | `DxMarketPrice_RecordStatus` | String |  |  |
| 79 | `DX.MKT.CURR.NO` | `DxMarketPrice_CurrNo` | String |  |  |
| 80 | `DX.MKT.INPUTTER` | `DxMarketPrice_Inputter` |  |  |  |
| 81 | `DX.MKT.DATE.TIME` | `DxMarketPrice_DateTime` |  |  |  |
| 82 | `DX.MKT.AUTHORISER` | `DxMarketPrice_Authoriser` | String |  |  |
| 83 | `DX.MKT.CO.CODE` | `DxMarketPrice_CoCode` | String |  |  |
| 84 | `DX.MKT.DEPT.CODE` | `DxMarketPrice_DeptCode` | String |  |  |
| 85 | `DX.MKT.AUDITOR.CODE` | `DxMarketPrice_AuditorCode` | String |  |  |
| 86 | `DX.MKT.AUDIT.DATE.TIME` | `DxMarketPrice_AuditDateTime` | String |  |  |
