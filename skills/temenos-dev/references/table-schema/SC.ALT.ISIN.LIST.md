# SC.ALT.ISIN.LIST — Table Schema

> Source: `INSERTS/I_F.SC.ALT.ISIN.LIST` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ALT.ALT.INDEX` | `ScAltIsinList_AltIndex` | TField |  | International security identification number This field will have the ISIN code of the Security Validation Rules: Alphabetical characters |
| 2 | `SC.ALT.TRADE.CURRENCY` | `ScAltIsinList_TradeCurrency` | TField |  | Trade currency as in the ID Validation Rules: Valid Currency in Currency Table |
| 3 | `SC.ALT.TRADE.EXCHANGE` | `ScAltIsinList_TradeExchange` | TField |  | The TRADE EXCHANGE is from SM, If there are multiple exchanges, the exchange will be the one associated with the trade currency Validation Rules: Valid Stock Exchange in STOCK.EXCHANGE table |
| 4 | `SC.ALT.TRADE.EXCH.MIC` | `ScAltIsinList_TradeExchMic` | TField |  | It stores the MIC of the above TRADE EXCHANGE field Validation Rules: 4 Alphabetical characters |
| 5 | `SC.ALT.RESERVED.2` | `ScAltIsinList_Reserved2` | TField |  | Standard T24 reserved field. |
| 6 | `SC.ALT.SECURITY.ID` | `ScAltIsinList_SecurityId` |  |  |  |
| 7 | `SC.ALT.SECURITY.CCY` | `ScAltIsinList_SecurityCcy` |  |  |  |
| 8 | `SC.ALT.SEC.EXCHANGE` | `ScAltIsinList_SecExchange` |  |  |  |
| 9 | `SC.ALT.EXCHANGE.MIC` | `ScAltIsinList_ExchangeMic` |  |  |  |
| 10 | `SC.ALT.RESERVED.MV2` | `ScAltIsinList_ReservedMv2` |  |  |  |
| 11 | `SC.ALT.SEC.STATUS` | `ScAltIsinList_SecStatus` |  |  |  |
| 12 | `SC.ALT.STATUS.DATE` | `ScAltIsinList_StatusDate` |  |  |  |
| 13 | `SC.ALT.SCRIP` | `ScAltIsinList_Scrip` |  |  |  |
| 14 | `SC.ALT.EXPIRED` | `ScAltIsinList_Expired` |  |  |  |
| 15 | `SC.ALT.BLOCKING.DATE` | `ScAltIsinList_BlockingDate` |  |  |  |
| 16 | `SC.ALT.MATURITY.DATE` | `ScAltIsinList_MaturityDate` |  |  |  |
