# CHSCRP.JOURNAL.DATA — Table Schema

> Source: `INSERTS/I_F.CHSCRP.JOURNAL.DATA` in `CHSCRP_SecuritiesJournal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHSCRP.SEC.NO` | `ChscrpJournalData_SecNo` | TField |  | Security number of the order that is being reported. |
| 2 | `CHSCRP.SEC.NAME` | `ChscrpJournalData_SecName` | TField |  | Securities name of the Instrument that is being reported. |
| 3 | `CHSCRP.IN.TIME.ORDER` | `ChscrpJournalData_InTimeOrder` | TField |  | Date and time of the order placed. |
| 4 | `CHSCRP.BUY.SELL` | `ChscrpJournalData_BuySell` | TField |  | Indicates the counterparty is Buying or Selling. |
| 5 | `CHSCRP.ORDER.TYPE` | `ChscrpJournalData_OrderType` | TField |  | Type of order being passed. |
| 6 | `CHSCRP.VALID.UNTIL` | `ChscrpJournalData_ValidUntil` | TField |  | Order expiry date. |
| 7 | `CHSCRP.ORDER.NO` | `ChscrpJournalData_OrderNo` | TField |  | It describes the @ID of the Journal like SEC.OPEN.ORDER, DX.ORDER, SEC.TRADE, DX.TRADE |
| 8 | `CHSCRP.ORDER.SIZE` | `ChscrpJournalData_OrderSize` | TField |  | Size of the order, order nominals. |
| 9 | `CHSCRP.DATE.TIME.EXE` | `ChscrpJournalData_DateTimeExe` |  |  |  |
| 10 | `CHSCRP.TRADE.SIZE` | `ChscrpJournalData_TradeSize` |  |  |  |
| 11 | `CHSCRP.ALLOC.PRICE` | `ChscrpJournalData_AllocPrice` |  |  |  |
| 12 | `CHSCRP.EXEC.PLACE` | `ChscrpJournalData_ExecPlace` |  |  |  |
| 13 | `CHSCRP.CLIENT` | `ChscrpJournalData_Client` |  |  |  |
| 14 | `CHSCRP.CP.TRADE.ID` | `ChscrpJournalData_CpTradeId` |  |  |  |
| 15 | `CHSCRP.VALUE.DATE` | `ChscrpJournalData_ValueDate` |  |  |  |
| 16 | `CHSCRP.COUNTERPARTY` | `ChscrpJournalData_Counterparty` |  |  |  |
| 17 | `CHSCRP.RESERVED.7` | `ChscrpJournalData_Reserved7` |  |  |  |
| 18 | `CHSCRP.RESERVED.8` | `ChscrpJournalData_Reserved8` |  |  |  |
| 19 | `CHSCRP.RESERVED.9` | `ChscrpJournalData_Reserved9` |  |  |  |
| 20 | `CHSCRP.RESERVED.10` | `ChscrpJournalData_Reserved10` |  |  |  |
| 21 | `CHSCRP.LOCAL.REF` | `ChscrpJournalData_LocalRef` |  |  |  |
| 22 | `CHSCRP.LIMITS` | `ChscrpJournalData_Limits` | TField |  | Price at which the shares are to be bought or sold. |
| 23 | `CHSCRP.RESERVED.2` | `ChscrpJournalData_Reserved2` | TField |  | Reserved field for future use |
| 24 | `CHSCRP.RESERVED.3` | `ChscrpJournalData_Reserved3` | TField |  | Reserved field for future use |
| 25 | `CHSCRP.RESERVED.4` | `ChscrpJournalData_Reserved4` | TField |  | Reserved field for future use |
| 26 | `CHSCRP.RESERVED.5` | `ChscrpJournalData_Reserved5` | TField |  | Reserved field for future use |
