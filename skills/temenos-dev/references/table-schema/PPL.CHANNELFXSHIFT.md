# PPL.CHANNELFXSHIFT — Table Schema

> Source: `INSERTS/I_F.PPL.CHANNELFXSHIFT` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPLCFS.ChannelCutoffID` | `PplChannelfxshift_Channelcutoffid` |  |  |  |
| 2 | `PPLCFS.CurrencyCode` | `PplChannelfxshift_Currencycode` |  |  |  |
| 3 | `PPLCFS.FXShift` | `PplChannelfxshift_Fxshift` |  |  |  |
| 4 | `PPLCFS.CutoffTimeWithFX` | `PplChannelfxshift_Cutofftimewithfx` |  |  |  |
