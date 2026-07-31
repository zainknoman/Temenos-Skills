# FS.GA.LOAN.TRANSACTION.BOOK — Table Schema

> Source: `INSERTS/I_F.FS.GA.LOAN.TRANSACTION.BOOK` in `FS_Loan.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LOAN.TRANSACTION.BOOK.PARENT.REF.ID` | `FsGaLoanTransactionBook_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.LOAN.TRANSACTION.BOOK.ORA.ROWID` | `FsGaLoanTransactionBook_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.LOAN.TRANSACTION.BOOK.FUND.ID` | `FsGaLoanTransactionBook_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.LOAN.TRANSACTION.BOOK.TRANSACTION.NUMBER` | `FsGaLoanTransactionBook_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.LOAN.TRANSACTION.BOOK.SERVICE.CODE` | `FsGaLoanTransactionBook_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 6 | `FS.GA.LOAN.TRANSACTION.BOOK.OPERATION.TYPE` | `FsGaLoanTransactionBook_OperationType` | TField |  | Refers to the transaction type like booking, rebooking, continuing a contract, etc Multifonds DB Column is OPERATION_TYPE. |
| 7 | `FS.GA.LOAN.TRANSACTION.BOOK.RESERVED10` | `FsGaLoanTransactionBook_Reserved10` | TField |  |  |
| 8 | `FS.GA.LOAN.TRANSACTION.BOOK.RESERVED9` | `FsGaLoanTransactionBook_Reserved9` | TField |  |  |
| 9 | `FS.GA.LOAN.TRANSACTION.BOOK.RESERVED8` | `FsGaLoanTransactionBook_Reserved8` | TField |  |  |
| 10 | `FS.GA.LOAN.TRANSACTION.BOOK.RESERVED7` | `FsGaLoanTransactionBook_Reserved7` | TField |  |  |
| 11 | `FS.GA.LOAN.TRANSACTION.BOOK.RESERVED6` | `FsGaLoanTransactionBook_Reserved6` | TField |  |  |
| 12 | `FS.GA.LOAN.TRANSACTION.BOOK.RESERVED5` | `FsGaLoanTransactionBook_Reserved5` | TField |  |  |
| 13 | `FS.GA.LOAN.TRANSACTION.BOOK.RESERVED4` | `FsGaLoanTransactionBook_Reserved4` | TField |  |  |
| 14 | `FS.GA.LOAN.TRANSACTION.BOOK.RESERVED3` | `FsGaLoanTransactionBook_Reserved3` | TField |  |  |
| 15 | `FS.GA.LOAN.TRANSACTION.BOOK.RESERVED2` | `FsGaLoanTransactionBook_Reserved2` | TField |  |  |
| 16 | `FS.GA.LOAN.TRANSACTION.BOOK.RESERVED1` | `FsGaLoanTransactionBook_Reserved1` | TField |  |  |
| 17 | `FS.GA.LOAN.TRANSACTION.BOOK.LOCAL.REF` | `FsGaLoanTransactionBook_LocalRef` |  |  |  |
| 18 | `FS.GA.LOAN.TRANSACTION.BOOK.OVERRIDE` | `FsGaLoanTransactionBook_Override` |  |  |  |
| 19 | `FS.GA.LOAN.TRANSACTION.BOOK.RECORD.STATUS` | `FsGaLoanTransactionBook_RecordStatus` | String |  |  |
| 20 | `FS.GA.LOAN.TRANSACTION.BOOK.CURR.NO` | `FsGaLoanTransactionBook_CurrNo` | String |  |  |
| 21 | `FS.GA.LOAN.TRANSACTION.BOOK.INPUTTER` | `FsGaLoanTransactionBook_Inputter` |  |  |  |
| 22 | `FS.GA.LOAN.TRANSACTION.BOOK.DATE.TIME` | `FsGaLoanTransactionBook_DateTime` |  |  |  |
| 23 | `FS.GA.LOAN.TRANSACTION.BOOK.AUTHORISER` | `FsGaLoanTransactionBook_Authoriser` | String |  |  |
| 24 | `FS.GA.LOAN.TRANSACTION.BOOK.CO.CODE` | `FsGaLoanTransactionBook_CoCode` | String |  |  |
| 25 | `FS.GA.LOAN.TRANSACTION.BOOK.DEPT.CODE` | `FsGaLoanTransactionBook_DeptCode` | String |  |  |
| 26 | `FS.GA.LOAN.TRANSACTION.BOOK.AUDITOR.CODE` | `FsGaLoanTransactionBook_AuditorCode` | String |  |  |
| 27 | `FS.GA.LOAN.TRANSACTION.BOOK.AUDIT.DATE.TIME` | `FsGaLoanTransactionBook_AuditDateTime` | String |  |  |
