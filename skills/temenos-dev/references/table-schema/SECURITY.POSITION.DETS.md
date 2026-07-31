# SECURITY.POSITION.DETS — Table Schema

> Source: `INSERTS/I_F.SECURITY.POSITION.DETS` in `SC_ScoSecurityPositionUpdate.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SCP.DETS.TXN.ID` | `SecurityPositionDets_TxnId` |  |  |  |
| 2 | `SC.SCP.DETS.TRADE.DATE.TIME` | `SecurityPositionDets_TradeDateTime` |  |  |  |
| 3 | `SC.SCP.DETS.VALUE.DATE.TIME` | `SecurityPositionDets_ValueDateTime` |  |  |  |
| 4 | `SC.SCP.DETS.TXN.TYPE` | `SecurityPositionDets_TxnType` |  |  |  |
| 5 | `SC.SCP.DETS.NOMINAL` | `SecurityPositionDets_Nominal` |  |  |  |
| 6 | `SC.SCP.DETS.COST` | `SecurityPositionDets_Cost` |  |  |  |
| 7 | `SC.SCP.DETS.EXPENSES` | `SecurityPositionDets_Expenses` |  |  |  |
| 8 | `SC.SCP.DETS.PAR.LVL.REAL.GN` | `SecurityPositionDets_ParLvlRealGn` |  |  |  |
| 9 | `SC.SCP.DETS.PURCHASE.TXN.REF` | `SecurityPositionDets_PurchaseTxnRef` |  |  |  |
| 10 | `SC.SCP.DETS.RESERVED3` | `SecurityPositionDets_Reserved3` |  |  |  |
| 11 | `SC.SCP.DETS.RESERVED4` | `SecurityPositionDets_Reserved4` |  |  |  |
| 12 | `SC.SCP.DETS.RESERVED5` | `SecurityPositionDets_Reserved5` |  |  |  |
| 13 | `SC.SCP.DETS.RESERVED6` | `SecurityPositionDets_Reserved6` |  |  |  |
| 14 | `SC.SCP.DETS.RESERVED7` | `SecurityPositionDets_Reserved7` |  |  |  |
| 15 | `SC.SCP.DETS.RESERVED8` | `SecurityPositionDets_Reserved8` |  |  |  |
| 16 | `SC.SCP.DETS.RESERVED9` | `SecurityPositionDets_Reserved9` |  |  |  |
| 17 | `SC.SCP.DETS.RESERVED10` | `SecurityPositionDets_Reserved10` |  |  |  |
| 18 | `SC.SCP.DETS.RESERVED11` | `SecurityPositionDets_Reserved11` |  |  |  |
| 19 | `SC.SCP.DETS.RESERVED12` | `SecurityPositionDets_Reserved12` |  |  |  |
| 20 | `SC.SCP.DETS.RESERVED13` | `SecurityPositionDets_Reserved13` |  |  |  |
| 21 | `SC.SCP.DETS.RESERVED14` | `SecurityPositionDets_Reserved14` |  |  |  |
| 22 | `SC.SCP.DETS.RESERVED15` | `SecurityPositionDets_Reserved15` |  |  |  |
| 23 | `SC.SCP.DETS.RESERVED16` | `SecurityPositionDets_Reserved16` |  |  |  |
| 24 | `SC.SCP.DETS.RESERVED17` | `SecurityPositionDets_Reserved17` |  |  |  |
| 25 | `SC.SCP.DETS.RESERVED18` | `SecurityPositionDets_Reserved18` |  |  |  |
| 26 | `SC.SCP.DETS.RESERVED19` | `SecurityPositionDets_Reserved19` |  |  |  |
| 27 | `SC.SCP.DETS.RESERVED20` | `SecurityPositionDets_Reserved20` |  |  |  |
| 28 | `SC.SCP.DETS.ACCRUED.INT` | `SecurityPositionDets_AccruedInt` |  |  |  |
| 29 | `SC.SCP.DETS.NET.NOMINAL` | `SecurityPositionDets_NetNominal` | TField |  | This field holds the total open nominal. |
| 30 | `SC.SCP.DETS.REALIZED.GAIN` | `SecurityPositionDets_RealizedGain` | TField |  | This field holds the Realized gain after the Sell transaction |
| 31 | `SC.SCP.DETS.UN.REALIZED.GAIN` | `SecurityPositionDets_UnRealizedGain` | TField |  | This field holds the Un Realized gain |
| 32 | `SC.SCP.DETS.SECURITY.ACCOUNT` | `SecurityPositionDets_SecurityAccount` | TField |  | This field holds portfolio Id. |
| 33 | `SC.SCP.DETS.SECURITY.NUMBER` | `SecurityPositionDets_SecurityNumber` | TField |  | This field holds Instrument Id. |
