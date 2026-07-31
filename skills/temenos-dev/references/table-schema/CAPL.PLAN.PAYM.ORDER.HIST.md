# CAPL.PLAN.PAYM.ORDER.HIST — Table Schema

> Source: `INSERTS/I_F.CAPL.PLAN.PAYM.ORDER.HIST` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.PAYM.ODR.HIS.ACCOUNT` | `CaplPlanPaymOrderHist_Account` |  |  |  |
| 2 | `CP.PAYM.ODR.HIS.BAL` | `CaplPlanPaymOrderHist_Bal` |  |  |  |
| 3 | `CP.PAYM.ODR.HIS.INT.RATE` | `CaplPlanPaymOrderHist_IntRate` |  |  |  |
| 4 | `CP.PAYM.ODR.HIS.INT.ACCR` | `CaplPlanPaymOrderHist_IntAccr` |  |  |  |
| 5 | `CP.PAYM.ODR.HIS.TOT.AVAIL.BAL` | `CaplPlanPaymOrderHist_TotAvailBal` |  |  |  |
