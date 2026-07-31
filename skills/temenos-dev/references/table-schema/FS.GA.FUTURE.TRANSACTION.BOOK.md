# FS.GA.FUTURE.TRANSACTION.BOOK — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUTURE.TRANSACTION.BOOK` in `FS_FutureTransaction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUTURE.TRANSACTION.BOOK.PARENT.REF.ID` | `FsGaFutureTransactionBook_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUTURE.TRANSACTION.BOOK.ORA.ROWID` | `FsGaFutureTransactionBook_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUTURE.TRANSACTION.BOOK.FUND.ID` | `FsGaFutureTransactionBook_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FUTURE.TRANSACTION.BOOK.TRANSACTION.NUMBER` | `FsGaFutureTransactionBook_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.FUTURE.TRANSACTION.BOOK.SERVICE.CODE` | `FsGaFutureTransactionBook_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 6 | `FS.GA.FUTURE.TRANSACTION.BOOK.OPERATION.TYPE` | `FsGaFutureTransactionBook_OperationType` | TField |  | Refers to the transaction type like booking, rebooking, continuing a contract, etc Multifonds DB Column is OPERATION_TYPE. |
| 7 | `FS.GA.FUTURE.TRANSACTION.BOOK.RESERVED10` | `FsGaFutureTransactionBook_Reserved10` | TField |  |  |
| 8 | `FS.GA.FUTURE.TRANSACTION.BOOK.RESERVED9` | `FsGaFutureTransactionBook_Reserved9` | TField |  |  |
| 9 | `FS.GA.FUTURE.TRANSACTION.BOOK.RESERVED8` | `FsGaFutureTransactionBook_Reserved8` | TField |  |  |
| 10 | `FS.GA.FUTURE.TRANSACTION.BOOK.RESERVED7` | `FsGaFutureTransactionBook_Reserved7` | TField |  |  |
| 11 | `FS.GA.FUTURE.TRANSACTION.BOOK.RESERVED6` | `FsGaFutureTransactionBook_Reserved6` | TField |  |  |
| 12 | `FS.GA.FUTURE.TRANSACTION.BOOK.RESERVED5` | `FsGaFutureTransactionBook_Reserved5` | TField |  |  |
| 13 | `FS.GA.FUTURE.TRANSACTION.BOOK.RESERVED4` | `FsGaFutureTransactionBook_Reserved4` | TField |  |  |
| 14 | `FS.GA.FUTURE.TRANSACTION.BOOK.RESERVED3` | `FsGaFutureTransactionBook_Reserved3` | TField |  |  |
| 15 | `FS.GA.FUTURE.TRANSACTION.BOOK.RESERVED2` | `FsGaFutureTransactionBook_Reserved2` | TField |  |  |
| 16 | `FS.GA.FUTURE.TRANSACTION.BOOK.RESERVED1` | `FsGaFutureTransactionBook_Reserved1` | TField |  |  |
| 17 | `FS.GA.FUTURE.TRANSACTION.BOOK.LOCAL.REF` | `FsGaFutureTransactionBook_LocalRef` |  |  |  |
| 18 | `FS.GA.FUTURE.TRANSACTION.BOOK.OVERRIDE` | `FsGaFutureTransactionBook_Override` |  |  |  |
| 19 | `FS.GA.FUTURE.TRANSACTION.BOOK.RECORD.STATUS` | `FsGaFutureTransactionBook_RecordStatus` | String |  |  |
| 20 | `FS.GA.FUTURE.TRANSACTION.BOOK.CURR.NO` | `FsGaFutureTransactionBook_CurrNo` | String |  |  |
| 21 | `FS.GA.FUTURE.TRANSACTION.BOOK.INPUTTER` | `FsGaFutureTransactionBook_Inputter` |  |  |  |
| 22 | `FS.GA.FUTURE.TRANSACTION.BOOK.DATE.TIME` | `FsGaFutureTransactionBook_DateTime` |  |  |  |
| 23 | `FS.GA.FUTURE.TRANSACTION.BOOK.AUTHORISER` | `FsGaFutureTransactionBook_Authoriser` | String |  |  |
| 24 | `FS.GA.FUTURE.TRANSACTION.BOOK.CO.CODE` | `FsGaFutureTransactionBook_CoCode` | String |  |  |
| 25 | `FS.GA.FUTURE.TRANSACTION.BOOK.DEPT.CODE` | `FsGaFutureTransactionBook_DeptCode` | String |  |  |
| 26 | `FS.GA.FUTURE.TRANSACTION.BOOK.AUDITOR.CODE` | `FsGaFutureTransactionBook_AuditorCode` | String |  |  |
| 27 | `FS.GA.FUTURE.TRANSACTION.BOOK.AUDIT.DATE.TIME` | `FsGaFutureTransactionBook_AuditDateTime` | String |  |  |
