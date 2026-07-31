# FS.GA.IML.EQUIVALENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.IML.EQUIVALENT` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.IML.EQUIVALENT.CHART.OF.ACCOUNTS.CODE` | `FsGaImlEquivalent_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 2 | `FS.GA.IML.EQUIVALENT.GL.ACCOUNT` | `FsGaImlEquivalent_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 3 | `FS.GA.IML.EQUIVALENT.LANGUAGE` | `FsGaImlEquivalent_Language` | TField |  | Language used for defining correspondent details Multifonds DB Column is CLANGUE. |
| 4 | `FS.GA.IML.EQUIVALENT.LONG.DESC` | `FsGaImlEquivalent_LongDesc` | TField |  | This represents description of a report, export type, language name etc Multifonds DB Column is LIBELLE. |
| 5 | `FS.GA.IML.EQUIVALENT.RESERVED10` | `FsGaImlEquivalent_Reserved10` | TField |  |  |
| 6 | `FS.GA.IML.EQUIVALENT.RESERVED9` | `FsGaImlEquivalent_Reserved9` | TField |  |  |
| 7 | `FS.GA.IML.EQUIVALENT.RESERVED8` | `FsGaImlEquivalent_Reserved8` | TField |  |  |
| 8 | `FS.GA.IML.EQUIVALENT.RESERVED7` | `FsGaImlEquivalent_Reserved7` | TField |  |  |
| 9 | `FS.GA.IML.EQUIVALENT.RESERVED6` | `FsGaImlEquivalent_Reserved6` | TField |  |  |
| 10 | `FS.GA.IML.EQUIVALENT.RESERVED5` | `FsGaImlEquivalent_Reserved5` | TField |  |  |
| 11 | `FS.GA.IML.EQUIVALENT.RESERVED4` | `FsGaImlEquivalent_Reserved4` | TField |  |  |
| 12 | `FS.GA.IML.EQUIVALENT.RESERVED3` | `FsGaImlEquivalent_Reserved3` | TField |  |  |
| 13 | `FS.GA.IML.EQUIVALENT.RESERVED2` | `FsGaImlEquivalent_Reserved2` | TField |  |  |
| 14 | `FS.GA.IML.EQUIVALENT.RESERVED1` | `FsGaImlEquivalent_Reserved1` | TField |  |  |
| 15 | `FS.GA.IML.EQUIVALENT.RECORD.STATUS` | `FsGaImlEquivalent_RecordStatus` | String |  |  |
| 16 | `FS.GA.IML.EQUIVALENT.CURR.NO` | `FsGaImlEquivalent_CurrNo` | String |  |  |
| 17 | `FS.GA.IML.EQUIVALENT.INPUTTER` | `FsGaImlEquivalent_Inputter` |  |  |  |
| 18 | `FS.GA.IML.EQUIVALENT.DATE.TIME` | `FsGaImlEquivalent_DateTime` |  |  |  |
| 19 | `FS.GA.IML.EQUIVALENT.AUTHORISER` | `FsGaImlEquivalent_Authoriser` | String |  |  |
| 20 | `FS.GA.IML.EQUIVALENT.CO.CODE` | `FsGaImlEquivalent_CoCode` | String |  |  |
| 21 | `FS.GA.IML.EQUIVALENT.DEPT.CODE` | `FsGaImlEquivalent_DeptCode` | String |  |  |
| 22 | `FS.GA.IML.EQUIVALENT.AUDITOR.CODE` | `FsGaImlEquivalent_AuditorCode` | String |  |  |
| 23 | `FS.GA.IML.EQUIVALENT.AUDIT.DATE.TIME` | `FsGaImlEquivalent_AuditDateTime` | String |  |  |
