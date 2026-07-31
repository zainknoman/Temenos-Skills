# FS.GA.FEE.CODE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GA.FEE.CODE.DEFINITION` in `FS_AccountingSchema.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FEE.CODE.DEFINITION.PARENT.REF.ID` | `FsGaFeeCodeDefinition_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FEE.CODE.DEFINITION.ORA.ROWID` | `FsGaFeeCodeDefinition_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FEE.CODE.DEFINITION.CHART.OF.ACCOUNTS.CODE` | `FsGaFeeCodeDefinition_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.FEE.CODE.DEFINITION.TRANSACTION.FEES.CODE` | `FsGaFeeCodeDefinition_TransactionFeesCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CFRAIS. |
| 5 | `FS.GA.FEE.CODE.DEFINITION.GTI.CODE` | `FsGaFeeCodeDefinition_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 6 | `FS.GA.FEE.CODE.DEFINITION.DEBIT.ACCOUNT.NUMBER` | `FsGaFeeCodeDefinition_DebitAccountNumber` | TField |  | Debit account number tagged to a fee code Multifonds DB Column is NRUBRDB. |
| 7 | `FS.GA.FEE.CODE.DEFINITION.DEBIT.ACCOUNT.SUFFIX.NUMBER` | `FsGaFeeCodeDefinition_DebitAccountSuffixNumber` | TField |  | Debit account suffix number tagged to a fee code Multifonds DB Column is NSUFFDB. |
| 8 | `FS.GA.FEE.CODE.DEFINITION.CREDIT.ACCOUNT.NUMBER` | `FsGaFeeCodeDefinition_CreditAccountNumber` | TField |  | Credit account number tagged to a fee code Multifonds DB Column is NRUBRCR. |
| 9 | `FS.GA.FEE.CODE.DEFINITION.CREDIT.ACCOUNT.SUFFIX.NUMBER` | `FsGaFeeCodeDefinition_CreditAccountSuffixNumber` | TField |  | Credit account suffix number tagged to a fee code Multifonds DB Column is NSUFFCR. |
| 10 | `FS.GA.FEE.CODE.DEFINITION.CURRENCY.IDENTIFIER` | `FsGaFeeCodeDefinition_CurrencyIdentifier` | TField |  | Currency flag to denote if the accrual should be in local or base currency Multifonds DB Column is FCDEV. |
| 11 | `FS.GA.FEE.CODE.DEFINITION.DATE.VAL` | `FsGaFeeCodeDefinition_DateVal` | TField |  | Indicates whether a deal&apos;s maturity date should be managed at account level. Only use for deposits, loans, IRS, forward FX and contingency accounts for options and futures Multifonds DB Column is FDVAL. |
| 12 | `FS.GA.FEE.CODE.DEFINITION.DEBIT.CREDIT.INDICATOR` | `FsGaFeeCodeDefinition_DebitCreditIndicator` | TField |  | Debit credit indicator tagged to an account number Multifonds DB Column is CSENS. |
| 13 | `FS.GA.FEE.CODE.DEFINITION.INTEREST.DAYS` | `FsGaFeeCodeDefinition_InterestDays` | TField |  | Number of days of accrued interest purchases/sold in a transaction on an income bearing instrument Multifonds DB Column is NBJ_JOUR. |
| 14 | `FS.GA.FEE.CODE.DEFINITION.NEGATIVE.DEBIT.ACCOUNT.NO` | `FsGaFeeCodeDefinition_NegativeDebitAccountNo` | TField |  | Negative Debit account number tagged to a fee code Multifonds DB Column is NRUBRDB_NEG. |
| 15 | `FS.GA.FEE.CODE.DEFINITION.NEG.DEBIT.ACCOUNT.SUFFIX.NO` | `FsGaFeeCodeDefinition_NegDebitAccountSuffixNo` | TField |  | Negative Debit account suffix number tagged to a fee code Multifonds DB Column is NSUFFDB_NEG. |
| 16 | `FS.GA.FEE.CODE.DEFINITION.NEGATIVE.CREDIT.ACCOUNT.NO` | `FsGaFeeCodeDefinition_NegativeCreditAccountNo` | TField |  | Negative Credit account number tagged to a fee code Multifonds DB Column is NRUBRCR_NEG. |
| 17 | `FS.GA.FEE.CODE.DEFINITION.NEG.CREDIT.ACCOUNT.SUFFIX.NO` | `FsGaFeeCodeDefinition_NegCreditAccountSuffixNo` | TField |  | Negative Credit account suffix number tagged to a fee code Multifonds DB Column is NSUFFCR_NEG. |
| 18 | `FS.GA.FEE.CODE.DEFINITION.IFRS.CATEGORY` | `FsGaFeeCodeDefinition_IfrsCategory` | TField |  | IFRS category assigned to a transaction Multifonds DB Column is SUB_TYPE. |
| 19 | `FS.GA.FEE.CODE.DEFINITION.RESERVED10` | `FsGaFeeCodeDefinition_Reserved10` | TField |  |  |
| 20 | `FS.GA.FEE.CODE.DEFINITION.RESERVED9` | `FsGaFeeCodeDefinition_Reserved9` | TField |  |  |
| 21 | `FS.GA.FEE.CODE.DEFINITION.RESERVED8` | `FsGaFeeCodeDefinition_Reserved8` | TField |  |  |
| 22 | `FS.GA.FEE.CODE.DEFINITION.RESERVED7` | `FsGaFeeCodeDefinition_Reserved7` | TField |  |  |
| 23 | `FS.GA.FEE.CODE.DEFINITION.RESERVED6` | `FsGaFeeCodeDefinition_Reserved6` | TField |  |  |
| 24 | `FS.GA.FEE.CODE.DEFINITION.RESERVED5` | `FsGaFeeCodeDefinition_Reserved5` | TField |  |  |
| 25 | `FS.GA.FEE.CODE.DEFINITION.RESERVED4` | `FsGaFeeCodeDefinition_Reserved4` | TField |  |  |
| 26 | `FS.GA.FEE.CODE.DEFINITION.RESERVED3` | `FsGaFeeCodeDefinition_Reserved3` | TField |  |  |
| 27 | `FS.GA.FEE.CODE.DEFINITION.RESERVED2` | `FsGaFeeCodeDefinition_Reserved2` | TField |  |  |
| 28 | `FS.GA.FEE.CODE.DEFINITION.RESERVED1` | `FsGaFeeCodeDefinition_Reserved1` | TField |  |  |
| 29 | `FS.GA.FEE.CODE.DEFINITION.LOCAL.REF` | `FsGaFeeCodeDefinition_LocalRef` |  |  |  |
| 30 | `FS.GA.FEE.CODE.DEFINITION.OVERRIDE` | `FsGaFeeCodeDefinition_Override` |  |  |  |
| 31 | `FS.GA.FEE.CODE.DEFINITION.RECORD.STATUS` | `FsGaFeeCodeDefinition_RecordStatus` | String |  |  |
| 32 | `FS.GA.FEE.CODE.DEFINITION.CURR.NO` | `FsGaFeeCodeDefinition_CurrNo` | String |  |  |
| 33 | `FS.GA.FEE.CODE.DEFINITION.INPUTTER` | `FsGaFeeCodeDefinition_Inputter` |  |  |  |
| 34 | `FS.GA.FEE.CODE.DEFINITION.DATE.TIME` | `FsGaFeeCodeDefinition_DateTime` |  |  |  |
| 35 | `FS.GA.FEE.CODE.DEFINITION.AUTHORISER` | `FsGaFeeCodeDefinition_Authoriser` | String |  |  |
| 36 | `FS.GA.FEE.CODE.DEFINITION.CO.CODE` | `FsGaFeeCodeDefinition_CoCode` | String |  |  |
| 37 | `FS.GA.FEE.CODE.DEFINITION.DEPT.CODE` | `FsGaFeeCodeDefinition_DeptCode` | String |  |  |
| 38 | `FS.GA.FEE.CODE.DEFINITION.AUDITOR.CODE` | `FsGaFeeCodeDefinition_AuditorCode` | String |  |  |
| 39 | `FS.GA.FEE.CODE.DEFINITION.AUDIT.DATE.TIME` | `FsGaFeeCodeDefinition_AuditDateTime` | String |  |  |
