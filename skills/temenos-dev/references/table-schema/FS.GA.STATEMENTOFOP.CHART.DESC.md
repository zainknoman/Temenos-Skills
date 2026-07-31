# FS.GA.STATEMENTOFOP.CHART.DESC — Table Schema

> Source: `INSERTS/I_F.FS.GA.STATEMENTOFOP.CHART.DESC` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.STATEMENTOFOP.CHART.DESC.PARENT.REF.ID` | `FsGaStatementofopChartDesc_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.STATEMENTOFOP.CHART.DESC.ORA.ROWID` | `FsGaStatementofopChartDesc_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.STATEMENTOFOP.CHART.DESC.CHART.OF.ACCOUNTS.CODE` | `FsGaStatementofopChartDesc_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.STATEMENTOFOP.CHART.DESC.GL.ACCOUNT` | `FsGaStatementofopChartDesc_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.STATEMENTOFOP.CHART.DESC.LANGUAGE` | `FsGaStatementofopChartDesc_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 6 | `FS.GA.STATEMENTOFOP.CHART.DESC.DESCRIPTION` | `FsGaStatementofopChartDesc_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GA.STATEMENTOFOP.CHART.DESC.RESERVED10` | `FsGaStatementofopChartDesc_Reserved10` | TField |  |  |
| 8 | `FS.GA.STATEMENTOFOP.CHART.DESC.RESERVED9` | `FsGaStatementofopChartDesc_Reserved9` | TField |  |  |
| 9 | `FS.GA.STATEMENTOFOP.CHART.DESC.RESERVED8` | `FsGaStatementofopChartDesc_Reserved8` | TField |  |  |
| 10 | `FS.GA.STATEMENTOFOP.CHART.DESC.RESERVED7` | `FsGaStatementofopChartDesc_Reserved7` | TField |  |  |
| 11 | `FS.GA.STATEMENTOFOP.CHART.DESC.RESERVED6` | `FsGaStatementofopChartDesc_Reserved6` | TField |  |  |
| 12 | `FS.GA.STATEMENTOFOP.CHART.DESC.RESERVED5` | `FsGaStatementofopChartDesc_Reserved5` | TField |  |  |
| 13 | `FS.GA.STATEMENTOFOP.CHART.DESC.RESERVED4` | `FsGaStatementofopChartDesc_Reserved4` | TField |  |  |
| 14 | `FS.GA.STATEMENTOFOP.CHART.DESC.RESERVED3` | `FsGaStatementofopChartDesc_Reserved3` | TField |  |  |
| 15 | `FS.GA.STATEMENTOFOP.CHART.DESC.RESERVED2` | `FsGaStatementofopChartDesc_Reserved2` | TField |  |  |
| 16 | `FS.GA.STATEMENTOFOP.CHART.DESC.RESERVED1` | `FsGaStatementofopChartDesc_Reserved1` | TField |  |  |
| 17 | `FS.GA.STATEMENTOFOP.CHART.DESC.LOCAL.REF` | `FsGaStatementofopChartDesc_LocalRef` |  |  |  |
| 18 | `FS.GA.STATEMENTOFOP.CHART.DESC.OVERRIDE` | `FsGaStatementofopChartDesc_Override` |  |  |  |
| 19 | `FS.GA.STATEMENTOFOP.CHART.DESC.RECORD.STATUS` | `FsGaStatementofopChartDesc_RecordStatus` | String |  |  |
| 20 | `FS.GA.STATEMENTOFOP.CHART.DESC.CURR.NO` | `FsGaStatementofopChartDesc_CurrNo` | String |  |  |
| 21 | `FS.GA.STATEMENTOFOP.CHART.DESC.INPUTTER` | `FsGaStatementofopChartDesc_Inputter` |  |  |  |
| 22 | `FS.GA.STATEMENTOFOP.CHART.DESC.DATE.TIME` | `FsGaStatementofopChartDesc_DateTime` |  |  |  |
| 23 | `FS.GA.STATEMENTOFOP.CHART.DESC.AUTHORISER` | `FsGaStatementofopChartDesc_Authoriser` | String |  |  |
| 24 | `FS.GA.STATEMENTOFOP.CHART.DESC.CO.CODE` | `FsGaStatementofopChartDesc_CoCode` | String |  |  |
| 25 | `FS.GA.STATEMENTOFOP.CHART.DESC.DEPT.CODE` | `FsGaStatementofopChartDesc_DeptCode` | String |  |  |
| 26 | `FS.GA.STATEMENTOFOP.CHART.DESC.AUDITOR.CODE` | `FsGaStatementofopChartDesc_AuditorCode` | String |  |  |
| 27 | `FS.GA.STATEMENTOFOP.CHART.DESC.AUDIT.DATE.TIME` | `FsGaStatementofopChartDesc_AuditDateTime` | String |  |  |
