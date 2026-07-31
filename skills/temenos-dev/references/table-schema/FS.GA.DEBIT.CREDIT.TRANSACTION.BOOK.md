# FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK — Table Schema

> Source: `INSERTS/I_F.FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK` in `FS_DebitCredit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.PARENT.REF.ID` | `FsGaDebitCreditTransactionBook_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.ORA.ROWID` | `FsGaDebitCreditTransactionBook_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.FUND.ID` | `FsGaDebitCreditTransactionBook_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.TRANSACTION.NUMBER` | `FsGaDebitCreditTransactionBook_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.SERVICE.CODE` | `FsGaDebitCreditTransactionBook_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 6 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.OPERATION.TYPE` | `FsGaDebitCreditTransactionBook_OperationType` | TField |  | Refers to the transaction type like booking, rebooking, continuing a contract, etc Multifonds DB Column is OPERATION_TYPE. |
| 7 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RESERVED10` | `FsGaDebitCreditTransactionBook_Reserved10` | TField |  |  |
| 8 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RESERVED9` | `FsGaDebitCreditTransactionBook_Reserved9` | TField |  |  |
| 9 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RESERVED8` | `FsGaDebitCreditTransactionBook_Reserved8` | TField |  |  |
| 10 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RESERVED7` | `FsGaDebitCreditTransactionBook_Reserved7` | TField |  |  |
| 11 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RESERVED6` | `FsGaDebitCreditTransactionBook_Reserved6` | TField |  |  |
| 12 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RESERVED5` | `FsGaDebitCreditTransactionBook_Reserved5` | TField |  |  |
| 13 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RESERVED4` | `FsGaDebitCreditTransactionBook_Reserved4` | TField |  |  |
| 14 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RESERVED3` | `FsGaDebitCreditTransactionBook_Reserved3` | TField |  |  |
| 15 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RESERVED2` | `FsGaDebitCreditTransactionBook_Reserved2` | TField |  |  |
| 16 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RESERVED1` | `FsGaDebitCreditTransactionBook_Reserved1` | TField |  |  |
| 17 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.LOCAL.REF` | `FsGaDebitCreditTransactionBook_LocalRef` |  |  |  |
| 18 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.OVERRIDE` | `FsGaDebitCreditTransactionBook_Override` |  |  |  |
| 19 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.RECORD.STATUS` | `FsGaDebitCreditTransactionBook_RecordStatus` | String |  |  |
| 20 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.CURR.NO` | `FsGaDebitCreditTransactionBook_CurrNo` | String |  |  |
| 21 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.INPUTTER` | `FsGaDebitCreditTransactionBook_Inputter` |  |  |  |
| 22 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.DATE.TIME` | `FsGaDebitCreditTransactionBook_DateTime` |  |  |  |
| 23 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.AUTHORISER` | `FsGaDebitCreditTransactionBook_Authoriser` | String |  |  |
| 24 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.CO.CODE` | `FsGaDebitCreditTransactionBook_CoCode` | String |  |  |
| 25 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.DEPT.CODE` | `FsGaDebitCreditTransactionBook_DeptCode` | String |  |  |
| 26 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.AUDITOR.CODE` | `FsGaDebitCreditTransactionBook_AuditorCode` | String |  |  |
| 27 | `FS.GA.DEBIT.CREDIT.TRANSACTION.BOOK.AUDIT.DATE.TIME` | `FsGaDebitCreditTransactionBook_AuditDateTime` | String |  |  |
