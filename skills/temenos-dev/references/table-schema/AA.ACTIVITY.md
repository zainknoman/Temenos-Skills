# AA.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY` in `AA_ProductFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ACT.DESCRIPTION` | `AaActivity_Description` |  |  |  |
| 2 | `AA.ACT.FULL.DESC` | `AaActivity_FullDesc` |  |  |  |
| 3 | `AA.ACT.LINKED.ACTIVITY` | `AaActivity_LinkedActivity` | TField | Yes | All user defined activities must be linked to a core system activity. This field defines system activity to which the given user defined activity is linked. This field cannot be input for system activities. Validation rules: Mandatory for User defined activities Input in this field should be a valid id in AA.ACTIVITY file Maximum of 55 characters Must link to a System activity The value in this field cannot be changed after authorisation of the record. |
| 4 | `AA.ACT.SYSTEM.ACTIVITY` | `AaActivity_SystemActivity` | TField |  | This field indicates whether the current activity is a system created or a user defined activity. For system created activity, this would default to YES. System maintained(NOINPUT) field |
| 5 | `AA.ACT.LOCAL.REF` | `AaActivity_LocalRef` |  |  |  |
| 6 | `AA.ACT.PRODUCT.LINE` | `AaActivity_ProductLine` | TField |  | This field denotes the product line for which this activity is valid. This field gets updated from the ID of the current record. For user activities, this defaults to the product line of the LINKED.ACTIVITY System maintained (NOINPUT) field. |
| 7 | `AA.ACT.PROCESS.ID` | `AaActivity_ProcessId` | TField |  | This field denotes the process that would be carried out in the activity. This field gets updated from the ID of the current record. For user activities, this defaults to the process id of the LINKED.ACTIVITY System maintained (NOINPUT) field. |
| 8 | `AA.ACT.PROPERTY` | `AaActivity_Property` | TField |  | The fields denotes the property on which this activity could be triggered. This field gets updated from the ID of the current record. For user activities, this defaults to the property of the LINKED.ACTIVITY System maintained(NOINPUT) field. |
| 9 | `AA.ACT.ATTRIBUTE` | `AaActivity_Attribute` |  |  |  |
| 10 | `AA.ACT.RELATED.ACTIVITY` | `AaActivity_RelatedActivity` | TField |  | This field is used ONLY whilst simulating an Arrangement scenario and is used only for LENDING, DEPOSIT product lines at the moment. For example, when a NEW arrangement is to be simulated for 2 schedules, the schedules could be run only after the arrangement could be disbursed(either fully or partially). But, disbursement is always transaction driven and may not be captured using a AA.SIMULATION.CAPTURE application. To automatically trigger an activity after the current activity(stated in this ID), this field may be utilised. So, a LENDING-NEW-ARRANGEMENT would have LENDING-DISBURSE-COMMITMENT as its RELATED.ACTIVITY. Similarly, automatic repayments on DUEs may be triggered by using this field. The disbursement and repayments generally assume FULL disbursement and payment which may be altered at the AA.SIMULATION.RUNNER to simulate partial disbursements and payments. Only an activity belonging to the Activity class stated in its AA.ACTIVITY.CLASS may be stated (RELATED.ACT.CLASS field). User Activities may also be stated here as long as they belong to the core Activity class. This field has NO relevance on activities triggered on Live arrangement. Validations: Should be a valid entry in AA.ACTIVITY file. Should belong to the Activity class stated in RELATED.ACT.CLASS field of the AA.ACTIVITY.CLASS. |
| 11 | `AA.ACT.ACTIVITY.TYPE` | `AaActivity_ActivityType` |  |  |  |
| 12 | `AA.ACT.EXCLUDE.ACTIVITY` | `AaActivity_ExcludeActivity` | TField |  | Indicates whether the activity needs to be exempt from evaluation of restrictions specified in CONSTRAINTS property class. The options for this field are: YES - Activity will be excluded from constraint evaluation. NULL - Activity will be considered for constraint evaluation. |
| 13 | `AA.ACT.PRE.ACTIVITY` | `AaActivity_PreActivity` | TField |  | Activity defined here will be triggered before the current activity being processed. |
| 14 | `AA.ACT.POST.ACTIVITY` | `AaActivity_PostActivity` | TField |  | Activity defined here will be triggered after the current activity is processed. |
| 15 | `AA.ACT.RESERVED04` | `AaActivity_Reserved04` | TField |  |  |
| 16 | `AA.ACT.RESERVED03` | `AaActivity_Reserved03` | TField |  |  |
| 17 | `AA.ACT.RESERVED02` | `AaActivity_Reserved02` | TField |  |  |
| 18 | `AA.ACT.RESERVED01` | `AaActivity_Reserved01` | TField |  |  |
| 19 | `AA.ACT.OVERRIDE` | `AaActivity_Override` |  |  |  |
| 20 | `AA.ACT.RECORD.STATUS` | `AaActivity_RecordStatus` | String |  |  |
| 21 | `AA.ACT.CURR.NO` | `AaActivity_CurrNo` | String |  |  |
| 22 | `AA.ACT.INPUTTER` | `AaActivity_Inputter` |  |  |  |
| 23 | `AA.ACT.DATE.TIME` | `AaActivity_DateTime` |  |  |  |
| 24 | `AA.ACT.AUTHORISER` | `AaActivity_Authoriser` | String |  |  |
| 25 | `AA.ACT.CO.CODE` | `AaActivity_CoCode` | String |  |  |
| 26 | `AA.ACT.DEPT.CODE` | `AaActivity_DeptCode` | String |  |  |
| 27 | `AA.ACT.AUDITOR.CODE` | `AaActivity_AuditorCode` | String |  |  |
| 28 | `AA.ACT.AUDIT.DATE.TIME` | `AaActivity_AuditDateTime` | String |  |  |
| 29 | `AA.ACT.EVENT` | `AaActivity_Event` | TField |  | Indicates the event (the detail variant of the payload) that would be used for this Activity. Validation Rules: Should be a valid entry in MS.EVENT Maximum of 35 Alphanumeric characters. |
| 30 | `AA.ACT.EVENT.NAME` | `AaActivity_EventName` | TField |  | Contents should be defined in EB.LOOKUP of AA.EVENT.NAME. |
