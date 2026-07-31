# TY.INTRADAY.CONCAT — Table Schema

> Source: `INSERTS/I_F.TY.INTRADAY.CONCAT` in `TY_Limits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.INT.CON.LONG.UTIL.AMT` | `TyIntradayConcat_LongUtilAmt` | TField |  | This field contains the long amount of the current incoming transaction. This amount would be moved to the LONG.UTIL.AMT field of TY.INTRADAY.LIM.CCY table. |
| 2 | `TY.INT.CON.SHORT.UTIL.AMT` | `TyIntradayConcat_ShortUtilAmt` | TField |  | This field contains the short amount of the current incoming transaction. This amount would be moved to the SHORT.UTIL.AMT field of TY.INTRADAY.LIM.CCY table. |
| 3 | `TY.INT.CON.CURRENCY` | `TyIntradayConcat_Currency` | TField |  |  |
| 4 | `TY.INT.CON.DEALER` | `TyIntradayConcat_Dealer` | TField |  |  |
| 5 | `TY.INT.CON.RESERVED.8` | `TyIntradayConcat_Reserved8` | TField |  |  |
| 6 | `TY.INT.CON.RESERVED.7` | `TyIntradayConcat_Reserved7` | TField |  |  |
| 7 | `TY.INT.CON.RESERVED.6` | `TyIntradayConcat_Reserved6` | TField |  |  |
| 8 | `TY.INT.CON.RESERVED.5` | `TyIntradayConcat_Reserved5` | TField |  |  |
| 9 | `TY.INT.CON.RESERVED.4` | `TyIntradayConcat_Reserved4` | TField |  |  |
| 10 | `TY.INT.CON.RESERVED.3` | `TyIntradayConcat_Reserved3` | TField |  |  |
| 11 | `TY.INT.CON.RESERVED.2` | `TyIntradayConcat_Reserved2` | TField |  |  |
| 12 | `TY.INT.CON.RESERVED.1` | `TyIntradayConcat_Reserved1` | TField |  |  |
| 13 | `TY.INT.CON.LOCAL.REF` | `TyIntradayConcat_LocalRef` |  |  |  |
