# PPL.CLIENTCHARGESFORMULA — Table Schema

> Source: `INSERTS/I_F.PPL.CLIENTCHARGESFORMULA` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCCF.ClientChargesFeeFormulaId` | `PplClientchargesformula_Clientchargesfeeformulaid` |  |  |  |
| 2 | `PPCCF.ClientChargesFeeTypeId` | `PplClientchargesformula_Clientchargesfeetypeid` |  |  |  |
| 3 | `PPCCF.FeeTierRangeLowerLimit` | `PplClientchargesformula_Feetierrangelowerlimit` |  |  |  |
| 4 | `PPCCF.FixedChargeAmount` | `PplClientchargesformula_Fixedchargeamount` |  |  |  |
| 5 | `PPCCF.PercentageVariableFee` | `PplClientchargesformula_Percentagevariablefee` |  |  |  |
| 6 | `PPCCF.BaseChargeAmount` | `PplClientchargesformula_Basechargeamount` |  |  |  |
| 7 | `PPCCF.ChargeDiscountAmount` | `PplClientchargesformula_Chargediscountamount` |  |  |  |
| 8 | `PPCCF.ChargeRiseAmount` | `PplClientchargesformula_Chargeriseamount` |  |  |  |
| 9 | `PPCCF.MinimumChargeAmount` | `PplClientchargesformula_Minimumchargeamount` |  |  |  |
| 10 | `PPCCF.MaximumChargeAmount` | `PplClientchargesformula_Maximumchargeamount` |  |  |  |
