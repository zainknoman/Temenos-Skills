# EB.SCALABILITY.GROUPS — Table Schema

> Source: `INSERTS/I_F.EB.SCALABILITY.GROUPS` in `EB_InternalUtility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SCGR.DESCRIPTION` | `EbScalabilityGroups_Description` | TField |  |  |
| 2 | `EB.SCGR.SCALABILITY.STAGE` | `EbScalabilityGroups_ScalabilityStage` | TField |  |  |
| 3 | `EB.SCGR.IGNORE.APPLICATIONS` | `EbScalabilityGroups_IgnoreApplications` |  |  |  |
| 4 | `EB.SCGR.RESERVED.6` | `EbScalabilityGroups_Reserved6` | TField |  |  |
| 5 | `EB.SCGR.RESERVED.5` | `EbScalabilityGroups_Reserved5` | TField |  |  |
| 6 | `EB.SCGR.RESERVED.4` | `EbScalabilityGroups_Reserved4` | TField |  |  |
| 7 | `EB.SCGR.RESERVED.3` | `EbScalabilityGroups_Reserved3` | TField |  |  |
| 8 | `EB.SCGR.RESERVED.2` | `EbScalabilityGroups_Reserved2` | TField |  |  |
| 9 | `EB.SCGR.RESERVED.1` | `EbScalabilityGroups_Reserved1` | TField |  |  |
| 10 | `EB.SCGR.RECORD.STATUS` | `EbScalabilityGroups_RecordStatus` | String |  |  |
| 11 | `EB.SCGR.CURR.NO` | `EbScalabilityGroups_CurrNo` | String |  |  |
| 12 | `EB.SCGR.INPUTTER` | `EbScalabilityGroups_Inputter` |  |  |  |
| 13 | `EB.SCGR.DATE.TIME` | `EbScalabilityGroups_DateTime` |  |  |  |
| 14 | `EB.SCGR.AUTHORISER` | `EbScalabilityGroups_Authoriser` | String |  |  |
| 15 | `EB.SCGR.CO.CODE` | `EbScalabilityGroups_CoCode` | String |  |  |
| 16 | `EB.SCGR.DEPT.CODE` | `EbScalabilityGroups_DeptCode` | String |  |  |
| 17 | `EB.SCGR.AUDITOR.CODE` | `EbScalabilityGroups_AuditorCode` | String |  |  |
| 18 | `EB.SCGR.AUDIT.DATE.TIME` | `EbScalabilityGroups_AuditDateTime` | String |  |  |
