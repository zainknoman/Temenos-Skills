# AA.ACTIVITY.CLASS — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY.CLASS` in `AA_ProductFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ACC.DESCRIPTION` | `AaActivityClass_Description` |  |  |  |
| 2 | `AA.ACC.FULL.DESC` | `AaActivityClass_FullDesc` |  |  |  |
| 3 | `AA.ACC.ATTRIBUTE` | `AaActivityClass_Attribute` |  |  |  |
| 4 | `AA.ACC.ACTIVITY.TYPE` | `AaActivityClass_ActivityType` |  |  |  |
| 5 | `AA.ACC.BATCH.NAME` | `AaActivityClass_BatchName` |  |  |  |
| 6 | `AA.ACC.BATCH.SEQ` | `AaActivityClass_BatchSeq` |  |  |  |
| 7 | `AA.ACC.RELATED.ACT.CLASS` | `AaActivityClass_RelatedActClass` | TField |  | This field is used ONLY whilst simulating an Arrangement scenario and is used only for LENDING and DEPOSIT product lines at the moment. For example, when a NEW arrangement is to be simulated for 2 schedules, the schedules could be run only after the arrangement could be disbursed(either fully or partially). But, disbursement is always transaction driven and may not be captured using a AA.SIMULATION.CAPTURE application. To automatically trigger an activity after the current activity(stated in this ID), this field may be utilised. So, a LENDING-NEW-ARRANGEMENT would have LENDING-DISBURSE-TERM.AMOUNT as its RELATED.ACT.CLASS. Similarly, automatic repayments on DUEs may be triggered by using this field. The disbursement and repayments generally assume FULL disbursement and payment which may be altered at the AA.SIMULATION.RUNNER to simulate partial disbursements and payments. Only an activity belonging to this Activity class may be stated in the RELATED.ACTIVITY field of AA.ACTIVITY record. Temenos would release the related activity class that may be used with this activity and cannot be modified by the user. This field has NO relevance on activities triggered on Live arrangement. Validations: Should be a valid entry in AA.ACTIVITY.CLASS file. Validation rules: Should be a valid ID in AA.ACTIVITY.CLASS table. |
| 8 | `AA.ACC.ALERT.EVENT.TYPE` | `AaActivityClass_AlertEventType` |  |  |  |
| 9 | `AA.ACC.PROPERTY.CLASS` | `AaActivityClass_PropertyClass` |  |  |  |
| 10 | `AA.ACC.USER.INPUT` | `AaActivityClass_UserInput` |  |  |  |
| 11 | `AA.ACC.ACTION` | `AaActivityClass_Action` |  |  |  |
| 12 | `AA.ACC.PRODUCT.LINE` | `AaActivityClass_ProductLine` | TField |  | This field denotes the product line for which this activity is valid. This field gets updated from the ID of the current record. System maintained(NOINPUT) field. |
| 13 | `AA.ACC.PROCESS.ID` | `AaActivityClass_ProcessId` | TField |  | This field denotes the process that would be carried out in the activity. This field gets updated from the ID of the current record System maintained (NOINPUT) field. |
| 14 | `AA.ACC.CLASS.ID` | `AaActivityClass_ClassId` | TField |  | This field represents the property class on which the said action would be performed. System maintained(NOINPUT) field. |
| 15 | `AA.ACC.RESERVED10` | `AaActivityClass_Reserved10` | TField |  |  |
| 16 | `AA.ACC.USED.PROPCLASS` | `AaActivityClass_UsedPropclass` |  |  |  |
| 17 | `AA.ACC.USED.FIELD` | `AaActivityClass_UsedField` |  |  |  |
| 18 | `AA.ACC.CAN.PROP.CLASS` | `AaActivityClass_CanPropClass` |  |  |  |
| 19 | `AA.ACC.CAN.USER.INP` | `AaActivityClass_CanUserInp` |  |  |  |
| 20 | `AA.ACC.CAN.ACTION` | `AaActivityClass_CanAction` |  |  |  |
| 21 | `AA.ACC.PRE.ACTIVITY.CLASS` | `AaActivityClass_PreActivityClass` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 22 | `AA.ACC.POST.ACTIVITY.CLASS` | `AaActivityClass_PostActivityClass` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 23 | `AA.ACC.PAYLOAD.MAPPER` | `AaActivityClass_PayloadMapper` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 24 | `AA.ACC.RESERVED01` | `AaActivityClass_Reserved01` | TField |  |  |
| 25 | `AA.ACC.RECORD.STATUS` | `AaActivityClass_RecordStatus` | String |  |  |
| 26 | `AA.ACC.CURR.NO` | `AaActivityClass_CurrNo` | String |  |  |
| 27 | `AA.ACC.INPUTTER` | `AaActivityClass_Inputter` |  |  |  |
| 28 | `AA.ACC.DATE.TIME` | `AaActivityClass_DateTime` |  |  |  |
| 29 | `AA.ACC.AUTHORISER` | `AaActivityClass_Authoriser` | String |  |  |
| 30 | `AA.ACC.CO.CODE` | `AaActivityClass_CoCode` | String |  |  |
| 31 | `AA.ACC.DEPT.CODE` | `AaActivityClass_DeptCode` | String |  |  |
| 32 | `AA.ACC.AUDITOR.CODE` | `AaActivityClass_AuditorCode` | String |  |  |
| 33 | `AA.ACC.AUDIT.DATE.TIME` | `AaActivityClass_AuditDateTime` | String |  |  |
| 34 | `AA.ACC.EVENT.CLASS` | `AaActivityClass_EventClass` | TField |  | Indicates the event class(the structure of the payload) that would be used for this Activity class. Validation rules: Should be a valid entry in MS.EVENT.CLASS Maximum of 35 Alphanumeric characters. |
| 35 | `AA.ACC.EVENT.GROUP` | `AaActivityClass_EventGroup` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
