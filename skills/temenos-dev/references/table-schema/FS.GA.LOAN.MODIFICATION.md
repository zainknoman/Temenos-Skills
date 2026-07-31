# FS.GA.LOAN.MODIFICATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.LOAN.MODIFICATION` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LOAN.MODIFICATION.FUND.ID` | `FsGaLoanModification_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.LOAN.MODIFICATION.LOT.NUMBER` | `FsGaLoanModification_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 3 | `FS.GA.LOAN.MODIFICATION.TRANSACTION.NUMBER` | `FsGaLoanModification_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 4 | `FS.GA.LOAN.MODIFICATION.SETTLE.DATE` | `FsGaLoanModification_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 5 | `FS.GA.LOAN.MODIFICATION.OPERATION.CODE` | `FsGaLoanModification_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 6 | `FS.GA.LOAN.MODIFICATION.DEAL.STATUS.CODE` | `FsGaLoanModification_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 7 | `FS.GA.LOAN.MODIFICATION.OLD.AMOUNT.OF.LOAN` | `FsGaLoanModification_OldAmountOfLoan` | TField |  | It refers to the old amount of Loan before changing the loan amount Multifonds DB Column is MONTANT_EMP_BF. |
| 8 | `FS.GA.LOAN.MODIFICATION.NEW.AMOUNT.OF.LOAN` | `FsGaLoanModification_NewAmountOfLoan` | TField |  | It refers to the New Amount of Loan after changing the loan amount Multifonds DB Column is MONTANT_EMP_AF. |
| 9 | `FS.GA.LOAN.MODIFICATION.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaLoanModification_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 10 | `FS.GA.LOAN.MODIFICATION.DEAL.FEES.AMOUNT` | `FsGaLoanModification_DealFeesAmount` | TField |  | Deal Fees Amount Multifonds DB Column is MFRAIS. |
| 11 | `FS.GA.LOAN.MODIFICATION.ACCRUED.INTEREST` | `FsGaLoanModification_AccruedInterest` | TField |  | Accrued interest of the security Multifonds DB Column is MINT. |
| 12 | `FS.GA.LOAN.MODIFICATION.STATUS.PENDING` | `FsGaLoanModification_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 13 | `FS.GA.LOAN.MODIFICATION.EXTERNAL.REFERENCE` | `FsGaLoanModification_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 14 | `FS.GA.LOAN.MODIFICATION.ARCHIVE` | `FsGaLoanModification_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 15 | `FS.GA.LOAN.MODIFICATION.TRADE.DATE` | `FsGaLoanModification_TradeDate` | TField |  | Trade date of the trnsaction Multifonds DB Column is DOPER. |
| 16 | `FS.GA.LOAN.MODIFICATION.ACCOUNTING.DATE` | `FsGaLoanModification_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 17 | `FS.GA.LOAN.MODIFICATION.DEAL.CURRENCY` | `FsGaLoanModification_DealCurrency` | TField |  | Currency of settlement or currency of deal Multifonds DB Column is CDEV. |
| 18 | `FS.GA.LOAN.MODIFICATION.DESCRIPTION` | `FsGaLoanModification_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 19 | `FS.GA.LOAN.MODIFICATION.CHECKED.BY` | `FsGaLoanModification_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 20 | `FS.GA.LOAN.MODIFICATION.CHECK.DATE` | `FsGaLoanModification_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 21 | `FS.GA.LOAN.MODIFICATION.RESERVED10` | `FsGaLoanModification_Reserved10` | TField |  |  |
| 22 | `FS.GA.LOAN.MODIFICATION.RESERVED9` | `FsGaLoanModification_Reserved9` | TField |  |  |
| 23 | `FS.GA.LOAN.MODIFICATION.RESERVED8` | `FsGaLoanModification_Reserved8` | TField |  |  |
| 24 | `FS.GA.LOAN.MODIFICATION.RESERVED7` | `FsGaLoanModification_Reserved7` | TField |  |  |
| 25 | `FS.GA.LOAN.MODIFICATION.RESERVED6` | `FsGaLoanModification_Reserved6` | TField |  |  |
| 26 | `FS.GA.LOAN.MODIFICATION.RESERVED5` | `FsGaLoanModification_Reserved5` | TField |  |  |
| 27 | `FS.GA.LOAN.MODIFICATION.RESERVED4` | `FsGaLoanModification_Reserved4` | TField |  |  |
| 28 | `FS.GA.LOAN.MODIFICATION.RESERVED3` | `FsGaLoanModification_Reserved3` | TField |  |  |
| 29 | `FS.GA.LOAN.MODIFICATION.RESERVED2` | `FsGaLoanModification_Reserved2` | TField |  |  |
| 30 | `FS.GA.LOAN.MODIFICATION.RESERVED1` | `FsGaLoanModification_Reserved1` | TField |  |  |
| 31 | `FS.GA.LOAN.MODIFICATION.RECORD.STATUS` | `FsGaLoanModification_RecordStatus` | String |  |  |
| 32 | `FS.GA.LOAN.MODIFICATION.CURR.NO` | `FsGaLoanModification_CurrNo` | String |  |  |
| 33 | `FS.GA.LOAN.MODIFICATION.INPUTTER` | `FsGaLoanModification_Inputter` |  |  |  |
| 34 | `FS.GA.LOAN.MODIFICATION.DATE.TIME` | `FsGaLoanModification_DateTime` |  |  |  |
| 35 | `FS.GA.LOAN.MODIFICATION.AUTHORISER` | `FsGaLoanModification_Authoriser` | String |  |  |
| 36 | `FS.GA.LOAN.MODIFICATION.CO.CODE` | `FsGaLoanModification_CoCode` | String |  |  |
| 37 | `FS.GA.LOAN.MODIFICATION.DEPT.CODE` | `FsGaLoanModification_DeptCode` | String |  |  |
| 38 | `FS.GA.LOAN.MODIFICATION.AUDITOR.CODE` | `FsGaLoanModification_AuditorCode` | String |  |  |
| 39 | `FS.GA.LOAN.MODIFICATION.AUDIT.DATE.TIME` | `FsGaLoanModification_AuditDateTime` | String |  |  |
