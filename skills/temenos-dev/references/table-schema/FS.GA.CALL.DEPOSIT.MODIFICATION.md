# FS.GA.CALL.DEPOSIT.MODIFICATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.CALL.DEPOSIT.MODIFICATION` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CALL.DEPOSIT.MODIFICATION.FUND.ID` | `FsGaCallDepositModification_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.CALL.DEPOSIT.MODIFICATION.LOT.NUMBER` | `FsGaCallDepositModification_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 3 | `FS.GA.CALL.DEPOSIT.MODIFICATION.TRANSACTION.NUMBER` | `FsGaCallDepositModification_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 4 | `FS.GA.CALL.DEPOSIT.MODIFICATION.SETTLE.DATE` | `FsGaCallDepositModification_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 5 | `FS.GA.CALL.DEPOSIT.MODIFICATION.OPERATION.CODE` | `FsGaCallDepositModification_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 6 | `FS.GA.CALL.DEPOSIT.MODIFICATION.DEAL.STATUS.CODE` | `FsGaCallDepositModification_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 7 | `FS.GA.CALL.DEPOSIT.MODIFICATION.OLD.DEPOSIT.AMOUNT` | `FsGaCallDepositModification_OldDepositAmount` | TField |  | Signifies the old amount for deposit modifications Multifonds DB Column is MONTANT_DPO_BF. |
| 8 | `FS.GA.CALL.DEPOSIT.MODIFICATION.NEW.DEPOSIT.AMOUNT` | `FsGaCallDepositModification_NewDepositAmount` | TField |  | Signifies the new amount for deposit modifications Multifonds DB Column is MONTANT_DPO_AF. |
| 9 | `FS.GA.CALL.DEPOSIT.MODIFICATION.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaCallDepositModification_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 10 | `FS.GA.CALL.DEPOSIT.MODIFICATION.DEAL.FEES.AMOUNT` | `FsGaCallDepositModification_DealFeesAmount` | TField |  | Deal Fees Amount Multifonds DB Column is MFRAIS. |
| 11 | `FS.GA.CALL.DEPOSIT.MODIFICATION.ACCRUED.INTEREST` | `FsGaCallDepositModification_AccruedInterest` | TField |  | Accrued interest of the security Multifonds DB Column is MINT. |
| 12 | `FS.GA.CALL.DEPOSIT.MODIFICATION.ARCHIVE` | `FsGaCallDepositModification_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 13 | `FS.GA.CALL.DEPOSIT.MODIFICATION.TRADE.DATE` | `FsGaCallDepositModification_TradeDate` | TField |  | Trade date of the trnsaction Multifonds DB Column is DOPER. |
| 14 | `FS.GA.CALL.DEPOSIT.MODIFICATION.ACCOUNTING.DATE` | `FsGaCallDepositModification_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 15 | `FS.GA.CALL.DEPOSIT.MODIFICATION.IMPOT.AMOUNT` | `FsGaCallDepositModification_ImpotAmount` | TField |  | Impot Amount Multifonds DB Column is MNT_IMPOT. |
| 16 | `FS.GA.CALL.DEPOSIT.MODIFICATION.TAX.AMOUNT` | `FsGaCallDepositModification_TaxAmount` | TField |  | Tax Amount Multifonds DB Column is MNT_IMPOT_DEV. |
| 17 | `FS.GA.CALL.DEPOSIT.MODIFICATION.IMPOT.CURRENCY` | `FsGaCallDepositModification_ImpotCurrency` | TField |  | Tax currency of the income Multifonds DB Column is CMON_IMPOT. |
| 18 | `FS.GA.CALL.DEPOSIT.MODIFICATION.EXCHANGE.RATE.BETWEEN.CCY` | `FsGaCallDepositModification_ExchangeRateBetweenCcy` | TField |  | Exchange rate between settlement currency and tax currency Multifonds DB Column is TCHG_IMPOT. |
| 19 | `FS.GA.CALL.DEPOSIT.MODIFICATION.STATUS.PENDING` | `FsGaCallDepositModification_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 20 | `FS.GA.CALL.DEPOSIT.MODIFICATION.EXTERNAL.REFERENCE` | `FsGaCallDepositModification_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 21 | `FS.GA.CALL.DEPOSIT.MODIFICATION.SERVICE.CODE` | `FsGaCallDepositModification_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 22 | `FS.GA.CALL.DEPOSIT.MODIFICATION.INTERNAL.REFERENCE.NUMBER` | `FsGaCallDepositModification_InternalReferenceNumber` | TField |  | Internal Reference Number for Deposits/Loans Multifonds DB Column is DEAL_ID. |
| 23 | `FS.GA.CALL.DEPOSIT.MODIFICATION.DEAL.CURRENCY` | `FsGaCallDepositModification_DealCurrency` | TField |  | Currency of settlement or currency of deal Multifonds DB Column is CDEV. |
| 24 | `FS.GA.CALL.DEPOSIT.MODIFICATION.IFRS.TAG` | `FsGaCallDepositModification_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 25 | `FS.GA.CALL.DEPOSIT.MODIFICATION.CHECKED.BY` | `FsGaCallDepositModification_CheckedBy` | TField |  | Checked By Multifonds DB Column is CHECKED_BY. |
| 26 | `FS.GA.CALL.DEPOSIT.MODIFICATION.CHECK.DATE` | `FsGaCallDepositModification_CheckDate` | TField |  | Check Date Multifonds DB Column is DCHECKED. |
| 27 | `FS.GA.CALL.DEPOSIT.MODIFICATION.LOCAL.SETTLE.VCI` | `FsGaCallDepositModification_LocalSettleVci` | TField |  | Local Settle VCI Multifonds DB Column is LOC_SETTL_VCI. |
| 28 | `FS.GA.CALL.DEPOSIT.MODIFICATION.FUND.SETTLEMENT.VCI` | `FsGaCallDepositModification_FundSettlementVci` | TField |  | Fund Settlement Vci Multifonds DB Column is SETTL_PTF_VCI. |
| 29 | `FS.GA.CALL.DEPOSIT.MODIFICATION.FUND.VCI.LOC` | `FsGaCallDepositModification_FundVciLoc` | TField |  | Fund VCI Loc Multifonds DB Column is LOC_PTF_VCI. |
| 30 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RESERVED10` | `FsGaCallDepositModification_Reserved10` | TField |  |  |
| 31 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RESERVED9` | `FsGaCallDepositModification_Reserved9` | TField |  |  |
| 32 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RESERVED8` | `FsGaCallDepositModification_Reserved8` | TField |  |  |
| 33 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RESERVED7` | `FsGaCallDepositModification_Reserved7` | TField |  |  |
| 34 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RESERVED6` | `FsGaCallDepositModification_Reserved6` | TField |  |  |
| 35 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RESERVED5` | `FsGaCallDepositModification_Reserved5` | TField |  |  |
| 36 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RESERVED4` | `FsGaCallDepositModification_Reserved4` | TField |  |  |
| 37 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RESERVED3` | `FsGaCallDepositModification_Reserved3` | TField |  |  |
| 38 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RESERVED2` | `FsGaCallDepositModification_Reserved2` | TField |  |  |
| 39 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RESERVED1` | `FsGaCallDepositModification_Reserved1` | TField |  |  |
| 40 | `FS.GA.CALL.DEPOSIT.MODIFICATION.RECORD.STATUS` | `FsGaCallDepositModification_RecordStatus` | String |  |  |
| 41 | `FS.GA.CALL.DEPOSIT.MODIFICATION.CURR.NO` | `FsGaCallDepositModification_CurrNo` | String |  |  |
| 42 | `FS.GA.CALL.DEPOSIT.MODIFICATION.INPUTTER` | `FsGaCallDepositModification_Inputter` |  |  |  |
| 43 | `FS.GA.CALL.DEPOSIT.MODIFICATION.DATE.TIME` | `FsGaCallDepositModification_DateTime` |  |  |  |
| 44 | `FS.GA.CALL.DEPOSIT.MODIFICATION.AUTHORISER` | `FsGaCallDepositModification_Authoriser` | String |  |  |
| 45 | `FS.GA.CALL.DEPOSIT.MODIFICATION.CO.CODE` | `FsGaCallDepositModification_CoCode` | String |  |  |
| 46 | `FS.GA.CALL.DEPOSIT.MODIFICATION.DEPT.CODE` | `FsGaCallDepositModification_DeptCode` | String |  |  |
| 47 | `FS.GA.CALL.DEPOSIT.MODIFICATION.AUDITOR.CODE` | `FsGaCallDepositModification_AuditorCode` | String |  |  |
| 48 | `FS.GA.CALL.DEPOSIT.MODIFICATION.AUDIT.DATE.TIME` | `FsGaCallDepositModification_AuditDateTime` | String |  |  |
