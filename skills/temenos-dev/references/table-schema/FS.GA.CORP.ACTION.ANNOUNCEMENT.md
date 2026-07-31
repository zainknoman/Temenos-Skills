# FS.GA.CORP.ACTION.ANNOUNCEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORP.ACTION.ANNOUNCEMENT` in `FS_CorporateAction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.PARENT.REF.ID` | `FsGaCorpActionAnnouncement_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.ORA.ROWID` | `FsGaCorpActionAnnouncement_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.OPERATION.CODE` | `FsGaCorpActionAnnouncement_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 4 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.OPTION.AND.FUTURES.SEC.TYPE` | `FsGaCorpActionAnnouncement_OptionAndFuturesSecType` | TField |  | Option And Futures Security Type Multifonds DB Column is TYPE. |
| 5 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.INTERNAL.SECURITY.ID` | `FsGaCorpActionAnnouncement_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 6 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.NSEQUENCE` | `FsGaCorpActionAnnouncement_Nsequence` | TField |  | Corresponds to the sequence number Multifonds DB Column is NSEQ. |
| 7 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.SUBSEQUENCE.NUMBER` | `FsGaCorpActionAnnouncement_SubsequenceNumber` | TField |  | Corresponds to the sub sequence number Multifonds DB Column is NSUB_SEQ. |
| 8 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.STATUS.CODE.TRANSACTIONS` | `FsGaCorpActionAnnouncement_StatusCodeTransactions` | TField |  | Status code for transaction like 10 outstanding, 20 accounted etc Multifonds DB Column is CDSTATUS. |
| 9 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.ENTITLEMENT.DATE` | `FsGaCorpActionAnnouncement_EntitlementDate` | TField |  | The ex-date, or ex-dividend date, is the date on or after which a security is traded without a previously declared dividend or distribution. Multifonds DB Column is DEXEC. |
| 10 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.TRADE.DATE.FOR.CA` | `FsGaCorpActionAnnouncement_TradeDateForCa` | TField |  | Trade Date of the corporate action Multifonds DB Column is DACC. |
| 11 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.PAY.DATE` | `FsGaCorpActionAnnouncement_PayDate` | TField |  | Pay Date Multifonds DB Column is DVAL. |
| 12 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CORRESPONDENT` | `FsGaCorpActionAnnouncement_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 13 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.GL.SETTLEMENT.ACCOUNT` | `FsGaCorpActionAnnouncement_GlSettlementAccount` | TField |  | GL Settlement Account Number Multifonds DB Column is NRUBR_CORR. |
| 14 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CORRESPONDENT.CASH.SUFFIX.NUM` | `FsGaCorpActionAnnouncement_CorrespondentCashSuffixNum` | TField |  | Correspondent Cash Suffix Number Multifonds DB Column is NSUFF_CORR. |
| 15 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.BASE.QUANTITY` | `FsGaCorpActionAnnouncement_BaseQuantity` | TField |  | Enter a ratio as follows: 1 old securities will be equal to X amount of new security (e.g. a split); orX amount of old security (e.g. a bonus) Multifonds DB Column is QTE_BASE. |
| 16 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.UNIT.AMOUNT.CODE` | `FsGaCorpActionAnnouncement_UnitAmountCode` | TField |  | Unit amount Code like Receive Pay for Corporate action Multifonds DB Column is COD_CASH. |
| 17 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.UNIT.AMOUNT.CA` | `FsGaCorpActionAnnouncement_UnitAmountCa` | TField |  | Unit amount to Receive Pay for Corporate action Multifonds DB Column is MNT_PD. |
| 18 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CURRENCY.UNIT.AMOUNT.CA` | `FsGaCorpActionAnnouncement_CurrencyUnitAmountCa` | TField |  | Currency of Unit amount to Receive Pay for Corporate action Multifonds DB Column is CMON_CASH. |
| 19 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.EXTERNAL.REFERENCE.NUMBER` | `FsGaCorpActionAnnouncement_ExternalReferenceNumber` | TField |  | External reference corresponds a trade,security or fund Multifonds DB Column is EXT_REF. |
| 20 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.SHORT.DESCRIPTION` | `FsGaCorpActionAnnouncement_ShortDescription` | TField |  | Input the description of the transaction, else auto generated Multifonds DB Column is TXT_OST. |
| 21 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CLOSE.OLD.POSITION` | `FsGaCorpActionAnnouncement_CloseOldPosition` | TField |  | Close Old position Identifier for CA Multifonds DB Column is CLOSE. |
| 22 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.NEW.SECURITY.ID.CA` | `FsGaCorpActionAnnouncement_NewSecurityIdCa` | TField |  | New Security Id entitled in Corporate action Multifonds DB Column is NOVAL_C1. |
| 23 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.EX.RATE.CA` | `FsGaCorpActionAnnouncement_ExRateCa` | TField |  | Exchange rate for CA new security Multifonds DB Column is COURS_C1. |
| 24 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.QUANTITY.EXISTING.SECURITY.CA` | `FsGaCorpActionAnnouncement_QuantityExistingSecurityCa` | TField |  | Qty of existing security CA to be exchanged from Multifonds DB Column is QTE_RIGHT_C1. |
| 25 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.QTY.EXISTING.OR.NEWSECURITY.CA` | `FsGaCorpActionAnnouncement_QtyExistingOrNewsecurityCa` | TField |  | Qty of existing or new security CA to be exchanged to Multifonds DB Column is QTE_RIGHT_C2. |
| 26 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CA.ADDITION.TYPE` | `FsGaCorpActionAnnouncement_CaAdditionType` | TField |  | Type of CA addition like In addition , In replacement , Subtraction Multifonds DB Column is TYPE_C2. |
| 27 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.BOOK.VALUE.ADJ.TYPE.CA` | `FsGaCorpActionAnnouncement_BookValueAdjTypeCa` | TField |  | Book Value Adjustment and other types like Stock divident, Split action Multifonds DB Column is COD_AJUST. |
| 28 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.BOOK.VALUE.CORRECTION.TYPE.CA` | `FsGaCorpActionAnnouncement_BookValueCorrectionTypeCa` | TField |  | Correct book value by: Book Unit Amount , Ratio , Percentage Multifonds DB Column is COD_AJUST_CPTA. |
| 29 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CORRECTION.UNIT.AMOUNT.CCY` | `FsGaCorpActionAnnouncement_CorrectionUnitAmountCcy` | TField |  | Correction unit amount currency for Corporate action Multifonds DB Column is CMON_AJUST. |
| 30 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CORRECTION.UNIT.AMOUNT` | `FsGaCorpActionAnnouncement_CorrectionUnitAmount` | TField |  | Correction unit amount to be given when Corporate action when Book value correction type is Book Unit Amount Multifonds DB Column is MNT_UNIT_AJUST. |
| 31 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CORRECTION.RATIO` | `FsGaCorpActionAnnouncement_CorrectionRatio` | TField |  | Correction Ratio to be given when Book value correction type is Ratio Multifonds DB Column is PCT_RATIO. |
| 32 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CORRECTION.PERCENTAGE` | `FsGaCorpActionAnnouncement_CorrectionPercentage` | TField |  | Correction percentage to be given when Book value correction type is Percentage Multifonds DB Column is PCT_AJUST. |
| 33 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.STATUS.PENDING` | `FsGaCorpActionAnnouncement_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 34 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.ARCHIVE` | `FsGaCorpActionAnnouncement_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 35 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.COST.EXCHANGE.RATE.CA` | `FsGaCorpActionAnnouncement_CostExchangeRateCa` | TField |  | Use Cost exchange rate in Corporate action Multifonds DB Column is COST_TCHG. |
| 36 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.NEW.LOT` | `FsGaCorpActionAnnouncement_NewLot` | TField |  | New Lot Multifonds DB Column is FLG_NEW_LOT. |
| 37 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.TRADE.DATE.IDENTIFIER` | `FsGaCorpActionAnnouncement_TradeDateIdentifier` | TField |  | if the trade calculation process is run after the trade cut off time, the trade will be calculated with a trade date of T+1 rather than taking no action Multifonds DB Column is FLG_DOPER. |
| 38 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.MARKET.OPERATION.CODE` | `FsGaCorpActionAnnouncement_MarketOperationCode` | TField |  | Market operation code of corporate action Multifonds DB Column is COPER_MARKET. |
| 39 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CA.CODE.FOR.DERIVATIVES` | `FsGaCorpActionAnnouncement_CaCodeForDerivatives` | TField |  | Derivatives CA code like CFD and other derivatives to be applied for Corporate action Multifonds DB Column is CODE_CA. |
| 40 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.NEW.CFD.ID` | `FsGaCorpActionAnnouncement_NewCfdId` | TField |  | User can give the CFD ID for which there is a new security created by the corporate action as its underlying security. Multifonds DB Column is NFUT_C1. |
| 41 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CASH.RECEIVED.ON.OLD.SECURITY` | `FsGaCorpActionAnnouncement_CashReceivedOnOldSecurity` | TField |  | Cash Received on Old security for corporate action Multifonds DB Column is RECD_ON_OLD_SECURITY. |
| 42 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.DROP.FRACTIONAL.SHARES.CA` | `FsGaCorpActionAnnouncement_DropFractionalSharesCa` | TField |  | Drop Fractional shares in case of odd shares entitled in Corporate action Multifonds DB Column is FLG_DROP_FRC_SHRS. |
| 43 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.SECURITY.RATIO` | `FsGaCorpActionAnnouncement_SecurityRatio` | TField |  | Security Ratio Multifonds DB Column is SEC_RATIO. |
| 44 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.SECURITY.DEFAULT` | `FsGaCorpActionAnnouncement_SecurityDefault` | TField |  | Security Default Multifonds DB Column is SEC_DEFAULT. |
| 45 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CASH.RATIO` | `FsGaCorpActionAnnouncement_CashRatio` | TField |  | Cash Ratio Multifonds DB Column is CASH_RATIO. |
| 46 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CASH.DEFAULT` | `FsGaCorpActionAnnouncement_CashDefault` | TField |  | Cash Default Multifonds DB Column is CASH_DEFAULT. |
| 47 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CASH.GROSS.RATE` | `FsGaCorpActionAnnouncement_CashGrossRate` | TField |  | Cash Gross Rate Multifonds DB Column is CASH_GROSS_RATE. |
| 48 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.ACCEPT` | `FsGaCorpActionAnnouncement_Accept` | TField |  | Flag Accept Multifonds DB Column is FLG_ACCEPT. |
| 49 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.REJECT` | `FsGaCorpActionAnnouncement_Reject` | TField |  | Flag Reject Multifonds DB Column is FLG_REJECT. |
| 50 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.PA.MODULE` | `FsGaCorpActionAnnouncement_PaModule` | TField |  | PA Module Multifonds DB Column is FLG_PA_MODULE. |
| 51 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RECORD.DATE` | `FsGaCorpActionAnnouncement_RecordDate` | TField |  | The record date, or date of record, is the cut-off date established by a company in order to determine which shareholders are eligible to receive a dividend or distribution Multifonds DB Column is DRECORD. |
| 52 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.ANNOUNCE.DATE` | `FsGaCorpActionAnnouncement_AnnounceDate` | TField |  | Announce Date Multifonds DB Column is DANNOUNCE. |
| 53 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.ACTION` | `FsGaCorpActionAnnouncement_Action` | TField |  | Action Multifonds DB Column is ACTION. |
| 54 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.PA.STATUS` | `FsGaCorpActionAnnouncement_PaStatus` | TField |  | PA Status Multifonds DB Column is PA_CDSTATUS. |
| 55 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.SECURITY.ID.CODE.C1` | `FsGaCorpActionAnnouncement_SecurityIdCodeC1` | TField |  | Security ID Code C1 Multifonds DB Column is ID_CODE_SEC_C1. |
| 56 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.EXTERNAL.SECURITY.ID` | `FsGaCorpActionAnnouncement_ExternalSecurityId` | TField |  | The External identification code for Security like 01 for Telekurs, 03 for Sedol. Also used for other provider identifiers Multifonds DB Column is SEC_ID. |
| 57 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.PROVIDER.CODE.OF.NEW.SECURITY` | `FsGaCorpActionAnnouncement_ProviderCodeOfNewSecurity` | TField |  | Exernal provider code for New security like 03 for Sedol Multifonds DB Column is SEC_ID_C1. |
| 58 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.SECURITY.ID.CODE` | `FsGaCorpActionAnnouncement_SecurityIdCode` | TField |  | Security Id Code Multifonds DB Column is ID_CODE_SEC. |
| 59 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.MIGRATE` | `FsGaCorpActionAnnouncement_Migrate` | TField |  | Flag Migrate Multifonds DB Column is FLG_MIGRATE. |
| 60 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.SECURITY` | `FsGaCorpActionAnnouncement_Security` | TField |  | Existing Security identification Multifonds DB Column is NOVAL_LINK. |
| 61 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CA.OPERATION.CODE.LINK` | `FsGaCorpActionAnnouncement_CaOperationCodeLink` | TField |  | Corporate action Op code like 421 etc for linking another corporate action Multifonds DB Column is COPER_LINK. |
| 62 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.SEQUENCE.NUMBER.OF.CA` | `FsGaCorpActionAnnouncement_SequenceNumberOfCa` | TField |  | Sequence number of CA Multifonds DB Column is NSEQ_LINK. |
| 63 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.SUB.SEQUENCE.NUMBER.OF.CA` | `FsGaCorpActionAnnouncement_SubSequenceNumberOfCa` | TField |  | Sub sequence Number of CA Multifonds DB Column is NSUB_SEQ_LINK. |
| 64 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.VOLUNTARY.CA.IDENTIFIER` | `FsGaCorpActionAnnouncement_VoluntaryCaIdentifier` | TField |  | Flag Voluntary CA Multifonds DB Column is FLG_VOLUNTARY. |
| 65 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.EX.DATE` | `FsGaCorpActionAnnouncement_ExDate` | TField |  | Execution date for Dividend announcement and Corporate Action Multifonds DB Column is DPAYMNT. |
| 66 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CUSTODIAN.DEADLINE` | `FsGaCorpActionAnnouncement_CustodianDeadline` | TField |  | Custodian Deadline Multifonds DB Column is DCUST_DEADLINE. |
| 67 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CLIENT.RESPOND.DEADLINE` | `FsGaCorpActionAnnouncement_ClientRespondDeadline` | TField |  | Client Respond Deadline Multifonds DB Column is DCLIENT_RESPOND. |
| 68 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CLIENT.RESPOND.RECEIPT.DATE` | `FsGaCorpActionAnnouncement_ClientRespondReceiptDate` | TField |  | Client Respond Receipt Date Multifonds DB Column is DCLIENT_RES_RECEIPT. |
| 69 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CUSTODIAN.STATUS.RECEIPT.DATE` | `FsGaCorpActionAnnouncement_CustodianStatusReceiptDate` | TField |  | Custodian Status Receipt Date Multifonds DB Column is DCUST_STAT_RECEIPT. |
| 70 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.PARTIAL.CA` | `FsGaCorpActionAnnouncement_PartialCa` | TField |  | Partial corporate action applicable or not Multifonds DB Column is FLG_PARTIAL_CA. |
| 71 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.IDENTIFIER.VOLUNTARY.CA` | `FsGaCorpActionAnnouncement_IdentifierVoluntaryCa` | TField |  | Voluntary CA Flag Multifonds DB Column is FLG_VOL_CA. |
| 72 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.FLAG.COST.ADJUSTMENT.CA` | `FsGaCorpActionAnnouncement_FlagCostAdjustmentCa` | TField |  | Flag Cost Adustment CA Multifonds DB Column is FLG_ROC_CA_TCHG. |
| 73 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.SHARE.AVAILABLE.DATE` | `FsGaCorpActionAnnouncement_ShareAvailableDate` | TField |  | Share Available Date Multifonds DB Column is SHARE_AVAIL_DATE. |
| 74 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CORPORATE.ACTION.TYPE` | `FsGaCorpActionAnnouncement_CorporateActionType` | TField |  | Corporate Action Type Multifonds DB Column is CA_TYPE. |
| 75 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RESERVED10` | `FsGaCorpActionAnnouncement_Reserved10` | TField |  |  |
| 76 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RESERVED9` | `FsGaCorpActionAnnouncement_Reserved9` | TField |  |  |
| 77 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RESERVED8` | `FsGaCorpActionAnnouncement_Reserved8` | TField |  |  |
| 78 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RESERVED7` | `FsGaCorpActionAnnouncement_Reserved7` | TField |  |  |
| 79 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RESERVED6` | `FsGaCorpActionAnnouncement_Reserved6` | TField |  |  |
| 80 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RESERVED5` | `FsGaCorpActionAnnouncement_Reserved5` | TField |  |  |
| 81 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RESERVED4` | `FsGaCorpActionAnnouncement_Reserved4` | TField |  |  |
| 82 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RESERVED3` | `FsGaCorpActionAnnouncement_Reserved3` | TField |  |  |
| 83 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RESERVED2` | `FsGaCorpActionAnnouncement_Reserved2` | TField |  |  |
| 84 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RESERVED1` | `FsGaCorpActionAnnouncement_Reserved1` | TField |  |  |
| 85 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.LOCAL.REF` | `FsGaCorpActionAnnouncement_LocalRef` |  |  |  |
| 86 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.OVERRIDE` | `FsGaCorpActionAnnouncement_Override` |  |  |  |
| 87 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.RECORD.STATUS` | `FsGaCorpActionAnnouncement_RecordStatus` | String |  |  |
| 88 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CURR.NO` | `FsGaCorpActionAnnouncement_CurrNo` | String |  |  |
| 89 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.INPUTTER` | `FsGaCorpActionAnnouncement_Inputter` |  |  |  |
| 90 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.DATE.TIME` | `FsGaCorpActionAnnouncement_DateTime` |  |  |  |
| 91 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.AUTHORISER` | `FsGaCorpActionAnnouncement_Authoriser` | String |  |  |
| 92 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.CO.CODE` | `FsGaCorpActionAnnouncement_CoCode` | String |  |  |
| 93 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.DEPT.CODE` | `FsGaCorpActionAnnouncement_DeptCode` | String |  |  |
| 94 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.AUDITOR.CODE` | `FsGaCorpActionAnnouncement_AuditorCode` | String |  |  |
| 95 | `FS.GA.CORP.ACTION.ANNOUNCEMENT.AUDIT.DATE.TIME` | `FsGaCorpActionAnnouncement_AuditDateTime` | String |  |  |
