# FS.GA.ACCOUNTS.DESCRIPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNTS.DESCRIPTION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ACCOUNTS.DESCRIPTION.PARENT.REF.ID` | `FsGaAccountsDescription_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.ACCOUNTS.DESCRIPTION.ORA.ROWID` | `FsGaAccountsDescription_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.ACCOUNTS.DESCRIPTION.LEDGER.NUMBER` | `FsGaAccountsDescription_LedgerNumber` | TField |  | This is the account number for the ledger. Multifonds DB Column is NCOMPTE. |
| 4 | `FS.GA.ACCOUNTS.DESCRIPTION.LANGUAGE` | `FsGaAccountsDescription_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 5 | `FS.GA.ACCOUNTS.DESCRIPTION.DESCRIPTION` | `FsGaAccountsDescription_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 6 | `FS.GA.ACCOUNTS.DESCRIPTION.CHART.OF.ACCOUNTS.CODE` | `FsGaAccountsDescription_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 7 | `FS.GA.ACCOUNTS.DESCRIPTION.RESERVED10` | `FsGaAccountsDescription_Reserved10` | TField |  |  |
| 8 | `FS.GA.ACCOUNTS.DESCRIPTION.RESERVED9` | `FsGaAccountsDescription_Reserved9` | TField |  |  |
| 9 | `FS.GA.ACCOUNTS.DESCRIPTION.RESERVED8` | `FsGaAccountsDescription_Reserved8` | TField |  |  |
| 10 | `FS.GA.ACCOUNTS.DESCRIPTION.RESERVED7` | `FsGaAccountsDescription_Reserved7` | TField |  |  |
| 11 | `FS.GA.ACCOUNTS.DESCRIPTION.RESERVED6` | `FsGaAccountsDescription_Reserved6` | TField |  |  |
| 12 | `FS.GA.ACCOUNTS.DESCRIPTION.RESERVED5` | `FsGaAccountsDescription_Reserved5` | TField |  |  |
| 13 | `FS.GA.ACCOUNTS.DESCRIPTION.RESERVED4` | `FsGaAccountsDescription_Reserved4` | TField |  |  |
| 14 | `FS.GA.ACCOUNTS.DESCRIPTION.RESERVED3` | `FsGaAccountsDescription_Reserved3` | TField |  |  |
| 15 | `FS.GA.ACCOUNTS.DESCRIPTION.RESERVED2` | `FsGaAccountsDescription_Reserved2` | TField |  |  |
| 16 | `FS.GA.ACCOUNTS.DESCRIPTION.RESERVED1` | `FsGaAccountsDescription_Reserved1` | TField |  |  |
| 17 | `FS.GA.ACCOUNTS.DESCRIPTION.LOCAL.REF` | `FsGaAccountsDescription_LocalRef` |  |  |  |
| 18 | `FS.GA.ACCOUNTS.DESCRIPTION.OVERRIDE` | `FsGaAccountsDescription_Override` |  |  |  |
| 19 | `FS.GA.ACCOUNTS.DESCRIPTION.RECORD.STATUS` | `FsGaAccountsDescription_RecordStatus` | String |  |  |
| 20 | `FS.GA.ACCOUNTS.DESCRIPTION.CURR.NO` | `FsGaAccountsDescription_CurrNo` | String |  |  |
| 21 | `FS.GA.ACCOUNTS.DESCRIPTION.INPUTTER` | `FsGaAccountsDescription_Inputter` |  |  |  |
| 22 | `FS.GA.ACCOUNTS.DESCRIPTION.DATE.TIME` | `FsGaAccountsDescription_DateTime` |  |  |  |
| 23 | `FS.GA.ACCOUNTS.DESCRIPTION.AUTHORISER` | `FsGaAccountsDescription_Authoriser` | String |  |  |
| 24 | `FS.GA.ACCOUNTS.DESCRIPTION.CO.CODE` | `FsGaAccountsDescription_CoCode` | String |  |  |
| 25 | `FS.GA.ACCOUNTS.DESCRIPTION.DEPT.CODE` | `FsGaAccountsDescription_DeptCode` | String |  |  |
| 26 | `FS.GA.ACCOUNTS.DESCRIPTION.AUDITOR.CODE` | `FsGaAccountsDescription_AuditorCode` | String |  |  |
| 27 | `FS.GA.ACCOUNTS.DESCRIPTION.AUDIT.DATE.TIME` | `FsGaAccountsDescription_AuditDateTime` | String |  |  |
