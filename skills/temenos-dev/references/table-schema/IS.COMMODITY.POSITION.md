# IS.COMMODITY.POSITION — Table Schema

> Source: `INSERTS/I_F.IS.COMMODITY.POSITION` in `IS_Purchase.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.CMP.PURCHASE.REF` | `IsCommodityPosition_PurchaseRef` | TField |  | The Contract Reference of the Asset through which the Asset is requested and purchased. |
| 2 | `IS.CMP.COMMODITY` | `IsCommodityPosition_Commodity` | TField |  | The Commodity for which the delivery of goods is being tracked. |
| 3 | `IS.CMP.ASSET.REF` | `IsCommodityPosition_AssetRef` | TField |  | The Asset for which the delivery of goods is being tracked. |
| 4 | `IS.CMP.PURCHASE.QTY` | `IsCommodityPosition_PurchaseQty` | TField |  | The quantity of Asset or Commodity purchased in the Contract. |
| 5 | `IS.CMP.TOT.DELIVERED.QTY` | `IsCommodityPosition_TotDeliveredQty` | TField |  | The total quantity of Asset or Commodity delivered out of the total purchase quantity. |
| 6 | `IS.CMP.TOT.SOLD.QTY` | `IsCommodityPosition_TotSoldQty` | TField |  | The total quantity of Asset or Commodity sold out of the total delivered quantity. |
| 7 | `IS.CMP.AVAILABLE.QTY` | `IsCommodityPosition_AvailableQty` | TField |  | The quantity available for sale. This quantity increases with the delivery and decreases with the reversal or sale. |
| 8 | `IS.CMP.REVERSED.QTY` | `IsCommodityPosition_ReversedQty` | TField |  | The quantity of Asset that are reversed out of the delivered quantity. When the goods delivered are reversed, the quantity available for sale also goes down with the same count. |
| 9 | `IS.CMP.DELIVERED.DATE` | `IsCommodityPosition_DeliveredDate` |  |  |  |
| 10 | `IS.CMP.DELIVERED.QTY` | `IsCommodityPosition_DeliveredQty` |  |  |  |
| 11 | `IS.CMP.RESERVED.12` | `IsCommodityPosition_Reserved12` |  |  |  |
| 12 | `IS.CMP.RESERVED.11` | `IsCommodityPosition_Reserved11` |  |  |  |
| 13 | `IS.CMP.RESERVED.10` | `IsCommodityPosition_Reserved10` |  |  |  |
| 14 | `IS.CMP.RESERVED.9` | `IsCommodityPosition_Reserved9` |  |  |  |
| 15 | `IS.CMP.RESERVED.8` | `IsCommodityPosition_Reserved8` |  |  |  |
| 16 | `IS.CMP.SALE.DATE` | `IsCommodityPosition_SaleDate` |  |  |  |
| 17 | `IS.CMP.DECLARATION.REF` | `IsCommodityPosition_DeclarationRef` |  |  |  |
| 18 | `IS.CMP.SALE.REFERENCE` | `IsCommodityPosition_SaleReference` |  |  |  |
| 19 | `IS.CMP.SOLD.QTY` | `IsCommodityPosition_SoldQty` |  |  |  |
| 20 | `IS.CMP.SOLD.PRICE` | `IsCommodityPosition_SoldPrice` |  |  |  |
| 21 | `IS.CMP.RESERVED.7` | `IsCommodityPosition_Reserved7` |  |  |  |
| 22 | `IS.CMP.RESERVED.6` | `IsCommodityPosition_Reserved6` |  |  |  |
| 23 | `IS.CMP.RESERVED.5` | `IsCommodityPosition_Reserved5` |  |  |  |
| 24 | `IS.CMP.RESERVED.4` | `IsCommodityPosition_Reserved4` |  |  |  |
| 25 | `IS.CMP.RESERVED.3` | `IsCommodityPosition_Reserved3` |  |  |  |
| 26 | `IS.CMP.RESERVED.2` | `IsCommodityPosition_Reserved2` |  |  |  |
| 27 | `IS.CMP.RESERVED.1` | `IsCommodityPosition_Reserved1` |  |  |  |
