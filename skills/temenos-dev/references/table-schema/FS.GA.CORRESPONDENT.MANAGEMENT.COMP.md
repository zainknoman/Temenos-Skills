# FS.GA.CORRESPONDENT.MANAGEMENT.COMP — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORRESPONDENT.MANAGEMENT.COMP` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CORRESPONDENT.MANAGEMENT.COMP.CORRESPONDENT.NUMBER` | `FsGaCorrespondentManagementComp_CorrespondentNumber` | TField |  | Correspondent Number Multifonds DB Column is NCORRESP. |
| 2 | `CORRESPONDENT.MANAGEMENT.COMP.MGMT.COMPANY.CORRESPONDENT` | `FsGaCorrespondentManagementComp_MgmtCompanyCorrespondent` | TField |  | Mgmt company correspondent Multifonds DB Column is NCORRESP_COMP. |
| 3 | `CORRESPONDENT.MANAGEMENT.COMP.COMPANY.TYPE` | `FsGaCorrespondentManagementComp_CompanyType` | TField |  | Company Type Multifonds DB Column is TYP_MCPNY. |
| 4 | `CORRESPONDENT.MANAGEMENT.COMP.DWH.EXPORT` | `FsGaCorrespondentManagementComp_DwhExport` | TField |  | DWH Export Multifonds DB Column is DWH_EXPORT. |
| 5 | `CORRESPONDENT.MANAGEMENT.COMP.RECORD.STATUS` | `FsGaCorrespondentManagementComp_RecordStatus` | String |  |  |
| 6 | `CORRESPONDENT.MANAGEMENT.COMP.CURR.NO` | `FsGaCorrespondentManagementComp_CurrNo` | String |  |  |
| 7 | `CORRESPONDENT.MANAGEMENT.COMP.INPUTTER` | `FsGaCorrespondentManagementComp_Inputter` |  |  |  |
| 8 | `CORRESPONDENT.MANAGEMENT.COMP.DATE.TIME` | `FsGaCorrespondentManagementComp_DateTime` |  |  |  |
| 9 | `CORRESPONDENT.MANAGEMENT.COMP.AUTHORISER` | `FsGaCorrespondentManagementComp_Authoriser` | String |  |  |
| 10 | `CORRESPONDENT.MANAGEMENT.COMP.CO.CODE` | `FsGaCorrespondentManagementComp_CoCode` | String |  |  |
| 11 | `CORRESPONDENT.MANAGEMENT.COMP.DEPT.CODE` | `FsGaCorrespondentManagementComp_DeptCode` | String |  |  |
| 12 | `CORRESPONDENT.MANAGEMENT.COMP.AUDITOR.CODE` | `FsGaCorrespondentManagementComp_AuditorCode` | String |  |  |
| 13 | `CORRESPONDENT.MANAGEMENT.COMP.AUDIT.DATE.TIME` | `FsGaCorrespondentManagementComp_AuditDateTime` | String |  |  |
