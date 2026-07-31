# FS.GA.CORPORATEACTION.ANNOUNCEMENTS — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORPORATEACTION.ANNOUNCEMENTS` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CORPORATEACTION.ANNOUNCEMENTS.TRANSACTION.CODE` | `FsGaCorporateactionAnnouncements_OperationCode` |  |  |  |
| 2 | `CORPORATEACTION.ANNOUNCEMENTS.OPTION.FUTURE.TYPE` | `FsGaCorporateactionAnnouncements_OptionFutureType` | TField |  | Option Future Type Multifonds DB Column is TYPE. |
| 3 | `CORPORATEACTION.ANNOUNCEMENTS.SECURITY` | `FsGaCorporateactionAnnouncements_Security` | TField |  | Security Multifonds DB Column is NOVAL. |
| 4 | `CORPORATEACTION.ANNOUNCEMENTS.SEQUENCE.NUMBER` | `FsGaCorporateactionAnnouncements_SequenceNumber` | TField |  | Sequence Number Multifonds DB Column is NSEQ. |
| 5 | `CORPORATEACTION.ANNOUNCEMENTS.SUB.SEQUENCE.NUMBER` | `FsGaCorporateactionAnnouncements_SubSequenceNumber` | TField |  | Sub Sequence Number Multifonds DB Column is NSUB_SEQ. |
| 6 | `CORPORATEACTION.ANNOUNCEMENTS.STATUS` | `FsGaCorporateactionAnnouncements_Status` | TField |  | Status Multifonds DB Column is CDSTATUS. |
| 7 | `CORPORATEACTION.ANNOUNCEMENTS.ENTITLEMENT.DATE` | `FsGaCorporateactionAnnouncements_EntitlementDate` | TField |  | Entitlement Date Multifonds DB Column is DEXEC. |
| 8 | `CORPORATEACTION.ANNOUNCEMENTS.ACCOUNTING.DATE` | `FsGaCorporateactionAnnouncements_AccountingDate` | TField |  | Accounting date Multifonds DB Column is DACC. |
| 9 | `CORPORATEACTION.ANNOUNCEMENTS.VALUE.DATE` | `FsGaCorporateactionAnnouncements_ValueDate` | TField |  | Value Date Multifonds DB Column is DVAL. |
| 10 | `CORPORATEACTION.ANNOUNCEMENTS.CORRESPONDANT` | `FsGaCorporateactionAnnouncements_Correspondant` | TField |  | Correspondant Multifonds DB Column is NCORRESP. |
| 11 | `CORPORATEACTION.ANNOUNCEMENTS.ACCOUNT` | `FsGaCorporateactionAnnouncements_Account` | TField |  | Account Multifonds DB Column is NRUBR_CORR. |
| 12 | `CORPORATEACTION.ANNOUNCEMENTS.SUFFIX` | `FsGaCorporateactionAnnouncements_Suffix` | TField |  | Suffix Multifonds DB Column is NSUFF_CORR. |
| 13 | `CORPORATEACTION.ANNOUNCEMENTS.GIVE.FOR` | `FsGaCorporateactionAnnouncements_GiveFor` | TField |  | Give For Multifonds DB Column is QTE_BASE. |
| 14 | `CORPORATEACTION.ANNOUNCEMENTS.UNIT.AMOUNT.TYPE` | `FsGaCorporateactionAnnouncements_UnitAmountType` | TField |  | Unit amount Type Multifonds DB Column is COD_CASH. |
| 15 | `CORPORATEACTION.ANNOUNCEMENTS.UNIT.AMOUNT.TO.PAY` | `FsGaCorporateactionAnnouncements_UnitAmountToPay` | TField |  | Unit amount to Pay Multifonds DB Column is MNT_PD. |
| 16 | `CORPORATEACTION.ANNOUNCEMENTS.NEW.SECURITY.LOCAL.CURRENCY` | `FsGaCorporateactionAnnouncements_NewSecurityCurrency` | TField |  | New security currency Multifonds DB Column is CMON_CASH. |
| 17 | `CORPORATEACTION.ANNOUNCEMENTS.TELEKURS` | `FsGaCorporateactionAnnouncements_Telekurs` | TField |  | Telekurs Multifonds DB Column is EXT_REF. |
| 18 | `CORPORATEACTION.ANNOUNCEMENTS.INTERNAL.DESCRIPTION` | `FsGaCorporateactionAnnouncements_InternalDescription` | TField |  | Internal Description Multifonds DB Column is TXT_OST. |
| 19 | `CORPORATEACTION.ANNOUNCEMENTS.CLOSE.OLD.POSITION` | `FsGaCorporateactionAnnouncements_CloseOldPosition` | TField |  | Close old Position Multifonds DB Column is CLOSE. |
| 20 | `CORPORATEACTION.ANNOUNCEMENTS.NEW.SECURITY` | `FsGaCorporateactionAnnouncements_NewSecurity` | TField |  | New security Multifonds DB Column is NOVAL_C1. |
| 21 | `CORPORATEACTION.ANNOUNCEMENTS.RATE.OF.EXCHANGE` | `FsGaCorporateactionAnnouncements_ExchangeRate` |  |  |  |
| 22 | `CORPORATEACTION.ANNOUNCEMENTS.RIGHT.QUANTITY.C1` | `FsGaCorporateactionAnnouncements_RightQuantityC1` | TField |  | Right Quantity C1 Multifonds DB Column is QTE_RIGHT_C1. |
| 23 | `CORPORATEACTION.ANNOUNCEMENTS.RIGHT.QUANTITY.C2` | `FsGaCorporateactionAnnouncements_RightQuantityC2` | TField |  | Right Quantity C2 Multifonds DB Column is QTE_RIGHT_C2. |
| 24 | `CORPORATEACTION.ANNOUNCEMENTS.OLD.SECURITIES` | `FsGaCorporateactionAnnouncements_OldSecurities` | TField |  | Old Securities Multifonds DB Column is TYPE_C2. |
| 25 | `CORPORATEACTION.ANNOUNCEMENTS.CORERCT.BOOK.VALUE.BY` | `FsGaCorporateactionAnnouncements_CorerctBookValueBy` | TField |  | Corerct Book Value By Multifonds DB Column is COD_AJUST. |
| 26 | `CORPORATEACTION.ANNOUNCEMENTS.BOOK.VALUE.ADJUSTMENT.TYPE` | `FsGaCorporateactionAnnouncements_BookValueAdjustmentType` | TField |  | Book Value Adjustment Type Multifonds DB Column is COD_AJUST_CPTA. |
| 27 | `CORPORATEACTION.ANNOUNCEMENTS.CORRECTION.UNIT.AMNT.LOCAL.CURRENCY` | `FsGaCorporateactionAnnouncements_CorrectionUnitAmntCurrency` | TField |  | Correction unit amnt currency Multifonds DB Column is CMON_AJUST. |
| 28 | `CORPORATEACTION.ANNOUNCEMENTS.CORRECTION.AMOUNT.UNIT` | `FsGaCorporateactionAnnouncements_CorrectionUnitAmount` | TField |  | Correction Unit amount Multifonds DB Column is MNT_UNIT_AJUST. |
| 29 | `CORPORATEACTION.ANNOUNCEMENTS.CORRECTION.RATIO` | `FsGaCorporateactionAnnouncements_CorrectionRatio` | TField |  | Correction Ratio Multifonds DB Column is PCT_RATIO. |
| 30 | `CORPORATEACTION.ANNOUNCEMENTS.CORRECTION.PERCENTAGE` | `FsGaCorporateactionAnnouncements_CorrectionPercentage` | TField |  | Correction percentage Multifonds DB Column is PCT_AJUST. |
| 31 | `CORPORATEACTION.ANNOUNCEMENTS.STATUS.PENDING` | `FsGaCorporateactionAnnouncements_StatusPending` | TField |  | Status Pending Multifonds DB Column is STATUS_PENDING. |
| 32 | `CORPORATEACTION.ANNOUNCEMENTS.ARCHIVE` | `FsGaCorporateactionAnnouncements_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 33 | `CORPORATEACTION.ANNOUNCEMENTS.DWH.EXPORT` | `FsGaCorporateactionAnnouncements_DwhExport` | TField |  | DWH Export Multifonds DB Column is DWH_EXPORT. |
| 34 | `CORPORATEACTION.ANNOUNCEMENTS.COST.RATE.OF.EXCHANGE` | `FsGaCorporateactionAnnouncements_CostExchangeRate` | TField |  | Cost Exchange rate Multifonds DB Column is COST_TCHG. |
| 35 | `CORPORATEACTION.ANNOUNCEMENTS.NEW.LOT.FLAG` | `FsGaCorporateactionAnnouncements_NewLotFlag` | TField |  | New Lot Flag Multifonds DB Column is FLG_NEW_LOT. |
| 36 | `CORPORATEACTION.ANNOUNCEMENTS.DOPER.FLAG` | `FsGaCorporateactionAnnouncements_DoperFlag` | TField |  | Doper Flag Multifonds DB Column is FLG_DOPER. |
| 37 | `CORPORATEACTION.ANNOUNCEMENTS.CA.EQUIVALENCE.CODE` | `FsGaCorporateactionAnnouncements_CaEquivalenceCode` | TField |  | CA Equivalence Code Multifonds DB Column is COPER_MARKET. |
| 38 | `CORPORATEACTION.ANNOUNCEMENTS.CORPORATE.ACTION.CODE` | `FsGaCorporateactionAnnouncements_CorporateActionCode` | TField |  | Corporate Action code Multifonds DB Column is CODE_CA. |
| 39 | `CORPORATEACTION.ANNOUNCEMENTS.NEW.CFD` | `FsGaCorporateactionAnnouncements_NewCfd` | TField |  | New CFD Multifonds DB Column is NFUT_C1. |
| 40 | `CORPORATEACTION.ANNOUNCEMENTS.RECEIVED.ON.OLD.SECURITY` | `FsGaCorporateactionAnnouncements_ReceivedOnOldSecurity` | TField |  | Received on old security Multifonds DB Column is RECD_ON_OLD_SECURITY. |
| 41 | `CORPORATEACTION.ANNOUNCEMENTS.DROP.FRACTIONAL.SHARES` | `FsGaCorporateactionAnnouncements_DropFractionalShares` | TField |  | Drop Fractional Shares Multifonds DB Column is FLG_DROP_FRC_SHRS. |
| 42 | `CORPORATEACTION.ANNOUNCEMENTS.SECURITY.RATIO` | `FsGaCorporateactionAnnouncements_SecurityRatio` | TField |  | Security Ratio Multifonds DB Column is SEC_RATIO. |
| 43 | `CORPORATEACTION.ANNOUNCEMENTS.DEFAULT.SECURITY` | `FsGaCorporateactionAnnouncements_DefaultSecurity` | TField |  | Default Security Multifonds DB Column is SEC_DEFAULT. |
| 44 | `CORPORATEACTION.ANNOUNCEMENTS.CASH.RATIO` | `FsGaCorporateactionAnnouncements_CashRatio` | TField |  | Cash Ratio Multifonds DB Column is CASH_RATIO. |
| 45 | `CORPORATEACTION.ANNOUNCEMENTS.DEFAULT.CASH` | `FsGaCorporateactionAnnouncements_DefaultCash` | TField |  | Default Cash Multifonds DB Column is CASH_DEFAULT. |
| 46 | `CORPORATEACTION.ANNOUNCEMENTS.GROSS.RATE.CASH` | `FsGaCorporateactionAnnouncements_GrossRateCash` | TField |  | Gross Rate Cash Multifonds DB Column is CASH_GROSS_RATE. |
| 47 | `CORPORATEACTION.ANNOUNCEMENTS.ACCEPT.FLAG` | `FsGaCorporateactionAnnouncements_AcceptFlag` | TField |  | Accept Flag Multifonds DB Column is FLG_ACCEPT. |
| 48 | `CORPORATEACTION.ANNOUNCEMENTS.REJECT.FLAG` | `FsGaCorporateactionAnnouncements_RejectFlag` | TField |  | Reject Flag Multifonds DB Column is FLG_REJECT. |
| 49 | `CORPORATEACTION.ANNOUNCEMENTS.PA.MODULE.FLAG` | `FsGaCorporateactionAnnouncements_PaModuleFlag` | TField |  | PA Module Flag Multifonds DB Column is FLG_PA_MODULE. |
| 50 | `CORPORATEACTION.ANNOUNCEMENTS.RECORD.DATE` | `FsGaCorporateactionAnnouncements_RecordDate` | TField |  | Record Date Multifonds DB Column is DRECORD. |
| 51 | `CORPORATEACTION.ANNOUNCEMENTS.ANNOUNCE.DATE` | `FsGaCorporateactionAnnouncements_AnnounceDate` | TField |  | Announce Date Multifonds DB Column is DANNOUNCE. |
| 52 | `CORPORATEACTION.ANNOUNCEMENTS.ACTION` | `FsGaCorporateactionAnnouncements_Action` | TField |  | Action Multifonds DB Column is ACTION. |
| 53 | `CORPORATEACTION.ANNOUNCEMENTS.PA.STATUS` | `FsGaCorporateactionAnnouncements_PaStatus` | TField |  | PA Status Multifonds DB Column is PA_CDSTATUS. |
| 54 | `CORPORATEACTION.ANNOUNCEMENTS.ID.CODE.SECURITY.1` | `FsGaCorporateactionAnnouncements_IdCodeSecurity1` | TField |  | ID Code Security 1 Multifonds DB Column is ID_CODE_SEC_C1. |
| 55 | `CORPORATEACTION.ANNOUNCEMENTS.PROVIDER.ID` | `FsGaCorporateactionAnnouncements_ProviderId` | TField |  | Provider ID Multifonds DB Column is SEC_ID. |
| 56 | `CORPORATEACTION.ANNOUNCEMENTS.SECURITY.ID.C1` | `FsGaCorporateactionAnnouncements_SecurityIdC1` | TField |  | Security ID C1 Multifonds DB Column is SEC_ID_C1. |
| 57 | `CORPORATEACTION.ANNOUNCEMENTS.ID.CODE.SECURITY` | `FsGaCorporateactionAnnouncements_IdCodeSecurity` | TField |  | ID Code Security Multifonds DB Column is ID_CODE_SEC. |
| 58 | `CORPORATEACTION.ANNOUNCEMENTS.MIGRATE.FLAG` | `FsGaCorporateactionAnnouncements_MigrateFlag` | TField |  | Migrate Flag Multifonds DB Column is FLG_MIGRATE. |
| 59 | `CORPORATEACTION.ANNOUNCEMENTS.SECURITY.LINK` | `FsGaCorporateactionAnnouncements_SecurityLink` | TField |  | Security Link Multifonds DB Column is NOVAL_LINK. |
| 60 | `CORPORATEACTION.ANNOUNCEMENTS.OPERATION.CODE.LINK` | `FsGaCorporateactionAnnouncements_OperationCodeLink` | TField |  | Operation Code link Multifonds DB Column is COPER_LINK. |
| 61 | `CORPORATEACTION.ANNOUNCEMENTS.SEQUENCE.LINK` | `FsGaCorporateactionAnnouncements_SequenceLink` | TField |  | Sequence link Multifonds DB Column is NSEQ_LINK. |
| 62 | `CORPORATEACTION.ANNOUNCEMENTS.SUB.SEQUENCE.LINK` | `FsGaCorporateactionAnnouncements_SubSequenceLink` | TField |  | Sub sequence link Multifonds DB Column is NSUB_SEQ_LINK. |
| 63 | `CORPORATEACTION.ANNOUNCEMENTS.VOLUNTARY.FLAG` | `FsGaCorporateactionAnnouncements_VoluntaryFlag` | TField |  | Voluntary Flag Multifonds DB Column is FLG_VOLUNTARY. |
| 64 | `CORPORATEACTION.ANNOUNCEMENTS.PAYMENT.DATE` | `FsGaCorporateactionAnnouncements_PaymentDate` | TField |  | Payment Date Multifonds DB Column is DPAYMNT. |
| 65 | `CORPORATEACTION.ANNOUNCEMENTS.CUSTODIAN.DEADLINE` | `FsGaCorporateactionAnnouncements_CustodianDeadline` | TField |  | Custodian Deadline Multifonds DB Column is DCUST_DEADLINE. |
| 66 | `CORPORATEACTION.ANNOUNCEMENTS.CLIEND.RESPOND.DEADLINE` | `FsGaCorporateactionAnnouncements_CliendRespondDeadline` | TField |  | Cliend Respond Deadline Multifonds DB Column is DCLIENT_RESPOND. |
| 67 | `CORPORATEACTION.ANNOUNCEMENTS.CLIENT.RESPONSE.RECEIPT.DATE` | `FsGaCorporateactionAnnouncements_ClientResponseReceiptDate` | TField |  | Client Response Receipt Date Multifonds DB Column is DCLIENT_RES_RECEIPT. |
| 68 | `CORPORATEACTION.ANNOUNCEMENTS.CUSTODIAN.STATUS.RECEIPT.DATE` | `FsGaCorporateactionAnnouncements_CustodianStatusReceiptDate` | TField |  | Custodian status receipt date Multifonds DB Column is DCUST_STAT_RECEIPT. |
| 69 | `CORPORATEACTION.ANNOUNCEMENTS.PARTIAL.CA` | `FsGaCorporateactionAnnouncements_PartialCa` | TField |  | Partial CA Multifonds DB Column is FLG_PARTIAL_CA. |
| 70 | `CORPORATEACTION.ANNOUNCEMENTS.VOLUNTARY.CA` | `FsGaCorporateactionAnnouncements_VoluntaryCa` | TField |  | Voluntary CA Multifonds DB Column is FLG_VOL_CA. |
| 71 | `CORPORATEACTION.ANNOUNCEMENTS.COST.ADJUSTMENT.FLAG` | `FsGaCorporateactionAnnouncements_CostAdjustmentFlag` | TField |  | Cost Adjustment Flag Multifonds DB Column is FLG_ROC_CA_TCHG. |
| 72 | `CORPORATEACTION.ANNOUNCEMENTS.SHARE.AVAILABLE.DATE` | `FsGaCorporateactionAnnouncements_ShareAvailableDate` | TField |  | Share Available date Multifonds DB Column is SHARE_AVAIL_DATE. |
| 73 | `CORPORATEACTION.ANNOUNCEMENTS.CA.TYPE` | `FsGaCorporateactionAnnouncements_CaType` | TField |  | CA Type Multifonds DB Column is CA_TYPE. |
| 74 | `CORPORATEACTION.ANNOUNCEMENTS.RECORD.STATUS` | `FsGaCorporateactionAnnouncements_RecordStatus` | String |  |  |
| 75 | `CORPORATEACTION.ANNOUNCEMENTS.CURR.NO` | `FsGaCorporateactionAnnouncements_CurrNo` | String |  |  |
| 76 | `CORPORATEACTION.ANNOUNCEMENTS.INPUTTER` | `FsGaCorporateactionAnnouncements_Inputter` |  |  |  |
| 77 | `CORPORATEACTION.ANNOUNCEMENTS.DATE.TIME` | `FsGaCorporateactionAnnouncements_DateTime` |  |  |  |
| 78 | `CORPORATEACTION.ANNOUNCEMENTS.AUTHORISER` | `FsGaCorporateactionAnnouncements_Authoriser` | String |  |  |
| 79 | `CORPORATEACTION.ANNOUNCEMENTS.CO.CODE` | `FsGaCorporateactionAnnouncements_CoCode` | String |  |  |
| 80 | `CORPORATEACTION.ANNOUNCEMENTS.DEPT.CODE` | `FsGaCorporateactionAnnouncements_DeptCode` | String |  |  |
| 81 | `CORPORATEACTION.ANNOUNCEMENTS.AUDITOR.CODE` | `FsGaCorporateactionAnnouncements_AuditorCode` | String |  |  |
| 82 | `CORPORATEACTION.ANNOUNCEMENTS.AUDIT.DATE.TIME` | `FsGaCorporateactionAnnouncements_AuditDateTime` | String |  |  |
