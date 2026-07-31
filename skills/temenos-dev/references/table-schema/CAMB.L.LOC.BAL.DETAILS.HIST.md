# CAMB.L.LOC.BAL.DETAILS.HIST — Table Schema

> Source: `INSERTS/I_F.CAMB.L.LOC.BAL.DETAILS.HIST` in `CALOCR_LineOfCredit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.LOC.BAL.CAPITALISATION.DT` | `CambLLocBalDetailsHist_CapitalisationDt` |  |  |  |
| 2 | `CAMB.LOC.BAL.DUE.BALANCE` | `CambLLocBalDetailsHist_DueBalance` |  |  |  |
| 3 | `CAMB.LOC.BAL.PAST.DUE` | `CambLLocBalDetailsHist_PastDue` |  |  |  |
| 4 | `CAMB.LOC.BAL.LAST.CR.ACTIVITY` | `CambLLocBalDetailsHist_LastCrActivity` |  |  |  |
| 5 | `CAMB.LOC.BAL.TRANSACTION.AMT` | `CambLLocBalDetailsHist_TransactionAmt` |  |  |  |
| 6 | `CAMB.LOC.BAL.TOTAL.OS.DUE.AMT` | `CambLLocBalDetailsHist_TotalOsDueAmt` |  |  |  |
| 7 | `CAMB.LOC.BAL.AMOUNT.PAID` | `CambLLocBalDetailsHist_AmountPaid` |  |  |  |
| 8 | `CAMB.LOC.BAL.LAST.PAY.DATE` | `CambLLocBalDetailsHist_LastPayDate` |  |  |  |
| 9 | `CAMB.LOC.BAL.ACCT.BALANCE` | `CambLLocBalDetailsHist_AcctBalance` |  |  |  |
