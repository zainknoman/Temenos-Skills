# UKCRSR.REPORT.GENERATION — Table Schema

> Source: `INSERTS/I_F.UKCRSR.REPORT.GENERATION` in `UKCRSR_CRSReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UKCRSR.REPORT.MESSAGE.CATEGORY` | `UkcrsrReportGeneration_MessageCategory` | TField |  |  |
| 2 | `UKCRSR.REPORT.XML.REFERENCE` | `UkcrsrReportGeneration_XmlReference` | TField |  |  |
| 3 | `UKCRSR.REPORT.RESERVED1` | `UkcrsrReportGeneration_Reserved1` | TField |  |  |
| 4 | `UKCRSR.REPORT.RESERVED2` | `UkcrsrReportGeneration_Reserved2` | TField |  |  |
| 5 | `UKCRSR.REPORT.RESERVED3` | `UkcrsrReportGeneration_Reserved3` | TField |  |  |
| 6 | `UKCRSR.REPORT.RESERVED4` | `UkcrsrReportGeneration_Reserved4` | TField |  |  |
| 7 | `UKCRSR.REPORT.RESERVED5` | `UkcrsrReportGeneration_Reserved5` | TField |  |  |
| 8 | `UKCRSR.REPORT.RESERVED6` | `UkcrsrReportGeneration_Reserved6` | TField |  |  |
| 9 | `UKCRSR.REPORT.RESERVED7` | `UkcrsrReportGeneration_Reserved7` | TField |  |  |
| 10 | `UKCRSR.REPORT.RESERVED8` | `UkcrsrReportGeneration_Reserved8` | TField |  |  |
| 11 | `UKCRSR.REPORT.RESERVED9` | `UkcrsrReportGeneration_Reserved9` | TField |  |  |
| 12 | `UKCRSR.REPORT.RESERVED10` | `UkcrsrReportGeneration_Reserved10` | TField |  |  |
| 13 | `UKCRSR.REPORT.OVERRIDE` | `UkcrsrReportGeneration_Override` |  |  |  |
| 14 | `UKCRSR.REPORT.RECORD.STATUS` | `UkcrsrReportGeneration_RecordStatus` | String |  |  |
| 15 | `UKCRSR.REPORT.CURR.NO` | `UkcrsrReportGeneration_CurrNo` | String |  |  |
| 16 | `UKCRSR.REPORT.INPUTTER` | `UkcrsrReportGeneration_Inputter` |  |  |  |
| 17 | `UKCRSR.REPORT.DATE.TIME` | `UkcrsrReportGeneration_DateTime` |  |  |  |
| 18 | `UKCRSR.REPORT.AUTHORISER` | `UkcrsrReportGeneration_Authoriser` | String |  |  |
| 19 | `UKCRSR.REPORT.CO.CODE` | `UkcrsrReportGeneration_CoCode` | String |  |  |
| 20 | `UKCRSR.REPORT.DEPT.CODE` | `UkcrsrReportGeneration_DeptCode` | String |  |  |
| 21 | `UKCRSR.REPORT.AUDITOR.CODE` | `UkcrsrReportGeneration_AuditorCode` | String |  |  |
| 22 | `UKCRSR.REPORT.AUDIT.DATE.TIME` | `UkcrsrReportGeneration_AuditDateTime` | String |  |  |
