# FS.GA.BLENDED.PAYMENT.BY.FUND — Table Schema

> Source: `INSERTS/I_F.FS.GA.BLENDED.PAYMENT.BY.FUND` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.BLENDED.PAYMENT.BY.FUND.PARENT.REF.ID` | `FsGaBlendedPaymentByFund_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.BLENDED.PAYMENT.BY.FUND.ORA.ROWID` | `FsGaBlendedPaymentByFund_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.BLENDED.PAYMENT.BY.FUND.FUND.ID` | `FsGaBlendedPaymentByFund_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.BLENDED.PAYMENT.BY.FUND.INTERNAL.SECURITY.ID` | `FsGaBlendedPaymentByFund_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.BLENDED.PAYMENT.BY.FUND.CORRESPONDENT` | `FsGaBlendedPaymentByFund_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 6 | `FS.GA.BLENDED.PAYMENT.BY.FUND.TRANSACTION.SERVICE.CODE` | `FsGaBlendedPaymentByFund_TransactionServiceCode` | TField |  | This is the transaction type. Multifonds DB Column is CSERV. |
| 7 | `FS.GA.BLENDED.PAYMENT.BY.FUND.LOT.NUMBER` | `FsGaBlendedPaymentByFund_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 8 | `FS.GA.BLENDED.PAYMENT.BY.FUND.MANAGER.CODE` | `FsGaBlendedPaymentByFund_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 9 | `FS.GA.BLENDED.PAYMENT.BY.FUND.FROM.DT` | `FsGaBlendedPaymentByFund_FromDt` | TField |  | From Date Multifonds DB Column is DDEBUT. |
| 10 | `FS.GA.BLENDED.PAYMENT.BY.FUND.TO.DATE` | `FsGaBlendedPaymentByFund_ToDate` | TField |  | To Date Multifonds DB Column is DFIN. |
| 11 | `FS.GA.BLENDED.PAYMENT.BY.FUND.BLENDED.PAYMENT.AMOUNT` | `FsGaBlendedPaymentByFund_BlendedPaymentAmount` | TField |  | Blended payment amount Multifonds DB Column is MNT_BP. |
| 12 | `FS.GA.BLENDED.PAYMENT.BY.FUND.INTEREST.ONLY.PERIOD` | `FsGaBlendedPaymentByFund_InterestOnlyPeriod` | TField |  | Interest only period Identifier Multifonds DB Column is FLG_IOP. |
| 13 | `FS.GA.BLENDED.PAYMENT.BY.FUND.BP.CURRENCY` | `FsGaBlendedPaymentByFund_BpCurrency` | TField |  | BP Currency Multifonds DB Column is CMON_BP. |
| 14 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RESERVED10` | `FsGaBlendedPaymentByFund_Reserved10` | TField |  |  |
| 15 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RESERVED9` | `FsGaBlendedPaymentByFund_Reserved9` | TField |  |  |
| 16 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RESERVED8` | `FsGaBlendedPaymentByFund_Reserved8` | TField |  |  |
| 17 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RESERVED7` | `FsGaBlendedPaymentByFund_Reserved7` | TField |  |  |
| 18 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RESERVED6` | `FsGaBlendedPaymentByFund_Reserved6` | TField |  |  |
| 19 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RESERVED5` | `FsGaBlendedPaymentByFund_Reserved5` | TField |  |  |
| 20 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RESERVED4` | `FsGaBlendedPaymentByFund_Reserved4` | TField |  |  |
| 21 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RESERVED3` | `FsGaBlendedPaymentByFund_Reserved3` | TField |  |  |
| 22 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RESERVED2` | `FsGaBlendedPaymentByFund_Reserved2` | TField |  |  |
| 23 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RESERVED1` | `FsGaBlendedPaymentByFund_Reserved1` | TField |  |  |
| 24 | `FS.GA.BLENDED.PAYMENT.BY.FUND.LOCAL.REF` | `FsGaBlendedPaymentByFund_LocalRef` |  |  |  |
| 25 | `FS.GA.BLENDED.PAYMENT.BY.FUND.OVERRIDE` | `FsGaBlendedPaymentByFund_Override` |  |  |  |
| 26 | `FS.GA.BLENDED.PAYMENT.BY.FUND.RECORD.STATUS` | `FsGaBlendedPaymentByFund_RecordStatus` | String |  |  |
| 27 | `FS.GA.BLENDED.PAYMENT.BY.FUND.CURR.NO` | `FsGaBlendedPaymentByFund_CurrNo` | String |  |  |
| 28 | `FS.GA.BLENDED.PAYMENT.BY.FUND.INPUTTER` | `FsGaBlendedPaymentByFund_Inputter` |  |  |  |
| 29 | `FS.GA.BLENDED.PAYMENT.BY.FUND.DATE.TIME` | `FsGaBlendedPaymentByFund_DateTime` |  |  |  |
| 30 | `FS.GA.BLENDED.PAYMENT.BY.FUND.AUTHORISER` | `FsGaBlendedPaymentByFund_Authoriser` | String |  |  |
| 31 | `FS.GA.BLENDED.PAYMENT.BY.FUND.CO.CODE` | `FsGaBlendedPaymentByFund_CoCode` | String |  |  |
| 32 | `FS.GA.BLENDED.PAYMENT.BY.FUND.DEPT.CODE` | `FsGaBlendedPaymentByFund_DeptCode` | String |  |  |
| 33 | `FS.GA.BLENDED.PAYMENT.BY.FUND.AUDITOR.CODE` | `FsGaBlendedPaymentByFund_AuditorCode` | String |  |  |
| 34 | `FS.GA.BLENDED.PAYMENT.BY.FUND.AUDIT.DATE.TIME` | `FsGaBlendedPaymentByFund_AuditDateTime` | String |  |  |
