# FS.GA.ENGAGEMENT.ADJUSTMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.ENGAGEMENT.ADJUSTMENT` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ENGAGEMENT.ADJUST.FUND.ID` | `FsGaEngagementAdjustment_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.ENGAGEMENT.ADJUST.SERVICE.CODE` | `FsGaEngagementAdjustment_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 3 | `FS.GA.ENGAGEMENT.ADJUST.INTERNAL.SECURITY.ID` | `FsGaEngagementAdjustment_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 4 | `FS.GA.ENGAGEMENT.ADJUST.PROVIDER.ID` | `FsGaEngagementAdjustment_ProviderId` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 5 | `FS.GA.ENGAGEMENT.ADJUST.COUNTERPARTY.CORRESPONDENT` | `FsGaEngagementAdjustment_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 6 | `FS.GA.ENGAGEMENT.ADJUST.LOT.NUMBER` | `FsGaEngagementAdjustment_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 7 | `FS.GA.ENGAGEMENT.ADJUST.TRANSACION.NUMBER` | `FsGaEngagementAdjustment_TransacNumber` |  |  |  |
| 8 | `FS.GA.ENGAGEMENT.ADJUST.QUANTITY` | `FsGaEngagementAdjustment_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 9 | `FS.GA.ENGAGEMENT.ADJUST.LAST.CONTRACT.PRICE` | `FsGaEngagementAdjustment_LastContractPrice` | TField |  | Contract price corresponding to the deal or to the last engagement adjustment modification Multifonds DB Column is COURS_LAST. |
| 10 | `FS.GA.ENGAGEMENT.ADJUST.NEW.CONTRACT.PRICE` | `FsGaEngagementAdjustment_NewContractPrice` | TField |  | New Contract price to be input Multifonds DB Column is COURS_NEW. |
| 11 | `FS.GA.ENGAGEMENT.ADJUST.LAST.EXCHANGE.RATE` | `FsGaEngagementAdjustment_LastExchangeRate` | TField |  | Corresponds to the exchange rate applied to the previous future engagement adjustment Multifonds DB Column is TCHG_LAST. |
| 12 | `FS.GA.ENGAGEMENT.ADJUST.NEW.EXCHANGE.RATE` | `FsGaEngagementAdjustment_NewExchangeRate` | TField |  | Exchange rate corresponding to the security borrowing deal or to the last engagement adjustment modification Multifonds DB Column is TCHG_NEW. |
| 13 | `FS.GA.ENGAGEMENT.ADJUST.SETTLE.DATE` | `FsGaEngagementAdjustment_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 14 | `FS.GA.ENGAGEMENT.ADJUST.TRADE.DATE` | `FsGaEngagementAdjustment_TradeDate` | TField |  | Trade date of the transaction Multifonds DB Column is DOPER. |
| 15 | `FS.GA.ENGAGEMENT.ADJUST.DEAL.STATUS.CODE` | `FsGaEngagementAdjustment_DealStatusCode` | TField |  | Deal Status Code Multifonds DB Column is CSTATUS. |
| 16 | `FS.GA.ENGAGEMENT.ADJUST.STATUS.PENDING` | `FsGaEngagementAdjustment_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 17 | `FS.GA.ENGAGEMENT.ADJUST.MANAGER.CODE` | `FsGaEngagementAdjustment_ManagerCodeId` |  |  |  |
| 18 | `FS.GA.ENGAGEMENT.ADJUST.DEAL.CURRENCY` | `FsGaEngagementAdjustment_DealCurrency` | TField |  | Currency of settlement or currency of deal Multifonds DB Column is CDEV. |
| 19 | `FS.GA.ENGAGEMENT.ADJUST.FLAG.UNDERLYING` | `FsGaEngagementAdjustment_FlagUnderlying` | TField |  | Flag Underlying Multifonds DB Column is FLG_JTITR. |
| 20 | `FS.GA.ENGAGEMENT.ADJUST.LENDING.SUFFIX.NUMBER` | `FsGaEngagementAdjustment_LendingSuffixNumber` | TField |  | Lending Suffix Number Multifonds DB Column is NSUFF_LEN. |
| 21 | `FS.GA.ENGAGEMENT.ADJUST.ARCHIVE` | `FsGaEngagementAdjustment_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 22 | `FS.GA.ENGAGEMENT.ADJUST.FUTURE.ENTRY.NUMBER` | `FsGaEngagementAdjustment_FutureEntryNumber` | TField |  | Future Entry Number Multifonds DB Column is NECRITUR_FUT. |
| 23 | `FS.GA.ENGAGEMENT.ADJUST.BASKET.REFERENCE` | `FsGaEngagementAdjustment_BasketReference` | TField |  | The basket reference is a control of uniqueness done on the fund ID, the currency, the counterpart and the maturity date Multifonds DB Column is BASKET_REF. |
| 24 | `FS.GA.ENGAGEMENT.ADJUST.GROSS.AMNT.IN.LOCAL.CCY` | `FsGaEngagementAdjustment_GrossAmntInLocalCcy` | TField |  | Gross amount in security currency Multifonds DB Column is MONTANT_OPER. |
| 25 | `FS.GA.ENGAGEMENT.ADJUST.FLAG.FONGIBILITY` | `FsGaEngagementAdjustment_FlagFongibility` | TField |  | Flag FONGIBILITY Multifonds DB Column is FLG_FONGIBILITY. |
| 26 | `FS.GA.ENGAGEMENT.ADJUST.SHARE.CLASS.CODE` | `FsGaEngagementAdjustment_ShareClassCode` | TField |  | Share class Multifonds DB Column is TPARTS. |
| 27 | `FS.GA.ENGAGEMENT.ADJUST.BROKER.ID` | `FsGaEngagementAdjustment_BrokerId` | TField |  | Enter the broker number Multifonds DB Column is NCORR_VAR_MARG. |
| 28 | `FS.GA.ENGAGEMENT.ADJUST.COMMISSION.AMOUNT.BALANCE` | `FsGaEngagementAdjustment_CommissionAmountBalance` | TField |  | Commission Amount Balance Multifonds DB Column is MNT_COMM_BAL. |
| 29 | `FS.GA.ENGAGEMENT.ADJUST.COMMISSION.AMOUNT.CLOSE` | `FsGaEngagementAdjustment_CommissionAmountClose` | TField |  | Commission Amount Close Multifonds DB Column is MNT_COMM_CLOSE. |
| 30 | `FS.GA.ENGAGEMENT.ADJUST.MATURITY.NB.DAYS` | `FsGaEngagementAdjustment_MaturityNbDays` | TField |  | Maturity NB Days Multifonds DB Column is MAT_NBJOURS. |
| 31 | `FS.GA.ENGAGEMENT.ADJUST.RESERVED10` | `FsGaEngagementAdjustment_Reserved10` | TField |  |  |
| 32 | `FS.GA.ENGAGEMENT.ADJUST.RESERVED9` | `FsGaEngagementAdjustment_Reserved9` | TField |  |  |
| 33 | `FS.GA.ENGAGEMENT.ADJUST.RESERVED8` | `FsGaEngagementAdjustment_Reserved8` | TField |  |  |
| 34 | `FS.GA.ENGAGEMENT.ADJUST.RESERVED7` | `FsGaEngagementAdjustment_Reserved7` | TField |  |  |
| 35 | `FS.GA.ENGAGEMENT.ADJUST.RESERVED6` | `FsGaEngagementAdjustment_Reserved6` | TField |  |  |
| 36 | `FS.GA.ENGAGEMENT.ADJUST.RESERVED5` | `FsGaEngagementAdjustment_Reserved5` | TField |  |  |
| 37 | `FS.GA.ENGAGEMENT.ADJUST.RESERVED4` | `FsGaEngagementAdjustment_Reserved4` | TField |  |  |
| 38 | `FS.GA.ENGAGEMENT.ADJUST.RESERVED3` | `FsGaEngagementAdjustment_Reserved3` | TField |  |  |
| 39 | `FS.GA.ENGAGEMENT.ADJUST.RESERVED2` | `FsGaEngagementAdjustment_Reserved2` | TField |  |  |
| 40 | `FS.GA.ENGAGEMENT.ADJUST.RESERVED1` | `FsGaEngagementAdjustment_Reserved1` | TField |  |  |
| 41 | `FS.GA.ENGAGEMENT.ADJUST.LOCAL.REF` | `FsGaEngagementAdjustment_LocalRef` |  |  |  |
| 42 | `FS.GA.ENGAGEMENT.ADJUST.OVERRIDE` | `FsGaEngagementAdjustment_Override` |  |  |  |
| 43 | `FS.GA.ENGAGEMENT.ADJUST.RECORD.STATUS` | `FsGaEngagementAdjustment_RecordStatus` | String |  |  |
| 44 | `FS.GA.ENGAGEMENT.ADJUST.CURR.NO` | `FsGaEngagementAdjustment_CurrNo` | String |  |  |
| 45 | `FS.GA.ENGAGEMENT.ADJUST.INPUTTER` | `FsGaEngagementAdjustment_Inputter` |  |  |  |
| 46 | `FS.GA.ENGAGEMENT.ADJUST.DATE.TIME` | `FsGaEngagementAdjustment_DateTime` |  |  |  |
| 47 | `FS.GA.ENGAGEMENT.ADJUST.AUTHORISER` | `FsGaEngagementAdjustment_Authoriser` | String |  |  |
| 48 | `FS.GA.ENGAGEMENT.ADJUST.CO.CODE` | `FsGaEngagementAdjustment_CoCode` | String |  |  |
| 49 | `FS.GA.ENGAGEMENT.ADJUST.DEPT.CODE` | `FsGaEngagementAdjustment_DeptCode` | String |  |  |
| 50 | `FS.GA.ENGAGEMENT.ADJUST.AUDITOR.CODE` | `FsGaEngagementAdjustment_AuditorCode` | String |  |  |
| 51 | `FS.GA.ENGAGEMENT.ADJUST.AUDIT.DATE.TIME` | `FsGaEngagementAdjustment_AuditDateTime` | String |  |  |
