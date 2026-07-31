# ST.RFR.DETAILS.HIST — Table Schema

> Source: `INSERTS/I_F.ST.RFR.DETAILS.HIST` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SRDH.INTEREST.DATE` | `StRfrDetailsHist_InterestDate` |  |  |  |
| 2 | `SRDH.RATE.DATE` | `StRfrDetailsHist_RateDate` |  |  |  |
| 3 | `SRDH.DAILY.RFR` | `StRfrDetailsHist_DailyRfr` |  |  |  |
| 4 | `SRDH.DAY.COUNT` | `StRfrDetailsHist_DayCount` |  |  |  |
| 5 | `SRDH.MARGIN` | `StRfrDetailsHist_Margin` |  |  |  |
| 6 | `SRDH.DAILY.RATE` | `StRfrDetailsHist_DailyRate` |  |  |  |
| 7 | `SRDH.RFR.RATE` | `StRfrDetailsHist_RfrRate` |  |  |  |
| 8 | `SRDH.UCR` | `StRfrDetailsHist_Ucr` |  |  |  |
| 9 | `SRDH.NCCR` | `StRfrDetailsHist_Nccr` |  |  |  |
| 10 | `SRDH.PRINCIPAL` | `StRfrDetailsHist_Principal` |  |  |  |
| 11 | `SRDH.NOTIONAL.PRINCIPAL` | `StRfrDetailsHist_NotionalPrincipal` |  |  |  |
| 12 | `SRDH.BASE.RATE.ACCRUAL` | `StRfrDetailsHist_BaseRateAccrual` |  |  |  |
| 13 | `SRDH.SPREAD.ACCRUAL` | `StRfrDetailsHist_SpreadAccrual` |  |  |  |
| 14 | `SRDH.DAILY.ACCRUAL` | `StRfrDetailsHist_DailyAccrual` |  |  |  |
| 15 | `SRDH.CUMULATIVE.ACCRUAL` | `StRfrDetailsHist_CumulativeAccrual` |  |  |  |
