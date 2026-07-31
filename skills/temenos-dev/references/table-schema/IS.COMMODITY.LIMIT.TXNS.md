# IS.COMMODITY.LIMIT.TXNS — Table Schema

> Source: `INSERTS/I_F.IS.COMMODITY.LIMIT.TXNS` in `IS_Purchase.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.LT.IS.CON.REF` | `IsCommodityLimitTxns_IsConRef` |  |  |  |
| 2 | `IS.LT.BUY.BROKER` | `IsCommodityLimitTxns_BuyBroker` |  |  |  |
| 3 | `IS.LT.BUY.QTY` | `IsCommodityLimitTxns_BuyQty` |  |  |  |
| 4 | `IS.LT.BUY.AMT` | `IsCommodityLimitTxns_BuyAmt` |  |  |  |
| 5 | `IS.LT.PUR.VAL.DATE` | `IsCommodityLimitTxns_PurValDate` |  |  |  |
| 6 | `IS.LT.RET.QTY` | `IsCommodityLimitTxns_RetQty` |  |  |  |
| 7 | `IS.LT.RET.AMT` | `IsCommodityLimitTxns_RetAmt` |  |  |  |
| 8 | `IS.LT.RET.VAL.DATE` | `IsCommodityLimitTxns_RetValDate` |  |  |  |
| 9 | `IS.LT.SELL.RET.BROKER` | `IsCommodityLimitTxns_SellRetBroker` |  |  |  |
| 10 | `IS.LT.PUR.REV.DATE` | `IsCommodityLimitTxns_PurRevDate` |  |  |  |
| 11 | `IS.LT.REC.STATUS` | `IsCommodityLimitTxns_RecStatus` |  |  |  |
