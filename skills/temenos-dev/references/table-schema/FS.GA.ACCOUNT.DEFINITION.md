# FS.GA.ACCOUNT.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNT.DEFINITION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ACCOUNT.DEFINITION.PARENT.REF.ID` | `FsGaAccountDefinition_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.ACCOUNT.DEFINITION.ORA.ROWID` | `FsGaAccountDefinition_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.ACCOUNT.DEFINITION.LEDGER.NUMBER` | `FsGaAccountDefinition_LedgerNumber` | TField |  | This is the account number for the ledger. Multifonds DB Column is NCOMPTE. |
| 4 | `FS.GA.ACCOUNT.DEFINITION.LANGUAGE` | `FsGaAccountDefinition_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 5 | `FS.GA.ACCOUNT.DEFINITION.DESCRIPTION` | `FsGaAccountDefinition_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 6 | `FS.GA.ACCOUNT.DEFINITION.DEBIT.CREDIT.INDICATOR` | `FsGaAccountDefinition_DebitCreditIndicator` | TField |  | Debit credit indicator tagged to an account number Multifonds DB Column is CSENS. |
| 7 | `FS.GA.ACCOUNT.DEFINITION.INTEREST.ACCOUNT` | `FsGaAccountDefinition_InterestAccount` | TField |  | This indicates whether calculation of interest will be supported on this account or not. Multifonds DB Column is FCIE. |
| 8 | `FS.GA.ACCOUNT.DEFINITION.SHADOW.ACCOUNT` | `FsGaAccountDefinition_ShadowAccount` | TField |  | Indicates the Assets and liabilities accounts used for the automatic booking of the unrealized P/L on securities, fee provisions and accrued interests during the NAV Process. Multifonds DB Column is CPTRANS. |
| 9 | `FS.GA.ACCOUNT.DEFINITION.VALUE.DATE.ACCOUNTS` | `FsGaAccountDefinition_ValueDateAccounts` | TField |  | Indicates if the account is used as a transitory account (payables, receivables). Multifonds DB Column is FVAL. |
| 10 | `FS.GA.ACCOUNT.DEFINITION.OFF.BALANCESHEET.ACCOUNT` | `FsGaAccountDefinition_OffBalancesheetAccount` | TField |  | Indicates if the account will be used as an off-balance sheet account. Multifonds DB Column is FHB. |
| 11 | `FS.GA.ACCOUNT.DEFINITION.SECURITY.ACCOUNT` | `FsGaAccountDefinition_SecurityAccount` | TField |  | Accounts representing securities positions Multifonds DB Column is FTIT. |
| 12 | `FS.GA.ACCOUNT.DEFINITION.CHART.OF.ACCOUNTS.CODE` | `FsGaAccountDefinition_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 13 | `FS.GA.ACCOUNT.DEFINITION.RESERVED10` | `FsGaAccountDefinition_Reserved10` | TField |  |  |
| 14 | `FS.GA.ACCOUNT.DEFINITION.RESERVED9` | `FsGaAccountDefinition_Reserved9` | TField |  |  |
| 15 | `FS.GA.ACCOUNT.DEFINITION.RESERVED8` | `FsGaAccountDefinition_Reserved8` | TField |  |  |
| 16 | `FS.GA.ACCOUNT.DEFINITION.RESERVED7` | `FsGaAccountDefinition_Reserved7` | TField |  |  |
| 17 | `FS.GA.ACCOUNT.DEFINITION.RESERVED6` | `FsGaAccountDefinition_Reserved6` | TField |  |  |
| 18 | `FS.GA.ACCOUNT.DEFINITION.RESERVED5` | `FsGaAccountDefinition_Reserved5` | TField |  |  |
| 19 | `FS.GA.ACCOUNT.DEFINITION.RESERVED4` | `FsGaAccountDefinition_Reserved4` | TField |  |  |
| 20 | `FS.GA.ACCOUNT.DEFINITION.RESERVED3` | `FsGaAccountDefinition_Reserved3` | TField |  |  |
| 21 | `FS.GA.ACCOUNT.DEFINITION.RESERVED2` | `FsGaAccountDefinition_Reserved2` | TField |  |  |
| 22 | `FS.GA.ACCOUNT.DEFINITION.RESERVED1` | `FsGaAccountDefinition_Reserved1` | TField |  |  |
| 23 | `FS.GA.ACCOUNT.DEFINITION.LOCAL.REF` | `FsGaAccountDefinition_LocalRef` |  |  |  |
| 24 | `FS.GA.ACCOUNT.DEFINITION.OVERRIDE` | `FsGaAccountDefinition_Override` |  |  |  |
| 25 | `FS.GA.ACCOUNT.DEFINITION.RECORD.STATUS` | `FsGaAccountDefinition_RecordStatus` | String |  |  |
| 26 | `FS.GA.ACCOUNT.DEFINITION.CURR.NO` | `FsGaAccountDefinition_CurrNo` | String |  |  |
| 27 | `FS.GA.ACCOUNT.DEFINITION.INPUTTER` | `FsGaAccountDefinition_Inputter` |  |  |  |
| 28 | `FS.GA.ACCOUNT.DEFINITION.DATE.TIME` | `FsGaAccountDefinition_DateTime` |  |  |  |
| 29 | `FS.GA.ACCOUNT.DEFINITION.AUTHORISER` | `FsGaAccountDefinition_Authoriser` | String |  |  |
| 30 | `FS.GA.ACCOUNT.DEFINITION.CO.CODE` | `FsGaAccountDefinition_CoCode` | String |  |  |
| 31 | `FS.GA.ACCOUNT.DEFINITION.DEPT.CODE` | `FsGaAccountDefinition_DeptCode` | String |  |  |
| 32 | `FS.GA.ACCOUNT.DEFINITION.AUDITOR.CODE` | `FsGaAccountDefinition_AuditorCode` | String |  |  |
| 33 | `FS.GA.ACCOUNT.DEFINITION.AUDIT.DATE.TIME` | `FsGaAccountDefinition_AuditDateTime` | String |  |  |
