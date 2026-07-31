# DX.PARENT.LOG — Table Schema

> Source: `INSERTS/I_F.DX.PARENT.LOG` in `DX_Order.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.DPL.CONTRACT.CODE` | `DxParentLog_ContractCode` | TField |  |  |
| 2 | `DX.DPL.MATURITY.DATE` | `DxParentLog_MaturityDate` | TField |  |  |
| 3 | `DX.DPL.OPTION.TYPE` | `DxParentLog_OptionType` | TField |  |  |
| 4 | `DX.DPL.OPTION.STYLE` | `DxParentLog_OptionStyle` | TField |  |  |
| 5 | `DX.DPL.STRIKE.PRICE` | `DxParentLog_StrikePrice` | TField |  |  |
| 6 | `DX.DPL.TRADE.DIRECTION` | `DxParentLog_TradeDirection` | TField |  |  |
| 7 | `DX.DPL.LIMIT.TYPE` | `DxParentLog_LimitType` | TField |  |  |
| 8 | `DX.DPL.LIMIT.PRICE` | `DxParentLog_LimitPrice` | TField |  |  |
| 9 | `DX.DPL.LIMIT.DATE` | `DxParentLog_LimitDate` | TField |  |  |
| 10 | `DX.DPL.PARENT.ORD.ID` | `DxParentLog_ParentOrdId` | TField |  |  |
| 11 | `DX.DPL.PARENT.LOTS` | `DxParentLog_ParentLots` | TField |  |  |
| 12 | `DX.DPL.PARENT.STATUS` | `DxParentLog_ParentStatus` | TField |  |  |
| 13 | `DX.DPL.CHILD.ORD.ID` | `DxParentLog_ChildOrdId` |  |  |  |
| 14 | `DX.DPL.CHILD.LOTS` | `DxParentLog_ChildLots` |  |  |  |
| 15 | `DX.DPL.TRADE.TXN.ID` | `DxParentLog_TradeTxnId` |  |  |  |
| 16 | `DX.DPL.TRADE.LOTS` | `DxParentLog_TradeLots` |  |  |  |
| 17 | `DX.DPL.MV.RESERVED1` | `DxParentLog_MvReserved1` |  |  |  |
| 18 | `DX.DPL.MV.RESERVED2` | `DxParentLog_MvReserved2` |  |  |  |
| 19 | `DX.DPL.MV.RESERVED3` | `DxParentLog_MvReserved3` |  |  |  |
| 20 | `DX.DPL.MV.RESERVED4` | `DxParentLog_MvReserved4` |  |  |  |
| 21 | `DX.DPL.MV.RESERVED5` | `DxParentLog_MvReserved5` |  |  |  |
| 22 | `DX.DPL.RESERVED1` | `DxParentLog_Reserved1` |  |  |  |
| 23 | `DX.DPL.RESERVED2` | `DxParentLog_Reserved2` |  |  |  |
| 24 | `DX.DPL.RESERVED3` | `DxParentLog_Reserved3` |  |  |  |
| 25 | `DX.DPL.RESERVED4` | `DxParentLog_Reserved4` |  |  |  |
| 26 | `DX.DPL.RESERVED5` | `DxParentLog_Reserved5` |  |  |  |
| 27 | `DX.DPL.RESERVED6` | `DxParentLog_Reserved6` |  |  |  |
| 28 | `DX.DPL.RESERVED7` | `DxParentLog_Reserved7` |  |  |  |
| 29 | `DX.DPL.RESERVED8` | `DxParentLog_Reserved8` |  |  |  |
| 30 | `DX.DPL.RESERVED9` | `DxParentLog_Reserved9` |  |  |  |
| 31 | `DX.DPL.RESERVED10` | `DxParentLog_Reserved10` |  |  |  |
| 32 | `DX.DPL.PARENT.ORIG.LOTS` | `DxParentLog_ParentOrigLots` | TField |  |  |
| 33 | `DX.DPL.TOT.DPC` | `DxParentLog_TotDpc` | TField |  |  |
