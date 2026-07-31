# FS.GI.FUND.TRANSACTION.RESTRICTION — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.TRANSACTION.RESTRICTION` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.TRANSACTION.RESTRICTION.PARENT.REF.ID` | `FsGiFundTransactionRestriction_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.TRANSACTION.RESTRICTION.ORA.ROWID` | `FsGiFundTransactionRestriction_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.TRANSACTION.RESTRICTION.TA.FUND.ID` | `FsGiFundTransactionRestriction_TaFundId` | TField |  | Fund for which the transaction restriction is applicable. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.TRANSACTION.RESTRICTION.OPERATION.CODE` | `FsGiFundTransactionRestriction_OperationCode` | TField |  | Operation code for which the transaction restriction check is applicable. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.FUND.TRANSACTION.RESTRICTION.NO.AMOUNT.FLAG` | `FsGiFundTransactionRestriction_NoAmountFlag` | TField |  | Flag allows to block amount transactions for the fund. Multifonds DB Column is FLG_NO_AMT. |
| 6 | `FS.GI.FUND.TRANSACTION.RESTRICTION.NO.QUANTITY.FLAG` | `FsGiFundTransactionRestriction_NoQuantityFlag` | TField |  | Flag allows to block quantity transactions for the fund. Multifonds DB Column is FLG_NO_QTY. |
| 7 | `FS.GI.FUND.TRANSACTION.RESTRICTION.INTERNAL.ID` | `FsGiFundTransactionRestriction_InternalId` | TField |  | Unique internal identifier of the fund transaction restriction record. Multifonds DB Column is INTERNAL_ID. |
| 8 | `FS.GI.FUND.TRANSACTION.RESTRICTION.FUND.ID` | `FsGiFundTransactionRestriction_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.FUND.TRANSACTION.RESTRICTION.CLASS.CURRENCY` | `FsGiFundTransactionRestriction_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RESERVED10` | `FsGiFundTransactionRestriction_Reserved10` | TField |  |  |
| 11 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RESERVED9` | `FsGiFundTransactionRestriction_Reserved9` | TField |  |  |
| 12 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RESERVED8` | `FsGiFundTransactionRestriction_Reserved8` | TField |  |  |
| 13 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RESERVED7` | `FsGiFundTransactionRestriction_Reserved7` | TField |  |  |
| 14 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RESERVED6` | `FsGiFundTransactionRestriction_Reserved6` | TField |  |  |
| 15 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RESERVED5` | `FsGiFundTransactionRestriction_Reserved5` | TField |  |  |
| 16 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RESERVED4` | `FsGiFundTransactionRestriction_Reserved4` | TField |  |  |
| 17 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RESERVED3` | `FsGiFundTransactionRestriction_Reserved3` | TField |  |  |
| 18 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RESERVED2` | `FsGiFundTransactionRestriction_Reserved2` | TField |  |  |
| 19 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RESERVED1` | `FsGiFundTransactionRestriction_Reserved1` | TField |  |  |
| 20 | `FS.GI.FUND.TRANSACTION.RESTRICTION.LOCAL.REF` | `FsGiFundTransactionRestriction_LocalRef` |  |  |  |
| 21 | `FS.GI.FUND.TRANSACTION.RESTRICTION.OVERRIDE` | `FsGiFundTransactionRestriction_Override` |  |  |  |
| 22 | `FS.GI.FUND.TRANSACTION.RESTRICTION.RECORD.STATUS` | `FsGiFundTransactionRestriction_RecordStatus` | String |  |  |
| 23 | `FS.GI.FUND.TRANSACTION.RESTRICTION.CURR.NO` | `FsGiFundTransactionRestriction_CurrNo` | String |  |  |
| 24 | `FS.GI.FUND.TRANSACTION.RESTRICTION.INPUTTER` | `FsGiFundTransactionRestriction_Inputter` |  |  |  |
| 25 | `FS.GI.FUND.TRANSACTION.RESTRICTION.DATE.TIME` | `FsGiFundTransactionRestriction_DateTime` |  |  |  |
| 26 | `FS.GI.FUND.TRANSACTION.RESTRICTION.AUTHORISER` | `FsGiFundTransactionRestriction_Authoriser` | String |  |  |
| 27 | `FS.GI.FUND.TRANSACTION.RESTRICTION.CO.CODE` | `FsGiFundTransactionRestriction_CoCode` | String |  |  |
| 28 | `FS.GI.FUND.TRANSACTION.RESTRICTION.DEPT.CODE` | `FsGiFundTransactionRestriction_DeptCode` | String |  |  |
| 29 | `FS.GI.FUND.TRANSACTION.RESTRICTION.AUDITOR.CODE` | `FsGiFundTransactionRestriction_AuditorCode` | String |  |  |
| 30 | `FS.GI.FUND.TRANSACTION.RESTRICTION.AUDIT.DATE.TIME` | `FsGiFundTransactionRestriction_AuditDateTime` | String |  |  |
