# TNFCOP.TRADE.TITLE.CLEARED — Table Schema

> Source: `INSERTS/I_F.TNFCOP.TRADE.TITLE.CLEARED` in `TNFCOP_TradeTitle.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TRADE.CLEARED.CLEARED.TRADE.TITLE` | `TnfcopTradeTitleCleared_ClearedTradeTitle` |  |  |  |
| 2 | `TRADE.CLEARED.IMPUTED.AMT.FCY` | `TnfcopTradeTitleCleared_ImputedAmtFcy` |  |  |  |
| 3 | `TRADE.CLEARED.SETTLEMENT.CCY.CODE` | `TnfcopTradeTitleCleared_SettlementCcyCode` |  |  |  |
| 4 | `TRADE.CLEARED.TOTAL.USED.AMT` | `TnfcopTradeTitleCleared_TotalUsedAmt` |  |  |  |
| 5 | `TRADE.CLEARED.RESERVED.10` | `TnfcopTradeTitleCleared_Reserved10` | TField |  | Field for future use |
| 6 | `TRADE.CLEARED.RESERVED.9` | `TnfcopTradeTitleCleared_Reserved9` | TField |  | Field for future use |
| 7 | `TRADE.CLEARED.RESERVED.8` | `TnfcopTradeTitleCleared_Reserved8` | TField |  | Field for future use |
| 8 | `TRADE.CLEARED.RESERVED.7` | `TnfcopTradeTitleCleared_Reserved7` | TField |  | Field for future use |
| 9 | `TRADE.CLEARED.RESERVED.6` | `TnfcopTradeTitleCleared_Reserved6` | TField |  | Field for future use |
| 10 | `TRADE.CLEARED.RESERVED.5` | `TnfcopTradeTitleCleared_Reserved5` | TField |  | Field for future use |
| 11 | `TRADE.CLEARED.RESERVED.4` | `TnfcopTradeTitleCleared_Reserved4` | TField |  | Field for future use |
| 12 | `TRADE.CLEARED.RESERVED.3` | `TnfcopTradeTitleCleared_Reserved3` | TField |  | Field for future use |
| 13 | `TRADE.CLEARED.RESERVED.2` | `TnfcopTradeTitleCleared_Reserved2` | TField |  | Field for future use |
| 14 | `TRADE.CLEARED.RESERVED.1` | `TnfcopTradeTitleCleared_Reserved1` | TField |  | Field for future use |
