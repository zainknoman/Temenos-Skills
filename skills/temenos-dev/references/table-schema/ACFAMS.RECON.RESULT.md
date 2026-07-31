# ACFAMS.RECON.RESULT — Table Schema

> Source: `INSERTS/I_F.ACFAMS.RECON.RESULT` in `ACFAMS_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACFAMS.RES.RECONC.CASE.NAME` | `AcfamsReconResult_ReconcCaseName` | TField |  | ID of the reconciliation case that generated the result. |
| 2 | `ACFAMS.RES.CREATE.DATE.TIME` | `AcfamsReconResult_CreateDateTime` |  |  |  |
| 3 | `ACFAMS.RES.RUN.ID` | `AcfamsReconResult_RunId` | TField |  | Holds the reference that identifies the reconciliation run. The Run ID is formed from the Sequence Number of the run, bank date when initiated. |
| 4 | `ACFAMS.RES.BUSINESS.OBJECT.COMPANY` | `AcfamsReconResult_BusinessObjectCompany` | TField |  | The company Id of the business object. |
| 5 | `ACFAMS.RES.BUSINESS.OBJECT.ID` | `AcfamsReconResult_BusinessObjectId` | TField |  | The business object id. |
| 6 | `ACFAMS.RES.MATCHING.RESULT` | `AcfamsReconResult_MatchingResult` | TField |  | Identifies the result of the comparison will be MATCHED/UNMATCHED. |
| 7 | `ACFAMS.RES.LEFT.SIDE.COMPARISON.DATA` | `AcfamsReconResult_LeftSideComparisonData` | TField |  | Serialized data retrieved from left retriever method. |
| 8 | `ACFAMS.RES.RIGHT.SIDE.COMPARISON.DATA` | `AcfamsReconResult_RightSideComparisonData` | TField |  | Serialized data retrieved from right retriever method. |
| 9 | `ACFAMS.RES.UNMATCHED.STATUS` | `AcfamsReconResult_UnmatchedStatus` | TField |  | The status of the unmatched record used to reflect the investigation process. Status vales can be created by the bank through EB.LOOKUP. |
| 10 | `ACFAMS.RES.UNMATCHED.REASON` | `AcfamsReconResult_UnmatchedReason` | TField |  | A text field allowing a description of the cause and corrective actions to be recorded. |
| 11 | `ACFAMS.RES.RESERVED.5` | `AcfamsReconResult_Reserved5` | TField |  |  |
| 12 | `ACFAMS.RES.RESERVED.4` | `AcfamsReconResult_Reserved4` | TField |  |  |
| 13 | `ACFAMS.RES.RESERVED.3` | `AcfamsReconResult_Reserved3` | TField |  |  |
| 14 | `ACFAMS.RES.RESERVED.2` | `AcfamsReconResult_Reserved2` | TField |  |  |
| 15 | `ACFAMS.RES.RESERVED.1` | `AcfamsReconResult_Reserved1` | TField |  |  |
| 16 | `ACFAMS.RES.LOCAL.REF` | `AcfamsReconResult_LocalRef` |  |  |  |
| 17 | `ACFAMS.RES.OVERRIDE` | `AcfamsReconResult_Override` |  |  |  |
| 18 | `ACFAMS.RES.RECORD.STATUS` | `AcfamsReconResult_RecordStatus` | String |  |  |
| 19 | `ACFAMS.RES.CURR.NO` | `AcfamsReconResult_CurrNo` | String |  |  |
| 20 | `ACFAMS.RES.INPUTTER` | `AcfamsReconResult_Inputter` |  |  |  |
| 21 | `ACFAMS.RES.DATE.TIME` | `AcfamsReconResult_DateTime` |  |  |  |
| 22 | `ACFAMS.RES.AUTHORISER` | `AcfamsReconResult_Authoriser` | String |  |  |
| 23 | `ACFAMS.RES.CO.CODE` | `AcfamsReconResult_CoCode` | String |  |  |
| 24 | `ACFAMS.RES.DEPT.CODE` | `AcfamsReconResult_DeptCode` | String |  |  |
| 25 | `ACFAMS.RES.AUDITOR.CODE` | `AcfamsReconResult_AuditorCode` | String |  |  |
| 26 | `ACFAMS.RES.AUDIT.DATE.TIME` | `AcfamsReconResult_AuditDateTime` | String |  |  |
