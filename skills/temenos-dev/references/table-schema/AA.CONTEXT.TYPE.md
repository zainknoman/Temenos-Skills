# AA.CONTEXT.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.CONTEXT.TYPE` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CNT.DESCRIPTION` | `AaContextType_Description` |  |  |  |
| 2 | `AA.CNT.SYSTEM.DEFINED.TYPE` | `AaContextType_SystemDefinedType` | TField |  | Denotes the type of value used for the context type ID. Eg: If a context type should be used for Term, PERIOD must be given this field. Validation Rules: 1.Allowed data types are AMOUNT, CURRENCY, DATE, NUMERIC, PERIOD, RATE, STRING, BIG.STRING, CUSTOMER &amp; ACCOUNT. 2.Value in this field is not allowed when VALIDATION.ROUTINE has value and vice versa. |
| 3 | `AA.CNT.VALIDATION.ROUTINE` | `AaContextType_ValidationRoutine` | TField |  | Routine can be specified for the purpose of validating the context type. Validation Rules: 1. This field is mutually exclusive with the field System Defined Type. If value is specified in this field, system will not allow value in System Defined Type and vice versa., 2. Must be a valid routine in EB.API |
| 4 | `AA.CNT.SYSTEM.MAINTAINED` | `AaContextType_SystemMaintained` | TField |  | Denotes the context type is used for internal purpose and user can not make any changes to this context type except for the description. |
| 5 | `AA.CNT.MAINTAIN.HISTORY` | `AaContextType_MaintainHistory` | TField |  | Acts as a filter to store context name along with the activity id in activity history. Only when this field is set to YES, system will store the context name in the activity history which will be used for periodic evaluations. Note: Flag this field to YES will create performance. Hence switch on this field only when it is really required. |
| 6 | `AA.CNT.MULTI.VALUE` | `AaContextType_MultiValue` | TField |  | If it is set then we can pass multiple values in to the same context type. Validation - If this field is set then MAINTAIN.HISTORY field should be null. |
| 7 | `AA.CNT.CONTEXT.GROUP` | `AaContextType_ContextGroup` | TField |  | Drop down field which enables user to select the context group to which the context type id should belong. |
| 8 | `AA.CNT.PASS.TO.EVENT` | `AaContextType_PassToEvent` | TField | Yes | Enables user to pass information to the accounting layer for soft mapping to extract details of the initiating transaction. Currently allowed values are &apos;Our reference&apos; ,&apos;PARENT.TXN.ID&apos;,&apos;PARENT.TXN.SYS.ID&apos; or &apos;None&apos; Our reference - Current transaction&apos;s reference. PARENT.TXN.ID - Reference of the parent which initiated the transaction . PARENT.TXN.SYS.ID - System ID of the parent which initiated the transaction. It is a non-mandatory field. |
| 9 | `AA.CNT.PARENT.CONTEXT` | `AaContextType_ParentContext` | TField |  | To define the parent context name which should be a valid AA.CONTEXT.TYPE record Id. If PARENT.CONTEXT field contains a value, then this record becomes a child for the context name entered in the PARENT.CONTEXT field. |
| 10 | `AA.CNT.CHILD.CONTEXT` | `AaContextType_ChildContext` | TField |  | It holds the child context name which gets automatically updated in Parent record when creating a child AA.CONTEXT.TYPE record. If CHILD.CONTEXT field has a value, then this record becomes the parent of the context name entered in this field. |
| 11 | `AA.CNT.RESERVED.2` | `AaContextType_Reserved2` | TField |  |  |
| 12 | `AA.CNT.RESERVED.1` | `AaContextType_Reserved1` | TField |  |  |
| 13 | `AA.CNT.LOCAL.REF` | `AaContextType_LocalRef` |  |  |  |
| 14 | `AA.CNT.OVERRIDE` | `AaContextType_Override` |  |  |  |
| 15 | `AA.CNT.RECORD.STATUS` | `AaContextType_RecordStatus` | String |  |  |
| 16 | `AA.CNT.CURR.NO` | `AaContextType_CurrNo` | String |  |  |
| 17 | `AA.CNT.INPUTTER` | `AaContextType_Inputter` |  |  |  |
| 18 | `AA.CNT.DATE.TIME` | `AaContextType_DateTime` |  |  |  |
| 19 | `AA.CNT.AUTHORISER` | `AaContextType_Authoriser` | String |  |  |
| 20 | `AA.CNT.CO.CODE` | `AaContextType_CoCode` | String |  |  |
| 21 | `AA.CNT.DEPT.CODE` | `AaContextType_DeptCode` | String |  |  |
| 22 | `AA.CNT.AUDITOR.CODE` | `AaContextType_AuditorCode` | String |  |  |
| 23 | `AA.CNT.AUDIT.DATE.TIME` | `AaContextType_AuditDateTime` | String |  |  |
