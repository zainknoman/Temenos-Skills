# FS.GA.ACCOUNT.MOVEMENTS — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNT.MOVEMENTS` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ACCOUNT.MOVEMENTS.PARENT.REF.ID` | `FsGaAccountMovements_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.ACCOUNT.MOVEMENTS.ORA.ROWID` | `FsGaAccountMovements_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.ACCOUNT.MOVEMENTS.FUND.ID` | `FsGaAccountMovements_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.ACCOUNT.MOVEMENTS.GL.ACCOUNT` | `FsGaAccountMovements_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.ACCOUNT.MOVEMENTS.GL.ACCOUNT.SUFFIX` | `FsGaAccountMovements_GlAccountSuffix` | TField |  | Suffix number tagged to the GL account number. In case of cash this identifies the correspondent and for other P&amp;L accounts it provides a more granular split. Multifonds DB Column is NSUFF. |
| 6 | `FS.GA.ACCOUNT.MOVEMENTS.LOCAL.CURRENCY` | `FsGaAccountMovements_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 7 | `FS.GA.ACCOUNT.MOVEMENTS.PAY.DATE` | `FsGaAccountMovements_PayDate` | TField |  | Pay Date Multifonds DB Column is DVAL. |
| 8 | `FS.GA.ACCOUNT.MOVEMENTS.NEXT` | `FsGaAccountMovements_Next` | TField |  | Next Multifonds DB Column is NEXT. |
| 9 | `FS.GA.ACCOUNT.MOVEMENTS.DEBIT.CREDIT.INDICATOR` | `FsGaAccountMovements_DebitCreditIndicator` | TField |  | Debit credit indicator tagged to an account number Multifonds DB Column is CSENS. |
| 10 | `FS.GA.ACCOUNT.MOVEMENTS.DESCRIPTION` | `FsGaAccountMovements_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 11 | `FS.GA.ACCOUNT.MOVEMENTS.ACCOUNTING.DATE` | `FsGaAccountMovements_AccountingDate` | TField |  | Accounting date of the transaction Multifonds DB Column is DJOURNAL. |
| 12 | `FS.GA.ACCOUNT.MOVEMENTS.SETTLE.DATE` | `FsGaAccountMovements_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 13 | `FS.GA.ACCOUNT.MOVEMENTS.TRADE.DATE` | `FsGaAccountMovements_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 14 | `FS.GA.ACCOUNT.MOVEMENTS.SERVICE.CODE` | `FsGaAccountMovements_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 15 | `FS.GA.ACCOUNT.MOVEMENTS.TRANSACTION.NUMBER` | `FsGaAccountMovements_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 16 | `FS.GA.ACCOUNT.MOVEMENTS.LINE` | `FsGaAccountMovements_Line` | TField |  | Line Multifonds DB Column is NLIGNE. |
| 17 | `FS.GA.ACCOUNT.MOVEMENTS.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaAccountMovements_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 18 | `FS.GA.ACCOUNT.MOVEMENTS.STATUS.CODE` | `FsGaAccountMovements_StatusCode` | TField |  | Status Code Multifonds DB Column is STATUS. |
| 19 | `FS.GA.ACCOUNT.MOVEMENTS.FUND.AMOUNT` | `FsGaAccountMovements_FundAmount` | TField |  | Fund Amount Multifonds DB Column is MNTPTF. |
| 20 | `FS.GA.ACCOUNT.MOVEMENTS.FACC` | `FsGaAccountMovements_Facc` | TField |  | Facc Multifonds DB Column is FACC. |
| 21 | `FS.GA.ACCOUNT.MOVEMENTS.ACCOUNT.VALUE` | `FsGaAccountMovements_AccountValue` | TField |  | Account Value Multifonds DB Column is NRUBR_VAL. |
| 22 | `FS.GA.ACCOUNT.MOVEMENTS.SECURITY.LOT.NUMBER` | `FsGaAccountMovements_SecurityLotNumber` | TField |  | Security Lot Number. Multifonds DB Column is NCONTRAT_VAL. |
| 23 | `FS.GA.ACCOUNT.MOVEMENTS.TRANSACTION.TYPE.VAL` | `FsGaAccountMovements_TransactionTypeVal` | TField |  | Transaction Type Val Multifonds DB Column is COPER_VAL. |
| 24 | `FS.GA.ACCOUNT.MOVEMENTS.ARCHIVE` | `FsGaAccountMovements_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 25 | `FS.GA.ACCOUNT.MOVEMENTS.ACCOUNT.BALANCE` | `FsGaAccountMovements_AccountBalance` | TField |  | Account Balance Multifonds DB Column is MSOLDE. |
| 26 | `FS.GA.ACCOUNT.MOVEMENTS.ACCOUNT.BALANCE.IN.FUND.CCY` | `FsGaAccountMovements_AccountBalanceInFundCcy` | TField |  | Account Balance In Fund Ccy Multifonds DB Column is MSPTF. |
| 27 | `FS.GA.ACCOUNT.MOVEMENTS.RATE.OF.EXCHANGE` | `FsGaAccountMovements_RateOfExchange` | TField |  | Exchange rate Multifonds DB Column is TCHG. |
| 28 | `FS.GA.ACCOUNT.MOVEMENTS.MANAGER.CODE` | `FsGaAccountMovements_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 29 | `FS.GA.ACCOUNT.MOVEMENTS.MT950` | `FsGaAccountMovements_Mt950` | TField |  | MT950 Identifier Multifonds DB Column is FLG_MT950. |
| 30 | `FS.GA.ACCOUNT.MOVEMENTS.FUND.ENTRY.NUMBER` | `FsGaAccountMovements_FundEntryNumber` | TField |  | Entry number of the fund Multifonds DB Column is NECRITUR_PTF. |
| 31 | `FS.GA.ACCOUNT.MOVEMENTS.EXECUTION.TIMESTAMP` | `FsGaAccountMovements_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 32 | `FS.GA.ACCOUNT.MOVEMENTS.IFRS.TAG` | `FsGaAccountMovements_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 33 | `FS.GA.ACCOUNT.MOVEMENTS.SPECIFIC.JOURNAL.ID` | `FsGaAccountMovements_SpecificJournalId` | TField |  | Specific Journal ID Multifonds DB Column is SPECIFIC_J_ID. |
| 34 | `FS.GA.ACCOUNT.MOVEMENTS.CORRESPONDENT` | `FsGaAccountMovements_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 35 | `FS.GA.ACCOUNT.MOVEMENTS.MANUAL.REVERSAL` | `FsGaAccountMovements_ManualReversal` | TField |  | Manual Reversal Flag Multifonds DB Column is FLG_MANUAL_REV. |
| 36 | `FS.GA.ACCOUNT.MOVEMENTS.ACTUAL.CREATED.DATE` | `FsGaAccountMovements_ActualCreatedDate` | TField |  | Actual Created Date Multifonds DB Column is DCREATE_ACTUAL. |
| 37 | `FS.GA.ACCOUNT.MOVEMENTS.ACTUAL.AMOUNT` | `FsGaAccountMovements_ActualAmount` | TField |  | Actual Amount Multifonds DB Column is MONTANT_ACTUAL. |
| 38 | `FS.GA.ACCOUNT.MOVEMENTS.SYSTEM.REVERSAL` | `FsGaAccountMovements_SystemReversal` | TField |  | System Reversal Identifier Multifonds DB Column is FLG_SYS_REV. |
| 39 | `FS.GA.ACCOUNT.MOVEMENTS.TRANSACTION.TYPE.TRANS` | `FsGaAccountMovements_TransactionTypeTrans` | TField |  | Transaction Type Trans Multifonds DB Column is COPER_TRANS. |
| 40 | `FS.GA.ACCOUNT.MOVEMENTS.SHARE.CLASS.CODE` | `FsGaAccountMovements_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 41 | `FS.GA.ACCOUNT.MOVEMENTS.ACCOUNT.DESCRIPTION` | `FsGaAccountMovements_AccountDescription` | TField |  | Account Description Multifonds DB Column is NRUBR_DESC. |
| 42 | `FS.GA.ACCOUNT.MOVEMENTS.INSTRUMENT.GROUP` | `FsGaAccountMovements_InstrumentGroup` | TField |  | Instrument Group Multifonds DB Column is INSTRUMENT_GROUP. |
| 43 | `FS.GA.ACCOUNT.MOVEMENTS.ID.OF.INSTRUMENT` | `FsGaAccountMovements_IdOfInstrument` | TField |  | Instrument ID Multifonds DB Column is INSTRUMENT_ID. |
| 44 | `FS.GA.ACCOUNT.MOVEMENTS.DESCRIPTION.OF.INSTRUMENT` | `FsGaAccountMovements_DescriptionOfInstrument` | TField |  | Instrument Description Multifonds DB Column is INSTRUMENT_DESC. |
| 45 | `FS.GA.ACCOUNT.MOVEMENTS.RESERVED10` | `FsGaAccountMovements_Reserved10` | TField |  |  |
| 46 | `FS.GA.ACCOUNT.MOVEMENTS.RESERVED9` | `FsGaAccountMovements_Reserved9` | TField |  |  |
| 47 | `FS.GA.ACCOUNT.MOVEMENTS.RESERVED8` | `FsGaAccountMovements_Reserved8` | TField |  |  |
| 48 | `FS.GA.ACCOUNT.MOVEMENTS.RESERVED7` | `FsGaAccountMovements_Reserved7` | TField |  |  |
| 49 | `FS.GA.ACCOUNT.MOVEMENTS.RESERVED6` | `FsGaAccountMovements_Reserved6` | TField |  |  |
| 50 | `FS.GA.ACCOUNT.MOVEMENTS.RESERVED5` | `FsGaAccountMovements_Reserved5` | TField |  |  |
| 51 | `FS.GA.ACCOUNT.MOVEMENTS.RESERVED4` | `FsGaAccountMovements_Reserved4` | TField |  |  |
| 52 | `FS.GA.ACCOUNT.MOVEMENTS.RESERVED3` | `FsGaAccountMovements_Reserved3` | TField |  |  |
| 53 | `FS.GA.ACCOUNT.MOVEMENTS.RESERVED2` | `FsGaAccountMovements_Reserved2` | TField |  |  |
| 54 | `FS.GA.ACCOUNT.MOVEMENTS.RESERVED1` | `FsGaAccountMovements_Reserved1` | TField |  |  |
| 55 | `FS.GA.ACCOUNT.MOVEMENTS.LOCAL.REF` | `FsGaAccountMovements_LocalRef` |  |  |  |
| 56 | `FS.GA.ACCOUNT.MOVEMENTS.OVERRIDE` | `FsGaAccountMovements_Override` |  |  |  |
| 57 | `FS.GA.ACCOUNT.MOVEMENTS.RECORD.STATUS` | `FsGaAccountMovements_RecordStatus` | String |  |  |
| 58 | `FS.GA.ACCOUNT.MOVEMENTS.CURR.NO` | `FsGaAccountMovements_CurrNo` | String |  |  |
| 59 | `FS.GA.ACCOUNT.MOVEMENTS.INPUTTER` | `FsGaAccountMovements_Inputter` |  |  |  |
| 60 | `FS.GA.ACCOUNT.MOVEMENTS.DATE.TIME` | `FsGaAccountMovements_DateTime` |  |  |  |
| 61 | `FS.GA.ACCOUNT.MOVEMENTS.AUTHORISER` | `FsGaAccountMovements_Authoriser` | String |  |  |
| 62 | `FS.GA.ACCOUNT.MOVEMENTS.CO.CODE` | `FsGaAccountMovements_CoCode` | String |  |  |
| 63 | `FS.GA.ACCOUNT.MOVEMENTS.DEPT.CODE` | `FsGaAccountMovements_DeptCode` | String |  |  |
| 64 | `FS.GA.ACCOUNT.MOVEMENTS.AUDITOR.CODE` | `FsGaAccountMovements_AuditorCode` | String |  |  |
| 65 | `FS.GA.ACCOUNT.MOVEMENTS.AUDIT.DATE.TIME` | `FsGaAccountMovements_AuditDateTime` | String |  |  |
