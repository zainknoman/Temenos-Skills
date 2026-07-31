# FS.GA.SECURITY.PRICE.UPDATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.SECURITY.PRICE.UPDATE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SECURITY.PRICE.UPDATE.PARENT.REF.ID` | `FsGaSecurityPriceUpdate_ParentRefId` |  |  |  |
| 2 | `FS.GA.SECURITY.PRICE.UPDATE.ORA.ROWID` | `FsGaSecurityPriceUpdate_OraRowid` |  |  |  |
| 3 | `FS.GA.SECURITY.PRICE.UPDATE.INTERNAL.SECURITY.ID` | `FsGaSecurityPriceUpdate_InternalSecurityId` |  |  |  |
| 4 | `FS.GA.SECURITY.PRICE.UPDATE.QUOTATION.PLACE` | `FsGaSecurityPriceUpdate_QuotationPlace` |  |  |  |
| 5 | `FS.GA.SECURITY.PRICE.UPDATE.QUOTATION.CURRENCY` | `FsGaSecurityPriceUpdate_QuotationCurrency` |  |  |  |
| 6 | `FS.GA.SECURITY.PRICE.UPDATE.MARKET.PRICE` | `FsGaSecurityPriceUpdate_MarketPrice` |  |  |  |
| 7 | `FS.GA.SECURITY.PRICE.UPDATE.TRADE.OR.VALUE.OR.ACC.DATE` | `FsGaSecurityPriceUpdate_TradeOrValueOrAccDate` |  |  |  |
| 8 | `FS.GA.SECURITY.PRICE.UPDATE.QUOTATION.TYPE` | `FsGaSecurityPriceUpdate_QuotationType` |  |  |  |
| 9 | `FS.GA.SECURITY.PRICE.UPDATE.BID.PRICE` | `FsGaSecurityPriceUpdate_BidPrice` |  |  |  |
| 10 | `FS.GA.SECURITY.PRICE.UPDATE.OFFER.PRICE` | `FsGaSecurityPriceUpdate_OfferPrice` |  |  |  |
| 11 | `FS.GA.SECURITY.PRICE.UPDATE.PROVENANCE` | `FsGaSecurityPriceUpdate_Provenance` |  |  |  |
| 12 | `FS.GA.SECURITY.PRICE.UPDATE.TYPE.OF.PRICE` | `FsGaSecurityPriceUpdate_TypeOfPrice` |  |  |  |
| 13 | `FS.GA.SECURITY.PRICE.UPDATE.SELECTED.BID.PRICE` | `FsGaSecurityPriceUpdate_SelectedBidPrice` |  |  |  |
| 14 | `FS.GA.SECURITY.PRICE.UPDATE.SELECTED.OFFER.PRICE` | `FsGaSecurityPriceUpdate_SelectedOfferPrice` |  |  |  |
| 15 | `FS.GA.SECURITY.PRICE.UPDATE.C.D` | `FsGaSecurityPriceUpdate_CD` |  |  |  |
| 16 | `FS.GA.SECURITY.PRICE.UPDATE.PRICING.DATE` | `FsGaSecurityPriceUpdate_PricingDate` |  |  |  |
| 17 | `FS.GA.SECURITY.PRICE.UPDATE.INCOME.EQUALISATION.PER.UNIT` | `FsGaSecurityPriceUpdate_IncomeEqualisationPerUnit` |  |  |  |
| 18 | `FS.GA.SECURITY.PRICE.UPDATE.AKTIENGEWINN.PER.UNIT` | `FsGaSecurityPriceUpdate_AktiengewinnPerUnit` |  |  |  |
| 19 | `FS.GA.SECURITY.PRICE.UPDATE.LEVERAGE` | `FsGaSecurityPriceUpdate_Leverage` |  |  |  |
| 20 | `FS.GA.SECURITY.PRICE.UPDATE.PERFORMANCE.FEES.PER.UNIT` | `FsGaSecurityPriceUpdate_PerformanceFeesPerUnit` |  |  |  |
| 21 | `FS.GA.SECURITY.PRICE.UPDATE.SENSIBILITY` | `FsGaSecurityPriceUpdate_Sensibility` |  |  |  |
| 22 | `FS.GA.SECURITY.PRICE.UPDATE.YIELD` | `FsGaSecurityPriceUpdate_Yield` |  |  |  |
| 23 | `FS.GA.SECURITY.PRICE.UPDATE.ACCRUED.INTEREST` | `FsGaSecurityPriceUpdate_AccruedInterest` |  |  |  |
| 24 | `FS.GA.SECURITY.PRICE.UPDATE.AKTIENGEWINN.IN.PERCENTAGE` | `FsGaSecurityPriceUpdate_AktiengewinnInPercentage` |  |  |  |
| 25 | `FS.GA.SECURITY.PRICE.UPDATE.INCOME.YIELD` | `FsGaSecurityPriceUpdate_IncomeYield` |  |  |  |
| 26 | `FS.GA.SECURITY.PRICE.UPDATE.ORIGIN.INCOME.YIELD` | `FsGaSecurityPriceUpdate_OriginIncomeYield` |  |  |  |
| 27 | `FS.GA.SECURITY.PRICE.UPDATE.ORIGIN.YIELD.TO.MATURITY` | `FsGaSecurityPriceUpdate_OriginYieldToMaturity` |  |  |  |
| 28 | `FS.GA.SECURITY.PRICE.UPDATE.PRICE.TRUE` | `FsGaSecurityPriceUpdate_PriceTrue` |  |  |  |
| 29 | `FS.GA.SECURITY.PRICE.UPDATE.MID.PRICE` | `FsGaSecurityPriceUpdate_MidPrice` |  |  |  |
| 30 | `FS.GA.SECURITY.PRICE.UPDATE.TAXABLE.INCOME.PER.SHARE.UNIT` | `FsGaSecurityPriceUpdate_TaxableIncomePerShareUnit` |  |  |  |
| 31 | `FS.GA.SECURITY.PRICE.UPDATE.TIS.PART.PERCENTAGE` | `FsGaSecurityPriceUpdate_TisPartPercentage` |  |  |  |
| 32 | `FS.GA.SECURITY.PRICE.UPDATE.SEQUENCE.NUMBER` | `FsGaSecurityPriceUpdate_SequenceNumber` |  |  |  |
| 33 | `FS.GA.SECURITY.PRICE.UPDATE.DELTA` | `FsGaSecurityPriceUpdate_Delta` |  |  |  |
| 34 | `FS.GA.SECURITY.PRICE.UPDATE.IG.PER.UNIT` | `FsGaSecurityPriceUpdate_IgPerUnit` |  |  |  |
| 35 | `FS.GA.SECURITY.PRICE.UPDATE.IMMOBILIENGEWINN.PERCENTAGE` | `FsGaSecurityPriceUpdate_ImmobiliengewinnPercentage` |  |  |  |
| 36 | `FS.GA.SECURITY.PRICE.UPDATE.GROSS.SHARE.PRICE` | `FsGaSecurityPriceUpdate_GrossSharePrice` |  |  |  |
| 37 | `FS.GA.SECURITY.PRICE.UPDATE.SPREAD` | `FsGaSecurityPriceUpdate_Spread` |  |  |  |
| 38 | `FS.GA.SECURITY.PRICE.UPDATE.KEST.PER.UNIT` | `FsGaSecurityPriceUpdate_KestPerUnit` |  |  |  |
| 39 | `FS.GA.SECURITY.PRICE.UPDATE.KEST.PART.PERCENTAGE` | `FsGaSecurityPriceUpdate_KestPartPercentage` |  |  |  |
| 40 | `FS.GA.SECURITY.PRICE.UPDATE.DISCOUNT.MARGIN` | `FsGaSecurityPriceUpdate_DiscountMargin` |  |  |  |
| 41 | `FS.GA.SECURITY.PRICE.UPDATE.TAXABLE.INCOME.2.PER.SHARE` | `FsGaSecurityPriceUpdate_TaxableIncome2PerShare` |  |  |  |
| 42 | `FS.GA.SECURITY.PRICE.UPDATE.TAXABLE.INCOME.3.PER.SHARE` | `FsGaSecurityPriceUpdate_TaxableIncome3PerShare` |  |  |  |
| 43 | `FS.GA.SECURITY.PRICE.UPDATE.KOREAN.TAXABLE.PER.SHARE` | `FsGaSecurityPriceUpdate_KoreanTaxablePerShare` |  |  |  |
| 44 | `FS.GA.SECURITY.PRICE.UPDATE.NON.TAXABLE.PRICE` | `FsGaSecurityPriceUpdate_NonTaxablePrice` |  |  |  |
| 45 | `FS.GA.SECURITY.PRICE.UPDATE.KOREAN.NONTAXABLE.PER.SHARE` | `FsGaSecurityPriceUpdate_KoreanNontaxablePerShare` |  |  |  |
| 46 | `FS.GA.SECURITY.PRICE.UPDATE.WEIGHTED.AVERAGE.LIFE.OF.SEC` | `FsGaSecurityPriceUpdate_WeightedAverageLifeOfSec` |  |  |  |
| 47 | `FS.GA.SECURITY.PRICE.UPDATE.INTERPOLATED.YIELD.OF.SECURITY` | `FsGaSecurityPriceUpdate_InterpolatedYieldOfSecurity` |  |  |  |
| 48 | `FS.GA.SECURITY.PRICE.UPDATE.PRICE.SOURCE` | `FsGaSecurityPriceUpdate_PriceSource` |  |  |  |
| 49 | `FS.GA.SECURITY.PRICE.UPDATE.MAKER.USER.NAME` | `FsGaSecurityPriceUpdate_MakerUserName` |  |  |  |
| 50 | `FS.GA.SECURITY.PRICE.UPDATE.MAKER.PROCESSING.DATE` | `FsGaSecurityPriceUpdate_MakerProcessingDate` |  |  |  |
| 51 | `FS.GA.SECURITY.PRICE.UPDATE.INV.FUNDS.TAX.1.PER.UNIT` | `FsGaSecurityPriceUpdate_InvFundsTax1PerUnit` |  |  |  |
| 52 | `FS.GA.SECURITY.PRICE.UPDATE.INV.FUNDS.TAX.2.PER.UNIT` | `FsGaSecurityPriceUpdate_InvFundsTax2PerUnit` |  |  |  |
| 53 | `FS.GA.SECURITY.PRICE.UPDATE.INV.FUNDS.TAX.3.PER.UNIT` | `FsGaSecurityPriceUpdate_InvFundsTax3PerUnit` |  |  |  |
| 54 | `FS.GA.SECURITY.PRICE.UPDATE.LOOK.THRU.RATIO` | `FsGaSecurityPriceUpdate_LookThruRatio` |  |  |  |
| 55 | `FS.GA.SECURITY.PRICE.UPDATE.COURS.CLEAN` | `FsGaSecurityPriceUpdate_CoursClean` |  |  |  |
| 56 | `FS.GA.SECURITY.PRICE.UPDATE.RESERVED10` | `FsGaSecurityPriceUpdate_Reserved10` |  |  |  |
| 57 | `FS.GA.SECURITY.PRICE.UPDATE.RESERVED9` | `FsGaSecurityPriceUpdate_Reserved9` |  |  |  |
| 58 | `FS.GA.SECURITY.PRICE.UPDATE.RESERVED8` | `FsGaSecurityPriceUpdate_Reserved8` |  |  |  |
| 59 | `FS.GA.SECURITY.PRICE.UPDATE.RESERVED7` | `FsGaSecurityPriceUpdate_Reserved7` |  |  |  |
| 60 | `FS.GA.SECURITY.PRICE.UPDATE.RESERVED6` | `FsGaSecurityPriceUpdate_Reserved6` |  |  |  |
| 61 | `FS.GA.SECURITY.PRICE.UPDATE.RESERVED5` | `FsGaSecurityPriceUpdate_Reserved5` |  |  |  |
| 62 | `FS.GA.SECURITY.PRICE.UPDATE.RESERVED4` | `FsGaSecurityPriceUpdate_Reserved4` |  |  |  |
| 63 | `FS.GA.SECURITY.PRICE.UPDATE.RESERVED3` | `FsGaSecurityPriceUpdate_Reserved3` |  |  |  |
| 64 | `FS.GA.SECURITY.PRICE.UPDATE.RESERVED2` | `FsGaSecurityPriceUpdate_Reserved2` |  |  |  |
| 65 | `FS.GA.SECURITY.PRICE.UPDATE.RESERVED1` | `FsGaSecurityPriceUpdate_Reserved1` |  |  |  |
| 66 | `FS.GA.SECURITY.PRICE.UPDATE.LOCAL.REF` | `FsGaSecurityPriceUpdate_LocalRef` |  |  |  |
| 67 | `FS.GA.SECURITY.PRICE.UPDATE.OVERRIDE` | `FsGaSecurityPriceUpdate_Override` |  |  |  |
| 68 | `FS.GA.SECURITY.PRICE.UPDATE.RECORD.STATUS` | `FsGaSecurityPriceUpdate_RecordStatus` |  |  |  |
| 69 | `FS.GA.SECURITY.PRICE.UPDATE.CURR.NO` | `FsGaSecurityPriceUpdate_CurrNo` |  |  |  |
| 70 | `FS.GA.SECURITY.PRICE.UPDATE.INPUTTER` | `FsGaSecurityPriceUpdate_Inputter` |  |  |  |
| 71 | `FS.GA.SECURITY.PRICE.UPDATE.DATE.TIME` | `FsGaSecurityPriceUpdate_DateTime` |  |  |  |
| 72 | `FS.GA.SECURITY.PRICE.UPDATE.AUTHORISER` | `FsGaSecurityPriceUpdate_Authoriser` |  |  |  |
| 73 | `FS.GA.SECURITY.PRICE.UPDATE.CO.CODE` | `FsGaSecurityPriceUpdate_CoCode` |  |  |  |
| 74 | `FS.GA.SECURITY.PRICE.UPDATE.DEPT.CODE` | `FsGaSecurityPriceUpdate_DeptCode` |  |  |  |
| 75 | `FS.GA.SECURITY.PRICE.UPDATE.AUDITOR.CODE` | `FsGaSecurityPriceUpdate_AuditorCode` |  |  |  |
| 76 | `FS.GA.SECURITY.PRICE.UPDATE.AUDIT.DATE.TIME` | `FsGaSecurityPriceUpdate_AuditDateTime` |  |  |  |
