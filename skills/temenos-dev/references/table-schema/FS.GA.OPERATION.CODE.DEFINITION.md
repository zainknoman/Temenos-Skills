# FS.GA.OPERATION.CODE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPERATION.CODE.DEFINITION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPERATION.CODE.DEFINITION.PARENT.REF.ID` | `FsGaOperationCodeDefinition_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.OPERATION.CODE.DEFINITION.ORA.ROWID` | `FsGaOperationCodeDefinition_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.OPERATION.CODE.DEFINITION.CHART.OF.ACCOUNTS.CODE` | `FsGaOperationCodeDefinition_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.OPERATION.CODE.DEFINITION.OPERATION.CODE` | `FsGaOperationCodeDefinition_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 5 | `FS.GA.OPERATION.CODE.DEFINITION.GTI.CODE` | `FsGaOperationCodeDefinition_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 6 | `FS.GA.OPERATION.CODE.DEFINITION.DEBIT.ACCOUNT.NUMBER` | `FsGaOperationCodeDefinition_DebitAccountNumber` | TField |  | Debit account number tagged to a fee code Multifonds DB Column is NRUBRDB. |
| 7 | `FS.GA.OPERATION.CODE.DEFINITION.CREDIT.ACCOUNT.NUMBER` | `FsGaOperationCodeDefinition_CreditAccountNumber` | TField |  | Credit account number tagged to a fee code Multifonds DB Column is NRUBRCR. |
| 8 | `FS.GA.OPERATION.CODE.DEFINITION.VALUE.DATE.ACCOUNT.DEBIT` | `FsGaOperationCodeDefinition_ValueDateAccountDebit` | TField |  | Account Number Debit Multifonds DB Column is NRUBVDB. |
| 9 | `FS.GA.OPERATION.CODE.DEFINITION.VALUE.DATE.ACCOUNT.CREDIT` | `FsGaOperationCodeDefinition_ValueDateAccountCredit` | TField |  | Account Number Credit Multifonds DB Column is NRUBVCR. |
| 10 | `FS.GA.OPERATION.CODE.DEFINITION.CURRENCY.IDENTIFIER` | `FsGaOperationCodeDefinition_CurrencyIdentifier` | TField |  | Currency flag to denote if the accrual should be in local or base currency Multifonds DB Column is FCDEV. |
| 11 | `FS.GA.OPERATION.CODE.DEFINITION.DATE.VAL` | `FsGaOperationCodeDefinition_DateVal` | TField |  | Indicates whether a deal&apos;s maturity date should be managed at account level. Only use for deposits, loans, IRS, forward FX and contingency accounts for options and futures Multifonds DB Column is FDVAL. |
| 12 | `FS.GA.OPERATION.CODE.DEFINITION.SUFFIX` | `FsGaOperationCodeDefinition_Suffix` | TField |  | Account Suffix Number Multifonds DB Column is FSUFF. |
| 13 | `FS.GA.OPERATION.CODE.DEFINITION.DEBIT.ACCOUNT.NEGATIVE` | `FsGaOperationCodeDefinition_DebitAccountNegative` | TField |  | Debit Account Negative Multifonds DB Column is NEGNRUBRDB. |
| 14 | `FS.GA.OPERATION.CODE.DEFINITION.CREDIT.ACCOUNT.NEGATIVE` | `FsGaOperationCodeDefinition_CreditAccountNegative` | TField |  | Credit Account Negative Multifonds DB Column is NEGNRUBRCR. |
| 15 | `FS.GA.OPERATION.CODE.DEFINITION.IFRS.CATEGORY` | `FsGaOperationCodeDefinition_IfrsCategory` | TField |  | IFRS category assigned to a transaction Multifonds DB Column is SUB_TYPE. |
| 16 | `FS.GA.OPERATION.CODE.DEFINITION.SUB.TYPE.CFD` | `FsGaOperationCodeDefinition_SubTypeCfd` | TField |  | Define to Supports more than to 99 contracts per CFD without changing the maturity date of the contract Multifonds DB Column is SUB_TYPE_CFD. |
| 17 | `FS.GA.OPERATION.CODE.DEFINITION.RESERVED10` | `FsGaOperationCodeDefinition_Reserved10` | TField |  |  |
| 18 | `FS.GA.OPERATION.CODE.DEFINITION.RESERVED9` | `FsGaOperationCodeDefinition_Reserved9` | TField |  |  |
| 19 | `FS.GA.OPERATION.CODE.DEFINITION.RESERVED8` | `FsGaOperationCodeDefinition_Reserved8` | TField |  |  |
| 20 | `FS.GA.OPERATION.CODE.DEFINITION.RESERVED7` | `FsGaOperationCodeDefinition_Reserved7` | TField |  |  |
| 21 | `FS.GA.OPERATION.CODE.DEFINITION.RESERVED6` | `FsGaOperationCodeDefinition_Reserved6` | TField |  |  |
| 22 | `FS.GA.OPERATION.CODE.DEFINITION.RESERVED5` | `FsGaOperationCodeDefinition_Reserved5` | TField |  |  |
| 23 | `FS.GA.OPERATION.CODE.DEFINITION.RESERVED4` | `FsGaOperationCodeDefinition_Reserved4` | TField |  |  |
| 24 | `FS.GA.OPERATION.CODE.DEFINITION.RESERVED3` | `FsGaOperationCodeDefinition_Reserved3` | TField |  |  |
| 25 | `FS.GA.OPERATION.CODE.DEFINITION.RESERVED2` | `FsGaOperationCodeDefinition_Reserved2` | TField |  |  |
| 26 | `FS.GA.OPERATION.CODE.DEFINITION.RESERVED1` | `FsGaOperationCodeDefinition_Reserved1` | TField |  |  |
| 27 | `FS.GA.OPERATION.CODE.DEFINITION.LOCAL.REF` | `FsGaOperationCodeDefinition_LocalRef` |  |  |  |
| 28 | `FS.GA.OPERATION.CODE.DEFINITION.OVERRIDE` | `FsGaOperationCodeDefinition_Override` |  |  |  |
| 29 | `FS.GA.OPERATION.CODE.DEFINITION.RECORD.STATUS` | `FsGaOperationCodeDefinition_RecordStatus` | String |  |  |
| 30 | `FS.GA.OPERATION.CODE.DEFINITION.CURR.NO` | `FsGaOperationCodeDefinition_CurrNo` | String |  |  |
| 31 | `FS.GA.OPERATION.CODE.DEFINITION.INPUTTER` | `FsGaOperationCodeDefinition_Inputter` |  |  |  |
| 32 | `FS.GA.OPERATION.CODE.DEFINITION.DATE.TIME` | `FsGaOperationCodeDefinition_DateTime` |  |  |  |
| 33 | `FS.GA.OPERATION.CODE.DEFINITION.AUTHORISER` | `FsGaOperationCodeDefinition_Authoriser` | String |  |  |
| 34 | `FS.GA.OPERATION.CODE.DEFINITION.CO.CODE` | `FsGaOperationCodeDefinition_CoCode` | String |  |  |
| 35 | `FS.GA.OPERATION.CODE.DEFINITION.DEPT.CODE` | `FsGaOperationCodeDefinition_DeptCode` | String |  |  |
| 36 | `FS.GA.OPERATION.CODE.DEFINITION.AUDITOR.CODE` | `FsGaOperationCodeDefinition_AuditorCode` | String |  |  |
| 37 | `FS.GA.OPERATION.CODE.DEFINITION.AUDIT.DATE.TIME` | `FsGaOperationCodeDefinition_AuditDateTime` | String |  |  |
