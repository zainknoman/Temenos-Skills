# IS.COMMODITY.LIMIT.TXNS.HIST — Table Schema

> Source: `INSERTS/I_F.IS.COMMODITY.LIMIT.TXNS.HIST` in `IS_Purchase.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.LTH.IS.CON.REF` | `IsCommodityLimitTxnsHist_IsConRef` |  |  |  |
| 2 | `IS.LTH.BUY.BROKER` | `IsCommodityLimitTxnsHist_BuyBroker` |  |  |  |
| 3 | `IS.LTH.BUY.QTY` | `IsCommodityLimitTxnsHist_BuyQty` |  |  |  |
| 4 | `IS.LTH.BUY.AMT` | `IsCommodityLimitTxnsHist_BuyAmt` |  |  |  |
| 5 | `IS.LTH.PUR.VAL.DATE` | `IsCommodityLimitTxnsHist_PurValDate` |  |  |  |
| 6 | `IS.LTH.RET.QTY` | `IsCommodityLimitTxnsHist_RetQty` |  |  |  |
| 7 | `IS.LTH.RET.AMT` | `IsCommodityLimitTxnsHist_RetAmt` |  |  |  |
| 8 | `IS.LTH.RET.VAL.DATE` | `IsCommodityLimitTxnsHist_RetValDate` |  |  |  |
| 9 | `IS.LTH.SELL.RET.BROKER` | `IsCommodityLimitTxnsHist_SellRetBroker` |  |  |  |
| 10 | `IS.LTH.PUR.REV.DATE` | `IsCommodityLimitTxnsHist_PurRevDate` |  |  |  |
| 11 | `IS.LTH.REC.STATUS` | `IsCommodityLimitTxnsHist_RecStatus` |  |  |  |
