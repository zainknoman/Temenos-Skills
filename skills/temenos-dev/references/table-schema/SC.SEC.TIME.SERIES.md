# SC.SEC.TIME.SERIES — Table Schema

> Source: `INSERTS/I_F.SC.SEC.TIME.SERIES` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.TIM.SECURITY.NUMBER` | `ScSecTimeSeries_SecurityNumber` | TField |  | The security ( a bond-type instrument from SECURITY MASTER) for which the unit accrual and yield is calculated. |
| 2 | `SC.TIM.SECURITY.CURRENCY` | `ScSecTimeSeries_SecurityCurrency` | TField |  | The currency of the security mentioned in the previous field. |
| 3 | `SC.TIM.ISSUE.DATE` | `ScSecTimeSeries_IssueDate` | TField |  | The issue date of the security. |
| 4 | `SC.TIM.ACCRUAL.START.DATE` | `ScSecTimeSeries_AccrualStartDate` | TField |  | This field will holds the accrual start date of the security. |
| 5 | `SC.TIM.INT.PAYMENT.DATE` | `ScSecTimeSeries_IntPaymentDate` | TField |  |  |
| 6 | `SC.TIM.MATURITY.DATE` | `ScSecTimeSeries_MaturityDate` | TField |  | The maturity date of the bond is stored in this field. |
| 7 | `SC.TIM.INTEREST.DAY.BASIS` | `ScSecTimeSeries_InterestDayBasis` | TField |  |  |
| 8 | `SC.TIM.BUSINESS.DATE` | `ScSecTimeSeries_BusinessDate` |  |  |  |
| 9 | `SC.TIM.MARKET.PRICE` | `ScSecTimeSeries_MarketPrice` |  |  |  |
| 10 | `SC.TIM.INTEREST.RATE` | `ScSecTimeSeries_InterestRate` |  |  |  |
| 11 | `SC.TIM.ACCRUED.INTEREST` | `ScSecTimeSeries_AccruedInterest` |  |  |  |
| 12 | `SC.TIM.YIELD` | `ScSecTimeSeries_Yield` |  |  |  |
