# FS.GA.ACCOUNTINGCHART.DESCRIPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNTINGCHART.DESCRIPTION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.PARENT.REF.ID` | `FsGaAccountingchartDescription_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.ORA.ROWID` | `FsGaAccountingchartDescription_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.CHART.OF.ACCOUNTS.CODE` | `FsGaAccountingchartDescription_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.GL.ACCOUNT` | `FsGaAccountingchartDescription_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.LANGUAGE` | `FsGaAccountingchartDescription_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 6 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.DESCRIPTION` | `FsGaAccountingchartDescription_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RESERVED10` | `FsGaAccountingchartDescription_Reserved10` | TField |  |  |
| 8 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RESERVED9` | `FsGaAccountingchartDescription_Reserved9` | TField |  |  |
| 9 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RESERVED8` | `FsGaAccountingchartDescription_Reserved8` | TField |  |  |
| 10 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RESERVED7` | `FsGaAccountingchartDescription_Reserved7` | TField |  |  |
| 11 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RESERVED6` | `FsGaAccountingchartDescription_Reserved6` | TField |  |  |
| 12 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RESERVED5` | `FsGaAccountingchartDescription_Reserved5` | TField |  |  |
| 13 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RESERVED4` | `FsGaAccountingchartDescription_Reserved4` | TField |  |  |
| 14 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RESERVED3` | `FsGaAccountingchartDescription_Reserved3` | TField |  |  |
| 15 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RESERVED2` | `FsGaAccountingchartDescription_Reserved2` | TField |  |  |
| 16 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RESERVED1` | `FsGaAccountingchartDescription_Reserved1` | TField |  |  |
| 17 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.LOCAL.REF` | `FsGaAccountingchartDescription_LocalRef` |  |  |  |
| 18 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.OVERRIDE` | `FsGaAccountingchartDescription_Override` |  |  |  |
| 19 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.RECORD.STATUS` | `FsGaAccountingchartDescription_RecordStatus` | String |  |  |
| 20 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.CURR.NO` | `FsGaAccountingchartDescription_CurrNo` | String |  |  |
| 21 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.INPUTTER` | `FsGaAccountingchartDescription_Inputter` |  |  |  |
| 22 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.DATE.TIME` | `FsGaAccountingchartDescription_DateTime` |  |  |  |
| 23 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.AUTHORISER` | `FsGaAccountingchartDescription_Authoriser` | String |  |  |
| 24 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.CO.CODE` | `FsGaAccountingchartDescription_CoCode` | String |  |  |
| 25 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.DEPT.CODE` | `FsGaAccountingchartDescription_DeptCode` | String |  |  |
| 26 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.AUDITOR.CODE` | `FsGaAccountingchartDescription_AuditorCode` | String |  |  |
| 27 | `FS.GA.ACCOUNTINGCHART.DESCRIPTION.AUDIT.DATE.TIME` | `FsGaAccountingchartDescription_AuditDateTime` | String |  |  |
