# FS.GA.STEP.SUBMIT.RESET — Table Schema

> Source: `INSERTS/I_F.FS.GA.STEP.SUBMIT.RESET` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STEP.SUBMIT.TYPE` | `FsGaStepSubmitReset_Type` | TField |  | TYPE Multifonds DB Column is P_TYPE. |
| 2 | `STEP.SUBMIT.FACET` | `FsGaStepSubmitReset_Facet` | TField |  | FACET Multifonds DB Column is P_FACET. |
| 3 | `STEP.SUBMIT.STEP.ID` | `FsGaStepSubmitReset_StepId` | TField |  | STEP.ID Multifonds DB Column is P_STEP_ID. |
| 4 | `STEP.SUBMIT.FAMILY.ID` | `FsGaStepSubmitReset_FamilyId` | TField |  | FAMILY.ID Multifonds DB Column is P_FAMILY_ID. |
| 5 | `STEP.SUBMIT.TASK.ID` | `FsGaStepSubmitReset_TaskId` | TField |  | TASK.ID. Multifonds DB Column is P_TASK_ID. |
| 6 | `STEP.SUBMIT.STEP.TASK.ID` | `FsGaStepSubmitReset_StepTaskId` | TField |  | STEP.TASK.ID Multifonds DB Column is P_STEP_TASK_ID. |
| 7 | `STEP.SUBMIT.NAV.DATE` | `FsGaStepSubmitReset_NavDate` | TField |  | NAV.DATE Multifonds DB Column is P_NAV_DATE. |
| 8 | `STEP.SUBMIT.CODE.PROCESS` | `FsGaStepSubmitReset_CodeProcess` | TField |  | CODE.PROCESS Multifonds DB Column is P_CODE_PROCESS. |
| 9 | `STEP.SUBMIT.USER.ID` | `FsGaStepSubmitReset_UserId` | TField |  | STEP.TASK.ID Multifonds DB Column is P_USER_ID. |
| 10 | `STEP.SUBMIT.NAV.GROUP` | `FsGaStepSubmitReset_NavGroup` | TField |  | STEP.TASK.ID Multifonds DB Column is P_NAVGROUP. |
| 11 | `STEP.SUBMIT.FUND.ID` | `FsGaStepSubmitReset_FundId` | TField |  | FUND.ID Multifonds DB Column is P_FUND_ID. |
| 12 | `STEP.SUBMIT.RESERVED5` | `FsGaStepSubmitReset_Reserved5` | TField |  |  |
| 13 | `STEP.SUBMIT.RESERVED4` | `FsGaStepSubmitReset_Reserved4` | TField |  |  |
| 14 | `STEP.SUBMIT.RESERVED3` | `FsGaStepSubmitReset_Reserved3` | TField |  |  |
| 15 | `STEP.SUBMIT.RESERVED2` | `FsGaStepSubmitReset_Reserved2` | TField |  |  |
| 16 | `STEP.SUBMIT.RESERVED1` | `FsGaStepSubmitReset_Reserved1` | TField |  |  |
| 17 | `STEP.SUBMIT.LOCAL.REF` | `FsGaStepSubmitReset_LocalRef` |  |  |  |
| 18 | `STEP.SUBMIT.OVERRIDE` | `FsGaStepSubmitReset_Override` |  |  |  |
| 19 | `STEP.SUBMIT.RECORD.STATUS` | `FsGaStepSubmitReset_RecordStatus` | String |  |  |
| 20 | `STEP.SUBMIT.CURR.NO` | `FsGaStepSubmitReset_CurrNo` | String |  |  |
| 21 | `STEP.SUBMIT.INPUTTER` | `FsGaStepSubmitReset_Inputter` |  |  |  |
| 22 | `STEP.SUBMIT.DATE.TIME` | `FsGaStepSubmitReset_DateTime` |  |  |  |
| 23 | `STEP.SUBMIT.AUTHORISER` | `FsGaStepSubmitReset_Authoriser` | String |  |  |
| 24 | `STEP.SUBMIT.CO.CODE` | `FsGaStepSubmitReset_CoCode` | String |  |  |
| 25 | `STEP.SUBMIT.DEPT.CODE` | `FsGaStepSubmitReset_DeptCode` | String |  |  |
| 26 | `STEP.SUBMIT.AUDITOR.CODE` | `FsGaStepSubmitReset_AuditorCode` | String |  |  |
| 27 | `STEP.SUBMIT.AUDIT.DATE.TIME` | `FsGaStepSubmitReset_AuditDateTime` | String |  |  |
