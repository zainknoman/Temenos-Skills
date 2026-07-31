# PPT.RISKFILTEROUTPUT — Table Schema

> Source: `INSERTS/I_F.PPT.RISKFILTEROUTPUT` in `PP_RiskFilterService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPRFO.CompanyID` | `PptRiskfilteroutput_Companyid` |  |  |  |
| 2 | `PPRFO.FTNumber` | `PptRiskfilteroutput_Ftnumber` |  |  |  |
| 3 | `PPRFO.FilterID` | `PptRiskfilteroutput_Filterid` |  |  |  |
| 4 | `PPRFO.TransactionAmountLimit` | `PptRiskfilteroutput_Transactionamountlimit` |  |  |  |
| 5 | `PPRFO.TRNLimitBreach` | `PptRiskfilteroutput_Trnlimitbreach` |  |  |  |
| 6 | `PPRFO.DailyAmountLimit` | `PptRiskfilteroutput_Dailyamountlimit` |  |  |  |
| 7 | `PPRFO.DailyLimitBreach` | `PptRiskfilteroutput_Dailylimitbreach` |  |  |  |
| 8 | `PPRFO.WeeklyAmountLimit` | `PptRiskfilteroutput_Weeklyamountlimit` |  |  |  |
| 9 | `PPRFO.WeeklyLimitBreach` | `PptRiskfilteroutput_Weeklylimitbreach` |  |  |  |
| 10 | `PPRFO.MonthlyAmountLimit` | `PptRiskfilteroutput_Monthlyamountlimit` |  |  |  |
| 11 | `PPRFO.MonthlyLimitBreach` | `PptRiskfilteroutput_Monthlylimitbreach` |  |  |  |
| 12 | `PPRFO.PaymentsPerDay` | `PptRiskfilteroutput_Paymentsperday` |  |  |  |
| 13 | `PPRFO.PPDLimitBreach` | `PptRiskfilteroutput_Ppdlimitbreach` |  |  |  |
| 14 | `PPRFO.PaymentsPerWeek` | `PptRiskfilteroutput_Paymentsperweek` |  |  |  |
| 15 | `PPRFO.PPWLimitBreach` | `PptRiskfilteroutput_Ppwlimitbreach` |  |  |  |
| 16 | `PPRFO.PaymentsPerMonth` | `PptRiskfilteroutput_Paymentspermonth` |  |  |  |
| 17 | `PPRFO.PPMLimitBreach` | `PptRiskfilteroutput_Ppmlimitbreach` |  |  |  |
