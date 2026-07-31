# FS.GA.FUTURE.TRANSACTION.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUTURE.TRANSACTION.DETAIL` in `FS_FutureTransaction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUTURE.TRANSACTION.DETAIL.PARENT.REF.ID` | `FsGaFutureTransactionDetail_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUTURE.TRANSACTION.DETAIL.ORA.ROWID` | `FsGaFutureTransactionDetail_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUTURE.TRANSACTION.DETAIL.FUND.ID` | `FsGaFutureTransactionDetail_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FUTURE.TRANSACTION.DETAIL.TRANSACTION.NUMBER` | `FsGaFutureTransactionDetail_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.FUTURE.TRANSACTION.DETAIL.NEXT` | `FsGaFutureTransactionDetail_Next` | TField |  | Next Multifonds DB Column is NEXT. |
| 6 | `FS.GA.FUTURE.TRANSACTION.DETAIL.FUTURE.ID.CODE` | `FsGaFutureTransactionDetail_FutureIdCode` | TField |  | Future, Security,Swap,Derivative,CFD ID Code Multifonds DB Column is NFUT. |
| 7 | `FS.GA.FUTURE.TRANSACTION.DETAIL.LOT.NUMBER` | `FsGaFutureTransactionDetail_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 8 | `FS.GA.FUTURE.TRANSACTION.DETAIL.MANAGER.CODE` | `FsGaFutureTransactionDetail_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 9 | `FS.GA.FUTURE.TRANSACTION.DETAIL.QUANTITY` | `FsGaFutureTransactionDetail_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 10 | `FS.GA.FUTURE.TRANSACTION.DETAIL.TRANSAC.PRICE` | `FsGaFutureTransactionDetail_TransacPrice` | TField |  | This field corresponds to the price of the transaction. Enter the price in quotation currency of the New CFN contract (unless the future is quoted in percent). Multifonds DB Column is PRICE. |
| 11 | `FS.GA.FUTURE.TRANSACTION.DETAIL.USED.QUANTITY` | `FsGaFutureTransactionDetail_UsedQuantity` | TField |  | Quantity which is used for closing Multifonds DB Column is QUANTITE_USED. |
| 12 | `FS.GA.FUTURE.TRANSACTION.DETAIL.TRADE.DATE` | `FsGaFutureTransactionDetail_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 13 | `FS.GA.FUTURE.TRANSACTION.DETAIL.ENGAGEMENT.AMOUNT` | `FsGaFutureTransactionDetail_EngagementAmount` | TField |  | This field displays calculated amount as being the quantity * the contract size * the price. Multifonds DB Column is MNT_ENGAG. |
| 14 | `FS.GA.FUTURE.TRANSACTION.DETAIL.NET.MNT` | `FsGaFutureTransactionDetail_NetMnt` | TField |  | Net Mnt Multifonds DB Column is MNT_NET. |
| 15 | `FS.GA.FUTURE.TRANSACTION.DETAIL.INITIAL.MARGIN` | `FsGaFutureTransactionDetail_InitialMargin` | TField |  | MultiFonds is able to compute the initial margin to be deposited with each opening or closing transaction. Enter the initial margin to be deposited per contract. Multifonds DB Column is MARG_INIT. |
| 16 | `FS.GA.FUTURE.TRANSACTION.DETAIL.ARCHIVE` | `FsGaFutureTransactionDetail_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 17 | `FS.GA.FUTURE.TRANSACTION.DETAIL.PROFIT.AND.LOSS.AMOUNT` | `FsGaFutureTransactionDetail_ProfitAndLossAmount` | TField |  | P&amp;L amount can be initialized for securities/futures/options Multifonds DB Column is MNT_GP. |
| 18 | `FS.GA.FUTURE.TRANSACTION.DETAIL.PROFIT.OR.LOSS.AMT.IN.FUND.CCY` | `FsGaFutureTransactionDetail_ProfitOrLossAmtInFundCcy` | TField |  | Will be filled by the system (e.g. in case of corporate actions) Multifonds DB Column is MNT_GP_PTF. |
| 19 | `FS.GA.FUTURE.TRANSACTION.DETAIL.ORIGINAL.BOOK.COST.LOCAL.CCY` | `FsGaFutureTransactionDetail_OriginalBookCostLocalCcy` | TField |  | Original Book Cost Local Ccy Multifonds DB Column is MNT_BOOK_COST. |
| 20 | `FS.GA.FUTURE.TRANSACTION.DETAIL.TRADE.DATE.OF.CONTRACT` | `FsGaFutureTransactionDetail_TradeDateOfContract` | TField |  | Trade Date or Accounting Date for Contractual Instrument Multifonds DB Column is DATACC. |
| 21 | `FS.GA.FUTURE.TRANSACTION.DETAIL.INITIAL.MARGIN.AMOUNT` | `FsGaFutureTransactionDetail_InitialMarginAmount` | TField |  | Initial margin amount of future Multifonds DB Column is MNT_MARG. |
| 22 | `FS.GA.FUTURE.TRANSACTION.DETAIL.MANUAL.LOT.SELECTION` | `FsGaFutureTransactionDetail_ManualLotSelection` | TField |  | Flag to denote that the lots relieved have been manually selected Multifonds DB Column is FLG_MANUAL_LOT. |
| 23 | `FS.GA.FUTURE.TRANSACTION.DETAIL.FUND.MARGIN.AMOUNT` | `FsGaFutureTransactionDetail_FundMarginAmount` | TField |  | Fund Margin Amount Multifonds DB Column is MNT_MARG_PTF. |
| 24 | `FS.GA.FUTURE.TRANSACTION.DETAIL.HEDGING.OR.TRADING.CATEGORY` | `FsGaFutureTransactionDetail_HedgingOrTradingCategory` | TField |  | Hedging or Trading Category Multifonds DB Column is CD_HEDG. |
| 25 | `FS.GA.FUTURE.TRANSACTION.DETAIL.SHARE.CLASS.CODE` | `FsGaFutureTransactionDetail_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 26 | `FS.GA.FUTURE.TRANSACTION.DETAIL.IFRS.TAG` | `FsGaFutureTransactionDetail_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 27 | `FS.GA.FUTURE.TRANSACTION.DETAIL.BROKER.CODE` | `FsGaFutureTransactionDetail_BrokerCode` | TField |  | The code to identify a broker. Multifonds DB Column is BROKER. |
| 28 | `FS.GA.FUTURE.TRANSACTION.DETAIL.EXECUTION.TIMESTAMP` | `FsGaFutureTransactionDetail_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 29 | `FS.GA.FUTURE.TRANSACTION.DETAIL.TRANSACTION.ID` | `FsGaFutureTransactionDetail_TransactionId` | TField |  | Transaction ID Multifonds DB Column is TRAN_ID. |
| 30 | `FS.GA.FUTURE.TRANSACTION.DETAIL.EXTERNAL.REFERENCE` | `FsGaFutureTransactionDetail_ExternalReference` | TField |  | Unique external reference of the transaction used for identifying it for subsequent operations like settlement and reversals. Multifonds DB Column is NUM_REPRISE. |
| 31 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RESERVED10` | `FsGaFutureTransactionDetail_Reserved10` | TField |  |  |
| 32 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RESERVED9` | `FsGaFutureTransactionDetail_Reserved9` | TField |  |  |
| 33 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RESERVED8` | `FsGaFutureTransactionDetail_Reserved8` | TField |  |  |
| 34 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RESERVED7` | `FsGaFutureTransactionDetail_Reserved7` | TField |  |  |
| 35 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RESERVED6` | `FsGaFutureTransactionDetail_Reserved6` | TField |  |  |
| 36 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RESERVED5` | `FsGaFutureTransactionDetail_Reserved5` | TField |  |  |
| 37 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RESERVED4` | `FsGaFutureTransactionDetail_Reserved4` | TField |  |  |
| 38 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RESERVED3` | `FsGaFutureTransactionDetail_Reserved3` | TField |  |  |
| 39 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RESERVED2` | `FsGaFutureTransactionDetail_Reserved2` | TField |  |  |
| 40 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RESERVED1` | `FsGaFutureTransactionDetail_Reserved1` | TField |  |  |
| 41 | `FS.GA.FUTURE.TRANSACTION.DETAIL.LOCAL.REF` | `FsGaFutureTransactionDetail_LocalRef` |  |  |  |
| 42 | `FS.GA.FUTURE.TRANSACTION.DETAIL.OVERRIDE` | `FsGaFutureTransactionDetail_Override` |  |  |  |
| 43 | `FS.GA.FUTURE.TRANSACTION.DETAIL.RECORD.STATUS` | `FsGaFutureTransactionDetail_RecordStatus` | String |  |  |
| 44 | `FS.GA.FUTURE.TRANSACTION.DETAIL.CURR.NO` | `FsGaFutureTransactionDetail_CurrNo` | String |  |  |
| 45 | `FS.GA.FUTURE.TRANSACTION.DETAIL.INPUTTER` | `FsGaFutureTransactionDetail_Inputter` |  |  |  |
| 46 | `FS.GA.FUTURE.TRANSACTION.DETAIL.DATE.TIME` | `FsGaFutureTransactionDetail_DateTime` |  |  |  |
| 47 | `FS.GA.FUTURE.TRANSACTION.DETAIL.AUTHORISER` | `FsGaFutureTransactionDetail_Authoriser` | String |  |  |
| 48 | `FS.GA.FUTURE.TRANSACTION.DETAIL.CO.CODE` | `FsGaFutureTransactionDetail_CoCode` | String |  |  |
| 49 | `FS.GA.FUTURE.TRANSACTION.DETAIL.DEPT.CODE` | `FsGaFutureTransactionDetail_DeptCode` | String |  |  |
| 50 | `FS.GA.FUTURE.TRANSACTION.DETAIL.AUDITOR.CODE` | `FsGaFutureTransactionDetail_AuditorCode` | String |  |  |
| 51 | `FS.GA.FUTURE.TRANSACTION.DETAIL.AUDIT.DATE.TIME` | `FsGaFutureTransactionDetail_AuditDateTime` | String |  |  |
