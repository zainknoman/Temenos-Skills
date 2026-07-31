# PPL.BANKCHARGESFEETYPE — Table Schema

> Source: `INSERTS/I_F.PPL.BANKCHARGESFEETYPE` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBCT.BankChargesFeeTypeID` | `PplBankchargesfeetype_Bankchargesfeetypeid` |  |  |  |
| 2 | `PPBCT.FeeType` | `PplBankchargesfeetype_Feetype` |  |  |  |
| 3 | `PPBCT.BankChargesID` | `PplBankchargesfeetype_Bankchargesid` |  |  |  |
| 4 | `PPBCT.Ranking` | `PplBankchargesfeetype_Ranking` |  |  |  |
| 5 | `PPBCT.AlwaysApplyFlag` | `PplBankchargesfeetype_Alwaysapplyflag` |  |  |  |
| 6 | `PPBCT.ApplyMeOnlyFlag` | `PplBankchargesfeetype_Applymeonlyflag` |  |  |  |
| 7 | `PPBCT.PercentageVATOnCharge` | `PplBankchargesfeetype_Percentagevatoncharge` |  |  |  |
