# FS.GA.SHAREHOLDER.TRANSACTION.BOOK — Table Schema

> Source: `INSERTS/I_F.FS.GA.SHAREHOLDER.TRANSACTION.BOOK` in `FS_Capstock.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.PARENT.REF.ID` | `FsGaShareholderTransactionBook_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.ORA.ROWID` | `FsGaShareholderTransactionBook_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.FUND.ID` | `FsGaShareholderTransactionBook_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.TRANSACTION.NUMBER` | `FsGaShareholderTransactionBook_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.SERVICE.CODE` | `FsGaShareholderTransactionBook_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 6 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.OPERATION.TYPE` | `FsGaShareholderTransactionBook_OperationType` | TField |  | Refers to the transaction type like booking, rebooking, continuing a contract, etc Multifonds DB Column is OPERATION_TYPE. |
| 7 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RESERVED10` | `FsGaShareholderTransactionBook_Reserved10` | TField |  |  |
| 8 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RESERVED9` | `FsGaShareholderTransactionBook_Reserved9` | TField |  |  |
| 9 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RESERVED8` | `FsGaShareholderTransactionBook_Reserved8` | TField |  |  |
| 10 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RESERVED7` | `FsGaShareholderTransactionBook_Reserved7` | TField |  |  |
| 11 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RESERVED6` | `FsGaShareholderTransactionBook_Reserved6` | TField |  |  |
| 12 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RESERVED5` | `FsGaShareholderTransactionBook_Reserved5` | TField |  |  |
| 13 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RESERVED4` | `FsGaShareholderTransactionBook_Reserved4` | TField |  |  |
| 14 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RESERVED3` | `FsGaShareholderTransactionBook_Reserved3` | TField |  |  |
| 15 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RESERVED2` | `FsGaShareholderTransactionBook_Reserved2` | TField |  |  |
| 16 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RESERVED1` | `FsGaShareholderTransactionBook_Reserved1` | TField |  |  |
| 17 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.LOCAL.REF` | `FsGaShareholderTransactionBook_LocalRef` |  |  |  |
| 18 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.OVERRIDE` | `FsGaShareholderTransactionBook_Override` |  |  |  |
| 19 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.RECORD.STATUS` | `FsGaShareholderTransactionBook_RecordStatus` | String |  |  |
| 20 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.CURR.NO` | `FsGaShareholderTransactionBook_CurrNo` | String |  |  |
| 21 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.INPUTTER` | `FsGaShareholderTransactionBook_Inputter` |  |  |  |
| 22 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.DATE.TIME` | `FsGaShareholderTransactionBook_DateTime` |  |  |  |
| 23 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.AUTHORISER` | `FsGaShareholderTransactionBook_Authoriser` | String |  |  |
| 24 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.CO.CODE` | `FsGaShareholderTransactionBook_CoCode` | String |  |  |
| 25 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.DEPT.CODE` | `FsGaShareholderTransactionBook_DeptCode` | String |  |  |
| 26 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.AUDITOR.CODE` | `FsGaShareholderTransactionBook_AuditorCode` | String |  |  |
| 27 | `FS.GA.SHAREHOLDER.TRANSACTION.BOOK.AUDIT.DATE.TIME` | `FsGaShareholderTransactionBook_AuditDateTime` | String |  |  |
