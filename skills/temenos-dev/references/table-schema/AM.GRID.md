# AM.GRID — Table Schema

> Source: `INSERTS/I_F.AM.GRID` in `AM_Modelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.GRD.VALUATION.CURRENCY` | `AmGrid_ValuationCurrency` | TField |  | Specifies the currency in which the Security Portfolio is to be valuated. For a portfolio, this field will be updated from the VALUATION.CURRENCY field of the SEC.ACC.MASTER file. For a consolidate portfolio, it will be updated from the CONSOLIDATE.CCY field of the AM.COMPARE file. Validation Rules: A maximum of 3 characters may be entered (No input field). Must exist on CURRENCY Code table. |
| 2 | `AM.GRD.ABC.AXIS` | `AmGrid_AbcAxis` | TField |  | Defines the X axis (abscissa) of the grid. Validation Rules: No input field. Must be a valid AXIS code. Automatically updated by the AM.GRID.BUILD routine whenever the comparison grid is re-built. |
| 3 | `AM.GRD.ABC.MEMBER` | `AmGrid_AbcMember` |  |  |  |
| 4 | `AM.GRD.ABC.LABEL` | `AmGrid_AbcLabel` |  |  |  |
| 5 | `AM.GRD.ORD.AXIS` | `AmGrid_OrdAxis` | TField |  | Defines the Y axis (ordinate) of the grid. Validation Rules: No input field. Must be a valid AXIS code. Automatically updated by the AM.GRID.BUILD routine whenever the comparison grid is re-built. |
| 6 | `AM.GRD.ORD.MEMBER` | `AmGrid_OrdMember` |  |  |  |
| 7 | `AM.GRD.ORD.LABEL` | `AmGrid_OrdLabel` |  |  |  |
| 8 | `AM.GRD.LINK` | `AmGrid_Link` |  |  |  |
| 9 | `AM.GRD.MODEL.TARGET` | `AmGrid_ModelTarget` |  |  |  |
| 10 | `AM.GRD.MODEL.MAX` | `AmGrid_ModelMax` |  |  |  |
| 11 | `AM.GRD.MODEL.MIN` | `AmGrid_ModelMin` |  |  |  |
| 12 | `AM.GRD.DATA.TARGET` | `AmGrid_DataTarget` |  |  |  |
| 13 | `AM.GRD.DATA.VALUE` | `AmGrid_DataValue` |  |  |  |
| 14 | `AM.GRD.REFERENCE` | `AmGrid_Reference` |  |  |  |
| 15 | `AM.GRD.REBALANCE` | `AmGrid_Rebalance` |  |  |  |
| 16 | `AM.GRD.APPLICATION` | `AmGrid_Application` |  |  |  |
| 17 | `AM.GRD.OPTION` | `AmGrid_Option` |  |  |  |
| 18 | `AM.GRD.CODE` | `AmGrid_Code` |  |  |  |
| 19 | `AM.GRD.ALLOC.RATE` | `AmGrid_AllocRate` |  |  |  |
| 20 | `AM.GRD.VALUATION` | `AmGrid_Valuation` |  |  |  |
| 21 | `AM.GRD.NOMINAL` | `AmGrid_Nominal` |  |  |  |
| 22 | `AM.GRD.MODEL.VALUE` | `AmGrid_ModelValue` |  |  |  |
| 23 | `AM.GRD.SELL.SECURITIES` | `AmGrid_SellSecurities` |  |  |  |
