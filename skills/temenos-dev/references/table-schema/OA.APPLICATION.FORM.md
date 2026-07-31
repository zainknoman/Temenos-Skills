# OA.APPLICATION.FORM — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.FORM` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.AF.DEFINITION` | `OaApplicationForm_Definition` | TField |  | It holds the ID of OA.FORM. It is NOINPUT field and system populated field. It populated based on the Purpose. |
| 2 | `OA.AF.VERSION` | `OaApplicationForm_Version` | TField |  | Version of the form being utilized for this application. This gets defaulted when the application form is begun and frozen. |
| 3 | `OA.AF.ACTIVITY` | `OaApplicationForm_Activity` | TField | Yes | This field defines the Activity to be processed against the Application Form. The activity may be a user activity or a system generated activity. The business functionality of the activity would be defined in the action routines which are defined in ACTIVITY.ACTION or ACTION fields Validation Rules 1. Input is mandatory in this field. 2. It must be a valid record in AA.CLASS.TYPE.ACTIVITY and valid application form activity. 3. The very first activity to capture the evidence would be NEW-FORM. Once the all the formlets recorded then the user can trigger the SUBMIT-FORM activity to submit the form. |
| 4 | `OA.AF.EFFECTIVE.DATE` | `OaApplicationForm_EffectiveDate` | TField |  | Effective date of the form being inputted. This gets defaulted with system date when the application form is begun and frozen. |
| 5 | `OA.AF.CLASS.INSTANCE` | `OaApplicationForm_ClassInstance` |  |  |  |
| 6 | `OA.AF.INSTANCE.KEY` | `OaApplicationForm_InstanceKey` |  |  |  |
| 7 | `OA.AF.INSTANCE.STATUS` | `OaApplicationForm_InstanceStatus` |  |  |  |
| 8 | `OA.AF.STD.RESERVE8` | `OaApplicationForm_StdReserve8` | TField |  | Reserved Field included for future purpose. |
| 9 | `OA.AF.STD.RESERVE7` | `OaApplicationForm_StdReserve7` | TField |  | Reserved Field included for future purpose. |
| 10 | `OA.AF.STD.RESERVE6` | `OaApplicationForm_StdReserve6` | TField |  | Reserved Field included for future purpose. |
| 11 | `OA.AF.CUSTOMER` | `OaApplicationForm_Customer` |  |  |  |
| 12 | `OA.AF.CUSTOMER.ROLE` | `OaApplicationForm_CustomerRole` |  |  |  |
| 13 | `OA.AF.TO.CLASS.INSTANCE` | `OaApplicationForm_ToClassInstance` |  |  |  |
| 14 | `OA.AF.TO.FIELD` | `OaApplicationForm_ToField` |  |  |  |
| 15 | `OA.AF.TO.VALUE` | `OaApplicationForm_ToValue` |  |  |  |
| 16 | `OA.AF.LAST.ACTIVITY` | `OaApplicationForm_LastActivity` | TField |  | Details of Last activity performed on this record. |
| 17 | `OA.AF.STD.RESERVE4` | `OaApplicationForm_StdReserve4` | TField |  | Reserved Field included for future purpose. |
| 18 | `OA.AF.STD.RESERVE3` | `OaApplicationForm_StdReserve3` | TField |  | Reserved Field included for future purpose. |
| 19 | `OA.AF.STD.RESERVE2` | `OaApplicationForm_StdReserve2` | TField |  | Reserved Field included for future purpose. |
| 20 | `OA.AF.STD.RESERVE1` | `OaApplicationForm_StdReserve1` | TField |  | Reserved Field included for future purpose. |
| 21 | `OA.AF.FORM.STATUS` | `OaApplicationForm_FormStatus` | TField |  | Status of the form with respect to this purpose. Currently reserved for future use. |
| 22 | `OA.AF.PURPOSE` | `OaApplicationForm_Purpose` |  |  |  |
| 23 | `OA.AF.LINKED.APPL` | `OaApplicationForm_LinkedAppl` | TField |  | Specifies the T24 application(s) the evidence is associated with. � CUSTOMER � COLLATERAL � OA.APPLICATION |
| 24 | `OA.AF.LINKED.APPL.ID` | `OaApplicationForm_LinkedApplId` | TField |  | The record ID(s) of the associated application. More than one ID can be added (e.g. in the case where the evidence is associated to multiple customers) |
| 25 | `OA.AF.DEF.APPLICATION.REFERENCE` | `OaApplicationForm_DefApplicationReference` | TField |  |  |
| 26 | `OA.AF.RESERVED.4` | `OaApplicationForm_Reserved4` | TField |  |  |
| 27 | `OA.AF.RESERVED.3` | `OaApplicationForm_Reserved3` | TField |  |  |
| 28 | `OA.AF.RESERVED.2` | `OaApplicationForm_Reserved2` | TField |  |  |
| 29 | `OA.AF.RESERVED.1` | `OaApplicationForm_Reserved1` | TField |  |  |
| 30 | `OA.AF.LOCAL.REF` | `OaApplicationForm_LocalRef` |  |  |  |
| 31 | `OA.AF.OVERRIDE` | `OaApplicationForm_Override` |  |  |  |
| 32 | `OA.AF.RECORD.STATUS` | `OaApplicationForm_RecordStatus` | String |  |  |
| 33 | `OA.AF.CURR.NO` | `OaApplicationForm_CurrNo` | String |  |  |
| 34 | `OA.AF.INPUTTER` | `OaApplicationForm_Inputter` |  |  |  |
| 35 | `OA.AF.DATE.TIME` | `OaApplicationForm_DateTime` |  |  |  |
| 36 | `OA.AF.AUTHORISER` | `OaApplicationForm_Authoriser` | String |  |  |
| 37 | `OA.AF.CO.CODE` | `OaApplicationForm_CoCode` | String |  |  |
| 38 | `OA.AF.DEPT.CODE` | `OaApplicationForm_DeptCode` | String |  |  |
| 39 | `OA.AF.AUDITOR.CODE` | `OaApplicationForm_AuditorCode` | String |  |  |
| 40 | `OA.AF.AUDIT.DATE.TIME` | `OaApplicationForm_AuditDateTime` | String |  |  |
| 41 | `OA.AF.OWNER.ROLE` | `OaApplicationForm_OwnerRole` |  |  |  |
| 42 | `OA.AF.OWNER.CUSTOMER` | `OaApplicationForm_OwnerCustomer` |  |  |  |
| 43 | `OA.AF.INPUT.ROLE` | `OaApplicationForm_InputRole` |  |  |  |
| 44 | `OA.AF.INPUT.CUSTOMER` | `OaApplicationForm_InputCustomer` |  |  |  |
| 45 | `OA.AF.SEE.ROLE` | `OaApplicationForm_SeeRole` |  |  |  |
| 46 | `OA.AF.SEE.CUSTOMER` | `OaApplicationForm_SeeCustomer` |  |  |  |
