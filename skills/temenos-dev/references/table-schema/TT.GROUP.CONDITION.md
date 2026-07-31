# TT.GROUP.CONDITION — Table Schema

> Source: `INSERTS/I_F.TT.GROUP.CONDITION` in `TT_GroupCondition.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TT.GRP.COND.RATE.SPREAD` | `TtGroupCondition_RateSpread` | TField |  | Specifies the percentage of preferential Rate on Customer Spread for a Currency exchange as against the standard Customer Spread. This percentage is a preferential treatment for the Contract Group mentioned in the @ID of this application. Where the absolute rate (no Rate Spread) is to be applied the rate specified here must be input as 0%. If the entire spread is to be applied the rate specified here must be input as 100%. Validation Rules: Rate input must be in range 0-100%. |
| 2 | `TT.GRP.COND.CHG.TYPE` | `TtGroupCondition_ChgType` |  |  |  |
| 3 | `TT.GRP.COND.CHG.PERCENT` | `TtGroupCondition_ChgPercent` |  |  |  |
| 4 | `TT.GRP.COND.CHG.CCY` | `TtGroupCondition_ChgCcy` |  |  |  |
| 5 | `TT.GRP.COND.CHG.MAXIMUM.AMT` | `TtGroupCondition_ChgMaximumAmt` |  |  |  |
| 6 | `TT.GRP.COND.CHG.MINIMUM.AMT` | `TtGroupCondition_ChgMinimumAmt` |  |  |  |
| 7 | `TT.GRP.COND.CHG.DISCOUNT.AMT` | `TtGroupCondition_ChgDiscountAmt` |  |  |  |
| 8 | `TT.GRP.COND.CHG.PREMIUM.AMT` | `TtGroupCondition_ChgPremiumAmt` |  |  |  |
| 9 | `TT.GRP.COND.CHG.AMT` | `TtGroupCondition_ChgAmt` |  |  |  |
| 10 | `TT.GRP.COND.RESERVED.10` | `TtGroupCondition_Reserved10` | TField |  |  |
| 11 | `TT.GRP.COND.RESERVED.9` | `TtGroupCondition_Reserved9` | TField |  |  |
| 12 | `TT.GRP.COND.RESERVED.8` | `TtGroupCondition_Reserved8` | TField |  |  |
| 13 | `TT.GRP.COND.RESERVED.7` | `TtGroupCondition_Reserved7` | TField |  |  |
| 14 | `TT.GRP.COND.RESERVED.6` | `TtGroupCondition_Reserved6` | TField |  |  |
| 15 | `TT.GRP.COND.RESERVED.5` | `TtGroupCondition_Reserved5` | TField |  |  |
| 16 | `TT.GRP.COND.RESERVED.4` | `TtGroupCondition_Reserved4` | TField |  |  |
| 17 | `TT.GRP.COND.RESERVED.3` | `TtGroupCondition_Reserved3` | TField |  |  |
| 18 | `TT.GRP.COND.RESERVED.2` | `TtGroupCondition_Reserved2` | TField |  |  |
| 19 | `TT.GRP.COND.RESERVED.1` | `TtGroupCondition_Reserved1` | TField |  |  |
| 20 | `TT.GRP.COND.LOCAL.REF` | `TtGroupCondition_LocalRef` |  |  |  |
| 21 | `TT.GRP.COND.OVERRIDE` | `TtGroupCondition_Override` |  |  |  |
| 22 | `TT.GRP.COND.RECORD.STATUS` | `TtGroupCondition_RecordStatus` | String |  |  |
| 23 | `TT.GRP.COND.CURR.NO` | `TtGroupCondition_CurrNo` | String |  |  |
| 24 | `TT.GRP.COND.INPUTTER` | `TtGroupCondition_Inputter` |  |  |  |
| 25 | `TT.GRP.COND.DATE.TIME` | `TtGroupCondition_DateTime` |  |  |  |
| 26 | `TT.GRP.COND.AUTHORISER` | `TtGroupCondition_Authoriser` | String |  |  |
| 27 | `TT.GRP.COND.CO.CODE` | `TtGroupCondition_CoCode` | String |  |  |
| 28 | `TT.GRP.COND.DEPT.CODE` | `TtGroupCondition_DeptCode` | String |  |  |
| 29 | `TT.GRP.COND.AUDITOR.CODE` | `TtGroupCondition_AuditorCode` | String |  |  |
| 30 | `TT.GRP.COND.AUDIT.DATE.TIME` | `TtGroupCondition_AuditDateTime` | String |  |  |
