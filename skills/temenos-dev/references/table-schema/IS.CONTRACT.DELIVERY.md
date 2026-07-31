# IS.CONTRACT.DELIVERY — Table Schema

> Source: `INSERTS/I_F.IS.CONTRACT.DELIVERY` in `IS_Purchase.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.DEL.CUSTOMER` | `IsContractDelivery_Customer` | TField |  | The Contract Customer who delivers the Asset. Validation Rules: 1. Field No-input. 2. Defaulted from the corresponding IS.CONTRACT record. 3. Must be a valid record in the table CUSTOMER. |
| 2 | `IS.DEL.PURCHASE.REF` | `IsContractDelivery_PurchaseRef` | TField |  | The Contract through which the Customer initiated the Asset Request. Validation Rules: 1. Field No-input. 2. Defaulted from ID of the current record. 2. Must be a valid record from the table IS.CONTRACT. |
| 3 | `IS.DEL.PRODUCT` | `IsContractDelivery_Product` | TField |  | The Islamic Product on which the customer requests the Asset. Validation Rules: 1. Field No-input. 2. Defaulted from the corresponding IS.CONTRACT record. 3. Must be a valid record from the table IS.PARAMETER. |
| 4 | `IS.DEL.COMMODITY` | `IsContractDelivery_Commodity` | TField |  | The Commodity for which the goods are being delivered. Validation Rules: 1. Field No-input. 2. Defaulted from ID of the current record. 3. Must be a valid entry in the IS.COMMODITY table. 4. Allowed only for Quantified Assets. 5. Fields COMMODITY and ASSET.REF are mutually exclusive. |
| 5 | `IS.DEL.ASSET.REF` | `IsContractDelivery_AssetRef` | TField |  | The Asset for which the goods are being delivered. Validation Rules: 1. Field No-input. 2. Defaulted from ID of the current record. 3. Must be a valid record in the Asset table defined in the Commodity record. 4. Fields COMMODITY and ASSET.REF are mutually exclusive. |
| 6 | `IS.DEL.CURRENCY` | `IsContractDelivery_Currency` | TField |  | The Currency in which the Asset Request contract is booked. Validation Rules: 1. Field No-input. 2. Defaulted from the IS.CONTRACT record. 2. Must be a valid record in the table CURRENCY. |
| 7 | `IS.DEL.UNIT.PRICE` | `IsContractDelivery_UnitPrice` | TField |  | Unit Price of the Asset or Commodity as captured in the IS.CONTRACT Validation Rules: 1. Field No-input. 2. Defaulted from the corresponding IS.CONTRACT record. |
| 8 | `IS.DEL.PURCHASE.QTY` | `IsContractDelivery_PurchaseQty` | TField |  | The quantity of Asset or Commodity purchased in the Contract. Validation Rules: 1. Field No-input. 2. Defaulted from the corresponding IS.CONTRACT record. |
| 9 | `IS.DEL.PURCHASE.PRICE` | `IsContractDelivery_PurchasePrice` | TField |  | The Total Purchase Price of the Asset or Commodity being delivered. Validation Rules: 1. Field No-input. 2. Defaulted from the corresponding IS.CONTRACT record. |
| 10 | `IS.DEL.TOT.DELIVERED.QTY` | `IsContractDelivery_TotDeliveredQty` | TField |  | The total quantity of Asset or Commodity delivered out of the total purchase quantity. Validation Rules: 1. Field No-input. |
| 11 | `IS.DEL.PENDING.QTY` | `IsContractDelivery_PendingQty` | TField |  | The pending quantity of the Asset or Commodity yet to be delivered out of the total purchase quantity. Validation Rules: 1. Field No-input. 2. Defaulted from the IS.COMMODITY.POSITION record |
| 12 | `IS.DEL.DELIVERY.DATE` | `IsContractDelivery_DeliveryDate` | TField | Yes | The date on which the goods are delivered. The value in this field gets cleared off after authorisation of the contract. Validation Rules: 1. Field Mandatory. 2. Defaulted to TODAY. 3. Cannot be future dated. 4. Standard T24 Date field. |
| 13 | `IS.DEL.DELIVER.QTY` | `IsContractDelivery_DeliverQty` | TField | Yes | The quantity of Asset or Commodity being delivered on the given Delivery Date. The value in this field gets cleared off after authorisation of the contract. Validation Rules: 1. Either Deliver Qty or Reverse Qty is mandatory. 2. Both Deliver Qty and Reverse Qty are not allowed. |
| 14 | `IS.DEL.REVERSE.QTY` | `IsContractDelivery_ReverseQty` | TField | Yes | The quantity of Asset or Commodity being reversed on the given Delivery Date. The value in this field gets cleared off after authorisation of the contract. Validation Rules: 1. Either Deliver Qty or Reverse Qty is mandatory. 2. Both Deliver Qty and Reverse Qty are not allowed. |
| 15 | `IS.DEL.RESERVED.15` | `IsContractDelivery_Reserved15` | TField |  |  |
| 16 | `IS.DEL.RESERVED.14` | `IsContractDelivery_Reserved14` | TField |  |  |
| 17 | `IS.DEL.RESERVED.13` | `IsContractDelivery_Reserved13` | TField |  |  |
| 18 | `IS.DEL.RESERVED.12` | `IsContractDelivery_Reserved12` | TField |  |  |
| 19 | `IS.DEL.RESERVED.11` | `IsContractDelivery_Reserved11` | TField |  |  |
| 20 | `IS.DEL.RESERVED.10` | `IsContractDelivery_Reserved10` | TField |  |  |
| 21 | `IS.DEL.RESERVED.9` | `IsContractDelivery_Reserved9` | TField |  |  |
| 22 | `IS.DEL.RESERVED.8` | `IsContractDelivery_Reserved8` | TField |  |  |
| 23 | `IS.DEL.RESERVED.7` | `IsContractDelivery_Reserved7` | TField |  |  |
| 24 | `IS.DEL.RESERVED.6` | `IsContractDelivery_Reserved6` | TField |  |  |
| 25 | `IS.DEL.RESERVED.5` | `IsContractDelivery_Reserved5` | TField |  |  |
| 26 | `IS.DEL.RESERVED.4` | `IsContractDelivery_Reserved4` | TField |  |  |
| 27 | `IS.DEL.RESERVED.3` | `IsContractDelivery_Reserved3` | TField |  |  |
| 28 | `IS.DEL.RESERVED.2` | `IsContractDelivery_Reserved2` | TField |  |  |
| 29 | `IS.DEL.RESERVED.1` | `IsContractDelivery_Reserved1` | TField |  |  |
| 30 | `IS.DEL.LOCAL.REF` | `IsContractDelivery_LocalRef` |  |  |  |
| 31 | `IS.DEL.STMT.NOS` | `IsContractDelivery_StmtNos` |  |  |  |
| 32 | `IS.DEL.OVERRIDE` | `IsContractDelivery_Override` |  |  |  |
| 33 | `IS.DEL.RECORD.STATUS` | `IsContractDelivery_RecordStatus` | String |  |  |
| 34 | `IS.DEL.CURR.NO` | `IsContractDelivery_CurrNo` | String |  |  |
| 35 | `IS.DEL.INPUTTER` | `IsContractDelivery_Inputter` |  |  |  |
| 36 | `IS.DEL.DATE.TIME` | `IsContractDelivery_DateTime` |  |  |  |
| 37 | `IS.DEL.AUTHORISER` | `IsContractDelivery_Authoriser` | String |  |  |
| 38 | `IS.DEL.CO.CODE` | `IsContractDelivery_CoCode` | String |  |  |
| 39 | `IS.DEL.DEPT.CODE` | `IsContractDelivery_DeptCode` | String |  |  |
| 40 | `IS.DEL.AUDITOR.CODE` | `IsContractDelivery_AuditorCode` | String |  |  |
| 41 | `IS.DEL.AUDIT.DATE.TIME` | `IsContractDelivery_AuditDateTime` | String |  |  |
