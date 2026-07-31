# FS.GA.OPTION.TRANSACTION.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPTION.TRANSACTION.DETAIL` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPTION.TRANSACTION.DETAIL.PARENT.REF.ID` | `FsGaOptionTransactionDetail_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.OPTION.TRANSACTION.DETAIL.ORA.ROWID` | `FsGaOptionTransactionDetail_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.OPTION.TRANSACTION.DETAIL.FUND.ID` | `FsGaOptionTransactionDetail_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.OPTION.TRANSACTION.DETAIL.TRANSACTION.NUMBER` | `FsGaOptionTransactionDetail_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.OPTION.TRANSACTION.DETAIL.NEXT` | `FsGaOptionTransactionDetail_Next` | TField |  | Next Multifonds DB Column is NEXT. |
| 6 | `FS.GA.OPTION.TRANSACTION.DETAIL.OPTION.ID` | `FsGaOptionTransactionDetail_OptionId` | TField |  | Option Security ID Multifonds DB Column is NOPT. |
| 7 | `FS.GA.OPTION.TRANSACTION.DETAIL.MANAGER.CODE` | `FsGaOptionTransactionDetail_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 8 | `FS.GA.OPTION.TRANSACTION.DETAIL.LOT.NUMBER` | `FsGaOptionTransactionDetail_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 9 | `FS.GA.OPTION.TRANSACTION.DETAIL.QUANTITY` | `FsGaOptionTransactionDetail_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 10 | `FS.GA.OPTION.TRANSACTION.DETAIL.TRADE.DATE` | `FsGaOptionTransactionDetail_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 11 | `FS.GA.OPTION.TRANSACTION.DETAIL.PREMIUM.AMOUNT` | `FsGaOptionTransactionDetail_PremiumAmount` | TField |  | Premium Amount paid/received for Options &amp; Futures transactions Multifonds DB Column is PREMIUM. |
| 12 | `FS.GA.OPTION.TRANSACTION.DETAIL.USED.QUANTITY` | `FsGaOptionTransactionDetail_UsedQuantity` | TField |  | Quantity which is used for closing Multifonds DB Column is QUANTITE_USED. |
| 13 | `FS.GA.OPTION.TRANSACTION.DETAIL.GROSS.AMOUNT.OF.TRANSACTION` | `FsGaOptionTransactionDetail_GrossAmountOfTransaction` | TField |  | Gross Amount of Transaction Multifonds DB Column is MNT_GROSS. |
| 14 | `FS.GA.OPTION.TRANSACTION.DETAIL.FEES.AMOUNT` | `FsGaOptionTransactionDetail_FeesAmount` | TField |  | Transaction Fees Amount Multifonds DB Column is MNT_FEES. |
| 15 | `FS.GA.OPTION.TRANSACTION.DETAIL.NET.MNT` | `FsGaOptionTransactionDetail_NetMnt` | TField |  | Net Mnt Multifonds DB Column is MNT_NET. |
| 16 | `FS.GA.OPTION.TRANSACTION.DETAIL.NET.AMOUNT.IN.SETTLEMENT.CCY` | `FsGaOptionTransactionDetail_NetAmountInSettlementCcy` | TField |  | Net amount of settlement as part of the transaction Multifonds DB Column is MNT_NET_CORR. |
| 17 | `FS.GA.OPTION.TRANSACTION.DETAIL.ARCHIVE` | `FsGaOptionTransactionDetail_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 18 | `FS.GA.OPTION.TRANSACTION.DETAIL.MANUAL.LOT.SELECTION` | `FsGaOptionTransactionDetail_ManualLotSelection` | TField |  | Flag to denote that the lots relieved have been manually selected Multifonds DB Column is FLG_MANUAL_LOT. |
| 19 | `FS.GA.OPTION.TRANSACTION.DETAIL.HEDGING.OR.TRADING.CATEGORY` | `FsGaOptionTransactionDetail_HedgingOrTradingCategory` | TField |  | Hedging or Trading Category Multifonds DB Column is CD_HEDG. |
| 20 | `FS.GA.OPTION.TRANSACTION.DETAIL.SHARE.CLASS.CODE` | `FsGaOptionTransactionDetail_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 21 | `FS.GA.OPTION.TRANSACTION.DETAIL.IFRS.TAG` | `FsGaOptionTransactionDetail_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 22 | `FS.GA.OPTION.TRANSACTION.DETAIL.BROKER.CODE` | `FsGaOptionTransactionDetail_BrokerCode` | TField |  | The code to identify a broker. Multifonds DB Column is BROKER. |
| 23 | `FS.GA.OPTION.TRANSACTION.DETAIL.PROFIT.AND.LOSS.AMOUNT` | `FsGaOptionTransactionDetail_ProfitAndLossAmount` | TField |  | P&amp;L amount can be initialized for securities/futures/options Multifonds DB Column is MNT_GP. |
| 24 | `FS.GA.OPTION.TRANSACTION.DETAIL.PROFIT.OR.LOSS.AMT.IN.FUND.CCY` | `FsGaOptionTransactionDetail_ProfitOrLossAmtInFundCcy` | TField |  | Will be filled by the system (e.g. in case of corporate actions) Multifonds DB Column is MNT_GP_PTF. |
| 25 | `FS.GA.OPTION.TRANSACTION.DETAIL.EXECUTION.TIMESTAMP` | `FsGaOptionTransactionDetail_ExecutionTimestamp` | TField |  | Time stamp of the trade execution in the market. Multifonds DB Column is EXEC_TIMESTAMP. |
| 26 | `FS.GA.OPTION.TRANSACTION.DETAIL.TRANSACTION.ID` | `FsGaOptionTransactionDetail_TransactionId` | TField |  | Transaction ID Multifonds DB Column is TRAN_ID. |
| 27 | `FS.GA.OPTION.TRANSACTION.DETAIL.TRADE.DATE.OPER` | `FsGaOptionTransactionDetail_TradeDateOper` | TField |  | Trade Date OPER Multifonds DB Column is TRADE_DOPER. |
| 28 | `FS.GA.OPTION.TRANSACTION.DETAIL.TRADE.DATE.ACCOUNTING` | `FsGaOptionTransactionDetail_TradeDateAccounting` | TField |  | Trade Date Accounting Multifonds DB Column is TRADE_DJOURNAL. |
| 29 | `FS.GA.OPTION.TRANSACTION.DETAIL.RESERVED10` | `FsGaOptionTransactionDetail_Reserved10` | TField |  |  |
| 30 | `FS.GA.OPTION.TRANSACTION.DETAIL.RESERVED9` | `FsGaOptionTransactionDetail_Reserved9` | TField |  |  |
| 31 | `FS.GA.OPTION.TRANSACTION.DETAIL.RESERVED8` | `FsGaOptionTransactionDetail_Reserved8` | TField |  |  |
| 32 | `FS.GA.OPTION.TRANSACTION.DETAIL.RESERVED7` | `FsGaOptionTransactionDetail_Reserved7` | TField |  |  |
| 33 | `FS.GA.OPTION.TRANSACTION.DETAIL.RESERVED6` | `FsGaOptionTransactionDetail_Reserved6` | TField |  |  |
| 34 | `FS.GA.OPTION.TRANSACTION.DETAIL.RESERVED5` | `FsGaOptionTransactionDetail_Reserved5` | TField |  |  |
| 35 | `FS.GA.OPTION.TRANSACTION.DETAIL.RESERVED4` | `FsGaOptionTransactionDetail_Reserved4` | TField |  |  |
| 36 | `FS.GA.OPTION.TRANSACTION.DETAIL.RESERVED3` | `FsGaOptionTransactionDetail_Reserved3` | TField |  |  |
| 37 | `FS.GA.OPTION.TRANSACTION.DETAIL.RESERVED2` | `FsGaOptionTransactionDetail_Reserved2` | TField |  |  |
| 38 | `FS.GA.OPTION.TRANSACTION.DETAIL.RESERVED1` | `FsGaOptionTransactionDetail_Reserved1` | TField |  |  |
| 39 | `FS.GA.OPTION.TRANSACTION.DETAIL.LOCAL.REF` | `FsGaOptionTransactionDetail_LocalRef` |  |  |  |
| 40 | `FS.GA.OPTION.TRANSACTION.DETAIL.OVERRIDE` | `FsGaOptionTransactionDetail_Override` |  |  |  |
| 41 | `FS.GA.OPTION.TRANSACTION.DETAIL.RECORD.STATUS` | `FsGaOptionTransactionDetail_RecordStatus` | String |  |  |
| 42 | `FS.GA.OPTION.TRANSACTION.DETAIL.CURR.NO` | `FsGaOptionTransactionDetail_CurrNo` | String |  |  |
| 43 | `FS.GA.OPTION.TRANSACTION.DETAIL.INPUTTER` | `FsGaOptionTransactionDetail_Inputter` |  |  |  |
| 44 | `FS.GA.OPTION.TRANSACTION.DETAIL.DATE.TIME` | `FsGaOptionTransactionDetail_DateTime` |  |  |  |
| 45 | `FS.GA.OPTION.TRANSACTION.DETAIL.AUTHORISER` | `FsGaOptionTransactionDetail_Authoriser` | String |  |  |
| 46 | `FS.GA.OPTION.TRANSACTION.DETAIL.CO.CODE` | `FsGaOptionTransactionDetail_CoCode` | String |  |  |
| 47 | `FS.GA.OPTION.TRANSACTION.DETAIL.DEPT.CODE` | `FsGaOptionTransactionDetail_DeptCode` | String |  |  |
| 48 | `FS.GA.OPTION.TRANSACTION.DETAIL.AUDITOR.CODE` | `FsGaOptionTransactionDetail_AuditorCode` | String |  |  |
| 49 | `FS.GA.OPTION.TRANSACTION.DETAIL.AUDIT.DATE.TIME` | `FsGaOptionTransactionDetail_AuditDateTime` | String |  |  |
