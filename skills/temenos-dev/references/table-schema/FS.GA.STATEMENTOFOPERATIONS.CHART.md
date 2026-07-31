# FS.GA.STATEMENTOFOPERATIONS.CHART — Table Schema

> Source: `INSERTS/I_F.FS.GA.STATEMENTOFOPERATIONS.CHART` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.STATEMENTOFOPERATIONS.CHART.PARENT.REF.ID` | `FsGaStatementofoperationsChart_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.STATEMENTOFOPERATIONS.CHART.ORA.ROWID` | `FsGaStatementofoperationsChart_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.STATEMENTOFOPERATIONS.CHART.CHART.OF.ACCOUNTS.CODE` | `FsGaStatementofoperationsChart_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.STATEMENTOFOPERATIONS.CHART.GL.ACCOUNT` | `FsGaStatementofoperationsChart_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.STATEMENTOFOPERATIONS.CHART.BS.GROUPING` | `FsGaStatementofoperationsChart_BsGrouping` | TField |  | Balance sheet grouping like Assets, Liabilities etc Multifonds DB Column is CTIF. |
| 6 | `FS.GA.STATEMENTOFOPERATIONS.CHART.DESCRIPTION` | `FsGaStatementofoperationsChart_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GA.STATEMENTOFOPERATIONS.CHART.BS.SUB.GROUPING` | `FsGaStatementofoperationsChart_BsSubGrouping` | TField |  | Balance sheet sub grouping Multifonds DB Column is CTIF2. |
| 8 | `FS.GA.STATEMENTOFOPERATIONS.CHART.DETAIL.OR.TOTAL` | `FsGaStatementofoperationsChart_DetailOrTotal` | TField |  | Detailed or Total information Multifonds DB Column is CDTOT. |
| 9 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RESERVED10` | `FsGaStatementofoperationsChart_Reserved10` | TField |  |  |
| 10 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RESERVED9` | `FsGaStatementofoperationsChart_Reserved9` | TField |  |  |
| 11 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RESERVED8` | `FsGaStatementofoperationsChart_Reserved8` | TField |  |  |
| 12 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RESERVED7` | `FsGaStatementofoperationsChart_Reserved7` | TField |  |  |
| 13 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RESERVED6` | `FsGaStatementofoperationsChart_Reserved6` | TField |  |  |
| 14 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RESERVED5` | `FsGaStatementofoperationsChart_Reserved5` | TField |  |  |
| 15 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RESERVED4` | `FsGaStatementofoperationsChart_Reserved4` | TField |  |  |
| 16 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RESERVED3` | `FsGaStatementofoperationsChart_Reserved3` | TField |  |  |
| 17 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RESERVED2` | `FsGaStatementofoperationsChart_Reserved2` | TField |  |  |
| 18 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RESERVED1` | `FsGaStatementofoperationsChart_Reserved1` | TField |  |  |
| 19 | `FS.GA.STATEMENTOFOPERATIONS.CHART.LOCAL.REF` | `FsGaStatementofoperationsChart_LocalRef` |  |  |  |
| 20 | `FS.GA.STATEMENTOFOPERATIONS.CHART.OVERRIDE` | `FsGaStatementofoperationsChart_Override` |  |  |  |
| 21 | `FS.GA.STATEMENTOFOPERATIONS.CHART.RECORD.STATUS` | `FsGaStatementofoperationsChart_RecordStatus` | String |  |  |
| 22 | `FS.GA.STATEMENTOFOPERATIONS.CHART.CURR.NO` | `FsGaStatementofoperationsChart_CurrNo` | String |  |  |
| 23 | `FS.GA.STATEMENTOFOPERATIONS.CHART.INPUTTER` | `FsGaStatementofoperationsChart_Inputter` |  |  |  |
| 24 | `FS.GA.STATEMENTOFOPERATIONS.CHART.DATE.TIME` | `FsGaStatementofoperationsChart_DateTime` |  |  |  |
| 25 | `FS.GA.STATEMENTOFOPERATIONS.CHART.AUTHORISER` | `FsGaStatementofoperationsChart_Authoriser` | String |  |  |
| 26 | `FS.GA.STATEMENTOFOPERATIONS.CHART.CO.CODE` | `FsGaStatementofoperationsChart_CoCode` | String |  |  |
| 27 | `FS.GA.STATEMENTOFOPERATIONS.CHART.DEPT.CODE` | `FsGaStatementofoperationsChart_DeptCode` | String |  |  |
| 28 | `FS.GA.STATEMENTOFOPERATIONS.CHART.AUDITOR.CODE` | `FsGaStatementofoperationsChart_AuditorCode` | String |  |  |
| 29 | `FS.GA.STATEMENTOFOPERATIONS.CHART.AUDIT.DATE.TIME` | `FsGaStatementofoperationsChart_AuditDateTime` | String |  |  |
