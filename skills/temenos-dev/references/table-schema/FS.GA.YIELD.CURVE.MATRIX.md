# FS.GA.YIELD.CURVE.MATRIX — Table Schema

> Source: `INSERTS/I_F.FS.GA.YIELD.CURVE.MATRIX` in `FS_PricesRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.YIELD.CURVE.MATRIX.INTEREST.RATE.TYPE` | `FsGaYieldCurveMatrix_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 2 | `FS.GA.YIELD.CURVE.MATRIX.RATE.AGENCY` | `FsGaYieldCurveMatrix_RateAgency` | TField |  | Rate Agency Multifonds DB Column is RATE_AGENCY. |
| 3 | `FS.GA.YIELD.CURVE.MATRIX.RATING.SCALE` | `FsGaYieldCurveMatrix_RatingScale` | TField |  | Credit Quality Rating Scale Multifonds DB Column is RATE_SCALE. |
| 4 | `FS.GA.YIELD.CURVE.MATRIX.RATING.VALUE` | `FsGaYieldCurveMatrix_RatingValue` | TField |  | Rating Value Multifonds DB Column is RATE_VALUE. |
| 5 | `FS.GA.YIELD.CURVE.MATRIX.LOCAL.CURRENCY` | `FsGaYieldCurveMatrix_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 6 | `FS.GA.YIELD.CURVE.MATRIX.EFFECTIVE.DATE` | `FsGaYieldCurveMatrix_EffectiveDate` | TField |  | Effective date to be applied. Multifonds DB Column is DATE_EFFECTIVE. |
| 7 | `FS.GA.YIELD.CURVE.MATRIX.SPREAD.RATE.EFFECTIVE.DATE` | `FsGaYieldCurveMatrix_SpreadRateEffectiveDate` | TField |  | Spread Rate Effective date Multifonds DB Column is DATE_SPREAD. |
| 8 | `FS.GA.YIELD.CURVE.MATRIX.RANK` | `FsGaYieldCurveMatrix_Rank` | TField |  | Ranking Order Multifonds DB Column is RANK. |
| 9 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.1D` | `FsGaYieldCurveMatrix_GovernmentYield1d` | TField |  | Government Yield 1D Multifonds DB Column is GOVT_YLD_1D. |
| 10 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.15D` | `FsGaYieldCurveMatrix_GovernmentYield15d` | TField |  | Government Yield 15D Multifonds DB Column is GOVT_YLD_15D. |
| 11 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.1M` | `FsGaYieldCurveMatrix_GovernmentYield1m` | TField |  | Government Yield 1M Multifonds DB Column is GOVT_YLD_1M. |
| 12 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.45D` | `FsGaYieldCurveMatrix_GovernmentYield45d` | TField |  | Government Yield 45D Multifonds DB Column is GOVT_YLD_45D. |
| 13 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.2M` | `FsGaYieldCurveMatrix_GovernmentYield2m` | TField |  | Government Yield 2M Multifonds DB Column is GOVT_YLD_2M. |
| 14 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.3M` | `FsGaYieldCurveMatrix_GovernmentYield3m` | TField |  | Government Yield 3M Multifonds DB Column is GOVT_YLD_3M. |
| 15 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.4M` | `FsGaYieldCurveMatrix_GovernmentYield4m` | TField |  | Government Yield 4M Multifonds DB Column is GOVT_YLD_4M. |
| 16 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.5M` | `FsGaYieldCurveMatrix_GovernmentYield5m` | TField |  | Government Yield 5M Multifonds DB Column is GOVT_YLD_5M. |
| 17 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.6M` | `FsGaYieldCurveMatrix_GovernmentYield6m` | TField |  | Government Yield 6M Multifonds DB Column is GOVT_YLD_6M. |
| 18 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.7M` | `FsGaYieldCurveMatrix_GovernmentYield7m` | TField |  | Government Yield 7M Multifonds DB Column is GOVT_YLD_7M. |
| 19 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.8M` | `FsGaYieldCurveMatrix_GovernmentYield8m` | TField |  | Government Yield 8M Multifonds DB Column is GOVT_YLD_8M. |
| 20 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.9M` | `FsGaYieldCurveMatrix_GovernmentYield9m` | TField |  | Government Yield 9M Multifonds DB Column is GOVT_YLD_9M. |
| 21 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.10M` | `FsGaYieldCurveMatrix_GovernmentYield10m` | TField |  | Government Yield 10M Multifonds DB Column is GOVT_YLD_10M. |
| 22 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.11M` | `FsGaYieldCurveMatrix_GovernmentYield11m` | TField |  | Government Yield 11M Multifonds DB Column is GOVT_YLD_11M. |
| 23 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.1YR` | `FsGaYieldCurveMatrix_GovernmentYield1yr` | TField |  | Government Yield 1YR Multifonds DB Column is GOVT_YLD_1YR. |
| 24 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.1.5YR` | `FsGaYieldCurveMatrix_GovernmentYield15yr` | TField |  | Government Yield 15YR Multifonds DB Column is GOVT_YLD_15YR. |
| 25 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.2YR` | `FsGaYieldCurveMatrix_GovernmentYield2yr` | TField |  | Government Yield 2YR Multifonds DB Column is GOVT_YLD_2YR. |
| 26 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.3YR` | `FsGaYieldCurveMatrix_GovernmentYield3yr` | TField |  | Government Yield 3YR Multifonds DB Column is GOVT_YLD_3YR. |
| 27 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.4YR` | `FsGaYieldCurveMatrix_GovernmentYield4yr` | TField |  | Government Yield 4YR Multifonds DB Column is GOVT_YLD_4YR. |
| 28 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.5YR` | `FsGaYieldCurveMatrix_GovernmentYield5yr` | TField |  | Government Yield 5YR Multifonds DB Column is GOVT_YLD_5YR. |
| 29 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.6YR` | `FsGaYieldCurveMatrix_GovernmentYield6yr` | TField |  | Government Yield 6YR Multifonds DB Column is GOVT_YLD_6YR. |
| 30 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.7YR` | `FsGaYieldCurveMatrix_GovernmentYield7yr` | TField |  | Government Yield 7YR Multifonds DB Column is GOVT_YLD_7YR. |
| 31 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.8YR` | `FsGaYieldCurveMatrix_GovernmentYield8yr` | TField |  | Government Yield 8YR Multifonds DB Column is GOVT_YLD_8YR. |
| 32 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.9YR` | `FsGaYieldCurveMatrix_GovernmentYield9yr` | TField |  | Government Yield 9YR Multifonds DB Column is GOVT_YLD_9YR. |
| 33 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.10YR` | `FsGaYieldCurveMatrix_GovernmentYield10yr` | TField |  | Government Yield 10YR Multifonds DB Column is GOVT_YLD_10YR. |
| 34 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.11YR` | `FsGaYieldCurveMatrix_GovernmentYield11yr` | TField |  | Government Yield 11YR Multifonds DB Column is GOVT_YLD_11YR. |
| 35 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.12YR` | `FsGaYieldCurveMatrix_GovernmentYield12yr` | TField |  | Government Yield 12YR Multifonds DB Column is GOVT_YLD_12YR. |
| 36 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.13YR` | `FsGaYieldCurveMatrix_GovernmentYield13yr` | TField |  | Government Yield 13YR Multifonds DB Column is GOVT_YLD_13YR. |
| 37 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.14YR` | `FsGaYieldCurveMatrix_GovernmentYield14yr` | TField |  | Government Yield 14YR Multifonds DB Column is GOVT_YLD_14YR. |
| 38 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.15YR` | `FsGaYieldCurveMatrix_GovernmentYield15yr` | TField |  | Government Yield 15YR Multifonds DB Column is GOVT_YLD_15YR. |
| 39 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.20YR` | `FsGaYieldCurveMatrix_GovernmentYield20yr` | TField |  | Government Yield 20YR Multifonds DB Column is GOVT_YLD_20YR. |
| 40 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.25YR` | `FsGaYieldCurveMatrix_GovernmentYield25yr` | TField |  | Government Yield 25YR Multifonds DB Column is GOVT_YLD_25YR. |
| 41 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.30YR` | `FsGaYieldCurveMatrix_GovernmentYield30yr` | TField |  | Government Yield 30YR Multifonds DB Column is GOVT_YLD_30YR. |
| 42 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.40YR` | `FsGaYieldCurveMatrix_GovernmentYield40yr` | TField |  | Government Yield 40YR Multifonds DB Column is GOVT_YLD_40YR. |
| 43 | `FS.GA.YIELD.CURVE.MATRIX.GOVERNMENT.YIELD.50YR` | `FsGaYieldCurveMatrix_GovernmentYield50yr` | TField |  | Government Yield 50YR Multifonds DB Column is GOVT_YLD_50YR. |
| 44 | `FS.GA.YIELD.CURVE.MATRIX.ONE.DAY.SPREAD.RATE` | `FsGaYieldCurveMatrix_OneDaySpreadRate` | TField |  | Credit Quality Spread Rate for One Day Multifonds DB Column is SPREAD_RATE_1D. |
| 45 | `FS.GA.YIELD.CURVE.MATRIX.FIFTEEN.DAYS.SPREAD.RATE` | `FsGaYieldCurveMatrix_FifteenDaysSpreadRate` | TField |  | Credit Quality Spread Rate for Fifteen Days Multifonds DB Column is SPREAD_RATE_15D. |
| 46 | `FS.GA.YIELD.CURVE.MATRIX.ONE.MONTH.SPREAD.RATE` | `FsGaYieldCurveMatrix_OneMonthSpreadRate` | TField |  | Credit Quality Spread Rate for One Month Multifonds DB Column is SPREAD_RATE_1M. |
| 47 | `FS.GA.YIELD.CURVE.MATRIX.FORTYFIVE.DAYS.SPREAD.RATE` | `FsGaYieldCurveMatrix_FortyfiveDaysSpreadRate` | TField |  | Credit Quality Spread Rate for Fortyfive Days Multifonds DB Column is SPREAD_RATE_45D. |
| 48 | `FS.GA.YIELD.CURVE.MATRIX.TWO.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_TwoMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Two Months Multifonds DB Column is SPREAD_RATE_2M. |
| 49 | `FS.GA.YIELD.CURVE.MATRIX.THREE.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_ThreeMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Three Months Multifonds DB Column is SPREAD_RATE_3M. |
| 50 | `FS.GA.YIELD.CURVE.MATRIX.FOUR.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_FourMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Four Months Multifonds DB Column is SPREAD_RATE_4M. |
| 51 | `FS.GA.YIELD.CURVE.MATRIX.FIVE.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_FiveMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Five Months Multifonds DB Column is SPREAD_RATE_5M. |
| 52 | `FS.GA.YIELD.CURVE.MATRIX.SIX.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_SixMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Six Months Multifonds DB Column is SPREAD_RATE_6M. |
| 53 | `FS.GA.YIELD.CURVE.MATRIX.SEVEN.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_SevenMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Seven Months Multifonds DB Column is SPREAD_RATE_7M. |
| 54 | `FS.GA.YIELD.CURVE.MATRIX.EIGHT.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_EightMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Eight Months Multifonds DB Column is SPREAD_RATE_8M. |
| 55 | `FS.GA.YIELD.CURVE.MATRIX.NINE.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_NineMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Nine Months Multifonds DB Column is SPREAD_RATE_9M. |
| 56 | `FS.GA.YIELD.CURVE.MATRIX.TEN.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_TenMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Ten Months Multifonds DB Column is SPREAD_RATE_10M. |
| 57 | `FS.GA.YIELD.CURVE.MATRIX.ELEVEN.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_ElevenMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Eleven Months Multifonds DB Column is SPREAD_RATE_11M. |
| 58 | `FS.GA.YIELD.CURVE.MATRIX.ONE.YEAR.SPREAD.RATE` | `FsGaYieldCurveMatrix_OneYearSpreadRate` | TField |  | Credit Quality Spread Rate for One Year Multifonds DB Column is SPREAD_RATE_1YR. |
| 59 | `FS.GA.YIELD.CURVE.MATRIX.EIGHTEEN.MONTHS.SPREAD.RATE` | `FsGaYieldCurveMatrix_EighteenMonthsSpreadRate` | TField |  | Credit Quality Spread Rate for Eighteen Months Multifonds DB Column is SPREAD_RATE_18M. |
| 60 | `FS.GA.YIELD.CURVE.MATRIX.TWO.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_TwoYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Two Years Multifonds DB Column is SPREAD_RATE_2YR. |
| 61 | `FS.GA.YIELD.CURVE.MATRIX.THREE.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_ThreeYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Three Years Multifonds DB Column is SPREAD_RATE_3YR. |
| 62 | `FS.GA.YIELD.CURVE.MATRIX.FOUR.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_FourYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Four Years Multifonds DB Column is SPREAD_RATE_4YR. |
| 63 | `FS.GA.YIELD.CURVE.MATRIX.FIVE.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_FiveYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Five Years Multifonds DB Column is SPREAD_RATE_5YR. |
| 64 | `FS.GA.YIELD.CURVE.MATRIX.SIX.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_SixYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Six Years Multifonds DB Column is SPREAD_RATE_6YR. |
| 65 | `FS.GA.YIELD.CURVE.MATRIX.SEVEN.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_SevenYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Seven Years Multifonds DB Column is SPREAD_RATE_7YR. |
| 66 | `FS.GA.YIELD.CURVE.MATRIX.EIGHT.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_EightYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Eight Years Multifonds DB Column is SPREAD_RATE_8YR. |
| 67 | `FS.GA.YIELD.CURVE.MATRIX.NINE.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_NineYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Nine Years Multifonds DB Column is SPREAD_RATE_9YR. |
| 68 | `FS.GA.YIELD.CURVE.MATRIX.TEN.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_TenYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Ten Years Multifonds DB Column is SPREAD_RATE_10YR. |
| 69 | `FS.GA.YIELD.CURVE.MATRIX.ELEVEN.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_ElevenYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Eleven Years Multifonds DB Column is SPREAD_RATE_11YR. |
| 70 | `FS.GA.YIELD.CURVE.MATRIX.TWELVE.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_TwelveYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Twelve Years Multifonds DB Column is SPREAD_RATE_12YR. |
| 71 | `FS.GA.YIELD.CURVE.MATRIX.THIRTEEN.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_ThirteenYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Thirteen Years Multifonds DB Column is SPREAD_RATE_13YR. |
| 72 | `FS.GA.YIELD.CURVE.MATRIX.FOURTEEN.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_FourteenYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Fourteen Years Multifonds DB Column is SPREAD_RATE_14YR. |
| 73 | `FS.GA.YIELD.CURVE.MATRIX.FIFTEEN.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_FifteenYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Fifteen Years Multifonds DB Column is SPREAD_RATE_15YR. |
| 74 | `FS.GA.YIELD.CURVE.MATRIX.TWENTY.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_TwentyYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Twenty Years Multifonds DB Column is SPREAD_RATE_20YR. |
| 75 | `FS.GA.YIELD.CURVE.MATRIX.TWENTY.FIVE.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_TwentyFiveYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Twenty five Years Multifonds DB Column is SPREAD_RATE_25YR. |
| 76 | `FS.GA.YIELD.CURVE.MATRIX.THIRTY.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_ThirtyYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Thirty Years Multifonds DB Column is SPREAD_RATE_30YR. |
| 77 | `FS.GA.YIELD.CURVE.MATRIX.FORTY.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_FortyYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Forty Years Multifonds DB Column is SPREAD_RATE_40YR. |
| 78 | `FS.GA.YIELD.CURVE.MATRIX.FIFTY.YEARS.SPREAD.RATE` | `FsGaYieldCurveMatrix_FiftyYearsSpreadRate` | TField |  | Credit Quality Spread Rate for Fifty Years Multifonds DB Column is SPREAD_RATE_50YR. |
| 79 | `FS.GA.YIELD.CURVE.MATRIX.ONE.DAY.YIELD` | `FsGaYieldCurveMatrix_OneDayYield` | TField |  | Credit Quality Spread Rate for One Day Yield Multifonds DB Column is YIELD_1D. |
| 80 | `FS.GA.YIELD.CURVE.MATRIX.FIFTEEN.DAYS.YIELD` | `FsGaYieldCurveMatrix_FifteenDaysYield` | TField |  | Credit Quality Spread Rate for Fifteen Days Yield Multifonds DB Column is YIELD_15D. |
| 81 | `FS.GA.YIELD.CURVE.MATRIX.ONE.MONTH.YIELD` | `FsGaYieldCurveMatrix_OneMonthYield` | TField |  | Credit Quality Spread Rate for One Month Yield Multifonds DB Column is YIELD_1M. |
| 82 | `FS.GA.YIELD.CURVE.MATRIX.FORTYFIVE.DAYS.YIELD` | `FsGaYieldCurveMatrix_FortyfiveDaysYield` | TField |  | Credit Quality Spread Rate for Fortyfive Days Yield Multifonds DB Column is YIELD_45D. |
| 83 | `FS.GA.YIELD.CURVE.MATRIX.TWO.MONTHS.YIELD` | `FsGaYieldCurveMatrix_TwoMonthsYield` | TField |  | Credit Quality Spread Rate for Two Months Yield Multifonds DB Column is YIELD_2M. |
| 84 | `FS.GA.YIELD.CURVE.MATRIX.THREE.MONTHS.YIELD` | `FsGaYieldCurveMatrix_ThreeMonthsYield` | TField |  | Credit Quality Spread Rate for Three Months Yield Multifonds DB Column is YIELD_3M. |
| 85 | `FS.GA.YIELD.CURVE.MATRIX.FOUR.MONTHS.YIELD` | `FsGaYieldCurveMatrix_FourMonthsYield` | TField |  | Credit Quality Spread Rate for Four Months Yield Multifonds DB Column is YIELD_4M. |
| 86 | `FS.GA.YIELD.CURVE.MATRIX.FIVE.MONTHS.YIELD` | `FsGaYieldCurveMatrix_FiveMonthsYield` | TField |  | Credit Quality Spread Rate for Five Months Yield Multifonds DB Column is YIELD_5M. |
| 87 | `FS.GA.YIELD.CURVE.MATRIX.SIX.MONTHS.YIELD` | `FsGaYieldCurveMatrix_SixMonthsYield` | TField |  | Credit Quality Spread Rate for Six Months Yield Multifonds DB Column is YIELD_6M. |
| 88 | `FS.GA.YIELD.CURVE.MATRIX.SEVEN.MONTHS.YIELD` | `FsGaYieldCurveMatrix_SevenMonthsYield` | TField |  | Credit Quality Spread Rate for Seven Months Yield Multifonds DB Column is YIELD_7M. |
| 89 | `FS.GA.YIELD.CURVE.MATRIX.EIGHT.MONTHS.YIELD` | `FsGaYieldCurveMatrix_EightMonthsYield` | TField |  | Credit Quality Spread Rate for Eight Months Yield Multifonds DB Column is YIELD_8M. |
| 90 | `FS.GA.YIELD.CURVE.MATRIX.NINE.MONTHS.YIELD` | `FsGaYieldCurveMatrix_NineMonthsYield` | TField |  | Credit Quality Spread Rate for Nine Months Yield Multifonds DB Column is YIELD_9M. |
| 91 | `FS.GA.YIELD.CURVE.MATRIX.TEN.MONTHS.YIELD` | `FsGaYieldCurveMatrix_TenMonthsYield` | TField |  | Credit Quality Spread Rate for Ten Months Yield Multifonds DB Column is YIELD_10M. |
| 92 | `FS.GA.YIELD.CURVE.MATRIX.ELEVEN.MONTHS.YIELD` | `FsGaYieldCurveMatrix_ElevenMonthsYield` | TField |  | Credit Quality Spread Rate for Eleven Months Yield Multifonds DB Column is YIELD_11M. |
| 93 | `FS.GA.YIELD.CURVE.MATRIX.ONE.YEAR.YIELD` | `FsGaYieldCurveMatrix_OneYearYield` | TField |  | Credit Quality Spread Rate for One Year Yield Multifonds DB Column is YIELD_1YR. |
| 94 | `FS.GA.YIELD.CURVE.MATRIX.EIGHTEEN.MONTHS.YIELD` | `FsGaYieldCurveMatrix_EighteenMonthsYield` | TField |  | Credit Quality Spread Rate for Eighteen Months Yield Multifonds DB Column is YIELD_18M. |
| 95 | `FS.GA.YIELD.CURVE.MATRIX.TWO.YEARS.YIELD` | `FsGaYieldCurveMatrix_TwoYearsYield` | TField |  | Credit Quality Spread Rate for Two Years Yield Multifonds DB Column is YIELD_2YR. |
| 96 | `FS.GA.YIELD.CURVE.MATRIX.THREE.YEARS.YIELD` | `FsGaYieldCurveMatrix_ThreeYearsYield` | TField |  | Credit Quality Spread Rate for Three Years Yield Multifonds DB Column is YIELD_3YR. |
| 97 | `FS.GA.YIELD.CURVE.MATRIX.FOUR.YEARS.YIELD` | `FsGaYieldCurveMatrix_FourYearsYield` | TField |  | Credit Quality Spread Rate for Four Years Yield Multifonds DB Column is YIELD_4YR. |
| 98 | `FS.GA.YIELD.CURVE.MATRIX.FIVE.YEARS.YIELD` | `FsGaYieldCurveMatrix_FiveYearsYield` | TField |  | Credit Quality Spread Rate for Five Years Yield Multifonds DB Column is YIELD_5YR. |
| 99 | `FS.GA.YIELD.CURVE.MATRIX.SIX.YEARS.YIELD` | `FsGaYieldCurveMatrix_SixYearsYield` | TField |  | Credit Quality Spread Rate for Six Years Yield Multifonds DB Column is YIELD_6YR. |
| 100 | `FS.GA.YIELD.CURVE.MATRIX.SEVEN.YEARS.YIELD` | `FsGaYieldCurveMatrix_SevenYearsYield` | TField |  | Credit Quality Spread Rate for Seven Years Yield Multifonds DB Column is YIELD_7YR. |
| 101 | `FS.GA.YIELD.CURVE.MATRIX.EIGHT.YEARS.YIELD` | `FsGaYieldCurveMatrix_EightYearsYield` | TField |  | Credit Quality Spread Rate for Eight Years Yield Multifonds DB Column is YIELD_8YR. |
| 102 | `FS.GA.YIELD.CURVE.MATRIX.NINE.YEARS.YIELD` | `FsGaYieldCurveMatrix_NineYearsYield` | TField |  | Credit Quality Spread Rate for Nine Years Yield Multifonds DB Column is YIELD_9YR. |
| 103 | `FS.GA.YIELD.CURVE.MATRIX.TEN.YEARS.YIELD` | `FsGaYieldCurveMatrix_TenYearsYield` | TField |  | Credit Quality Spread Rate for Ten Years Yield Multifonds DB Column is YIELD_10YR. |
| 104 | `FS.GA.YIELD.CURVE.MATRIX.ELEVEN.YEARS.YIELD` | `FsGaYieldCurveMatrix_ElevenYearsYield` | TField |  | Credit Quality Spread Rate for Eleven Years Yield Multifonds DB Column is YIELD_11YR. |
| 105 | `FS.GA.YIELD.CURVE.MATRIX.TWELVE.YEARS.YIELD` | `FsGaYieldCurveMatrix_TwelveYearsYield` | TField |  | Credit Quality Spread Rate for Twelve Years Yield Multifonds DB Column is YIELD_12YR. |
| 106 | `FS.GA.YIELD.CURVE.MATRIX.THIRTEEN.YEARS.YIELD` | `FsGaYieldCurveMatrix_ThirteenYearsYield` | TField |  | Credit Quality Spread Rate for Thirteen Years Yield Multifonds DB Column is YIELD_13YR. |
| 107 | `FS.GA.YIELD.CURVE.MATRIX.FOURTEEN.YEARS.YIELD` | `FsGaYieldCurveMatrix_FourteenYearsYield` | TField |  | Credit Quality Spread Rate for Fourteen Years Yield Multifonds DB Column is YIELD_14YR. |
| 108 | `FS.GA.YIELD.CURVE.MATRIX.FIFTEEN.YEARS.YIELD` | `FsGaYieldCurveMatrix_FifteenYearsYield` | TField |  | Credit Quality Spread Rate for Fifteen Years Yield Multifonds DB Column is YIELD_15YR. |
| 109 | `FS.GA.YIELD.CURVE.MATRIX.TWENTY.YEARS.YIELD` | `FsGaYieldCurveMatrix_TwentyYearsYield` | TField |  | Credit Quality Spread Rate for Twenty Years Yield Multifonds DB Column is YIELD_20YR. |
| 110 | `FS.GA.YIELD.CURVE.MATRIX.TWENTY.FIVE.YEARS.YIELD` | `FsGaYieldCurveMatrix_TwentyFiveYearsYield` | TField |  | Credit Quality Spread Rate for Twenty five Years Yield Multifonds DB Column is YIELD_25YR. |
| 111 | `FS.GA.YIELD.CURVE.MATRIX.THIRTY.YEARS.YIELD` | `FsGaYieldCurveMatrix_ThirtyYearsYield` | TField |  | Credit Quality Spread Rate for Thirty Years Yield Multifonds DB Column is YIELD_30YR. |
| 112 | `FS.GA.YIELD.CURVE.MATRIX.FORTY.YEARS.YIELD` | `FsGaYieldCurveMatrix_FortyYearsYield` | TField |  | Credit Quality Spread Rate for Forty Years Yield Multifonds DB Column is YIELD_40YR. |
| 113 | `FS.GA.YIELD.CURVE.MATRIX.FIFTY.YEARS.YIELD` | `FsGaYieldCurveMatrix_FiftyYearsYield` | TField |  | Credit Quality Spread Rate for Fifty Years Yield Multifonds DB Column is YIELD_50YR. |
| 114 | `FS.GA.YIELD.CURVE.MATRIX.RESERVED10` | `FsGaYieldCurveMatrix_Reserved10` | TField |  |  |
| 115 | `FS.GA.YIELD.CURVE.MATRIX.RESERVED9` | `FsGaYieldCurveMatrix_Reserved9` | TField |  |  |
| 116 | `FS.GA.YIELD.CURVE.MATRIX.RESERVED8` | `FsGaYieldCurveMatrix_Reserved8` | TField |  |  |
| 117 | `FS.GA.YIELD.CURVE.MATRIX.RESERVED7` | `FsGaYieldCurveMatrix_Reserved7` | TField |  |  |
| 118 | `FS.GA.YIELD.CURVE.MATRIX.RESERVED6` | `FsGaYieldCurveMatrix_Reserved6` | TField |  |  |
| 119 | `FS.GA.YIELD.CURVE.MATRIX.RESERVED5` | `FsGaYieldCurveMatrix_Reserved5` | TField |  |  |
| 120 | `FS.GA.YIELD.CURVE.MATRIX.RESERVED4` | `FsGaYieldCurveMatrix_Reserved4` | TField |  |  |
| 121 | `FS.GA.YIELD.CURVE.MATRIX.RESERVED3` | `FsGaYieldCurveMatrix_Reserved3` | TField |  |  |
| 122 | `FS.GA.YIELD.CURVE.MATRIX.RESERVED2` | `FsGaYieldCurveMatrix_Reserved2` | TField |  |  |
| 123 | `FS.GA.YIELD.CURVE.MATRIX.RESERVED1` | `FsGaYieldCurveMatrix_Reserved1` | TField |  |  |
| 124 | `FS.GA.YIELD.CURVE.MATRIX.RECORD.STATUS` | `FsGaYieldCurveMatrix_RecordStatus` | String |  |  |
| 125 | `FS.GA.YIELD.CURVE.MATRIX.CURR.NO` | `FsGaYieldCurveMatrix_CurrNo` | String |  |  |
| 126 | `FS.GA.YIELD.CURVE.MATRIX.INPUTTER` | `FsGaYieldCurveMatrix_Inputter` |  |  |  |
| 127 | `FS.GA.YIELD.CURVE.MATRIX.DATE.TIME` | `FsGaYieldCurveMatrix_DateTime` |  |  |  |
| 128 | `FS.GA.YIELD.CURVE.MATRIX.AUTHORISER` | `FsGaYieldCurveMatrix_Authoriser` | String |  |  |
| 129 | `FS.GA.YIELD.CURVE.MATRIX.CO.CODE` | `FsGaYieldCurveMatrix_CoCode` | String |  |  |
| 130 | `FS.GA.YIELD.CURVE.MATRIX.DEPT.CODE` | `FsGaYieldCurveMatrix_DeptCode` | String |  |  |
| 131 | `FS.GA.YIELD.CURVE.MATRIX.AUDITOR.CODE` | `FsGaYieldCurveMatrix_AuditorCode` | String |  |  |
| 132 | `FS.GA.YIELD.CURVE.MATRIX.AUDIT.DATE.TIME` | `FsGaYieldCurveMatrix_AuditDateTime` | String |  |  |
