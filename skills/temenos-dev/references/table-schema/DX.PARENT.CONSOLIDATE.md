# DX.PARENT.CONSOLIDATE — Table Schema

> Source: `INSERTS/I_F.DX.PARENT.CONSOLIDATE` in `DX_Order.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.DPC.LOTS` | `DxParentConsolidate_Lots` | TField |  |  |
| 2 | `DX.DPC.PRICE` | `DxParentConsolidate_Price` | TField |  |  |
| 3 | `DX.DPC.INT.PRICE` | `DxParentConsolidate_IntPrice` | TField |  |  |
| 4 | `DX.DPC.TOT.TRADE.COST` | `DxParentConsolidate_TotTradeCost` | TField |  |  |
| 5 | `DX.DPC.TRADE.CCY` | `DxParentConsolidate_TradeCcy` | TField |  |  |
| 6 | `DX.DPC.TRADE.ID` | `DxParentConsolidate_TradeId` |  |  |  |
| 7 | `DX.DPC.SEC.COMM.TYPE` | `DxParentConsolidate_SecCommType` |  |  |  |
| 8 | `DX.DPC.SEC.COMM.CDE` | `DxParentConsolidate_SecCommCde` |  |  |  |
| 9 | `DX.DPC.SEC.COMM.CCY` | `DxParentConsolidate_SecCommCcy` |  |  |  |
| 10 | `DX.DPC.SEC.COMM.AMT` | `DxParentConsolidate_SecCommAmt` |  |  |  |
| 11 | `DX.DPC.SEC.COMM.ACC` | `DxParentConsolidate_SecCommAcc` |  |  |  |
| 12 | `DX.DPC.SEC.CACC.CCY` | `DxParentConsolidate_SecCaccCcy` |  |  |  |
| 13 | `DX.DPC.SEC.COMM.EXCH` | `DxParentConsolidate_SecCommExch` |  |  |  |
| 14 | `DX.DPC.SEC.CACC.AMT` | `DxParentConsolidate_SecCaccAmt` |  |  |  |
| 15 | `DX.DPC.SV.RESERVED10` | `DxParentConsolidate_SvReserved10` |  |  |  |
| 16 | `DX.DPC.SV.RESERVED9` | `DxParentConsolidate_SvReserved9` |  |  |  |
| 17 | `DX.DPC.SV.RESERVED8` | `DxParentConsolidate_SvReserved8` |  |  |  |
| 18 | `DX.DPC.SV.RESERVED7` | `DxParentConsolidate_SvReserved7` |  |  |  |
| 19 | `DX.DPC.SV.RESERVED6` | `DxParentConsolidate_SvReserved6` |  |  |  |
| 20 | `DX.DPC.SV.RESERVED5` | `DxParentConsolidate_SvReserved5` |  |  |  |
| 21 | `DX.DPC.SV.RESERVED4` | `DxParentConsolidate_SvReserved4` |  |  |  |
| 22 | `DX.DPC.SV.RESERVED3` | `DxParentConsolidate_SvReserved3` |  |  |  |
| 23 | `DX.DPC.SV.RESERVED2` | `DxParentConsolidate_SvReserved2` |  |  |  |
| 24 | `DX.DPC.SV.RESERVED1` | `DxParentConsolidate_SvReserved1` |  |  |  |
| 25 | `DX.DPC.STATUS` | `DxParentConsolidate_Status` |  |  |  |
| 26 | `DX.DPC.MV.RESERVED10` | `DxParentConsolidate_MvReserved10` |  |  |  |
| 27 | `DX.DPC.MV.RESERVED9` | `DxParentConsolidate_MvReserved9` |  |  |  |
| 28 | `DX.DPC.MV.RESERVED8` | `DxParentConsolidate_MvReserved8` |  |  |  |
| 29 | `DX.DPC.MV.RESERVED7` | `DxParentConsolidate_MvReserved7` |  |  |  |
| 30 | `DX.DPC.MV.RESERVED6` | `DxParentConsolidate_MvReserved6` |  |  |  |
| 31 | `DX.DPC.MV.RESERVED5` | `DxParentConsolidate_MvReserved5` |  |  |  |
| 32 | `DX.DPC.MV.RESERVED4` | `DxParentConsolidate_MvReserved4` |  |  |  |
| 33 | `DX.DPC.MV.RESERVED3` | `DxParentConsolidate_MvReserved3` |  |  |  |
| 34 | `DX.DPC.MV.RESERVED2` | `DxParentConsolidate_MvReserved2` |  |  |  |
| 35 | `DX.DPC.MV.RESERVED1` | `DxParentConsolidate_MvReserved1` |  |  |  |
| 36 | `DX.DPC.ACC.CCY` | `DxParentConsolidate_AccCcy` |  |  |  |
| 37 | `DX.DPC.EX.RATE.ACC` | `DxParentConsolidate_ExRateAcc` |  |  |  |
| 38 | `DX.DPC.AC.EXC.TRD` | `DxParentConsolidate_AcExcTrd` |  |  |  |
| 39 | `DX.DPC.REF.CCY` | `DxParentConsolidate_RefCcy` |  |  |  |
| 40 | `DX.DPC.EX.RATE.REF` | `DxParentConsolidate_ExRateRef` |  |  |  |
| 41 | `DX.DPC.REF.EXC.TRD` | `DxParentConsolidate_RefExcTrd` |  |  |  |
| 42 | `DX.DPC.TRD.ARCHIVED` | `DxParentConsolidate_TrdArchived` | TField |  |  |
| 43 | `DX.DPC.RESERVED3` | `DxParentConsolidate_Reserved3` |  |  |  |
| 44 | `DX.DPC.RESERVED2` | `DxParentConsolidate_Reserved2` | TField |  |  |
| 45 | `DX.DPC.RESERVED1` | `DxParentConsolidate_Reserved1` | TField |  |  |
