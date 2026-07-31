# FS.GA.OPTION.TRANSACTION.BOOK — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPTION.TRANSACTION.BOOK` in `FS_OptionTransaction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPTION.TRANSACTION.BOOK.PARENT.REF.ID` | `FsGaOptionTransactionBook_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.OPTION.TRANSACTION.BOOK.ORA.ROWID` | `FsGaOptionTransactionBook_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.OPTION.TRANSACTION.BOOK.FUND.ID` | `FsGaOptionTransactionBook_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.OPTION.TRANSACTION.BOOK.TRANSACTION.NUMBER` | `FsGaOptionTransactionBook_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.OPTION.TRANSACTION.BOOK.SERVICE.CODE` | `FsGaOptionTransactionBook_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 6 | `FS.GA.OPTION.TRANSACTION.BOOK.OPERATION.TYPE` | `FsGaOptionTransactionBook_OperationType` | TField |  | Refers to the transaction type like booking, rebooking, continuing a contract, etc Multifonds DB Column is OPERATION_TYPE. |
| 7 | `FS.GA.OPTION.TRANSACTION.BOOK.RESERVED10` | `FsGaOptionTransactionBook_Reserved10` | TField |  |  |
| 8 | `FS.GA.OPTION.TRANSACTION.BOOK.RESERVED9` | `FsGaOptionTransactionBook_Reserved9` | TField |  |  |
| 9 | `FS.GA.OPTION.TRANSACTION.BOOK.RESERVED8` | `FsGaOptionTransactionBook_Reserved8` | TField |  |  |
| 10 | `FS.GA.OPTION.TRANSACTION.BOOK.RESERVED7` | `FsGaOptionTransactionBook_Reserved7` | TField |  |  |
| 11 | `FS.GA.OPTION.TRANSACTION.BOOK.RESERVED6` | `FsGaOptionTransactionBook_Reserved6` | TField |  |  |
| 12 | `FS.GA.OPTION.TRANSACTION.BOOK.RESERVED5` | `FsGaOptionTransactionBook_Reserved5` | TField |  |  |
| 13 | `FS.GA.OPTION.TRANSACTION.BOOK.RESERVED4` | `FsGaOptionTransactionBook_Reserved4` | TField |  |  |
| 14 | `FS.GA.OPTION.TRANSACTION.BOOK.RESERVED3` | `FsGaOptionTransactionBook_Reserved3` | TField |  |  |
| 15 | `FS.GA.OPTION.TRANSACTION.BOOK.RESERVED2` | `FsGaOptionTransactionBook_Reserved2` | TField |  |  |
| 16 | `FS.GA.OPTION.TRANSACTION.BOOK.RESERVED1` | `FsGaOptionTransactionBook_Reserved1` | TField |  |  |
| 17 | `FS.GA.OPTION.TRANSACTION.BOOK.LOCAL.REF` | `FsGaOptionTransactionBook_LocalRef` |  |  |  |
| 18 | `FS.GA.OPTION.TRANSACTION.BOOK.OVERRIDE` | `FsGaOptionTransactionBook_Override` |  |  |  |
| 19 | `FS.GA.OPTION.TRANSACTION.BOOK.RECORD.STATUS` | `FsGaOptionTransactionBook_RecordStatus` | String |  |  |
| 20 | `FS.GA.OPTION.TRANSACTION.BOOK.CURR.NO` | `FsGaOptionTransactionBook_CurrNo` | String |  |  |
| 21 | `FS.GA.OPTION.TRANSACTION.BOOK.INPUTTER` | `FsGaOptionTransactionBook_Inputter` |  |  |  |
| 22 | `FS.GA.OPTION.TRANSACTION.BOOK.DATE.TIME` | `FsGaOptionTransactionBook_DateTime` |  |  |  |
| 23 | `FS.GA.OPTION.TRANSACTION.BOOK.AUTHORISER` | `FsGaOptionTransactionBook_Authoriser` | String |  |  |
| 24 | `FS.GA.OPTION.TRANSACTION.BOOK.CO.CODE` | `FsGaOptionTransactionBook_CoCode` | String |  |  |
| 25 | `FS.GA.OPTION.TRANSACTION.BOOK.DEPT.CODE` | `FsGaOptionTransactionBook_DeptCode` | String |  |  |
| 26 | `FS.GA.OPTION.TRANSACTION.BOOK.AUDITOR.CODE` | `FsGaOptionTransactionBook_AuditorCode` | String |  |  |
| 27 | `FS.GA.OPTION.TRANSACTION.BOOK.AUDIT.DATE.TIME` | `FsGaOptionTransactionBook_AuditDateTime` | String |  |  |
