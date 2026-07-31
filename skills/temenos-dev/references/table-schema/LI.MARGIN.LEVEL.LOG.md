# LI.MARGIN.LEVEL.LOG — Table Schema

> Source: `INSERTS/I_F.LI.MARGIN.LEVEL.LOG` in `LI_Collateral.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.MLL.CURRENCY` | `LiMarginLevelLog_Currency` | TField |  |  |
| 2 | `LI.MLL.EVENT` | `LiMarginLevelLog_Event` | TField |  |  |
| 3 | `LI.MLL.EVENT.PERCENT` | `LiMarginLevelLog_EventPercent` | TField |  |  |
| 4 | `LI.MLL.LIMIT.AMOUNT` | `LiMarginLevelLog_LimitAmount` | TField |  |  |
| 5 | `LI.MLL.SECURED.AMOUNT` | `LiMarginLevelLog_SecuredAmount` | TField |  |  |
| 6 | `LI.MLL.DATE.TIME.STAMP` | `LiMarginLevelLog_DateTimeStamp` | TField |  |  |
| 7 | `LI.MLL.PREV.EVENT` | `LiMarginLevelLog_PrevEvent` | TField |  |  |
| 8 | `LI.MLL.PREV.EVENT.PERCENT` | `LiMarginLevelLog_PrevEventPercent` | TField |  |  |
| 9 | `LI.MLL.PREV.LIMIT.AMOUNT` | `LiMarginLevelLog_PrevLimitAmount` | TField |  |  |
| 10 | `LI.MLL.PREV.SECURED.AMOUNT` | `LiMarginLevelLog_PrevSecuredAmount` | TField |  |  |
| 11 | `LI.MLL.PREV.DATE.TIME` | `LiMarginLevelLog_PrevDateTime` |  |  |  |
