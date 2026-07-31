# AM.GRP.GRID — Table Schema

> Source: `INSERTS/I_F.AM.GRP.GRID` in `AM_Modelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.GGR.VALUATION.CURRENCY` | `AmGrpGrid_ValuationCurrency` | TField |  | Holds the group valuation currency as mentioned in AM.GROUP.PORT Validation Rules: Ccy |
| 2 | `AM.GGR.ABC.AXIS` | `AmGrpGrid_AbcAxis` | TField |  | Defines the X axis of the grid. Validation Rules: Alpha numeric |
| 3 | `AM.GGR.ABC.MEMBER` | `AmGrpGrid_AbcMember` |  |  |  |
| 4 | `AM.GGR.ABC.LABEL` | `AmGrpGrid_AbcLabel` |  |  |  |
| 5 | `AM.GGR.ORD.AXIS` | `AmGrpGrid_OrdAxis` | TField |  | Defines the Y axis of the grid. Validation Rules: Alpha numeric |
| 6 | `AM.GGR.ORD.MEMBER` | `AmGrpGrid_OrdMember` |  |  |  |
| 7 | `AM.GGR.ORD.LABEL` | `AmGrpGrid_OrdLabel` |  |  |  |
| 8 | `AM.GGR.LINK` | `AmGrpGrid_Link` |  |  |  |
| 9 | `AM.GGR.MODEL.TARGET` | `AmGrpGrid_ModelTarget` |  |  |  |
| 10 | `AM.GGR.MODEL.MAX` | `AmGrpGrid_ModelMax` |  |  |  |
| 11 | `AM.GGR.MODEL.MIN` | `AmGrpGrid_ModelMin` |  |  |  |
| 12 | `AM.GGR.DATA.TARGET` | `AmGrpGrid_DataTarget` |  |  |  |
| 13 | `AM.GGR.DATA.VALUE` | `AmGrpGrid_DataValue` |  |  |  |
| 14 | `AM.GGR.REFERENCE` | `AmGrpGrid_Reference` |  |  |  |
| 15 | `AM.GGR.REBALANCE` | `AmGrpGrid_Rebalance` |  |  |  |
| 16 | `AM.GGR.APPLICATION` | `AmGrpGrid_Application` |  |  |  |
| 17 | `AM.GGR.OPTION` | `AmGrpGrid_Option` |  |  |  |
| 18 | `AM.GGR.CODE` | `AmGrpGrid_Code` |  |  |  |
| 19 | `AM.GGR.ALLOC.RATE` | `AmGrpGrid_AllocRate` |  |  |  |
| 20 | `AM.GGR.VALUATION` | `AmGrpGrid_Valuation` |  |  |  |
| 21 | `AM.GGR.NOMINAL` | `AmGrpGrid_Nominal` |  |  |  |
| 22 | `AM.GGR.MODEL.VALUE` | `AmGrpGrid_ModelValue` |  |  |  |
| 23 | `AM.GGR.AM.GRID.ID` | `AmGrpGrid_AmGridId` |  |  |  |
| 24 | `AM.GGR.PREFER.VALUE` | `AmGrpGrid_PreferValue` |  |  |  |
| 25 | `AM.GGR.SELL.SECURITIES` | `AmGrpGrid_SellSecurities` |  |  |  |
