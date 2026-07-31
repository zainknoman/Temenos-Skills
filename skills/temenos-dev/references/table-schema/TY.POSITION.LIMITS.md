# TY.POSITION.LIMITS — Table Schema

> Source: `INSERTS/I_F.TY.POSITION.LIMITS` in `TY_Limits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.POS.LIM.DESCRIPTION` | `TyPositionLimits_Description` |  |  |  |
| 2 | `TY.POS.LIM.LIMIT.CCY` | `TyPositionLimits_LimitCcy` |  |  |  |
| 3 | `TY.POS.LIM.INTRADAY.LIM.AMT` | `TyPositionLimits_IntradayLimAmt` |  |  |  |
| 4 | `TY.POS.LIM.OVN.LIMIT.AMT` | `TyPositionLimits_OvnLimitAmt` |  |  |  |
| 5 | `TY.POS.LIM.OVN.LIMIT.UTIL` | `TyPositionLimits_OvnLimitUtil` |  |  |  |
| 6 | `TY.POS.LIM.OVN.TIME.BAND` | `TyPositionLimits_OvnTimeBand` |  |  |  |
| 7 | `TY.POS.LIM.OVN.TB.LIMIT.AMT` | `TyPositionLimits_OvnTbLimitAmt` |  |  |  |
| 8 | `TY.POS.LIM.OVN.TB.LIMIT.UTIL` | `TyPositionLimits_OvnTbLimitUtil` |  |  |  |
| 9 | `TY.POS.LIM.RESERVED.20` | `TyPositionLimits_Reserved20` |  |  |  |
| 10 | `TY.POS.LIM.RESERVED.19` | `TyPositionLimits_Reserved19` |  |  |  |
| 11 | `TY.POS.LIM.RESERVED.18` | `TyPositionLimits_Reserved18` |  |  |  |
| 12 | `TY.POS.LIM.RESERVED.17` | `TyPositionLimits_Reserved17` |  |  |  |
| 13 | `TY.POS.LIM.RESERVED.16` | `TyPositionLimits_Reserved16` |  |  |  |
| 14 | `TY.POS.LIM.AGG.LIM.CCY` | `TyPositionLimits_AggLimCcy` | TField |  | An user defined field that contains the common currency in which the limits are to be monitored. The transaction amounts of all transactions would be converted into this common currency and be validated against the defined limit amount. Validations: Should be defined only at company level and cannot be defined at dealer level. Should be a valid currency. |
| 15 | `TY.POS.LIM.AGG.INTRA.LIM.AMT` | `TyPositionLimits_AggIntraLimAmt` | TField | Yes | An user defined field that contains the intraday limit amount for the aggregate(common) currency. This amount is automatically assigned to the respective TY.INTRADAY.LIM.CCY record when TY.POSITIONS.LIMITS is authorized. The intraday position during a deal capture would be validated against the amount defined here and in case of a breach, overrides are raised in respective applications. This field is mandatory when a currency is defined in AGG.LIM.CCY field. Validation: Should be a valid amount. Mandatory when AGG.LIM.CCY is defined. |
| 16 | `TY.POS.LIM.AGG.OVN.LIM.AMT` | `TyPositionLimits_AggOvnLimAmt` | TField | Yes | An user defined field that contains the overnight limit amount for the aggregate(common) currency. The overnight position for the limit currency would be validated against the amount defined here and in case of a breach, the exceptions are raised in a report during cob. This field is mandatory when a currency is defined in AGG.LIM.CCY field. Validation: Should be a valid amount. Mandatory when AGG.LIM.CCY is defined. Should be less than intraday amount defined in AGG.INTRA.LIM.AMT field. |
| 17 | `TY.POS.LIM.AGG.OVN.LIM.UTIL` | `TyPositionLimits_AggOvnLimUtil` | TField |  | System defaulted field that contains the overnight limit utilized amount for the aggregate currency. This field is updated during COB from the utilization amounts picked from currency POSITION. |
| 18 | `TY.POS.LIM.AGG.OVN.TIME.BAND` | `TyPositionLimits_AggOvnTimeBand` |  |  |  |
| 19 | `TY.POS.LIM.AGG.OVN.TB.LIM.AMT` | `TyPositionLimits_AggOvnTbLimAmt` |  |  |  |
| 20 | `TY.POS.LIM.AGG.OVN.TB.UTIL` | `TyPositionLimits_AggOvnTbUtil` |  |  |  |
| 21 | `TY.POS.LIM.RESERVED.15` | `TyPositionLimits_Reserved15` | TField |  |  |
| 22 | `TY.POS.LIM.RESERVED.14` | `TyPositionLimits_Reserved14` | TField |  |  |
| 23 | `TY.POS.LIM.RESERVED.13` | `TyPositionLimits_Reserved13` | TField |  |  |
| 24 | `TY.POS.LIM.RESERVED.12` | `TyPositionLimits_Reserved12` | TField |  |  |
| 25 | `TY.POS.LIM.RESERVED.11` | `TyPositionLimits_Reserved11` | TField |  |  |
| 26 | `TY.POS.LIM.STOP.LOSS.CCY` | `TyPositionLimits_StopLossCcy` | TField |  | An user defined field that contains the currency in which the stop loss limits are to be monitored. Validations: Must be defined only at dealer level. |
| 27 | `TY.POS.LIM.STOP.LOSS.AMT` | `TyPositionLimits_StopLossAmt` | TField | Yes | An user defined field that contains the stop loss amount for the stop loss currency. This is the limit amount for stop loss and any breaches are reported during cob through a report. Validations: Mandatory when STOP.LOSS.CCY is defined. Must be defined only at dealer level. |
| 28 | `TY.POS.LIM.INCL.OVN.TO.INTRA` | `TyPositionLimits_InclOvnToIntra` | TField |  | An user defined field to indicate if the intraday positions at close of day are to be retained for the next day or to be cleared. Allowed values are &quot;YES&quot; or NULL. |
| 29 | `TY.POS.LIM.RESERVED.9` | `TyPositionLimits_Reserved9` | TField |  |  |
| 30 | `TY.POS.LIM.RESERVED.8` | `TyPositionLimits_Reserved8` | TField |  |  |
| 31 | `TY.POS.LIM.RESERVED.7` | `TyPositionLimits_Reserved7` | TField |  |  |
| 32 | `TY.POS.LIM.RESERVED.6` | `TyPositionLimits_Reserved6` | TField |  |  |
| 33 | `TY.POS.LIM.RESERVED.5` | `TyPositionLimits_Reserved5` | TField |  |  |
| 34 | `TY.POS.LIM.RESERVED.4` | `TyPositionLimits_Reserved4` | TField |  |  |
| 35 | `TY.POS.LIM.RESERVED.3` | `TyPositionLimits_Reserved3` | TField |  |  |
| 36 | `TY.POS.LIM.RESERVED.2` | `TyPositionLimits_Reserved2` | TField |  |  |
| 37 | `TY.POS.LIM.RESERVED.1` | `TyPositionLimits_Reserved1` | TField |  |  |
| 38 | `TY.POS.LIM.LOCAL.REF` | `TyPositionLimits_LocalRef` |  |  |  |
| 39 | `TY.POS.LIM.OVERRIDE` | `TyPositionLimits_Override` |  |  |  |
| 40 | `TY.POS.LIM.RECORD.STATUS` | `TyPositionLimits_RecordStatus` | String |  |  |
| 41 | `TY.POS.LIM.CURR.NO` | `TyPositionLimits_CurrNo` | String |  |  |
| 42 | `TY.POS.LIM.INPUTTER` | `TyPositionLimits_Inputter` |  |  |  |
| 43 | `TY.POS.LIM.DATE.TIME` | `TyPositionLimits_DateTime` |  |  |  |
| 44 | `TY.POS.LIM.AUTHORISER` | `TyPositionLimits_Authoriser` | String |  |  |
| 45 | `TY.POS.LIM.CO.CODE` | `TyPositionLimits_CoCode` | String |  |  |
| 46 | `TY.POS.LIM.DEPT.CODE` | `TyPositionLimits_DeptCode` | String |  |  |
| 47 | `TY.POS.LIM.AUDITOR.CODE` | `TyPositionLimits_AuditorCode` | String |  |  |
| 48 | `TY.POS.LIM.AUDIT.DATE.TIME` | `TyPositionLimits_AuditDateTime` | String |  |  |
