# PPL.BANKCHARGESFORMULA — Table Schema

> Source: `INSERTS/I_F.PPL.BANKCHARGESFORMULA` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBCF.BankChargesFeeFormulaId` | `PplBankchargesformula_Bankchargesfeeformulaid` |  |  |  |
| 2 | `PPBCF.BankChargesFeeTypeID` | `PplBankchargesformula_Bankchargesfeetypeid` |  |  |  |
| 3 | `PPBCF.FeeTierRangeLowerLimit` | `PplBankchargesformula_Feetierrangelowerlimit` |  |  |  |
| 4 | `PPBCF.FixedChargeAmount` | `PplBankchargesformula_Fixedchargeamount` |  |  |  |
| 5 | `PPBCF.PercentageVariableFee` | `PplBankchargesformula_Percentagevariablefee` |  |  |  |
| 6 | `PPBCF.BaseChargeAmount` | `PplBankchargesformula_Basechargeamount` |  |  |  |
| 7 | `PPBCF.ChargeDiscountAmount` | `PplBankchargesformula_Chargediscountamount` |  |  |  |
| 8 | `PPBCF.ChargeRiseAmount` | `PplBankchargesformula_Chargeriseamount` |  |  |  |
| 9 | `PPBCF.MinimumChargeAmount` | `PplBankchargesformula_Minimumchargeamount` |  |  |  |
| 10 | `PPBCF.MaximumChargeAmount` | `PplBankchargesformula_Maximumchargeamount` |  |  |  |
