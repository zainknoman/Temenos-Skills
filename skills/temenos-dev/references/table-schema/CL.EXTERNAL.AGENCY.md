# CL.EXTERNAL.AGENCY — Table Schema

> Source: `INSERTS/I_F.CL.EXTERNAL.AGENCY` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.EXTAG.AGENCY.NAME` | `ClExternalAgency_AgencyName` |  |  |  |
| 2 | `CL.EXTAG.CONTRACT.DATE` | `ClExternalAgency_ContractDate` | TField |  | Contract Date signed with the agency. |
| 3 | `CL.EXTAG.NO.OF.BRANCHES` | `ClExternalAgency_NoOfBranches` | TField |  | No of branches available for this agency. |
| 4 | `CL.EXTAG.OWNER.NAME` | `ClExternalAgency_OwnerName` |  |  |  |
| 5 | `CL.EXTAG.OWNER.MOBILE.PH` | `ClExternalAgency_OwnerMobilePh` | TField |  | Mobile no of the Agency Owner. |
| 6 | `CL.EXTAG.OWNER.ID` | `ClExternalAgency_OwnerId` | TField |  | Agnecy ID of the Agency Owner. |
| 7 | `CL.EXTAG.BRANCH.ID` | `ClExternalAgency_BranchId` |  |  |  |
| 8 | `CL.EXTAG.BRANCH.ADDR` | `ClExternalAgency_BranchAddr` |  |  |  |
| 9 | `CL.EXTAG.BRANCH.PH` | `ClExternalAgency_BranchPh` |  |  |  |
| 10 | `CL.EXTAG.FAX.NO` | `ClExternalAgency_FaxNo` |  |  |  |
| 11 | `CL.EXTAG.BRANCH.MGR` | `ClExternalAgency_BranchMgr` |  |  |  |
| 12 | `CL.EXTAG.BRANCH.MGR.MOB` | `ClExternalAgency_BranchMgrMob` |  |  |  |
| 13 | `CL.EXTAG.COMMISSION.PERC` | `ClExternalAgency_CommissionPerc` | TField |  | Commission Percentage is mentioned for APAY. |
| 14 | `CL.EXTAG.ASAL.OAMT.UPTO` | `ClExternalAgency_AsalOamtUpto` |  |  |  |
| 15 | `CL.EXTAG.ASAL.FLAT.COMM` | `ClExternalAgency_AsalFlatComm` |  |  |  |
| 16 | `CL.EXTAG.LOCAL.REF` | `ClExternalAgency_LocalRef` |  |  |  |
| 17 | `CL.EXTAG.RESERVED.5` | `ClExternalAgency_Reserved5` | TField |  |  |
| 18 | `CL.EXTAG.RESERVED.4` | `ClExternalAgency_Reserved4` | TField |  |  |
| 19 | `CL.EXTAG.RESERVED.3` | `ClExternalAgency_Reserved3` | TField |  |  |
| 20 | `CL.EXTAG.RESERVED.2` | `ClExternalAgency_Reserved2` | TField |  |  |
| 21 | `CL.EXTAG.RESERVED.1` | `ClExternalAgency_Reserved1` | TField |  |  |
| 22 | `CL.EXTAG.RECORD.STATUS` | `ClExternalAgency_RecordStatus` | String |  |  |
| 23 | `CL.EXTAG.CURR.NO` | `ClExternalAgency_CurrNo` | String |  |  |
| 24 | `CL.EXTAG.INPUTTER` | `ClExternalAgency_Inputter` |  |  |  |
| 25 | `CL.EXTAG.DATE.TIME` | `ClExternalAgency_DateTime` |  |  |  |
| 26 | `CL.EXTAG.AUTHORISER` | `ClExternalAgency_Authoriser` | String |  |  |
| 27 | `CL.EXTAG.CO.CODE` | `ClExternalAgency_CoCode` | String |  |  |
| 28 | `CL.EXTAG.DEPT.CODE` | `ClExternalAgency_DeptCode` | String |  |  |
| 29 | `CL.EXTAG.AUDITOR.CODE` | `ClExternalAgency_AuditorCode` | String |  |  |
| 30 | `CL.EXTAG.AUDIT.DATE.TIME` | `ClExternalAgency_AuditDateTime` | String |  |  |
