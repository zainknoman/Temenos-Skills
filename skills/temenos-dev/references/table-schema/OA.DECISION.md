# OA.DECISION — Table Schema

> Source: `INSERTS/I_F.OA.DECISION` in `OA_Decision.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.DEC.DEFINITION` | `OaDecision_Definition` | TField |  | This field defines that type of the decision being recorded. Validation Rules 1. It should be valid record from OA.DECISION.TYPE 2. It should be a published definition |
| 2 | `OA.DEC.VERSION` | `OaDecision_Version` | TField |  | The version of the Decision being utilized for this application. If the user doesn't input any version, then the system will default the latest version number of current decision (DEFINITION). If user inputs, then version would be validated against all available versions of decision. |
| 3 | `OA.DEC.ACTIVITY` | `OaDecision_Activity` | TField | Yes | This field defines the Activity to be processed against the decision. The activity may be a user activity or a system generated activity. The business functionality of the activity would be defined in the action routines which are defined in ACTIVITY.ACTION or ACTION fields. Validation Rules 1. Input is mandatory in this field. 2. It must be a valid record in AA.CLASS.TYPE.ACTIVITY and valid decision activity. 3. The very first activity to make a decision would be NEW-DECISION. Activity UPDATE-DECISION would be used to vote on the decision. Activity UPDATE.NOTES-DECISION would be used to update the comments and conditions. |
| 4 | `OA.DEC.EFFECTIVE.DATE` | `OaDecision_EffectiveDate` | TField |  | Effective date of the decision being inputted. It will default to system date when the user does not input any date. Validation rules are 1. The effective date should be greater than or equals to AVAILABLE.DATE of decision definition, which will be taken from OA.DECISION record of definition. 2. The effective date should be less than to EXPIRY.DATE of decision definition, which will be taken from OA.DECISION.TYPE record of definition. |
| 5 | `OA.DEC.CLASS.INSTANCE` | `OaDecision_ClassInstance` |  |  |  |
| 6 | `OA.DEC.INSTANCE.KEY` | `OaDecision_InstanceKey` |  |  |  |
| 7 | `OA.DEC.INSTANCE.STATUS` | `OaDecision_InstanceStatus` |  |  |  |
| 8 | `OA.DEC.STD.RESERVE8` | `OaDecision_StdReserve8` | TField |  | Reserved Field included for future purpose. |
| 9 | `OA.DEC.STD.RESERVE7` | `OaDecision_StdReserve7` | TField |  | Reserved Field included for future purpose. |
| 10 | `OA.DEC.STD.RESERVE6` | `OaDecision_StdReserve6` | TField |  | Reserved Field included for future purpose. |
| 11 | `OA.DEC.CUSTOMER` | `OaDecision_Customer` |  |  |  |
| 12 | `OA.DEC.CUSTOMER.ROLE` | `OaDecision_CustomerRole` |  |  |  |
| 13 | `OA.DEC.TO.CLASS.INSTANCE` | `OaDecision_ToClassInstance` |  |  |  |
| 14 | `OA.DEC.TO.FIELD` | `OaDecision_ToField` |  |  |  |
| 15 | `OA.DEC.TO.VALUE` | `OaDecision_ToValue` |  |  |  |
| 16 | `OA.DEC.LAST.ACTIVITY` | `OaDecision_LastActivity` | TField |  |  |
| 17 | `OA.DEC.STD.RESERVE4` | `OaDecision_StdReserve4` | TField |  | Reserved Field included for future purpose. |
| 18 | `OA.DEC.STD.RESERVE3` | `OaDecision_StdReserve3` | TField |  | Reserved Field included for future purpose. |
| 19 | `OA.DEC.STD.RESERVE2` | `OaDecision_StdReserve2` | TField |  | Reserved Field included for future purpose. |
| 20 | `OA.DEC.STD.RESERVE1` | `OaDecision_StdReserve1` | TField |  |  |
| 21 | `OA.DEC.APPLICATION` | `OaDecision_Application` | TField |  | A Valid OA.APPLICATION record |
| 22 | `OA.DEC.PURPOSE` | `OaDecision_Purpose` | TField |  | Purpose of the Application input. |
| 23 | `OA.DEC.DATA.CONTEXT` | `OaDecision_DataContext` | TField |  | Context specified in the decision type. |
| 24 | `OA.DEC.DATA.REFERENCE` | `OaDecision_DataReference` | TField |  | Reference of the record for which decision needs to be made. Should be a valid record in the given DATA.CONTEXT |
| 25 | `OA.DEC.PREV.DECISION` | `OaDecision_PrevDecision` | TField |  | This is a no input field, which will hold the reference of then previous decision record associated with the current decision. |
| 26 | `OA.DEC.NEXT.DECISION` | `OaDecision_NextDecision` | TField |  | This is a no input field, which will hold the subsequent decision reference. |
| 27 | `OA.DEC.METHOD` | `OaDecision_Method` | TField |  | Specifies whether the decision was made by a body or was made automatically. Noinput field |
| 28 | `OA.DEC.EVALUATED.DECISION.MATRIX` | `OaDecision_EvaluatedDecisionMatrix` | TField |  | Populated with the matrix which either made the decision or which selected the Decision Body. Noinput field |
| 29 | `OA.DEC.EVALUATED.DECISION.BODY` | `OaDecision_EvaluatedDecisionBody` | TField |  | The decision body selected to make the decision. Noinput field |
| 30 | `OA.DEC.LOCAL.REF` | `OaDecision_LocalRef` |  |  |  |
| 31 | `OA.DEC.OVERRIDE` | `OaDecision_Override` |  |  |  |
| 32 | `OA.DEC.RECORD.STATUS` | `OaDecision_RecordStatus` | String |  | Reserved Field included for future purpose. |
| 33 | `OA.DEC.CURR.NO` | `OaDecision_CurrNo` | String |  |  |
| 34 | `OA.DEC.INPUTTER` | `OaDecision_Inputter` |  |  |  |
| 35 | `OA.DEC.DATE.TIME` | `OaDecision_DateTime` |  |  |  |
| 36 | `OA.DEC.AUTHORISER` | `OaDecision_Authoriser` | String |  |  |
| 37 | `OA.DEC.CO.CODE` | `OaDecision_CoCode` | String |  |  |
| 38 | `OA.DEC.DEPT.CODE` | `OaDecision_DeptCode` | String |  |  |
| 39 | `OA.DEC.AUDITOR.CODE` | `OaDecision_AuditorCode` | String |  |  |
| 40 | `OA.DEC.AUDIT.DATE.TIME` | `OaDecision_AuditDateTime` | String |  |  |
| 41 | `OA.DEC.AUTO.DECISION` | `OaDecision_AutoDecision` | TField |  |  |
