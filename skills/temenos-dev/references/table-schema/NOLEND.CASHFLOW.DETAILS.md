# NOLEND.CASHFLOW.DETAILS — Table Schema

> Source: `INSERTS/I_F.NOLEND.CASHFLOW.DETAILS` in `NOLEND_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NOLEND.CASHFLOW.CASE.NO` | `NolendCashflowDetails_CaseNo` | TField |  | Specifies the account number. |
| 2 | `NOLEND.CASHFLOW.AGREEMENT.CURRENCY` | `NolendCashflowDetails_AgreementCurrency` | TField |  | Specifies the account currency. |
| 3 | `NOLEND.CASHFLOW.RESIDUAL.DEBT` | `NolendCashflowDetails_ResidualDebt` | TField |  | Specifies the current loan outstanding. |
| 4 | `NOLEND.CASHFLOW.AGREEMENT.NAME` | `NolendCashflowDetails_AgreementName` | TField |  | Specifies the current periodic interest rate description. |
| 5 | `NOLEND.CASHFLOW.AGREEMENT.START.DATE` | `NolendCashflowDetails_AgreementStartDate` | TField |  | Specifies the loan creation date. |
| 6 | `NOLEND.CASHFLOW.AGREEMENT.END.DATE` | `NolendCashflowDetails_AgreementEndDate` | TField |  | Specifies the fixed interest rate agreement period. |
| 7 | `NOLEND.CASHFLOW.AGREED.INTEREST.RATE` | `NolendCashflowDetails_AgreedInterestRate` | TField |  | Specifies the current loan principal interest rate. |
| 8 | `NOLEND.CASHFLOW.FRA.BREACHED.ON` | `NolendCashflowDetails_RedemptionDate` |  |  |  |
| 9 | `NOLEND.CASHFLOW.REMAINING.DURATION` | `NolendCashflowDetails_RemainingDuration` | TField |  | Specifies arrangement remaining duration. |
| 10 | `NOLEND.CASHFLOW.LONG.OFFER.DURATION` | `NolendCashflowDetails_LongOfferDuration` | TField |  | Specifies the longer duration period. |
| 11 | `NOLEND.CASHFLOW.SHORT.OFFER.DURATION` | `NolendCashflowDetails_ShortOfferDuration` | TField |  | Specifies the shorter duration period. |
| 12 | `NOLEND.CASHFLOW.LONG.INTEREST.RATE` | `NolendCashflowDetails_LongInterestRate` | TField |  | Specifies the longer duration interest rate. |
| 13 | `NOLEND.CASHFLOW.SHORT.INTEREST.RATE` | `NolendCashflowDetails_ShortInterestRate` | TField |  | Specifies the shorter duration interest rate. |
| 14 | `NOLEND.CASHFLOW.WEIGHTED.AVERAGE` | `NolendCashflowDetails_WeightedAverage` | TField |  | Specifies the calculated eighted average. |
| 15 | `NOLEND.CASHFLOW.INTEREST.DIFFERENCE` | `NolendCashflowDetails_InterestDifference` | TField |  | Specifies the calculated interest difference. |
| 16 | `NOLEND.CASHFLOW.DISCOUNT.RATE` | `NolendCashflowDetails_DiscountRate` | TField |  | Specifies the calculated discount rate. |
| 17 | `NOLEND.CASHFLOW.DUE.DATE` | `NolendCashflowDetails_DueDate` |  |  |  |
| 18 | `NOLEND.CASHFLOW.BALANCE` | `NolendCashflowDetails_Balance` |  |  |  |
| 19 | `NOLEND.CASHFLOW.NPV` | `NolendCashflowDetails_Npv` |  |  |  |
| 20 | `NOLEND.CASHFLOW.DIFFERENCE` | `NolendCashflowDetails_Difference` |  |  |  |
| 21 | `NOLEND.CASHFLOW.PREMIUM.OR.DISCOUNT` | `NolendCashflowDetails_PremiumOrDiscount` | TField |  |  |
| 22 | `NOLEND.CASHFLOW.LOCAL.REF` | `NolendCashflowDetails_LocalRef` |  |  |  |
| 23 | `NOLEND.CASHFLOW.ACTIVITY` | `NolendCashflowDetails_Activity` | TField |  | Specifies the activity for which Premium/Discount is calculated |
| 24 | `NOLEND.CASHFLOW.ACTIVITY.ID` | `NolendCashflowDetails_ActivityId` | TField |  | Specifies the activity Id. |
| 25 | `NOLEND.CASHFLOW.NPV.ADJUSTMENT.FIRST` | `NolendCashflowDetails_NpvAdjustmentFirst` | TField |  | Specifies the NPV Adjustment till Next Due Date. |
| 26 | `NOLEND.CASHFLOW.NPV.ADJUSTMENT.FINAL` | `NolendCashflowDetails_NpvAdjustmentFinal` | TField |  | Specifies the NPV adjustment Per Full Installment. |
| 27 | `NOLEND.CASHFLOW.FRA.END.DATE` | `NolendCashflowDetails_FraEndDate` | TField |  | Specifies the fixed rate arrangement date. |
