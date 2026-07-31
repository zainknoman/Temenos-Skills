# SL.LOAN.ACCR.DETAILS — Table Schema

> Source: `INSERTS/I_F.SL.LOAN.ACCR.DETAILS` in `SL_Interest.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SL.LN.ACCR.PART.ID` | `SlLoanAccrDetails_PartId` | TField |  | Holds the ID of the participant |
| 2 | `SL.LN.ACCR.FROM.DATE` | `SlLoanAccrDetails_FromDate` |  |  |  |
| 3 | `SL.LN.ACCR.TO.DATE` | `SlLoanAccrDetails_ToDate` |  |  |  |
| 4 | `SL.LN.ACCR.ACCR.DAYS` | `SlLoanAccrDetails_AccrDays` |  |  |  |
| 5 | `SL.LN.ACCR.BASE.AMT` | `SlLoanAccrDetails_BaseAmt` |  |  |  |
| 6 | `SL.LN.ACCR.INT.RATE` | `SlLoanAccrDetails_IntRate` |  |  |  |
| 7 | `SL.LN.ACCR.ACCR.AMT` | `SlLoanAccrDetails_AccrAmt` |  |  |  |
| 8 | `SL.LN.ACCR.ACCR.ACT.AMT` | `SlLoanAccrDetails_AccrActAmt` |  |  |  |
| 9 | `SL.LN.ACCR.PIK.REFERENCE` | `SlLoanAccrDetails_PikReference` |  |  |  |
| 10 | `SL.LN.ACCR.PIK.FROM.DT` | `SlLoanAccrDetails_PikFromDt` |  |  |  |
| 11 | `SL.LN.ACCR.PIK.TO.DT` | `SlLoanAccrDetails_PikToDt` |  |  |  |
| 12 | `SL.LN.ACCR.PIK.ACCR.DAYS` | `SlLoanAccrDetails_PikAccrDays` |  |  |  |
| 13 | `SL.LN.ACCR.PIK.BASE.AMT` | `SlLoanAccrDetails_PikBaseAmt` |  |  |  |
| 14 | `SL.LN.ACCR.PIK.INT.RATE` | `SlLoanAccrDetails_PikIntRate` |  |  |  |
| 15 | `SL.LN.ACCR.PIK.ACCR.AMT` | `SlLoanAccrDetails_PikAccrAmt` |  |  |  |
| 16 | `SL.LN.ACCR.PIK.ACCR.ACT.AMT` | `SlLoanAccrDetails_PikAccrActAmt` |  |  |  |
| 17 | `SL.LN.ACCR.SPRD.ACCR.AMT` | `SlLoanAccrDetails_SprdAccrAmt` |  |  |  |
| 18 | `SL.LN.ACCR.SPRD.ACCR.ACT.AMT` | `SlLoanAccrDetails_SprdAccrActAmt` |  |  |  |
