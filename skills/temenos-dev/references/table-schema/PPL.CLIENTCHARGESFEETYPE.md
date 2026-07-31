# PPL.CLIENTCHARGESFEETYPE — Table Schema

> Source: `INSERTS/I_F.PPL.CLIENTCHARGESFEETYPE` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCCT.ClientChargesFeeTypeId` | `PplClientchargesfeetype_Clientchargesfeetypeid` |  |  |  |
| 2 | `PPCCT.ClientChargesID` | `PplClientchargesfeetype_Clientchargesid` |  |  |  |
| 3 | `PPCCT.FeeType` | `PplClientchargesfeetype_Feetype` |  |  |  |
| 4 | `PPCCT.Ranking` | `PplClientchargesfeetype_Ranking` |  |  |  |
| 5 | `PPCCT.AlwaysApplyFlag` | `PplClientchargesfeetype_Alwaysapplyflag` |  |  |  |
| 6 | `PPCCT.ApplyMeOnlyFlag` | `PplClientchargesfeetype_Applymeonlyflag` |  |  |  |
| 7 | `PPCCT.PercentageVATOnCharge` | `PplClientchargesfeetype_Percentagevatoncharge` |  |  |  |
