# OA.APPLICATION.CATALOG — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.CATALOG` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.FCAT.DESCRIPTION` | `OaApplicationCatalog_Description` |  |  |  |
| 2 | `OA.FCAT.FULL.DESC` | `OaApplicationCatalog_FullDesc` |  |  |  |
| 3 | `OA.FCAT.PARENT.PURPOSE` | `OaApplicationCatalog_ParentPurpose` | TField |  |  |
| 4 | `OA.FCAT.DOMAIN.CLASS` | `OaApplicationCatalog_DomainClass` |  |  |  |
| 5 | `OA.FCAT.ROLE` | `OaApplicationCatalog_Role` |  |  |  |
| 6 | `OA.FCAT.MINIMUM.ROLE` | `OaApplicationCatalog_MinimumRole` |  |  |  |
| 7 | `OA.FCAT.MAXIMUM.ROLE` | `OaApplicationCatalog_MaximumRole` |  |  |  |
| 8 | `OA.FCAT.DOMAIN.TYPE` | `OaApplicationCatalog_DomainType` |  |  |  |
| 9 | `OA.FCAT.MIN.DOMAIN.PART` | `OaApplicationCatalog_MinDomainPart` |  |  |  |
| 10 | `OA.FCAT.MAX.DOMAIN.PART` | `OaApplicationCatalog_MaxDomainPart` |  |  |  |
| 11 | `OA.FCAT.FORM` | `OaApplicationCatalog_Form` |  |  |  |
| 12 | `OA.FCAT.ATTRIBUTE` | `OaApplicationCatalog_Attribute` |  |  |  |
| 13 | `OA.FCAT.RESERVED.15` | `OaApplicationCatalog_Reserved15` | TField |  |  |
| 14 | `OA.FCAT.APPLICATION.OWNER` | `OaApplicationCatalog_ApplicationOwner` | TField |  | This field will hold the owner which would refer to OA.OWNERSHIP.DEFINITION table where the user has mapped dossier owner against each rule |
| 15 | `OA.FCAT.STATUS.CODE` | `OaApplicationCatalog_StatusCode` |  |  |  |
| 16 | `OA.FCAT.STATUS.TYPE` | `OaApplicationCatalog_StatusType` |  |  |  |
| 17 | `OA.FCAT.STATUS.RULE` | `OaApplicationCatalog_StatusRule` |  |  |  |
| 18 | `OA.FCAT.STATUS.VARIABLE` | `OaApplicationCatalog_StatusVariable` |  |  |  |
| 19 | `OA.FCAT.STATUS.VARIABLE.VALUE` | `OaApplicationCatalog_StatusVariableValue` |  |  |  |
| 20 | `OA.FCAT.CONSOLIDATION.RULE` | `OaApplicationCatalog_ConsolidationRule` |  |  |  |
| 21 | `OA.FCAT.DOMAIN` | `OaApplicationCatalog_Domain` |  |  |  |
| 22 | `OA.FCAT.OWNER` | `OaApplicationCatalog_Owner` |  |  |  |
| 23 | `OA.FCAT.FORMLET` | `OaApplicationCatalog_Formlet` |  |  |  |
| 24 | `OA.FCAT.EVIDENCE.REQUIREMENT` | `OaApplicationCatalog_EvidenceRequirement` |  |  |  |
| 25 | `OA.FCAT.PROCESS.ACTIVITY` | `OaApplicationCatalog_ProcessActivity` |  |  |  |
| 26 | `OA.FCAT.PW.DEFINITION.ID` | `OaApplicationCatalog_PwDefinitionId` | TField |  | This field indicates the name of the Definition Manager Object. The Nature of the Object depends on the CLASS.TYPE that the object uses. For Example if the class type is PROPERTY.CLASS , the object will be a PRODUCT. If the class type is FORMLET.CLASS the object will be a FORM 1) Validation Rules a. Non Input. b. System Maintained. Based on the ID of the Definition Manager record .The part between the first "-" character and the Second '-' character in the ID is the REFERENCE c. Input should be a valid AA.CLASS.TYPE record |
| 27 | `OA.FCAT.RESERVED.12` | `OaApplicationCatalog_Reserved12` | TField |  |  |
| 28 | `OA.FCAT.RESERVED.11` | `OaApplicationCatalog_Reserved11` | TField |  |  |
| 29 | `OA.FCAT.ADVICE.TYPE` | `OaApplicationCatalog_AdviceType` |  |  |  |
| 30 | `OA.FCAT.STATUS.TRIGGER.RULE` | `OaApplicationCatalog_StatusTriggerRule` |  |  |  |
| 31 | `OA.FCAT.CONSTRAINT.RULE` | `OaApplicationCatalog_ConstraintRule` |  |  |  |
| 32 | `OA.FCAT.RESERVED.22` | `OaApplicationCatalog_Reserved22` |  |  |  |
| 33 | `OA.FCAT.RESERVED.21` | `OaApplicationCatalog_Reserved21` |  |  |  |
| 34 | `OA.FCAT.RESERVED.20` | `OaApplicationCatalog_Reserved20` |  |  |  |
| 35 | `OA.FCAT.DEF.RECIPIENT.ROLE` | `OaApplicationCatalog_DefRecipientRole` |  |  |  |
| 36 | `OA.FCAT.DEF.RECIPIENT.SEQ` | `OaApplicationCatalog_DefRecipientSeq` |  |  |  |
| 37 | `OA.FCAT.AVL.RECIPIENT.ROLE` | `OaApplicationCatalog_AvlRecipientRole` |  |  |  |
| 38 | `OA.FCAT.AVL.RECIPIENT.SEQ` | `OaApplicationCatalog_AvlRecipientSeq` |  |  |  |
| 39 | `OA.FCAT.RESERVED.19` | `OaApplicationCatalog_Reserved19` |  |  |  |
| 40 | `OA.FCAT.RESERVED.18` | `OaApplicationCatalog_Reserved18` |  |  |  |
| 41 | `OA.FCAT.RESERVED.17` | `OaApplicationCatalog_Reserved17` |  |  |  |
| 42 | `OA.FCAT.ACTION` | `OaApplicationCatalog_Action` | TField |  |  |
| 43 | `OA.FCAT.EXPIRY.DATE` | `OaApplicationCatalog_ExpiryDate` | TField | No | This is the date beyond which the PURPOSE represented by the ID of this record can no longer be used for an OA Application 2)Optional Input 3) Validation Rules a. Date provided should be in the future. b.T24 Date Input |
| 44 | `OA.FCAT.PUBLISH.STATUS` | `OaApplicationCatalog_PublishStatus` | TField |  | This field will contain the result of the publishing effort 1) Validation Rules a. Non Input. b. System Maintained c. Allowed values are : Completed Successfully or Completed with Errors |
| 45 | `OA.FCAT.PUBLISH.ERROR` | `OaApplicationCatalog_PublishError` |  |  |  |
| 46 | `OA.FCAT.ERROR.SUGGESTION` | `OaApplicationCatalog_ErrorSuggestion` |  |  |  |
| 47 | `OA.FCAT.REFERENCE` | `OaApplicationCatalog_Reference` | TField |  |  |
| 48 | `OA.FCAT.VERSION` | `OaApplicationCatalog_Version` | TField |  | A Purpose is Versionned . This means that more than one version of the same exist in the system. Depending on the nature of the object, updates may be performed on existing version without the need to advance the object to its NEXT VERSION in the sequence. 1) Validation Rules a. Non Input. b. System Maintained. Based on the ID of the Definition Manager record .The part between the second "-" character and the third '-' character in the ID is the VERSION |
| 49 | `OA.FCAT.DEFINITION.VERSION` | `OaApplicationCatalog_DefinitionVersion` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 50 | `OA.FCAT.STAGE.TO.LOCK` | `OaApplicationCatalog_StageToLock` |  |  |  |
| 51 | `OA.FCAT.STAGE.DEFAULT` | `OaApplicationCatalog_StageDefault` |  |  |  |
| 52 | `OA.FCAT.STAGE.NOINPUT.FIELD` | `OaApplicationCatalog_StageNoinputField` |  |  |  |
| 53 | `OA.FCAT.STAGE.NOINPUT.FLD.RULE` | `OaApplicationCatalog_StageNoinputFldRule` |  |  |  |
| 54 | `OA.FCAT.STAGE.INPUT.FIELD` | `OaApplicationCatalog_StageInputField` |  |  |  |
| 55 | `OA.FCAT.STAGE.INPUT.FLD.RULE` | `OaApplicationCatalog_StageInputFldRule` |  |  |  |
| 56 | `OA.FCAT.STAGE.RULE` | `OaApplicationCatalog_StageRule` |  |  |  |
| 57 | `OA.FCAT.FULFILMENT.TYPE` | `OaApplicationCatalog_FulfilmentType` |  |  |  |
| 58 | `OA.FCAT.DECISION.TYPE` | `OaApplicationCatalog_DecisionType` |  |  |  |
| 59 | `OA.FCAT.RESERVED.1` | `OaApplicationCatalog_Reserved1` | TField |  |  |
| 60 | `OA.FCAT.LOCAL.REF` | `OaApplicationCatalog_LocalRef` |  |  |  |
| 61 | `OA.FCAT.OVERRIDE` | `OaApplicationCatalog_Override` |  |  |  |
| 62 | `OA.FCAT.RECORD.STATUS` | `OaApplicationCatalog_RecordStatus` | String |  |  |
| 63 | `OA.FCAT.CURR.NO` | `OaApplicationCatalog_CurrNo` | String |  |  |
| 64 | `OA.FCAT.INPUTTER` | `OaApplicationCatalog_Inputter` |  |  |  |
| 65 | `OA.FCAT.DATE.TIME` | `OaApplicationCatalog_DateTime` |  |  |  |
| 66 | `OA.FCAT.AUTHORISER` | `OaApplicationCatalog_Authoriser` | String |  |  |
| 67 | `OA.FCAT.CO.CODE` | `OaApplicationCatalog_CoCode` | String |  |  |
| 68 | `OA.FCAT.DEPT.CODE` | `OaApplicationCatalog_DeptCode` | String |  |  |
| 69 | `OA.FCAT.AUDITOR.CODE` | `OaApplicationCatalog_AuditorCode` | String |  |  |
| 70 | `OA.FCAT.AUDIT.DATE.TIME` | `OaApplicationCatalog_AuditDateTime` | String |  |  |
| 71 | `OA.FCAT.ENTITY.TYPE` | `OaApplicationCatalog_EntityType` |  |  |  |
