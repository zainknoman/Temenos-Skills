# FS.GA.DEBIT.CREDIT.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GA.DEBIT.CREDIT.MASTER` in `FS_DebitCredit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DEBIT.CREDIT.MASTER.PARENT.REF.ID` | `FsGaDebitCreditMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.DEBIT.CREDIT.MASTER.ORA.ROWID` | `FsGaDebitCreditMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.DEBIT.CREDIT.MASTER.FUND.ID` | `FsGaDebitCreditMaster_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.DEBIT.CREDIT.MASTER.MANAGER.CODE` | `FsGaDebitCreditMaster_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 5 | `FS.GA.DEBIT.CREDIT.MASTER.TRANSACTION.NUMBER` | `FsGaDebitCreditMaster_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 6 | `FS.GA.DEBIT.CREDIT.MASTER.DESCRIPTION` | `FsGaDebitCreditMaster_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GA.DEBIT.CREDIT.MASTER.ACCOUNTING.DATE` | `FsGaDebitCreditMaster_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 8 | `FS.GA.DEBIT.CREDIT.MASTER.STATUS.CODE` | `FsGaDebitCreditMaster_StatusCode` | TField |  | Status Code Multifonds DB Column is STATUS. |
| 9 | `FS.GA.DEBIT.CREDIT.MASTER.SERVICE.CODE` | `FsGaDebitCreditMaster_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 10 | `FS.GA.DEBIT.CREDIT.MASTER.LINE` | `FsGaDebitCreditMaster_Line` | TField |  | Line Multifonds DB Column is NLIGNE. |
| 11 | `FS.GA.DEBIT.CREDIT.MASTER.STATUS.PENDING` | `FsGaDebitCreditMaster_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 12 | `FS.GA.DEBIT.CREDIT.MASTER.EXTERNAL.REFERENCE` | `FsGaDebitCreditMaster_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 13 | `FS.GA.DEBIT.CREDIT.MASTER.OPERATION.CODE` | `FsGaDebitCreditMaster_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 14 | `FS.GA.DEBIT.CREDIT.MASTER.TRADE.DATE` | `FsGaDebitCreditMaster_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 15 | `FS.GA.DEBIT.CREDIT.MASTER.SETTLE.DATE` | `FsGaDebitCreditMaster_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 16 | `FS.GA.DEBIT.CREDIT.MASTER.FUND.STRATEGY` | `FsGaDebitCreditMaster_FundStrategy` | TField |  | Fund Strategy Multifonds DB Column is FUND_STRATEGY. |
| 17 | `FS.GA.DEBIT.CREDIT.MASTER.FUND.LINK.ID` | `FsGaDebitCreditMaster_FundLinkId` | TField |  | Fund Link ID Multifonds DB Column is FUND_LINK_ID. |
| 18 | `FS.GA.DEBIT.CREDIT.MASTER.AC.EXTERNAL.REFERENCE` | `FsGaDebitCreditMaster_AcExternalReference` | TField |  | Unique external reference of the AC transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE_AC. |
| 19 | `FS.GA.DEBIT.CREDIT.MASTER.CHECK.DATE` | `FsGaDebitCreditMaster_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 20 | `FS.GA.DEBIT.CREDIT.MASTER.CHECKED.BY` | `FsGaDebitCreditMaster_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 21 | `FS.GA.DEBIT.CREDIT.MASTER.RESERVED10` | `FsGaDebitCreditMaster_Reserved10` | TField |  |  |
| 22 | `FS.GA.DEBIT.CREDIT.MASTER.RESERVED9` | `FsGaDebitCreditMaster_Reserved9` | TField |  |  |
| 23 | `FS.GA.DEBIT.CREDIT.MASTER.RESERVED8` | `FsGaDebitCreditMaster_Reserved8` | TField |  |  |
| 24 | `FS.GA.DEBIT.CREDIT.MASTER.RESERVED7` | `FsGaDebitCreditMaster_Reserved7` | TField |  |  |
| 25 | `FS.GA.DEBIT.CREDIT.MASTER.RESERVED6` | `FsGaDebitCreditMaster_Reserved6` | TField |  |  |
| 26 | `FS.GA.DEBIT.CREDIT.MASTER.RESERVED5` | `FsGaDebitCreditMaster_Reserved5` | TField |  |  |
| 27 | `FS.GA.DEBIT.CREDIT.MASTER.RESERVED4` | `FsGaDebitCreditMaster_Reserved4` | TField |  |  |
| 28 | `FS.GA.DEBIT.CREDIT.MASTER.RESERVED3` | `FsGaDebitCreditMaster_Reserved3` | TField |  |  |
| 29 | `FS.GA.DEBIT.CREDIT.MASTER.RESERVED2` | `FsGaDebitCreditMaster_Reserved2` | TField |  |  |
| 30 | `FS.GA.DEBIT.CREDIT.MASTER.RESERVED1` | `FsGaDebitCreditMaster_Reserved1` | TField |  |  |
| 31 | `FS.GA.DEBIT.CREDIT.MASTER.LOCAL.REF` | `FsGaDebitCreditMaster_LocalRef` |  |  |  |
| 32 | `FS.GA.DEBIT.CREDIT.MASTER.OVERRIDE` | `FsGaDebitCreditMaster_Override` |  |  |  |
| 33 | `FS.GA.DEBIT.CREDIT.MASTER.RECORD.STATUS` | `FsGaDebitCreditMaster_RecordStatus` | String |  |  |
| 34 | `FS.GA.DEBIT.CREDIT.MASTER.CURR.NO` | `FsGaDebitCreditMaster_CurrNo` | String |  |  |
| 35 | `FS.GA.DEBIT.CREDIT.MASTER.INPUTTER` | `FsGaDebitCreditMaster_Inputter` |  |  |  |
| 36 | `FS.GA.DEBIT.CREDIT.MASTER.DATE.TIME` | `FsGaDebitCreditMaster_DateTime` |  |  |  |
| 37 | `FS.GA.DEBIT.CREDIT.MASTER.AUTHORISER` | `FsGaDebitCreditMaster_Authoriser` | String |  |  |
| 38 | `FS.GA.DEBIT.CREDIT.MASTER.CO.CODE` | `FsGaDebitCreditMaster_CoCode` | String |  |  |
| 39 | `FS.GA.DEBIT.CREDIT.MASTER.DEPT.CODE` | `FsGaDebitCreditMaster_DeptCode` | String |  |  |
| 40 | `FS.GA.DEBIT.CREDIT.MASTER.AUDITOR.CODE` | `FsGaDebitCreditMaster_AuditorCode` | String |  |  |
| 41 | `FS.GA.DEBIT.CREDIT.MASTER.AUDIT.DATE.TIME` | `FsGaDebitCreditMaster_AuditDateTime` | String |  |  |
