# FS.GI.TXN.MANUAL.VD.UPDATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.MANUAL.VD.UPDATE` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.MANUAL.VD.UPDATE.PARENT.REF.ID` | `FsGiTxnManualVdUpdate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.MANUAL.VD.UPDATE.ORA.ROWID` | `FsGiTxnManualVdUpdate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.MANUAL.VD.UPDATE.ORDER.ID` | `FsGiTxnManualVdUpdate_OrderId` | TField |  | Order identification number. Multifonds DB Column is P_NORDER. |
| 4 | `FS.GI.TXN.MANUAL.VD.UPDATE.DEAL.REFERENCE` | `FsGiTxnManualVdUpdate_DealReference` | TField |  | Unique internal reference that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is P_DEAL_REF. |
| 5 | `FS.GI.TXN.MANUAL.VD.UPDATE.AGENT.ID` | `FsGiTxnManualVdUpdate_AgentId` | TField |  | Agentlinked to the order. Multifonds DB Column is P_NOUTLET. |
| 6 | `FS.GI.TXN.MANUAL.VD.UPDATE.VALUE.DATE` | `FsGiTxnManualVdUpdate_ValueDate` | TField |  | Fund settlement date for the order. Multifonds DB Column is P_VALUE_DATE_FORCED. |
| 7 | `FS.GI.TXN.MANUAL.VD.UPDATE.LATE.TRADING.REASON` | `FsGiTxnManualVdUpdate_LateTradingReason` | TField |  | Value date forced reason. Multifonds DB Column is P_LATE_TRADING_REASON. |
| 8 | `FS.GI.TXN.MANUAL.VD.UPDATE.EXCHANGE.GROUP` | `FsGiTxnManualVdUpdate_ExchangeGroup` | TField |  | Fund exchange group. Multifonds DB Column is CGROUPE_COURS. |
| 9 | `FS.GI.TXN.MANUAL.VD.UPDATE.IN.DEAL.REFERENCE` | `FsGiTxnManualVdUpdate_InDealReference` | TField |  | Unique internal reference for two-leg orders that will allow tracking of the order throughout the transactiona s lifecycle. Multifonds DB Column is DEAL_REF_IN. |
| 10 | `FS.GI.TXN.MANUAL.VD.UPDATE.LEGAL.ENTITY.ID` | `FsGiTxnManualVdUpdate_LegalEntityId` | TField |  | Legal Entity linked to the order. Multifonds DB Column is NTFC. |
| 11 | `FS.GI.TXN.MANUAL.VD.UPDATE.TA.FUND.ID` | `FsGiTxnManualVdUpdate_TaFundId` | TField |  | Fund in which the order is placed. Multifonds DB Column is NPTF. |
| 12 | `FS.GI.TXN.MANUAL.VD.UPDATE.SHARE.CLASS.CODE` | `FsGiTxnManualVdUpdate_ShareClassCode` | TField |  | Fund share class in which the order is placed. Multifonds DB Column is TPART. |
| 13 | `FS.GI.TXN.MANUAL.VD.UPDATE.OPERATION.CODE` | `FsGiTxnManualVdUpdate_OperationCode` | TField |  | Type of operation performed such as subscription, redemption, switch, transfer etc. Multifonds DB Column is COPERATION. |
| 14 | `FS.GI.TXN.MANUAL.VD.UPDATE.REGISTER.ID` | `FsGiTxnManualVdUpdate_RegisterId` | TField |  | Register for which the order is placed. Multifonds DB Column is NREGISTER. |
| 15 | `FS.GI.TXN.MANUAL.VD.UPDATE.ORDER.STATUS` | `FsGiTxnManualVdUpdate_OrderStatus` | TField |  | Transaction status indicating whether the order is in initial status, validated, deleted, cancelled etc. Multifonds DB Column is STATUS. |
| 16 | `FS.GI.TXN.MANUAL.VD.UPDATE.REGISTER.TYPE` | `FsGiTxnManualVdUpdate_RegisterType` | TField |  | Register type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_REG. |
| 17 | `FS.GI.TXN.MANUAL.VD.UPDATE.SETTLEMENT.TYPE` | `FsGiTxnManualVdUpdate_SettlementType` | TField |  | Settlement type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_SETTLEMENT. |
| 18 | `FS.GI.TXN.MANUAL.VD.UPDATE.DEAL.TYPE` | `FsGiTxnManualVdUpdate_DealType` | TField |  | Deal type automatically populated based on the setup at register or agent level. Multifonds DB Column is TYPE_DEAL. |
| 19 | `FS.GI.TXN.MANUAL.VD.UPDATE.DEAL.STATUS` | `FsGiTxnManualVdUpdate_DealStatus` | TField |  | Deal status of the order based on cash handling setup. Multifonds DB Column is DEAL_STATUS. |
| 20 | `FS.GI.TXN.MANUAL.VD.UPDATE.TRADE.DATE` | `FsGiTxnManualVdUpdate_TradeDate` | TField |  | Trade Date on which NAV is to be applied for the order. Multifonds DB Column is DATE_EXE. |
| 21 | `FS.GI.TXN.MANUAL.VD.UPDATE.LEG.LINK` | `FsGiTxnManualVdUpdate_LegLink` | TField |  | System created ID for switch, transfer, Aller Retour and merge order entries. Multifonds DB Column is LEG_LINK. |
| 22 | `FS.GI.TXN.MANUAL.VD.UPDATE.SWITCH.IN.CALC.NAV.DATE` | `FsGiTxnManualVdUpdate_SwitchInCalcNavDate` | TField |  | Price date for switch in calculated by applying the hard and soft conditional trade date rules. Multifonds DB Column is PRICE_DATE_IN. |
| 23 | `FS.GI.TXN.MANUAL.VD.UPDATE.SWITCH.OUT.CALC.NAV.DATE` | `FsGiTxnManualVdUpdate_SwitchOutCalcNavDate` | TField |  | Price date for switch out calculated by applying the hard and soft conditional trade date rules. Multifonds DB Column is PRICE_DATE_OUT. |
| 24 | `FS.GI.TXN.MANUAL.VD.UPDATE.TRADE.DATE.FROM.PARAMETER` | `FsGiTxnManualVdUpdate_TradeDateFromParameter` | TField |  | Trade date from filter. Multifonds DB Column is PRM_DATE_EXE_FROM. |
| 25 | `FS.GI.TXN.MANUAL.VD.UPDATE.TRADE.DATE.TO.PARAMETER` | `FsGiTxnManualVdUpdate_TradeDateToParameter` | TField |  | Trade date to filter. Multifonds DB Column is PRM_DATE_EXE_TO. |
| 26 | `FS.GI.TXN.MANUAL.VD.UPDATE.EXCHANGE.GROUP.PARAMETER` | `FsGiTxnManualVdUpdate_ExchangeGroupParameter` | TField |  | Fund exchange group filter. Multifonds DB Column is PRM_CGROUPE_COURS. |
| 27 | `FS.GI.TXN.MANUAL.VD.UPDATE.TA.FUND.ID.PARAMETER` | `FsGiTxnManualVdUpdate_TaFundIdParameter` | TField |  | Fund ID filter. Multifonds DB Column is PRM_NPTF. |
| 28 | `FS.GI.TXN.MANUAL.VD.UPDATE.LEGAL.ENTITY.ID.PARAMETER` | `FsGiTxnManualVdUpdate_LegalEntityIdParameter` | TField |  | Legal Entity ID filter. Multifonds DB Column is PRM_NTFC. |
| 29 | `FS.GI.TXN.MANUAL.VD.UPDATE.ENTITY.TYPE.PARAMETER` | `FsGiTxnManualVdUpdate_EntityTypeParameter` | TField |  | Entity type filter. Multifonds DB Column is PRM_ENTITY_TYPE. |
| 30 | `FS.GI.TXN.MANUAL.VD.UPDATE.FUND.ID` | `FsGiTxnManualVdUpdate_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 31 | `FS.GI.TXN.MANUAL.VD.UPDATE.CLASS.CURRENCY` | `FsGiTxnManualVdUpdate_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 32 | `FS.GI.TXN.MANUAL.VD.UPDATE.STATUS.DESCRIPTION` | `FsGiTxnManualVdUpdate_StatusDescription` | TField |  | Status description. Multifonds DB Column is STATUS_DESC. |
| 33 | `FS.GI.TXN.MANUAL.VD.UPDATE.RESERVED10` | `FsGiTxnManualVdUpdate_Reserved10` | TField |  |  |
| 34 | `FS.GI.TXN.MANUAL.VD.UPDATE.RESERVED9` | `FsGiTxnManualVdUpdate_Reserved9` | TField |  |  |
| 35 | `FS.GI.TXN.MANUAL.VD.UPDATE.RESERVED8` | `FsGiTxnManualVdUpdate_Reserved8` | TField |  |  |
| 36 | `FS.GI.TXN.MANUAL.VD.UPDATE.RESERVED7` | `FsGiTxnManualVdUpdate_Reserved7` | TField |  |  |
| 37 | `FS.GI.TXN.MANUAL.VD.UPDATE.RESERVED6` | `FsGiTxnManualVdUpdate_Reserved6` | TField |  |  |
| 38 | `FS.GI.TXN.MANUAL.VD.UPDATE.RESERVED5` | `FsGiTxnManualVdUpdate_Reserved5` | TField |  |  |
| 39 | `FS.GI.TXN.MANUAL.VD.UPDATE.RESERVED4` | `FsGiTxnManualVdUpdate_Reserved4` | TField |  |  |
| 40 | `FS.GI.TXN.MANUAL.VD.UPDATE.RESERVED3` | `FsGiTxnManualVdUpdate_Reserved3` | TField |  |  |
| 41 | `FS.GI.TXN.MANUAL.VD.UPDATE.RESERVED2` | `FsGiTxnManualVdUpdate_Reserved2` | TField |  |  |
| 42 | `FS.GI.TXN.MANUAL.VD.UPDATE.RESERVED1` | `FsGiTxnManualVdUpdate_Reserved1` | TField |  |  |
| 43 | `FS.GI.TXN.MANUAL.VD.UPDATE.LOCAL.REF` | `FsGiTxnManualVdUpdate_LocalRef` |  |  |  |
| 44 | `FS.GI.TXN.MANUAL.VD.UPDATE.OVERRIDE` | `FsGiTxnManualVdUpdate_Override` |  |  |  |
| 45 | `FS.GI.TXN.MANUAL.VD.UPDATE.RECORD.STATUS` | `FsGiTxnManualVdUpdate_RecordStatus` | String |  |  |
| 46 | `FS.GI.TXN.MANUAL.VD.UPDATE.CURR.NO` | `FsGiTxnManualVdUpdate_CurrNo` | String |  |  |
| 47 | `FS.GI.TXN.MANUAL.VD.UPDATE.INPUTTER` | `FsGiTxnManualVdUpdate_Inputter` |  |  |  |
| 48 | `FS.GI.TXN.MANUAL.VD.UPDATE.DATE.TIME` | `FsGiTxnManualVdUpdate_DateTime` |  |  |  |
| 49 | `FS.GI.TXN.MANUAL.VD.UPDATE.AUTHORISER` | `FsGiTxnManualVdUpdate_Authoriser` | String |  |  |
| 50 | `FS.GI.TXN.MANUAL.VD.UPDATE.CO.CODE` | `FsGiTxnManualVdUpdate_CoCode` | String |  |  |
| 51 | `FS.GI.TXN.MANUAL.VD.UPDATE.DEPT.CODE` | `FsGiTxnManualVdUpdate_DeptCode` | String |  |  |
| 52 | `FS.GI.TXN.MANUAL.VD.UPDATE.AUDITOR.CODE` | `FsGiTxnManualVdUpdate_AuditorCode` | String |  |  |
| 53 | `FS.GI.TXN.MANUAL.VD.UPDATE.AUDIT.DATE.TIME` | `FsGiTxnManualVdUpdate_AuditDateTime` | String |  |  |
