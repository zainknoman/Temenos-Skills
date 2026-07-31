# EB.SCALABILITY.JOBS — Table Schema

> Source: `INSERTS/I_F.EB.SCALABILITY.JOBS` in `EB_InternalUtility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SCJO.DESCRIPTION` | `EbScalabilityJobs_Description` | TField |  |  |
| 2 | `EB.SCJO.SCALABILITY.GROUPS` | `EbScalabilityJobs_ScalabilityGroups` |  |  |  |
| 3 | `EB.SCJO.RESERVED.8` | `EbScalabilityJobs_Reserved8` | TField |  |  |
| 4 | `EB.SCJO.RESERVED.7` | `EbScalabilityJobs_Reserved7` | TField |  |  |
| 5 | `EB.SCJO.RESERVED.6` | `EbScalabilityJobs_Reserved6` | TField |  |  |
| 6 | `EB.SCJO.RESERVED.5` | `EbScalabilityJobs_Reserved5` | TField |  |  |
| 7 | `EB.SCJO.RESERVED.4` | `EbScalabilityJobs_Reserved4` | TField |  |  |
| 8 | `EB.SCJO.RESERVED.3` | `EbScalabilityJobs_Reserved3` | TField |  |  |
| 9 | `EB.SCJO.RESERVED.2` | `EbScalabilityJobs_Reserved2` | TField |  |  |
| 10 | `EB.SCJO.RESERVED.1` | `EbScalabilityJobs_Reserved1` | TField |  |  |
| 11 | `EB.SCJO.RECORD.STATUS` | `EbScalabilityJobs_RecordStatus` | String |  |  |
| 12 | `EB.SCJO.CURR.NO` | `EbScalabilityJobs_CurrNo` | String |  |  |
| 13 | `EB.SCJO.INPUTTER` | `EbScalabilityJobs_Inputter` |  |  |  |
| 14 | `EB.SCJO.DATE.TIME` | `EbScalabilityJobs_DateTime` |  |  |  |
| 15 | `EB.SCJO.AUTHORISER` | `EbScalabilityJobs_Authoriser` | String |  |  |
| 16 | `EB.SCJO.CO.CODE` | `EbScalabilityJobs_CoCode` | String |  |  |
| 17 | `EB.SCJO.DEPT.CODE` | `EbScalabilityJobs_DeptCode` | String |  |  |
| 18 | `EB.SCJO.AUDITOR.CODE` | `EbScalabilityJobs_AuditorCode` | String |  |  |
| 19 | `EB.SCJO.AUDIT.DATE.TIME` | `EbScalabilityJobs_AuditDateTime` | String |  |  |
