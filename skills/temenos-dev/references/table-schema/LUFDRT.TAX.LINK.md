# LUFDRT.TAX.LINK — Table Schema

> Source: `INSERTS/I_F.LUFDRT.TAX.LINK` in `LUFDRT_FdrTaxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LUFTAX.TRADE.ID` | `LufdrtTaxLink_TradeId` |  |  |  |
| 2 | `LUFTAX.TRADE.DATE` | `LufdrtTaxLink_TradeDate` |  |  |  |
| 3 | `LUFTAX.ACTUAL.NOMINAL` | `LufdrtTaxLink_ActualNominal` |  |  |  |
| 4 | `LUFTAX.UTILISED.NOMINAL` | `LufdrtTaxLink_UtilisedNominal` |  |  |  |
| 5 | `LUFTAX.DISC.COUNTER` | `LufdrtTaxLink_DiscCounter` |  |  |  |
