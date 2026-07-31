# PPL.CLIENTFXDISCOUNT — Table Schema

> Source: `INSERTS/I_F.PPL.CLIENTFXDISCOUNT` in `PP_ClientConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCFX.FXDiscountID` | `PplClientfxdiscount_Fxdiscountid` |  |  |  |
| 2 | `PPCFX.ClientConditionsID` | `PplClientfxdiscount_Clientconditionsid` |  |  |  |
| 3 | `PPCFX.TransactionCurrency` | `PplClientfxdiscount_Transactioncurrency` |  |  |  |
| 4 | `PPCFX.Discount` | `PplClientfxdiscount_Discount` |  |  |  |
