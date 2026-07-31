# LC.GROUP.CONDITION — Table Schema

> Source: `INSERTS/I_F.LC.GROUP.CONDITION` in `LC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LC3.RATE.SPREAD` | `LcGroupCondition_RateSpread` | TField |  | Specifies the preferential rate used to determine the Customer Spread for a currency exchange as a percentage of the standard Customer Spread. Where a customer or group of customers are given preferential exchange rates this field is used to define what percentage of the standard Customer Spread (as defined in the Currency table) should be applied. Where the absolute rate (no Rate Spread) is to be applied the rate specified here must be input as 0%. If the entire spread is to be applied the rate specified here must be input as 100%. If left blank the Rate Spread will be the same as for a standard customer (as if 100% was entered). Validation Rules: Up to 10 type R characters plus a decimal point (standard rate format), but must not exceed 100%. Rate input must be in the range 0-100% Not more than 3 integers may be entered. Not more than 9 decimals may be entered. |
| 2 | `LC3.COMM.TYPE` | `LcGroupCondition_CommType` |  |  |  |
| 3 | `LC3.COMM.PERCENT` | `LcGroupCondition_CommPercent` |  |  |  |
| 4 | `LC3.COMM.CCY` | `LcGroupCondition_CommCcy` |  |  |  |
| 5 | `LC3.COMM.MAXIMUM.AMT` | `LcGroupCondition_CommMaximumAmt` |  |  |  |
| 6 | `LC3.COMM.MINIMUM.AMT` | `LcGroupCondition_CommMinimumAmt` |  |  |  |
| 7 | `LC3.COMM.DISCOUNT.AMT` | `LcGroupCondition_CommDiscountAmt` |  |  |  |
| 8 | `LC3.COMM.PREMIUM.AMT` | `LcGroupCondition_CommPremiumAmt` |  |  |  |
| 9 | `LC3.COMM.F.AMT` | `LcGroupCondition_CommFAmt` |  |  |  |
| 10 | `LC3.CHARGE.TYPE` | `LcGroupCondition_ChargeType` |  |  |  |
| 11 | `LC3.CHARGE.PERCENT` | `LcGroupCondition_ChargePercent` |  |  |  |
| 12 | `LC3.CHARGE.CCY` | `LcGroupCondition_ChargeCcy` |  |  |  |
| 13 | `LC3.CHG.MAXIMUM.AMT` | `LcGroupCondition_ChgMaximumAmt` |  |  |  |
| 14 | `LC3.CHG.MINIMUM.AMT` | `LcGroupCondition_ChgMinimumAmt` |  |  |  |
| 15 | `LC3.CHG.DISCOUNT.AMT` | `LcGroupCondition_ChgDiscountAmt` |  |  |  |
| 16 | `LC3.CHG.PREMIUM.AMT` | `LcGroupCondition_ChgPremiumAmt` |  |  |  |
| 17 | `LC3.CHARGE.F.AMT` | `LcGroupCondition_ChargeFAmt` |  |  |  |
| 18 | `LC3.CHG.COMM.SEPARATE` | `LcGroupCondition_ChgCommSeparate` | TField |  | This field is currently not in use. |
| 19 | `LC3.PAYMENT.TYPE` | `LcGroupCondition_PaymentType` |  |  |  |
| 20 | `LC3.CUSTOMER.FLOAT` | `LcGroupCondition_CustomerFloat` |  |  |  |
| 21 | `LC3.LOCAL.REF` | `LcGroupCondition_LocalRef` |  |  |  |
| 22 | `LC3.PRD.COMM.CODE` | `LcGroupCondition_PrdCommCode` |  |  |  |
| 23 | `LC3.PRD.COMM.PCT` | `LcGroupCondition_PrdCommPct` |  |  |  |
| 24 | `LC3.PRD.COMM.RATE` | `LcGroupCondition_PrdCommRate` |  |  |  |
| 25 | `LC3.PRD.COMM.CCY` | `LcGroupCondition_PrdCommCcy` |  |  |  |
| 26 | `LC3.PRD.COMM.AMT` | `LcGroupCondition_PrdCommAmt` |  |  |  |
| 27 | `LC3.RESERVED.5` | `LcGroupCondition_Reserverd5` |  |  |  |
| 28 | `LC3.RESERVED.4` | `LcGroupCondition_Reserverd4` |  |  |  |
| 29 | `LC3.RESERVED.3` | `LcGroupCondition_Reserverd3` |  |  |  |
| 30 | `LC3.RESERVED.2` | `LcGroupCondition_Reserverd2` |  |  |  |
| 31 | `LC3.RESERVED.1` | `LcGroupCondition_Reserverd1` |  |  |  |
| 32 | `LC3.RECORD.STATUS` | `LcGroupCondition_RecordStatus` | String |  |  |
| 33 | `LC3.CURR.NO` | `LcGroupCondition_CurrNo` | String |  |  |
| 34 | `LC3.INPUTTER` | `LcGroupCondition_Inputter` |  |  |  |
| 35 | `LC3.DATE.TIME` | `LcGroupCondition_DateTime` |  |  |  |
| 36 | `LC3.AUTHORISER` | `LcGroupCondition_Authoriser` | String |  |  |
| 37 | `LC3.CO.CODE` | `LcGroupCondition_CoCode` | String |  |  |
| 38 | `LC3.DEPT.CODE` | `LcGroupCondition_DeptCode` | String |  |  |
| 39 | `LC3.AUDITOR.CODE` | `LcGroupCondition_AuditorCode` | String |  |  |
| 40 | `LC3.AUDIT.DATE.TIME` | `LcGroupCondition_AuditDateTime` | String |  |  |
