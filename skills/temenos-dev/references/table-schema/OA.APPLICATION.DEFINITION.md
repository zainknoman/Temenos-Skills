# OA.APPLICATION.DEFINITION — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.DEFINITION` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.ADF.DESCRIPTION` | `OaApplicationDefinition_Description` |  |  |  |
| 2 | `OA.ADF.FULL.DESC` | `OaApplicationDefinition_FullDesc` |  |  |  |
| 3 | `OA.ADF.PARENT.PURPOSE` | `OaApplicationDefinition_ParentPurpose` | TField |  |  |
| 4 | `OA.ADF.DOMAIN.CLASS` | `OaApplicationDefinition_DomainClass` |  |  |  |
| 5 | `OA.ADF.ROLE` | `OaApplicationDefinition_Role` |  |  |  |
| 6 | `OA.ADF.MINIMUM.ROLE` | `OaApplicationDefinition_MinimumRole` |  |  |  |
| 7 | `OA.ADF.MAXIMUM.ROLE` | `OaApplicationDefinition_MaximumRole` |  |  |  |
| 8 | `OA.ADF.DOMAIN.TYPE` | `OaApplicationDefinition_DomainType` |  |  |  |
| 9 | `OA.ADF.MIN.DOMAIN.PART` | `OaApplicationDefinition_MinDomainPart` |  |  |  |
| 10 | `OA.ADF.MAX.DOMAIN.PART` | `OaApplicationDefinition_MaxDomainPart` |  |  |  |
| 11 | `OA.ADF.FORM` | `OaApplicationDefinition_Form` |  |  |  |
| 12 | `OA.ADF.ATTRIBUTE` | `OaApplicationDefinition_Attribute` |  |  |  |
| 13 | `OA.ADF.RESERVED.15` | `OaApplicationDefinition_Reserved15` | TField |  |  |
| 14 | `OA.ADF.APPLICATION.OWNER` | `OaApplicationDefinition_ApplicationOwner` | TField |  | This field will hold the owner which would refer to OA.OWNERSHIP.DEFINITION table where the user has mapped dossier owner against each rule |
| 15 | `OA.ADF.STATUS.CODE` | `OaApplicationDefinition_StatusCode` |  |  |  |
| 16 | `OA.ADF.STATUS.TYPE` | `OaApplicationDefinition_StatusType` |  |  |  |
| 17 | `OA.ADF.STATUS.RULE` | `OaApplicationDefinition_StatusRule` |  |  |  |
| 18 | `OA.ADF.STATUS.VARIABLE` | `OaApplicationDefinition_StatusVariable` |  |  |  |
| 19 | `OA.ADF.STATUS.VARIABLE.VALUE` | `OaApplicationDefinition_StatusVariableValue` |  |  |  |
| 20 | `OA.ADF.CONSOLIDATION.RULE` | `OaApplicationDefinition_ConsolidationRule` |  |  |  |
| 21 | `OA.ADF.DOMAIN` | `OaApplicationDefinition_Domain` |  |  |  |
| 22 | `OA.ADF.OWNER` | `OaApplicationDefinition_Owner` |  |  |  |
| 23 | `OA.ADF.FORMLET` | `OaApplicationDefinition_Formlet` |  |  |  |
| 24 | `OA.ADF.EVIDENCE.REQUIREMENT` | `OaApplicationDefinition_EvidenceRequirement` |  |  |  |
| 25 | `OA.ADF.PROCESS.ACTIVITY` | `OaApplicationDefinition_ProcessActivity` |  |  |  |
| 26 | `OA.ADF.PW.DEFINITION.ID` | `OaApplicationDefinition_PwDefinitionId` | TField |  | This field indicates the name of the Definition Manager Object. The Nature of the Object depends on the CLASS.TYPE that the object uses. For Example if the class type is PROPERTY.CLASS , the object will be a PRODUCT .If the class type is FORMLET.CLASS the object will be a FORM 1) Validation Rules a. Non Input. b. System Maintained. Based on the ID of the Definition Manager record .The part between the first character and the Second character in the ID is the REFERENCE c. Input should be a valid AA.CLASS.TYPE record |
| 27 | `OA.ADF.RESERVED.12` | `OaApplicationDefinition_Reserved12` | TField |  |  |
| 28 | `OA.ADF.RESERVED.11` | `OaApplicationDefinition_Reserved11` | TField |  |  |
| 29 | `OA.ADF.ADVICE.TYPE` | `OaApplicationDefinition_AdviceType` |  |  |  |
| 30 | `OA.ADF.STATUS.TRIGGER.RULE` | `OaApplicationDefinition_StatusTriggerRule` |  |  |  |
| 31 | `OA.ADF.CONSTRAINT.RULE` | `OaApplicationDefinition_ConstraintRule` |  |  |  |
| 32 | `OA.ADF.RESERVED.22` | `OaApplicationDefinition_Reserved22` |  |  |  |
| 33 | `OA.ADF.RESERVED.21` | `OaApplicationDefinition_Reserved21` |  |  |  |
| 34 | `OA.ADF.RESERVED.20` | `OaApplicationDefinition_Reserved20` |  |  |  |
| 35 | `OA.ADF.DEF.RECIPIENT.ROLE` | `OaApplicationDefinition_DefRecipientRole` |  |  |  |
| 36 | `OA.ADF.DEF.RECIPIENT.SEQ` | `OaApplicationDefinition_DefRecipientSeq` |  |  |  |
| 37 | `OA.ADF.AVL.RECIPIENT.ROLE` | `OaApplicationDefinition_AvlRecipientRole` |  |  |  |
| 38 | `OA.ADF.AVL.RECIPIENT.SEQ` | `OaApplicationDefinition_AvlRecipientSeq` |  |  |  |
| 39 | `OA.ADF.RESERVED.19` | `OaApplicationDefinition_Reserved19` |  |  |  |
| 40 | `OA.ADF.RESERVED.18` | `OaApplicationDefinition_Reserved18` |  |  |  |
| 41 | `OA.ADF.RESERVED.17` | `OaApplicationDefinition_Reserved17` |  |  |  |
| 42 | `OA.ADF.ACTION` | `OaApplicationDefinition_Action` | TField |  |  |
| 43 | `OA.ADF.EXPIRY.DATE` | `OaApplicationDefinition_ExpiryDate` | TField | No | This is the date beyond which the PURPOSE represented by the ID of this record can no longer be used for an OA Application 2)Optional Input 3) Validation Rules a. Date provided should be in the future. b.T24 Date Input |
| 44 | `OA.ADF.PUBLISH.STATUS` | `OaApplicationDefinition_PublishStatus` | TField |  | This field will contain the result of the publishing effort 1) Validation Rules a. Non Input. b. System Maintained c. Allowed values are : Completed Successfully or Completed with Errors |
| 45 | `OA.ADF.PUBLISH.ERROR` | `OaApplicationDefinition_PublishError` |  |  |  |
| 46 | `OA.ADF.ERROR.SUGGESTION` | `OaApplicationDefinition_ErrorSuggestion` |  |  |  |
| 47 | `OA.ADF.REFERENCE` | `OaApplicationDefinition_Reference` | TField |  |  |
| 48 | `OA.ADF.VERSION` | `OaApplicationDefinition_Version` | TField |  | A Purpose is Versionned . This means that more than one version of the same exist in the system. Depending on the nature of the object, updates may be performed on existing version without the need to advance the object to its NEXT VERSION in the sequence. 1) Validation Rules a. Non Input. b. System Maintained. Based on the ID of the Definition Manager record .The part between the second character and the third character in the ID is the VERSION |
| 49 | `OA.ADF.DEFINITION.VERSION` | `OaApplicationDefinition_DefinitionVersion` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 50 | `OA.ADF.STAGE.TO.LOCK` | `OaApplicationDefinition_StageToLock` |  |  |  |
| 51 | `OA.ADF.STAGE.DEFAULT` | `OaApplicationDefinition_StageDefault` |  |  |  |
| 52 | `OA.ADF.STAGE.NOINPUT.FIELD` | `OaApplicationDefinition_StageNoinputField` |  |  |  |
| 53 | `OA.ADF.STAGE.NOINPUT.FLD.RULE` | `OaApplicationDefinition_StageNoinputFldRule` |  |  |  |
| 54 | `OA.ADF.STAGE.INPUT.FIELD` | `OaApplicationDefinition_StageInputField` |  |  |  |
| 55 | `OA.ADF.STAGE.INPUT.FLD.RULE` | `OaApplicationDefinition_StageInputFldRule` |  |  |  |
| 56 | `OA.ADF.STAGE.RULE` | `OaApplicationDefinition_StageRule` |  |  |  |
| 57 | `OA.ADF.FULFILMENT.TYPE` | `OaApplicationDefinition_FulfilmentType` |  |  |  |
| 58 | `OA.ADF.DECISION.TYPE` | `OaApplicationDefinition_DecisionType` |  |  |  |
| 59 | `OA.ADF.RESERVED.1` | `OaApplicationDefinition_Reserved1` | TField |  |  |
| 60 | `OA.ADF.LOCAL.REF` | `OaApplicationDefinition_LocalRef` |  |  |  |
| 61 | `OA.ADF.OVERRIDE` | `OaApplicationDefinition_Override` |  |  |  |
| 62 | `OA.ADF.RECORD.STATUS` | `OaApplicationDefinition_RecordStatus` | String |  |  |
| 63 | `OA.ADF.CURR.NO` | `OaApplicationDefinition_CurrNo` | String |  |  |
| 64 | `OA.ADF.INPUTTER` | `OaApplicationDefinition_Inputter` |  |  |  |
| 65 | `OA.ADF.DATE.TIME` | `OaApplicationDefinition_DateTime` |  |  |  |
| 66 | `OA.ADF.AUTHORISER` | `OaApplicationDefinition_Authoriser` | String |  |  |
| 67 | `OA.ADF.CO.CODE` | `OaApplicationDefinition_CoCode` | String |  |  |
| 68 | `OA.ADF.DEPT.CODE` | `OaApplicationDefinition_DeptCode` | String |  |  |
| 69 | `OA.ADF.AUDITOR.CODE` | `OaApplicationDefinition_AuditorCode` | String |  |  |
| 70 | `OA.ADF.AUDIT.DATE.TIME` | `OaApplicationDefinition_AuditDateTime` | String |  |  |
| 71 | `OA.ADF.ENTITY.TYPE` | `OaApplicationDefinition_EntityType` |  |  |  |
