# FS.ACCOUNTING.CHART — Table Schema

> Source: `INSERTS/I_F.FS.ACCOUNTING.CHART` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ACCOUNTING.CHART.DESCRIPTION` | `FsAccountingChart_Description` |  |  |  |
| 2 | `FS.ACCOUNTING.CHART.FILTER.KEY` | `FsAccountingChart_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ACCOUNTING.CHART.RECORD.ID` | `FsAccountingChart_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ACCOUNTING.CHART.RESERVED10` | `FsAccountingChart_Reserved10` | TField |  |  |
| 5 | `FS.ACCOUNTING.CHART.RESERVED9` | `FsAccountingChart_Reserved9` | TField |  |  |
| 6 | `FS.ACCOUNTING.CHART.RESERVED8` | `FsAccountingChart_Reserved8` | TField |  |  |
| 7 | `FS.ACCOUNTING.CHART.RESERVED7` | `FsAccountingChart_Reserved7` | TField |  |  |
| 8 | `FS.ACCOUNTING.CHART.RESERVED6` | `FsAccountingChart_Reserved6` | TField |  |  |
| 9 | `FS.ACCOUNTING.CHART.RESERVED5` | `FsAccountingChart_Reserved5` | TField |  |  |
| 10 | `FS.ACCOUNTING.CHART.RESERVED4` | `FsAccountingChart_Reserved4` | TField |  |  |
| 11 | `FS.ACCOUNTING.CHART.RESERVED3` | `FsAccountingChart_Reserved3` | TField |  |  |
| 12 | `FS.ACCOUNTING.CHART.RESERVED2` | `FsAccountingChart_Reserved2` | TField |  |  |
| 13 | `FS.ACCOUNTING.CHART.RESERVED1` | `FsAccountingChart_Reserved1` | TField |  |  |
| 14 | `FS.ACCOUNTING.CHART.LOCAL.REF` | `FsAccountingChart_LocalRef` |  |  |  |
| 15 | `FS.ACCOUNTING.CHART.OVERRIDE` | `FsAccountingChart_Override` |  |  |  |
| 16 | `FS.ACCOUNTING.CHART.RECORD.STATUS` | `FsAccountingChart_RecordStatus` | String |  |  |
| 17 | `FS.ACCOUNTING.CHART.CURR.NO` | `FsAccountingChart_CurrNo` | String |  |  |
| 18 | `FS.ACCOUNTING.CHART.INPUTTER` | `FsAccountingChart_Inputter` |  |  |  |
| 19 | `FS.ACCOUNTING.CHART.DATE.TIME` | `FsAccountingChart_DateTime` |  |  |  |
| 20 | `FS.ACCOUNTING.CHART.AUTHORISER` | `FsAccountingChart_Authoriser` | String |  |  |
| 21 | `FS.ACCOUNTING.CHART.CO.CODE` | `FsAccountingChart_CoCode` | String |  |  |
| 22 | `FS.ACCOUNTING.CHART.DEPT.CODE` | `FsAccountingChart_DeptCode` | String |  |  |
| 23 | `FS.ACCOUNTING.CHART.AUDITOR.CODE` | `FsAccountingChart_AuditorCode` | String |  |  |
| 24 | `FS.ACCOUNTING.CHART.AUDIT.DATE.TIME` | `FsAccountingChart_AuditDateTime` | String |  |  |
