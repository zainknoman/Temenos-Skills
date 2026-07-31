# FS.GA.NAVCHART.DESCRIPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAVCHART.DESCRIPTION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAVCHART.DESCRIPTION.PARENT.REF.ID` | `FsGaNavchartDescription_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAVCHART.DESCRIPTION.ORA.ROWID` | `FsGaNavchartDescription_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAVCHART.DESCRIPTION.CHART.OF.ACCOUNTS.CODE` | `FsGaNavchartDescription_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 4 | `FS.GA.NAVCHART.DESCRIPTION.GL.ACCOUNT` | `FsGaNavchartDescription_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.NAVCHART.DESCRIPTION.LANGUAGE` | `FsGaNavchartDescription_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 6 | `FS.GA.NAVCHART.DESCRIPTION.DESCRIPTION` | `FsGaNavchartDescription_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 7 | `FS.GA.NAVCHART.DESCRIPTION.RESERVED10` | `FsGaNavchartDescription_Reserved10` | TField |  |  |
| 8 | `FS.GA.NAVCHART.DESCRIPTION.RESERVED9` | `FsGaNavchartDescription_Reserved9` | TField |  |  |
| 9 | `FS.GA.NAVCHART.DESCRIPTION.RESERVED8` | `FsGaNavchartDescription_Reserved8` | TField |  |  |
| 10 | `FS.GA.NAVCHART.DESCRIPTION.RESERVED7` | `FsGaNavchartDescription_Reserved7` | TField |  |  |
| 11 | `FS.GA.NAVCHART.DESCRIPTION.RESERVED6` | `FsGaNavchartDescription_Reserved6` | TField |  |  |
| 12 | `FS.GA.NAVCHART.DESCRIPTION.RESERVED5` | `FsGaNavchartDescription_Reserved5` | TField |  |  |
| 13 | `FS.GA.NAVCHART.DESCRIPTION.RESERVED4` | `FsGaNavchartDescription_Reserved4` | TField |  |  |
| 14 | `FS.GA.NAVCHART.DESCRIPTION.RESERVED3` | `FsGaNavchartDescription_Reserved3` | TField |  |  |
| 15 | `FS.GA.NAVCHART.DESCRIPTION.RESERVED2` | `FsGaNavchartDescription_Reserved2` | TField |  |  |
| 16 | `FS.GA.NAVCHART.DESCRIPTION.RESERVED1` | `FsGaNavchartDescription_Reserved1` | TField |  |  |
| 17 | `FS.GA.NAVCHART.DESCRIPTION.LOCAL.REF` | `FsGaNavchartDescription_LocalRef` |  |  |  |
| 18 | `FS.GA.NAVCHART.DESCRIPTION.OVERRIDE` | `FsGaNavchartDescription_Override` |  |  |  |
| 19 | `FS.GA.NAVCHART.DESCRIPTION.RECORD.STATUS` | `FsGaNavchartDescription_RecordStatus` | String |  |  |
| 20 | `FS.GA.NAVCHART.DESCRIPTION.CURR.NO` | `FsGaNavchartDescription_CurrNo` | String |  |  |
| 21 | `FS.GA.NAVCHART.DESCRIPTION.INPUTTER` | `FsGaNavchartDescription_Inputter` |  |  |  |
| 22 | `FS.GA.NAVCHART.DESCRIPTION.DATE.TIME` | `FsGaNavchartDescription_DateTime` |  |  |  |
| 23 | `FS.GA.NAVCHART.DESCRIPTION.AUTHORISER` | `FsGaNavchartDescription_Authoriser` | String |  |  |
| 24 | `FS.GA.NAVCHART.DESCRIPTION.CO.CODE` | `FsGaNavchartDescription_CoCode` | String |  |  |
| 25 | `FS.GA.NAVCHART.DESCRIPTION.DEPT.CODE` | `FsGaNavchartDescription_DeptCode` | String |  |  |
| 26 | `FS.GA.NAVCHART.DESCRIPTION.AUDITOR.CODE` | `FsGaNavchartDescription_AuditorCode` | String |  |  |
| 27 | `FS.GA.NAVCHART.DESCRIPTION.AUDIT.DATE.TIME` | `FsGaNavchartDescription_AuditDateTime` | String |  |  |
