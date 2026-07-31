# NA.QUESTIONNAIRE — Table Schema

> Source: `INSERTS/I_F.NA.QUESTIONNAIRE` in `NA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.QNR.DEFINITION` | `NaQuestionnaire_Definition` | TField |  | This field defines that type of the needs questionnaire for the customer. Validation Rules 1. It should be valid record from NA.QUESTIONNAIRE.TYPE. 2. It should be a published definition |
| 2 | `NA.QNR.VERSION` | `NaQuestionnaire_Version` | TField |  | The version of the Questionnaire type being utilized for this application. If the user doesn&apos;t input any version, then the system will default the latest version number of current questionnaire type(DEFINITION). If user inputs, then version would be validated against all available versions of evidence. |
| 3 | `NA.QNR.ACTIVITY` | `NaQuestionnaire_Activity` | TField | Yes | This field defines the Activity to be processed against the Questionnaire. The activity may be a user activity or a system generated activity. The business functionality of the activity would be defined in the action routines which are defined in ACTIVITY.ACTION or ACTION fields. Validation Rules 1. Input is mandatory in this field. 2. It must be a valid record in AA.CLASS.TYPE.ACTIVITY and valid evidence activity. 3. The very first activity to capture the needs would be NEW.REQUEST-NEEDS. 4. Any modification to an existing record must be done through UPDATE.REQUEST-NEEDS. |
| 4 | `NA.QNR.EFFECTIVE.DATE` | `NaQuestionnaire_EffectiveDate` | TField |  | Effective date of the evidence being inputted. It will default to system date when the user does not input any date. Validation rules are 1. The effective date should be greater than or equals to AVAILABLE.DATE of questionnaire definition, which will be taken from NA.QUESTIONNAIRE.TYPE record of definition. 2. The effective date should be less than to EXPIRY.DATE of questionnaire definition, which will be taken from NA.QUESTIONNAIRE.TYPE record of definition. |
| 5 | `NA.QNR.CLASS.INSTANCE` | `NaQuestionnaire_ClassInstance` |  |  |  |
| 6 | `NA.QNR.INSTANCE.KEY` | `NaQuestionnaire_InstanceKey` |  |  |  |
| 7 | `NA.QNR.INSTANCE.STATUS` | `NaQuestionnaire_InstanceStatus` |  |  |  |
| 8 | `NA.QNR.STD.RESERVE8` | `NaQuestionnaire_StdReserve8` | TField |  |  |
| 9 | `NA.QNR.STD.RESERVE7` | `NaQuestionnaire_StdReserve7` | TField |  |  |
| 10 | `NA.QNR.STD.RESERVE6` | `NaQuestionnaire_StdReserve6` | TField |  |  |
| 11 | `NA.QNR.CUSTOMER` | `NaQuestionnaire_Customer` |  |  |  |
| 12 | `NA.QNR.CUSTOMER.ROLE` | `NaQuestionnaire_CustomerRole` |  |  |  |
| 13 | `NA.QNR.TO.CLASS.INSTANCE` | `NaQuestionnaire_ToClassInstance` |  |  |  |
| 14 | `NA.QNR.TO.FIELD` | `NaQuestionnaire_ToField` |  |  |  |
| 15 | `NA.QNR.TO.VALUE` | `NaQuestionnaire_ToValue` |  |  |  |
| 16 | `NA.QNR.LAST.ACTIVITY` | `NaQuestionnaire_LastActivity` | TField |  | Details of last activity performed on the current record. |
| 17 | `NA.QNR.STD.RESERVE4` | `NaQuestionnaire_StdReserve4` | TField |  |  |
| 18 | `NA.QNR.STD.RESERVE3` | `NaQuestionnaire_StdReserve3` | TField |  |  |
| 19 | `NA.QNR.STD.RESERVE2` | `NaQuestionnaire_StdReserve2` | TField |  |  |
| 20 | `NA.QNR.STD.RESERVE1` | `NaQuestionnaire_StdReserve1` | TField |  |  |
| 21 | `NA.QNR.APPLICATION` | `NaQuestionnaire_Application` | TField |  | It is a valid record from the OA.APPLICATION table. If the user gives input this field then the system will link the current quotation Request along with Application. And the Linked quotation details will get updated in the OA.APPLICATION.STATUS record. |
| 22 | `NA.QNR.PURPOSE` | `NaQuestionnaire_Purpose` |  |  |  |
| 23 | `NA.QNR.RESERVED.4` | `NaQuestionnaire_Reserved4` | TField |  |  |
| 24 | `NA.QNR.RESERVED.3` | `NaQuestionnaire_Reserved3` | TField |  |  |
| 25 | `NA.QNR.RESERVED.2` | `NaQuestionnaire_Reserved2` | TField |  |  |
| 26 | `NA.QNR.RESERVED.1` | `NaQuestionnaire_Reserved1` | TField |  |  |
| 27 | `NA.QNR.LOCAL.REF` | `NaQuestionnaire_LocalRef` |  |  |  |
| 28 | `NA.QNR.STMT.NOS` | `NaQuestionnaire_StmtNos` |  |  |  |
| 29 | `NA.QNR.OVERRIDE` | `NaQuestionnaire_Override` |  |  |  |
| 30 | `NA.QNR.RECORD.STATUS` | `NaQuestionnaire_RecordStatus` | String |  |  |
| 31 | `NA.QNR.CURR.NO` | `NaQuestionnaire_CurrNo` | String |  |  |
| 32 | `NA.QNR.INPUTTER` | `NaQuestionnaire_Inputter` |  |  |  |
| 33 | `NA.QNR.DATE.TIME` | `NaQuestionnaire_DateTime` |  |  |  |
| 34 | `NA.QNR.AUTHORISER` | `NaQuestionnaire_Authoriser` | String |  |  |
| 35 | `NA.QNR.CO.CODE` | `NaQuestionnaire_CoCode` | String |  |  |
| 36 | `NA.QNR.DEPT.CODE` | `NaQuestionnaire_DeptCode` | String |  |  |
| 37 | `NA.QNR.AUDITOR.CODE` | `NaQuestionnaire_AuditorCode` | String |  |  |
| 38 | `NA.QNR.AUDIT.DATE.TIME` | `NaQuestionnaire_AuditDateTime` | String |  |  |
