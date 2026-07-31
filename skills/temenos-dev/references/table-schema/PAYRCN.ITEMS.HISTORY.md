# PAYRCN.ITEMS.HISTORY — Table Schema

> Source: `INSERTS/I_F.PAYRCN.ITEMS.HISTORY` in `FINEXT_ATMRECON.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PAYRCN.ITEM.HIST.REFERENCE.NUMBER` | `PayrcnItemsHistory_ReferenceNumber` |  |  |  |
| 2 | `PAYRCN.ITEM.HIST.ADD.INFO` | `PayrcnItemsHistory_AddInfo` |  |  |  |
| 3 | `PAYRCN.ITEM.HIST.OUR.THEIR.FLAG` | `PayrcnItemsHistory_OurTheirFlag` |  |  |  |
| 4 | `PAYRCN.ITEM.HIST.CURRENCY` | `PayrcnItemsHistory_Currency` |  |  |  |
| 5 | `PAYRCN.ITEM.HIST.TXN.AMT` | `PayrcnItemsHistory_TxnAmt` |  |  |  |
| 6 | `PAYRCN.ITEM.HIST.TXN.AMT.LCY` | `PayrcnItemsHistory_TxnAmtLcy` |  |  |  |
| 7 | `PAYRCN.ITEM.HIST.TRANSACTION.DATE` | `PayrcnItemsHistory_TransactionDate` |  |  |  |
| 8 | `PAYRCN.ITEM.HIST.TRANSACTION.TIME` | `PayrcnItemsHistory_TransactionTime` |  |  |  |
| 9 | `PAYRCN.ITEM.HIST.VALUE.DATE` | `PayrcnItemsHistory_ValueDate` |  |  |  |
| 10 | `PAYRCN.ITEM.HIST.MATCHED.ID` | `PayrcnItemsHistory_MatchedId` |  |  |  |
| 11 | `PAYRCN.ITEM.HIST.STATUS` | `PayrcnItemsHistory_Status` |  |  |  |
| 12 | `PAYRCN.ITEM.HIST.STATUS.DESC` | `PayrcnItemsHistory_StatusDesc` |  |  |  |
| 13 | `PAYRCN.ITEM.HIST.DATE.MATCHED` | `PayrcnItemsHistory_DateMatched` |  |  |  |
| 14 | `PAYRCN.ITEM.HIST.CR.DR.INDICATOR` | `PayrcnItemsHistory_CrDrIndicator` |  |  |  |
| 15 | `PAYRCN.ITEM.HIST.RESERVED.31` | `PayrcnItemsHistory_Reserved31` |  |  |  |
| 16 | `PAYRCN.ITEM.HIST.RESERVED.30` | `PayrcnItemsHistory_Reserved30` |  |  |  |
| 17 | `PAYRCN.ITEM.HIST.RESERVED.29` | `PayrcnItemsHistory_Reserved29` |  |  |  |
| 18 | `PAYRCN.ITEM.HIST.RESERVED.28` | `PayrcnItemsHistory_Reserved28` |  |  |  |
| 19 | `PAYRCN.ITEM.HIST.RESERVED.27` | `PayrcnItemsHistory_Reserved27` |  |  |  |
| 20 | `PAYRCN.ITEM.HIST.RESERVED.26` | `PayrcnItemsHistory_Reserved26` |  |  |  |
| 21 | `PAYRCN.ITEM.HIST.RESERVED.25` | `PayrcnItemsHistory_Reserved25` |  |  |  |
| 22 | `PAYRCN.ITEM.HIST.RESERVED.24` | `PayrcnItemsHistory_Reserved24` |  |  |  |
| 23 | `PAYRCN.ITEM.HIST.RESERVED.23` | `PayrcnItemsHistory_Reserved23` |  |  |  |
| 24 | `PAYRCN.ITEM.HIST.RESERVED.22` | `PayrcnItemsHistory_Reserved22` |  |  |  |
| 25 | `PAYRCN.ITEM.HIST.RESERVED.21` | `PayrcnItemsHistory_Reserved21` |  |  |  |
| 26 | `PAYRCN.ITEM.HIST.VARIABLE.1` | `PayrcnItemsHistory_Variable1` |  |  |  |
| 27 | `PAYRCN.ITEM.HIST.VARIABLE.2` | `PayrcnItemsHistory_Variable2` |  |  |  |
| 28 | `PAYRCN.ITEM.HIST.VARIABLE.3` | `PayrcnItemsHistory_Variable3` |  |  |  |
| 29 | `PAYRCN.ITEM.HIST.VARIABLE.4` | `PayrcnItemsHistory_Variable4` |  |  |  |
| 30 | `PAYRCN.ITEM.HIST.VARIABLE.5` | `PayrcnItemsHistory_Variable5` |  |  |  |
| 31 | `PAYRCN.ITEM.HIST.VARIABLE.6` | `PayrcnItemsHistory_Variable6` |  |  |  |
| 32 | `PAYRCN.ITEM.HIST.VARIABLE.7` | `PayrcnItemsHistory_Variable7` |  |  |  |
| 33 | `PAYRCN.ITEM.HIST.VARIABLE.8` | `PayrcnItemsHistory_Variable8` |  |  |  |
| 34 | `PAYRCN.ITEM.HIST.VARIABLE.9` | `PayrcnItemsHistory_Variable9` |  |  |  |
| 35 | `PAYRCN.ITEM.HIST.VARIABLE.10` | `PayrcnItemsHistory_Variable10` |  |  |  |
| 36 | `PAYRCN.ITEM.HIST.VARIABLE.11` | `PayrcnItemsHistory_Variable11` |  |  |  |
| 37 | `PAYRCN.ITEM.HIST.VARIABLE.12` | `PayrcnItemsHistory_Variable12` |  |  |  |
| 38 | `PAYRCN.ITEM.HIST.VARIABLE.13` | `PayrcnItemsHistory_Variable13` |  |  |  |
| 39 | `PAYRCN.ITEM.HIST.VARIABLE.14` | `PayrcnItemsHistory_Variable14` |  |  |  |
| 40 | `PAYRCN.ITEM.HIST.VARIABLE.15` | `PayrcnItemsHistory_Variable15` |  |  |  |
| 41 | `PAYRCN.ITEM.HIST.VARIABLE.16` | `PayrcnItemsHistory_Variable16` |  |  |  |
| 42 | `PAYRCN.ITEM.HIST.VARIABLE.17` | `PayrcnItemsHistory_Variable17` |  |  |  |
| 43 | `PAYRCN.ITEM.HIST.VARIABLE.18` | `PayrcnItemsHistory_Variable18` |  |  |  |
| 44 | `PAYRCN.ITEM.HIST.VARIABLE.19` | `PayrcnItemsHistory_Variable19` |  |  |  |
| 45 | `PAYRCN.ITEM.HIST.VARIABLE.20` | `PayrcnItemsHistory_Variable20` |  |  |  |
| 46 | `PAYRCN.ITEM.HIST.VARIABLE.21` | `PayrcnItemsHistory_Variable21` |  |  |  |
| 47 | `PAYRCN.ITEM.HIST.VARIABLE.22` | `PayrcnItemsHistory_Variable22` |  |  |  |
| 48 | `PAYRCN.ITEM.HIST.VARIABLE.23` | `PayrcnItemsHistory_Variable23` |  |  |  |
| 49 | `PAYRCN.ITEM.HIST.VARIABLE.24` | `PayrcnItemsHistory_Variable24` |  |  |  |
| 50 | `PAYRCN.ITEM.HIST.VARIABLE.25` | `PayrcnItemsHistory_Variable25` |  |  |  |
| 51 | `PAYRCN.ITEM.HIST.RESERVED.20` | `PayrcnItemsHistory_Reserved20` |  |  |  |
| 52 | `PAYRCN.ITEM.HIST.RESERVED.19` | `PayrcnItemsHistory_Reserved19` |  |  |  |
| 53 | `PAYRCN.ITEM.HIST.RESERVED.18` | `PayrcnItemsHistory_Reserved18` |  |  |  |
| 54 | `PAYRCN.ITEM.HIST.RESERVED.17` | `PayrcnItemsHistory_Reserved17` |  |  |  |
| 55 | `PAYRCN.ITEM.HIST.RESERVED.16` | `PayrcnItemsHistory_Reserved16` |  |  |  |
| 56 | `PAYRCN.ITEM.HIST.RESERVED.15` | `PayrcnItemsHistory_Reserved15` |  |  |  |
| 57 | `PAYRCN.ITEM.HIST.RESERVED.14` | `PayrcnItemsHistory_Reserved14` |  |  |  |
| 58 | `PAYRCN.ITEM.HIST.RESERVED.13` | `PayrcnItemsHistory_Reserved13` |  |  |  |
| 59 | `PAYRCN.ITEM.HIST.RESERVED.12` | `PayrcnItemsHistory_Reserved12` |  |  |  |
| 60 | `PAYRCN.ITEM.HIST.RESERVED.11` | `PayrcnItemsHistory_Reserved11` |  |  |  |
| 61 | `PAYRCN.ITEM.HIST.RESERVED.10` | `PayrcnItemsHistory_Reserved10` |  |  |  |
| 62 | `PAYRCN.ITEM.HIST.RESERVED.9` | `PayrcnItemsHistory_Reserved9` |  |  |  |
| 63 | `PAYRCN.ITEM.HIST.RESERVED.8` | `PayrcnItemsHistory_Reserved8` |  |  |  |
| 64 | `PAYRCN.ITEM.HIST.RESERVED.7` | `PayrcnItemsHistory_Reserved7` |  |  |  |
| 65 | `PAYRCN.ITEM.HIST.RESERVED.6` | `PayrcnItemsHistory_Reserved6` |  |  |  |
| 66 | `PAYRCN.ITEM.HIST.RESERVED.5` | `PayrcnItemsHistory_Reserved5` |  |  |  |
| 67 | `PAYRCN.ITEM.HIST.RESERVED.4` | `PayrcnItemsHistory_Reserved4` |  |  |  |
| 68 | `PAYRCN.ITEM.HIST.RESERVED.3` | `PayrcnItemsHistory_Reserved3` |  |  |  |
| 69 | `PAYRCN.ITEM.HIST.RESERVED.2` | `PayrcnItemsHistory_Reserved2` |  |  |  |
| 70 | `PAYRCN.ITEM.HIST.RESERVED.1` | `PayrcnItemsHistory_Reserved1` |  |  |  |
