# FS.GA.DEPOSIT.BOOK — Table Schema

> Source: `INSERTS/I_F.FS.GA.DEPOSIT.BOOK` in `FS_Deposit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DEPOSIT.BOOK.PARENT.REF.ID` | `FsGaDepositBook_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.DEPOSIT.BOOK.ORA.ROWID` | `FsGaDepositBook_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.DEPOSIT.BOOK.FUND.ID` | `FsGaDepositBook_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.DEPOSIT.BOOK.TRANSACTION.NUMBER` | `FsGaDepositBook_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.DEPOSIT.BOOK.SERVICE.CODE` | `FsGaDepositBook_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 6 | `FS.GA.DEPOSIT.BOOK.OPERATION.TYPE` | `FsGaDepositBook_OperationType` | TField |  | Refers to the transaction type like booking, rebooking, continuing a contract, etc Multifonds DB Column is OPERATION_TYPE. |
| 7 | `FS.GA.DEPOSIT.BOOK.RESERVED10` | `FsGaDepositBook_Reserved10` | TField |  |  |
| 8 | `FS.GA.DEPOSIT.BOOK.RESERVED9` | `FsGaDepositBook_Reserved9` | TField |  |  |
| 9 | `FS.GA.DEPOSIT.BOOK.RESERVED8` | `FsGaDepositBook_Reserved8` | TField |  |  |
| 10 | `FS.GA.DEPOSIT.BOOK.RESERVED7` | `FsGaDepositBook_Reserved7` | TField |  |  |
| 11 | `FS.GA.DEPOSIT.BOOK.RESERVED6` | `FsGaDepositBook_Reserved6` | TField |  |  |
| 12 | `FS.GA.DEPOSIT.BOOK.RESERVED5` | `FsGaDepositBook_Reserved5` | TField |  |  |
| 13 | `FS.GA.DEPOSIT.BOOK.RESERVED4` | `FsGaDepositBook_Reserved4` | TField |  |  |
| 14 | `FS.GA.DEPOSIT.BOOK.RESERVED3` | `FsGaDepositBook_Reserved3` | TField |  |  |
| 15 | `FS.GA.DEPOSIT.BOOK.RESERVED2` | `FsGaDepositBook_Reserved2` | TField |  |  |
| 16 | `FS.GA.DEPOSIT.BOOK.RESERVED1` | `FsGaDepositBook_Reserved1` | TField |  |  |
| 17 | `FS.GA.DEPOSIT.BOOK.LOCAL.REF` | `FsGaDepositBook_LocalRef` |  |  |  |
| 18 | `FS.GA.DEPOSIT.BOOK.OVERRIDE` | `FsGaDepositBook_Override` |  |  |  |
| 19 | `FS.GA.DEPOSIT.BOOK.RECORD.STATUS` | `FsGaDepositBook_RecordStatus` | String |  |  |
| 20 | `FS.GA.DEPOSIT.BOOK.CURR.NO` | `FsGaDepositBook_CurrNo` | String |  |  |
| 21 | `FS.GA.DEPOSIT.BOOK.INPUTTER` | `FsGaDepositBook_Inputter` |  |  |  |
| 22 | `FS.GA.DEPOSIT.BOOK.DATE.TIME` | `FsGaDepositBook_DateTime` |  |  |  |
| 23 | `FS.GA.DEPOSIT.BOOK.AUTHORISER` | `FsGaDepositBook_Authoriser` | String |  |  |
| 24 | `FS.GA.DEPOSIT.BOOK.CO.CODE` | `FsGaDepositBook_CoCode` | String |  |  |
| 25 | `FS.GA.DEPOSIT.BOOK.DEPT.CODE` | `FsGaDepositBook_DeptCode` | String |  |  |
| 26 | `FS.GA.DEPOSIT.BOOK.AUDITOR.CODE` | `FsGaDepositBook_AuditorCode` | String |  |  |
| 27 | `FS.GA.DEPOSIT.BOOK.AUDIT.DATE.TIME` | `FsGaDepositBook_AuditDateTime` | String |  |  |
