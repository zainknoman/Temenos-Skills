# OA.APPLICATION.STAGES.DEFINITION — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.STAGES.DEFINITION` in `OA_Stages.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.SGD.DESCRIPTION` | `OaApplicationStagesDefinition_Description` |  |  |  |
| 2 | `OA.SGD.FULL.DESC` | `OaApplicationStagesDefinition_FullDesc` | TField |  | Full Description of the Stages |
| 3 | `OA.SGD.STAGE` | `OaApplicationStagesDefinition_Stage` |  |  |  |
| 4 | `OA.SGD.RETURN` | `OaApplicationStagesDefinition_Return` |  |  |  |
| 5 | `OA.SGD.RETURN.STAGE` | `OaApplicationStagesDefinition_ReturnStage` |  |  |  |
| 6 | `OA.SGD.STAGE.OWNER` | `OaApplicationStagesDefinition_StageOwner` |  |  |  |
| 7 | `OA.SGD.RESERVED.11` | `OaApplicationStagesDefinition_Reserved11` |  |  |  |
| 8 | `OA.SGD.RESERVED.10` | `OaApplicationStagesDefinition_Reserved10` |  |  |  |
| 9 | `OA.SGD.RESERVED.9` | `OaApplicationStagesDefinition_Reserved9` | TField |  |  |
| 10 | `OA.SGD.RESERVED.8` | `OaApplicationStagesDefinition_Reserved8` | TField |  |  |
| 11 | `OA.SGD.ACTION` | `OaApplicationStagesDefinition_Action` | TField |  | Action that the system should perform on authorization of the record. Allowed value is PUBLISH |
| 12 | `OA.SGD.PUBLISH.STATUS` | `OaApplicationStagesDefinition_PublishStatus` | TField |  | Status resulting from the Action performed. Allowed values are Published Successfully or Published with errors |
| 13 | `OA.SGD.PUBLISH.DATE` | `OaApplicationStagesDefinition_PublishDate` | TField |  | Date the Action of Publish is Performed |
| 14 | `OA.SGD.EXPIRY.DATE` | `OaApplicationStagesDefinition_ExpiryDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 15 | `OA.SGD.PUBLISH.ERROR` | `OaApplicationStagesDefinition_PublishError` |  |  |  |
| 16 | `OA.SGD.ERROR.SUGGESTION` | `OaApplicationStagesDefinition_ErrorSuggestion` |  |  |  |
| 17 | `OA.SGD.REFERENCE` | `OaApplicationStagesDefinition_Reference` | TField |  | The Purpose Code contained in the ID of the Definition |
| 18 | `OA.SGD.VERSION` | `OaApplicationStagesDefinition_Version` | TField |  | The version Number contained in the Id of the definiton |
| 19 | `OA.SGD.RESERVED.5` | `OaApplicationStagesDefinition_Reserved5` | TField |  |  |
| 20 | `OA.SGD.RESERVED.4` | `OaApplicationStagesDefinition_Reserved4` | TField |  |  |
| 21 | `OA.SGD.RESERVED.3` | `OaApplicationStagesDefinition_Reserved3` | TField |  |  |
| 22 | `OA.SGD.RESERVED.2` | `OaApplicationStagesDefinition_Reserved2` | TField |  |  |
| 23 | `OA.SGD.RESERVED.1` | `OaApplicationStagesDefinition_Reserved1` | TField |  |  |
| 24 | `OA.SGD.LOCAL.REF` | `OaApplicationStagesDefinition_LocalRef` |  |  |  |
| 25 | `OA.SGD.OVERRIDE` | `OaApplicationStagesDefinition_Override` |  |  |  |
| 26 | `OA.SGD.RECORD.STATUS` | `OaApplicationStagesDefinition_RecordStatus` | String |  |  |
| 27 | `OA.SGD.CURR.NO` | `OaApplicationStagesDefinition_CurrNo` | String |  |  |
| 28 | `OA.SGD.INPUTTER` | `OaApplicationStagesDefinition_Inputter` |  |  |  |
| 29 | `OA.SGD.DATE.TIME` | `OaApplicationStagesDefinition_DateTime` |  |  |  |
| 30 | `OA.SGD.AUTHORISER` | `OaApplicationStagesDefinition_Authoriser` | String |  |  |
| 31 | `OA.SGD.CO.CODE` | `OaApplicationStagesDefinition_CoCode` | String |  |  |
| 32 | `OA.SGD.DEPT.CODE` | `OaApplicationStagesDefinition_DeptCode` | String |  |  |
| 33 | `OA.SGD.AUDITOR.CODE` | `OaApplicationStagesDefinition_AuditorCode` | String |  |  |
| 34 | `OA.SGD.AUDIT.DATE.TIME` | `OaApplicationStagesDefinition_AuditDateTime` | String |  |  |
