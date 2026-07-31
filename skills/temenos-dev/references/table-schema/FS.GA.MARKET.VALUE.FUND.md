# FS.GA.MARKET.VALUE.FUND — Table Schema

> Source: `INSERTS/I_F.FS.GA.MARKET.VALUE.FUND` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.MARKET.VALUE.FUND.PARENT.REF.ID` | `FsGaMarketValueFund_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.MARKET.VALUE.FUND.ORA.ROWID` | `FsGaMarketValueFund_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.MARKET.VALUE.FUND.INTERNAL.SECURITY.ID` | `FsGaMarketValueFund_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 4 | `FS.GA.MARKET.VALUE.FUND.GTI.CODE` | `FsGaMarketValueFund_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 5 | `FS.GA.MARKET.VALUE.FUND.IDENTIFIER.CODE.TELEKURS` | `FsGaMarketValueFund_IdentifierCodeTelekurs` | TField |  | Identifiier Code Telekurs Multifonds DB Column is ID_TELK. |
| 6 | `FS.GA.MARKET.VALUE.FUND.PREVIOUS.BID.PRICE` | `FsGaMarketValueFund_PreviousBidPrice` | TField |  | Reflects the Bid Price of an instrument Multifonds DB Column is COURSVAL_BID_PRED. |
| 7 | `FS.GA.MARKET.VALUE.FUND.PREVIOUS.OFFER.PRICE` | `FsGaMarketValueFund_PreviousOfferPrice` | TField |  | Reflects the Previous Day Offer Price of an instrument Multifonds DB Column is COURSVAL_OFFER_PRED. |
| 8 | `FS.GA.MARKET.VALUE.FUND.SECURITY.TYPE` | `FsGaMarketValueFund_SecurityType` | TField |  | Type OF security Multifonds DB Column is SECURITY_TYPE. |
| 9 | `FS.GA.MARKET.VALUE.FUND.RATE.TYPE` | `FsGaMarketValueFund_RateType` | TField |  | Indicates the rate type inserted (Manually, Loader or MF Calculated) Multifonds DB Column is PRICE_TYPE. |
| 10 | `FS.GA.MARKET.VALUE.FUND.BID.PRICE.PRED.TYPE` | `FsGaMarketValueFund_BidPricePredType` | TField |  | Bid Price Pred Type Multifonds DB Column is TYPE_COURSVAL_BID_PRED. |
| 11 | `FS.GA.MARKET.VALUE.FUND.OFFER.PRICE.PRED.TYPE` | `FsGaMarketValueFund_OfferPricePredType` | TField |  | Offer Price Pred Type Multifonds DB Column is TYPE_COURSVAL_OFFER_PRED. |
| 12 | `FS.GA.MARKET.VALUE.FUND.EXTERNAL.SECURITY.ID` | `FsGaMarketValueFund_ExternalSecurityId` | TField |  | The External identification code for Security like 01 for Telekurs, 03 for Sedol. Also used for other provider identifiers Multifonds DB Column is SEC_ID. |
| 13 | `FS.GA.MARKET.VALUE.FUND.PRICE.TYPE.IDENTIFIER` | `FsGaMarketValueFund_PriceTypeIdentifier` | TField |  | Price type identifier as mid/bid/offer Multifonds DB Column is TYPE_PRICE. |
| 14 | `FS.GA.MARKET.VALUE.FUND.TELEKURS.ID` | `FsGaMarketValueFund_TelekursId` | TField |  | Telekurs Id Multifonds DB Column is TELEKURS_ID. |
| 15 | `FS.GA.MARKET.VALUE.FUND.SESSION.NUMBER` | `FsGaMarketValueFund_SessionNumber` | TField |  | Session Number Multifonds DB Column is NO_SESSION. |
| 16 | `FS.GA.MARKET.VALUE.FUND.FUND.ID` | `FsGaMarketValueFund_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 17 | `FS.GA.MARKET.VALUE.FUND.CUSIP` | `FsGaMarketValueFund_Cusip` | TField |  | Committee on Uniform Securities Identification Procedures. A CUSIP is a nine digit numeric or alphanumeric code that identifies security and facilitates clearing and settlement of trades Multifonds DB Column is CUSIP. |
| 18 | `FS.GA.MARKET.VALUE.FUND.SHORT.DESC` | `FsGaMarketValueFund_ShortDesc` | TField |  | This can be used to provide a Short description of the fields like security,Ctable,Account Group etc. Multifonds DB Column is ABREGE. |
| 19 | `FS.GA.MARKET.VALUE.FUND.ISIN.CODE` | `FsGaMarketValueFund_IsinCode` | TField |  | International security identification number (ISIN) Multifonds DB Column is CODISIN. |
| 20 | `FS.GA.MARKET.VALUE.FUND.ISIN.SEQUENCE` | `FsGaMarketValueFund_IsinSequence` | TField |  | ISIN sequence of the security. Multifonds DB Column is SEQISIN. |
| 21 | `FS.GA.MARKET.VALUE.FUND.SECURITY.DESCRIPTION` | `FsGaMarketValueFund_SecurityDescription` | TField |  | Description of security Multifonds DB Column is NOMVAL. |
| 22 | `FS.GA.MARKET.VALUE.FUND.QUOTATION.CURRENCY` | `FsGaMarketValueFund_QuotationCurrency` | TField |  | The quotation currency of the security in general Multifonds DB Column is CMONCOTA. |
| 23 | `FS.GA.MARKET.VALUE.FUND.ISSUE.COUNTRY` | `FsGaMarketValueFund_IssueCountry` | TField |  | Internal Identifier for a country, which is used in various places to include or exclude a specific country from a functionality Multifonds DB Column is CPAYSVAL. |
| 24 | `FS.GA.MARKET.VALUE.FUND.QUOTATION.PLACE` | `FsGaMarketValueFund_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 25 | `FS.GA.MARKET.VALUE.FUND.INCOME.TYPE` | `FsGaMarketValueFund_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 26 | `FS.GA.MARKET.VALUE.FUND.PRICE.SOURCE` | `FsGaMarketValueFund_PriceSource` | TField |  | Provider code like Telekers, Reuters etc Multifonds DB Column is CORC. |
| 27 | `FS.GA.MARKET.VALUE.FUND.CFOURC` | `FsGaMarketValueFund_Cfourc` | TField |  | Cfourc Multifonds DB Column is CFOURC. |
| 28 | `FS.GA.MARKET.VALUE.FUND.PREVIOUS.PRICE.DATE` | `FsGaMarketValueFund_PreviousPriceDate` | TField |  | Previous Price Date Multifonds DB Column is DATECOURS_PRED. |
| 29 | `FS.GA.MARKET.VALUE.FUND.PREVIOUS.PRICE` | `FsGaMarketValueFund_PreviousPrice` | TField |  | Previous Price Multifonds DB Column is COURSVAL_PRED. |
| 30 | `FS.GA.MARKET.VALUE.FUND.DATE.OF.PRICE` | `FsGaMarketValueFund_DateOfPrice` | TField |  | Value date of the securities prices Multifonds DB Column is DATECOURS. |
| 31 | `FS.GA.MARKET.VALUE.FUND.MARKET.PRICE` | `FsGaMarketValueFund_MarketPrice` | TField |  | Market price for NAV Multifonds DB Column is COURSVAL. |
| 32 | `FS.GA.MARKET.VALUE.FUND.DURATION` | `FsGaMarketValueFund_Duration` | TField |  | Average period (in years) of the time of the binding of cash Multifonds DB Column is DURATION. |
| 33 | `FS.GA.MARKET.VALUE.FUND.PERCENTAGE.VAR` | `FsGaMarketValueFund_PercentageVar` | TField |  | Percentage Var Multifonds DB Column is PC_VAR. |
| 34 | `FS.GA.MARKET.VALUE.FUND.TEST.A` | `FsGaMarketValueFund_TestA` | TField |  | Test A Multifonds DB Column is TEST_A. |
| 35 | `FS.GA.MARKET.VALUE.FUND.TEST.B` | `FsGaMarketValueFund_TestB` | TField |  | Test B Multifonds DB Column is TEST_B. |
| 36 | `FS.GA.MARKET.VALUE.FUND.TEST.C` | `FsGaMarketValueFund_TestC` | TField |  | Test C Multifonds DB Column is TEST_C. |
| 37 | `FS.GA.MARKET.VALUE.FUND.TEST.D` | `FsGaMarketValueFund_TestD` | TField |  | Test D Multifonds DB Column is TEST_D. |
| 38 | `FS.GA.MARKET.VALUE.FUND.TEST.E` | `FsGaMarketValueFund_TestE` | TField |  | Test E Multifonds DB Column is TEST_E. |
| 39 | `FS.GA.MARKET.VALUE.FUND.TEST.F` | `FsGaMarketValueFund_TestF` | TField |  | Test F Multifonds DB Column is TEST_F. |
| 40 | `FS.GA.MARKET.VALUE.FUND.TEST.G` | `FsGaMarketValueFund_TestG` | TField |  | Test G Multifonds DB Column is TEST_G. |
| 41 | `FS.GA.MARKET.VALUE.FUND.TEST.H` | `FsGaMarketValueFund_TestH` | TField |  | Test H Multifonds DB Column is TEST_H. |
| 42 | `FS.GA.MARKET.VALUE.FUND.EVALUATION.TYPE` | `FsGaMarketValueFund_EvaluationType` | TField |  | Valuation method for specific security types such as zero bonds, polish T-bills, Mortgaged Backed Securities. Multifonds DB Column is TEVALUATION. |
| 43 | `FS.GA.MARKET.VALUE.FUND.TRADE.OR.VALUE.OR.ACC.DATE` | `FsGaMarketValueFund_TradeOrValueOrAccDate` | TField |  | Input Trade date or Value date or accounting date. Depends on the feature that is used Multifonds DB Column is DCTA. |
| 44 | `FS.GA.MARKET.VALUE.FUND.COURSVAL.VNI` | `FsGaMarketValueFund_CoursvalVni` | TField |  | Coursval Vni Multifonds DB Column is COURSVAL_VNI. |
| 45 | `FS.GA.MARKET.VALUE.FUND.PC.VAR.VNI.VAL` | `FsGaMarketValueFund_PcVarVniVal` | TField |  | Pc Var Vni Val Multifonds DB Column is PC_VAR_VNI_VAL. |
| 46 | `FS.GA.MARKET.VALUE.FUND.VALUATION.METHOD` | `FsGaMarketValueFund_ValuationMethod` | TField |  | This field enable user to define a default valuation method by Fund / GTI / Process Multifonds DB Column is FCYELD. |
| 47 | `FS.GA.MARKET.VALUE.FUND.LOT.NUMBER` | `FsGaMarketValueFund_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 48 | `FS.GA.MARKET.VALUE.FUND.USER.COURS` | `FsGaMarketValueFund_UserCours` | TField |  | User Cours Multifonds DB Column is USR_COURS. |
| 49 | `FS.GA.MARKET.VALUE.FUND.EXPIRY.DATE` | `FsGaMarketValueFund_ExpiryDate` | TField |  | Expiry Date Multifonds DB Column is DATE_ECH. |
| 50 | `FS.GA.MARKET.VALUE.FUND.TRI` | `FsGaMarketValueFund_Tri` | TField |  | Tri Multifonds DB Column is TRI. |
| 51 | `FS.GA.MARKET.VALUE.FUND.PROVENANCE` | `FsGaMarketValueFund_Provenance` | TField |  | Provenance Multifonds DB Column is PROVENANCE. |
| 52 | `FS.GA.MARKET.VALUE.FUND.WORK.ACCOUNTING.DATE` | `FsGaMarketValueFund_WorkAccountingDate` | TField |  | Work Accounting Date Multifonds DB Column is WORK_DCTA. |
| 53 | `FS.GA.MARKET.VALUE.FUND.TRAVAIL.TYPE` | `FsGaMarketValueFund_TravailType` | TField |  | Travail Type Multifonds DB Column is TYPE_TRAVAIL. |
| 54 | `FS.GA.MARKET.VALUE.FUND.CORRESPONDENT` | `FsGaMarketValueFund_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 55 | `FS.GA.MARKET.VALUE.FUND.OPTION.ID` | `FsGaMarketValueFund_OptionId` | TField |  | Option Security ID Multifonds DB Column is NOPT. |
| 56 | `FS.GA.MARKET.VALUE.FUND.FUTURE.ID.CODE` | `FsGaMarketValueFund_FutureIdCode` | TField |  | Future, Security,Swap,Derivative,CFD ID Code Multifonds DB Column is NFUT. |
| 57 | `FS.GA.MARKET.VALUE.FUND.BID.PRICE` | `FsGaMarketValueFund_BidPrice` | TField |  | Denotes the Bid price of the securities Multifonds DB Column is COURSVAL_BID. |
| 58 | `FS.GA.MARKET.VALUE.FUND.OFFER.PRICE` | `FsGaMarketValueFund_OfferPrice` | TField |  | Denotes the Offer price of the securities Multifonds DB Column is COURSVAL_OFFER. |
| 59 | `FS.GA.MARKET.VALUE.FUND.OLD.NAV.VALUE.DATE` | `FsGaMarketValueFund_OldNavValueDate` | TField |  | Old Nav Value Date Multifonds DB Column is DATE_COURS_OLD_NAV. |
| 60 | `FS.GA.MARKET.VALUE.FUND.YIELD` | `FsGaMarketValueFund_Yield` | TField |  | Security Yield Multifonds DB Column is YIELD. |
| 61 | `FS.GA.MARKET.VALUE.FUND.DAYS.OF.ACCRUED.INTEREST` | `FsGaMarketValueFund_DaysOfAccruedInterest` | TField |  | Number of days of purchase/sale interest in a transaction done on an interest bearing instrument Multifonds DB Column is NBJOURS. |
| 62 | `FS.GA.MARKET.VALUE.FUND.QUALITY.CODE` | `FsGaMarketValueFund_QualityCode` | TField |  | Quality code Multifonds DB Column is QUALITY_CODE. |
| 63 | `FS.GA.MARKET.VALUE.FUND.TYPE.OF.PRICE` | `FsGaMarketValueFund_TypeOfPrice` | TField |  | Price Type Code Multifonds DB Column is TYPE_COURSVAL. |
| 64 | `FS.GA.MARKET.VALUE.FUND.PRICING.QUALITY.CODE` | `FsGaMarketValueFund_PricingQualityCode` | TField |  | Pricing Quality Code Multifonds DB Column is LIB_QUALITY_CODE. |
| 65 | `FS.GA.MARKET.VALUE.FUND.PREVIOUS.PRICE.TYPE` | `FsGaMarketValueFund_PreviousPriceType` | TField |  | Previous Price Type Multifonds DB Column is TYPE_COURSVAL_PRED. |
| 66 | `FS.GA.MARKET.VALUE.FUND.C.D` | `FsGaMarketValueFund_CD` | TField |  | C D Multifonds DB Column is COD_DPRICE. |
| 67 | `FS.GA.MARKET.VALUE.FUND.SELECTED.BID.PRICE` | `FsGaMarketValueFund_SelectedBidPrice` | TField |  | Selected bid price during price injection based on pricing parmeters. Multifonds DB Column is TYPE_COURSVAL_BID. |
| 68 | `FS.GA.MARKET.VALUE.FUND.SELECTED.OFFER.PRICE` | `FsGaMarketValueFund_SelectedOfferPrice` | TField |  | Selected offer price during price injection based on pricing parmeters. Multifonds DB Column is TYPE_COURSVAL_OFFER. |
| 69 | `FS.GA.MARKET.VALUE.FUND.AFF` | `FsGaMarketValueFund_Aff` | TField |  | AFF Flag Multifonds DB Column is FLG_AFF. |
| 70 | `FS.GA.MARKET.VALUE.FUND.ERROR.CODE` | `FsGaMarketValueFund_ErrorCode` | TField |  | Error code definition Multifonds DB Column is CSORT. |
| 71 | `FS.GA.MARKET.VALUE.FUND.PROVIDER.DESCRIPTION` | `FsGaMarketValueFund_ProviderDescription` | TField |  | Provider Description Multifonds DB Column is LIB_PROVIDER. |
| 72 | `FS.GA.MARKET.VALUE.FUND.COURS.DESCRIPTION` | `FsGaMarketValueFund_CoursDescription` | TField |  | Cours Description Multifonds DB Column is LIB_COURS. |
| 73 | `FS.GA.MARKET.VALUE.FUND.FIXED.PC` | `FsGaMarketValueFund_FixedPc` | TField |  | Fixed Pc Multifonds DB Column is FIXED_PC. |
| 74 | `FS.GA.MARKET.VALUE.FUND.CODPRICE.DESCRIPTION` | `FsGaMarketValueFund_CodpriceDescription` | TField |  | Codprice Description Multifonds DB Column is LIB_CODPRICE. |
| 75 | `FS.GA.MARKET.VALUE.FUND.SECURITY.VAL.DESCRIPTION` | `FsGaMarketValueFund_SecurityValDescription` | TField |  | Description of security Multifonds DB Column is LIB_VAL. |
| 76 | `FS.GA.MARKET.VALUE.FUND.COUNTRY` | `FsGaMarketValueFund_Country` | TField |  | Country identifier linked to secuity/ fund, etc. Multifonds DB Column is PAYSVAL. |
| 77 | `FS.GA.MARKET.VALUE.FUND.NUM.VAL` | `FsGaMarketValueFund_NumVal` | TField |  | Num Val Multifonds DB Column is NUM_VAL. |
| 78 | `FS.GA.MARKET.VALUE.FUND.LIB.REASON.PC.VAR` | `FsGaMarketValueFund_LibReasonPcVar` | TField |  | Lib Reason Pc Var Multifonds DB Column is LIB_REASON_PC_VAR. |
| 79 | `FS.GA.MARKET.VALUE.FUND.REASON.PC.VAR` | `FsGaMarketValueFund_ReasonPcVar` | TField |  | Reason Pc Var Multifonds DB Column is REASON_PC_VAR. |
| 80 | `FS.GA.MARKET.VALUE.FUND.SAVE.ORDER` | `FsGaMarketValueFund_SaveOrder` | TField |  | Save Order Multifonds DB Column is ORDRE_SAVE. |
| 81 | `FS.GA.MARKET.VALUE.FUND.B.SAVE.TEST` | `FsGaMarketValueFund_BSaveTest` | TField |  | B Save Test Multifonds DB Column is TEST_B_SAVE. |
| 82 | `FS.GA.MARKET.VALUE.FUND.SEC.PC.VAR` | `FsGaMarketValueFund_SecPcVar` | TField |  | Sec Pc Var Multifonds DB Column is SEC_PC_VAR. |
| 83 | `FS.GA.MARKET.VALUE.FUND.NUMBER.OF.DAYS.TO.SWITCH` | `FsGaMarketValueFund_NumberOfDaysToSwitch` | TField |  | Number of days to switch one valaution method to other. Multifonds DB Column is NB_SWITCH. |
| 84 | `FS.GA.MARKET.VALUE.FUND.INCOME.EQUALISATION.PER.UNIT` | `FsGaMarketValueFund_IncomeEqualisationPerUnit` | TField |  | Income Equalisation Per Unit Multifonds DB Column is RNI_PART. |
| 85 | `FS.GA.MARKET.VALUE.FUND.INCOME.EQ.PER.UNIT.PREV` | `FsGaMarketValueFund_IncomeEqPerUnitPrev` | TField |  | Prior day income equalisation per unit Multifonds DB Column is RNI_PART_PREC. |
| 86 | `FS.GA.MARKET.VALUE.FUND.COURS.SEL.DATE` | `FsGaMarketValueFund_CoursSelDate` | TField |  | Cours Sel Date Multifonds DB Column is NB_JOURS_PREC_COURS. |
| 87 | `FS.GA.MARKET.VALUE.FUND.PRICE.DATE.SELECT` | `FsGaMarketValueFund_PriceDateSelect` | TField |  | Selection of price date by comparing prices before injection Multifonds DB Column is DATE_COURS_SEL. |
| 88 | `FS.GA.MARKET.VALUE.FUND.MID.PRICE.SELECT` | `FsGaMarketValueFund_MidPriceSelect` | TField |  | Selection of mid price by comparing prices before injection Multifonds DB Column is COURS_SEL. |
| 89 | `FS.GA.MARKET.VALUE.FUND.BID.PRICE.SELECT` | `FsGaMarketValueFund_BidPriceSelect` | TField |  | Selection of bid price by comparing prices before injection Multifonds DB Column is COURS_SEL_BID. |
| 90 | `FS.GA.MARKET.VALUE.FUND.OFFER.PRICE.SELECT` | `FsGaMarketValueFund_OfferPriceSelect` | TField |  | Selection of offer price by comparing prices before injection Multifonds DB Column is COURS_SEL_OFFER. |
| 91 | `FS.GA.MARKET.VALUE.FUND.AKTIENGEWINN.PER.UNIT` | `FsGaMarketValueFund_AktiengewinnPerUnit` | TField |  | Increase in value of units attributable to gain on shares. Multifonds DB Column is ACTIENGEWINN_PART. |
| 92 | `FS.GA.MARKET.VALUE.FUND.AKTIEN.PERUNIT.PREV.DAY` | `FsGaMarketValueFund_AktienPerunitPrevDay` | TField |  | Prior day Aktiengewinn per unit Multifonds DB Column is ACTIENGEWINN_PART_PREC. |
| 93 | `FS.GA.MARKET.VALUE.FUND.LEVERAGE` | `FsGaMarketValueFund_Leverage` | TField |  | Leverage Multifonds DB Column is LEVERAGE. |
| 94 | `FS.GA.MARKET.VALUE.FUND.INDEX.ID` | `FsGaMarketValueFund_IndexId` | TField |  | Index Identifier Multifonds DB Column is NOVAL_INDEX_ID. |
| 95 | `FS.GA.MARKET.VALUE.FUND.VARIATION.PERCENT` | `FsGaMarketValueFund_VariationPercent` | TField |  | Maximum variation admitted from the previous quote, above which a warning window is prompted. Multifonds DB Column is PCT_INDEX. |
| 96 | `FS.GA.MARKET.VALUE.FUND.DEVIATION.PERCENTAGE` | `FsGaMarketValueFund_DeviationPercentage` | TField |  | Deviation Percentage Multifonds DB Column is PCT_ECART. |
| 97 | `FS.GA.MARKET.VALUE.FUND.SPREAD.HIGH.PERCENTAGE` | `FsGaMarketValueFund_SpreadHighPercentage` | TField |  | Spreadh Percentage Multifonds DB Column is PCT_SPREADH. |
| 98 | `FS.GA.MARKET.VALUE.FUND.SPREAD.LOW.PERCENTAGE` | `FsGaMarketValueFund_SpreadLowPercentage` | TField |  | Spreadl Percentage Multifonds DB Column is PCT_SPREADL. |
| 99 | `FS.GA.MARKET.VALUE.FUND.OST` | `FsGaMarketValueFund_Ost` | TField |  | indicates the operation on security (split, merge, etc.). Multifonds DB Column is OST. |
| 100 | `FS.GA.MARKET.VALUE.FUND.PERFORMANCE.FEES.PER.UNIT` | `FsGaMarketValueFund_PerformanceFeesPerUnit` | TField |  | Performance fees per unit applied on a transaction. Multifonds DB Column is PF_PART. |
| 101 | `FS.GA.MARKET.VALUE.FUND.PF.PART` | `FsGaMarketValueFund_PfPart` | TField |  | Pf Part Multifonds DB Column is PF_PART_PREC. |
| 102 | `FS.GA.MARKET.VALUE.FUND.TEST.I` | `FsGaMarketValueFund_TestI` | TField |  | Test I Multifonds DB Column is TEST_I. |
| 103 | `FS.GA.MARKET.VALUE.FUND.TEST.J` | `FsGaMarketValueFund_TestJ` | TField |  | Test J Multifonds DB Column is TEST_J. |
| 104 | `FS.GA.MARKET.VALUE.FUND.TEST.K` | `FsGaMarketValueFund_TestK` | TField |  | Test K Multifonds DB Column is TEST_K. |
| 105 | `FS.GA.MARKET.VALUE.FUND.SENSIBILITY` | `FsGaMarketValueFund_Sensibility` | TField |  | Sensibility relates to security Multifonds DB Column is SENSIBILITY. |
| 106 | `FS.GA.MARKET.VALUE.FUND.DELTA` | `FsGaMarketValueFund_Delta` | TField |  | Delta-Difference Multifonds DB Column is DELTA. |
| 107 | `FS.GA.MARKET.VALUE.FUND.ACCRUED.INTEREST` | `FsGaMarketValueFund_AccruedInterest` | TField |  | Accrued interest of the security Multifonds DB Column is MINT. |
| 108 | `FS.GA.MARKET.VALUE.FUND.AKTIENGEWINN.IN.PERCENTAGE` | `FsGaMarketValueFund_AktiengewinnInPercentage` | TField |  | Aktiengewinn in percentage Multifonds DB Column is ACTIENGEWINN_PART_PCT. |
| 109 | `FS.GA.MARKET.VALUE.FUND.ACTIENGEWINN.PRT.PCT.PRECEDING` | `FsGaMarketValueFund_ActiengewinnPrtPctPreceding` | TField |  | Actiengewinn Prt Pct Preceding Multifonds DB Column is ACTIENGEWINN_PART_PCT_PREC. |
| 110 | `FS.GA.MARKET.VALUE.FUND.INCOME.YIELD` | `FsGaMarketValueFund_IncomeYield` | TField |  | Income Yield Multifonds DB Column is INC_YIELD. |
| 111 | `FS.GA.MARKET.VALUE.FUND.ORIGIN.INCOME.YIELD` | `FsGaMarketValueFund_OriginIncomeYield` | TField |  | Origin income yield/Income Yield Feeder Multifonds DB Column is CTYPE_INC_YIELD. |
| 112 | `FS.GA.MARKET.VALUE.FUND.ORIGIN.YIELD.TO.MATURITY` | `FsGaMarketValueFund_OriginYieldToMaturity` | TField |  | Origin Yield To Maturity/Redumption Yield Feeder Multifonds DB Column is CTYPE_RED_YIELD. |
| 113 | `FS.GA.MARKET.VALUE.FUND.TEST.L` | `FsGaMarketValueFund_TestL` | TField |  | Test L Multifonds DB Column is TEST_L. |
| 114 | `FS.GA.MARKET.VALUE.FUND.PRICE.TRUE` | `FsGaMarketValueFund_PriceTrue` | TField |  | Price True Multifonds DB Column is COURSVAL_TRUE. |
| 115 | `FS.GA.MARKET.VALUE.FUND.MID.PRICE` | `FsGaMarketValueFund_MidPrice` | TField |  | Reflects the Middle Price of an instrument Multifonds DB Column is COURSVAL_MIDDLE. |
| 116 | `FS.GA.MARKET.VALUE.FUND.PRICE.TRUE.PRED` | `FsGaMarketValueFund_PriceTruePred` | TField |  | Price True Pred Multifonds DB Column is COURSVAL_TRUE_PRED. |
| 117 | `FS.GA.MARKET.VALUE.FUND.PRICE.MIDDLE.PRED` | `FsGaMarketValueFund_PriceMiddlePred` | TField |  | Price Middle Pred Multifonds DB Column is COURSVAL_MIDDLE_PRED. |
| 118 | `FS.GA.MARKET.VALUE.FUND.PROCESS.ID` | `FsGaMarketValueFund_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 119 | `FS.GA.MARKET.VALUE.FUND.TAXABLE.INCOME.PER.SHARE.UNIT` | `FsGaMarketValueFund_TaxableIncomePerShareUnit` | TField |  | The taxable income per share in unit Multifonds DB Column is TIS_PART. |
| 120 | `FS.GA.MARKET.VALUE.FUND.TIS.PART.PERCENTAGE` | `FsGaMarketValueFund_TisPartPercentage` | TField |  | Tis Part Percentage Multifonds DB Column is TIS_PART_PCT. |
| 121 | `FS.GA.MARKET.VALUE.FUND.TIS.PART.PREVIOUS` | `FsGaMarketValueFund_TisPartPrevious` | TField |  | Tis Part Prec Multifonds DB Column is TIS_PART_PREC. |
| 122 | `FS.GA.MARKET.VALUE.FUND.TIS.PART.PREVIOUS.PERCENTAGE` | `FsGaMarketValueFund_TisPartPreviousPercentage` | TField |  | Tis Part Prec Percentage Multifonds DB Column is TIS_PART_PCT_PREC. |
| 123 | `FS.GA.MARKET.VALUE.FUND.PLACE2` | `FsGaMarketValueFund_Place2` | TField |  | Place2 Multifonds DB Column is CPLACE2. |
| 124 | `FS.GA.MARKET.VALUE.FUND.PRICING.FACTOR.CODE` | `FsGaMarketValueFund_PricingFactorCode` | TField |  | Pricing factor code of security to determine how the price is quoted based on which the transaction amount is determined Multifonds DB Column is CCALCUL. |
| 125 | `FS.GA.MARKET.VALUE.FUND.MATURITY.REPAYMENT.PRICE` | `FsGaMarketValueFund_MaturityRepaymentPrice` | TField |  | The price at which an instruments if matured Multifonds DB Column is COURS_REMB. |
| 126 | `FS.GA.MARKET.VALUE.FUND.CALC.TYPE` | `FsGaMarketValueFund_CalcType` | TField |  | Calc Type Multifonds DB Column is CCALC_TYPE. |
| 127 | `FS.GA.MARKET.VALUE.FUND.PRICING` | `FsGaMarketValueFund_Pricing` | TField |  | Pricing Flag Multifonds DB Column is FLG_PRICING. |
| 128 | `FS.GA.MARKET.VALUE.FUND.SERVICE.CODE` | `FsGaMarketValueFund_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 129 | `FS.GA.MARKET.VALUE.FUND.MANAGER.CODE` | `FsGaMarketValueFund_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 130 | `FS.GA.MARKET.VALUE.FUND.QUALITY.CODE.BID` | `FsGaMarketValueFund_QualityCodeBid` | TField |  | Quality Code Bid Multifonds DB Column is QUALITY_CODE_BID. |
| 131 | `FS.GA.MARKET.VALUE.FUND.QUALITY.CODE.OFFER` | `FsGaMarketValueFund_QualityCodeOffer` | TField |  | Quality Code Offer Multifonds DB Column is QUALITY_CODE_OFFER. |
| 132 | `FS.GA.MARKET.VALUE.FUND.LIB.QUALITY.CODE.BID` | `FsGaMarketValueFund_LibQualityCodeBid` | TField |  | Lib Quality Code Bid Multifonds DB Column is LIB_QUALITY_CODE_BID. |
| 133 | `FS.GA.MARKET.VALUE.FUND.LIB.QUALITY.CODE.OFFER` | `FsGaMarketValueFund_LibQualityCodeOffer` | TField |  | Lib Quality Code Offer Multifonds DB Column is LIB_QUALITY_CODE_OFFER. |
| 134 | `FS.GA.MARKET.VALUE.FUND.IG.PER.UNIT` | `FsGaMarketValueFund_IgPerUnit` | TField |  | Target fund income per unit attributed to income generate from real estate Multifonds DB Column is IG_PART. |
| 135 | `FS.GA.MARKET.VALUE.FUND.IMMOBILIENGEWINN.PERCENTAGE` | `FsGaMarketValueFund_ImmobiliengewinnPercentage` | TField |  | Immobiliengewinn Percentage: German compliance field meaning Real Estate gain Multifonds DB Column is IG_PART_PCT. |
| 136 | `FS.GA.MARKET.VALUE.FUND.IG.PART.PERCENTAGE.PRECEDING` | `FsGaMarketValueFund_IgPartPercentagePreceding` | TField |  | Ig Part Percentage Preceding Multifonds DB Column is IG_PART_PCT_PREC. |
| 137 | `FS.GA.MARKET.VALUE.FUND.IG.PART.PRECEDING` | `FsGaMarketValueFund_IgPartPreceding` | TField |  | Ig Part Preceding Multifonds DB Column is IG_PART_PREC. |
| 138 | `FS.GA.MARKET.VALUE.FUND.REC.LINK` | `FsGaMarketValueFund_RecLink` | TField |  | Rec Link Multifonds DB Column is REC_LINK. |
| 139 | `FS.GA.MARKET.VALUE.FUND.QUANTITY` | `FsGaMarketValueFund_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 140 | `FS.GA.MARKET.VALUE.FUND.DELTA.2` | `FsGaMarketValueFund_Delta2` | TField |  | Delta-Difference 2 Multifonds DB Column is DELTA_2. |
| 141 | `FS.GA.MARKET.VALUE.FUND.KEST.PER.UNIT` | `FsGaMarketValueFund_KestPerUnit` | TField |  | German witholding tax per unit Multifonds DB Column is KEST_PART. |
| 142 | `FS.GA.MARKET.VALUE.FUND.KEST.PART.PERCENTAGE` | `FsGaMarketValueFund_KestPartPercentage` | TField |  | Kest Part Percentage Multifonds DB Column is KEST_PART_PCT. |
| 143 | `FS.GA.MARKET.VALUE.FUND.KEST.PART.PRECEDING` | `FsGaMarketValueFund_KestPartPreceding` | TField |  | Kest Part Preceding Multifonds DB Column is KEST_PART_PREC. |
| 144 | `FS.GA.MARKET.VALUE.FUND.KEST.PART.PERCENTAGE.PRECEDING` | `FsGaMarketValueFund_KestPartPercentagePreceding` | TField |  | Kest Part Percentage Preceding Multifonds DB Column is KEST_PART_PCT_PREC. |
| 145 | `FS.GA.MARKET.VALUE.FUND.VARIABLE.BID` | `FsGaMarketValueFund_VariableBid` | TField |  | Variable Bid Multifonds DB Column is PC_VAR_BID. |
| 146 | `FS.GA.MARKET.VALUE.FUND.VARIABLE.OFFER` | `FsGaMarketValueFund_VariableOffer` | TField |  | Variable Offer Multifonds DB Column is PC_VAR_OFFER. |
| 147 | `FS.GA.MARKET.VALUE.FUND.DISCOUNT.MARGIN` | `FsGaMarketValueFund_DiscountMargin` | TField |  | Discount margin or spread on security interest rates. Specific to Thai securities Multifonds DB Column is MARGIN_DM. |
| 148 | `FS.GA.MARKET.VALUE.FUND.TAXABLE.INCOME.2.PER.SHARE` | `FsGaMarketValueFund_TaxableIncome2PerShare` | TField |  | The taxable income 2 per share in unit Multifonds DB Column is TIS2_PART. |
| 149 | `FS.GA.MARKET.VALUE.FUND.TIS2.PART.PERCENTAGE` | `FsGaMarketValueFund_Tis2PartPercentage` | TField |  | Tis2 Part Percentage Multifonds DB Column is TIS2_PART_PCT. |
| 150 | `FS.GA.MARKET.VALUE.FUND.TIS2.PART.PRECEDING` | `FsGaMarketValueFund_Tis2PartPreceding` | TField |  | Tis2 Part Preceding Multifonds DB Column is TIS2_PART_PREC. |
| 151 | `FS.GA.MARKET.VALUE.FUND.TIS2.PART.PERCENTAGE.PRECEDING` | `FsGaMarketValueFund_Tis2PartPercentagePreceding` | TField |  | Tis2 Part Percentage Preceding Multifonds DB Column is TIS2_PART_PCT_PREC. |
| 152 | `FS.GA.MARKET.VALUE.FUND.TAXABLE.INCOME.3.PER.SHARE` | `FsGaMarketValueFund_TaxableIncome3PerShare` | TField |  | The taxable income 3 per share in unit Multifonds DB Column is TIS3_PART. |
| 153 | `FS.GA.MARKET.VALUE.FUND.TIS3.PART.PERCENTAGE` | `FsGaMarketValueFund_Tis3PartPercentage` | TField |  | Tis3 Part Percentage Multifonds DB Column is TIS3_PART_PCT. |
| 154 | `FS.GA.MARKET.VALUE.FUND.TIS3.PART.PRECEDING` | `FsGaMarketValueFund_Tis3PartPreceding` | TField |  | Tis3 Part Preceding Multifonds DB Column is TIS3_PART_PREC. |
| 155 | `FS.GA.MARKET.VALUE.FUND.TIS3.PART.PERCENTAGE.PRECEDING` | `FsGaMarketValueFund_Tis3PartPercentagePreceding` | TField |  | Tis3 Part Percentage Preceding Multifonds DB Column is TIS3_PART_PCT_PREC. |
| 156 | `FS.GA.MARKET.VALUE.FUND.TEST.M` | `FsGaMarketValueFund_TestM` | TField |  | Test M Multifonds DB Column is TEST_M. |
| 157 | `FS.GA.MARKET.VALUE.FUND.KOREAN.TAXABLE.PER.SHARE` | `FsGaMarketValueFund_KoreanTaxablePerShare` | TField |  | Korean Taxable per Share Multifonds DB Column is TCOURS_TX. |
| 158 | `FS.GA.MARKET.VALUE.FUND.TAXABLE.PERCENTAGE` | `FsGaMarketValueFund_TaxablePercentage` | TField |  | Taxable Percentage Multifonds DB Column is TCOURS_TX_PCT. |
| 159 | `FS.GA.MARKET.VALUE.FUND.TAXABLE.PERCENTAGE.PRECEDING` | `FsGaMarketValueFund_TaxablePercentagePreceding` | TField |  | Taxable Percentage Preceding Multifonds DB Column is TCOURS_TX_PCT_PREC. |
| 160 | `FS.GA.MARKET.VALUE.FUND.TAXABLE.PREVIOUS.DAY.PRICE` | `FsGaMarketValueFund_TaxablePreviousDayPrice` | TField |  | Taxable Price Previous Day Multifonds DB Column is TCOURS_TX_PREC. |
| 161 | `FS.GA.MARKET.VALUE.FUND.KOREAN.NONTAXABLE.PER.SHARE` | `FsGaMarketValueFund_KoreanNontaxablePerShare` | TField |  | Korean Nontaxable per Share Multifonds DB Column is TCOURS_NRTX. |
| 162 | `FS.GA.MARKET.VALUE.FUND.NON.TAXABLE.PRICE.PERCENT` | `FsGaMarketValueFund_NonTaxablePricePercent` | TField |  | Nominal price - (Taxable price - Normal price) Multifonds DB Column is TCOURS_NRTX_PCT. |
| 163 | `FS.GA.MARKET.VALUE.FUND.TAXABLE.NR.PERCENTAGE.PREC` | `FsGaMarketValueFund_TaxableNrPercentagePrec` | TField |  | Taxable Nr Percentage Prec Multifonds DB Column is TCOURS_NRTX_PCT_PREC. |
| 164 | `FS.GA.MARKET.VALUE.FUND.NR.TAXABLE.PRICE` | `FsGaMarketValueFund_NrTaxablePrice` | TField |  | NR Taxable Price Multifonds DB Column is TCOURS_NRTX_PREC. |
| 165 | `FS.GA.MARKET.VALUE.FUND.NON.TAXABLE.PRICE` | `FsGaMarketValueFund_NonTaxablePrice` | TField |  | Non Taxable Price Multifonds DB Column is TCOURS_NTX. |
| 166 | `FS.GA.MARKET.VALUE.FUND.NON.TAXABLE.PERCENTAGE` | `FsGaMarketValueFund_NonTaxablePercentage` | TField |  | Non Taxable Percentage Multifonds DB Column is TCOURS_NTX_PCT. |
| 167 | `FS.GA.MARKET.VALUE.FUND.NON.TAXABLE.PERCENTAGE.PREC` | `FsGaMarketValueFund_NonTaxablePercentagePrec` | TField |  | Non Taxable Percentage Prec Multifonds DB Column is TCOURS_NTX_PCT_PREC. |
| 168 | `FS.GA.MARKET.VALUE.FUND.NON.TAXABLE.PREVIOUS.DAY.PRICE` | `FsGaMarketValueFund_NonTaxablePreviousDayPrice` | TField |  | Non-Taxable Price Previous Day Multifonds DB Column is TCOURS_NTX_PREC. |
| 169 | `FS.GA.MARKET.VALUE.FUND.LOAD.DATE` | `FsGaMarketValueFund_LoadDate` | TField |  | Load Date Multifonds DB Column is LOAD_DATE. |
| 170 | `FS.GA.MARKET.VALUE.FUND.ID.CODE.DISPLAY` | `FsGaMarketValueFund_IdCodeDisplay` | TField |  | Id Code Display Multifonds DB Column is ID_CODE_DISP. |
| 171 | `FS.GA.MARKET.VALUE.FUND.SECURITY.ID.DISPLAY` | `FsGaMarketValueFund_SecurityIdDisplay` | TField |  | Security Id Display Multifonds DB Column is SEC_ID_DISP. |
| 172 | `FS.GA.MARKET.VALUE.FUND.FV.HIERARCHY` | `FsGaMarketValueFund_FvHierarchy` | TField |  | Fair Value Hierarchy Multifonds DB Column is FV_HIERARCHY. |
| 173 | `FS.GA.MARKET.VALUE.FUND.VM.VALUE` | `FsGaMarketValueFund_VmValue` | TField |  | Vm Value Multifonds DB Column is COURS_VM. |
| 174 | `FS.GA.MARKET.VALUE.FUND.UNDERLIER.PRICE` | `FsGaMarketValueFund_UnderlierPrice` | TField |  | Underlier Price Multifonds DB Column is UNDERLIER_PRICE. |
| 175 | `FS.GA.MARKET.VALUE.FUND.COURS.CLEAN` | `FsGaMarketValueFund_CoursClean` | TField |  | Cours Clean Multifonds DB Column is COURS_CLEAN. |
| 176 | `FS.GA.MARKET.VALUE.FUND.INV.FUNDS.TAX.1.PER.UNIT` | `FsGaMarketValueFund_InvFundsTax1PerUnit` | TField |  | Investment Funds Tax 1 Per Unit Multifonds DB Column is TG1_PART. |
| 177 | `FS.GA.MARKET.VALUE.FUND.TG1.PART.PERCENTAGE` | `FsGaMarketValueFund_Tg1PartPercentage` | TField |  | Tg1 Part Percentage Multifonds DB Column is TG1_PART_PCT. |
| 178 | `FS.GA.MARKET.VALUE.FUND.TG1.PART.PRECEDING` | `FsGaMarketValueFund_Tg1PartPreceding` | TField |  | Tg1 Part Preceding Multifonds DB Column is TG1_PART_PREC. |
| 179 | `FS.GA.MARKET.VALUE.FUND.TG1.PART.PRECEDING.PERCENTAGE` | `FsGaMarketValueFund_Tg1PartPrecedingPercentage` | TField |  | Tg1 Part Preceding Percentage Multifonds DB Column is TG1_PART_PCT_PREC. |
| 180 | `FS.GA.MARKET.VALUE.FUND.INV.FUNDS.TAX.2.PER.UNIT` | `FsGaMarketValueFund_InvFundsTax2PerUnit` | TField |  | Investment Funds Tax 2 Per Unit Multifonds DB Column is TG2_PART. |
| 181 | `FS.GA.MARKET.VALUE.FUND.TG2.PART.PERCENTAGE` | `FsGaMarketValueFund_Tg2PartPercentage` | TField |  | Tg2 Part Percentage Multifonds DB Column is TG2_PART_PCT. |
| 182 | `FS.GA.MARKET.VALUE.FUND.TG2.PART.PRECEDING` | `FsGaMarketValueFund_Tg2PartPreceding` | TField |  | Tg2 Part Preceding Multifonds DB Column is TG2_PART_PREC. |
| 183 | `FS.GA.MARKET.VALUE.FUND.TG2.PART.PRECEDING.PERCENTAGE` | `FsGaMarketValueFund_Tg2PartPrecedingPercentage` | TField |  | Tg2 Part Preceding Percentage Multifonds DB Column is TG2_PART_PCT_PREC. |
| 184 | `FS.GA.MARKET.VALUE.FUND.INV.FUNDS.TAX.3.PER.UNIT` | `FsGaMarketValueFund_InvFundsTax3PerUnit` | TField |  | Investment Funds Tax 3 Per Unit Multifonds DB Column is TG3_PART. |
| 185 | `FS.GA.MARKET.VALUE.FUND.TG3.PART.PERCENTAGE` | `FsGaMarketValueFund_Tg3PartPercentage` | TField |  | Tg3 Part Percentage Multifonds DB Column is TG3_PART_PCT. |
| 186 | `FS.GA.MARKET.VALUE.FUND.TG3.PART.PRECEDING` | `FsGaMarketValueFund_Tg3PartPreceding` | TField |  | Tg3 Part Preceding Multifonds DB Column is TG3_PART_PREC. |
| 187 | `FS.GA.MARKET.VALUE.FUND.TG3.PART.PRECEDING.PERCENTAGE` | `FsGaMarketValueFund_Tg3PartPrecedingPercentage` | TField |  | Tg3 Part Preceding Percentage Multifonds DB Column is TG3_PART_PCT_PREC. |
| 188 | `FS.GA.MARKET.VALUE.FUND.LOOK.THRU.RATIO` | `FsGaMarketValueFund_LookThruRatio` | TField |  | Percentage of investment/portfolio of the fund of fund which is in scope for the TIS calculation Multifonds DB Column is LOOK_THRU_RATIO. |
| 189 | `FS.GA.MARKET.VALUE.FUND.CLEAN.BID.VALUE` | `FsGaMarketValueFund_CleanBidValue` | TField |  | Clean Bid Value Multifonds DB Column is COURS_CLEAN_BID. |
| 190 | `FS.GA.MARKET.VALUE.FUND.CLEAN.OFFER.VALUE` | `FsGaMarketValueFund_CleanOfferValue` | TField |  | Clean Offer Value Multifonds DB Column is COURS_CLEAN_OFFER. |
| 191 | `FS.GA.MARKET.VALUE.FUND.MMF.VALUATION` | `FsGaMarketValueFund_MmfValuation` | TField |  | Money market Fund Valuation Multifonds DB Column is FLG_MMF_VALUATION. |
| 192 | `FS.GA.MARKET.VALUE.FUND.RESERVED10` | `FsGaMarketValueFund_Reserved10` | TField |  |  |
| 193 | `FS.GA.MARKET.VALUE.FUND.RESERVED9` | `FsGaMarketValueFund_Reserved9` | TField |  |  |
| 194 | `FS.GA.MARKET.VALUE.FUND.RESERVED8` | `FsGaMarketValueFund_Reserved8` | TField |  |  |
| 195 | `FS.GA.MARKET.VALUE.FUND.RESERVED7` | `FsGaMarketValueFund_Reserved7` | TField |  |  |
| 196 | `FS.GA.MARKET.VALUE.FUND.RESERVED6` | `FsGaMarketValueFund_Reserved6` | TField |  |  |
| 197 | `FS.GA.MARKET.VALUE.FUND.RESERVED5` | `FsGaMarketValueFund_Reserved5` | TField |  |  |
| 198 | `FS.GA.MARKET.VALUE.FUND.RESERVED4` | `FsGaMarketValueFund_Reserved4` | TField |  |  |
| 199 | `FS.GA.MARKET.VALUE.FUND.RESERVED3` | `FsGaMarketValueFund_Reserved3` | TField |  |  |
| 200 | `FS.GA.MARKET.VALUE.FUND.RESERVED2` | `FsGaMarketValueFund_Reserved2` | TField |  |  |
| 201 | `FS.GA.MARKET.VALUE.FUND.RESERVED1` | `FsGaMarketValueFund_Reserved1` | TField |  |  |
| 202 | `FS.GA.MARKET.VALUE.FUND.LOCAL.REF` | `FsGaMarketValueFund_LocalRef` |  |  |  |
| 203 | `FS.GA.MARKET.VALUE.FUND.OVERRIDE` | `FsGaMarketValueFund_Override` |  |  |  |
| 204 | `FS.GA.MARKET.VALUE.FUND.RECORD.STATUS` | `FsGaMarketValueFund_RecordStatus` | String |  |  |
| 205 | `FS.GA.MARKET.VALUE.FUND.CURR.NO` | `FsGaMarketValueFund_CurrNo` | String |  |  |
| 206 | `FS.GA.MARKET.VALUE.FUND.INPUTTER` | `FsGaMarketValueFund_Inputter` |  |  |  |
| 207 | `FS.GA.MARKET.VALUE.FUND.DATE.TIME` | `FsGaMarketValueFund_DateTime` |  |  |  |
| 208 | `FS.GA.MARKET.VALUE.FUND.AUTHORISER` | `FsGaMarketValueFund_Authoriser` | String |  |  |
| 209 | `FS.GA.MARKET.VALUE.FUND.CO.CODE` | `FsGaMarketValueFund_CoCode` | String |  |  |
| 210 | `FS.GA.MARKET.VALUE.FUND.DEPT.CODE` | `FsGaMarketValueFund_DeptCode` | String |  |  |
| 211 | `FS.GA.MARKET.VALUE.FUND.AUDITOR.CODE` | `FsGaMarketValueFund_AuditorCode` | String |  |  |
| 212 | `FS.GA.MARKET.VALUE.FUND.AUDIT.DATE.TIME` | `FsGaMarketValueFund_AuditDateTime` | String |  |  |
