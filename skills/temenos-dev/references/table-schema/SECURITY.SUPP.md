# SECURITY.SUPP — Table Schema

> Source: `INSERTS/I_F.SECURITY.SUPP` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SSP.SECURITY.CURRENCY` | `SecuritySupp_SecurityCurrency` | TField |  | Defines the currency of the Security. Currency is entered automatically from the SECURITY.MASTER file. Validation Rules: 3 Alphabetic characters No Input field. |
| 2 | `SC.SSP.TOTAL.ISSUED` | `SecuritySupp_TotalIssued` | TField | No | Records the total number of shares or bonds issued or in circulation in this particular Security. Validation Rules: 1-18 Numeric characters. (Optional Input) |
| 3 | `SC.SSP.SHARE.ANALYSIS` | `SecuritySupp_ShareAnalysis` | TField | Yes | Specifies whether or not a particular Security is to be included in analysis reporting. Not used currently but included for future enhancement. Validation Rules: 1 - 2 Alphabetic characters. (Mandatory Input) Only "Y" or "NO" can be entered in this field. Default is "NO". |
| 4 | `SC.SSP.TICKER.SYMBOL` | `SecuritySupp_TickerSymbol` | TField | No | Records the U.S Stock Exchanges' stock codes where known. Each Ticker Symbol must be unique. Validation Rules: 1-10 Alpha-numeric characters. (Optional Input) Examples: I B M Corp. Common Stock = IBMco. |
| 5 | `SC.SSP.CONVERSION.PREMIUM` | `SecuritySupp_ConversionPremium` | TField | No | Records the conversion premium of convertible stock. Validation Rules: 1-18 numeric characters. (Optional Input) |
| 6 | `SC.SSP.PRICE.EARN.RATIO` | `SecuritySupp_PriceEarnRatio` | TField |  | Contains the latest or projected price earnings ratio, i.e. price over its earnings per share. |
| 7 | `SC.SSP.EX.DATE` | `SecuritySupp_ExDate` |  |  |  |
| 8 | `SC.SSP.PAY.DATE` | `SecuritySupp_PayDate` |  |  |  |
| 9 | `SC.SSP.DIVIDEND.RATE` | `SecuritySupp_DividendRate` |  |  |  |
| 10 | `SC.SSP.COUPON.NO` | `SecuritySupp_CouponNo` |  |  |  |
| 11 | `SC.SSP.CALL.DATES` | `SecuritySupp_CallDates` |  |  |  |
| 12 | `SC.SSP.CPN.NO.CALC` | `SecuritySupp_CpnNoCalc` | TField |  | Indicates whether the Security has numbered coupons attached and if the interest contained in these should be calculated. Validation Rules: 1 - 2 Alphabetic characters. Only "Y" or "NO" can be entered in this field. Default value is "NO". |
| 13 | `SC.SSP.TAX.DECLARE.VALUE` | `SecuritySupp_TaxDeclareValue` | TField | No | This field is used to record the value (price) of the security at the financial year-end, for Tax purposes. Validation Rules: 1 - 18 Numeric characters. (Optional input) |
| 14 | `SC.SSP.LAST.DIV.PAID` | `SecuritySupp_LastDivPaid` | TField |  | Validation Rules: 1 - 18 Numeric characters (No input field) |
| 15 | `SC.SSP.LAST.DIV.DATE` | `SecuritySupp_LastDivDate` | TField |  | Records the date at which the last Dividend was paid. Used in conjunction with the LAST.DIV.PAID field. Validation Rules: Standard date format (No Input field) |
| 16 | `SC.SSP.MAXIMUM.PRICE` | `SecuritySupp_MaximumPrice` | TField |  | Records the highest price reached for this Security within a specified period of time. Validation Rules: 0 - 18 Numeric characters No Input field |
| 17 | `SC.SSP.MAX.PRICE.DATE` | `SecuritySupp_MaxPriceDate` | TField |  | Records the date at which the "MAXIMUM.PRICE" was reached. Validation Rules: Standard Date format No Input field |
| 18 | `SC.SSP.MINIMUM.PRICE` | `SecuritySupp_MinimumPrice` | TField |  | Records the lowest price paid for this Security within a particular time period. Validation Rules: 1 - 18 Numeric characters (No Input field) |
| 19 | `SC.SSP.MIN.PRICE.DATE` | `SecuritySupp_MinPriceDate` | TField |  | Records the date at which the "MINIMUM.PRICE" was reached. Validation Rules: Standard date format No Input field |
| 20 | `SC.SSP.CALL.PUT.MATRTY` | `SecuritySupp_CallPutMatrty` |  |  |  |
| 21 | `SC.SSP.DATE.FROM` | `SecuritySupp_DateFrom` |  |  |  |
| 22 | `SC.SSP.DATE.TO` | `SecuritySupp_DateTo` |  |  |  |
| 23 | `SC.SSP.PRICE` | `SecuritySupp_Price` |  |  |  |
| 24 | `SC.SSP.QUANTITY` | `SecuritySupp_Quantity` |  |  |  |
| 25 | `SC.SSP.PROBABILITY` | `SecuritySupp_Probability` |  |  |  |
| 26 | `SC.SSP.CURRENT.YIELD` | `SecuritySupp_CurrentYield` |  |  |  |
| 27 | `SC.SSP.DURATION` | `SecuritySupp_Duration` |  |  |  |
| 28 | `SC.SSP.DURATION.MODIFY` | `SecuritySupp_DurationModify` |  |  |  |
| 29 | `SC.SSP.CONVEXITY` | `SecuritySupp_Convexity` |  |  |  |
| 30 | `SC.SSP.YIELD.TO.CALL` | `SecuritySupp_YieldToCall` |  |  |  |
| 31 | `SC.SSP.YIELD.TO.LIFE` | `SecuritySupp_YieldToLife` |  |  |  |
| 32 | `SC.SSP.YIELD.TO.MAT` | `SecuritySupp_YieldToMat` |  |  |  |
| 33 | `SC.SSP.BID.PRICE` | `SecuritySupp_BidPrice` | TField |  | Contains the latest 'highest' price a prospective buyer is prepared to pay for a security and will be updated automatically from the Pricing System. Validation Rules: No Input |
| 34 | `SC.SSP.OFFER.PRICE` | `SecuritySupp_OfferPrice` | TField |  | Contains the latest 'lowest' price a Seller is prepared to accept for his security and will be updated automatically from the Pricing System. Validation Rules: No Input |
| 35 | `SC.SSP.STRIKING.PRICE` | `SecuritySupp_StrikingPrice` | TField |  | Records the price at which the owner of an option can buy or sell the underlying stock. Validation Rules: No Input |
| 36 | `SC.SSP.MARKET.RATING` | `SecuritySupp_MarketRating` | TField |  | Records the market rating of the Security according to a particular rating service such as Standard and Poor's etc. Validation Rules: No Input. |
| 37 | `SC.SSP.BETA.FACTOR` | `SecuritySupp_BetaFactor` | TField |  | Updated automatically with a rating for each particular Security. Validation Rules: No Input. |
| 38 | `SC.SSP.TK.EX.CODE` | `SecuritySupp_TkExCode` |  |  |  |
| 39 | `SC.SSP.TAXATION.VALUE` | `SecuritySupp_TaxationValue` | TField |  | This Field is used to Store the Value of the Secuirty for Taxation Purposes. Validation Rules: No Input field |
| 40 | `SC.SSP.TAXATION.DATE` | `SecuritySupp_TaxationDate` | TField |  | This field denotes the Date the Taxation Value was calculated Validation Rules: No input Field |
| 41 | `SC.SSP.EQUALISE.PRD` | `SecuritySupp_EqualisePrd` |  |  |  |
| 42 | `SC.SSP.DIARY.ID` | `SecuritySupp_DiaryId` |  |  |  |
| 43 | `SC.SSP.PRICE.CURRENCY` | `SecuritySupp_PriceCurrency` | TField |  | Defines the price currency of the Security. Currency is entered automatically from the SECURITY.MASTER file. |
| 44 | `SC.SSP.EXP.YEAR` | `SecuritySupp_ExpYear` |  |  |  |
| 45 | `SC.SSP.NET.EXP.RATIO` | `SecuritySupp_NetExpRatio` |  |  |  |
| 46 | `SC.SSP.NET.EXP.CATEG.AVG` | `SecuritySupp_NetExpCategAvg` |  |  |  |
| 47 | `SC.SSP.MGT.FEE.ACTUAL` | `SecuritySupp_MgtFeeActual` |  |  |  |
| 48 | `SC.SSP.MGT.FEE.CATEG.AVG` | `SecuritySupp_MgtFeeCategAvg` |  |  |  |
| 49 | `SC.SSP.ADMIN.FEE.ACTUAL` | `SecuritySupp_AdminFeeActual` |  |  |  |
| 50 | `SC.SSP.ADMIN.FEE.CATEG.AVG` | `SecuritySupp_AdminFeeCategAvg` |  |  |  |
| 51 | `SC.SSP.PERIOD` | `SecuritySupp_Period` |  |  |  |
| 52 | `SC.SSP.RETURN` | `SecuritySupp_Return` |  |  |  |
| 53 | `SC.SSP.BENCHMARK` | `SecuritySupp_Benchmark` |  |  |  |
| 54 | `SC.SSP.ALPHA` | `SecuritySupp_Alpha` |  |  |  |
| 55 | `SC.SSP.BETA` | `SecuritySupp_Beta` |  |  |  |
| 56 | `SC.SSP.STND.DEVIATN` | `SecuritySupp_StndDeviatn` |  |  |  |
| 57 | `SC.SSP.R.SQUARED` | `SecuritySupp_RSquared` |  |  |  |
| 58 | `SC.SSP.SHARPE.RATIO` | `SecuritySupp_SharpeRatio` |  |  |  |
| 59 | `SC.SSP.SORTINO.RATIO` | `SecuritySupp_SortinoRatio` |  |  |  |
| 60 | `SC.SSP.TREYNOR.RATIO` | `SecuritySupp_TreynorRatio` |  |  |  |
| 61 | `SC.SSP.INFO.RATIO` | `SecuritySupp_InfoRatio` |  |  |  |
| 62 | `SC.SSP.BENCHMARK.RTN` | `SecuritySupp_BenchmarkRtn` |  |  |  |
| 63 | `SC.SSP.CATEG.RTN` | `SecuritySupp_CategRtn` |  |  |  |
| 64 | `SC.SSP.SUB.CATG.RTN` | `SecuritySupp_SubCatgRtn` |  |  |  |
| 65 | `SC.SSP.RTN.CATG.RANK` | `SecuritySupp_RtnCatgRank` |  |  |  |
| 66 | `SC.SSP.RISK` | `SecuritySupp_Risk` |  |  |  |
| 67 | `SC.SSP.RATING` | `SecuritySupp_Rating` |  |  |  |
| 68 | `SC.SSP.TOT.ASSETS.CCY` | `SecuritySupp_TotAssetsCcy` |  |  |  |
| 69 | `SC.SSP.TOT.ASSETS` | `SecuritySupp_TotAssets` |  |  |  |
| 70 | `SC.SSP.GEOG.REG.CNTY` | `SecuritySupp_GeogRegCnty` |  |  |  |
| 71 | `SC.SSP.GEOG.PERC` | `SecuritySupp_GeogPerc` |  |  |  |
| 72 | `SC.SSP.LARGEST.HLDNG` | `SecuritySupp_LargestHldng` |  |  |  |
| 73 | `SC.SSP.LARGEST.HLD.PERC` | `SecuritySupp_LargestHldPerc` |  |  |  |
| 74 | `SC.SSP.RESERVED.8` | `SecuritySupp_Reserved8` | TField |  |  |
| 75 | `SC.SSP.RESERVED.7` | `SecuritySupp_Reserved7` | TField |  |  |
| 76 | `SC.SSP.RESERVED.6` | `SecuritySupp_Reserved6` | TField |  |  |
| 77 | `SC.SSP.RESERVED.5` | `SecuritySupp_Reserved5` | TField |  |  |
| 78 | `SC.SSP.RESERVED.4` | `SecuritySupp_Reserved4` | TField |  |  |
| 79 | `SC.SSP.RESERVED.3` | `SecuritySupp_Reserved3` | TField |  |  |
| 80 | `SC.SSP.RESERVED.2` | `SecuritySupp_Reserved2` | TField |  |  |
| 81 | `SC.SSP.RESERVED.1` | `SecuritySupp_Reserved1` | TField |  |  |
| 82 | `SC.SSP.LOCAL.REF` | `SecuritySupp_LocalRef` |  |  |  |
| 83 | `SC.SSP.RECORD.STATUS` | `SecuritySupp_RecordStatus` | String |  |  |
| 84 | `SC.SSP.CURR.NO` | `SecuritySupp_CurrNo` | String |  |  |
| 85 | `SC.SSP.INPUTTER` | `SecuritySupp_Inputter` |  |  |  |
| 86 | `SC.SSP.DATE.TIME` | `SecuritySupp_DateTime` |  |  |  |
| 87 | `SC.SSP.AUTHORISER` | `SecuritySupp_Authoriser` | String |  |  |
| 88 | `SC.SSP.CO.CODE` | `SecuritySupp_CoCode` | String |  |  |
| 89 | `SC.SSP.DEPT.CODE` | `SecuritySupp_DeptCode` | String |  |  |
| 90 | `SC.SSP.AUDITOR.CODE` | `SecuritySupp_AuditorCode` | String |  |  |
| 91 | `SC.SSP.AUDIT.DATE.TIME` | `SecuritySupp_AuditDateTime` | String |  |  |
