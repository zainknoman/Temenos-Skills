# ILMATX.RESPONSES — Table Schema

> Source: `INSERTS/I_F.ILMATX.RESPONSES` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.RESPONSES.CUSTOMER.REF` | `IlmatxResponses_CustomerRef` | TField |  | This field is Customer/Portfolio reference. |
| 2 | `ILMATX.RESPONSES.TAX.RATE` | `IlmatxResponses_TaxRate` | TField |  | This field is Calculated tax rate. |
| 3 | `ILMATX.RESPONSES.OUTPUT.CAL.TAX` | `IlmatxResponses_OutputCalTax` | TField |  | This field is Calculated Tax to be paid. |
| 4 | `ILMATX.RESPONSES.IND.COST.PAY` | `IlmatxResponses_IndCostPay` | TField |  | This field is Adjusted cost to be pay . |
| 5 | `ILMATX.RESPONSES.IND.COST.PAY.NOM` | `IlmatxResponses_IndCostPayNom` | TField |  | This field is Nominal cost to be Pay. |
| 6 | `ILMATX.RESPONSES.SUM.CAL.TAX` | `IlmatxResponses_SumCalTax` | TField |  | This field is Gain/Loss for tax calculation. |
| 7 | `ILMATX.RESPONSES.DEDUCT.CODE` | `IlmatxResponses_DeductCode` | TField |  | This field is Deducted code. |
| 8 | `ILMATX.RESPONSES.DEDUCT.GROUP` | `IlmatxResponses_DeductGroup` | TField |  | This field is Summary of deduction, gain that was deducted against previous Loss . |
| 9 | `ILMATX.RESPONSES.REFUND.CODE` | `IlmatxResponses_RefundCode` | TField |  | This field is Refund code. |
| 10 | `ILMATX.RESPONSES.REFUND.GROUP` | `IlmatxResponses_RefundGroup` | TField |  | This field is Tax refund from provisional gain. |
| 11 | `ILMATX.RESPONSES.ERROR.CODE` | `IlmatxResponses_ErrorCode` |  |  |  |
| 12 | `ILMATX.RESPONSES.ERROR.DESC` | `IlmatxResponses_ErrorDesc` |  |  |  |
| 13 | `ILMATX.RESPONSES.CAL.FREE.TAX.IND` | `IlmatxResponses_CalFreeTaxInd` | TField |  | This field is Exemption indicator 0: not exempted 1: exempted . |
| 14 | `ILMATX.RESPONSES.NIS.CAL.TAX.POS.35` | `IlmatxResponses_NisCalTaxPos35` | TField |  | This field is Linear gain sum, for 25% / 35%. Related to calculation period year 2004. |
| 15 | `ILMATX.RESPONSES.TAX.RATE.POS.35` | `IlmatxResponses_TaxRatePos35` | TField |  | This field is Calculated linear tax rate, for 25% / 35%. Related to the period prior year 2005. |
| 16 | `ILMATX.RESPONSES.SUM.CAL.TAX.POS.35` | `IlmatxResponses_SumCalTaxPos35` | TField |  | Gain for tax calculation. For the linear period prior year 2005. Tax rate 25% / 35%. |
| 17 | `ILMATX.RESPONSES.NIS.CAL.TAX.POS.15` | `IlmatxResponses_NisCalTaxPos15` | TField |  | This field is The calculated linear gain sum for the period post year 2004. |
| 18 | `ILMATX.RESPONSES.TAX.RATE.POS.15` | `IlmatxResponses_TaxRatePos15` | TField |  | This field is The linear tax rate for the period post year 2004.. |
| 19 | `ILMATX.RESPONSES.SUM.CAL.TAX.POS.15` | `IlmatxResponses_SumCalTaxPos15` | TField |  | This field is Gain for linear tax calculation for the period starting on the year 2005 beginning. |
| 20 | `ILMATX.RESPONSES.NIS.CAL.TAX.NEG.15` | `IlmatxResponses_NisCalTaxNeg15` | TField |  | This field is Calculated tax for loss. |
| 21 | `ILMATX.RESPONSES.TAX.RATE.NEG.15` | `IlmatxResponses_TaxRateNeg15` | TField |  | This field is Calculated tax rate for loss. |
| 22 | `ILMATX.RESPONSES.SUM.CAL.TAX.NEG.15` | `IlmatxResponses_SumCalTaxNeg15` | TField |  | This field is Loss summary for linear calculation. |
| 23 | `ILMATX.RESPONSES.STORNO.IND` | `IlmatxResponses_StornoInd` | TField |  | This field is Storno Indicator 1: Retroactive 2: Canceled 3: Canceling 4: Affected. |
| 24 | `ILMATX.RESPONSES.NIS.PAY.VAL.NET` | `IlmatxResponses_NisPayValNet` | TField |  | This field is Net proceeds on short transactions. |
| 25 | `ILMATX.RESPONSES.NIS.PAY.VAL` | `IlmatxResponses_NisPayVal` | TField |  | This field is Gross proceeds on short transactions. |
| 26 | `ILMATX.RESPONSES.PL.AFTER.DEDUCT` | `IlmatxResponses_PlAfterDeduct` | TField |  | This field is for Gain/Loss after deduction. |
| 27 | `ILMATX.RESPONSES.DECIDING.PAY.VAL` | `IlmatxResponses_DecidingPayVal` | TField |  | This field is for Cost for tax calculation. |
| 28 | `ILMATX.RESPONSES.TAX.FOR.REFUND` | `IlmatxResponses_TaxForRefund` | TField |  | This field is for Tax for customer refund. |
| 29 | `ILMATX.RESPONSES.SUM.CAL.TAX.25.EX` | `IlmatxResponses_SumCalTax25Ex` | TField |  | Gain/Loss for linearity of 35% / 25% for the exempt part of the calculation. |
| 30 | `ILMATX.RESPONSES.RESERVED.5` | `IlmatxResponses_Reserved5` | TField |  | Reserved for future use. |
| 31 | `ILMATX.RESPONSES.RESERVED.4` | `IlmatxResponses_Reserved4` | TField |  | Reserved for future use. |
| 32 | `ILMATX.RESPONSES.RESERVED.3` | `IlmatxResponses_Reserved3` | TField |  | Reserved for future use. |
| 33 | `ILMATX.RESPONSES.RESERVED.2` | `IlmatxResponses_Reserved2` | TField |  | Reserved for future use. |
| 34 | `ILMATX.RESPONSES.RESERVED.1` | `IlmatxResponses_Reserved1` | TField |  | Reserved for future use. |
| 35 | `ILMATX.RESPONSES.LOCAL.REF` | `IlmatxResponses_LocalRef` |  |  |  |
| 36 | `ILMATX.RESPONSES.OVERRIDE` | `IlmatxResponses_Override` |  |  |  |
| 37 | `ILMATX.RESPONSES.RECORD.STATUS` | `IlmatxResponses_RecordStatus` | String |  |  |
| 38 | `ILMATX.RESPONSES.CURR.NO` | `IlmatxResponses_CurrNo` | String |  |  |
| 39 | `ILMATX.RESPONSES.INPUTTER` | `IlmatxResponses_Inputter` |  |  |  |
| 40 | `ILMATX.RESPONSES.DATE.TIME` | `IlmatxResponses_DateTime` |  |  |  |
| 41 | `ILMATX.RESPONSES.AUTHORISER` | `IlmatxResponses_Authoriser` | String |  |  |
| 42 | `ILMATX.RESPONSES.CO.CODE` | `IlmatxResponses_CoCode` | String |  |  |
| 43 | `ILMATX.RESPONSES.DEPT.CODE` | `IlmatxResponses_DeptCode` | String |  |  |
| 44 | `ILMATX.RESPONSES.AUDITOR.CODE` | `IlmatxResponses_AuditorCode` | String |  |  |
| 45 | `ILMATX.RESPONSES.AUDIT.DATE.TIME` | `IlmatxResponses_AuditDateTime` | String |  |  |
