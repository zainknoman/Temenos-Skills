# LI.RESTRICTION.LIMIT.LIST — Table Schema

> Source: `INSERTS/I_F.LI.RESTRICTION.LIMIT.LIST` in `LI_RestrictionLimit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.RSTL.OLD.CONTEXT.NAME` | `LiRestrictionLimitList_OldContextName` |  |  |  |
| 2 | `LI.RSTL.OLD.CONTEXT.VALUE` | `LiRestrictionLimitList_OldContextValue` |  |  |  |
| 3 | `LI.RSTL.NEW.CONTEXT.NAME` | `LiRestrictionLimitList_NewContextName` |  |  |  |
| 4 | `LI.RSTL.NEW.CONTEXT.VALUE` | `LiRestrictionLimitList_NewContextValue` |  |  |  |
| 5 | `LI.RSTL.OTHER.DETAILS` | `LiRestrictionLimitList_OtherDetails` |  |  |  |
