# CP.ENTITY.WORKFLOW — Table Schema

> Source: `INSERTS/I_F.CP.ENTITY.WORKFLOW` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.EWF.WF.DESCRIPTION` | `CpEntityWorkflow_WfDescription` | TField | Yes | This fields stores a short description of the workflow for the specific type. Validation Rules :Mandatory field, any 500 characters. |
| 2 | `CP.EWF.WORKFLOW.TYPE` | `CpEntityWorkflow_WorkflowType` | TField | Yes | THis field represents the type of object for which the workflow applies.The values are: Program Workflow, Campaign Workflow, Global Exlusion Profile Workflow, Global Campaign Profile Workflow, Global Details Record Workflow, Admin Workflow for Admin items. Validation Rules :Mandatory field, any 50 characters. |
| 3 | `CP.EWF.WF.ENABLED` | `CpEntityWorkflow_WfEnabled` | TField | Yes | This field represents the status of the workflow when it is linked to the business objective.Values: Y/N. Validation Rules :Mandatory field, any 1 characters. |
| 4 | `CP.EWF.PURPOSE.TYPE` | `CpEntityWorkflow_PurposeType` | TField |  | This field represents the purpose for which we can have a workflow.Values: business objective, product, group of products, context. Validation Rules :Any 35 characters. |
| 5 | `CP.EWF.PURPOSE` | `CpEntityWorkflow_Purpose` | TField |  | This field represents the actual value of the purpose. Validation Rules :Any 200 characters. |
| 6 | `CP.EWF.STATUS.CODE` | `CpEntityWorkflow_StatusCode` |  |  |  |
| 7 | `CP.EWF.STATUS.CODE.DESC` | `CpEntityWorkflow_StatusCodeDesc` |  |  |  |
| 8 | `CP.EWF.STATUS.TYPE` | `CpEntityWorkflow_StatusType` |  |  |  |
| 9 | `CP.EWF.NEXT.BTN.LABEL` | `CpEntityWorkflow_NextBtnLabel` |  |  |  |
| 10 | `CP.EWF.NEXT.MSG.ID` | `CpEntityWorkflow_NextMsgId` |  |  |  |
| 11 | `CP.EWF.NEXT.TT.ID` | `CpEntityWorkflow_NextTtId` |  |  |  |
| 12 | `CP.EWF.NEXT.STATUS` | `CpEntityWorkflow_NextStatus` |  |  |  |
| 13 | `CP.EWF.BACK.BTN.LABEL` | `CpEntityWorkflow_BackBtnLabel` |  |  |  |
| 14 | `CP.EWF.BACK.MSG.ID` | `CpEntityWorkflow_BackMsgId` |  |  |  |
| 15 | `CP.EWF.BACK.TT.ID` | `CpEntityWorkflow_BackTtId` |  |  |  |
| 16 | `CP.EWF.BACK.STATUS` | `CpEntityWorkflow_BackStatus` |  |  |  |
| 17 | `CP.EWF.AUTO.START.STATUS` | `CpEntityWorkflow_AutoStartStatus` |  |  |  |
| 18 | `CP.EWF.AUTO.END.STATUS` | `CpEntityWorkflow_AutoEndStatus` |  |  |  |
| 19 | `CP.EWF.APP.EDITABLE` | `CpEntityWorkflow_AppEditable` |  |  |  |
| 20 | `CP.EWF.NB.OF.AUTH` | `CpEntityWorkflow_NbOfAuth` |  |  |  |
| 21 | `CP.EWF.USER.ROLE` | `CpEntityWorkflow_UserRole` |  |  |  |
| 22 | `CP.EWF.DASHBOARD.VIEW` | `CpEntityWorkflow_DashboardView` |  |  |  |
| 23 | `CP.EWF.WF.NEEDED` | `CpEntityWorkflow_WfNeeded` | TField | Yes | This field states if an object requires an approval workflow to go through.Values: Y/N. Validation Rules :Mandatory field, any 1 characters. |
| 24 | `CP.EWF.RESERVED.6` | `CpEntityWorkflow_Reserved6` | TField |  |  |
| 25 | `CP.EWF.RESERVED.5` | `CpEntityWorkflow_Reserved5` | TField |  |  |
| 26 | `CP.EWF.RESERVED.4` | `CpEntityWorkflow_Reserved4` | TField |  |  |
| 27 | `CP.EWF.RESERVED.3` | `CpEntityWorkflow_Reserved3` | TField |  |  |
| 28 | `CP.EWF.RESERVED.2` | `CpEntityWorkflow_Reserved2` | TField |  |  |
| 29 | `CP.EWF.RESERVED.1` | `CpEntityWorkflow_Reserved1` | TField |  |  |
| 30 | `CP.EWF.LOCAL.REF` | `CpEntityWorkflow_LocalRef` |  |  |  |
| 31 | `CP.EWF.OVERRIDE` | `CpEntityWorkflow_Override` |  |  |  |
| 32 | `CP.EWF.RECORD.STATUS` | `CpEntityWorkflow_RecordStatus` | String |  |  |
| 33 | `CP.EWF.CURR.NO` | `CpEntityWorkflow_CurrNo` | String |  |  |
| 34 | `CP.EWF.INPUTTER` | `CpEntityWorkflow_Inputter` |  |  |  |
| 35 | `CP.EWF.DATE.TIME` | `CpEntityWorkflow_DateTime` |  |  |  |
| 36 | `CP.EWF.AUTHORISER` | `CpEntityWorkflow_Authoriser` | String |  |  |
| 37 | `CP.EWF.CO.CODE` | `CpEntityWorkflow_CoCode` | String |  |  |
| 38 | `CP.EWF.DEPT.CODE` | `CpEntityWorkflow_DeptCode` | String |  |  |
| 39 | `CP.EWF.AUDITOR.CODE` | `CpEntityWorkflow_AuditorCode` | String |  |  |
| 40 | `CP.EWF.AUDIT.DATE.TIME` | `CpEntityWorkflow_AuditDateTime` | String |  |  |
