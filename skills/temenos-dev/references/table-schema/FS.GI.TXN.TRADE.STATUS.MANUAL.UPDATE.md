# FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.PARENT.REF.ID` | `FsGiTxnTradeStatusManualUpdate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.ORA.ROWID` | `FsGiTxnTradeStatusManualUpdate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.EXCHANGE.GROUP` | `FsGiTxnTradeStatusManualUpdate_ExchangeGroup` | TField |  | Fund exchange group. Multifonds DB Column is CGROUPE_COURS. |
| 4 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.CURRENT.DEAL.STATUS` | `FsGiTxnTradeStatusManualUpdate_CurrentDealStatus` | TField |  | Current deal status of the transaction. Multifonds DB Column is DEAL_STATUS_FROM. |
| 5 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.NEXT.DEAL.STATUS` | `FsGiTxnTradeStatusManualUpdate_NextDealStatus` | TField |  | Next deal status of the transaction. Multifonds DB Column is DEAL_STATUS_TO. |
| 6 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.ORDER.TYPE` | `FsGiTxnTradeStatusManualUpdate_OrderType` | TField |  | Order type. Multifonds DB Column is ORDER_TYPE. |
| 7 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.PII.RIGHTS.ENTITY.ONLY` | `FsGiTxnTradeStatusManualUpdate_PiiRightsEntityOnly` | TField |  | Entity type - All entities or PII Rights entity only. Multifonds DB Column is ENTITY_TYPE. |
| 8 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.ORDER.ID` | `FsGiTxnTradeStatusManualUpdate_OrderId` | TField |  | Order identification number. Multifonds DB Column is NORDER. |
| 9 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.DEAL.REFERENCE` | `FsGiTxnTradeStatusManualUpdate_DealReference` | TField |  | Deal reference number. Multifonds DB Column is DEAL_REF. |
| 10 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.IN.DEAL.REFERENCE` | `FsGiTxnTradeStatusManualUpdate_InDealReference` | TField |  | Deal reference number for transfer-in / switch-in leg. Multifonds DB Column is DEAL_REF_IN. |
| 11 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.AGENT.ID` | `FsGiTxnTradeStatusManualUpdate_AgentId` | TField |  | Agent identification number. Multifonds DB Column is NOUTLET. |
| 12 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.REGISTER.ID` | `FsGiTxnTradeStatusManualUpdate_RegisterId` | TField |  | Register identification number. Multifonds DB Column is NREGISTER. |
| 13 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.LEGAL.ENTITY.ID` | `FsGiTxnTradeStatusManualUpdate_LegalEntityId` | TField |  | Legal entity identification number. Multifonds DB Column is NTFC. |
| 14 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.TA.FUND.ID` | `FsGiTxnTradeStatusManualUpdate_TaFundId` | TField |  | Fund identification number. Multifonds DB Column is NPTF. |
| 15 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.SHARE.CLASS.CODE` | `FsGiTxnTradeStatusManualUpdate_ShareClassCode` | TField |  | Share class code linked to the fund. Multifonds DB Column is TPART. |
| 16 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.OPERATION.CODE` | `FsGiTxnTradeStatusManualUpdate_OperationCode` | TField |  | Operation code. Multifonds DB Column is COPERATION. |
| 17 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.STATUS` | `FsGiTxnTradeStatusManualUpdate_Status` | TField |  | Order status. Multifonds DB Column is STATUS. |
| 18 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.STATUS.DESCRIPTION` | `FsGiTxnTradeStatusManualUpdate_StatusDescription` | TField |  | Status description. Multifonds DB Column is STATUS_DESC. |
| 19 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.DEAL.STATUS` | `FsGiTxnTradeStatusManualUpdate_DealStatus` | TField |  | Deal status. Multifonds DB Column is DEAL_STATUS. |
| 20 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.NO.CASH.FLAG` | `FsGiTxnTradeStatusManualUpdate_NoCashFlag` | TField |  | External cash flag. Multifonds DB Column is FLG_NO_CASH. |
| 21 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.REGISTER.TYPE` | `FsGiTxnTradeStatusManualUpdate_RegisterType` | TField |  | Register Type code for cash handling Multifonds DB Column is TYPE_REG. |
| 22 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.SETTLEMENT.TYPE` | `FsGiTxnTradeStatusManualUpdate_SettlementType` | TField |  | Settlement type for Cash handling. Multifonds DB Column is TYPE_SETTLEMENT. |
| 23 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.DEAL.TYPE` | `FsGiTxnTradeStatusManualUpdate_DealType` | TField |  | Deal type for cash handling. Multifonds DB Column is TYPE_DEAL. |
| 24 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.LEG.LINK` | `FsGiTxnTradeStatusManualUpdate_LegLink` | TField |  | Leg link for switch / transfer orders; automatically populated. Multifonds DB Column is LEG_LINK. |
| 25 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.MANUAL.UPDATE.FLAG` | `FsGiTxnTradeStatusManualUpdate_ManualUpdateFlag` | TField |  | Flag to not count orders for pending warning messages if deal status is manually changed. Multifonds DB Column is FLG_MANUAL_UPDATE. |
| 26 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.PII.AGENT` | `FsGiTxnTradeStatusManualUpdate_PiiAgent` | TField |  | PII Agent Id. Multifonds DB Column is PII_OUTLET. |
| 27 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.PII.REGISTER` | `FsGiTxnTradeStatusManualUpdate_PiiRegister` | TField |  | PII Register Id. Multifonds DB Column is PII_REG. |
| 28 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.EXCHANGE.GROUP.PARAMETER` | `FsGiTxnTradeStatusManualUpdate_ExchangeGroupParameter` | TField |  | Fund exchange group filter. Multifonds DB Column is PRM_CGROUPE_COURS. |
| 29 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.DEAL.STATUS.FROM.PARAMETER` | `FsGiTxnTradeStatusManualUpdate_DealStatusFromParameter` | TField |  | Deal status from filter. Multifonds DB Column is PRM_DEAL_STATUS_FROM. |
| 30 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.ORDER.TYPE.PARAMETER` | `FsGiTxnTradeStatusManualUpdate_OrderTypeParameter` | TField |  | Order Type filter. Multifonds DB Column is PRM_ORDER_TYPE. |
| 31 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.ENTITY.TYPE.PARAMETER` | `FsGiTxnTradeStatusManualUpdate_EntityTypeParameter` | TField |  | Entity type filter. Multifonds DB Column is PRM_ENTITY_TYPE. |
| 32 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.FUND.ID` | `FsGiTxnTradeStatusManualUpdate_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 33 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.CLASS.CURRENCY` | `FsGiTxnTradeStatusManualUpdate_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 34 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RESERVED10` | `FsGiTxnTradeStatusManualUpdate_Reserved10` | TField |  |  |
| 35 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RESERVED9` | `FsGiTxnTradeStatusManualUpdate_Reserved9` | TField |  |  |
| 36 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RESERVED8` | `FsGiTxnTradeStatusManualUpdate_Reserved8` | TField |  |  |
| 37 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RESERVED7` | `FsGiTxnTradeStatusManualUpdate_Reserved7` | TField |  |  |
| 38 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RESERVED6` | `FsGiTxnTradeStatusManualUpdate_Reserved6` | TField |  |  |
| 39 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RESERVED5` | `FsGiTxnTradeStatusManualUpdate_Reserved5` | TField |  |  |
| 40 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RESERVED4` | `FsGiTxnTradeStatusManualUpdate_Reserved4` | TField |  |  |
| 41 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RESERVED3` | `FsGiTxnTradeStatusManualUpdate_Reserved3` | TField |  |  |
| 42 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RESERVED2` | `FsGiTxnTradeStatusManualUpdate_Reserved2` | TField |  |  |
| 43 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RESERVED1` | `FsGiTxnTradeStatusManualUpdate_Reserved1` | TField |  |  |
| 44 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.LOCAL.REF` | `FsGiTxnTradeStatusManualUpdate_LocalRef` |  |  |  |
| 45 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.OVERRIDE` | `FsGiTxnTradeStatusManualUpdate_Override` |  |  |  |
| 46 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.RECORD.STATUS` | `FsGiTxnTradeStatusManualUpdate_RecordStatus` | String |  |  |
| 47 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.CURR.NO` | `FsGiTxnTradeStatusManualUpdate_CurrNo` | String |  |  |
| 48 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.INPUTTER` | `FsGiTxnTradeStatusManualUpdate_Inputter` |  |  |  |
| 49 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.DATE.TIME` | `FsGiTxnTradeStatusManualUpdate_DateTime` |  |  |  |
| 50 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.AUTHORISER` | `FsGiTxnTradeStatusManualUpdate_Authoriser` | String |  |  |
| 51 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.CO.CODE` | `FsGiTxnTradeStatusManualUpdate_CoCode` | String |  |  |
| 52 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.DEPT.CODE` | `FsGiTxnTradeStatusManualUpdate_DeptCode` | String |  |  |
| 53 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.AUDITOR.CODE` | `FsGiTxnTradeStatusManualUpdate_AuditorCode` | String |  |  |
| 54 | `FS.GI.TXN.TRADE.STATUS.MANUAL.UPDATE.AUDIT.DATE.TIME` | `FsGiTxnTradeStatusManualUpdate_AuditDateTime` | String |  |  |
