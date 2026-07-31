# CAMB.L.SL.REPAY.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAMB.L.SL.REPAY.DETAILS` in `CASYLN_SyndicatedLending.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.L.SL.REPAY.DETAILS.PRIN.AMT` | `CambLSlRepayDetails_PrinAmt` |  |  |  |
| 2 | `CAMB.L.SL.REPAY.DETAILS.INT.AMT` | `CambLSlRepayDetails_IntAmt` |  |  |  |
| 3 | `CAMB.L.SL.REPAY.DETAILS.AA.ACTIVITY` | `CambLSlRepayDetails_AaActivity` |  |  |  |
| 4 | `CAMB.L.SL.REPAY.DETAILS.CURR.PRIN.AMT` | `CambLSlRepayDetails_CurrPrinAmt` |  |  |  |
| 5 | `CAMB.L.SL.REPAY.DETAILS.CURR.INT.AMT` | `CambLSlRepayDetails_CurrIntAmt` |  |  |  |
| 6 | `CAMB.L.SL.REPAY.DETAILS.ACT.REF` | `CambLSlRepayDetails_ActRef` |  |  |  |
