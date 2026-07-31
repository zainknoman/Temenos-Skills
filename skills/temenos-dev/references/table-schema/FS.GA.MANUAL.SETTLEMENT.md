# FS.GA.MANUAL.SETTLEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.MANUAL.SETTLEMENT` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.MANUAL.SETTLEMENT.FUND.ID` | `FsGaManualSettlement_Fund` |  |  |  |
| 2 | `GA.MANUAL.SETTLEMENT.SERVICE.CODE` | `FsGaManualSettlement_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 3 | `GA.MANUAL.SETTLEMENT.INTERNAL.TRANSACTION.ENTRY.NUM` | `FsGaManualSettlement_InternalTransactionEntryNum` | TField |  | This is the internal entry number for a transaction. Multifonds DB Column is NECRITURE. |
| 4 | `GA.MANUAL.SETTLEMENT.SETTLEMENT.SERVICE.CODE` | `FsGaManualSettlement_SettlementServiceCode` | TField |  | Settlement Service Code Multifonds DB Column is CSERV_SETTLE. |
| 5 | `GA.MANUAL.SETTLEMENT.TRANSACTION.NUMBER` | `FsGaManualSettlement_EntryNumber` |  |  |  |
| 6 | `GA.MANUAL.SETTLEMENT.DEAL.STATUS.CODE` | `FsGaManualSettlement_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 7 | `GA.MANUAL.SETTLEMENT.LOCAL.CURRENCY` | `FsGaManualSettlement_Currency` |  |  |  |
| 8 | `GA.MANUAL.SETTLEMENT.AMOUNT.IN.LOCAL.LOCAL.CURRENCY` | `FsGaManualSettlement_FeesAmountDealCcy` |  |  |  |
| 9 | `GA.MANUAL.RATE.OF.EXCHANGE` | `FsGaManualSettlement_ExchangeRate` |  |  |  |
| 10 | `GA.MANUAL.SETTLEMENT.ARCHIVE` | `FsGaManualSettlement_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 11 | `GA.MANUAL.SETTLEMENT.FUND.AMOUNT` | `FsGaManualSettlement_FundAmount` | TField |  | Fund Amount Multifonds DB Column is MNTPTF. |
| 12 | `GA.MANUAL.SETTLEMENT.EXCH.RATE.SETTLEMENT.TO.DEAL` | `FsGaManualSettlement_ExchRateSettlementToDeal` | TField |  | The exchange rate between the settlement and deal currency Multifonds DB Column is TCHG_PTF. |
| 13 | `GA.MANUAL.SETTLEMENT.FUND.TRANSAC.NUMBER` | `FsGaManualSettlement_FundEntryNumber` | TField |  | Entry number of the fund Multifonds DB Column is NECRITUR_PTF. |
| 14 | `GA.MANUAL.SETTLEMENT.IFRS.TAG` | `FsGaManualSettlement_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 15 | `GA.MANUAL.SETTLEMENT.STATUS.PENDING` | `FsGaManualSettlement_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 16 | `GA.MANUAL.SETTLEMENT.QUANTITIES` | `FsGaManualSettlement_Quantities` | TField |  | Quantities Multifonds DB Column is QUANTITY. |
| 17 | `GA.MANUAL.SETTLEMENT.OPERATION.CODE` | `FsGaManualSettlement_TransactionType` |  |  |  |
| 18 | `GA.MANUAL.SETTLEMENT.EXTERNAL.REFERENCE.NUMBER` | `FsGaManualSettlement_ReferenceExternal` |  |  |  |
| 19 | `GA.MANUAL.SETTLEMENT.TRADE.DATE` | `FsGaManualSettlement_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 20 | `GA.MANUAL.SETTLEMENT.INTERNAL.SECURITY.ID` | `FsGaManualSettlement_SecurityId` |  |  |  |
| 21 | `GA.MANUAL.SETTLEMENT.DEAL.AMOUNT` | `FsGaManualSettlement_DealAmount` | TField |  | Deal Amount Multifonds DB Column is MONTANT_DEAL. |
| 22 | `GA.MANUAL.SETTLEMENT.FORCED.RATE.OF.EXCHANGE` | `FsGaManualSettlement_ForcedExchangeRate` | TField |  | Forced Exchange Rate Multifonds DB Column is TCHG_FORCED. |
| 23 | `GA.MANUAL.SETTLEMENT.FORCED.LOCAL.CURRENCY` | `FsGaManualSettlement_ForcedCurrency` | TField |  | Forced Currency Multifonds DB Column is CMON_FORCED. |
| 24 | `GA.MANUAL.SETTLEMENT.FORCED.AMOUNT` | `FsGaManualSettlement_ForcedAmount` | TField |  | Forced Amount Multifonds DB Column is MONTANT_FORCED. |
| 25 | `GA.MANUAL.SETTLEMENT.REC.TAX.IN.AMOUNT.TYPE.1` | `FsGaManualSettlement_RecTaxInAmountType1` | TField |  | Recoverable tax amount on Income , type 1 Multifonds DB Column is MNTRECTAX. |
| 26 | `GA.MANUAL.SETTLEMENT.UNREC.TAX.IN.AMOUNT.TYPE.1` | `FsGaManualSettlement_UnrecTaxInAmountType1` | TField |  | Unrecoverable tax amount on Income , type 1 Multifonds DB Column is MNTUNRECTAX. |
| 27 | `GA.MANUAL.SETTLEMENT.SETTLE.DATE` | `FsGaManualSettlement_SettlementDate` |  |  |  |
| 28 | `GA.MANUAL.SETTLEMENT.MANUAL.SETTLEMENT.FLAG` | `FsGaManualSettlement_ManualSettlementFlag` | TField |  | Manual Settlement Flag Multifonds DB Column is FLG_MANUAL_SETTL. |
| 29 | `GA.MANUAL.SETTLEMENT.LOCAL.SETTLEMENT.VCI` | `FsGaManualSettlement_LocalSettlementVci` | TField |  | Local Settlement Vci Multifonds DB Column is LOC_SETT_VCI. |
| 30 | `GA.MANUAL.SETTLEMENT.FUND.SETTLEMENT.VCI` | `FsGaManualSettlement_FundSettlementVci` | TField |  | Fund Settlement Vci Multifonds DB Column is SETTL_PTF_VCI. |
| 31 | `GA.MANUAL.SETTLEMENT.FUND.VCI.LOC` | `FsGaManualSettlement_FundVciLoc` | TField |  | Fund VCI Loc Multifonds DB Column is LOC_PTF_VCI. |
| 32 | `GA.MANUAL.SETTLEMENT.OLD.AMOUNT` | `FsGaManualSettlement_OldAmount` | TField |  | Old Amount Multifonds DB Column is OLD_MONTANT. |
| 33 | `GA.MANUAL.SETTLEMENT.OLD.FUND.AMOUNT` | `FsGaManualSettlement_OldFundAmount` | TField |  | Old Fund Amount Multifonds DB Column is OLD_MNTPTF. |
| 34 | `GA.MANUAL.SETTLEMENT.REBATE.FEE.FLAG` | `FsGaManualSettlement_RebateFeeFlag` | TField |  | Rebate Fee Flag Multifonds DB Column is FLG_REBATE_FEE. |
| 35 | `GA.MANUAL.SETTLEMENT.OLD.STATUS` | `FsGaManualSettlement_OldStatus` | TField |  | Old Status Multifonds DB Column is OLD_CSTATUS. |
| 36 | `GA.MANUAL.SETTLEMENT.NEXT` | `FsGaManualSettlement_Next` | TField |  | Next Multifonds DB Column is NEXT. |
| 37 | `GA.MANUAL.SETTLEMENT.SETTLE.ID` | `FsGaManualSettlement_SettleId` | TField |  | Settle ID Multifonds DB Column is SETTLEID. |
| 38 | `GA.MANUAL.SETTLEMENT.RESERVED10` | `FsGaManualSettlement_Reserved10` | TField |  |  |
| 39 | `GA.MANUAL.SETTLEMENT.RESERVED9` | `FsGaManualSettlement_Reserved9` | TField |  |  |
| 40 | `GA.MANUAL.SETTLEMENT.RESERVED8` | `FsGaManualSettlement_Reserved8` | TField |  |  |
| 41 | `GA.MANUAL.SETTLEMENT.RESERVED7` | `FsGaManualSettlement_Reserved7` | TField |  |  |
| 42 | `GA.MANUAL.SETTLEMENT.RESERVED6` | `FsGaManualSettlement_Reserved6` | TField |  |  |
| 43 | `GA.MANUAL.SETTLEMENT.RESERVED5` | `FsGaManualSettlement_Reserved5` | TField |  |  |
| 44 | `GA.MANUAL.SETTLEMENT.RESERVED4` | `FsGaManualSettlement_Reserved4` | TField |  |  |
| 45 | `GA.MANUAL.SETTLEMENT.RESERVED3` | `FsGaManualSettlement_Reserved3` | TField |  |  |
| 46 | `GA.MANUAL.SETTLEMENT.RESERVED2` | `FsGaManualSettlement_Reserved2` | TField |  |  |
| 47 | `GA.MANUAL.SETTLEMENT.RESERVED1` | `FsGaManualSettlement_Reserved1` | TField |  |  |
| 48 | `GA.MANUAL.SETTLEMENT.RECORD.STATUS` | `FsGaManualSettlement_RecordStatus` | String |  |  |
| 49 | `GA.MANUAL.SETTLEMENT.CURR.NO` | `FsGaManualSettlement_CurrNo` | String |  |  |
| 50 | `GA.MANUAL.SETTLEMENT.INPUTTER` | `FsGaManualSettlement_Inputter` |  |  |  |
| 51 | `GA.MANUAL.SETTLEMENT.DATE.TIME` | `FsGaManualSettlement_DateTime` |  |  |  |
| 52 | `GA.MANUAL.SETTLEMENT.AUTHORISER` | `FsGaManualSettlement_Authoriser` | String |  |  |
| 53 | `GA.MANUAL.SETTLEMENT.CO.CODE` | `FsGaManualSettlement_CoCode` | String |  |  |
| 54 | `GA.MANUAL.SETTLEMENT.DEPT.CODE` | `FsGaManualSettlement_DeptCode` | String |  |  |
| 55 | `GA.MANUAL.SETTLEMENT.AUDITOR.CODE` | `FsGaManualSettlement_AuditorCode` | String |  |  |
| 56 | `GA.MANUAL.SETTLEMENT.AUDIT.DATE.TIME` | `FsGaManualSettlement_AuditDateTime` | String |  |  |
