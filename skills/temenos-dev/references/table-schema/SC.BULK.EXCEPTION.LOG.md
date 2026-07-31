# SC.BULK.EXCEPTION.LOG — Table Schema

> Source: `INSERTS/I_F.SC.BULK.EXCEPTION.LOG` in `SC_SctServiceBasedOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.BLE.TRADE.DATE` | `ScBulkExceptionLog_TradeDate` | TField |  | This field will hold trade date of parent trade or parent order Validation Rules Valid Date Format |
| 2 | `SC.BLE.VALUE.DATE` | `ScBulkExceptionLog_ValueDate` | TField |  | This field will hold value date of parent trade or parent order Validation Rules Valid Date Format |
| 3 | `SC.BLE.TOTAL.CR.NOM` | `ScBulkExceptionLog_TotalCrNom` | TField |  | This field will hold the total nominal in parent if, parent transaction is customer buy otherwise this field will be total of all child nominal Validation Rules Standard T24 Amount field |
| 4 | `SC.BLE.TOTAL.DR.NOM` | `ScBulkExceptionLog_TotalDrNom` | TField |  | This field will hold the total nominal in parent if, parent transaction is customer sell otherwise this field will be total of all child nominal Validation Rules Standard T24 Amount field |
| 5 | `SC.BLE.TOTAL.CR.INT` | `ScBulkExceptionLog_TotalCrInt` | TField |  | This field will hold the total interest in parent if, parent transaction is customer buy otherwise this field will be total of all child interest Validation Rules Standard T24 amount field. |
| 6 | `SC.BLE.TOTAL.DR.INT` | `ScBulkExceptionLog_TotalDrInt` | TField |  | This field will hold the total interest in parent if, parent transaction is customer buy otherwise this field will be total of all child interest Validation Rules Standard T24 amount field. |
| 7 | `SC.BLE.TRADE.CREATED` | `ScBulkExceptionLog_TradeCreated` | TField |  | This field will hold number of child trades created. Value will be reduced if child trade are deleted or reversed Validation Rules |
| 8 | `SC.BLE.TRADE.AUTHORISED` | `ScBulkExceptionLog_TradeAuthorised` | TField |  | This field will hold number of child trades authorised. Value will be reduced if child trades are reversed or deleted. Validation Rules |
| 9 | `SC.BLE.PARENT.AUTH` | `ScBulkExceptionLog_ParentAuth` | TField |  | Field to determine whether parent is authorised. This field will be reset if parent is reversed. Validation Rules Alphabetical characters |
| 10 | `SC.BLE.STATUS` | `ScBulkExceptionLog_Status` | TField |  | STATUS will be updated as PENDING if parent or child are not authorized. STATUS will be updated as COMPLETED if parent and all child are all authorized.STATUS of TRADED is applicable only for records pertaining to SEC.OPEN.ORDER and will be updated on execution of order Validation Rules Alphabetical characters |
| 11 | `SC.BLE.EXCEPTION` | `ScBulkExceptionLog_Exception` | TField |  | Field to hold common exceptions such as nominal not matching or interest not matching Validation Rules Alphabetical characters |
| 12 | `SC.BLE.EXCEPTION.FLD` | `ScBulkExceptionLog_ExceptionFld` |  |  |  |
| 13 | `SC.BLE.EXCEPTION.TXN` | `ScBulkExceptionLog_ExceptionTxn` |  |  |  |
| 14 | `SC.BLE.PARENT.REFERENCE` | `ScBulkExceptionLog_ParentReference` | TField |  | This field will hold unique reference common to parent and child |
| 15 | `SC.BLE.RESERVED.9` | `ScBulkExceptionLog_Reserved9` | TField |  |  |
| 16 | `SC.BLE.RESERVED.8` | `ScBulkExceptionLog_Reserved8` | TField |  |  |
| 17 | `SC.BLE.RESERVED.7` | `ScBulkExceptionLog_Reserved7` | TField |  |  |
| 18 | `SC.BLE.RESERVED.6` | `ScBulkExceptionLog_Reserved6` | TField |  |  |
| 19 | `SC.BLE.RESERVED.5` | `ScBulkExceptionLog_Reserved5` | TField |  |  |
| 20 | `SC.BLE.RESERVED.4` | `ScBulkExceptionLog_Reserved4` | TField |  |  |
| 21 | `SC.BLE.RESERVED.3` | `ScBulkExceptionLog_Reserved3` | TField |  |  |
| 22 | `SC.BLE.RESERVED.2` | `ScBulkExceptionLog_Reserved2` | TField |  |  |
| 23 | `SC.BLE.RESERVED.1` | `ScBulkExceptionLog_Reserved1` | TField |  |  |
| 24 | `SC.BLE.LOCAL.REF` | `ScBulkExceptionLog_LocalRef` |  |  |  |
| 25 | `SC.BLE.OVERRIDE` | `ScBulkExceptionLog_Override` |  |  |  |
