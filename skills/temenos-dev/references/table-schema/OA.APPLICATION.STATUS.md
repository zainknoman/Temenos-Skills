# OA.APPLICATION.STATUS — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.STATUS` in `OA_Status.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.AS.STAGE` | `OaApplicationStatus_Stage` | TField |  | This field specifies the Current stage of the application. It could be used to identify the current stage of the application to initiate the next processing which can be PW activity. |
| 2 | `OA.AS.STATUS.CODE` | `OaApplicationStatus_StatusCode` |  |  |  |
| 3 | `OA.AS.STATUS.VALUE` | `OaApplicationStatus_StatusValue` |  |  |  |
| 4 | `OA.AS.FORM.REFERENCE` | `OaApplicationStatus_FormReference` |  |  |  |
| 5 | `OA.AS.DOMAIN.TYPE` | `OaApplicationStatus_DomainType` |  |  |  |
| 6 | `OA.AS.ROLE` | `OaApplicationStatus_Role` |  |  |  |
| 7 | `OA.AS.SEQUENCE` | `OaApplicationStatus_Sequence` |  |  |  |
| 8 | `OA.AS.FORM.ID` | `OaApplicationStatus_FormId` |  |  |  |
| 9 | `OA.AS.FORM.DATA.STATUS` | `OaApplicationStatus_FormDataStatus` |  |  |  |
| 10 | `OA.AS.FORM.EVIDENCE.STATUS` | `OaApplicationStatus_FormEvidenceStatus` |  |  |  |
| 11 | `OA.AS.FORM.VERIFICATION.STATUS` | `OaApplicationStatus_FormVerificationStatus` |  |  |  |
| 12 | `OA.AS.RESERVED.10` | `OaApplicationStatus_Reserved10` |  |  |  |
| 13 | `OA.AS.RESERVED.9` | `OaApplicationStatus_Reserved9` |  |  |  |
| 14 | `OA.AS.RESERVED.8` | `OaApplicationStatus_Reserved8` |  |  |  |
| 15 | `OA.AS.RESERVED.7` | `OaApplicationStatus_Reserved7` |  |  |  |
| 16 | `OA.AS.RESERVED.6` | `OaApplicationStatus_Reserved6` |  |  |  |
| 17 | `OA.AS.FORM.OWNER` | `OaApplicationStatus_FormOwner` |  |  |  |
| 18 | `OA.AS.FORM.OWNER.DATA.STATUS` | `OaApplicationStatus_FormOwnerDataStatus` |  |  |  |
| 19 | `OA.AS.FORM.OWNER.EVIDENCE.STATUS` | `OaApplicationStatus_FormOwnerEvidenceStatus` |  |  |  |
| 20 | `OA.AS.FORM.OWNER.VERIFICATION` | `OaApplicationStatus_FormOwnerVerification` |  |  |  |
| 21 | `OA.AS.FORMLET` | `OaApplicationStatus_Formlet` |  |  |  |
| 22 | `OA.AS.FORMLET.CLASS` | `OaApplicationStatus_FormletClass` |  |  |  |
| 23 | `OA.AS.FORMLET.RECORD.ID` | `OaApplicationStatus_FormletRecordId` |  |  |  |
| 24 | `OA.AS.FORMLET.OWNER` | `OaApplicationStatus_FormletOwner` |  |  |  |
| 25 | `OA.AS.FORMLET.EVIDENCE.STATUS` | `OaApplicationStatus_FormletEvidenceStatus` |  |  |  |
| 26 | `OA.AS.FORMLET.VERIFICATION` | `OaApplicationStatus_FormletVerification` |  |  |  |
| 27 | `OA.AS.FORMLET.STATUS` | `OaApplicationStatus_FormletStatus` |  |  |  |
| 28 | `OA.AS.DATA.VERIFICATION.REF` | `OaApplicationStatus_DataVerificationRef` |  |  |  |
| 29 | `OA.AS.FORMLET.ATTRIBUTE` | `OaApplicationStatus_FormletAttribute` |  |  |  |
| 30 | `OA.AS.RESERVED.3` | `OaApplicationStatus_Reserved3` |  |  |  |
| 31 | `OA.AS.RESERVED.2` | `OaApplicationStatus_Reserved2` |  |  |  |
| 32 | `OA.AS.RESERVED.1` | `OaApplicationStatus_Reserved1` |  |  |  |
| 33 | `OA.AS.EVIDENCE.REQUIREMENT` | `OaApplicationStatus_EvidenceRequirement` |  |  |  |
| 34 | `OA.AS.EVIDENCE.REQ.STATUS` | `OaApplicationStatus_EvidenceReqStatus` |  |  |  |
| 35 | `OA.AS.PW.PROCESS.ID` | `OaApplicationStatus_PwProcessId` | TField |  | This field will hold the PW.PROCESS record id which is linked to the application for the specific purpose. |
| 36 | `OA.AS.STAGE.VERSION` | `OaApplicationStatus_StageVersion` | TField |  | This field will hold the version of the current stage of the application. |
| 37 | `OA.AS.DATA.MODEL.CATEGORY` | `OaApplicationStatus_DataModelCategory` |  |  |  |
| 38 | `OA.AS.DATA.MODEL` | `OaApplicationStatus_DataModel` |  |  |  |
| 39 | `OA.AS.DATA` | `OaApplicationStatus_Data` |  |  |  |
| 40 | `OA.AS.DATA.REFERENCE` | `OaApplicationStatus_DataReference` |  |  |  |
| 41 | `OA.AS.ADVICE.TYPE` | `OaApplicationStatus_AdviceType` |  |  |  |
| 42 | `OA.AS.ADVICE.REFERENCE` | `OaApplicationStatus_AdviceReference` |  |  |  |
| 43 | `OA.AS.FULFILMENT.TYPE` | `OaApplicationStatus_FulfilmentType` |  |  |  |
| 44 | `OA.AS.FULFILMENT.VERSION` | `OaApplicationStatus_FulfilmentVersion` |  |  |  |
| 45 | `OA.AS.FULFILMENT.MAP.REFERENCE` | `OaApplicationStatus_FulfilmentMapReference` |  |  |  |
| 46 | `OA.AS.TARGET.APPLICATION` | `OaApplicationStatus_TargetApplication` |  |  |  |
| 47 | `OA.AS.TARGET.REFERENCE` | `OaApplicationStatus_TargetReference` |  |  |  |
| 48 | `OA.AS.TARGET.RESULT` | `OaApplicationStatus_TargetResult` |  |  |  |
| 49 | `OA.AS.DECISION.TYPE` | `OaApplicationStatus_DecisionType` |  |  |  |
| 50 | `OA.AS.DECISION.RESULT` | `OaApplicationStatus_DecisionResult` |  |  |  |
| 51 | `OA.AS.DECISION.METHOD` | `OaApplicationStatus_DecisionMethod` |  |  |  |
| 52 | `OA.AS.MAPPING.LOG.REF` | `OaApplicationStatus_MappingLogRef` |  |  |  |
| 53 | `OA.AS.MAPPING.LOG.STATUS` | `OaApplicationStatus_MappingLogStatus` |  |  |  |
| 54 | `OA.AS.OWNER` | `OaApplicationStatus_Owner` | TField |  | This field will hold the Dossier Owner for the current purpose. |
| 55 | `OA.AS.STAGE.OWNER` | `OaApplicationStatus_StageOwner` | TField |  | This field will hold the owner of the current stage. |
