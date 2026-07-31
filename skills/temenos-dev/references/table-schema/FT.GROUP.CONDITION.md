# FT.GROUP.CONDITION — Table Schema

> Source: `INSERTS/I_F.FT.GROUP.CONDITION` in `FT_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FT3.RATE.SPREAD` | `FtGroupCondition_RateSpread` | TField | No | Specifies the preferential Rate used to determine the Customer Spread for a Currency exchange as a percentage of the standard Customer Spread. Where a group of Customers are given preferential exchange rates this field is used to define what percentage of the standard Customer Spread (as defined in the Currency table) should be applied. Where the absolute rate (no Rate Spread) is to be applied the rate specified here must be input as 0%. If the entire spread is to be applied the rate specified here must be input as 100%. If left blank the Rate Spread will be the same as the standard Customer Spread for the Currency involved (as if 100% when entered). Validation Rules: Up to 10 type R characters plus a decimal point, (standard rate format), but must not exceed 100%. (Optional input.) Rate input must be in range 0-100%. Not more than 3 integers may be entered. Not more than 9 decimals may be entered. |
| 2 | `FT3.COMM.TYPE` | `FtGroupCondition_CommType` |  |  |  |
| 3 | `FT3.COMM.PERCENT` | `FtGroupCondition_CommPercent` |  |  |  |
| 4 | `FT3.COMM.CCY` | `FtGroupCondition_CommCcy` |  |  |  |
| 5 | `FT3.COMM.MAXIMUM.AMT` | `FtGroupCondition_CommMaximumAmt` |  |  |  |
| 6 | `FT3.COMM.MINIMUM.AMT` | `FtGroupCondition_CommMinimumAmt` |  |  |  |
| 7 | `FT3.COMM.DISCOUNT.AMT` | `FtGroupCondition_CommDiscountAmt` |  |  |  |
| 8 | `FT3.COMM.PREMIUM.AMT` | `FtGroupCondition_CommPremiumAmt` |  |  |  |
| 9 | `FT3.COMM.F.AMT` | `FtGroupCondition_CommFAmt` |  |  |  |
| 10 | `FT3.CHARGE.TYPE` | `FtGroupCondition_ChargeType` |  |  |  |
| 11 | `FT3.CHARGE.PERCENT` | `FtGroupCondition_ChargePercent` |  |  |  |
| 12 | `FT3.CHARGE.CCY` | `FtGroupCondition_ChargeCcy` |  |  |  |
| 13 | `FT3.CHG.MAXIMUM.AMT` | `FtGroupCondition_ChgMaximumAmt` |  |  |  |
| 14 | `FT3.CHG.MINIMUM.AMT` | `FtGroupCondition_ChgMinimumAmt` |  |  |  |
| 15 | `FT3.CHG.DISCOUNT.AMT` | `FtGroupCondition_ChgDiscountAmt` |  |  |  |
| 16 | `FT3.CHG.PREMIUM.AMT` | `FtGroupCondition_ChgPremiumAmt` |  |  |  |
| 17 | `FT3.CHARGE.F.AMT` | `FtGroupCondition_ChargeFAmt` |  |  |  |
| 18 | `FT3.CHG.COMM.SEPARATE` | `FtGroupCondition_ChgCommSeparate` | TField | No | Defines whether Charges on Funds Transfer are to appear on the Customer statement as a separate amount. If "Y" is input in this field, a separate Charge entry will then be generated for all the Customers included in the Group. Validation Rules: 'Y' (yes) or Blank = (NO) (Optional input. Default is No) |
| 19 | `FT3.PAYMENT.TYPE` | `FtGroupCondition_PaymentType` |  |  |  |
| 20 | `FT3.CUSTOMER.FLOAT` | `FtGroupCondition_CustomerFloat` |  |  |  |
| 21 | `FT3.LOCAL.REF` | `FtGroupCondition_LocalRef` |  |  |  |
| 22 | `FT3.DETAIL.COMM.CHG` | `FtGroupCondition_DetailCommChg` | TField |  | Field to control whether multiple commissions should be posted separately or combined in a single posting. Validation Rules: YES : Multiple commissions will be posted separately. Can be set to YES only when CHG.COMM.SEPARATE is Y. NO or None : Multiple commissions are combined in a single posting. Default is None. |
| 23 | `FT3.DETAIL.TAX` | `FtGroupCondition_DetailTax` | TField |  | Field to control whether each tax should be posted separately or combined in a single posting. Validation Rules: YES : Multiple taxes will be posted separately. Can be set to YES only when CHG.COMM.SEPARATE is Y. NO or None : Multiple taxes are combined in a single posting. Default is None. |
| 24 | `FT3.RESERVED.3` | `FtGroupCondition_Reserved3` | TField |  |  |
| 25 | `FT3.RESERVED.2` | `FtGroupCondition_Reserved2` | TField |  |  |
| 26 | `FT3.RESERVED.1` | `FtGroupCondition_Reserved1` | TField |  |  |
| 27 | `FT3.RECORD.STATUS` | `FtGroupCondition_RecordStatus` | String |  |  |
| 28 | `FT3.CURR.NO` | `FtGroupCondition_CurrNo` | String |  |  |
| 29 | `FT3.INPUTTER` | `FtGroupCondition_Inputter` |  |  |  |
| 30 | `FT3.DATE.TIME` | `FtGroupCondition_DateTime` |  |  |  |
| 31 | `FT3.AUTHORISER` | `FtGroupCondition_Authoriser` | String |  |  |
| 32 | `FT3.CO.CODE` | `FtGroupCondition_CoCode` | String |  |  |
| 33 | `FT3.DEPT.CODE` | `FtGroupCondition_DeptCode` | String |  |  |
| 34 | `FT3.AUDITOR.CODE` | `FtGroupCondition_AuditorCode` | String |  |  |
| 35 | `FT3.AUDIT.DATE.TIME` | `FtGroupCondition_AuditDateTime` | String |  |  |
