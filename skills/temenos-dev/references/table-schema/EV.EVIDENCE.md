# EV.EVIDENCE — Table Schema

> Source: `INSERTS/I_F.EV.EVIDENCE` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.EVI.DEFINITION` | `EvEvidence_Definition` | TField |  | This field defines that type of the evidence capturing for the customer. Validation Rules 1. It should be valid record from EV.EVIDENCE. 2. It should be a published definition |
| 2 | `EV.EVI.VERSION` | `EvEvidence_Version` | TField |  | The version of the Evidence being utilized for this application. If the user doesn't input any version, then the system will default the latest version number of current evidence (DEFINITION). If user inputs, then version would be validated against all available versions of evidence. |
| 3 | `EV.EVI.ACTIVITY` | `EvEvidence_Activity` | TField | Yes | This field defines the Activity to be processed against the Evidence. The activity may be a user activity or a system generated activity. The business functionality of the activity would be defined in the action routines which are defined in ACTIVITY.ACTION or ACTION fields. Validation Rules 1. Input is mandatory in this field. 2. It must be a valid record in AA.CLASS.TYPE.ACTIVITY and valid evidence activity. 3. The very first activity to capture the evidence would be NEW-EVIDENCE. Once evidence has committed then any modification would have done by using UPDATE-EVIDENCE.ACTIVITY. Activity ACCEPT-EVIDENCE would be used to accept the evidence. Activity REJECT-EVIDENCE would be used to reject the evidence. 4. Schedule activity EXPIRE-EVIDENCE would be triggered to make the evidence status as EXPIRES, based on the validity of the evidence. |
| 4 | `EV.EVI.EFFECTIVE.DATE` | `EvEvidence_EffectiveDate` | TField |  | Effective date of the evidence being inputted. It will default to system date when the user does not input any date. Validation rules are 1. The effective date should be greater than or equals to AVAILABLE.DATE of evidence definition, which will be taken from EV.EVIDENCE.TYPE record of definition. 2. The effective date should be less than to EXPIRY.DATE of evidence definition, which will be taken from EV.EVIDENCE.TYPE record of definition. |
| 5 | `EV.EVI.CLASS.INSTANCE` | `EvEvidence_ClassInstance` |  |  |  |
| 6 | `EV.EVI.INSTANCE.KEY` | `EvEvidence_InstanceKey` |  |  |  |
| 7 | `EV.EVI.INSTANCE.STATUS` | `EvEvidence_InstanceStatus` |  |  |  |
| 8 | `EV.EVI.STD.RESERVE8` | `EvEvidence_StdReserve8` | TField |  | Reserved Field included for future purpose. |
| 9 | `EV.EVI.STD.RESERVE7` | `EvEvidence_StdReserve7` | TField |  | Reserved Field included for future purpose. |
| 10 | `EV.EVI.STD.RESERVE6` | `EvEvidence_StdReserve6` | TField |  | Reserved Field included for future purpose. |
| 11 | `EV.EVI.CUSTOMER` | `EvEvidence_Customer` |  |  |  |
| 12 | `EV.EVI.CUSTOMER.ROLE` | `EvEvidence_CustomerRole` |  |  |  |
| 13 | `EV.EVI.TO.CLASS.INSTANCE` | `EvEvidence_ToClassInstance` |  |  |  |
| 14 | `EV.EVI.TO.FIELD` | `EvEvidence_ToField` |  |  |  |
| 15 | `EV.EVI.TO.VALUE` | `EvEvidence_ToValue` |  |  |  |
| 16 | `EV.EVI.LAST.ACTIVITY` | `EvEvidence_LastActivity` | TField |  | Details of Last activity performed on this record. |
| 17 | `EV.EVI.STD.RESERVE4` | `EvEvidence_StdReserve4` | TField |  | Reserved Field included for future purpose. |
| 18 | `EV.EVI.STD.RESERVE3` | `EvEvidence_StdReserve3` | TField |  | Reserved Field included for future purpose. |
| 19 | `EV.EVI.STD.RESERVE2` | `EvEvidence_StdReserve2` | TField |  | Reserved Field included for future purpose. |
| 20 | `EV.EVI.STD.RESERVE1` | `EvEvidence_StdReserve1` | TField |  | Reserved Field included for future purpose. |
| 21 | `EV.EVI.SOFT.LINK` | `EvEvidence_SoftLink` |  |  |  |
| 22 | `EV.EVI.LINKED.APPL` | `EvEvidence_LinkedAppl` |  |  |  |
| 23 | `EV.EVI.LINKED.APPL.ID` | `EvEvidence_LinkedApplId` |  |  |  |
| 24 | `EV.EVI.START.DATE` | `EvEvidence_StartDate` | TField |  | This should represent the start date of the evidence as it will also be used to calculate the validity period. It can be left blank when the evidence is received however it is required for the evidence to be considered accepted. If no value has been entered by the user, the system will default the acceptance date. |
| 25 | `EV.EVI.END.DATE` | `EvEvidence_EndDate` | TField |  | Represents the date this evidence is no longer considered valid. This can either be entered by a user or can be calculated based upon the Start Date, Valid Period and Valid Period Based Date defined in evidence product condition. This calculation will be done when the document is being moved to accept. |
| 26 | `EV.EVI.SIGNATURE.DATE` | `EvEvidence_SignatureDate` | TField |  | If a signature is required this field must be populated for evidence to be considered accepted. |
| 27 | `EV.EVI.STATUS` | `EvEvidence_Status` | TField |  | The current status of the evidence. In the valid status are Received, Accepted and Expired. |
| 28 | `EV.EVI.STATUS.DATE` | `EvEvidence_StatusDate` | TField |  | The date the current status was set. |
| 29 | `EV.EVI.STATUS.NOTES` | `EvEvidence_StatusNotes` | TField |  | it is user inpttable field. The user can write any notes pertaining to current status. |
| 30 | `EV.EVI.PREV.STATUS` | `EvEvidence_PrevStatus` |  |  |  |
| 31 | `EV.EVI.PREV.STATUS.DATE` | `EvEvidence_PrevStatusDate` |  |  |  |
| 32 | `EV.EVI.PREV.STATUS.NOTES` | `EvEvidence_PrevStatusNotes` |  |  |  |
| 33 | `EV.EVI.PROCESS.METHOD` | `EvEvidence_ProcessMethod` | TField | No | This field would decide the submitted evidence which would apply on evidence requirement in online or through the service. It is optional field and accepts two values. 1. Online 2. Service Online � The evidence update will happen in Online itself. Service � The evidence update will happen through the service EV.EVIDENCE.STATUS.SERVICE |
| 34 | `EV.EVI.RESERVED.4` | `EvEvidence_Reserved4` | TField |  |  |
| 35 | `EV.EVI.RESERVED.3` | `EvEvidence_Reserved3` | TField |  |  |
| 36 | `EV.EVI.RESERVED.2` | `EvEvidence_Reserved2` | TField |  |  |
| 37 | `EV.EVI.RESERVED.1` | `EvEvidence_Reserved1` | TField |  |  |
| 38 | `EV.EVI.LOCAL.REF` | `EvEvidence_LocalRef` |  |  |  |
| 39 | `EV.EVI.OVERRIDE` | `EvEvidence_Override` |  |  |  |
| 40 | `EV.EVI.RECORD.STATUS` | `EvEvidence_RecordStatus` | String |  |  |
| 41 | `EV.EVI.CURR.NO` | `EvEvidence_CurrNo` | String |  |  |
| 42 | `EV.EVI.INPUTTER` | `EvEvidence_Inputter` |  |  |  |
| 43 | `EV.EVI.DATE.TIME` | `EvEvidence_DateTime` |  |  |  |
| 44 | `EV.EVI.AUTHORISER` | `EvEvidence_Authoriser` | String |  |  |
| 45 | `EV.EVI.CO.CODE` | `EvEvidence_CoCode` | String |  |  |
| 46 | `EV.EVI.DEPT.CODE` | `EvEvidence_DeptCode` | String |  |  |
| 47 | `EV.EVI.AUDITOR.CODE` | `EvEvidence_AuditorCode` | String |  |  |
| 48 | `EV.EVI.AUDIT.DATE.TIME` | `EvEvidence_AuditDateTime` | String |  |  |
