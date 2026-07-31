# IS.COMMODITY.LIMIT.POSITION — Table Schema

> Source: `INSERTS/I_F.IS.COMMODITY.LIMIT.POSITION` in `IS_Purchase.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.LP.COMMODITY` | `IsCommodityLimitPosition_Commodity` | TField |  | It is used to store the commodity reference, @ID of IS.COMMODITY. |
| 2 | `IS.LP.BUY.BROKER` | `IsCommodityLimitPosition_BuyBroker` | TField |  | It is used to store the Buy Broker ID captured in the purchase contract. IS.CONTRACT>BUY.BROKER. |
| 3 | `IS.LP.CURRENCY` | `IsCommodityLimitPosition_Currency` | TField |  | It is used to store the Commodity currency. IS.CONTRACT>CURRENCY. |
| 4 | `IS.LP.DAILY.ALLWD.QTY` | `IsCommodityLimitPosition_DailyAllwdQty` | TField |  | It is Applicable only for Broker level limit tracking It contains daily maximum allowed commodity quantity. |
| 5 | `IS.LP.DAILY.ALLWD.AMT` | `IsCommodityLimitPosition_DailyAllwdAmt` | TField |  | It contains maximum allowed amount for commodity or broker |
| 6 | `IS.LP.DAILY.USED.QTY` | `IsCommodityLimitPosition_DailyUsedQty` | TField |  | It is Applicable only for Broker level limit tracking. It contains total used quantity as of now during the day. |
| 7 | `IS.LP.DAILY.USED.AMT` | `IsCommodityLimitPosition_DailyUsedAmt` | TField |  | It contains total used amount as of now during the day for purchasing the commodity from buy broker. |
| 8 | `IS.LP.DAILY.AVL.QTY` | `IsCommodityLimitPosition_DailyAvlQty` | TField |  | It is Applicable only for Broker level limit tracking. Contains available quantity as of now during the day. |
| 9 | `IS.LP.DAILY.AVL.AMT` | `IsCommodityLimitPosition_DailyAvlAmt` | TField |  | It Contains available [Remaining] amount as of now during the day. |
| 10 | `IS.LP.DAILY.BUY.QTY` | `IsCommodityLimitPosition_DailyBuyQty` | TField |  | It is Applicable only for Broker level limit tracking. Contains total commodity quantity bought as of now during the day. |
| 11 | `IS.LP.DAILY.BUY.AMT` | `IsCommodityLimitPosition_DailyBuyAmt` | TField |  | Contains total amount spent for commodity purchase as of now during the day. |
| 12 | `IS.LP.DAILY.RET.QTY` | `IsCommodityLimitPosition_DailyRetQty` | TField |  | It is Applicable only for Broker level limit tracking. Contains total returned commodity quantity as of now during the day. |
| 13 | `IS.LP.DAILY.RET.AMT` | `IsCommodityLimitPosition_DailyRetAmt` | TField |  | Contains total returned commodity purchase amount as of now during the day. |
| 14 | `IS.LP.DAILY.REV.QTY` | `IsCommodityLimitPosition_DailyRevQty` | TField |  | It is Applicable only for Broker level limit tracking. Contains total reversed quantity as of now during the day. |
| 15 | `IS.LP.DAILY.REV.AMT` | `IsCommodityLimitPosition_DailyRevAmt` | TField |  | Contains total reversed commodity amount as of now during the day. |
