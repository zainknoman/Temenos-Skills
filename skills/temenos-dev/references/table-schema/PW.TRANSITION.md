# PW.TRANSITION — Table Schema

> Source: `INSERTS/I_F.PW.TRANSITION` in `PW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PW.TRANS.DESCRIPTION` | `PwTransition_Description` |  |  |  |
| 2 | `PW.TRANS.SELECTION.FIELD` | `PwTransition_SelectionField` |  |  |  |
| 3 | `PW.TRANS.OPERAND` | `PwTransition_Operand` |  |  |  |
| 4 | `PW.TRANS.CRITERIA` | `PwTransition_Criteria` |  |  |  |
| 5 | `PW.TRANS.SELECTION.OPERAND` | `PwTransition_SelectionOperand` | TField |  | PW.TRANSITION SELECTION.OPERAND Used in conjunction with multi-value group, SELECTION.FIELD. If set to AND then the conditions set up in the SELECTION.FIELD multi-value group will have to be met as well as the conditions set in the routine indicated in the ROUTINE field. Validation Rules: Only AND, OR or a blank field is valid. If both SELECTION.FIELDS and a Routine is defined SELECTION.OPERAND must be set. |
| 6 | `PW.TRANS.ROUTINE` | `PwTransition_Routine` | TField |  | PW.TRANSITION ROUTINE Local routine name &amp;#8211; routine to return 1 argument containing an error if conditions or rules within the local routine are not met. Validation Rules: Valid local routine name. |
| 7 | `PW.TRANS.CONTEXT` | `PwTransition_Context` | TField |  | PW.TRANSITION CONTEXT CONTEXT field must link to EB.CONTEXT and give a drop down to select any EB.CONTEXT fields When CONTEXT field has value, then all the validations must refer to the fields in the Primary table / linked table (or) data fields added in the EB.CONTEXT. |
| 8 | `PW.TRANS.CONTEXT.REFERENCE` | `PwTransition_ContextReference` | TField |  | PW.TRANSITION CONTEXT.REFERENCE CONTEXT.REFERENCE can have two values pre-req activity or process variable If pre-req activity is selected, then the txn id of the before activity (pre-req activity) will be loaded in the EB.CONTEXT If process variable is selected, then the process variable in the PW.PROCESS.DEFINITION table for that specific transition will be loaded in the EB.CONTEXT |
| 9 | `PW.TRANS.RESERVED.8` | `PwTransition_Reserved8` | TField |  |  |
| 10 | `PW.TRANS.RESERVED.7` | `PwTransition_Reserved7` | TField |  |  |
| 11 | `PW.TRANS.RESERVED.6` | `PwTransition_Reserved6` | TField |  |  |
| 12 | `PW.TRANS.RESERVED.5` | `PwTransition_Reserved5` | TField |  |  |
| 13 | `PW.TRANS.RESERVED.4` | `PwTransition_Reserved4` | TField |  |  |
| 14 | `PW.TRANS.RESERVED.3` | `PwTransition_Reserved3` | TField |  |  |
| 15 | `PW.TRANS.VERSION.ID` | `PwTransition_VersionId` | TField |  | PW.TRANSITION VERSION.ID Specifies the latest version of a process definition Validation Rules: This is a non-input field. Gets auto incremented by one when a process definition is published |
| 16 | `PW.TRANS.PUBLISHED` | `PwTransition_Published` | TField |  | PW.TANSITION PUBLISHED This field holds the information whether the particular process definition has been published Validation Rules: This is a non-input field. Can take values �YES�, �NO� When any changes are made to the PWD except DEF.VER.TO.USE field, this field changes to 'NO' This field changes to 'YES' when the process definition is published |
| 17 | `PW.TRANS.LOCAL.REF` | `PwTransition_LocalRef` |  |  |  |
| 18 | `PW.TRANS.OVERRIDE` | `PwTransition_Override` |  |  |  |
| 19 | `PW.TRANS.RECORD.STATUS` | `PwTransition_RecordStatus` | String |  |  |
| 20 | `PW.TRANS.CURR.NO` | `PwTransition_CurrNo` | String |  |  |
| 21 | `PW.TRANS.INPUTTER` | `PwTransition_Inputter` |  |  |  |
| 22 | `PW.TRANS.DATE.TIME` | `PwTransition_DateTime` |  |  |  |
| 23 | `PW.TRANS.AUTHORISER` | `PwTransition_Authoriser` | String |  |  |
| 24 | `PW.TRANS.CO.CODE` | `PwTransition_CoCode` | String |  |  |
| 25 | `PW.TRANS.DEPT.CODE` | `PwTransition_DeptCode` | String |  |  |
| 26 | `PW.TRANS.AUDITOR.CODE` | `PwTransition_AuditorCode` | String |  |  |
| 27 | `PW.TRANS.AUDIT.DATE.TIME` | `PwTransition_AuditDateTime` | String |  |  |
