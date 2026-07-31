# FS.GA.STOCK.TRANSACTION.BOOKING — Table Schema

> Source: `INSERTS/I_F.FS.GA.STOCK.TRANSACTION.BOOKING` in `FS_StockTransaction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.STOCK.TRANSACTION.BOOKING.PARENT.REF.ID` | `FsGaStockTransactionBooking_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.STOCK.TRANSACTION.BOOKING.ORA.ROWID` | `FsGaStockTransactionBooking_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.STOCK.TRANSACTION.BOOKING.FUND.ID` | `FsGaStockTransactionBooking_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.STOCK.TRANSACTION.BOOKING.TRANSACTION.NUMBER` | `FsGaStockTransactionBooking_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.STOCK.TRANSACTION.BOOKING.SERVICE.CODE` | `FsGaStockTransactionBooking_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 6 | `FS.GA.STOCK.TRANSACTION.BOOKING.OPERATION.TYPE` | `FsGaStockTransactionBooking_OperationType` | TField |  | Refers to the transaction type like booking, rebooking, continuing a contract, etc Multifonds DB Column is OPERATION_TYPE. |
| 7 | `FS.GA.STOCK.TRANSACTION.BOOKING.RESERVED10` | `FsGaStockTransactionBooking_Reserved10` | TField |  |  |
| 8 | `FS.GA.STOCK.TRANSACTION.BOOKING.RESERVED9` | `FsGaStockTransactionBooking_Reserved9` | TField |  |  |
| 9 | `FS.GA.STOCK.TRANSACTION.BOOKING.RESERVED8` | `FsGaStockTransactionBooking_Reserved8` | TField |  |  |
| 10 | `FS.GA.STOCK.TRANSACTION.BOOKING.RESERVED7` | `FsGaStockTransactionBooking_Reserved7` | TField |  |  |
| 11 | `FS.GA.STOCK.TRANSACTION.BOOKING.RESERVED6` | `FsGaStockTransactionBooking_Reserved6` | TField |  |  |
| 12 | `FS.GA.STOCK.TRANSACTION.BOOKING.RESERVED5` | `FsGaStockTransactionBooking_Reserved5` | TField |  |  |
| 13 | `FS.GA.STOCK.TRANSACTION.BOOKING.RESERVED4` | `FsGaStockTransactionBooking_Reserved4` | TField |  |  |
| 14 | `FS.GA.STOCK.TRANSACTION.BOOKING.RESERVED3` | `FsGaStockTransactionBooking_Reserved3` | TField |  |  |
| 15 | `FS.GA.STOCK.TRANSACTION.BOOKING.RESERVED2` | `FsGaStockTransactionBooking_Reserved2` | TField |  |  |
| 16 | `FS.GA.STOCK.TRANSACTION.BOOKING.RESERVED1` | `FsGaStockTransactionBooking_Reserved1` | TField |  |  |
| 17 | `FS.GA.STOCK.TRANSACTION.BOOKING.LOCAL.REF` | `FsGaStockTransactionBooking_LocalRef` |  |  |  |
| 18 | `FS.GA.STOCK.TRANSACTION.BOOKING.OVERRIDE` | `FsGaStockTransactionBooking_Override` |  |  |  |
| 19 | `FS.GA.STOCK.TRANSACTION.BOOKING.RECORD.STATUS` | `FsGaStockTransactionBooking_RecordStatus` | String |  |  |
| 20 | `FS.GA.STOCK.TRANSACTION.BOOKING.CURR.NO` | `FsGaStockTransactionBooking_CurrNo` | String |  |  |
| 21 | `FS.GA.STOCK.TRANSACTION.BOOKING.INPUTTER` | `FsGaStockTransactionBooking_Inputter` |  |  |  |
| 22 | `FS.GA.STOCK.TRANSACTION.BOOKING.DATE.TIME` | `FsGaStockTransactionBooking_DateTime` |  |  |  |
| 23 | `FS.GA.STOCK.TRANSACTION.BOOKING.AUTHORISER` | `FsGaStockTransactionBooking_Authoriser` | String |  |  |
| 24 | `FS.GA.STOCK.TRANSACTION.BOOKING.CO.CODE` | `FsGaStockTransactionBooking_CoCode` | String |  |  |
| 25 | `FS.GA.STOCK.TRANSACTION.BOOKING.DEPT.CODE` | `FsGaStockTransactionBooking_DeptCode` | String |  |  |
| 26 | `FS.GA.STOCK.TRANSACTION.BOOKING.AUDITOR.CODE` | `FsGaStockTransactionBooking_AuditorCode` | String |  |  |
| 27 | `FS.GA.STOCK.TRANSACTION.BOOKING.AUDIT.DATE.TIME` | `FsGaStockTransactionBooking_AuditDateTime` | String |  |  |
