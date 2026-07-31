# ST.RFR.DETAILS — Table Schema

> Source: `INSERTS/I_F.ST.RFR.DETAILS` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SRD.INTEREST.DATE` | `StRfrDetails_InterestDate` |  |  |  |
| 2 | `SRD.RATE.DATE` | `StRfrDetails_RateDate` |  |  |  |
| 3 | `SRD.DAILY.RFR` | `StRfrDetails_DailyRfr` |  |  |  |
| 4 | `SRD.DAY.COUNT` | `StRfrDetails_DayCount` |  |  |  |
| 5 | `SRD.MARGIN` | `StRfrDetails_Margin` |  |  |  |
| 6 | `SRD.DAILY.RATE` | `StRfrDetails_DailyRate` |  |  |  |
| 7 | `SRD.RFR.RATE` | `StRfrDetails_RfrRate` |  |  |  |
| 8 | `SRD.UCR` | `StRfrDetails_Ucr` |  |  |  |
| 9 | `SRD.NCCR` | `StRfrDetails_Nccr` |  |  |  |
| 10 | `SRD.PRINCIPAL` | `StRfrDetails_Principal` |  |  |  |
| 11 | `SRD.NOTIONAL.PRINCIPAL` | `StRfrDetails_NotionalPrincipal` |  |  |  |
| 12 | `SRD.BASE.RATE.ACCRUAL` | `StRfrDetails_BaseRateAccrual` |  |  |  |
| 13 | `SRD.SPREAD.ACCRUAL` | `StRfrDetails_SpreadAccrual` |  |  |  |
| 14 | `SRD.DAILY.ACCRUAL` | `StRfrDetails_DailyAccrual` |  |  |  |
| 15 | `SRD.CUMULATIVE.ACCRUAL` | `StRfrDetails_CumulativeAccrual` |  |  |  |
