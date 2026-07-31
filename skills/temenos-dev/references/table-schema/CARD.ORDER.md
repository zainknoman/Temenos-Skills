# CARD.ORDER — Table Schema

> Source: `INSERTS/I_F.CARD.ORDER` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAOR.TMP.CUSTOMER` | `CardOrder_TmpCustomer` | TField |  | Purpose of the field to indicate a dummy customer used for ordering cards.Validation - Valid record in CUSTOMER Table.While issuing a card from inventory, customer ID to be updated to the actual customer to whom the card is issued. |
| 2 | `CAOR.TMP.ACCOUNT` | `CardOrder_TmpAccount` | TField |  | Purpose of the field to indicate a temporary account used for ordering cards.Validation - Valid record in ACCOUNT Table. |
| 3 | `CAOR.ORDER.QUANTITY` | `CardOrder_OrderQuantity` | TField |  | Field to indicate the number of Card's to be Ordered.Validations : Numeric value. Allowed up to 999999999.When the number of cards in the inventory goes below the minimum quantity, system orders the card with the quantity defined in this field.Eg.ORDER.QUANTITY: 10MINIMUM.QUANTITY: 5When the number of cards in the inventory goes below 5, system order the cards with quantity 10. |
| 4 | `CAOR.MINIMUM.QUANTITY` | `CardOrder_MinimumQuantity` | TField |  | Field to indicate the minimum number of Card's to maintain before Auto Reorder.Validations : Numeric value. Allowed up to 999999999.Minimum number of cards in the inventory to be maintained.Eg.ORDER.QUANTITY: 10MINIMUM.QUANTITY: 5When the number of cards in the inventory goes below 5, system order the cards with quantity 10. |
| 5 | `CAOR.CURRENT.QUANTITY` | `CardOrder_CurrentQuantity` | TField |  | Field to indicate the current quantity of the cards in the inventory.If the current quantity reaches the minimum quantity, system order the number of cards defined in ORDER.QUANTITY. |
| 6 | `CAOR.ORDER.STATUS` | `CardOrder_OrderStatus` |  |  |  |
| 7 | `CAOR.ORDER.DATE.TIME` | `CardOrder_OrderDateTime` |  |  |  |
| 8 | `CAOR.MSG.POSTED` | `CardOrder_MsgPosted` |  |  |  |
| 9 | `CAOR.AUTO.REORDER.QTY` | `CardOrder_AutoReorderQty` | TField |  | Field to indicate the number of Card's to Reorder when the current quantity reaches the minimum quantity.Current quanitity defined in CURRENT.QUANTITY field and minimum quantity in MINIMUM.QUANTITY field. |
| 10 | `CAOR.TOT.ORDERED.NOS` | `CardOrder_TotOrderedNos` | TField |  | Field to indicate the total number of Ordered Cards.Validations : Numeric value. Allowed up to 999999999. |
| 11 | `CAOR.TOT.DELIVERED.NOS` | `CardOrder_TotDeliveredNos` | TField |  | Field to indicate the total number of Delivered Cards.Validations : Numeric value. Allowed up to 999999999. |
| 12 | `CAOR.OUT.DIR` | `CardOrder_OutDir` | TField |  | Out Directory for File to Vendor.Reserved for future use. |
| 13 | `CAOR.LOG.DIR` | `CardOrder_LogDir` | TField |  | Log Dir for the Extract and FTP.Reserved for future use. |
| 14 | `CAOR.LOCAL.REF` | `CardOrder_LocalRef` |  |  |  |
| 15 | `CAOR.OVERRIDE` | `CardOrder_Override` |  |  |  |
| 16 | `CAOR.NAME` | `CardOrder_Name` | TField |  | Field is used to hold the Name of card holder. |
| 17 | `CAOR.ADDRESS` | `CardOrder_Address` | TField |  | Field is used to Hold the address of the bank. |
| 18 | `CAOR.RESERVED.3` | `CardOrder_Reserved3` | TField |  |  |
| 19 | `CAOR.RESERVED.4` | `CardOrder_Reserved4` | TField |  |  |
| 20 | `CAOR.RESERVED.5` | `CardOrder_Reserved5` | TField |  |  |
| 21 | `CAOR.RESERVED.6` | `CardOrder_Reserved6` | TField |  |  |
| 22 | `CAOR.RESERVED.7` | `CardOrder_Reserved7` | TField |  |  |
| 23 | `CAOR.RESERVED.8` | `CardOrder_Reserved8` | TField |  |  |
| 24 | `CAOR.RESERVED.9` | `CardOrder_Reserved9` | TField |  |  |
| 25 | `CAOR.RESERVED.10` | `CardOrder_Reserved10` | TField |  |  |
| 26 | `CAOR.RESERVED.11` | `CardOrder_Reserved11` | TField |  |  |
| 27 | `CAOR.RESERVED.12` | `CardOrder_Reserved12` | TField |  |  |
| 28 | `CAOR.RESERVED.13` | `CardOrder_Reserved13` | TField |  |  |
| 29 | `CAOR.RESERVED.14` | `CardOrder_Reserved14` | TField |  |  |
| 30 | `CAOR.RESERVED.15` | `CardOrder_Reserved15` | TField |  |  |
| 31 | `CAOR.RECORD.STATUS` | `CardOrder_RecordStatus` | String |  |  |
| 32 | `CAOR.CURR.NO` | `CardOrder_CurrNo` | String |  |  |
| 33 | `CAOR.INPUTTER` | `CardOrder_Inputter` |  |  |  |
| 34 | `CAOR.DATE.TIME` | `CardOrder_DateTime` |  |  |  |
| 35 | `CAOR.AUTHORISER` | `CardOrder_Authoriser` | String |  |  |
| 36 | `CAOR.CO.CODE` | `CardOrder_CoCode` | String |  |  |
| 37 | `CAOR.DEPT.CODE` | `CardOrder_DeptCode` | String |  |  |
| 38 | `CAOR.AUDITOR.CODE` | `CardOrder_AuditorCode` | String |  |  |
| 39 | `CAOR.AUDIT.DATE.TIME` | `CardOrder_AuditDateTime` | String |  |  |
