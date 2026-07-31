# FS.GI.TXN.ORDER.LOT.SELECTION — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.ORDER.LOT.SELECTION` in `FS_TransactionEntry.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.ORDER.LOT.SELECTION.PARENT.REF.ID` | `FsGiTxnOrderLotSelection_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.ORDER.LOT.SELECTION.ORA.ROWID` | `FsGiTxnOrderLotSelection_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.ORDER.LOT.SELECTION.TA.FUND.ID` | `FsGiTxnOrderLotSelection_TaFundId` | TField |  | Fund ID in which order is created. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.TXN.ORDER.LOT.SELECTION.REGISTER.ID` | `FsGiTxnOrderLotSelection_RegisterId` | TField |  | Register internal ID. Multifonds DB Column is NREGISTER. |
| 5 | `FS.GI.TXN.ORDER.LOT.SELECTION.SHARE.CLASS.CODE` | `FsGiTxnOrderLotSelection_ShareClassCode` | TField |  | Fund share class in which order is created. Multifonds DB Column is TPART. |
| 6 | `FS.GI.TXN.ORDER.LOT.SELECTION.ORDER.ID` | `FsGiTxnOrderLotSelection_OrderId` | TField |  | Order identification number. Multifonds DB Column is NORDER. |
| 7 | `FS.GI.TXN.ORDER.LOT.SELECTION.AGENT.ID` | `FsGiTxnOrderLotSelection_AgentId` | TField |  | Agent Internal ID. Multifonds DB Column is NOUTLET. |
| 8 | `FS.GI.TXN.ORDER.LOT.SELECTION.CONTRACT.LINKED` | `FsGiTxnOrderLotSelection_ContractLinked` | TField |  | Linked Contract ID of the lot selection contract Multifonds DB Column is CONTRACT_LINKED. |
| 9 | `FS.GI.TXN.ORDER.LOT.SELECTION.TRADE.DATE` | `FsGiTxnOrderLotSelection_TradeDate` | TField |  | Trade Date of the Lot Selection Contract Multifonds DB Column is DOPER. |
| 10 | `FS.GI.TXN.ORDER.LOT.SELECTION.QUANTITY.AVAILABLE` | `FsGiTxnOrderLotSelection_QuantityAvailable` | TField |  | Total quantity available in the Lot selection contract. Multifonds DB Column is QTY_AVAILABLE. |
| 11 | `FS.GI.TXN.ORDER.LOT.SELECTION.QUANTITY.USED` | `FsGiTxnOrderLotSelection_QuantityUsed` | TField |  | Number of units used for the LOT. Multifonds DB Column is QTY_USED. |
| 12 | `FS.GI.TXN.ORDER.LOT.SELECTION.TRANSFER.HISTORY` | `FsGiTxnOrderLotSelection_TransferHistory` | TField |  | Transfer History details. Multifonds DB Column is TRANSFER_HISTO. |
| 13 | `FS.GI.TXN.ORDER.LOT.SELECTION.QUANTITY.LEFT` | `FsGiTxnOrderLotSelection_QuantityLeft` | TField |  | Order quantity remaining for lot selection. Multifonds DB Column is QTY_LEFT. |
| 14 | `FS.GI.TXN.ORDER.LOT.SELECTION.DEAL.REFERENCE` | `FsGiTxnOrderLotSelection_DealReference` | TField |  | Deal reference number. Multifonds DB Column is DEAL_REF. |
| 15 | `FS.GI.TXN.ORDER.LOT.SELECTION.IN.DEAL.REFERENCE` | `FsGiTxnOrderLotSelection_InDealReference` | TField |  | Unique internal reference for two-leg orders that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF_IN. |
| 16 | `FS.GI.TXN.ORDER.LOT.SELECTION.LEG.LINK` | `FsGiTxnOrderLotSelection_LegLink` | TField |  | Leg link for switch / transfer orders; automatically populated. Multifonds DB Column is LEG_LINK. |
| 17 | `FS.GI.TXN.ORDER.LOT.SELECTION.LOT.SELECTION.TOTAL` | `FsGiTxnOrderLotSelection_LotSelectionTotal` | TField |  | Sum of the individual open lot selected quantity for the debit transaction. Multifonds DB Column is TOT_QTY_USED. |
| 18 | `FS.GI.TXN.ORDER.LOT.SELECTION.ORDER.QUANTITY` | `FsGiTxnOrderLotSelection_OrderQuantity` | TField |  | Quantity of the transaction. Multifonds DB Column is ORD_QTY. |
| 19 | `FS.GI.TXN.ORDER.LOT.SELECTION.ORDER.QUANTITY.LEFT` | `FsGiTxnOrderLotSelection_OrderQuantityLeft` | TField |  | Remaining quantity of the transaction after applying the Lots seletion quantity. Multifonds DB Column is DIFF_QTY. |
| 20 | `FS.GI.TXN.ORDER.LOT.SELECTION.FUND.ID` | `FsGiTxnOrderLotSelection_FundId` | TField |  | Fund is in scope for the document type. Multifonds DB Column is MULTIFONDS_ID. |
| 21 | `FS.GI.TXN.ORDER.LOT.SELECTION.CLASS.CURRENCY` | `FsGiTxnOrderLotSelection_ClassCurrency` | TField |  | Fund share class currency. Multifonds DB Column is CLASS_CURRENCY. |
| 22 | `FS.GI.TXN.ORDER.LOT.SELECTION.REDEMPTION.TRANCHE.FLAG` | `FsGiTxnOrderLotSelection_RedemptionTrancheFlag` | TField |  | Redemption contract flag. Multifonds DB Column is RED_TRANCHE. |
| 23 | `FS.GI.TXN.ORDER.LOT.SELECTION.LOCKUP` | `FsGiTxnOrderLotSelection_Lockup` | TField |  | Identifier to display if the contract/tranche is within the lock-up or not. Multifonds DB Column is LOCKUP_OPT. |
| 24 | `FS.GI.TXN.ORDER.LOT.SELECTION.TRANCHE.PERCENTAGE` | `FsGiTxnOrderLotSelection_TranchePercentage` | TField |  | Tranche percentage. Multifonds DB Column is TRANCHE_PCT. |
| 25 | `FS.GI.TXN.ORDER.LOT.SELECTION.CAPITAL.BALANCE` | `FsGiTxnOrderLotSelection_CapitalBalance` | TField |  | Latest capital balance of the tranche based on the opening or closing deal. Multifonds DB Column is CAP_BAL. |
| 26 | `FS.GI.TXN.ORDER.LOT.SELECTION.RED.TRANCHE.AMOUNT` | `FsGiTxnOrderLotSelection_RedTrancheAmount` | TField |  | Amount to be redeemed from the tranche based on the tranche% for proportioniate withdrawal method. Multifonds DB Column is RED_TRANCH_AMOUNT. |
| 27 | `FS.GI.TXN.ORDER.LOT.SELECTION.LOT.SELECTION.FLAG` | `FsGiTxnOrderLotSelection_LotSelectionFlag` | TField |  | Flag to select the lots manually which would signify the percentage of the capital to be redeemed from each of the selected tranche. Multifonds DB Column is FLG_LOT_SEL. |
| 28 | `FS.GI.TXN.ORDER.LOT.SELECTION.ORIGINAL.DEAL.REFERENCE` | `FsGiTxnOrderLotSelection_OriginalDealReference` | TField |  | Original deal reference number. Multifonds DB Column is ORIGINAL_DEAL_REF. |
| 29 | `FS.GI.TXN.ORDER.LOT.SELECTION.END.OF.RECORD.FLAG` | `FsGiTxnOrderLotSelection_EndOfRecordFlag` | TField |  | End of record flag. Multifonds DB Column is FLG_EOR. |
| 30 | `FS.GI.TXN.ORDER.LOT.SELECTION.BY.PASS.FLAG` | `FsGiTxnOrderLotSelection_ByPassFlag` | TField |  | By pass flag. Multifonds DB Column is FLG_BY_PASS. |
| 31 | `FS.GI.TXN.ORDER.LOT.SELECTION.ORDER.AMOUNT` | `FsGiTxnOrderLotSelection_OrderAmount` | TField |  | Order Amount Multifonds DB Column is ORDER_AMOUNT. |
| 32 | `FS.GI.TXN.ORDER.LOT.SELECTION.ORDER.AMOUNT.REMAINING` | `FsGiTxnOrderLotSelection_OrderAmountRemaining` | TField |  | Order Amount Remaining Multifonds DB Column is ORDER_AMT_REMAINING. |
| 33 | `FS.GI.TXN.ORDER.LOT.SELECTION.RESERVED10` | `FsGiTxnOrderLotSelection_Reserved10` | TField |  |  |
| 34 | `FS.GI.TXN.ORDER.LOT.SELECTION.RESERVED9` | `FsGiTxnOrderLotSelection_Reserved9` | TField |  |  |
| 35 | `FS.GI.TXN.ORDER.LOT.SELECTION.RESERVED8` | `FsGiTxnOrderLotSelection_Reserved8` | TField |  |  |
| 36 | `FS.GI.TXN.ORDER.LOT.SELECTION.RESERVED7` | `FsGiTxnOrderLotSelection_Reserved7` | TField |  |  |
| 37 | `FS.GI.TXN.ORDER.LOT.SELECTION.RESERVED6` | `FsGiTxnOrderLotSelection_Reserved6` | TField |  |  |
| 38 | `FS.GI.TXN.ORDER.LOT.SELECTION.RESERVED5` | `FsGiTxnOrderLotSelection_Reserved5` | TField |  |  |
| 39 | `FS.GI.TXN.ORDER.LOT.SELECTION.RESERVED4` | `FsGiTxnOrderLotSelection_Reserved4` | TField |  |  |
| 40 | `FS.GI.TXN.ORDER.LOT.SELECTION.RESERVED3` | `FsGiTxnOrderLotSelection_Reserved3` | TField |  |  |
| 41 | `FS.GI.TXN.ORDER.LOT.SELECTION.RESERVED2` | `FsGiTxnOrderLotSelection_Reserved2` | TField |  |  |
| 42 | `FS.GI.TXN.ORDER.LOT.SELECTION.RESERVED1` | `FsGiTxnOrderLotSelection_Reserved1` | TField |  |  |
| 43 | `FS.GI.TXN.ORDER.LOT.SELECTION.LOCAL.REF` | `FsGiTxnOrderLotSelection_LocalRef` |  |  |  |
| 44 | `FS.GI.TXN.ORDER.LOT.SELECTION.OVERRIDE` | `FsGiTxnOrderLotSelection_Override` |  |  |  |
| 45 | `FS.GI.TXN.ORDER.LOT.SELECTION.RECORD.STATUS` | `FsGiTxnOrderLotSelection_RecordStatus` | String |  |  |
| 46 | `FS.GI.TXN.ORDER.LOT.SELECTION.CURR.NO` | `FsGiTxnOrderLotSelection_CurrNo` | String |  |  |
| 47 | `FS.GI.TXN.ORDER.LOT.SELECTION.INPUTTER` | `FsGiTxnOrderLotSelection_Inputter` |  |  |  |
| 48 | `FS.GI.TXN.ORDER.LOT.SELECTION.DATE.TIME` | `FsGiTxnOrderLotSelection_DateTime` |  |  |  |
| 49 | `FS.GI.TXN.ORDER.LOT.SELECTION.AUTHORISER` | `FsGiTxnOrderLotSelection_Authoriser` | String |  |  |
| 50 | `FS.GI.TXN.ORDER.LOT.SELECTION.CO.CODE` | `FsGiTxnOrderLotSelection_CoCode` | String |  |  |
| 51 | `FS.GI.TXN.ORDER.LOT.SELECTION.DEPT.CODE` | `FsGiTxnOrderLotSelection_DeptCode` | String |  |  |
| 52 | `FS.GI.TXN.ORDER.LOT.SELECTION.AUDITOR.CODE` | `FsGiTxnOrderLotSelection_AuditorCode` | String |  |  |
| 53 | `FS.GI.TXN.ORDER.LOT.SELECTION.AUDIT.DATE.TIME` | `FsGiTxnOrderLotSelection_AuditDateTime` | String |  |  |
