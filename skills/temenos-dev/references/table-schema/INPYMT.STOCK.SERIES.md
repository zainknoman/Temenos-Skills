# INPYMT.STOCK.SERIES — Table Schema

> Source: `INSERTS/I_F.INPYMT.STOCK.SERIES` in `INPYMT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INPYMT.SS.SERIES.NO` | `InpymtStockSeries_SeriesNo` |  |  |  |
| 2 | `INPYMT.SS.STOCK.SERIES.STATUS` | `InpymtStockSeries_StockSeriesStatus` |  |  |  |
| 3 | `INPYMT.SS.CHEQUE.TYPE` | `InpymtStockSeries_ChequeType` |  |  |  |
| 4 | `INPYMT.SS.STOCK.ENTRY.ID` | `InpymtStockSeries_StockEntryId` |  |  |  |
| 5 | `INPYMT.SS.LOCAL.REF` | `InpymtStockSeries_LocalRef` |  |  |  |
| 6 | `INPYMT.SS.RESERVED.10` | `InpymtStockSeries_Reserved10` | TField |  | Reserved for future purpose |
| 7 | `INPYMT.SS.RESERVED.9` | `InpymtStockSeries_Reserved9` | TField |  | Reserved for future purpose |
| 8 | `INPYMT.SS.RESERVED.8` | `InpymtStockSeries_Reserved8` | TField |  | Reserved for future purpose |
| 9 | `INPYMT.SS.RESERVED.7` | `InpymtStockSeries_Reserved7` | TField |  | Reserved for future purpose |
| 10 | `INPYMT.SS.RESERVED.6` | `InpymtStockSeries_Reserved6` | TField |  | Reserved for future purpose |
| 11 | `INPYMT.SS.RESERVED.5` | `InpymtStockSeries_Reserved5` | TField |  | Reserved for future purpose |
| 12 | `INPYMT.SS.RESERVED.4` | `InpymtStockSeries_Reserved4` | TField |  | Reserved for future purpose |
| 13 | `INPYMT.SS.RESERVED.3` | `InpymtStockSeries_Reserved3` | TField |  | Reserved for future purpose |
| 14 | `INPYMT.SS.RESERVED.2` | `InpymtStockSeries_Reserved2` | TField |  | Reserved for future purpose |
| 15 | `INPYMT.SS.RESERVED.1` | `InpymtStockSeries_Reserved1` | TField |  | Reserved for future purpose |
| 16 | `INPYMT.SS.OVERRIDE` | `InpymtStockSeries_Override` |  |  |  |
| 17 | `INPYMT.SS.RECORD.STATUS` | `InpymtStockSeries_RecordStatus` | String |  |  |
| 18 | `INPYMT.SS.CURR.NO` | `InpymtStockSeries_CurrNo` | String |  |  |
| 19 | `INPYMT.SS.INPUTTER` | `InpymtStockSeries_Inputter` |  |  |  |
| 20 | `INPYMT.SS.DATE.TIME` | `InpymtStockSeries_DateTime` |  |  |  |
| 21 | `INPYMT.SS.AUTHORISER` | `InpymtStockSeries_Authoriser` | String |  |  |
| 22 | `INPYMT.SS.CO.CODE` | `InpymtStockSeries_CoCode` | String |  |  |
| 23 | `INPYMT.SS.DEPT.CODE` | `InpymtStockSeries_DeptCode` | String |  |  |
| 24 | `INPYMT.SS.AUDITOR.CODE` | `InpymtStockSeries_AuditorCode` | String |  |  |
| 25 | `INPYMT.SS.AUDIT.DATE.TIME` | `InpymtStockSeries_AuditDateTime` | String |  |  |
