# TNFCOP.TRADE.TITLE.NOTCLEARED — Table Schema

> Source: `INSERTS/I_F.TNFCOP.TRADE.TITLE.NOTCLEARED` in `TNFCOP_TradeTitle.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TRADE.NOTCLEARED.NOTCLEARED.TRADE.TITLE` | `TnfcopTradeTitleNotcleared_NotclearedTradeTitle` |  |  |  |
| 2 | `TRADE.NOTCLEARED.IMPUTED.AMT.FCY` | `TnfcopTradeTitleNotcleared_ImputedAmtFcy` |  |  |  |
| 3 | `TRADE.NOTCLEARED.SETTLEMENT.CCY.CODE` | `TnfcopTradeTitleNotcleared_SettlementCcyCode` |  |  |  |
| 4 | `TRADE.NOTCLEARED.TOTAL.USED.AMT` | `TnfcopTradeTitleNotcleared_TotalUsedAmt` |  |  |  |
| 5 | `TRADE.NOTCLEARED.RESERVED.10` | `TnfcopTradeTitleNotcleared_Reserved10` | TField |  | Field for future use |
| 6 | `TRADE.NOTCLEARED.RESERVED.9` | `TnfcopTradeTitleNotcleared_Reserved9` | TField |  | Field for future use |
| 7 | `TRADE.NOTCLEARED.RESERVED.8` | `TnfcopTradeTitleNotcleared_Reserved8` | TField |  | Field for future use |
| 8 | `TRADE.NOTCLEARED.RESERVED.7` | `TnfcopTradeTitleNotcleared_Reserved7` | TField |  | Field for future use |
| 9 | `TRADE.NOTCLEARED.RESERVED.6` | `TnfcopTradeTitleNotcleared_Reserved6` | TField |  | Field for future use |
| 10 | `TRADE.NOTCLEARED.RESERVED.5` | `TnfcopTradeTitleNotcleared_Reserved5` | TField |  | Field for future use |
| 11 | `TRADE.NOTCLEARED.RESERVED.4` | `TnfcopTradeTitleNotcleared_Reserved4` | TField |  | Field for future use |
| 12 | `TRADE.NOTCLEARED.RESERVED.3` | `TnfcopTradeTitleNotcleared_Reserved3` | TField |  | Field for future use |
| 13 | `TRADE.NOTCLEARED.RESERVED.2` | `TnfcopTradeTitleNotcleared_Reserved2` | TField |  | Field for future use |
| 14 | `TRADE.NOTCLEARED.RESERVED.1` | `TnfcopTradeTitleNotcleared_Reserved1` | TField |  | Field for future use |
