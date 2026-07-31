# SC.HIST.VAL.UPDATE — Table Schema

> Source: `INSERTS/I_F.SC.HIST.VAL.UPDATE` in `SC_ScvValuationUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.HIS.SECURITY.CODE` | `ScHistValUpdate_SecurityCode` |  |  |  |
| 2 | `SC.HIS.MARKET.PRICE` | `ScHistValUpdate_MarketPrice` |  |  |  |
| 3 | `SC.HIS.START.DATE` | `ScHistValUpdate_StartDate` |  |  |  |
| 4 | `SC.HIS.END.DATE` | `ScHistValUpdate_EndDate` |  |  |  |
