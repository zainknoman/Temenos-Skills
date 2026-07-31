# FS.GA.ACCOUNTING.CHART — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNTING.CHART` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ACCOUNTING.CHART.PARENT.REF.ID` | `FsGaAccountingChart_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.ACCOUNTING.CHART.ORA.ROWID` | `FsGaAccountingChart_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.ACCOUNTING.CHART.CHART.OF.ACCOUNTS.CODE` | `FsGaAccountingChart_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.ACCOUNTING.CHART.GL.ACCOUNT` | `FsGaAccountingChart_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.ACCOUNTING.CHART.BS.GROUPING` | `FsGaAccountingChart_BsGrouping` | TField |  | Balance sheet grouping like Assets, Liabilities etc Multifonds DB Column is CTIF. |
| 6 | `FS.GA.ACCOUNTING.CHART.DESCRIPTION` | `FsGaAccountingChart_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GA.ACCOUNTING.CHART.CURRENCY.SETUP.ON.ACCOUNTS` | `FsGaAccountingChart_CurrencySetupOnAccounts` | TField |  | Currency Setup on Accounts at chart level parameterization Multifonds DB Column is FDEV. |
| 8 | `FS.GA.ACCOUNTING.CHART.RESERVED10` | `FsGaAccountingChart_Reserved10` | TField |  |  |
| 9 | `FS.GA.ACCOUNTING.CHART.RESERVED9` | `FsGaAccountingChart_Reserved9` | TField |  |  |
| 10 | `FS.GA.ACCOUNTING.CHART.RESERVED8` | `FsGaAccountingChart_Reserved8` | TField |  |  |
| 11 | `FS.GA.ACCOUNTING.CHART.RESERVED7` | `FsGaAccountingChart_Reserved7` | TField |  |  |
| 12 | `FS.GA.ACCOUNTING.CHART.RESERVED6` | `FsGaAccountingChart_Reserved6` | TField |  |  |
| 13 | `FS.GA.ACCOUNTING.CHART.RESERVED5` | `FsGaAccountingChart_Reserved5` | TField |  |  |
| 14 | `FS.GA.ACCOUNTING.CHART.RESERVED4` | `FsGaAccountingChart_Reserved4` | TField |  |  |
| 15 | `FS.GA.ACCOUNTING.CHART.RESERVED3` | `FsGaAccountingChart_Reserved3` | TField |  |  |
| 16 | `FS.GA.ACCOUNTING.CHART.RESERVED2` | `FsGaAccountingChart_Reserved2` | TField |  |  |
| 17 | `FS.GA.ACCOUNTING.CHART.RESERVED1` | `FsGaAccountingChart_Reserved1` | TField |  |  |
| 18 | `FS.GA.ACCOUNTING.CHART.LOCAL.REF` | `FsGaAccountingChart_LocalRef` |  |  |  |
| 19 | `FS.GA.ACCOUNTING.CHART.OVERRIDE` | `FsGaAccountingChart_Override` |  |  |  |
| 20 | `FS.GA.ACCOUNTING.CHART.RECORD.STATUS` | `FsGaAccountingChart_RecordStatus` | String |  |  |
| 21 | `FS.GA.ACCOUNTING.CHART.CURR.NO` | `FsGaAccountingChart_CurrNo` | String |  |  |
| 22 | `FS.GA.ACCOUNTING.CHART.INPUTTER` | `FsGaAccountingChart_Inputter` |  |  |  |
| 23 | `FS.GA.ACCOUNTING.CHART.DATE.TIME` | `FsGaAccountingChart_DateTime` |  |  |  |
| 24 | `FS.GA.ACCOUNTING.CHART.AUTHORISER` | `FsGaAccountingChart_Authoriser` | String |  |  |
| 25 | `FS.GA.ACCOUNTING.CHART.CO.CODE` | `FsGaAccountingChart_CoCode` | String |  |  |
| 26 | `FS.GA.ACCOUNTING.CHART.DEPT.CODE` | `FsGaAccountingChart_DeptCode` | String |  |  |
| 27 | `FS.GA.ACCOUNTING.CHART.AUDITOR.CODE` | `FsGaAccountingChart_AuditorCode` | String |  |  |
| 28 | `FS.GA.ACCOUNTING.CHART.AUDIT.DATE.TIME` | `FsGaAccountingChart_AuditDateTime` | String |  |  |
