# PD.RFR.DETAILS.HIST — Table Schema

> Source: `INSERTS/I_F.PD.RFR.DETAILS.HIST` in `PD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRDH.INTEREST.DATE` | `PdRfrDetailsHist_InterestDate` |  |  |  |
| 2 | `PRDH.RATE.DATE` | `PdRfrDetailsHist_RateDate` |  |  |  |
| 3 | `PRDH.DAILY.RFR` | `PdRfrDetailsHist_DailyRfr` |  |  |  |
| 4 | `PRDH.DAY.COUNT` | `PdRfrDetailsHist_DayCount` |  |  |  |
| 5 | `PRDH.CAS.VALUE` | `PdRfrDetailsHist_CasValue` |  |  |  |
| 6 | `PRDH.LOAN.MARGIN` | `PdRfrDetailsHist_LoanMargin` |  |  |  |
| 7 | `PRDH.PD.MARGIN.RATE` | `PdRfrDetailsHist_PdMarginRate` |  |  |  |
| 8 | `PRDH.PENALTY.RATE` | `PdRfrDetailsHist_PenaltyRate` |  |  |  |
| 9 | `PRDH.PENALTY.SPREAD` | `PdRfrDetailsHist_PenaltySpread` |  |  |  |
| 10 | `PRDH.UCR.RATE` | `PdRfrDetailsHist_UcrRate` |  |  |  |
| 11 | `PRDH.APPLICABLE.RATE` | `PdRfrDetailsHist_ApplicableRate` |  |  |  |
| 12 | `PRDH.ACR.RATE` | `PdRfrDetailsHist_AcrRate` |  |  |  |
| 13 | `PRDH.RESERVED.13` | `PdRfrDetailsHist_Reserved13` |  |  |  |
| 14 | `PRDH.RESERVED.12` | `PdRfrDetailsHist_Reserved12` |  |  |  |
| 15 | `PRDH.RESERVED.11` | `PdRfrDetailsHist_Reserved11` |  |  |  |
| 16 | `PRDH.PRINCIPAL.DUE` | `PdRfrDetailsHist_PrincipalDue` |  |  |  |
| 17 | `PRDH.IN.DUE` | `PdRfrDetailsHist_InDue` |  |  |  |
| 18 | `PRDH.CE.AMT` | `PdRfrDetailsHist_CeAmt` |  |  |  |
| 19 | `PRDH.CS.AMT` | `PdRfrDetailsHist_CsAmt` |  |  |  |
| 20 | `PRDH.OTHER.DUE` | `PdRfrDetailsHist_OtherDue` |  |  |  |
| 21 | `PRDH.BASE.AMT.1` | `PdRfrDetailsHist_BaseAmt1` |  |  |  |
| 22 | `PRDH.ACCR.AMT.1` | `PdRfrDetailsHist_AccrAmt1` |  |  |  |
| 23 | `PRDH.RESERVED.10` | `PdRfrDetailsHist_Reserved10` |  |  |  |
| 24 | `PRDH.RESERVED.9` | `PdRfrDetailsHist_Reserved9` |  |  |  |
| 25 | `PRDH.RESERVED.8` | `PdRfrDetailsHist_Reserved8` |  |  |  |
| 26 | `PRDH.RESERVED.7` | `PdRfrDetailsHist_Reserved7` |  |  |  |
| 27 | `PRDH.BASE.AMT.2` | `PdRfrDetailsHist_BaseAmt2` |  |  |  |
| 28 | `PRDH.ACCR.AMT.2` | `PdRfrDetailsHist_AccrAmt2` |  |  |  |
| 29 | `PRDH.RESERVED.6` | `PdRfrDetailsHist_Reserved6` |  |  |  |
| 30 | `PRDH.RESERVED.5` | `PdRfrDetailsHist_Reserved5` |  |  |  |
| 31 | `PRDH.RESERVED.4` | `PdRfrDetailsHist_Reserved4` |  |  |  |
| 32 | `PRDH.RESERVED.3` | `PdRfrDetailsHist_Reserved3` |  |  |  |
| 33 | `PRDH.DAILY.ACCRUAL` | `PdRfrDetailsHist_DailyAccrual` |  |  |  |
| 34 | `PRDH.CUMULATIVE.ACCRUAL` | `PdRfrDetailsHist_CumulativeAccrual` |  |  |  |
| 35 | `PRDH.TOTAL.DUE` | `PdRfrDetailsHist_TotalDue` |  |  |  |
| 36 | `PRDH.RESERVED.2` | `PdRfrDetailsHist_Reserved2` |  |  |  |
| 37 | `PRDH.RESERVED.1` | `PdRfrDetailsHist_Reserved1` |  |  |  |
