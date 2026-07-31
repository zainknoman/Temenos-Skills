# IS.COMMODITY.SALE — Table Schema

> Source: `INSERTS/I_F.IS.COMMODITY.SALE` in `IS_Purchase.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.CMS.CUSTOMER` | `IsCommoditySale_Customer` | TField | Yes | The Customer for whom the Sale is placed with/without differential pricing. Validation Rules: 1. Field Mandatory. 2. Must be a valid record in the table CUSTOMER. |
| 2 | `IS.CMS.CURRENCY` | `IsCommoditySale_Currency` | TField | Yes | The Currency in which the Asset Request contract is booked. Validation Rules: 1. Field Mandatory. 2. Must be a valid record in the table CURRENCY. |
| 3 | `IS.CMS.VALUE.DATE` | `IsCommoditySale_ValueDate` | TField |  | Value Date on which the Sale Contract is agreed. Validation Rules: 1. Standard T24 Date field. 2. Cannot be future dated. |
| 4 | `IS.CMS.REQ.TYPE` | `IsCommoditySale_ReqType` | TField |  | The type of request that the sale is placed for. This field will opened during Bulk Trading Features are enhanced. |
| 5 | `IS.CMS.REQ.COMMODITY` | `IsCommoditySale_ReqCommodity` | TField | Yes | The Commodity for which the goods are being delivered. Validation Rules: 1. Field Mandatory. 2. Must be a valid record from the table IS.COMMODITY. |
| 6 | `IS.CMS.REQ.QUANTITY` | `IsCommoditySale_ReqQuantity` | TField | Yes | The quantity of the Commodity being sold. Validation Rules: 1. Field Mandatory. |
| 7 | `IS.CMS.REQ.PRIORITY` | `IsCommoditySale_ReqPriority` | TField |  | The method through which the commodity can be selected for Commodity Trading from the available commodity. This field will opened during Bulk Trading Features are enhanced. |
| 8 | `IS.CMS.PRODUCT` | `IsCommoditySale_Product` | TField | Yes | The Islamic Product in which the asset request is processed. Validation Rules: 1. Field Mandatory. 2. Must be a valid record from the table IS.PARAMETER. |
| 9 | `IS.CMS.PURCHASE.REF` | `IsCommoditySale_PurchaseRef` |  |  |  |
| 10 | `IS.CMS.ASSET.REF` | `IsCommoditySale_AssetRef` |  |  |  |
| 11 | `IS.CMS.UNIT.PRICE` | `IsCommoditySale_UnitPrice` |  |  |  |
| 12 | `IS.CMS.PURCHASE.QTY` | `IsCommoditySale_PurchaseQty` |  |  |  |
| 13 | `IS.CMS.TOT.DELIVERED.QTY` | `IsCommoditySale_TotDeliveredQty` |  |  |  |
| 14 | `IS.CMS.TOT.SOLD.QTY` | `IsCommoditySale_TotSoldQty` |  |  |  |
| 15 | `IS.CMS.SALE.UNIT.PRICE` | `IsCommoditySale_SaleUnitPrice` |  |  |  |
| 16 | `IS.CMS.SALE.QTY` | `IsCommoditySale_SaleQty` |  |  |  |
| 17 | `IS.CMS.SALE.PRICE` | `IsCommoditySale_SalePrice` |  |  |  |
| 18 | `IS.CMS.ORIG.SALE.PRICE` | `IsCommoditySale_OrigSalePrice` |  |  |  |
| 19 | `IS.CMS.ASSET.SALE.PRICE` | `IsCommoditySale_AssetSalePrice` |  |  |  |
| 20 | `IS.CMS.PURCHASE.PRICE` | `IsCommoditySale_PurchasePrice` |  |  |  |
| 21 | `IS.CMS.RESERVED.20` | `IsCommoditySale_Reserved20` |  |  |  |
| 22 | `IS.CMS.RESERVED.19` | `IsCommoditySale_Reserved19` |  |  |  |
| 23 | `IS.CMS.RESERVED.18` | `IsCommoditySale_Reserved18` |  |  |  |
| 24 | `IS.CMS.RESERVED.17` | `IsCommoditySale_Reserved17` |  |  |  |
| 25 | `IS.CMS.RESERVED.16` | `IsCommoditySale_Reserved16` |  |  |  |
| 26 | `IS.CMS.TOT.SALE.QTY` | `IsCommoditySale_TotSaleQty` | TField |  | The Total Number of quantities declared for Sale. Validation Rules: 1. Field No-input. |
| 27 | `IS.CMS.TOT.ORIG.PRICE` | `IsCommoditySale_TotOrigPrice` | TField |  | The Total Price of the Asset/commodity with UNIT.PRICE defined in the Asset Request contract. Validation Rules: 1. Field No-input. 2. System defaults the amount that is sum of all the New Sale Prices, i.e., PURCHASE.PRICE |
| 28 | `IS.CMS.TOT.SALE.PRICE` | `IsCommoditySale_TotSalePrice` | TField |  | The Total Sale Price which will be eligible for Finance. This is derived from the new Sale Prices declared. Validation Rules: 1. Field No-input. 2. System defaults the amount that is sum of all the New Sale Prices, i.e., ASSET.SALE.PRICE |
| 29 | `IS.CMS.TXN.PL.AMOUNT` | `IsCommoditySale_TxnPlAmount` | TField |  | The Profit or Loss incurred as a result of declaration of the new Selling Price. If the new Selling Price is same as the original price, then this field will be zero. No PL entry is raised. Validation Rules: 1. Field No-input. 2. System defaults the difference of TOT.SALE.PRICE and TOT.ORIG.PRICE. |
| 30 | `IS.CMS.SALE.REFERENCE` | `IsCommoditySale_SaleReference` | TField |  | The AA arrangement reference is captured in this field when the contract is financed. Validation Rules: 1. Field No-input. |
| 31 | `IS.CMS.RESERVED.15` | `IsCommoditySale_Reserved15` | TField |  |  |
| 32 | `IS.CMS.RESERVED.14` | `IsCommoditySale_Reserved14` | TField |  |  |
| 33 | `IS.CMS.RESERVED.13` | `IsCommoditySale_Reserved13` | TField |  |  |
| 34 | `IS.CMS.RESERVED.12` | `IsCommoditySale_Reserved12` | TField |  |  |
| 35 | `IS.CMS.RESERVED.11` | `IsCommoditySale_Reserved11` | TField |  |  |
| 36 | `IS.CMS.RESERVED.10` | `IsCommoditySale_Reserved10` | TField |  |  |
| 37 | `IS.CMS.RESERVED.9` | `IsCommoditySale_Reserved9` | TField |  |  |
| 38 | `IS.CMS.RESERVED.8` | `IsCommoditySale_Reserved8` | TField |  |  |
| 39 | `IS.CMS.RESERVED.7` | `IsCommoditySale_Reserved7` | TField |  |  |
| 40 | `IS.CMS.RESERVED.6` | `IsCommoditySale_Reserved6` | TField |  |  |
| 41 | `IS.CMS.RESERVED.5` | `IsCommoditySale_Reserved5` | TField |  |  |
| 42 | `IS.CMS.RESERVED.4` | `IsCommoditySale_Reserved4` | TField |  |  |
| 43 | `IS.CMS.RESERVED.3` | `IsCommoditySale_Reserved3` | TField |  |  |
| 44 | `IS.CMS.RESERVED.2` | `IsCommoditySale_Reserved2` | TField |  |  |
| 45 | `IS.CMS.RESERVED.1` | `IsCommoditySale_Reserved1` | TField |  |  |
| 46 | `IS.CMS.LOCAL.REF` | `IsCommoditySale_LocalRef` |  |  |  |
| 47 | `IS.CMS.STMT.NOS` | `IsCommoditySale_StmtNos` |  |  |  |
| 48 | `IS.CMS.OVERRIDE` | `IsCommoditySale_Override` |  |  |  |
| 49 | `IS.CMS.RECORD.STATUS` | `IsCommoditySale_RecordStatus` | String |  |  |
| 50 | `IS.CMS.CURR.NO` | `IsCommoditySale_CurrNo` | String |  |  |
| 51 | `IS.CMS.INPUTTER` | `IsCommoditySale_Inputter` |  |  |  |
| 52 | `IS.CMS.DATE.TIME` | `IsCommoditySale_DateTime` |  |  |  |
| 53 | `IS.CMS.AUTHORISER` | `IsCommoditySale_Authoriser` | String |  |  |
| 54 | `IS.CMS.CO.CODE` | `IsCommoditySale_CoCode` | String |  |  |
| 55 | `IS.CMS.DEPT.CODE` | `IsCommoditySale_DeptCode` | String |  |  |
| 56 | `IS.CMS.AUDITOR.CODE` | `IsCommoditySale_AuditorCode` | String |  |  |
| 57 | `IS.CMS.AUDIT.DATE.TIME` | `IsCommoditySale_AuditDateTime` | String |  |  |
