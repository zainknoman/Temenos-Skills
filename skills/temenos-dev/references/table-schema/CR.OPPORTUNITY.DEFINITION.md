# CR.OPPORTUNITY.DEFINITION — Table Schema

> Source: `INSERTS/I_F.CR.OPPORTUNITY.DEFINITION` in `CR_Operational.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.OD.SHORT.DESC` | `CrOpportunityDefinition_ShortDesc` |  |  |  |
| 2 | `CR.OD.DESCRIPTION` | `CrOpportunityDefinition_Description` | TField |  | Text description of this template � describe the opportunity being tested for, and any other details to distinguish this opportunity. |
| 3 | `CR.OD.PRODUCT` | `CrOpportunityDefinition_Product` | TField |  | Product that this opportunity relates to. Validation Rules :If AA product is configured then it will accept PRODUCT value. If AA is not available, it will not be possible to enter a value here.If the OPPOR.DEF.ID (ID) field is the same as an AA.PRODUCT record, then the value in this field must also be the same PRODUCT record. |
| 4 | `CR.OD.PRODUCT.GRP` | `CrOpportunityDefinition_ProductGroup` |  |  |  |
| 5 | `CR.OD.CATEGORY` | `CrOpportunityDefinition_Category` | TField |  | Category that this Opportunity relates to. Validation Rules :Must be a valid id on CATEGORY table.Input Allowed only when PRODUCT or PRODUCT.GRP field is null and OPPOR.DEF.ID is free text. |
| 6 | `CR.OD.COMMUNICATION` | `CrOpportunityDefinition_Communication` | TField |  | Phase 2 Enhancement.Reserved for future use. |
| 7 | `CR.OD.DIRECTION` | `CrOpportunityDefinition_Direction` | TField |  | Campaigns may only reference Outbound opportunities. Propensities may only reference Inbound opportunities.Indicates whether this is an inbound opportunity, only to be communicated when the customer talks to the bank, or an outbound opportunity, where the bank initiates the communication Validation Rules :Options are : Inbound or Outbound. |
| 8 | `CR.OD.QUAL.RULE` | `CrOpportunityDefinition_QualRule` |  |  |  |
| 9 | `CR.OD.PROB.RULE` | `CrOpportunityDefinition_ProbRule` | TField |  | Phase 2 Enhancement. Reserved for future use. |
| 10 | `CR.OD.VALUE.RULE` | `CrOpportunityDefinition_ValueRule` | TField |  | Phase 2 Enhancement. Reserved for future use. |
| 11 | `CR.OD.OPPOR.CHANNEL` | `CrOpportunityDefinition_OpporChannel` |  |  |  |
| 12 | `CR.OD.OPPOR.WORKFLOW` | `CrOpportunityDefinition_OpporWorkflow` |  |  |  |
| 13 | `CR.OD.TRIGGER.STATUS` | `CrOpportunityDefinition_TriggerStatus` |  |  |  |
| 14 | `CR.OD.ORIG.PROCESS` | `CrOpportunityDefinition_OrigProcess` | TField |  | Process that will be initiated if the opportunity to be generated is taken up by the customer. Validation Rule:Must exist on PW.PROCESS.DEFINITION table |
| 15 | `CR.OD.OFS.SOURCE` | `CrOpportunityDefinition_OfsSource` | TField |  | OFS source ID that is used to create Process Workflow.Field FIELD.VAL on OFS.SOURCE record should not be set to YES. Validation Rules :Must be a valid id on OFS.SOURCE table |
| 16 | `CR.OD.OFS.VERSION` | `CrOpportunityDefinition_OfsVersion` | TField |  | Version of PW.PROCESS application. This will be used to create Process Workflow through OFS Validation Rules :Input must a version of PW.PROCESS |
| 17 | `CR.OD.RT.START.DATE` | `CrOpportunityDefinition_RtStartDate` | TField |  | Date from when a particular opportunity will be available to a customer. |
| 18 | `CR.OD.RT.DURATION` | `CrOpportunityDefinition_RtDuration` | TField |  | Duration of the days for which a particular opportunity will be available for the customer. |
| 19 | `CR.OD.DEFAULT.STATUS` | `CrOpportunityDefinition_DefaultStatus` | TField | Yes | This will be first status that is set for the opportunity when it is first created,OPPOR.STATUS field on CR.OPPORTUNITY will inherit the value entered on this field. Validation Rules :Mandatory Input.Must be a valid id on CR.OPPORTUNITY.STATUS table. |
| 20 | `CR.OD.REJECT.STATUS` | `CrOpportunityDefinition_RejectStatus` |  |  |  |
| 21 | `CR.OD.OPP.DURATION` | `CrOpportunityDefinition_OppDuration` | TField | Yes | This field is used to calculate the End date of the CR.OPPORTUNITY created. Validation Rules :Mandatory Input.Only a valid period will be allowed for input in this field. |
| 22 | `CR.OD.RESERVED.10` | `CrOpportunityDefinition_Reserved10` | TField |  |  |
| 23 | `CR.OD.RESERVED.9` | `CrOpportunityDefinition_Reserved9` | TField |  |  |
| 24 | `CR.OD.RESERVED.8` | `CrOpportunityDefinition_Reserved8` | TField |  |  |
| 25 | `CR.OD.RESERVED.7` | `CrOpportunityDefinition_Reserved7` | TField |  |  |
| 26 | `CR.OD.RESERVED.6` | `CrOpportunityDefinition_Reserved6` | TField |  |  |
| 27 | `CR.OD.RESERVED.5` | `CrOpportunityDefinition_Reserved5` | TField |  |  |
| 28 | `CR.OD.RESERVED.4` | `CrOpportunityDefinition_Reserved4` | TField |  |  |
| 29 | `CR.OD.RESERVED.3` | `CrOpportunityDefinition_Reserved3` | TField |  |  |
| 30 | `CR.OD.RESERVED.2` | `CrOpportunityDefinition_Reserved2` | TField |  |  |
| 31 | `CR.OD.RESERVED.1` | `CrOpportunityDefinition_Reserved1` | TField |  |  |
| 32 | `CR.OD.LOCAL.REF` | `CrOpportunityDefinition_LocalRef` |  |  |  |
| 33 | `CR.OD.RECORD.STATUS` | `CrOpportunityDefinition_RecordStatus` | String |  |  |
| 34 | `CR.OD.CURR.NO` | `CrOpportunityDefinition_CurrNo` | String |  |  |
| 35 | `CR.OD.INPUTTER` | `CrOpportunityDefinition_Inputter` |  |  |  |
| 36 | `CR.OD.DATE.TIME` | `CrOpportunityDefinition_DateTime` |  |  |  |
| 37 | `CR.OD.AUTHORISER` | `CrOpportunityDefinition_Authoriser` | String |  |  |
| 38 | `CR.OD.CO.CODE` | `CrOpportunityDefinition_CoCode` | String |  |  |
| 39 | `CR.OD.DEPT.CODE` | `CrOpportunityDefinition_DeptCode` | String |  |  |
| 40 | `CR.OD.AUDITOR.CODE` | `CrOpportunityDefinition_AuditorCode` | String |  |  |
| 41 | `CR.OD.AUDIT.DATE.TIME` | `CrOpportunityDefinition_AuditDateTime` | String |  |  |
