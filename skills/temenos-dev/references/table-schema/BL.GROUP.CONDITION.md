# BL.GROUP.CONDITION — Table Schema

> Source: `INSERTS/I_F.BL.GROUP.CONDITION` in `BL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BL.GRP.COND.INT.DIFFERENTIAL` | `BlGroupCondition_IntDifferential` | TField |  | Interest Spread (difference) applied to the Interest Rate is input in this field by the user, which is defaulted by the system, to arrive at the Effective Interest Rate. The value could be either positive or negative. System would however |
| 2 | `BL.GRP.COND.GRACE.DAYS` | `BlGroupCondition_GraceDays` | TField | No | This is an optional field with the Format nnC or nnW where nn is a number from 1 to 99. An input of 0 is also allowed. "C" stands for Calendar days and "W" for Working days. If no value is entered, then the value would default as explained below in a defaulting mechanism. The values input in this field would be defaulted to the Bill Contracts.In the Bill Contract, if BTTC value is defined (not null) Validation Rules: Value of 1-99 allowed suffixed by "C" or "W". |
| 3 | `BL.GRP.COND.RETENTION.MARGIN` | `BlGroupCondition_RetentionMargin` | TField |  | This field is to specifiy the default value for Retention margin for an invoice at customer level. It can be set both at customer level or by group level Validation Rules: Standard T24 Rate field to specify retention margin percentage Accepts values in range 0 � 99 |
| 4 | `BL.GRP.COND.CHG.TYPE` | `BlGroupCondition_ChgType` |  |  |  |
| 5 | `BL.GRP.COND.CHG.PERCENT` | `BlGroupCondition_ChgPercent` |  |  |  |
| 6 | `BL.GRP.COND.CHG.CCY` | `BlGroupCondition_ChgCcy` |  |  |  |
| 7 | `BL.GRP.COND.CHG.MAXIMUM.AMT` | `BlGroupCondition_ChgMaximumAmt` |  |  |  |
| 8 | `BL.GRP.COND.CHG.MINIMUM.AMT` | `BlGroupCondition_ChgMinimumAmt` |  |  |  |
| 9 | `BL.GRP.COND.CHG.DISCOUNT.AMT` | `BlGroupCondition_ChgDiscountAmt` |  |  |  |
| 10 | `BL.GRP.COND.CHG.PREMIUM.AMT` | `BlGroupCondition_ChgPremiumAmt` |  |  |  |
| 11 | `BL.GRP.COND.CHG.AMT` | `BlGroupCondition_ChgAmt` |  |  |  |
| 12 | `BL.GRP.COND.EXCH.SPREAD` | `BlGroupCondition_ExchSpread` | TField |  | Field refers the spread for currency exchange Validation Rules: Standard T24 Rate field to specify preferential spread. It can accept 0 from 100 % |
| 13 | `BL.GRP.COND.RESERVED.9` | `BlGroupCondition_Reserved9` | TField |  |  |
| 14 | `BL.GRP.COND.RESERVED.8` | `BlGroupCondition_Reserved8` | TField |  |  |
| 15 | `BL.GRP.COND.RESERVED.7` | `BlGroupCondition_Reserved7` | TField |  |  |
| 16 | `BL.GRP.COND.RESERVED.6` | `BlGroupCondition_Reserved6` | TField |  |  |
| 17 | `BL.GRP.COND.RESERVED.5` | `BlGroupCondition_Reserved5` | TField |  |  |
| 18 | `BL.GRP.COND.RESERVED.4` | `BlGroupCondition_Reserved4` | TField |  |  |
| 19 | `BL.GRP.COND.RESERVED.3` | `BlGroupCondition_Reserved3` | TField |  |  |
| 20 | `BL.GRP.COND.RESERVED.2` | `BlGroupCondition_Reserved2` | TField |  |  |
| 21 | `BL.GRP.COND.RESERVED.1` | `BlGroupCondition_Reserved1` | TField |  |  |
| 22 | `BL.GRP.COND.LOCAL.REF` | `BlGroupCondition_LocalRef` |  |  |  |
| 23 | `BL.GRP.COND.OVERRIDE` | `BlGroupCondition_Override` |  |  |  |
| 24 | `BL.GRP.COND.RECORD.STATUS` | `BlGroupCondition_RecordStatus` | String |  |  |
| 25 | `BL.GRP.COND.CURR.NO` | `BlGroupCondition_CurrNo` | String |  |  |
| 26 | `BL.GRP.COND.INPUTTER` | `BlGroupCondition_Inputter` |  |  |  |
| 27 | `BL.GRP.COND.DATE.TIME` | `BlGroupCondition_DateTime` |  |  |  |
| 28 | `BL.GRP.COND.AUTHORISER` | `BlGroupCondition_Authoriser` | String |  |  |
| 29 | `BL.GRP.COND.CO.CODE` | `BlGroupCondition_CoCode` | String |  |  |
| 30 | `BL.GRP.COND.DEPT.CODE` | `BlGroupCondition_DeptCode` | String |  |  |
| 31 | `BL.GRP.COND.AUDITOR.CODE` | `BlGroupCondition_AuditorCode` | String |  |  |
| 32 | `BL.GRP.COND.AUDIT.DATE.TIME` | `BlGroupCondition_AuditDateTime` | String |  |  |
