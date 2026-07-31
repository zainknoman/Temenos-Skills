# FS.GA.SECURITY.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GA.SECURITY.MASTER` in `FS_SecurityMaster.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SECURITY.MASTER.PARENT.REF.ID` | `FsGaSecurityMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SECURITY.MASTER.ORA.ROWID` | `FsGaSecurityMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SECURITY.MASTER.SHORT.DESC` | `FsGaSecurityMaster_ShortDesc` | TField |  | This can be used to provide a Short description of the fields like security,Ctable,Account Group etc. Multifonds DB Column is ABREGE. |
| 4 | `FS.GA.SECURITY.MASTER.ACCOUNTING.FACTOR` | `FsGaSecurityMaster_AccountingFactor` | TField |  | Used for German compliance (MIG21). The factor indicates to which extent an amount has to be imputed for the calculation of the limits. Multifonds DB Column is ACC_FACTOR. |
| 5 | `FS.GA.SECURITY.MASTER.ACCRUAL.CONVENTION` | `FsGaSecurityMaster_AccrualConvention` | TField |  | Accrual convention for income securities which enable the management of week-ends and holidays for the determination of the coupon amount and interest&apos;s accruals Multifonds DB Column is ACCRUAL_CONV. |
| 6 | `FS.GA.SECURITY.MASTER.STATUS` | `FsGaSecurityMaster_Status` | TField |  | It representing the status of the securiies if they are active are not,this field could corresponds to security,Future,options etc. Multifonds DB Column is ACTIF. |
| 7 | `FS.GA.SECURITY.MASTER.ADJUSTED.HIGH.WATER.MARK` | `FsGaSecurityMaster_AdjustedHighWaterMark` | TField |  | Related to performance fees, calculated adjustment HWM value will be updated in this field. Multifonds DB Column is ADJ_HWM. |
| 8 | `FS.GA.SECURITY.MASTER.ASSET.TYPE` | `FsGaSecurityMaster_AssetType` | TField |  | Can define the asset of the security like, Bonds, Future,Mutual Funds, Swaps etc. Multifonds DB Column is ASSET_TYPE. |
| 9 | `FS.GA.SECURITY.MASTER.ALL.TIME.HIGH.NAV` | `FsGaSecurityMaster_AllTimeHighNav` | TField |  | Related to performance fees,Allows storing the ATH (all time high) information. The ATH is the highest NAV/share ever reached. Multifonds DB Column is ATH. |
| 10 | `FS.GA.SECURITY.MASTER.BASE.TOLERANCE.IN.BPS` | `FsGaSecurityMaster_BaseToleranceInBps` | TField |  | Used to define base tolerance rate in basis points for each market index security. The base tolerance defined at market index security is used exclusively for dynamic adjusted tolerance calculation. Multifonds DB Column is BASE_TOL_BPS. |
| 11 | `FS.GA.SECURITY.MASTER.ISSUE.CAPITAL` | `FsGaSecurityMaster_IssueCapital` | TField |  | Total amount of the issue. Used for investment restrictions control. Multifonds DB Column is CAPITAL_EMISSION. |
| 12 | `FS.GA.SECURITY.MASTER.POOL.COMMERCIAL.UNIT` | `FsGaSecurityMaster_PoolCommercialUnit` | TField |  | Pool commercial unit Multifonds DB Column is CARRONDI_POOL. |
| 13 | `FS.GA.SECURITY.MASTER.QUANTITY.ROUNDING.METHOD` | `FsGaSecurityMaster_QuantityRoundingMethod` | TField |  | Quantity Rounding Method Multifonds DB Column is CARRONDI_QTE_CONV. |
| 14 | `FS.GA.SECURITY.MASTER.PRICING.FACTOR.CODE` | `FsGaSecurityMaster_PricingFactorCode` | TField |  | Pricing factor code of security to determine how the price is quoted based on which the transaction amount is determined Multifonds DB Column is CCALCUL. |
| 15 | `FS.GA.SECURITY.MASTER.CONVERSION` | `FsGaSecurityMaster_Conversion` | TField |  | Conversion Multifonds DB Column is CCONV. |
| 16 | `FS.GA.SECURITY.MASTER.DECIMAL.ROUNDING.CODE` | `FsGaSecurityMaster_DecimalRoundingCode` | TField |  | Number of decimals to be taken for currency amounts . Generally,the number of decimals would be 2 except for currencies like Japanese Yen for instance, where the number of decimals is equal to zero. Multifonds DB Column is CDEC. |
| 17 | `FS.GA.SECURITY.MASTER.ROUNDING.CODE` | `FsGaSecurityMaster_RoundingCode` | TField |  | Decimal Rounding Code Multifonds DB Column is CDEC_ROUND. |
| 18 | `FS.GA.SECURITY.MASTER.TRUNCATION.CODE` | `FsGaSecurityMaster_TruncationCode` | TField |  | This field will be used to truncate The index factor automatically with defined decimal number Multifonds DB Column is CDEC_TRUNC. |
| 19 | `FS.GA.SECURITY.MASTER.INTEREST.COMPOUNDING.FREQUENCY` | `FsGaSecurityMaster_InterestCompoundingFrequency` | TField |  | This field defines the interest compounding frequency for the security . Multifonds DB Column is CFREQCOMP. |
| 20 | `FS.GA.SECURITY.MASTER.COUPON.FREQUENCY.CODE` | `FsGaSecurityMaster_CouponFrequencyCode` | TField |  | Frequency of payment of coupon/ commission Multifonds DB Column is CFREQCOUP. |
| 21 | `FS.GA.SECURITY.MASTER.GUARANTEE.CODE` | `FsGaSecurityMaster_GuaranteeCode` | TField |  | This field defines if the securities are idenfied as Guaranteed or Non Guaranteed Multifonds DB Column is CGARANTIE. |
| 22 | `FS.GA.SECURITY.MASTER.GTI.CODE` | `FsGaSecurityMaster_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 23 | `FS.GA.SECURITY.MASTER.RISK.CODE` | `FsGaSecurityMaster_RiskCode` | TField |  | This field is used to store the risk type for the Catastrophe bonds. Multifonds DB Column is CGTI_RISK. |
| 24 | `FS.GA.SECURITY.MASTER.CIMP.SOURCE` | `FsGaSecurityMaster_CimpSource` | TField |  | Cimp source Multifonds DB Column is CIMPSOURCE. |
| 25 | `FS.GA.SECURITY.MASTER.INSTRUMENT.CODE` | `FsGaSecurityMaster_InstrumentCode` | TField |  | This is can be defined to so that transaction can be processed by charging default fees based on different countries of trading. Multifonds DB Column is CINSTRUMENT. |
| 26 | `FS.GA.SECURITY.MASTER.INSTRUMENT.CODE.2` | `FsGaSecurityMaster_InstrumentCode2` | TField |  | This field is used for compliance purpose. This field is an alternative to Instrument code 1 (MIG21). It is country of incorporation whenever applicable. Multifonds DB Column is CINSTRUMENT2. |
| 27 | `FS.GA.SECURITY.MASTER.CLHIA.REPORTING` | `FsGaSecurityMaster_ClhiaReporting` | TField |  | CLHIA Reporting Multifonds DB Column is CLHIA_REPORTING. |
| 28 | `FS.GA.SECURITY.MASTER.CONVERSION.METHOD` | `FsGaSecurityMaster_ConversionMethod` | TField |  | Euro conversion method code Multifonds DB Column is CMETHOD. |
| 29 | `FS.GA.SECURITY.MASTER.CURRENCY.BEFORE.CONVERSION` | `FsGaSecurityMaster_CurrencyBeforeConversion` | TField |  | Currency before conversion Multifonds DB Column is CMON_BEFORE_EURO. |
| 30 | `FS.GA.SECURITY.MASTER.COUPON.PAYMENT.CURRENCY` | `FsGaSecurityMaster_CouponPaymentCurrency` | TField |  | This fields indicates the currency in which security incomes are recongnised Multifonds DB Column is CMON_COUPON. |
| 31 | `FS.GA.SECURITY.MASTER.REDEMPTION.CURRENCY` | `FsGaSecurityMaster_RedemptionCurrency` | TField |  | This fields indicates the currency in which security redemption takes places Multifonds DB Column is CMON_REDEM. |
| 32 | `FS.GA.SECURITY.MASTER.QUOTATION.CURRENCY` | `FsGaSecurityMaster_QuotationCurrency` | TField |  | The quotation currency of the security in general Multifonds DB Column is CMONCOTA. |
| 33 | `FS.GA.SECURITY.MASTER.LOOK.BACK.PERIOD.END` | `FsGaSecurityMaster_LookBackPeriodEnd` | TField |  | Number of publication cycles that have to be turned backwards from the given date to select the inflation value for the end-point required for index factor calculation (e.g. 003 = 3 months). Multifonds DB Column is CMONTH_END. |
| 34 | `FS.GA.SECURITY.MASTER.LOOK.BACK.START.PERIOD` | `FsGaSecurityMaster_LookBackStartPeriod` | TField |  | Number of publication cycles that have to be turned backwards from the given date to select the inflation value for the start-point required for index factor calculation (e.g. 002 = 2 months). Multifonds DB Column is CMONTH_START. |
| 35 | `FS.GA.SECURITY.MASTER.MATURITY.DATE.FOR.YIELD` | `FsGaSecurityMaster_MaturityDateForYield` | TField |  | Corresponds to default parameters to be used for calculation of specific yield report (Enter 1 for &apos;Final Maturity Date&apos;, 2 for &apos;Next Redemption&apos;). Multifonds DB Column is COD_DATE_EVAL. |
| 36 | `FS.GA.SECURITY.MASTER.REIMBURSEMENT` | `FsGaSecurityMaster_Reimbursement` | TField |  | Reimbursement Multifonds DB Column is COD_SOULTE. |
| 37 | `FS.GA.SECURITY.MASTER.ASSET.SUB.TYPE.CODE` | `FsGaSecurityMaster_AssetSubTypeCode` | TField |  | To enter Asset sub type for reporting. Multifonds DB Column is CODE_AST. |
| 38 | `FS.GA.SECURITY.MASTER.ASSET.TYPE.CODE` | `FsGaSecurityMaster_AssetTypeCode` | TField |  | To enter Asset type for reporting. Multifonds DB Column is CODE_AT. |
| 39 | `FS.GA.SECURITY.MASTER.PUBLICATION.CYCLE` | `FsGaSecurityMaster_PublicationCycle` | TField |  | This field defines the Frequency of the index factor publication Multifonds DB Column is CODE_CYCLE. |
| 40 | `FS.GA.SECURITY.MASTER.MATURITY.CODE` | `FsGaSecurityMaster_MaturityCode` | TField |  | Maturity code of the floating interest rate that needs to be applied for commission accrual on a lending/borrowing transaction Multifonds DB Column is CODE_MOIS. |
| 41 | `FS.GA.SECURITY.MASTER.REPORTING.CODE` | `FsGaSecurityMaster_ReportingCode` | TField |  | This is the reporting code tagged to an account. Multifonds DB Column is CODE_RAPPORT. |
| 42 | `FS.GA.SECURITY.MASTER.NEW.MINIMUM.DENOMINATION` | `FsGaSecurityMaster_NewMinimumDenomination` | TField |  | New minimum denomination Convertion Factor Multifonds DB Column is CONV_FACTOR. |
| 43 | `FS.GA.SECURITY.MASTER.PRICE.SOURCE` | `FsGaSecurityMaster_PriceSource` | TField |  | Provider code like Telekers, Reuters etc Multifonds DB Column is CORC. |
| 44 | `FS.GA.SECURITY.MASTER.LOCALE.TYPE` | `FsGaSecurityMaster_LocaleType` | TField |  | Local Type of granular information to query in Chart Charesteric screen Multifonds DB Column is COTLOCALE. |
| 45 | `FS.GA.SECURITY.MASTER.COUPON.GENERATION` | `FsGaSecurityMaster_CouponGeneration` | TField |  | Helps in definining how manage the coupon payment on holiday Multifonds DB Column is COUP_GEN. |
| 46 | `FS.GA.SECURITY.MASTER.ISSUE.PRICE` | `FsGaSecurityMaster_IssuePrice` | TField |  | Relects the Initial Price at which the bond is issued. Multifonds DB Column is COURS_EMIS. |
| 47 | `FS.GA.SECURITY.MASTER.MATURITY.REPAYMENT.PRICE` | `FsGaSecurityMaster_MaturityRepaymentPrice` | TField |  | The price at which an instruments if matured Multifonds DB Column is COURS_REMB. |
| 48 | `FS.GA.SECURITY.MASTER.MARKET.PRICE` | `FsGaSecurityMaster_MarketPrice` | TField |  | Market price for NAV Multifonds DB Column is COURSVAL. |
| 49 | `FS.GA.SECURITY.MASTER.ISSUE.COUNTRY` | `FsGaSecurityMaster_IssueCountry` | TField |  | Internal Identifier for a country, which is used in various places to include or exclude a specific country from a functionality Multifonds DB Column is CPAYSVAL. |
| 50 | `FS.GA.SECURITY.MASTER.QUOTATION.PLACE` | `FsGaSecurityMaster_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 51 | `FS.GA.SECURITY.MASTER.SUBMITTED` | `FsGaSecurityMaster_Submitted` | TField |  | Submission of records for processing or saving record. Multifonds DB Column is CSUBMIT. |
| 52 | `FS.GA.SECURITY.MASTER.TAX.CODE` | `FsGaSecurityMaster_TaxCode` | TField |  | Taxation code Multifonds DB Column is CTAX. |
| 53 | `FS.GA.SECURITY.MASTER.SECURITY.CTYPE` | `FsGaSecurityMaster_SecurityCtype` | TField |  | Reflects the security type/GTI-Genre de titre Multifonds DB Column is CTYPE_SEC. |
| 54 | `FS.GA.SECURITY.MASTER.DAY.COUNT.CONVENTION` | `FsGaSecurityMaster_DayCountConvention` | TField |  | Corresponds to default parameters to be used for calculation of specific hedged yield report. Multifonds DB Column is CUSANCE. |
| 55 | `FS.GA.SECURITY.MASTER.CUSIP` | `FsGaSecurityMaster_Cusip` | TField |  | Committee on Uniform Securities Identification Procedures. A CUSIP is a nine digit numeric or alphanumeric code that identifies security and facilitates clearing and settlement of trades Multifonds DB Column is CUSIP. |
| 56 | `FS.GA.SECURITY.MASTER.DATE.OF.INDIRECT.INVESTMENT` | `FsGaSecurityMaster_DateOfIndirectInvestment` | TField |  | Indirect Investment Date Multifonds DB Column is D_IND_INV_2. |
| 57 | `FS.GA.SECURITY.MASTER.INDIRECT.INVESTMENT` | `FsGaSecurityMaster_IndirectInvestment` | TField |  | Indirect Investment Multifonds DB Column is D_INDIRECT_INVEST. |
| 58 | `FS.GA.SECURITY.MASTER.IRREGULAR.PERIOD.BEGIN.DATE` | `FsGaSecurityMaster_IrregularPeriodBeginDate` | TField |  | Reflects the Irregular Interest period begin date Multifonds DB Column is DAT_DEB_PER_IRR. |
| 59 | `FS.GA.SECURITY.MASTER.IRREGULAR.PERIOD.BEGIN.DATE.2` | `FsGaSecurityMaster_IrregularPeriodBeginDate2` | TField |  | Reflects the Irregular next Interest period begin date Multifonds DB Column is DAT_DEB_PER_IRR_1. |
| 60 | `FS.GA.SECURITY.MASTER.IRREGULAR.PERIOD.END.DATE` | `FsGaSecurityMaster_IrregularPeriodEndDate` | TField |  | Reflects the Irregular next Interest period END date Multifonds DB Column is DAT_FIN_PER_IRR. |
| 61 | `FS.GA.SECURITY.MASTER.IRREGULAR.PERIOD.END.DATE.2` | `FsGaSecurityMaster_IrregularPeriodEndDate2` | TField |  | Reflects the Irregular next Interest period End date Multifonds DB Column is DAT_FIN_PER_IRR_1. |
| 62 | `FS.GA.SECURITY.MASTER.CONVERTIBILITY.DATE` | `FsGaSecurityMaster_ConvertibilityDate` | TField |  | Convertibility date: Related to step up bonds, convertibility date has to be defined with the switch date of the interest from zero/low coupon to the higher coupon. Multifonds DB Column is DATCONVERT. |
| 63 | `FS.GA.SECURITY.MASTER.FIRST.COUPON.DATE` | `FsGaSecurityMaster_FirstCouponDate` | TField |  | First Coupon Date Multifonds DB Column is DATCOUPON. |
| 64 | `FS.GA.SECURITY.MASTER.FATCA.EFFECTIVE.DATE` | `FsGaSecurityMaster_FatcaEffectiveDate` | TField |  | Effective date of FACTA rule defintion in the fund Multifonds DB Column is DATE_EFFECTIVE_FATCA. |
| 65 | `FS.GA.SECURITY.MASTER.MATURITY.DATE` | `FsGaSecurityMaster_MaturityDate` | TField |  | Maturity Date of an instrument, like for Bonds Multifonds DB Column is DATECH. |
| 66 | `FS.GA.SECURITY.MASTER.DATE.OF.PRICE` | `FsGaSecurityMaster_DateOfPrice` | TField |  | Value date of the securities prices Multifonds DB Column is DATECOURS. |
| 67 | `FS.GA.SECURITY.MASTER.ISSUE.DATE` | `FsGaSecurityMaster_IssueDate` | TField |  | Issue Date of an instrument, like for Bonds Multifonds DB Column is DATEMISS. |
| 68 | `FS.GA.SECURITY.MASTER.REDEMPTION.DATE` | `FsGaSecurityMaster_RedemptionDate` | TField |  | Redemption,repayment Date Multifonds DB Column is DATREMANT. |
| 69 | `FS.GA.SECURITY.MASTER.DATE` | `FsGaSecurityMaster_Date` | TField |  | Date Multifonds DB Column is DCONV. |
| 70 | `FS.GA.SECURITY.MASTER.TBC.SUSPENSION.START` | `FsGaSecurityMaster_TbcSuspensionStart` | TField |  | Tax Book Cost Suspension start Date Multifonds DB Column is DDEBUT_TBC. |
| 71 | `FS.GA.SECURITY.MASTER.INTEREST.DEFAULT.END.DATE` | `FsGaSecurityMaster_InterestDefaultEndDate` | TField |  | Interest Default End Date:The interest accrual will begin on the fund from this date forward Multifonds DB Column is DDEFAULT_END. |
| 72 | `FS.GA.SECURITY.MASTER.INTEREST.DEFAULT.START.DATE` | `FsGaSecurityMaster_InterestDefaultStartDate` | TField |  | Interest Default Start Date:The interest accrual will stop on the fund from this date forward Multifonds DB Column is DDEFAULT_START. |
| 73 | `FS.GA.SECURITY.MASTER.DELAY.DAYS` | `FsGaSecurityMaster_DelayDays` | TField |  | Delay days to be applied on coupon/ paydown transactions to trigger payment Multifonds DB Column is DELAY_DAYS. |
| 74 | `FS.GA.SECURITY.MASTER.DE.MINIMIS.VALUE` | `FsGaSecurityMaster_DeMinimisValue` | TField |  | Corresponds to a fix minimum amount which is used for defining whether a security is OID. Multifonds DB Column is DEMINI. |
| 75 | `FS.GA.SECURITY.MASTER.TBC.SUSPENSION.END` | `FsGaSecurityMaster_TbcSuspensionEnd` | TField |  | Tax Book Cost Suspension end Date Multifonds DB Column is DFIN_TBC. |
| 76 | `FS.GA.SECURITY.MASTER.DIRECT.YIELD` | `FsGaSecurityMaster_DirectYield` | TField |  | Measures the coupon of an interest-bearing instrument as a percentage of the clean price of the interest-bearing instrument Multifonds DB Column is DIRECT_YIELD. |
| 77 | `FS.GA.SECURITY.MASTER.DIVIDEND.FREQUENCY` | `FsGaSecurityMaster_DividendFrequency` | TField |  | Dividend Frequency of a security Multifonds DB Column is DIV_FREQ. |
| 78 | `FS.GA.SECURITY.MASTER.DIVIDEND.RATE` | `FsGaSecurityMaster_DividendRate` | TField |  | Dividend rate of security Multifonds DB Column is DIV_RATE. |
| 79 | `FS.GA.SECURITY.MASTER.INTEREST.START.DATE` | `FsGaSecurityMaster_InterestStartDate` | TField |  | The Date from which interest accruals begin on securities, generally for bonds Multifonds DB Column is DJOUISSANCE. |
| 80 | `FS.GA.SECURITY.MASTER.LAST.DIVIDEND.DECLARATION.DATE` | `FsGaSecurityMaster_LastDividendDeclarationDate` | TField |  | Last Dividend Declaration Date of the security Multifonds DB Column is DLAST_DIV. |
| 81 | `FS.GA.SECURITY.MASTER.TRADE.CUTOFF.TIME` | `FsGaSecurityMaster_TradeCutoffTime` | TField |  | A field to define the default trade deadline for the security. Multifonds DB Column is DOPER_CUTOFF. |
| 82 | `FS.GA.SECURITY.MASTER.CONVERSION.DATE` | `FsGaSecurityMaster_ConversionDate` | TField |  | Conversion allowed since Multifonds DB Column is DSTARTCONV. |
| 83 | `FS.GA.SECURITY.MASTER.DURATION` | `FsGaSecurityMaster_Duration` | TField |  | Average period (in years) of the time of the binding of cash Multifonds DB Column is DURATION. |
| 84 | `FS.GA.SECURITY.MASTER.EX.DAYS` | `FsGaSecurityMaster_ExDays` | TField |  | In Thai Bond markets, when bonds are issued the ex-coupon date is known in advance and is usually &apos;x&apos; number of days prior to the actual payment date. Multifonds DB Column is EX_DAYS. |
| 85 | `FS.GA.SECURITY.MASTER.EXPIRATION.DATE` | `FsGaSecurityMaster_ExpirationDate` | TField |  | Epiration date of the letter of credit which is backing the security. Multifonds DB Column is EXPIRATION_DATE. |
| 86 | `FS.GA.SECURITY.MASTER.FCYIELD` | `FsGaSecurityMaster_Fcyield` | TField |  | Yield Multifonds DB Column is FCYIELD. |
| 87 | `FS.GA.SECURITY.MASTER.FEES.CODE` | `FsGaSecurityMaster_FeesCode` | TField |  | This field hepls the user to take into account or remove from the fees based amount the sum of specific fees codes setup of the security master. Multifonds DB Column is FFEES. |
| 88 | `FS.GA.SECURITY.MASTER.FIX.PERCENTAGE.HURDLE` | `FsGaSecurityMaster_FixPercentageHurdle` | TField |  | Related to performance fees, fixed hurdle value will be taken for the adjustment HWM calculation if hurdle type is fixed hurdle rate Multifonds DB Column is FIX_HURDLE. |
| 89 | `FS.GA.SECURITY.MASTER.FIXED.RETURN.BENCHMARK` | `FsGaSecurityMaster_FixedReturnBenchmark` | TField |  | Corresponds to Fixed Return Securities for the adjustment of the Daily Return due to the impact of Non-Business day Multifonds DB Column is FIXED_RETURN_BM. |
| 90 | `FS.GA.SECURITY.MASTER.SWAP` | `FsGaSecurityMaster_Swap` | TField |  | Swapped security flag Multifonds DB Column is FLAG_SWAP. |
| 91 | `FS.GA.SECURITY.MASTER.TAX.EXEMPT` | `FsGaSecurityMaster_TaxExempt` | TField |  | If checked, the security will be excluded from the CGT reports even if the GTI has been linked to the valuation model for the CGT reporting. Multifonds DB Column is FLG_AU_TAX_EXMT. |
| 92 | `FS.GA.SECURITY.MASTER.SECURITY.COUPON.DATE` | `FsGaSecurityMaster_SecurityCouponDate` | TField |  | Security coupon date Multifonds DB Column is FLG_COUPON. |
| 93 | `FS.GA.SECURITY.MASTER.DEFAULT.STATUS` | `FsGaSecurityMaster_DefaultStatus` | TField |  | Indicate is the security is in default status Multifonds DB Column is FLG_DEFAULT_INT. |
| 94 | `FS.GA.SECURITY.MASTER.TRADE.DATE.IDENTIFIER` | `FsGaSecurityMaster_TradeDateIdentifier` | TField |  | if the trade calculation process is run after the trade cut off time, the trade will be calculated with a trade date of T+1 rather than taking no action Multifonds DB Column is FLG_DOPER. |
| 95 | `FS.GA.SECURITY.MASTER.SECURITY.EX.COUPON.DATE` | `FsGaSecurityMaster_SecurityExCouponDate` | TField |  | allows review and update of the ex-coupon dates for the interest receivable. Multifonds DB Column is FLG_EXCOUPON. |
| 96 | `FS.GA.SECURITY.MASTER.FATCA.GRANDFATHER` | `FsGaSecurityMaster_FatcaGrandfather` | TField |  | Foreign Account Tax Compliance Act Flag Multifonds DB Column is FLG_FATCA_GF. |
| 97 | `FS.GA.SECURITY.MASTER.FATCA.LIABILITY.STATUS` | `FsGaSecurityMaster_FatcaLiabilityStatus` | TField |  | Foreign Account Tax Compliance Act liability Status Flag Multifonds DB Column is FLG_FATCA_VAL_LIABILITY. |
| 98 | `FS.GA.SECURITY.MASTER.FIXED.RATE.RISK` | `FsGaSecurityMaster_FixedRateRisk` | TField |  | If set, securities will appear on the French Legal reports: &apos;Rate risk report&apos; and &apos;Ventilation by interest rate type report&apos;. Multifonds DB Column is FLG_FR_RISK. |
| 99 | `FS.GA.SECURITY.MASTER.USE.TRADE.DATE` | `FsGaSecurityMaster_UseTradeDate` | TField |  | If set, accrued interest on securities purchases and sales will be calculated as of the trade date of the respective transaction. If not set, will be calculated as of the value date. Multifonds DB Column is FLG_INT_TRADE. |
| 100 | `FS.GA.SECURITY.MASTER.INTERIM.PROFIT.IDENTIFIER` | `FsGaSecurityMaster_InterimProfitIdentifier` | TField |  | Flag for IP(Interim Profit) Multifonds DB Column is FLG_IP. |
| 101 | `FS.GA.SECURITY.MASTER.INTERIM.PROFIT.TRANSPARENCY` | `FsGaSecurityMaster_InterimProfitTransparency` | TField |  | Interim profit Transparency Multifonds DB Column is FLG_IP_TRANSP. |
| 102 | `FS.GA.SECURITY.MASTER.KEST` | `FsGaSecurityMaster_Kest` | TField |  | If Set, Austrian KEST will be calculated for the underlying share class Multifonds DB Column is FLG_KEST. |
| 103 | `FS.GA.SECURITY.MASTER.LETTER.OF.CREDIT` | `FsGaSecurityMaster_LetterOfCredit` | TField |  | Indicates the security is backed by a Letter of Credit Multifonds DB Column is FLG_LOC. |
| 104 | `FS.GA.SECURITY.MASTER.OTHER.RATE.RISK` | `FsGaSecurityMaster_OtherRateRisk` | TField |  | to define if securities will appear on the French Legal reports: &apos;Rate risk report&apos; and &apos;Ventilation by interest rate type report&apos; Multifonds DB Column is FLG_RATE_OTH. |
| 105 | `FS.GA.SECURITY.MASTER.RISK.ACT` | `FsGaSecurityMaster_RiskAct` | TField |  | to define if securities will appear on the French Legal report &apos;Share risk exposition&apos;. Multifonds DB Column is FLG_RISK_ACT. |
| 106 | `FS.GA.SECURITY.MASTER.FLOATING.RATE.RISK` | `FsGaSecurityMaster_FloatingRateRisk` | TField |  | to define if securities will appear on the French Legal reports: &apos;Rate risk report&apos; and &apos;Ventilation by interest rate type report&apos;. Multifonds DB Column is FLG_RISK_FLT. |
| 107 | `FS.GA.SECURITY.MASTER.SPREAD.APPLICABLE` | `FsGaSecurityMaster_SpreadApplicable` | TField |  | The spread applicable to a security Multifonds DB Column is FLG_SPR. |
| 108 | `FS.GA.SECURITY.MASTER.SECURITIES.VOTING.RIGHT` | `FsGaSecurityMaster_SecuritiesVotingRight` | TField |  | Select &quot;Y&quot; or &quot;N&quot; (used for information in an IAS fund structure). It is only used for the Infocenter export, but is not currently used within Multifonds. Multifonds DB Column is FLG_VOTING. |
| 109 | `FS.GA.SECURITY.MASTER.VARIABLE.RATE.RISK` | `FsGaSecurityMaster_VariableRateRisk` | TField |  | to define if securities will appear on the French Legal reports: &apos;Rate risk report&apos; and &apos;Ventilation by interest rate type report&apos;. Multifonds DB Column is FLG_VR_RISK. |
| 110 | `FS.GA.SECURITY.MASTER.YIELD.CURVE.PRICING` | `FsGaSecurityMaster_YieldCurvePricing` | TField |  | define Security for Yield curve pricing Multifonds DB Column is FLG_YLD_CURVE_PRICING. |
| 111 | `FS.GA.SECURITY.MASTER.CONTRACT.SIZE` | `FsGaSecurityMaster_ContractSize` | TField |  | The contract size (if not zero) is used as a multiplier. Multifonds DB Column is FMULTI. |
| 112 | `FS.GA.SECURITY.MASTER.FUND.OF.FUND.DECIMAL.CODE` | `FsGaSecurityMaster_FundOfFundDecimalCode` | TField |  | This involves Fund of Fund auto-pricing. Multifonds DB Column is FOF_DEC. |
| 113 | `FS.GA.SECURITY.MASTER.GIVE.FOR` | `FsGaSecurityMaster_GiveFor` | TField |  | Quantity to give for Multifonds DB Column is FOR_OLD. |
| 114 | `FS.GA.SECURITY.MASTER.GRAND.FATHER.OR.TIS.REPORTING` | `FsGaSecurityMaster_GrandFatherOrTisReporting` | TField |  | Grand Father or Non Grand Father i.e TIS Reporting applicable Multifonds DB Column is GDF_TISR. |
| 115 | `FS.GA.SECURITY.MASTER.NEW.SECURITY.UNITS` | `FsGaSecurityMaster_NewSecurityUnits` | TField |  | New security proportion Multifonds DB Column is GIVE_NEW. |
| 116 | `FS.GA.SECURITY.MASTER.USER.DEFINABLE.FIELDS.GROUP` | `FsGaSecurityMaster_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 117 | `FS.GA.SECURITY.MASTER.HOLIDAY.COMPOUNDING` | `FsGaSecurityMaster_HolidayCompounding` | TField |  | Management of Compounding on Holidays Multifonds DB Column is HOLIDAY_COMP. |
| 118 | `FS.GA.SECURITY.MASTER.HURDLE.SCOPE` | `FsGaSecurityMaster_HurdleScope` | TField |  | Hurdle Scope related to performance fees Multifonds DB Column is HURDLE_SCOPE. |
| 119 | `FS.GA.SECURITY.MASTER.HURDLE.TYPE` | `FsGaSecurityMaster_HurdleType` | TField |  | Related to performance fees, for example as follows: 1- Fixed Hurdle Rate: 2- Variable Hurdle Rate: Multifonds DB Column is HURDLE_TYPE. |
| 120 | `FS.GA.SECURITY.MASTER.HIGH.WATER.MARK` | `FsGaSecurityMaster_HighWaterMark` | TField |  | A high-water mark is the highest peak in value that investments fund or account has reached. Multifonds DB Column is HWM. |
| 121 | `FS.GA.SECURITY.MASTER.HIGH.WATER.MARK.DATE` | `FsGaSecurityMaster_HighWaterMarkDate` | TField |  | Related to performance fees, the High Water Mark date is automatically updated with the NAV accounting process. Multifonds DB Column is HWM_DATE. |
| 122 | `FS.GA.SECURITY.MASTER.IDENTIFIER.CODE.TELEKURS` | `FsGaSecurityMaster_IdentifierCodeTelekurs` | TField |  | Identifiier Code Telekurs Multifonds DB Column is ID_TELK. |
| 123 | `FS.GA.SECURITY.MASTER.YIELD.ADJUSTMENT` | `FsGaSecurityMaster_YieldAdjustment` | TField |  | Yield Adjustment Multifonds DB Column is IND_CODE_YLD_ADJ. |
| 124 | `FS.GA.SECURITY.MASTER.INDEX.TOLERANCE.DYNAMIC.ADJUST` | `FsGaSecurityMaster_IndexToleranceDynamicAdjust` | TField |  | To apply Factor on Base Tolerance defined at Tolerance Group level or Market Index Tolerance Multifonds DB Column is IND_TOL_DYN_ADJ. |
| 125 | `FS.GA.SECURITY.MASTER.INDEX.SINCE.LAST.RESET` | `FsGaSecurityMaster_IndexSinceLastReset` | TField |  | Related to performance fees, reflects the index since last reset. Multifonds DB Column is INDEX_LAST_RESET. |
| 126 | `FS.GA.SECURITY.MASTER.INTEREST.ADJUSTMENT.DAYS` | `FsGaSecurityMaster_InterestAdjustmentDays` | TField |  | To enter number of interest adjustment days as additional fixed days to settle for dirty bond to calculate clean price. Multifonds DB Column is INT_ADJ_DAYS. |
| 127 | `FS.GA.SECURITY.MASTER.LOOK.THROUGH.RATIO` | `FsGaSecurityMaster_LookThroughRatio` | TField |  | Percentage of investment/portfolio of the fund of fund which is in scope for the TIS calculation Multifonds DB Column is LOOK_THR_RATIO. |
| 128 | `FS.GA.SECURITY.MASTER.DISCOUNT.MARGIN` | `FsGaSecurityMaster_DiscountMargin` | TField |  | Discount margin or spread on security interest rates. Specific to Thai securities Multifonds DB Column is MARGIN_DM. |
| 129 | `FS.GA.SECURITY.MASTER.QUOTED.MARGIN` | `FsGaSecurityMaster_QuotedMargin` | TField |  | Quoted margin or spread on security interest rates. Specific to Thai securities Multifonds DB Column is MARGIN_QM. |
| 130 | `FS.GA.SECURITY.MASTER.MARK.UP.BASIS.POINT` | `FsGaSecurityMaster_MarkUpBasisPoint` | TField |  | The markup will be added to the variable hurdle rate to compute the hurdle rate adjusted HWM. Multifonds DB Column is MARKUP_BPS. |
| 131 | `FS.GA.SECURITY.MASTER.MAXIMUM.AMOUNT` | `FsGaSecurityMaster_MaximumAmount` | TField |  | define a maximum amount for the transaction Multifonds DB Column is MAX_FPRT. |
| 132 | `FS.GA.SECURITY.MASTER.MINIMUM.AMOUNT` | `FsGaSecurityMaster_MinimumAmount` | TField |  | define a minimum amount for the transaction Multifonds DB Column is MIN_FPRT. |
| 133 | `FS.GA.SECURITY.MASTER.MINIMUM.INCREMENT` | `FsGaSecurityMaster_MinimumIncrement` | TField |  | Define prevent users to process transactions into Multifonds with an incorrect incremental value Multifonds DB Column is MIN_INCREMENT. |
| 134 | `FS.GA.SECURITY.MASTER.MINIMUM.TRADE.AMOUNT` | `FsGaSecurityMaster_MinimumTradeAmount` | TField |  | to specify the security default minimum trade amount. Multifonds DB Column is MIN_MNTNET. |
| 135 | `FS.GA.SECURITY.MASTER.MINIMUM.QUANTITY` | `FsGaSecurityMaster_MinimumQuantity` | TField |  | to define the minimum quantity that must be purchased or sold of the security Multifonds DB Column is MIN_QUANTITY. |
| 136 | `FS.GA.SECURITY.MASTER.NAV.CALCULATION` | `FsGaSecurityMaster_NavCalculation` | TField |  | Tax Calculation During Nav Multifonds DB Column is NAV_INT. |
| 137 | `FS.GA.SECURITY.MASTER.NAV.SINCE.LAST.RESET` | `FsGaSecurityMaster_NavSinceLastReset` | TField |  | The out-performance at Year End is the variation between the fund performance including the dividend payment and the benchmark performance including the Hurdle rate since last reset date. Multifonds DB Column is NAV_LAST_RESET. |
| 138 | `FS.GA.SECURITY.MASTER.CURRENT.MINIMUM.DENOMINATION` | `FsGaSecurityMaster_CurrentMinimumDenomination` | TField |  | Minimal contract size for new securities Multifonds DB Column is NB_LOT. |
| 139 | `FS.GA.SECURITY.MASTER.NUMBER.OF.DAYS` | `FsGaSecurityMaster_NumberOfDays` | TField |  | Compare variation D / Situation Date&apos; in the field &quot;Type&quot;. Then, it has to be completed with a number of days as of which the error message &quot;the difference is greater than X day&quot; will be prompted. Multifonds DB Column is NBJ_COURS. |
| 140 | `FS.GA.SECURITY.MASTER.RISK.COUNTERPARTY` | `FsGaSecurityMaster_RiskCounterparty` | TField |  | Risk correspondent number Multifonds DB Column is NCORR_RISQUE. |
| 141 | `FS.GA.SECURITY.MASTER.CORRESPONDENT.CONV` | `FsGaSecurityMaster_CorrespondentConv` | TField |  | Correspondant Multifonds DB Column is NCORRESP_CONV. |
| 142 | `FS.GA.SECURITY.MASTER.COUNTERPARTY.CORRESPONDENT` | `FsGaSecurityMaster_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 143 | `FS.GA.SECURITY.MASTER.MANAGEMENT.COMPANY` | `FsGaSecurityMaster_ManagementCompany` | TField |  | To define management company Multifonds DB Column is NCSP. |
| 144 | `FS.GA.SECURITY.MASTER.COUNTER.PARTY.CODE` | `FsGaSecurityMaster_CounterPartyCode` | TField |  | Guarantor,Issuer Multifonds DB Column is NISSUER_GUARANTEED. |
| 145 | `FS.GA.SECURITY.MASTER.ISSUER` | `FsGaSecurityMaster_Issuer` | TField |  | To enter Issuer of the security Multifonds DB Column is NISSUING. |
| 146 | `FS.GA.SECURITY.MASTER.NOMINAL.VALUE` | `FsGaSecurityMaster_NominalValue` | TField |  | Nominal of the Instrument Multifonds DB Column is NOMINAL. |
| 147 | `FS.GA.SECURITY.MASTER.NON.QSI` | `FsGaSecurityMaster_NonQsi` | TField |  | to define any Non Qualified Stated Interest income for the security Multifonds DB Column is NON_QSI. |
| 148 | `FS.GA.SECURITY.MASTER.NEW.SECURITY.ID` | `FsGaSecurityMaster_NewSecurityId` | TField |  | New security internal number Multifonds DB Column is NOVAL_NEW. |
| 149 | `FS.GA.SECURITY.MASTER.FUND.MANAGER` | `FsGaSecurityMaster_FundManager` | TField |  | Fund manager code Multifonds DB Column is NPTF_NSPORTFOLIO. |
| 150 | `FS.GA.SECURITY.MASTER.DEPOSITORY` | `FsGaSecurityMaster_Depository` | TField |  | Third party depository/correcpondence number Multifonds DB Column is NRACINE. |
| 151 | `FS.GA.SECURITY.MASTER.ACCOUNT` | `FsGaSecurityMaster_Account` | TField |  | Account Number Multifonds DB Column is NRUBR_CONV. |
| 152 | `FS.GA.SECURITY.MASTER.ACCOUNT.CONVERSION` | `FsGaSecurityMaster_AccountConversion` | TField |  | Account number for EURO conversion at security level Multifonds DB Column is NSUFF_CONV. |
| 153 | `FS.GA.SECURITY.MASTER.UNDERLYING.SECURITY` | `FsGaSecurityMaster_UnderlyingSecurity` | TField |  | Underlying internal security number Multifonds DB Column is NUNDER. |
| 154 | `FS.GA.SECURITY.MASTER.UNDERLYING.SECURITY.1` | `FsGaSecurityMaster_UnderlyingSecurity1` | TField |  | Underlying internal security number 1 Multifonds DB Column is NUNDER_1. |
| 155 | `FS.GA.SECURITY.MASTER.OFFICIAL.STOCK.EXCHANGE` | `FsGaSecurityMaster_OfficialStockExchange` | TField | Yes | It has the same characteristics as the field &quot;quotation place&quot;, but it is not a mandatory field. Multifonds DB Column is OFF_STOCK_EXCHGE. |
| 156 | `FS.GA.SECURITY.MASTER.ORIGINAL.ISSUE.DISCOUNT` | `FsGaSecurityMaster_OriginalIssueDiscount` | TField |  | Original Issue Discount Calculated at \Security Master Level Multifonds DB Column is OID. |
| 157 | `FS.GA.SECURITY.MASTER.ORIGINAL.ISSUE.DISCOUNT.YTM.1` | `FsGaSecurityMaster_OriginalIssueDiscountYtm1` | TField |  | Original Issue Discount Yield to Maturity Annaul Multifonds DB Column is OID_YTM1. |
| 158 | `FS.GA.SECURITY.MASTER.ORIGINAL.ISSUE.DISCOUNT.YTM.2` | `FsGaSecurityMaster_OriginalIssueDiscountYtm2` | TField |  | Original Issue Discount Yield to Maturity Semi Annaul Multifonds DB Column is OID_YTM2. |
| 159 | `FS.GA.SECURITY.MASTER.OUTAGE.NUMBER.OF.DAYS` | `FsGaSecurityMaster_OutageNumberOfDays` | TField |  | Related to the benchmark and peer group analysis to calculate the outage percentage for each security based on the No. of exception breaks during last fixed number of days for outage calculation Multifonds DB Column is OUTAGE_NBDAYS. |
| 160 | `FS.GA.SECURITY.MASTER.PA.ASSET.CODE` | `FsGaSecurityMaster_PaAssetCode` | TField |  | Pa Asset Code Multifonds DB Column is PA_ASSET_CODE. |
| 161 | `FS.GA.SECURITY.MASTER.PA.ASSET.SUB.CODE` | `FsGaSecurityMaster_PaAssetSubCode` | TField |  | Pa Asset Sub Code Multifonds DB Column is PA_ASSET_SUB_CODE. |
| 162 | `FS.GA.SECURITY.MASTER.CAPPED.INTEREST.RATE` | `FsGaSecurityMaster_CappedInterestRate` | TField |  | The upper capped limit on the interest rate applicable to securities, generally bonds Multifonds DB Column is PC_CAP. |
| 163 | `FS.GA.SECURITY.MASTER.FLOOR.INTEREST.RATE` | `FsGaSecurityMaster_FloorInterestRate` | TField |  | The Floor rate on the interest rate applicable to securities, generally bonds Multifonds DB Column is PC_FLOOR. |
| 164 | `FS.GA.SECURITY.MASTER.EXCHANGE.RATE.PERCENTAGE` | `FsGaSecurityMaster_ExchangeRatePercentage` | TField |  | Enter a maximum tolerance percentage for exchange rate deviations. The percentage indicated here will be used in the control report Multifonds DB Column is PCT_COURS. |
| 165 | `FS.GA.SECURITY.MASTER.FATCA.LIABILITY.PERCENT` | `FsGaSecurityMaster_FatcaLiabilityPercent` | TField |  | Foreign Account Tax Compliance Act liability Percentage Multifonds DB Column is PCT_FATCA_VAL_LIABILITY. |
| 166 | `FS.GA.SECURITY.MASTER.PERCENTAGE.OF.FEES` | `FsGaSecurityMaster_PercentageOfFees` | TField |  | The percentage of fee calculated at target fund level is set in the field &quot;Percentage of fees Multifonds DB Column is PCT_FPRT. |
| 167 | `FS.GA.SECURITY.MASTER.RECOVERABLE.TAX.1.PERCENTAGE` | `FsGaSecurityMaster_RecoverableTax1Percentage` | TField |  | Recoverable tax percentage at dividend announcement , type 1 Multifonds DB Column is PCT_RC. |
| 168 | `FS.GA.SECURITY.MASTER.PAYABLE.TAX.1.PERCENTAGE` | `FsGaSecurityMaster_PayableTax1Percentage` | TField |  | Rate of Tax payable on the income , type of tax 1 Multifonds DB Column is PCT_TAX_1. |
| 169 | `FS.GA.SECURITY.MASTER.PAYABLE.TAX.2.PERCENTAGE` | `FsGaSecurityMaster_PayableTax2Percentage` | TField |  | Rate of Tax payable on the income , type of tax 2 Multifonds DB Column is PCT_TAX_2. |
| 170 | `FS.GA.SECURITY.MASTER.UNRECOVERABLE.TAX.1.PERCENTAGE` | `FsGaSecurityMaster_UnrecoverableTax1Percentage` | TField |  | Unrecoverable tax percentage at dividend announcement , type 1 Multifonds DB Column is PCT_UN. |
| 171 | `FS.GA.SECURITY.MASTER.PIK.FACTOR` | `FsGaSecurityMaster_PikFactor` | TField |  | Factor for PIK security Multifonds DB Column is PIK_FACTOR. |
| 172 | `FS.GA.SECURITY.MASTER.RECOVERABLE.TAX.PERCENT.2` | `FsGaSecurityMaster_RecoverableTaxPercent2` | TField |  | Recoverable tax percentage on Income , type 2 Multifonds DB Column is PRECTAX_2. |
| 173 | `FS.GA.SECURITY.MASTER.PRICING.DAYS` | `FsGaSecurityMaster_PricingDays` | TField |  | Number of days look back for pricing the security incase of missing price. Multifonds DB Column is PRICING_DAYS. |
| 174 | `FS.GA.SECURITY.MASTER.UNRECOVERABLE.TAX.PERCENT.2` | `FsGaSecurityMaster_UnrecoverableTaxPercent2` | TField |  | Unrecoverable tax percentage on Income , type 2 Multifonds DB Column is PUNRECTAX_2. |
| 175 | `FS.GA.SECURITY.MASTER.REFERENCE.CONSUMER.PRICE.INDEX` | `FsGaSecurityMaster_ReferenceConsumerPriceIndex` | TField |  | Define the reference Consumer Price Index as at the issue date of the Inflation Protected bond. Multifonds DB Column is REF_CPI. |
| 176 | `FS.GA.SECURITY.MASTER.REPORT.ASSET.SUB.TYPE` | `FsGaSecurityMaster_ReportAssetSubType` | TField |  | Duplicate to Report Assest type (CODE_AST) Multifonds DB Column is REPORT_ASSET_SUB_TYPE. |
| 177 | `FS.GA.SECURITY.MASTER.REPORT.ASSET.TYPE` | `FsGaSecurityMaster_ReportAssetType` | TField |  | Duplicate to Report Assest type (CODE_AT) Multifonds DB Column is REPORT_ASSET_TYPE. |
| 178 | `FS.GA.SECURITY.MASTER.RESET.DATE` | `FsGaSecurityMaster_ResetDate` | TField |  | Related to performance fees, the reset date is the starting date for the calculation of the out-performance at year-end. Multifonds DB Column is RESET_DATE. |
| 179 | `FS.GA.SECURITY.MASTER.SECTOR` | `FsGaSecurityMaster_Sector` | TField |  | Industry sector linked to a correspondent Multifonds DB Column is SCO. |
| 180 | `FS.GA.SECURITY.MASTER.ISIN.SEQUENCE` | `FsGaSecurityMaster_IsinSequence` | TField |  | ISIN sequence of the security. Multifonds DB Column is SEQISIN. |
| 181 | `FS.GA.SECURITY.MASTER.SIMPLE.YIELD` | `FsGaSecurityMaster_SimpleYield` | TField |  | Also known as the Japanese yield. In addition to the direct yield, takes also into consideration the effect of a capital gain or loss up to the maturity. Multifonds DB Column is SIMPLE_YIELD. |
| 182 | `FS.GA.SECURITY.MASTER.SIMPLE.YIELD.1` | `FsGaSecurityMaster_SimpleYield1` | TField |  | Simple yield method 1 Multifonds DB Column is SIMPLE_YIELD1. |
| 183 | `FS.GA.SECURITY.MASTER.ESD.ASSET.TEST.SOURCE` | `FsGaSecurityMaster_EsdAssetTestSource` | TField |  | Related to the ESD Asset Test. Multifonds DB Column is SOURCE. |
| 184 | `FS.GA.SECURITY.MASTER.EFFECTIVE.DATE.OF.SPREAD` | `FsGaSecurityMaster_EffectiveDateOfSpread` | TField |  | The effective date from which the spread is appiicable Multifonds DB Column is SPRDDATE. |
| 185 | `FS.GA.SECURITY.MASTER.SPREAD.PERCENTAGE` | `FsGaSecurityMaster_SpreadPercentage` | TField |  | The Spread percentage on floating rate securities Multifonds DB Column is SPRDRATE. |
| 186 | `FS.GA.SECURITY.MASTER.STATE.CODE` | `FsGaSecurityMaster_StateCode` | TField |  | Field is used to store the region type for Catastrophe bonds Multifonds DB Column is STATE_CODE. |
| 187 | `FS.GA.SECURITY.MASTER.EXCHANGE.RATE.COUPON` | `FsGaSecurityMaster_ExchangeRateCoupon` | TField |  | Forieghn Exchange rate Multifonds DB Column is TCHG_COUPON. |
| 188 | `FS.GA.SECURITY.MASTER.EVALUATION.TYPE` | `FsGaSecurityMaster_EvaluationType` | TField |  | Valuation method for specific security types such as zero bonds, polish T-bills, Mortgaged Backed Securities. Multifonds DB Column is TEVALUATION. |
| 189 | `FS.GA.SECURITY.MASTER.FUND.CLASS` | `FsGaSecurityMaster_FundClass` | TField |  | Fund Class For German Tax Multifonds DB Column is TG_FUND_CLASS. |
| 190 | `FS.GA.SECURITY.MASTER.THEORETICAL.DATE` | `FsGaSecurityMaster_TheoreticalDate` | TField |  | Theoretical date Multifonds DB Column is THEORETICAL_DATE. |
| 191 | `FS.GA.SECURITY.MASTER.TIS.AVAILABILITY` | `FsGaSecurityMaster_TisAvailability` | TField |  | used to control that all positions that have these values set, require the injection of the TIS Multifonds DB Column is TIS_AVAIL. |
| 192 | `FS.GA.SECURITY.MASTER.INCOME.TYPE` | `FsGaSecurityMaster_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 193 | `FS.GA.SECURITY.MASTER.UNDERLYING.RECEIVABLE` | `FsGaSecurityMaster_UnderlyingReceivable` | TField |  | Underlying Recievable Multifonds DB Column is TUNDER. |
| 194 | `FS.GA.SECURITY.MASTER.UNDERLYING.PAYABLE` | `FsGaSecurityMaster_UnderlyingPayable` | TField |  | Underlying Payable Multifonds DB Column is TUNDER_1. |
| 195 | `FS.GA.SECURITY.MASTER.INTEREST.RATE` | `FsGaSecurityMaster_InterestRate` | TField |  | Interest rate applicable on the interest bearing instrument in the transaction Multifonds DB Column is TXINT. |
| 196 | `FS.GA.SECURITY.MASTER.PRICE.INDICATOR` | `FsGaSecurityMaster_PriceIndicator` | TField |  | Price indicator to denote if the price of the bond is dirty or clean Multifonds DB Column is TYP_INT_COURS. |
| 197 | `FS.GA.SECURITY.MASTER.INTEREST.RATE.TYPE` | `FsGaSecurityMaster_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 198 | `FS.GA.SECURITY.MASTER.PRICE.YIELD.CURVE` | `FsGaSecurityMaster_PriceYieldCurve` | TField |  | Price yield curve to enable yield curve pricing Multifonds DB Column is TYP_TAUX_YIELD. |
| 199 | `FS.GA.SECURITY.MASTER.VALID.ISIN` | `FsGaSecurityMaster_ValidIsin` | TField |  | n International Securities Identification Number (ISIN) is a code that uniquely identifies a specific securities issue. Multifonds DB Column is VALID_ISIN. |
| 200 | `FS.GA.SECURITY.MASTER.VARIABLE.HURDLE` | `FsGaSecurityMaster_VariableHurdle` | TField |  | Related to performance fees, variable hurdle value will be taken for the adjustment HWM calculation if the hurdle type is variable hurdle rate. Multifonds DB Column is VARI_HURDLE. |
| 201 | `FS.GA.SECURITY.MASTER.MODIFIED.DURATION` | `FsGaSecurityMaster_ModifiedDuration` | TField |  | Gives the percentage alteration of the price of an interest-bearing instrument for a yield alteration of one unit (one percent) Multifonds DB Column is VOLATILITY. |
| 202 | `FS.GA.SECURITY.MASTER.WORKING.DAYS.TO.ADD` | `FsGaSecurityMaster_WorkingDaysToAdd` | TField |  | defines the number of days to be added to the Trade date Multifonds DB Column is WRK_DAYS_ADD. |
| 203 | `FS.GA.SECURITY.MASTER.SOURCE` | `FsGaSecurityMaster_Source` | TField |  | Quotation source Multifonds DB Column is XSOURCE. |
| 204 | `FS.GA.SECURITY.MASTER.YIELD.CAP` | `FsGaSecurityMaster_YieldCap` | TField |  | the computed yield to maturity using the YTM formula for fixed income securities is &gt; Yield cap then the Yield cap is used for computing SEC income. Multifonds DB Column is YIELD_CAP. |
| 205 | `FS.GA.SECURITY.MASTER.ISSUE.YIELD` | `FsGaSecurityMaster_IssueYield` | TField |  | purchase issue yield of the security. Multifonds DB Column is YIELD_EMIS. |
| 206 | `FS.GA.SECURITY.MASTER.YIELD.TO.MATURITY` | `FsGaSecurityMaster_YieldToMaturity` | TField |  | Yield To maturity of the security Multifonds DB Column is YIELD_TO_MATURITY. |
| 207 | `FS.GA.SECURITY.MASTER.INTERNAL.SECURITY.ID` | `FsGaSecurityMaster_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 208 | `FS.GA.SECURITY.MASTER.SECURITY.DESCRIPTION` | `FsGaSecurityMaster_SecurityDescription` | TField |  | Description of security Multifonds DB Column is NOMVAL. |
| 209 | `FS.GA.SECURITY.MASTER.ISIN.CODE` | `FsGaSecurityMaster_IsinCode` | TField |  | International security identification number (ISIN) Multifonds DB Column is CODISIN. |
| 210 | `FS.GA.SECURITY.MASTER.EXTERNAL.REF` | `FsGaSecurityMaster_ExternalRef` | TField |  | External reference of the correspondent Multifonds DB Column is EXTERNAL_REF. |
| 211 | `FS.GA.SECURITY.MASTER.SEDOL` | `FsGaSecurityMaster_Sedol` | TField |  | Sedol Multifonds DB Column is SEDOL. |
| 212 | `FS.GA.SECURITY.MASTER.BOND.MARKET.TYPE` | `FsGaSecurityMaster_BondMarketType` | TField |  | Bond Market Type Multifonds DB Column is BOND_MARKET_TYPE. |
| 213 | `FS.GA.SECURITY.MASTER.IP.CODE` | `FsGaSecurityMaster_IpCode` | TField |  | Ip Code Multifonds DB Column is IP_CODE. |
| 214 | `FS.GA.SECURITY.MASTER.TAX.COUNTRY.CODE` | `FsGaSecurityMaster_TaxCountryCode` | TField |  | Tax Country Code Multifonds DB Column is TC_CODE. |
| 215 | `FS.GA.SECURITY.MASTER.TAX.TYPE` | `FsGaSecurityMaster_TaxType` | TField |  | Tax Type Multifonds DB Column is TAX_TYPE. |
| 216 | `FS.GA.SECURITY.MASTER.45.DAY.INCLUSION` | `FsGaSecurityMaster_45DayInclusion` |  |  |  |
| 217 | `FS.GA.SECURITY.MASTER.INVESTMENT.REFERENCE` | `FsGaSecurityMaster_InvestmentReference` | TField |  | Investment Reference Multifonds DB Column is FLG_KAPITAL_INV_REF. |
| 218 | `FS.GA.SECURITY.MASTER.DEFAULT.LTR` | `FsGaSecurityMaster_DefaultLtr` | TField |  | Default Ltr Multifonds DB Column is DEFAULT_LTR. |
| 219 | `FS.GA.SECURITY.MASTER.IY.PROCESS` | `FsGaSecurityMaster_IyProcess` | TField |  | Iy Process Multifonds DB Column is FLG_IY_PROCESS. |
| 220 | `FS.GA.SECURITY.MASTER.CLIENT.ID.SEC` | `FsGaSecurityMaster_ClientIdSec` | TField |  | Client Id Multifonds DB Column is CLIENT_ID_SEC. |
| 221 | `FS.GA.SECURITY.MASTER.IY.FOR.IP.CALCULATION` | `FsGaSecurityMaster_IyForIpCalculation` | TField |  | Iy For Ip Calculation Multifonds DB Column is FLG_IY_IP. |
| 222 | `FS.GA.SECURITY.MASTER.LAST.DATE.COUPON.PAID` | `FsGaSecurityMaster_LastDateCouponPaid` | TField |  | Last Date Coupon Paid Multifonds DB Column is DDPC. |
| 223 | `FS.GA.SECURITY.MASTER.CTXFLT` | `FsGaSecurityMaster_Ctxflt` | TField |  | Ctxflt Multifonds DB Column is CTXFLT. |
| 224 | `FS.GA.SECURITY.MASTER.PERCENTAGE.VARIATION` | `FsGaSecurityMaster_PercentageVariation` | TField |  | Variation of Price in Percentage Multifonds DB Column is PCTVAR. |
| 225 | `FS.GA.SECURITY.MASTER.NEW.CALCULATION.DATE` | `FsGaSecurityMaster_NewCalculationDate` | TField |  | New Calculation Date Multifonds DB Column is DATE_CALCUL. |
| 226 | `FS.GA.SECURITY.MASTER.BID.PRICE` | `FsGaSecurityMaster_BidPrice` | TField |  | Denotes the Bid price of the securities Multifonds DB Column is COURSVAL_BID. |
| 227 | `FS.GA.SECURITY.MASTER.OFFER.PRICE` | `FsGaSecurityMaster_OfferPrice` | TField |  | Denotes the Offer price of the securities Multifonds DB Column is COURSVAL_OFFER. |
| 228 | `FS.GA.SECURITY.MASTER.PREVIOUS.COURS.DATE` | `FsGaSecurityMaster_PreviousCoursDate` | TField |  | Previous Cours Date Multifonds DB Column is DATE_COURS_PREC. |
| 229 | `FS.GA.SECURITY.MASTER.ACTUAL.COURS.DATE` | `FsGaSecurityMaster_ActualCoursDate` | TField |  | Actual Cours Date Multifonds DB Column is DATE_COURS_ACTUEL. |
| 230 | `FS.GA.SECURITY.MASTER.REPAYMENT.MODEL` | `FsGaSecurityMaster_RepaymentModel` | TField |  | Repayment Model Multifonds DB Column is REPAY_MODEL. |
| 231 | `FS.GA.SECURITY.MASTER.POOL.ID` | `FsGaSecurityMaster_PoolId` | TField |  | Pool Id Multifonds DB Column is POOL_ID. |
| 232 | `FS.GA.SECURITY.MASTER.MBS.FACTOR` | `FsGaSecurityMaster_MbsFactor` | TField |  | MBS Factor Multifonds DB Column is MBS_FACTOR. |
| 233 | `FS.GA.SECURITY.MASTER.MBS.DATE` | `FsGaSecurityMaster_MbsDate` | TField |  | MBS Date Multifonds DB Column is MBS_DATE. |
| 234 | `FS.GA.SECURITY.MASTER.PRIMARY.SECURITY.ID` | `FsGaSecurityMaster_PrimarySecurityId` | TField |  | Primary Security Id Multifonds DB Column is PRIMARY_NOVAL. |
| 235 | `FS.GA.SECURITY.MASTER.NUMBER.SEQUENCE` | `FsGaSecurityMaster_NumberSequence` | TField |  | Sequence Number Multifonds DB Column is NO_SEQ. |
| 236 | `FS.GA.SECURITY.MASTER.WEIGHT` | `FsGaSecurityMaster_Weight` | TField |  | Weight Multifonds DB Column is WEIGHT. |
| 237 | `FS.GA.SECURITY.MASTER.ITL.ISSUER` | `FsGaSecurityMaster_ItlIssuer` | TField |  | Itl Issuer Multifonds DB Column is ITL_ISSUER. |
| 238 | `FS.GA.SECURITY.MASTER.MANUAL.DIV.RATE` | `FsGaSecurityMaster_ManualDivRate` | TField |  | Manual Div Rate Multifonds DB Column is FLG_DIVRATE_MANUAL. |
| 239 | `FS.GA.SECURITY.MASTER.ORIGINAL.ISSUE.DISCOUNT.TXINT` | `FsGaSecurityMaster_OriginalIssueDiscountTxint` | TField |  | Original Issue Discount Txint Multifonds DB Column is OID_TXINT. |
| 240 | `FS.GA.SECURITY.MASTER.FACTOR.ASSUMPTION` | `FsGaSecurityMaster_FactorAssumption` | TField |  | Estimated Income Trust Factor Multifonds DB Column is FACTOR_ASSUMPTIONS. |
| 241 | `FS.GA.SECURITY.MASTER.MBS.YIELD.MATURITY` | `FsGaSecurityMaster_MbsYieldMaturity` | TField |  | MBS Yield Maturity Multifonds DB Column is MBS_YIELD_MATURITY. |
| 242 | `FS.GA.SECURITY.MASTER.MBS.TXINT` | `FsGaSecurityMaster_MbsTxint` | TField |  | MBS Txint Multifonds DB Column is MBS_TXINT. |
| 243 | `FS.GA.SECURITY.MASTER.RATING.FOR.LONG` | `FsGaSecurityMaster_RatingForLong` | TField |  | Rating For Long Multifonds DB Column is CRATING_L. |
| 244 | `FS.GA.SECURITY.MASTER.RATING.FOR.SHORT` | `FsGaSecurityMaster_RatingForShort` | TField |  | Rating For Short Multifonds DB Column is CRATING_S. |
| 245 | `FS.GA.SECURITY.MASTER.RATING.TYPE.FOR.LONG` | `FsGaSecurityMaster_RatingTypeForLong` | TField |  | Rating Type For Long Multifonds DB Column is TYP_RATING_L. |
| 246 | `FS.GA.SECURITY.MASTER.RATING.TYPE.FOR.SHORT` | `FsGaSecurityMaster_RatingTypeForShort` | TField |  | Rating Type For Short Multifonds DB Column is TYP_RATING_S. |
| 247 | `FS.GA.SECURITY.MASTER.ARCHIVE` | `FsGaSecurityMaster_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 248 | `FS.GA.SECURITY.MASTER.NOTIF` | `FsGaSecurityMaster_Notif` | TField |  | Notif Multifonds DB Column is FLG_NOTIF. |
| 249 | `FS.GA.SECURITY.MASTER.TCN.SPREAD.APPLICABLE` | `FsGaSecurityMaster_TcnSpreadApplicable` | TField |  | The spread applicable to a TCN security, type of French bonds Multifonds DB Column is FLG_TCN_SPR. |
| 250 | `FS.GA.SECURITY.MASTER.OPER.AMOUNT` | `FsGaSecurityMaster_OperAmount` | TField |  | Oper Amount Multifonds DB Column is MNT_OPER. |
| 251 | `FS.GA.SECURITY.MASTER.PAYDOWN.AMOUNT` | `FsGaSecurityMaster_PaydownAmount` | TField |  | Paydown Amount Multifonds DB Column is MNT_PAYDWN. |
| 252 | `FS.GA.SECURITY.MASTER.PRINCIPAL.AMOUNT` | `FsGaSecurityMaster_PrincipalAmount` | TField |  | Principal Amount Multifonds DB Column is MNT_PRINCIPAL. |
| 253 | `FS.GA.SECURITY.MASTER.TOTAL.PAYMENT.AMOUNT` | `FsGaSecurityMaster_TotalPaymentAmount` | TField |  | Total Payment Amount Multifonds DB Column is MNT_PYMNT_TOT. |
| 254 | `FS.GA.SECURITY.MASTER.ENDING.BALANCE.AMOUNT` | `FsGaSecurityMaster_EndingBalanceAmount` | TField |  | Ending Balance Amount Multifonds DB Column is MNT_END_BAL. |
| 255 | `FS.GA.SECURITY.MASTER.EX.COUPON` | `FsGaSecurityMaster_ExCoupon` | TField |  | Ex Coupon Multifonds DB Column is EXCOUPON. |
| 256 | `FS.GA.SECURITY.MASTER.NEXT.EX.COUPON.DATE` | `FsGaSecurityMaster_NextExCouponDate` | TField |  | Next Ex Coupon Date Multifonds DB Column is NEXTEXCOUPONDATE. |
| 257 | `FS.GA.SECURITY.MASTER.DELAY.FACTOR.DAYS.FOR.IIB` | `FsGaSecurityMaster_DelayFactorDaysForIib` | TField |  | Delay Factor Days For IIB Multifonds DB Column is DELAY_DAYS_IIB. |
| 258 | `FS.GA.SECURITY.MASTER.NA.ASSET.TYPE` | `FsGaSecurityMaster_NaAssetType` | TField |  | Na Asset Type Multifonds DB Column is NA_ASSET_TYPE. |
| 259 | `FS.GA.SECURITY.MASTER.NA.ASSET.SUB.TYPE` | `FsGaSecurityMaster_NaAssetSubType` | TField |  | Na Asset Sub Type Multifonds DB Column is NA_ASSET_SUBTYPE. |
| 260 | `FS.GA.SECURITY.MASTER.INSTRUMENT.GROUP` | `FsGaSecurityMaster_InstrumentGroup` | TField |  | Instrument Group Multifonds DB Column is INSTRUMENT_GROUP. |
| 261 | `FS.GA.SECURITY.MASTER.INSTRUMENT.TEMPLATE` | `FsGaSecurityMaster_InstrumentTemplate` | TField |  | Instrument Template Multifonds DB Column is INST_TEMPLATE. |
| 262 | `FS.GA.SECURITY.MASTER.PARENT.SECURITY.ID` | `FsGaSecurityMaster_ParentSecurityId` | TField |  | Parent Security Id Multifonds DB Column is PARENT_NOVAL. |
| 263 | `FS.GA.SECURITY.MASTER.LOAN.TYPE` | `FsGaSecurityMaster_LoanType` | TField |  | Loan Type Multifonds DB Column is LOAN_TYPE. |
| 264 | `FS.GA.SECURITY.MASTER.PLACE.HOLDER.CONTRACT` | `FsGaSecurityMaster_PlaceHolderContract` | TField |  | Place Holder Contract Multifonds DB Column is FLG_PLACEHOLDER_CONTRACT. |
| 265 | `FS.GA.SECURITY.MASTER.MATURED` | `FsGaSecurityMaster_Matured` | TField |  | Matured Flag Multifonds DB Column is INST_MATURED_FLG. |
| 266 | `FS.GA.SECURITY.MASTER.TAX.EXCEPT.COUNTRY` | `FsGaSecurityMaster_TaxExceptCountry` | TField |  | Tax Except Country Multifonds DB Column is TAX_EXP_CPAYSVAL. |
| 267 | `FS.GA.SECURITY.MASTER.BOND.TAX.OR.CGT` | `FsGaSecurityMaster_BondTaxOrCgt` | TField |  | Bond Tax Or CGT Multifonds DB Column is FLG_CGT_BONDTAX. |
| 268 | `FS.GA.SECURITY.MASTER.MARKET.VALUE.CRYSTALLIZATION` | `FsGaSecurityMaster_MarketValueCrystallization` | TField |  | Market Value Crystallization Multifonds DB Column is FLG_MVCRYST_BT. |
| 269 | `FS.GA.SECURITY.MASTER.DEEMED.DISPOSITION` | `FsGaSecurityMaster_DeemedDisposition` | TField |  | Deemed Disposition Multifonds DB Column is FLG_DEEMED_DISP. |
| 270 | `FS.GA.SECURITY.MASTER.YIELD.CURVE` | `FsGaSecurityMaster_YieldCurve` | TField |  | Yield Curve Multifonds DB Column is YIELD_CURVE. |
| 271 | `FS.GA.SECURITY.MASTER.SA.BOND.C` | `FsGaSecurityMaster_SaBondC` | TField |  | Sa Bond C Multifonds DB Column is FLG_SA_BOND_C. |
| 272 | `FS.GA.SECURITY.MASTER.SA.BOND.S` | `FsGaSecurityMaster_SaBondS` | TField |  | Sa Bond S Multifonds DB Column is FLG_SA_BOND_N. |
| 273 | `FS.GA.SECURITY.MASTER.PERCENTAGE.SPREAD` | `FsGaSecurityMaster_PercentageSpread` | TField |  | Percentage Spread Multifonds DB Column is FLG_SPRD_PCT. |
| 274 | `FS.GA.SECURITY.MASTER.UNDERLYING.SWAP` | `FsGaSecurityMaster_UnderlyingSwap` | TField |  | Underlying Swap Multifonds DB Column is FLG_SWAP_UNDERLYING. |
| 275 | `FS.GA.SECURITY.MASTER.FRANKED.DIVIDEND.TAX.PERCENT` | `FsGaSecurityMaster_FrankedDividendTaxPercent` | TField |  | Franked tax percentage on the dividend income Multifonds DB Column is PFRANKTAX. |
| 276 | `FS.GA.SECURITY.MASTER.ENTITLEMENT.DATE` | `FsGaSecurityMaster_EntitlementDate` | TField |  | The ex-date, or ex-dividend date, is the date on or after which a security is traded without a previously declared dividend or distribution. Multifonds DB Column is DEXEC. |
| 277 | `FS.GA.SECURITY.MASTER.FIXED.COUPON.DAYS` | `FsGaSecurityMaster_FixedCouponDays` | TField |  | Fixed Coupon Days Multifonds DB Column is FIXED_COUP_DAYS. |
| 278 | `FS.GA.SECURITY.MASTER.FIXED.FREQUENCY` | `FsGaSecurityMaster_FixedFrequency` | TField |  | Fixed Frequency Multifonds DB Column is FIXED_FREQ. |
| 279 | `FS.GA.SECURITY.MASTER.SPECIFIC.ROUNDING` | `FsGaSecurityMaster_SpecificRounding` | TField |  | Specific Rounding Multifonds DB Column is FLG_SPEC_ROUND. |
| 280 | `FS.GA.SECURITY.MASTER.RESERVED10` | `FsGaSecurityMaster_Reserved10` | TField |  |  |
| 281 | `FS.GA.SECURITY.MASTER.RESERVED9` | `FsGaSecurityMaster_Reserved9` | TField |  |  |
| 282 | `FS.GA.SECURITY.MASTER.RESERVED8` | `FsGaSecurityMaster_Reserved8` | TField |  |  |
| 283 | `FS.GA.SECURITY.MASTER.RESERVED7` | `FsGaSecurityMaster_Reserved7` | TField |  |  |
| 284 | `FS.GA.SECURITY.MASTER.RESERVED6` | `FsGaSecurityMaster_Reserved6` | TField |  |  |
| 285 | `FS.GA.SECURITY.MASTER.RESERVED5` | `FsGaSecurityMaster_Reserved5` | TField |  |  |
| 286 | `FS.GA.SECURITY.MASTER.RESERVED4` | `FsGaSecurityMaster_Reserved4` | TField |  |  |
| 287 | `FS.GA.SECURITY.MASTER.RESERVED3` | `FsGaSecurityMaster_Reserved3` | TField |  |  |
| 288 | `FS.GA.SECURITY.MASTER.RESERVED2` | `FsGaSecurityMaster_Reserved2` | TField |  |  |
| 289 | `FS.GA.SECURITY.MASTER.RESERVED1` | `FsGaSecurityMaster_Reserved1` | TField |  |  |
| 290 | `FS.GA.SECURITY.MASTER.LOCAL.REF` | `FsGaSecurityMaster_LocalRef` |  |  |  |
| 291 | `FS.GA.SECURITY.MASTER.OVERRIDE` | `FsGaSecurityMaster_Override` |  |  |  |
| 292 | `FS.GA.SECURITY.MASTER.RECORD.STATUS` | `FsGaSecurityMaster_RecordStatus` | String |  |  |
| 293 | `FS.GA.SECURITY.MASTER.CURR.NO` | `FsGaSecurityMaster_CurrNo` | String |  |  |
| 294 | `FS.GA.SECURITY.MASTER.INPUTTER` | `FsGaSecurityMaster_Inputter` |  |  |  |
| 295 | `FS.GA.SECURITY.MASTER.DATE.TIME` | `FsGaSecurityMaster_DateTime` |  |  |  |
| 296 | `FS.GA.SECURITY.MASTER.AUTHORISER` | `FsGaSecurityMaster_Authoriser` | String |  |  |
| 297 | `FS.GA.SECURITY.MASTER.CO.CODE` | `FsGaSecurityMaster_CoCode` | String |  |  |
| 298 | `FS.GA.SECURITY.MASTER.DEPT.CODE` | `FsGaSecurityMaster_DeptCode` | String |  |  |
| 299 | `FS.GA.SECURITY.MASTER.AUDITOR.CODE` | `FsGaSecurityMaster_AuditorCode` | String |  |  |
| 300 | `FS.GA.SECURITY.MASTER.AUDIT.DATE.TIME` | `FsGaSecurityMaster_AuditDateTime` | String |  |  |
