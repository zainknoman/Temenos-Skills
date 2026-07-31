# FS.GI.FUND.TRANSACTION.LIMIT — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.TRANSACTION.LIMIT` in `FS_FundStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.TRANSACTION.LIMIT.PARENT.REF.ID` | `FsGiFundTransactionLimit_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.TRANSACTION.LIMIT.ORA.ROWID` | `FsGiFundTransactionLimit_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.TRANSACTION.LIMIT.TA.FUND.ID` | `FsGiFundTransactionLimit_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.TRANSACTION.LIMIT.OPERATION.CODE` | `FsGiFundTransactionLimit_OperationCode` | TField |  | Operation code for which transaction limit applies. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.FUND.TRANSACTION.LIMIT.SHARE.CLASS.CODE` | `FsGiFundTransactionLimit_ShareClassCode` | TField |  | Fund Share class code. Multifonds DB Column is TPART. |
| 6 | `FS.GI.FUND.TRANSACTION.LIMIT.PAYMENT.CURRENCY` | `FsGiFundTransactionLimit_PaymentCurrency` | TField |  | Fund limit currency (in 3 letter ISO format eg. &apos;USD&apos;). Multifonds DB Column is CMON. |
| 7 | `FS.GI.FUND.TRANSACTION.LIMIT.MINIMUM.LIMIT` | `FsGiFundTransactionLimit_MinimumLimit` | TField |  | Minimum transaction limit check that will be performed at order level for a fund share class. Multifonds DB Column is NMIN_LIMIT. |
| 8 | `FS.GI.FUND.TRANSACTION.LIMIT.MAXIMUM.LIMIT` | `FsGiFundTransactionLimit_MaximumLimit` | TField |  | Maximum transaction limit check that will be performed at order level for a fund share class. Multifonds DB Column is NMAX_LIMIT. |
| 9 | `FS.GI.FUND.TRANSACTION.LIMIT.MINIMUM.BATCH.LIMIT` | `FsGiFundTransactionLimit_MinimumBatchLimit` | TField |  | Minimum transaction limit check that will be performed at batch process level for a fund share class. Multifonds DB Column is NBATCH_LIMIT. |
| 10 | `FS.GI.FUND.TRANSACTION.LIMIT.FIRST.SUBSCRIPTION.FLAG` | `FsGiFundTransactionLimit_FirstSubscriptionFlag` | TField |  | Its an internal technical flag to indicate the transaction limits defined for the fund share class first subscription functionality. Multifonds DB Column is FLG_FIRST_SUB. |
| 11 | `FS.GI.FUND.TRANSACTION.LIMIT.FIRST.TRANSACTION.FLAG` | `FsGiFundTransactionLimit_FirstTransactionFlag` | TField |  | Its an internal technical flag to indicate the transaction limits defined for the fund share class first transaction limit functionality. Multifonds DB Column is FLG_FIRST_TRANS. |
| 12 | `FS.GI.FUND.TRANSACTION.LIMIT.INTERNAL.ID` | `FsGiFundTransactionLimit_InternalId` | TField |  | Unique internal identifier supplied as a reference to external processes creating new details in the table. Multifonds DB Column is INTERNAL_ID. |
| 13 | `FS.GI.FUND.TRANSACTION.LIMIT.FUND.ID` | `FsGiFundTransactionLimit_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 14 | `FS.GI.FUND.TRANSACTION.LIMIT.CLASS.CURRENCY` | `FsGiFundTransactionLimit_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 15 | `FS.GI.FUND.TRANSACTION.LIMIT.RESERVED10` | `FsGiFundTransactionLimit_Reserved10` | TField |  |  |
| 16 | `FS.GI.FUND.TRANSACTION.LIMIT.RESERVED9` | `FsGiFundTransactionLimit_Reserved9` | TField |  |  |
| 17 | `FS.GI.FUND.TRANSACTION.LIMIT.RESERVED8` | `FsGiFundTransactionLimit_Reserved8` | TField |  |  |
| 18 | `FS.GI.FUND.TRANSACTION.LIMIT.RESERVED7` | `FsGiFundTransactionLimit_Reserved7` | TField |  |  |
| 19 | `FS.GI.FUND.TRANSACTION.LIMIT.RESERVED6` | `FsGiFundTransactionLimit_Reserved6` | TField |  |  |
| 20 | `FS.GI.FUND.TRANSACTION.LIMIT.RESERVED5` | `FsGiFundTransactionLimit_Reserved5` | TField |  |  |
| 21 | `FS.GI.FUND.TRANSACTION.LIMIT.RESERVED4` | `FsGiFundTransactionLimit_Reserved4` | TField |  |  |
| 22 | `FS.GI.FUND.TRANSACTION.LIMIT.RESERVED3` | `FsGiFundTransactionLimit_Reserved3` | TField |  |  |
| 23 | `FS.GI.FUND.TRANSACTION.LIMIT.RESERVED2` | `FsGiFundTransactionLimit_Reserved2` | TField |  |  |
| 24 | `FS.GI.FUND.TRANSACTION.LIMIT.RESERVED1` | `FsGiFundTransactionLimit_Reserved1` | TField |  |  |
| 25 | `FS.GI.FUND.TRANSACTION.LIMIT.LOCAL.REF` | `FsGiFundTransactionLimit_LocalRef` |  |  |  |
| 26 | `FS.GI.FUND.TRANSACTION.LIMIT.OVERRIDE` | `FsGiFundTransactionLimit_Override` |  |  |  |
| 27 | `FS.GI.FUND.TRANSACTION.LIMIT.RECORD.STATUS` | `FsGiFundTransactionLimit_RecordStatus` | String |  |  |
| 28 | `FS.GI.FUND.TRANSACTION.LIMIT.CURR.NO` | `FsGiFundTransactionLimit_CurrNo` | String |  |  |
| 29 | `FS.GI.FUND.TRANSACTION.LIMIT.INPUTTER` | `FsGiFundTransactionLimit_Inputter` |  |  |  |
| 30 | `FS.GI.FUND.TRANSACTION.LIMIT.DATE.TIME` | `FsGiFundTransactionLimit_DateTime` |  |  |  |
| 31 | `FS.GI.FUND.TRANSACTION.LIMIT.AUTHORISER` | `FsGiFundTransactionLimit_Authoriser` | String |  |  |
| 32 | `FS.GI.FUND.TRANSACTION.LIMIT.CO.CODE` | `FsGiFundTransactionLimit_CoCode` | String |  |  |
| 33 | `FS.GI.FUND.TRANSACTION.LIMIT.DEPT.CODE` | `FsGiFundTransactionLimit_DeptCode` | String |  |  |
| 34 | `FS.GI.FUND.TRANSACTION.LIMIT.AUDITOR.CODE` | `FsGiFundTransactionLimit_AuditorCode` | String |  |  |
| 35 | `FS.GI.FUND.TRANSACTION.LIMIT.AUDIT.DATE.TIME` | `FsGiFundTransactionLimit_AuditDateTime` | String |  |  |
