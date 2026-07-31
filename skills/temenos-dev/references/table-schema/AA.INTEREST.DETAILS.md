# AA.INTEREST.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.INTEREST.DETAILS` in `AA_Interest.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.INT.DET.PAY.DATE` | `AaInterestDetails_PayDate` |  |  |  |
| 2 | `AA.INT.DET.FROM.DATE` | `AaInterestDetails_FromDate` |  |  |  |
| 3 | `AA.INT.DET.TO.DATE` | `AaInterestDetails_ToDate` |  |  |  |
| 4 | `AA.INT.DET.DAYS` | `AaInterestDetails_Days` |  |  |  |
| 5 | `AA.INT.DET.BALANCE` | `AaInterestDetails_Balance` |  |  |  |
| 6 | `AA.INT.DET.BASIS` | `AaInterestDetails_Basis` |  |  |  |
| 7 | `AA.INT.DET.RATE` | `AaInterestDetails_Rate` |  |  |  |
| 8 | `AA.INT.DET.MARGIN` | `AaInterestDetails_Margin` |  |  |  |
| 9 | `AA.INT.DET.ACCRUAL.AMT` | `AaInterestDetails_AccrualAmt` |  |  |  |
| 10 | `AA.INT.DET.ACT.ACC.AMT` | `AaInterestDetails_ActAccAmt` |  |  |  |
| 11 | `AA.INT.DET.COMPOUND.FQU` | `AaInterestDetails_CompoundFqu` |  |  |  |
| 12 | `AA.INT.DET.COMPOUND.YIELD` | `AaInterestDetails_CompoundYield` |  |  |  |
| 13 | `AA.INT.DET.LAST.ARCHIVE.DATE` | `AaInterestDetails_LastArchiveDate` | TField |  | This field represent the date when the record was last archived. |
| 14 | `AA.INT.DET.PERIOD.START` | `AaInterestDetails_PeriodStart` |  |  |  |
| 15 | `AA.INT.DET.PERIOD.END` | `AaInterestDetails_PeriodEnd` |  |  |  |
| 16 | `AA.INT.DET.TOT.ACCR.AMT` | `AaInterestDetails_TotAccrAmt` |  |  |  |
| 17 | `AA.INT.DET.TOT.SUSP.AMT` | `AaInterestDetails_TotSuspAmt` |  |  |  |
| 18 | `AA.INT.DET.RFR.FIELD.NAME` | `AaInterestDetails_RfrFieldName` |  |  |  |
| 19 | `AA.INT.DET.RFR.FIELD.VALUE` | `AaInterestDetails_RfrFieldValue` |  |  |  |
| 20 | `AA.INT.DET.SPREAD` | `AaInterestDetails_Spread` |  |  |  |
| 21 | `AA.INT.DET.SPREAD.ACCR.AMT` | `AaInterestDetails_SpreadAccrAmt` |  |  |  |
| 22 | `AA.INT.DET.SPREAD.ACCR.ACT.AMT` | `AaInterestDetails_SpreadAccrActAmt` |  |  |  |
