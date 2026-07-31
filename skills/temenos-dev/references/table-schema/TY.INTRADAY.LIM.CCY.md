# TY.INTRADAY.LIM.CCY — Table Schema

> Source: `INSERTS/I_F.TY.INTRADAY.LIM.CCY` in `TY_Limits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.INT.LIM.INTRADAY.LIMIT` | `TyIntradayLimCcy_IntradayLimit` | TField |  | This field contains the intraday limit for the currency. This limit amount is defaulted from the intraday amount defined in TY.POSITION.LIMITS. |
| 2 | `TY.INT.LIM.OVN.OUTSTANDING` | `TyIntradayLimCcy_OvnOutstanding` | TField |  |  |
| 3 | `TY.INT.LIM.RESERVED.13` | `TyIntradayLimCcy_Reserved13` | TField |  |  |
| 4 | `TY.INT.LIM.RESERVED.12` | `TyIntradayLimCcy_Reserved12` | TField |  |  |
| 5 | `TY.INT.LIM.RESERVED.11` | `TyIntradayLimCcy_Reserved11` | TField |  |  |
| 6 | `TY.INT.LIM.RESERVED.10` | `TyIntradayLimCcy_Reserved10` | TField |  |  |
| 7 | `TY.INT.LIM.RESERVED.9` | `TyIntradayLimCcy_Reserved9` | TField |  |  |
| 8 | `TY.INT.LIM.RESERVED.8` | `TyIntradayLimCcy_Reserved8` | TField |  |  |
| 9 | `TY.INT.LIM.RESERVED.7` | `TyIntradayLimCcy_Reserved7` | TField |  |  |
| 10 | `TY.INT.LIM.RESERVED.6` | `TyIntradayLimCcy_Reserved6` | TField |  |  |
| 11 | `TY.INT.LIM.RESERVED.5` | `TyIntradayLimCcy_Reserved5` | TField |  |  |
| 12 | `TY.INT.LIM.RESERVED.4` | `TyIntradayLimCcy_Reserved4` | TField |  |  |
| 13 | `TY.INT.LIM.RESERVED.3` | `TyIntradayLimCcy_Reserved3` | TField |  |  |
| 14 | `TY.INT.LIM.RESERVED.2` | `TyIntradayLimCcy_Reserved2` | TField |  |  |
| 15 | `TY.INT.LIM.RESERVED.1` | `TyIntradayLimCcy_Reserved1` | TField |  |  |
| 16 | `TY.INT.LIM.LOCAL.REF` | `TyIntradayLimCcy_LocalRef` |  |  |  |
