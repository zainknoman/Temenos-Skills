# FS.GA.NAV.CODE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.CODE.DEFINITION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.CODE.DEFINITION.PARENT.REF.ID` | `FsGaNavCodeDefinition_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.CODE.DEFINITION.ORA.ROWID` | `FsGaNavCodeDefinition_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.CODE.DEFINITION.CHART.OF.ACCOUNTS.CODE` | `FsGaNavCodeDefinition_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.NAV.CODE.DEFINITION.OPERATION.CODE` | `FsGaNavCodeDefinition_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 5 | `FS.GA.NAV.CODE.DEFINITION.GTI.CODE` | `FsGaNavCodeDefinition_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 6 | `FS.GA.NAV.CODE.DEFINITION.DEBIT.ACCOUNT.NUMBER` | `FsGaNavCodeDefinition_DebitAccountNumber` | TField |  | Debit account number tagged to a fee code Multifonds DB Column is NRUBRDB. |
| 7 | `FS.GA.NAV.CODE.DEFINITION.CREDIT.ACCOUNT.NUMBER` | `FsGaNavCodeDefinition_CreditAccountNumber` | TField |  | Credit account number tagged to a fee code Multifonds DB Column is NRUBRCR. |
| 8 | `FS.GA.NAV.CODE.DEFINITION.CURRENCY.IDENTIFIER` | `FsGaNavCodeDefinition_CurrencyIdentifier` | TField |  | Currency flag to denote if the accrual should be in local or base currency Multifonds DB Column is FCDEV. |
| 9 | `FS.GA.NAV.CODE.DEFINITION.DATE.VAL` | `FsGaNavCodeDefinition_DateVal` | TField |  | Indicates whether a deal&apos;s maturity date should be managed at account level. Only use for deposits, loans, IRS, forward FX and contingency accounts for options and futures Multifonds DB Column is FDVAL. |
| 10 | `FS.GA.NAV.CODE.DEFINITION.SUFFIX` | `FsGaNavCodeDefinition_Suffix` | TField |  | Account Suffix Number Multifonds DB Column is FSUFF. |
| 11 | `FS.GA.NAV.CODE.DEFINITION.NEGATIVE.DEBIT.ACCOUNT.NO` | `FsGaNavCodeDefinition_NegativeDebitAccountNo` | TField |  | Negative Debit account number tagged to a fee code Multifonds DB Column is NRUBRDB_NEG. |
| 12 | `FS.GA.NAV.CODE.DEFINITION.NEGATIVE.CREDIT.ACCOUNT.NO` | `FsGaNavCodeDefinition_NegativeCreditAccountNo` | TField |  | Negative Credit account number tagged to a fee code Multifonds DB Column is NRUBRCR_NEG. |
| 13 | `FS.GA.NAV.CODE.DEFINITION.SECURITY.PRICE.NET` | `FsGaNavCodeDefinition_SecurityPriceNet` | TField |  | This field allow user to include or exclude the brokerage and Transaction fees as part of the Cost Multifonds DB Column is FLG_NET. |
| 14 | `FS.GA.NAV.CODE.DEFINITION.IFRS.CATEGORY` | `FsGaNavCodeDefinition_IfrsCategory` | TField |  | IFRS category assigned to a transaction Multifonds DB Column is SUB_TYPE. |
| 15 | `FS.GA.NAV.CODE.DEFINITION.RESERVED10` | `FsGaNavCodeDefinition_Reserved10` | TField |  |  |
| 16 | `FS.GA.NAV.CODE.DEFINITION.RESERVED9` | `FsGaNavCodeDefinition_Reserved9` | TField |  |  |
| 17 | `FS.GA.NAV.CODE.DEFINITION.RESERVED8` | `FsGaNavCodeDefinition_Reserved8` | TField |  |  |
| 18 | `FS.GA.NAV.CODE.DEFINITION.RESERVED7` | `FsGaNavCodeDefinition_Reserved7` | TField |  |  |
| 19 | `FS.GA.NAV.CODE.DEFINITION.RESERVED6` | `FsGaNavCodeDefinition_Reserved6` | TField |  |  |
| 20 | `FS.GA.NAV.CODE.DEFINITION.RESERVED5` | `FsGaNavCodeDefinition_Reserved5` | TField |  |  |
| 21 | `FS.GA.NAV.CODE.DEFINITION.RESERVED4` | `FsGaNavCodeDefinition_Reserved4` | TField |  |  |
| 22 | `FS.GA.NAV.CODE.DEFINITION.RESERVED3` | `FsGaNavCodeDefinition_Reserved3` | TField |  |  |
| 23 | `FS.GA.NAV.CODE.DEFINITION.RESERVED2` | `FsGaNavCodeDefinition_Reserved2` | TField |  |  |
| 24 | `FS.GA.NAV.CODE.DEFINITION.RESERVED1` | `FsGaNavCodeDefinition_Reserved1` | TField |  |  |
| 25 | `FS.GA.NAV.CODE.DEFINITION.LOCAL.REF` | `FsGaNavCodeDefinition_LocalRef` |  |  |  |
| 26 | `FS.GA.NAV.CODE.DEFINITION.OVERRIDE` | `FsGaNavCodeDefinition_Override` |  |  |  |
| 27 | `FS.GA.NAV.CODE.DEFINITION.RECORD.STATUS` | `FsGaNavCodeDefinition_RecordStatus` | String |  |  |
| 28 | `FS.GA.NAV.CODE.DEFINITION.CURR.NO` | `FsGaNavCodeDefinition_CurrNo` | String |  |  |
| 29 | `FS.GA.NAV.CODE.DEFINITION.INPUTTER` | `FsGaNavCodeDefinition_Inputter` |  |  |  |
| 30 | `FS.GA.NAV.CODE.DEFINITION.DATE.TIME` | `FsGaNavCodeDefinition_DateTime` |  |  |  |
| 31 | `FS.GA.NAV.CODE.DEFINITION.AUTHORISER` | `FsGaNavCodeDefinition_Authoriser` | String |  |  |
| 32 | `FS.GA.NAV.CODE.DEFINITION.CO.CODE` | `FsGaNavCodeDefinition_CoCode` | String |  |  |
| 33 | `FS.GA.NAV.CODE.DEFINITION.DEPT.CODE` | `FsGaNavCodeDefinition_DeptCode` | String |  |  |
| 34 | `FS.GA.NAV.CODE.DEFINITION.AUDITOR.CODE` | `FsGaNavCodeDefinition_AuditorCode` | String |  |  |
| 35 | `FS.GA.NAV.CODE.DEFINITION.AUDIT.DATE.TIME` | `FsGaNavCodeDefinition_AuditDateTime` | String |  |  |
