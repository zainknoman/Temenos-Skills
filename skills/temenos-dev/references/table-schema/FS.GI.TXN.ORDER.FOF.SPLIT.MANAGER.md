# FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.PARENT.REF.ID` | `FsGiTxnOrderFofSplitManager_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.ORA.ROWID` | `FsGiTxnOrderFofSplitManager_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.AGENT.ID` | `FsGiTxnOrderFofSplitManager_AgentId` | TField |  | Agent ID linked to the order. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.ORDER.ID` | `FsGiTxnOrderFofSplitManager_OrderId` | TField |  | System generated order ID. Multifonds DB Column is NORDER. |
| 5 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.FUND.ID` | `FsGiTxnOrderFofSplitManager_FundId` | TField |  | Fund in which the order is placed. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.MANAGER.ID` | `FsGiTxnOrderFofSplitManager_ManagerId` | TField |  | Central register that will represent the manager of the fund. Multifonds DB Column is NS_PORTFOLIO. |
| 7 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.SPLIT.PCT` | `FsGiTxnOrderFofSplitManager_SplitPct` | TField |  | Split percentage of the order. Multifonds DB Column is SPLIT_PCT. |
| 8 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.SPLIT.AMOUNT` | `FsGiTxnOrderFofSplitManager_SplitAmount` | TField |  | Split amount of the order. Multifonds DB Column is SPLIT_AMOUNT. |
| 9 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.FOF.REGISTER.ID` | `FsGiTxnOrderFofSplitManager_FofRegisterId` | TField |  | Fund Of Fund Register ID who will be placing the transactions for the fund of funds (If the fund type is 0020 - Fund of funds). Multifonds DB Column is FOF_NREGISTER. |
| 10 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.FOF.FUND.ID` | `FsGiTxnOrderFofSplitManager_FofFundId` | TField |  | Fund ID of the underlying TA Fund that will be part of the fund of fund functionality. Multifonds DB Column is NPTF_FOF. |
| 11 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.OPERATION.CODE` | `FsGiTxnOrderFofSplitManager_OperationCode` | TField |  | Type of operation performed such as subscription, redemption, switch, transfer etc. Multifonds DB Column is COPERATION. |
| 12 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.DEAL.REFERENCE` | `FsGiTxnOrderFofSplitManager_DealReference` | TField |  | Unique internal reference that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF. |
| 13 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.IN.DEAL.REFERENCE` | `FsGiTxnOrderFofSplitManager_InDealReference` | TField |  | Unique internal reference for two-leg orders that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF_IN. |
| 14 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.LEG.LINK` | `FsGiTxnOrderFofSplitManager_LegLink` | TField |  | System created ID for switch, transfer, Aller Retour and merge order entries. Multifonds DB Column is LEG_LINK. |
| 15 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RESERVED10` | `FsGiTxnOrderFofSplitManager_Reserved10` | TField |  |  |
| 16 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RESERVED9` | `FsGiTxnOrderFofSplitManager_Reserved9` | TField |  |  |
| 17 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RESERVED8` | `FsGiTxnOrderFofSplitManager_Reserved8` | TField |  |  |
| 18 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RESERVED7` | `FsGiTxnOrderFofSplitManager_Reserved7` | TField |  |  |
| 19 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RESERVED6` | `FsGiTxnOrderFofSplitManager_Reserved6` | TField |  |  |
| 20 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RESERVED5` | `FsGiTxnOrderFofSplitManager_Reserved5` | TField |  |  |
| 21 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RESERVED4` | `FsGiTxnOrderFofSplitManager_Reserved4` | TField |  |  |
| 22 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RESERVED3` | `FsGiTxnOrderFofSplitManager_Reserved3` | TField |  |  |
| 23 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RESERVED2` | `FsGiTxnOrderFofSplitManager_Reserved2` | TField |  |  |
| 24 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RESERVED1` | `FsGiTxnOrderFofSplitManager_Reserved1` | TField |  |  |
| 25 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.LOCAL.REF` | `FsGiTxnOrderFofSplitManager_LocalRef` |  |  |  |
| 26 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.OVERRIDE` | `FsGiTxnOrderFofSplitManager_Override` |  |  |  |
| 27 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.RECORD.STATUS` | `FsGiTxnOrderFofSplitManager_RecordStatus` | String |  |  |
| 28 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.CURR.NO` | `FsGiTxnOrderFofSplitManager_CurrNo` | String |  |  |
| 29 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.INPUTTER` | `FsGiTxnOrderFofSplitManager_Inputter` |  |  |  |
| 30 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.DATE.TIME` | `FsGiTxnOrderFofSplitManager_DateTime` |  |  |  |
| 31 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.AUTHORISER` | `FsGiTxnOrderFofSplitManager_Authoriser` | String |  |  |
| 32 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.CO.CODE` | `FsGiTxnOrderFofSplitManager_CoCode` | String |  |  |
| 33 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.DEPT.CODE` | `FsGiTxnOrderFofSplitManager_DeptCode` | String |  |  |
| 34 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.AUDITOR.CODE` | `FsGiTxnOrderFofSplitManager_AuditorCode` | String |  |  |
| 35 | `FS.GI.TXN.ORDER.FOF.SPLIT.MANAGER.AUDIT.DATE.TIME` | `FsGiTxnOrderFofSplitManager_AuditDateTime` | String |  |  |
