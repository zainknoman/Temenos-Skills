# LI.RESTRICTION.LIMITS — Table Schema

> Source: `INSERTS/I_F.LI.RESTRICTION.LIMITS` in `LI_RestrictionLimit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.RST.CONTEXT.NAME` | `LiRestrictionLimits_ContextName` |  |  |  |
| 2 | `LI.RST.RESTRICTION.LIMIT.ID` | `LiRestrictionLimits_RestrictionLimitId` |  |  |  |
| 3 | `LI.RST.EXPIRY.DATE` | `LiRestrictionLimits_ExpiryDate` |  |  |  |
| 4 | `LI.RST.CONTEXT.VALUE` | `LiRestrictionLimits_ContextValue` |  |  |  |
| 5 | `LI.RST.CONTEXT.ARRAY` | `LiRestrictionLimits_ContextArray` |  |  |  |
| 6 | `LI.RST.CHECK.LIMIT` | `LiRestrictionLimits_CheckLimit` |  |  |  |
