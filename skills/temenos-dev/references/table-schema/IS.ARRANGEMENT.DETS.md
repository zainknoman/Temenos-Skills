# IS.ARRANGEMENT.DETS — Table Schema

> Source: `INSERTS/I_F.IS.ARRANGEMENT.DETS` in `IS_Purchase.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.ARR.PURCHASE.REF` | `IsArrangementDets_PurchaseRef` | TField |  | The contract reference for which a finance is created. The field is updated with a record key of the application IS.CONTRACT |
| 2 | `IS.ARR.IS.PRODUCT` | `IsArrangementDets_IsProduct` | TField |  | The IS product reference for which AA finance is created. The field is updated with a record key of the application IS.PARAMETER |
| 3 | `IS.ARR.WAK.PURCHASE.REF` | `IsArrangementDets_WakPurchaseRef` | TField |  | The contract reference for which the WAKALA(AA) contract is related to IS.CONTRACT. The field is updated with a record key of the application IS.CONTRACT |
| 4 | `IS.ARR.COMMODITY.SALE.REF` | `IsArrangementDets_CommoditySaleRef` |  |  |  |
| 5 | `IS.ARR.DISBURSE.REF` | `IsArrangementDets_DisburseRef` |  |  |  |
| 6 | `IS.ARR.DISB.ACTIVITY.REF` | `IsArrangementDets_DisbActivityRef` |  |  |  |
| 7 | `IS.ARR.DP.SETTLE.REF` | `IsArrangementDets_DpSettleRef` | TField |  | The Settlement reference through which the down payment is settled ass repayment to the Finance contract. The settlement of down payment is done through FT screen as AA Repayment. |
