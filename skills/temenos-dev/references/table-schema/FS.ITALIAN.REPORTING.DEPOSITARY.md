# FS.ITALIAN.REPORTING.DEPOSITARY — Table Schema

> Source: `INSERTS/I_F.FS.ITALIAN.REPORTING.DEPOSITARY` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ITALIAN.REPORTING.DEPOSITARY.DESCRIPTION` | `FsItalianReportingDepositary_Description` |  |  |  |
| 2 | `FS.ITALIAN.REPORTING.DEPOSITARY.FILTER.KEY` | `FsItalianReportingDepositary_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ITALIAN.REPORTING.DEPOSITARY.RECORD.ID` | `FsItalianReportingDepositary_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ITALIAN.REPORTING.DEPOSITARY.RESERVED10` | `FsItalianReportingDepositary_Reserved10` | TField |  |  |
| 5 | `FS.ITALIAN.REPORTING.DEPOSITARY.RESERVED9` | `FsItalianReportingDepositary_Reserved9` | TField |  |  |
| 6 | `FS.ITALIAN.REPORTING.DEPOSITARY.RESERVED8` | `FsItalianReportingDepositary_Reserved8` | TField |  |  |
| 7 | `FS.ITALIAN.REPORTING.DEPOSITARY.RESERVED7` | `FsItalianReportingDepositary_Reserved7` | TField |  |  |
| 8 | `FS.ITALIAN.REPORTING.DEPOSITARY.RESERVED6` | `FsItalianReportingDepositary_Reserved6` | TField |  |  |
| 9 | `FS.ITALIAN.REPORTING.DEPOSITARY.RESERVED5` | `FsItalianReportingDepositary_Reserved5` | TField |  |  |
| 10 | `FS.ITALIAN.REPORTING.DEPOSITARY.RESERVED4` | `FsItalianReportingDepositary_Reserved4` | TField |  |  |
| 11 | `FS.ITALIAN.REPORTING.DEPOSITARY.RESERVED3` | `FsItalianReportingDepositary_Reserved3` | TField |  |  |
| 12 | `FS.ITALIAN.REPORTING.DEPOSITARY.RESERVED2` | `FsItalianReportingDepositary_Reserved2` | TField |  |  |
| 13 | `FS.ITALIAN.REPORTING.DEPOSITARY.RESERVED1` | `FsItalianReportingDepositary_Reserved1` | TField |  |  |
| 14 | `FS.ITALIAN.REPORTING.DEPOSITARY.LOCAL.REF` | `FsItalianReportingDepositary_LocalRef` |  |  |  |
| 15 | `FS.ITALIAN.REPORTING.DEPOSITARY.OVERRIDE` | `FsItalianReportingDepositary_Override` |  |  |  |
| 16 | `FS.ITALIAN.REPORTING.DEPOSITARY.RECORD.STATUS` | `FsItalianReportingDepositary_RecordStatus` | String |  |  |
| 17 | `FS.ITALIAN.REPORTING.DEPOSITARY.CURR.NO` | `FsItalianReportingDepositary_CurrNo` | String |  |  |
| 18 | `FS.ITALIAN.REPORTING.DEPOSITARY.INPUTTER` | `FsItalianReportingDepositary_Inputter` |  |  |  |
| 19 | `FS.ITALIAN.REPORTING.DEPOSITARY.DATE.TIME` | `FsItalianReportingDepositary_DateTime` |  |  |  |
| 20 | `FS.ITALIAN.REPORTING.DEPOSITARY.AUTHORISER` | `FsItalianReportingDepositary_Authoriser` | String |  |  |
| 21 | `FS.ITALIAN.REPORTING.DEPOSITARY.CO.CODE` | `FsItalianReportingDepositary_CoCode` | String |  |  |
| 22 | `FS.ITALIAN.REPORTING.DEPOSITARY.DEPT.CODE` | `FsItalianReportingDepositary_DeptCode` | String |  |  |
| 23 | `FS.ITALIAN.REPORTING.DEPOSITARY.AUDITOR.CODE` | `FsItalianReportingDepositary_AuditorCode` | String |  |  |
| 24 | `FS.ITALIAN.REPORTING.DEPOSITARY.AUDIT.DATE.TIME` | `FsItalianReportingDepositary_AuditDateTime` | String |  |  |
