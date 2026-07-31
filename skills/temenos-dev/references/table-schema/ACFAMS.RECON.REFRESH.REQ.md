# ACFAMS.RECON.REFRESH.REQ — Table Schema

> Source: `INSERTS/I_F.ACFAMS.RECON.REFRESH.REQ` in `ACFAMS_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACFAMS.REF.RECON.CASE.NAME` | `AcfamsReconRefreshReq_ReconCaseName` | TField |  | Id of the reconciliation case to be refreshed. |
| 2 | `ACFAMS.REF.BUSINESS.OBJECT.ID` | `AcfamsReconRefreshReq_BusinessObjectId` | TField |  | The business object id for which the refresh of data is required e.g. the arrangement number. |
| 3 | `ACFAMS.REF.RECON.RESULT.ID` | `AcfamsReconRefreshReq_ReconResultId` | TField |  | The id of the reconciliation result that has required the refresh of data. |
| 4 | `ACFAMS.REF.REFRESH.NOTES` | `AcfamsReconRefreshReq_RefreshNotes` | TField |  | Text field to allow any additional description of the refresh. |
| 5 | `ACFAMS.REF.CREATE.DATE.TIME` | `AcfamsReconRefreshReq_CreateDateTime` |  |  |  |
| 6 | `ACFAMS.REF.RESERVED.5` | `AcfamsReconRefreshReq_Reserved5` | TField |  |  |
| 7 | `ACFAMS.REF.RESERVED.4` | `AcfamsReconRefreshReq_Reserved4` | TField |  |  |
| 8 | `ACFAMS.REF.RESERVED.3` | `AcfamsReconRefreshReq_Reserved3` | TField |  |  |
| 9 | `ACFAMS.REF.RESERVED.2` | `AcfamsReconRefreshReq_Reserved2` | TField |  |  |
| 10 | `ACFAMS.REF.RESERVED.1` | `AcfamsReconRefreshReq_Reserved1` | TField |  |  |
| 11 | `ACFAMS.REF.LOCAL.REF` | `AcfamsReconRefreshReq_LocalRef` |  |  |  |
| 12 | `ACFAMS.REF.OVERRIDE` | `AcfamsReconRefreshReq_Override` |  |  |  |
| 13 | `ACFAMS.REF.RECORD.STATUS` | `AcfamsReconRefreshReq_RecordStatus` | String |  |  |
| 14 | `ACFAMS.REF.CURR.NO` | `AcfamsReconRefreshReq_CurrNo` | String |  |  |
| 15 | `ACFAMS.REF.INPUTTER` | `AcfamsReconRefreshReq_Inputter` |  |  |  |
| 16 | `ACFAMS.REF.DATE.TIME` | `AcfamsReconRefreshReq_DateTime` |  |  |  |
| 17 | `ACFAMS.REF.AUTHORISER` | `AcfamsReconRefreshReq_Authoriser` | String |  |  |
| 18 | `ACFAMS.REF.CO.CODE` | `AcfamsReconRefreshReq_CoCode` | String |  |  |
| 19 | `ACFAMS.REF.DEPT.CODE` | `AcfamsReconRefreshReq_DeptCode` | String |  |  |
| 20 | `ACFAMS.REF.AUDITOR.CODE` | `AcfamsReconRefreshReq_AuditorCode` | String |  |  |
| 21 | `ACFAMS.REF.AUDIT.DATE.TIME` | `AcfamsReconRefreshReq_AuditDateTime` | String |  |  |
