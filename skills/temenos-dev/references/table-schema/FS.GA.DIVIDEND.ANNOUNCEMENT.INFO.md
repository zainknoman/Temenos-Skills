# FS.GA.DIVIDEND.ANNOUNCEMENT.INFO — Table Schema

> Source: `INSERTS/I_F.FS.GA.DIVIDEND.ANNOUNCEMENT.INFO` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DIVIDEND.ANNOUNCEMENT.INFO.SECURITY` | `FsGaDividendAnnouncementInfo_Security` | TField |  | Security Multifonds DB Column is NOVAL. |
| 2 | `DIVIDEND.ANNOUNCEMENT.INFO.EXECUTION.DATE` | `FsGaDividendAnnouncementInfo_ExecutionDate` | TField |  | Execution date Multifonds DB Column is DATE_EX. |
| 3 | `DIVIDEND.ANNOUNCEMENT.INFO.AMOUNT.UNIT` | `FsGaDividendAnnouncementInfo_UnitAmount` |  |  |  |
| 4 | `DIVIDEND.ANNOUNCEMENT.INFO.PAYMENT.DATE` | `FsGaDividendAnnouncementInfo_PaymentDate` | TField |  | Payment date Multifonds DB Column is DPAYMNT. |
| 5 | `DIVIDEND.ANNOUNCEMENT.INFO.VALUE.DATE` | `FsGaDividendAnnouncementInfo_ValueDate` | TField |  | Value Date Multifonds DB Column is DVALEUR. |
| 6 | `DIVIDEND.ANNOUNCEMENT.INFO.DIVIDEND.ANNOUNCEMENT.LOCAL.CURRENCY` | `FsGaDividendAnnouncementInfo_DividendAnnouncementCurrency` | TField |  | Dividend announcement Currency Multifonds DB Column is CMON. |
| 7 | `DIVIDEND.ANNOUNCEMENT.INFO.PERCENTAGE.OF.RECOVERABLE.TAX` | `FsGaDividendAnnouncementInfo_PercentageOfRecoverableTax` | TField |  | Percentage of recoverable tax Multifonds DB Column is PCT_RC. |
| 8 | `DIVIDEND.ANNOUNCEMENT.INFO.PERCENTAGE.UNRECOVERABLE.TAX` | `FsGaDividendAnnouncementInfo_PercentageUnrecoverableTax` | TField |  | Percentage unrecoverable tax Multifonds DB Column is PCT_UN. |
| 9 | `DIVIDEND.ANNOUNCEMENT.INFO.PERCENTAGE.RECOVERABLE.TAX.2` | `FsGaDividendAnnouncementInfo_PercentageRecoverableTax2` | TField |  | Percentage recoverable tax 2 Multifonds DB Column is PCT_RC_2. |
| 10 | `DIVIDEND.ANNOUNCEMENT.INFO.PERCENTAGE.UNRECOVERABLE.TAX.2` | `FsGaDividendAnnouncementInfo_PercentageUnrecoverableTax2` | TField |  | Percentage unrecoverable tax 2 Multifonds DB Column is PCT_UN_2. |
| 11 | `DIVIDEND.ANNOUNCEMENT.INFO.NET.AMOUNT.FLAG` | `FsGaDividendAnnouncementInfo_NetAmountFlag` | TField |  | Net amount FLAG Multifonds DB Column is FLAG_BRUT. |
| 12 | `DIVIDEND.ANNOUNCEMENT.INFO.TRANSACTION.CODE` | `FsGaDividendAnnouncementInfo_OperationCode` |  |  |  |
| 13 | `DIVIDEND.ANNOUNCEMENT.INFO.RECOVERABLE.TAX.AMOUNT` | `FsGaDividendAnnouncementInfo_RecoverableTaxAmount` | TField |  | Recoverable tax amount Multifonds DB Column is RECOVERABLE. |
| 14 | `DIVIDEND.ANNOUNCEMENT.INFO.RECOVERABLE.TAX.1.AMOUNT` | `FsGaDividendAnnouncementInfo_RecoverableTax1Amount` | TField |  | Recoverable tax 1 amount Multifonds DB Column is RECOVERABLE_1. |
| 15 | `DIVIDEND.ANNOUNCEMENT.INFO.EXTERNAL.REFERENCE` | `FsGaDividendAnnouncementInfo_ExternalReference` | TField |  | External reference Multifonds DB Column is EXT_REF. |
| 16 | `DIVIDEND.ANNOUNCEMENT.INFO.TAX.RULE` | `FsGaDividendAnnouncementInfo_TaxRule` | TField |  | Tax RULE Multifonds DB Column is TAX_REG. |
| 17 | `DIVIDEND.ANNOUNCEMENT.INFO.ANNOUNCEMENT.DESCRIPTION` | `FsGaDividendAnnouncementInfo_AnnouncementDescription` | TField |  | Announcement description Multifonds DB Column is TXT_OST. |
| 18 | `DIVIDEND.ANNOUNCEMENT.INFO.DWH.EXPORT` | `FsGaDividendAnnouncementInfo_DwhExport` | TField |  | DWH EXPORT Multifonds DB Column is DWH_EXPORT. |
| 19 | `DIVIDEND.ANNOUNCEMENT.INFO.PAYABLE.TAX.PERCENTAGE` | `FsGaDividendAnnouncementInfo_PayableTaxPercentage` | TField |  | Payable Tax Percentage Multifonds DB Column is PCT_TAX_1. |
| 20 | `DIVIDEND.ANNOUNCEMENT.INFO.PAYABLE.TAX.PERCENTAGE.2` | `FsGaDividendAnnouncementInfo_PayableTaxPercentage2` | TField |  | Payable Tax Percentage 2 Multifonds DB Column is PCT_TAX_2. |
| 21 | `DIVIDEND.ANNOUNCEMENT.INFO.ENTITLEMENT.DATE` | `FsGaDividendAnnouncementInfo_EntitlementDate` | TField |  | Entitlement date Multifonds DB Column is DENTITLE. |
| 22 | `DIVIDEND.ANNOUNCEMENT.INFO.STATUS.CODE` | `FsGaDividendAnnouncementInfo_StatusCode` | TField |  | Status Code Multifonds DB Column is CSTATUS. |
| 23 | `DIVIDEND.ANNOUNCEMENT.INFO.STRIP` | `FsGaDividendAnnouncementInfo_Strip` | TField |  | Strip Multifonds DB Column is NOVAL_LINK. |
| 24 | `DIVIDEND.ANNOUNCEMENT.INFO.FEE` | `FsGaDividendAnnouncementInfo_Fee` | TField |  | Fee Multifonds DB Column is MFRAIS1. |
| 25 | `DIVIDEND.ANNOUNCEMENT.INFO.FEE.2` | `FsGaDividendAnnouncementInfo_Fee2` | TField |  | Fee 2 Multifonds DB Column is MFRAIS2. |
| 26 | `DIVIDEND.ANNOUNCEMENT.INFO.FRANKED.INCOME` | `FsGaDividendAnnouncementInfo_FrankedIncome` | TField |  | Franked Income Multifonds DB Column is FRANK_INC. |
| 27 | `DIVIDEND.ANNOUNCEMENT.INFO.RECORD.DATE` | `FsGaDividendAnnouncementInfo_RecordDate` | TField |  | Record Date Multifonds DB Column is DRECORD. |
| 28 | `DIVIDEND.ANNOUNCEMENT.INFO.ISSUE.COUNTRY` | `FsGaDividendAnnouncementInfo_CountryCode` |  |  |  |
| 29 | `DIVIDEND.ANNOUNCEMENT.INFO.SEQUENCE.NUMBER` | `FsGaDividendAnnouncementInfo_SequenceNumber` | TField |  | Sequence Number Multifonds DB Column is NO_SEQ. |
| 30 | `DIVIDEND.ANNOUNCEMENT.INFO.ANNOUNCEMENT.LONG.DESC` | `FsGaDividendAnnouncementInfo_AnnouncementLongDescription` | TField |  | Announcement long description Multifonds DB Column is XLIBELLE_NEW. |
| 31 | `DIVIDEND.ANNOUNCEMENT.INFO.CA.TRANSACTION.CODE` | `FsGaDividendAnnouncementInfo_CaOperationCode` | TField |  | CA Operation code Multifonds DB Column is COPER_CA. |
| 32 | `DIVIDEND.ANNOUNCEMENT.INFO.NSEQUENCE` | `FsGaDividendAnnouncementInfo_Nsequence` | TField |  | NSequence Multifonds DB Column is NSEQ. |
| 33 | `DIVIDEND.ANNOUNCEMENT.INFO.SUBSEQUENCE.NUMBER` | `FsGaDividendAnnouncementInfo_SubsequenceNumber` | TField |  | Subsequence Number Multifonds DB Column is NSUB_SEQ. |
| 34 | `DIVIDEND.ANNOUNCEMENT.INFO.FLG.PA.MODULE` | `FsGaDividendAnnouncementInfo_FlgPaModule` | TField |  | FLG PA MODULE Multifonds DB Column is FLG_PA_MODULE. |
| 35 | `DIVIDEND.ANNOUNCEMENT.INFO.ANNOUNCE.DATE` | `FsGaDividendAnnouncementInfo_AnnounceDate` | TField |  | ANNOUNCE Date Multifonds DB Column is DANNOUNCE. |
| 36 | `DIVIDEND.ANNOUNCEMENT.INFO.ACTION` | `FsGaDividendAnnouncementInfo_Action` | TField |  | ACTION Multifonds DB Column is ACTION. |
| 37 | `DIVIDEND.ANNOUNCEMENT.INFO.PA.CDSTATUS` | `FsGaDividendAnnouncementInfo_PaCdstatus` | TField |  | PA CDSTATUS Multifonds DB Column is PA_CDSTATUS. |
| 38 | `DIVIDEND.ANNOUNCEMENT.INFO.INTERNAL.SECURITY.ID` | `FsGaDividendAnnouncementInfo_SecurityId` |  |  |  |
| 39 | `DIVIDEND.ANNOUNCEMENT.INFO.ID.CODE.SEC` | `FsGaDividendAnnouncementInfo_IdCodeSec` | TField |  | ID CODE SEC Multifonds DB Column is ID_CODE_SEC. |
| 40 | `DIVIDEND.ANNOUNCEMENT.INFO.DIVIDEND.REINVESTMENT.DATE` | `FsGaDividendAnnouncementInfo_DividendReinvestmentDate` | TField |  | Dividend Reinvestment Date Multifonds DB Column is DREINV. |
| 41 | `DIVIDEND.ANNOUNCEMENT.INFO.REINVESTMENT.TRANSACTION.PRICE` | `FsGaDividendAnnouncementInfo_ReinvestmentPrice` | TField |  | Reinvestment price Multifonds DB Column is COURS_REINV. |
| 42 | `DIVIDEND.ANNOUNCEMENT.INFO.CONDUIT.FORIEN.INCOME` | `FsGaDividendAnnouncementInfo_ConduitForienIncome` | TField |  | Conduit Forien Income Multifonds DB Column is CFI_RATE. |
| 43 | `DIVIDEND.ANNOUNCEMENT.INFO.CORPORATE.ACTION.TYPE` | `FsGaDividendAnnouncementInfo_CorporateActionType` | TField |  | Corporate Action TYPE Multifonds DB Column is CA_TYPE. |
| 44 | `DIVIDEND.ANNOUNCEMENT.INFO.RECORD.STATUS` | `FsGaDividendAnnouncementInfo_RecordStatus` | String |  |  |
| 45 | `DIVIDEND.ANNOUNCEMENT.INFO.CURR.NO` | `FsGaDividendAnnouncementInfo_CurrNo` | String |  |  |
| 46 | `DIVIDEND.ANNOUNCEMENT.INFO.INPUTTER` | `FsGaDividendAnnouncementInfo_Inputter` |  |  |  |
| 47 | `DIVIDEND.ANNOUNCEMENT.INFO.DATE.TIME` | `FsGaDividendAnnouncementInfo_DateTime` |  |  |  |
| 48 | `DIVIDEND.ANNOUNCEMENT.INFO.AUTHORISER` | `FsGaDividendAnnouncementInfo_Authoriser` | String |  |  |
| 49 | `DIVIDEND.ANNOUNCEMENT.INFO.CO.CODE` | `FsGaDividendAnnouncementInfo_CoCode` | String |  |  |
| 50 | `DIVIDEND.ANNOUNCEMENT.INFO.DEPT.CODE` | `FsGaDividendAnnouncementInfo_DeptCode` | String |  |  |
| 51 | `DIVIDEND.ANNOUNCEMENT.INFO.AUDITOR.CODE` | `FsGaDividendAnnouncementInfo_AuditorCode` | String |  |  |
| 52 | `DIVIDEND.ANNOUNCEMENT.INFO.AUDIT.DATE.TIME` | `FsGaDividendAnnouncementInfo_AuditDateTime` | String |  |  |
