# ILFEES.ORDER.TRADE.PROCESSED.LIST — Table Schema

> Source: `INSERTS/I_F.ILFEES.ORDER.TRADE.PROCESSED.LIST` in `ILFEES_FeeOptimisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILFEES.DTLS.TRADE.DATE` | `IlfeesOrderTradeProcessedList_TradeDate` |  |  |  |
| 2 | `ILFEES.DTLS.RECALC.FLAG` | `IlfeesOrderTradeProcessedList_RecalcFlag` |  |  |  |
| 3 | `ILFEES.DTLS.FINAL.FEE.AMT` | `IlfeesOrderTradeProcessedList_FinalFeeAmt` |  |  |  |
| 4 | `ILFEES.DTLS.FEE.TYPE` | `IlfeesOrderTradeProcessedList_FeeType` |  |  |  |
| 5 | `ILFEES.DTLS.TRADE.ID` | `IlfeesOrderTradeProcessedList_TradeId` |  |  |  |
| 6 | `ILFEES.DTLS.PROCESSED.FLAG` | `IlfeesOrderTradeProcessedList_ProcessedFlag` | TField |  | Flag to indicate whether the SEC.OPEN.ORDER/DX.ORDER record is processed for fee adjustment. |
| 7 | `ILFEES.DTLS.LOCAL.REF` | `IlfeesOrderTradeProcessedList_LocalRef` |  |  |  |
