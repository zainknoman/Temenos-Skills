# CG.PORTFOLIO — Table Schema

> Source: `INSERTS/I_F.CG.PORTFOLIO` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.CPG.CUSTOMER` | `CgPortfolio_Customer` | TField |  | Field will hold the Customer for whom the capital gain details are updated for the mentioned Financial Year This will be the first half of the ID i.e the Customer ID Valid Customer Number No input, system generated field |
| 2 | `CG.CPG.PORT.GRP.ID` | `CgPortfolio_PortGrpId` | TField |  | Field will hold the Portfolio group name for whom the capital gain details are updated for the mentioned Financial Year This will be the second half of the ID i.e the name of the Portfolio group No input, system generated field |
| 3 | `CG.CPG.PERIOD.START` | `CgPortfolio_PeriodStart` | TField |  | This field will hold the start date of the period i.e the start date of the financial year for which Capital gains are consolidated. Valid Date format No input, system generated field |
| 4 | `CG.CPG.PERIOD.END` | `CgPortfolio_PeriodEnd` | TField |  | This field will hold the end date of the period. Valid Date format No input, system generated field |
| 5 | `CG.CPG.LOSS.BF.YEAR` | `CgPortfolio_LossBfYear` |  |  |  |
| 6 | `CG.CPG.LT.LOSS.BF.AMT` | `CgPortfolio_LtLossBfAmt` |  |  |  |
| 7 | `CG.CPG.ST.LOSS.BF.AMT` | `CgPortfolio_StLossBfAmt` |  |  |  |
| 8 | `CG.CPG.CALCULATED.BY` | `CgPortfolio_CalculatedBy` |  |  |  |
| 9 | `CG.CPG.BF.RESERVED5` | `CgPortfolio_BfReserved5` |  |  |  |
| 10 | `CG.CPG.BF.RESERVED4` | `CgPortfolio_BfReserved4` |  |  |  |
| 11 | `CG.CPG.BF.RESERVED3` | `CgPortfolio_BfReserved3` |  |  |  |
| 12 | `CG.CPG.BF.RESERVED2` | `CgPortfolio_BfReserved2` |  |  |  |
| 13 | `CG.CPG.BF.RESERVED1` | `CgPortfolio_BfReserved1` |  |  |  |
| 14 | `CG.CPG.SEC.CCY` | `CgPortfolio_SecCcy` |  |  |  |
| 15 | `CG.CPG.LT.CG.SEC.CCY` | `CgPortfolio_LtCgSecCcy` |  |  |  |
| 16 | `CG.CPG.LT.CL.SEC.CCY` | `CgPortfolio_LtClSecCcy` |  |  |  |
| 17 | `CG.CPG.ST.CG.SEC.CCY` | `CgPortfolio_StCgSecCcy` |  |  |  |
| 18 | `CG.CPG.ST.CL.SEC.CCY` | `CgPortfolio_StClSecCcy` |  |  |  |
| 19 | `CG.CPG.INCOME.SEC.CCY` | `CgPortfolio_IncomeSecCcy` |  |  |  |
| 20 | `CG.CPG.REVENUE.SEC.CCY` | `CgPortfolio_RevenueSecCcy` |  |  |  |
| 21 | `CG.CPG.FC.RETAINED.SEC.CCY` | `CgPortfolio_FcRetainedSecCcy` |  |  |  |
| 22 | `CG.CPG.FC.LOST.SEC.CCY` | `CgPortfolio_FcLostSecCcy` |  |  |  |
| 23 | `CG.CPG.SEC.RESERVED10` | `CgPortfolio_SecReserved10` |  |  |  |
| 24 | `CG.CPG.SEC.RESERVED9` | `CgPortfolio_SecReserved9` |  |  |  |
| 25 | `CG.CPG.SEC.RESERVED8` | `CgPortfolio_SecReserved8` |  |  |  |
| 26 | `CG.CPG.SEC.RESERVED7` | `CgPortfolio_SecReserved7` |  |  |  |
| 27 | `CG.CPG.SEC.RESERVED6` | `CgPortfolio_SecReserved6` |  |  |  |
| 28 | `CG.CPG.SEC.RESERVED5` | `CgPortfolio_SecReserved5` |  |  |  |
| 29 | `CG.CPG.SEC.RESERVED4` | `CgPortfolio_SecReserved4` |  |  |  |
| 30 | `CG.CPG.SEC.RESERVED3` | `CgPortfolio_SecReserved3` |  |  |  |
| 31 | `CG.CPG.SEC.RESERVED2` | `CgPortfolio_SecReserved2` |  |  |  |
| 32 | `CG.CPG.SEC.RESERVED1` | `CgPortfolio_SecReserved1` |  |  |  |
| 33 | `CG.CPG.LT.CG.LCY` | `CgPortfolio_LtCgLcy` |  |  |  |
| 34 | `CG.CPG.LT.CL.LCY` | `CgPortfolio_LtClLcy` |  |  |  |
| 35 | `CG.CPG.ST.CG.LCY` | `CgPortfolio_StCgLcy` |  |  |  |
| 36 | `CG.CPG.ST.CL.LCY` | `CgPortfolio_StClLcy` |  |  |  |
| 37 | `CG.CPG.INCOME.LCY` | `CgPortfolio_IncomeLcy` |  |  |  |
| 38 | `CG.CPG.REVENUE.LCY` | `CgPortfolio_RevenueLcy` |  |  |  |
| 39 | `CG.CPG.FC.RETAINED.LCY` | `CgPortfolio_FcRetainedLcy` |  |  |  |
| 40 | `CG.CPG.FC.LOST.LCY` | `CgPortfolio_FcLostLcy` |  |  |  |
| 41 | `CG.CPG.LCY.RESERVED10` | `CgPortfolio_LcyReserved10` |  |  |  |
| 42 | `CG.CPG.LCY.RESERVED9` | `CgPortfolio_LcyReserved9` |  |  |  |
| 43 | `CG.CPG.LCY.RESERVED8` | `CgPortfolio_LcyReserved8` |  |  |  |
| 44 | `CG.CPG.LCY.RESERVED7` | `CgPortfolio_LcyReserved7` |  |  |  |
| 45 | `CG.CPG.LCY.RESERVED6` | `CgPortfolio_LcyReserved6` |  |  |  |
| 46 | `CG.CPG.LCY.RESERVED5` | `CgPortfolio_LcyReserved5` |  |  |  |
| 47 | `CG.CPG.LCY.RESERVED4` | `CgPortfolio_LcyReserved4` |  |  |  |
| 48 | `CG.CPG.LCY.RESERVED3` | `CgPortfolio_LcyReserved3` |  |  |  |
| 49 | `CG.CPG.LCY.RESERVED2` | `CgPortfolio_LcyReserved2` |  |  |  |
| 50 | `CG.CPG.LCY.RESERVED1` | `CgPortfolio_LcyReserved1` |  |  |  |
| 51 | `CG.CPG.RECALC.EX.RATE.SEC.LCY` | `CgPortfolio_RecalcExRateSecLcy` |  |  |  |
| 52 | `CG.CPG.TOT.LT.CG.LCY` | `CgPortfolio_TotLtCgLcy` | TField |  | This will be the sum total of all values in field LT.CG.LCY. It displays the total long term capital gains in local currency for the portfolio for the period No input, system generated field |
| 53 | `CG.CPG.TOT.LT.CL.LCY` | `CgPortfolio_TotLtClLcy` | TField |  | This will be the sum total of all values in field LT.CL.LCY. It displays the total long term capital losses in local currency for the portfolio for the period No input, system generated field |
| 54 | `CG.CPG.TOT.ST.CG.LCY` | `CgPortfolio_TotStCgLcy` | TField |  | This will be the sum total of all values in field ST.CG.LCY. It displays the total short term capital gains in local currency for the portfolio for the period No input, system generated field |
| 55 | `CG.CPG.TOT.ST.CL.LCY` | `CgPortfolio_TotStClLcy` | TField |  | This will be the sum total of all values in field ST.CL.LCY. It displays the total short term capital gains in local currency for the portfolio for the period No input, system generated field |
| 56 | `CG.CPG.TOT.INCOME.LCY` | `CgPortfolio_TotIncomeLcy` | TField |  | This will be the sum total of all values in field INCOME.LCY. It displays the total income PL in local currency for the portfolio for the period No input, system generated field |
| 57 | `CG.CPG.TOT.REVENUE.LCY` | `CgPortfolio_TotRevenueLcy` | TField |  | This will be the sum total of all values in field REVENUE.LCY. It displays the total Revenue PL in local currency for the portfolio for the period No input, system generated field |
| 58 | `CG.CPG.TOT.FC.RETAINED.LCY` | `CgPortfolio_TotFcRetainedLcy` | TField |  | This will be the sum total of all values in field FC.RETAINED.LCY It displays the total retained franking credit in local currency for the portfolio for the period No input, system generated field |
| 59 | `CG.CPG.TOT.FC.LOST.LCY` | `CgPortfolio_TotFcLostLcy` | TField |  | This will be the sum total of all values in field FC.LOST.LCY It displays the total lost franking credit in local currency for the portfolio for the period No input, system generated field |
| 60 | `CG.CPG.NET.LT.CG.LCY` | `CgPortfolio_NetLtCgLcy` | TField |  |  |
| 61 | `CG.CPG.NET.ST.CG.LCY` | `CgPortfolio_NetStCgLcy` | TField |  |  |
| 62 | `CG.CPG.LT.GAIN.LCY` | `CgPortfolio_LtGainLcy` | TField |  |  |
| 63 | `CG.CPG.ST.GAIN.LCY` | `CgPortfolio_StGainLcy` | TField |  |  |
| 64 | `CG.CPG.TOT.LT.CG.LCY.RECALC` | `CgPortfolio_TotLtCgLcyRecalc` | TField |  | This field holds the recalculated long term capital gains if an exchange rate is specified in RECALC.EX.RATE.SEC.LCY above. No input, system generated field |
| 65 | `CG.CPG.TOT.LT.CL.LCY.RECALC` | `CgPortfolio_TotLtClLcyRecalc` | TField |  | This field holds the recalculated long term capital loss if an exchange rate is specified in RECALC.EX.RATE.SEC.LCY above. No input, system generated field |
| 66 | `CG.CPG.TOT.ST.CG.LCY.RECALC` | `CgPortfolio_TotStCgLcyRecalc` | TField |  | This field holds the recalculated short term capital gains if an exchange rate is specified in RECALC.EX.RATE.SEC.LCY above. No input, system generated field |
| 67 | `CG.CPG.TOT.ST.CL.LCY.RECALC` | `CgPortfolio_TotStClLcyRecalc` | TField |  | This field holds the recalculated short term capital loss if an exchange rate is specified in RECALC.EX.RATE.SEC.LCY above. No input, system generated field |
| 68 | `CG.CPG.TOT.INCOME.LCY.RECALC` | `CgPortfolio_TotIncomeLcyRecalc` | TField |  | This field holds the recalculated income PL if an exchange rate is specified in RECALC.EX.RATE.SEC.LCY above. No input, system generated field |
| 69 | `CG.CPG.TOT.REVENUE.LCY.RECALC` | `CgPortfolio_TotRevenueLcyRecalc` | TField |  | This field holds the recalculated revenue PL if an exchange rate is specified in RECALC.EX.RATE.SEC.LCY above. No input, system generated field |
| 70 | `CG.CPG.MAX.AMT.LT.PENDING` | `CgPortfolio_MaxAmtLtPending` | TField |  | This field will hold the remaining maximum amount of long term loss that can be carried forward per yearbased on the value defined in MAX.AMT.CF.LT mentioned in CG.PARAMETER No input, system generated field |
| 71 | `CG.CPG.MAX.AMT.ST.PENDING` | `CgPortfolio_MaxAmtStPending` | TField |  | This field will hold the remaining maximum amount of short term loss that can be carried forward per yearbased on the value defined in MAX.AMT.CF.ST mentioned in CG.PARAMETER No input, system generated field |
| 72 | `CG.CPG.ANNUAL.ADJ.AMT.LT.PENDING` | `CgPortfolio_AnnualAdjAmtLtPending` | TField |  | This field holds the remaining maximum carried forward long term loss that can be adjusted in a yearbased on the value defined in ANNUAL.ADJ.AMT.LT mentioned in CG.PARAMETER No input, system generated field |
| 73 | `CG.CPG.ANNUAL.ADJ.AMT.ST.PENDING` | `CgPortfolio_AnnualAdjAmtStPending` | TField |  | This field holds remaining maximum carried forward short term loss that can be adjusted in a yearbased on the value defined in ANNUAL.ADJ.AMT.ST mentioned in CG.PARAMETER No input, system generated field |
| 74 | `CG.CPG.RESERVED1` | `CgPortfolio_Reserved1` | TField |  |  |
| 75 | `CG.CPG.RESERVED2` | `CgPortfolio_Reserved2` | TField |  |  |
| 76 | `CG.CPG.RESERVED3` | `CgPortfolio_Reserved3` | TField |  |  |
| 77 | `CG.CPG.RESERVED4` | `CgPortfolio_Reserved4` | TField |  |  |
| 78 | `CG.CPG.RESERVED5` | `CgPortfolio_Reserved5` | TField |  |  |
| 79 | `CG.CPG.RESERVED6` | `CgPortfolio_Reserved6` | TField |  |  |
| 80 | `CG.CPG.RESERVED7` | `CgPortfolio_Reserved7` | TField |  |  |
| 81 | `CG.CPG.RESERVED8` | `CgPortfolio_Reserved8` | TField |  |  |
| 82 | `CG.CPG.RESERVED9` | `CgPortfolio_Reserved9` | TField |  |  |
| 83 | `CG.CPG.RESERVED10` | `CgPortfolio_Reserved10` | TField |  |  |
| 84 | `CG.CPG.RESERVED11` | `CgPortfolio_Reserved11` | TField |  |  |
| 85 | `CG.CPG.RESERVED12` | `CgPortfolio_Reserved12` | TField |  |  |
| 86 | `CG.CPG.RESERVED13` | `CgPortfolio_Reserved13` | TField |  |  |
| 87 | `CG.CPG.RESERVED14` | `CgPortfolio_Reserved14` | TField |  |  |
| 88 | `CG.CPG.RESERVED15` | `CgPortfolio_Reserved15` | TField |  |  |
| 89 | `CG.CPG.RESERVED16` | `CgPortfolio_Reserved16` | TField |  |  |
| 90 | `CG.CPG.RESERVED17` | `CgPortfolio_Reserved17` | TField |  |  |
| 91 | `CG.CPG.RESERVED18` | `CgPortfolio_Reserved18` | TField |  |  |
| 92 | `CG.CPG.RESERVED19` | `CgPortfolio_Reserved19` | TField |  |  |
| 93 | `CG.CPG.RESERVED20` | `CgPortfolio_Reserved20` | TField |  |  |
| 94 | `CG.CPG.LOSS.CF.YEAR` | `CgPortfolio_LossCfYear` |  |  |  |
| 95 | `CG.CPG.LT.LOSS.CF.AMT` | `CgPortfolio_LtLossCfAmt` |  |  |  |
| 96 | `CG.CPG.ST.LOSS.CF.AMT` | `CgPortfolio_StLossCfAmt` |  |  |  |
| 97 | `CG.CPG.CF.RESERVED5` | `CgPortfolio_CfReserved5` |  |  |  |
| 98 | `CG.CPG.CF.RESERVED4` | `CgPortfolio_CfReserved4` |  |  |  |
| 99 | `CG.CPG.CF.RESERVED3` | `CgPortfolio_CfReserved3` |  |  |  |
| 100 | `CG.CPG.CF.RESERVED2` | `CgPortfolio_CfReserved2` |  |  |  |
| 101 | `CG.CPG.CF.RESERVED1` | `CgPortfolio_CfReserved1` |  |  |  |
