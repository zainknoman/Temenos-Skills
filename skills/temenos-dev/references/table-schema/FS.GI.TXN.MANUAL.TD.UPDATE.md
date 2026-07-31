# FS.GI.TXN.MANUAL.TD.UPDATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.MANUAL.TD.UPDATE` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.MANUAL.TD.UPDATE.PARENT.REF.ID` | `FsGiTxnManualTdUpdate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.MANUAL.TD.UPDATE.ORA.ROWID` | `FsGiTxnManualTdUpdate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.MANUAL.TD.UPDATE.ORDER.ID` | `FsGiTxnManualTdUpdate_OrderId` | TField |  | Order identification number. Multifonds DB Column is P_NORDER. |
| 4 | `FS.GI.TXN.MANUAL.TD.UPDATE.DEAL.REFERENCE` | `FsGiTxnManualTdUpdate_DealReference` | TField |  | Unique internal reference that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is P_DEAL_REF. |
| 5 | `FS.GI.TXN.MANUAL.TD.UPDATE.AGENT.ID` | `FsGiTxnManualTdUpdate_AgentId` | TField |  | Agentlinked to the order. Multifonds DB Column is P_NOUTLET. |
| 6 | `FS.GI.TXN.MANUAL.TD.UPDATE.SIMULATION.DATE` | `FsGiTxnManualTdUpdate_SimulationDate` | TField |  | Date on which simulation will be processed for the order. Multifonds DB Column is P_FORCED_SEND_TFC_DATE. |
| 7 | `FS.GI.TXN.MANUAL.TD.UPDATE.TRADE.DATE` | `FsGiTxnManualTdUpdate_TradeDate` | TField |  | Trade Date on which NAV is to be applied for the order. Multifonds DB Column is P_FORCED_TRADE_DATE. |
| 8 | `FS.GI.TXN.MANUAL.TD.UPDATE.LATE.TRADING.REASON` | `FsGiTxnManualTdUpdate_LateTradingReason` | TField |  | Reason for Late Trading. Multifonds DB Column is P_LATE_TRADING_REASON. |
| 9 | `FS.GI.TXN.MANUAL.TD.UPDATE.EXCHANGE.GROUP` | `FsGiTxnManualTdUpdate_ExchangeGroup` | TField |  | Fund exchange group. Multifonds DB Column is CGROUPE_COURS. |
| 10 | `FS.GI.TXN.MANUAL.TD.UPDATE.IN.DEAL.REFERENCE` | `FsGiTxnManualTdUpdate_InDealReference` | TField |  | Unique internal reference for two-leg orders that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF_IN. |
| 11 | `FS.GI.TXN.MANUAL.TD.UPDATE.LEGAL.ENTITY.ID` | `FsGiTxnManualTdUpdate_LegalEntityId` | TField |  | Legal Entity linked to the order. Multifonds DB Column is NTFC. |
| 12 | `FS.GI.TXN.MANUAL.TD.UPDATE.TA.FUND.ID` | `FsGiTxnManualTdUpdate_TaFundId` | TField |  | Fund in which the order is placed. Multifonds DB Column is NPTF. |
| 13 | `FS.GI.TXN.MANUAL.TD.UPDATE.SHARE.CLASS.CODE` | `FsGiTxnManualTdUpdate_ShareClassCode` | TField |  | Fund share class in which the order is placed. Multifonds DB Column is TPART. |
| 14 | `FS.GI.TXN.MANUAL.TD.UPDATE.OPERATION.CODE` | `FsGiTxnManualTdUpdate_OperationCode` | TField |  | Type of operation performed such as subscription, redemption, switch, transfer etc. Multifonds DB Column is COPERATION. |
| 15 | `FS.GI.TXN.MANUAL.TD.UPDATE.REGISTER.ID` | `FsGiTxnManualTdUpdate_RegisterId` | TField |  | Register for which the order is placed. Multifonds DB Column is NREGISTER. |
| 16 | `FS.GI.TXN.MANUAL.TD.UPDATE.ORDER.STATUS` | `FsGiTxnManualTdUpdate_OrderStatus` | TField |  | Transaction status indicating whether the order is in initial status, validated, deleted, cancelled etc. Multifonds DB Column is STATUS. |
| 17 | `FS.GI.TXN.MANUAL.TD.UPDATE.REGISTER.TYPE` | `FsGiTxnManualTdUpdate_RegisterType` | TField |  | Register type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_REG. |
| 18 | `FS.GI.TXN.MANUAL.TD.UPDATE.SETTLEMENT.TYPE` | `FsGiTxnManualTdUpdate_SettlementType` | TField |  | Settlement type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_SETTLEMENT. |
| 19 | `FS.GI.TXN.MANUAL.TD.UPDATE.DEAL.TYPE` | `FsGiTxnManualTdUpdate_DealType` | TField |  | Deal type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_DEAL. |
| 20 | `FS.GI.TXN.MANUAL.TD.UPDATE.DEAL.STATUS` | `FsGiTxnManualTdUpdate_DealStatus` | TField |  | Deal status of the order based on cash handling setup. Multifonds DB Column is DEAL_STATUS. |
| 21 | `FS.GI.TXN.MANUAL.TD.UPDATE.RECEPTION.DATE.TIME` | `FsGiTxnManualTdUpdate_ReceptionDateTime` |  |  |  |
| 22 | `FS.GI.TXN.MANUAL.TD.UPDATE.VALUE.DATE` | `FsGiTxnManualTdUpdate_ValueDate` | TField |  | Fund settlement date for the order. Multifonds DB Column is DVALEUR. |
| 23 | `FS.GI.TXN.MANUAL.TD.UPDATE.LEG.LINK` | `FsGiTxnManualTdUpdate_LegLink` | TField |  | System created ID for switch, transfer, Aller Retour and merge order entries. Multifonds DB Column is LEG_LINK. |
| 24 | `FS.GI.TXN.MANUAL.TD.UPDATE.SWITCH.IN.CALC.NAV.DATE` | `FsGiTxnManualTdUpdate_SwitchInCalcNavDate` | TField |  | Price date for switch in calculated by applying the hard and soft conditional trade date rules. Multifonds DB Column is PRICE_DATE_IN. |
| 25 | `FS.GI.TXN.MANUAL.TD.UPDATE.SWITCH.OUT.CALC.NAV.DATE` | `FsGiTxnManualTdUpdate_SwitchOutCalcNavDate` | TField |  | Price date for switch out calculated by applying the hard and soft conditional trade date rules. Multifonds DB Column is PRICE_DATE_OUT. |
| 26 | `FS.GI.TXN.MANUAL.TD.UPDATE.TRADE.DATE.FROM.PARAMETER` | `FsGiTxnManualTdUpdate_TradeDateFromParameter` | TField |  | Trade date from filter. Multifonds DB Column is PRM_DATE_EXE_FROM. |
| 27 | `FS.GI.TXN.MANUAL.TD.UPDATE.TRADE.DATE.TO.PARAMETER` | `FsGiTxnManualTdUpdate_TradeDateToParameter` | TField |  | Trade date to filter. Multifonds DB Column is PRM_DATE_EXE_TO. |
| 28 | `FS.GI.TXN.MANUAL.TD.UPDATE.EXCHANGE.GROUP.PARAMETER` | `FsGiTxnManualTdUpdate_ExchangeGroupParameter` | TField |  | Fund exchange group filter. Multifonds DB Column is PRM_CGROUPE_COURS. |
| 29 | `FS.GI.TXN.MANUAL.TD.UPDATE.TA.FUND.ID.PARAMETER` | `FsGiTxnManualTdUpdate_TaFundIdParameter` | TField |  | Fund ID filter. Multifonds DB Column is PRM_NPTF. |
| 30 | `FS.GI.TXN.MANUAL.TD.UPDATE.AGENT.ID.PARAMETER` | `FsGiTxnManualTdUpdate_AgentIdParameter` | TField |  | Agent ID filter. Multifonds DB Column is PRM_NOUTLET. |
| 31 | `FS.GI.TXN.MANUAL.TD.UPDATE.ENTITY.TYPE.PARAMETER` | `FsGiTxnManualTdUpdate_EntityTypeParameter` | TField |  | Entity type filter. Multifonds DB Column is PRM_ENTITY_TYPE. |
| 32 | `FS.GI.TXN.MANUAL.TD.UPDATE.FUND.ID` | `FsGiTxnManualTdUpdate_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 33 | `FS.GI.TXN.MANUAL.TD.UPDATE.CLASS.CURRENCY` | `FsGiTxnManualTdUpdate_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 34 | `FS.GI.TXN.MANUAL.TD.UPDATE.STATUS.DESCRIPTION` | `FsGiTxnManualTdUpdate_StatusDescription` | TField |  | Status Description. Multifonds DB Column is STATUS_DESC. |
| 35 | `FS.GI.TXN.MANUAL.TD.UPDATE.NO.CASH.FLAG` | `FsGiTxnManualTdUpdate_NoCashFlag` | TField |  | Flag to indicate external cash movement. Multifonds DB Column is FLG_NO_CASH. |
| 36 | `FS.GI.TXN.MANUAL.TD.UPDATE.LATE.TRADE.FLAG` | `FsGiTxnManualTdUpdate_LateTradeFlag` | TField |  | flag to indicate late trading. Multifonds DB Column is FLG_LATE_TRADE. |
| 37 | `FS.GI.TXN.MANUAL.TD.UPDATE.RESERVED10` | `FsGiTxnManualTdUpdate_Reserved10` | TField |  |  |
| 38 | `FS.GI.TXN.MANUAL.TD.UPDATE.RESERVED9` | `FsGiTxnManualTdUpdate_Reserved9` | TField |  |  |
| 39 | `FS.GI.TXN.MANUAL.TD.UPDATE.RESERVED8` | `FsGiTxnManualTdUpdate_Reserved8` | TField |  |  |
| 40 | `FS.GI.TXN.MANUAL.TD.UPDATE.RESERVED7` | `FsGiTxnManualTdUpdate_Reserved7` | TField |  |  |
| 41 | `FS.GI.TXN.MANUAL.TD.UPDATE.RESERVED6` | `FsGiTxnManualTdUpdate_Reserved6` | TField |  |  |
| 42 | `FS.GI.TXN.MANUAL.TD.UPDATE.RESERVED5` | `FsGiTxnManualTdUpdate_Reserved5` | TField |  |  |
| 43 | `FS.GI.TXN.MANUAL.TD.UPDATE.RESERVED4` | `FsGiTxnManualTdUpdate_Reserved4` | TField |  |  |
| 44 | `FS.GI.TXN.MANUAL.TD.UPDATE.RESERVED3` | `FsGiTxnManualTdUpdate_Reserved3` | TField |  |  |
| 45 | `FS.GI.TXN.MANUAL.TD.UPDATE.RESERVED2` | `FsGiTxnManualTdUpdate_Reserved2` | TField |  |  |
| 46 | `FS.GI.TXN.MANUAL.TD.UPDATE.RESERVED1` | `FsGiTxnManualTdUpdate_Reserved1` | TField |  |  |
| 47 | `FS.GI.TXN.MANUAL.TD.UPDATE.LOCAL.REF` | `FsGiTxnManualTdUpdate_LocalRef` |  |  |  |
| 48 | `FS.GI.TXN.MANUAL.TD.UPDATE.OVERRIDE` | `FsGiTxnManualTdUpdate_Override` |  |  |  |
| 49 | `FS.GI.TXN.MANUAL.TD.UPDATE.RECORD.STATUS` | `FsGiTxnManualTdUpdate_RecordStatus` | String |  |  |
| 50 | `FS.GI.TXN.MANUAL.TD.UPDATE.CURR.NO` | `FsGiTxnManualTdUpdate_CurrNo` | String |  |  |
| 51 | `FS.GI.TXN.MANUAL.TD.UPDATE.INPUTTER` | `FsGiTxnManualTdUpdate_Inputter` |  |  |  |
| 52 | `FS.GI.TXN.MANUAL.TD.UPDATE.DATE.TIME` | `FsGiTxnManualTdUpdate_DateTime` |  |  |  |
| 53 | `FS.GI.TXN.MANUAL.TD.UPDATE.AUTHORISER` | `FsGiTxnManualTdUpdate_Authoriser` | String |  |  |
| 54 | `FS.GI.TXN.MANUAL.TD.UPDATE.CO.CODE` | `FsGiTxnManualTdUpdate_CoCode` | String |  |  |
| 55 | `FS.GI.TXN.MANUAL.TD.UPDATE.DEPT.CODE` | `FsGiTxnManualTdUpdate_DeptCode` | String |  |  |
| 56 | `FS.GI.TXN.MANUAL.TD.UPDATE.AUDITOR.CODE` | `FsGiTxnManualTdUpdate_AuditorCode` | String |  |  |
| 57 | `FS.GI.TXN.MANUAL.TD.UPDATE.AUDIT.DATE.TIME` | `FsGiTxnManualTdUpdate_AuditDateTime` | String |  |  |
