# AC.RFR.DETAILS — Table Schema

> Source: `INSERTS/I_F.AC.RFR.DETAILS` in `AC_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.RFR.FROM.DATE` | `AcRfrDetails_FromDate` |  |  |  |
| 2 | `AC.RFR.TO.DATE` | `AcRfrDetails_ToDate` |  |  |  |
| 3 | `AC.RFR.DAYS` | `AcRfrDetails_Days` |  |  |  |
| 4 | `AC.RFR.PRINCIPAL` | `AcRfrDetails_Principal` |  |  |  |
| 5 | `AC.RFR.RATE` | `AcRfrDetails_Rate` |  |  |  |
| 6 | `AC.RFR.ACT.ACCR.AMT` | `AcRfrDetails_ActAccrAmt` |  |  |  |
| 7 | `AC.RFR.ACCR.AMT` | `AcRfrDetails_AccrAmt` |  |  |  |
| 8 | `AC.RFR.INT.EFF.DATE` | `AcRfrDetails_IntEffDate` |  |  |  |
| 9 | `AC.RFR.INT.RATE` | `AcRfrDetails_IntRate` |  |  |  |
