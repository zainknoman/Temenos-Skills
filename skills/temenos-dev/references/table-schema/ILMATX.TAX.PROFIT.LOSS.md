# ILMATX.TAX.PROFIT.LOSS — Table Schema

> Source: `INSERTS/I_F.ILMATX.TAX.PROFIT.LOSS` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.TAX.PROFIT.LOSS.DEDUCT.CODE` | `IlmatxTaxProfitLoss_DeductCode` | TField |  | This field is Deduction Code. |
| 2 | `ILMATX.TAX.PROFIT.LOSS.DEDUCT.SUM` | `IlmatxTaxProfitLoss_DeductSum` | TField |  | This field is Loss summary. |
| 3 | `ILMATX.TAX.PROFIT.LOSS.REFUND.CODE` | `IlmatxTaxProfitLoss_RefundCode` | TField |  | This field is Refund Code (always 1). |
| 4 | `ILMATX.TAX.PROFIT.LOSS.REFUND.TAX` | `IlmatxTaxProfitLoss_RefundTax` | TField |  | This field is Tax for refund . |
| 5 | `ILMATX.TAX.PROFIT.LOSS.REFUND.TAX.RATE.1` | `IlmatxTaxProfitLoss_RefundTaxRate1` | TField |  | This field is Refund summary and tax rate varies according to the different tax rates related to the customer activity. |
| 6 | `ILMATX.TAX.PROFIT.LOSS.REFUND.SUM.1` | `IlmatxTaxProfitLoss_RefundSum1` | TField |  | This field is Refund/Gain summary. |
| 7 | `ILMATX.TAX.PROFIT.LOSS.REFUND.TAX.RATE.2` | `IlmatxTaxProfitLoss_RefundTaxRate2` | TField |  | This field is Tax rate. |
| 8 | `ILMATX.TAX.PROFIT.LOSS.REFUND.SUM.2` | `IlmatxTaxProfitLoss_RefundSum2` | TField |  | This field is Refund/Gain summary. |
| 9 | `ILMATX.TAX.PROFIT.LOSS.REFUND.TAX.RATE.3` | `IlmatxTaxProfitLoss_RefundTaxRate3` | TField |  | This field is Tax rate. |
| 10 | `ILMATX.TAX.PROFIT.LOSS.REFUND.SUM.3` | `IlmatxTaxProfitLoss_RefundSum3` | TField |  | This field is Refund/Gain summary. |
| 11 | `ILMATX.TAX.PROFIT.LOSS.REFUND.TAX.RATE.4` | `IlmatxTaxProfitLoss_RefundTaxRate4` | TField |  | This field is Tax rate. |
| 12 | `ILMATX.TAX.PROFIT.LOSS.REFUND.SUM.4` | `IlmatxTaxProfitLoss_RefundSum4` | TField |  | This field is Refund/Gain summary. |
| 13 | `ILMATX.TAX.PROFIT.LOSS.REFUND.TAX.RATE.5` | `IlmatxTaxProfitLoss_RefundTaxRate5` | TField |  | This field is Tax rate. |
| 14 | `ILMATX.TAX.PROFIT.LOSS.REFUND.SUM.5` | `IlmatxTaxProfitLoss_RefundSum5` | TField |  | This field is Refund/Gain summary. |
| 15 | `ILMATX.TAX.PROFIT.LOSS.REFUND.TAX.RATE.6` | `IlmatxTaxProfitLoss_RefundTaxRate6` | TField |  | This field is Tax rate. |
| 16 | `ILMATX.TAX.PROFIT.LOSS.REFUND.SUM.6` | `IlmatxTaxProfitLoss_RefundSum6` | TField |  | This field is Refund/Gain summary. |
| 17 | `ILMATX.TAX.PROFIT.LOSS.RESERVED.5` | `IlmatxTaxProfitLoss_Reserved5` | TField |  | Reserved for future use. |
| 18 | `ILMATX.TAX.PROFIT.LOSS.RESERVED.4` | `IlmatxTaxProfitLoss_Reserved4` | TField |  | Reserved for future use. |
| 19 | `ILMATX.TAX.PROFIT.LOSS.RESERVED.3` | `IlmatxTaxProfitLoss_Reserved3` | TField |  | Reserved for future use. |
| 20 | `ILMATX.TAX.PROFIT.LOSS.RESERVED.2` | `IlmatxTaxProfitLoss_Reserved2` | TField |  | Reserved for future use. |
| 21 | `ILMATX.TAX.PROFIT.LOSS.RESERVED.1` | `IlmatxTaxProfitLoss_Reserved1` | TField |  | Reserved for future use. |
| 22 | `ILMATX.TAX.PROFIT.LOSS.LOCAL.REF` | `IlmatxTaxProfitLoss_LocalRef` |  |  |  |
| 23 | `ILMATX.TAX.PROFIT.LOSS.OVERRIDE` | `IlmatxTaxProfitLoss_Override` |  |  |  |
| 24 | `ILMATX.TAX.PROFIT.LOSS.RECORD.STATUS` | `IlmatxTaxProfitLoss_RecordStatus` | String |  |  |
| 25 | `ILMATX.TAX.PROFIT.LOSS.CURR.NO` | `IlmatxTaxProfitLoss_CurrNo` | String |  |  |
| 26 | `ILMATX.TAX.PROFIT.LOSS.INPUTTER` | `IlmatxTaxProfitLoss_Inputter` |  |  |  |
| 27 | `ILMATX.TAX.PROFIT.LOSS.DATE.TIME` | `IlmatxTaxProfitLoss_DateTime` |  |  |  |
| 28 | `ILMATX.TAX.PROFIT.LOSS.AUTHORISER` | `IlmatxTaxProfitLoss_Authoriser` | String |  |  |
| 29 | `ILMATX.TAX.PROFIT.LOSS.CO.CODE` | `IlmatxTaxProfitLoss_CoCode` | String |  |  |
| 30 | `ILMATX.TAX.PROFIT.LOSS.DEPT.CODE` | `IlmatxTaxProfitLoss_DeptCode` | String |  |  |
| 31 | `ILMATX.TAX.PROFIT.LOSS.AUDITOR.CODE` | `IlmatxTaxProfitLoss_AuditorCode` | String |  |  |
| 32 | `ILMATX.TAX.PROFIT.LOSS.AUDIT.DATE.TIME` | `IlmatxTaxProfitLoss_AuditDateTime` | String |  |  |
