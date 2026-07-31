# PD.RFR.DETAILS — Table Schema

> Source: `INSERTS/I_F.PD.RFR.DETAILS` in `PD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRD.INTEREST.DATE` | `PdRfrDetails_InterestDate` |  |  |  |
| 2 | `PRD.RATE.DATE` | `PdRfrDetails_RateDate` |  |  |  |
| 3 | `PRD.DAILY.RFR` | `PdRfrDetails_DailyRfr` |  |  |  |
| 4 | `PRD.DAY.COUNT` | `PdRfrDetails_DayCount` |  |  |  |
| 5 | `PRD.CAS.VALUE` | `PdRfrDetails_CasValue` |  |  |  |
| 6 | `PRD.LOAN.MARGIN` | `PdRfrDetails_LoanMargin` |  |  |  |
| 7 | `PRD.PD.MARGIN.RATE` | `PdRfrDetails_PdMarginRate` |  |  |  |
| 8 | `PRD.PENALTY.RATE` | `PdRfrDetails_PenaltyRate` |  |  |  |
| 9 | `PRD.PENALTY.SPREAD` | `PdRfrDetails_PenaltySpread` |  |  |  |
| 10 | `PRD.UCR.RATE` | `PdRfrDetails_UcrRate` |  |  |  |
| 11 | `PRD.APPLICABLE.RATE` | `PdRfrDetails_ApplicableRate` |  |  |  |
| 12 | `PRD.ACR.RATE` | `PdRfrDetails_AcrRate` |  |  |  |
| 13 | `PRD.RESERVED.13` | `PdRfrDetails_Reserved13` |  |  |  |
| 14 | `PRD.RESERVED.12` | `PdRfrDetails_Reserved12` |  |  |  |
| 15 | `PRD.RESERVED.11` | `PdRfrDetails_Reserved11` |  |  |  |
| 16 | `PRD.PRINCIPAL.DUE` | `PdRfrDetails_PrincipalDue` |  |  |  |
| 17 | `PRD.IN.DUE` | `PdRfrDetails_InDue` |  |  |  |
| 18 | `PRD.CE.AMT` | `PdRfrDetails_CeAmt` |  |  |  |
| 19 | `PRD.CS.AMT` | `PdRfrDetails_CsAmt` |  |  |  |
| 20 | `PRD.OTHER.DUE` | `PdRfrDetails_OtherDue` |  |  |  |
| 21 | `PRD.BASE.AMT.1` | `PdRfrDetails_BaseAmt1` |  |  |  |
| 22 | `PRD.ACCR.AMT.1` | `PdRfrDetails_AccrAmt1` |  |  |  |
| 23 | `PRD.RESERVED.10` | `PdRfrDetails_Reserved10` |  |  |  |
| 24 | `PRD.RESERVED.9` | `PdRfrDetails_Reserved9` |  |  |  |
| 25 | `PRD.RESERVED.8` | `PdRfrDetails_Reserved8` |  |  |  |
| 26 | `PRD.RESERVED.7` | `PdRfrDetails_Reserved7` |  |  |  |
| 27 | `PRD.BASE.AMT.2` | `PdRfrDetails_BaseAmt2` |  |  |  |
| 28 | `PRD.ACCR.AMT.2` | `PdRfrDetails_AccrAmt2` |  |  |  |
| 29 | `PRD.RESERVED.6` | `PdRfrDetails_Reserved6` |  |  |  |
| 30 | `PRD.RESERVED.5` | `PdRfrDetails_Reserved5` |  |  |  |
| 31 | `PRD.RESERVED.4` | `PdRfrDetails_Reserved4` |  |  |  |
| 32 | `PRD.RESERVED.3` | `PdRfrDetails_Reserved3` |  |  |  |
| 33 | `PRD.DAILY.ACCRUAL` | `PdRfrDetails_DailyAccrual` |  |  |  |
| 34 | `PRD.CUMULATIVE.ACCRUAL` | `PdRfrDetails_CumulativeAccrual` |  |  |  |
| 35 | `PRD.TOTAL.DUE` | `PdRfrDetails_TotalDue` |  |  |  |
| 36 | `PRD.RESERVED.2` | `PdRfrDetails_Reserved2` |  |  |  |
| 37 | `PRD.RESERVED.1` | `PdRfrDetails_Reserved1` |  |  |  |
