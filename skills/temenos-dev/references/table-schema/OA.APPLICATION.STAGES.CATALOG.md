# OA.APPLICATION.STAGES.CATALOG — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.STAGES.CATALOG` in `OA_Stages.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.SGC.DESCRIPTION` | `OaApplicationStagesCatalog_Description` |  |  |  |
| 2 | `OA.SGC.FULL.DESC` | `OaApplicationStagesCatalog_FullDesc` | TField |  | Full Description of the Stages |
| 3 | `OA.SGC.STAGE` | `OaApplicationStagesCatalog_Stage` |  |  |  |
| 4 | `OA.SGC.RETURN` | `OaApplicationStagesCatalog_Return` |  |  |  |
| 5 | `OA.SGC.RETURN.STAGE` | `OaApplicationStagesCatalog_ReturnStage` |  |  |  |
| 6 | `OA.SGC.STAGE.OWNER` | `OaApplicationStagesCatalog_StageOwner` |  |  |  |
| 7 | `OA.SGC.RESERVED.11` | `OaApplicationStagesCatalog_Reserved11` |  |  |  |
| 8 | `OA.SGC.RESERVED.10` | `OaApplicationStagesCatalog_Reserved10` |  |  |  |
| 9 | `OA.SGC.RESERVED.9` | `OaApplicationStagesCatalog_Reserved9` | TField |  |  |
| 10 | `OA.SGC.RESERVED.8` | `OaApplicationStagesCatalog_Reserved8` | TField |  |  |
| 11 | `OA.SGC.ACTION` | `OaApplicationStagesCatalog_Action` | TField |  | Action that the system should perform on authorization of the record. Allowed value is PUBLISH |
| 12 | `OA.SGC.PUBLISH.STATUS` | `OaApplicationStagesCatalog_PublishStatus` | TField |  | Status resulting from the Action performed. Allowed values are Published Successfully or Published with errors |
| 13 | `OA.SGC.PUBLISH.DATE` | `OaApplicationStagesCatalog_PublishDate` | TField |  | Date the Action of Publish is Performed |
| 14 | `OA.SGC.EXPIRY.DATE` | `OaApplicationStagesCatalog_ExpiryDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 15 | `OA.SGC.PUBLISH.ERROR` | `OaApplicationStagesCatalog_PublishError` |  |  |  |
| 16 | `OA.SGC.ERROR.SUGGESTION` | `OaApplicationStagesCatalog_ErrorSuggestion` |  |  |  |
| 17 | `OA.SGC.REFERENCE` | `OaApplicationStagesCatalog_Reference` | TField |  | The Purpose Code contained in the ID of the Definition |
| 18 | `OA.SGC.VERSION` | `OaApplicationStagesCatalog_Version` | TField |  | The version Number contained in the Id of the definiton |
| 19 | `OA.SGC.RESERVED.5` | `OaApplicationStagesCatalog_Reserved5` | TField |  |  |
| 20 | `OA.SGC.RESERVED.4` | `OaApplicationStagesCatalog_Reserved4` | TField |  |  |
| 21 | `OA.SGC.RESERVED.3` | `OaApplicationStagesCatalog_Reserved3` | TField |  |  |
| 22 | `OA.SGC.RESERVED.2` | `OaApplicationStagesCatalog_Reserved2` | TField |  |  |
| 23 | `OA.SGC.RESERVED.1` | `OaApplicationStagesCatalog_Reserved1` | TField |  |  |
| 24 | `OA.SGC.LOCAL.REF` | `OaApplicationStagesCatalog_LocalRef` |  |  |  |
| 25 | `OA.SGC.OVERRIDE` | `OaApplicationStagesCatalog_Override` |  |  |  |
| 26 | `OA.SGC.RECORD.STATUS` | `OaApplicationStagesCatalog_RecordStatus` | String |  |  |
| 27 | `OA.SGC.CURR.NO` | `OaApplicationStagesCatalog_CurrNo` | String |  |  |
| 28 | `OA.SGC.INPUTTER` | `OaApplicationStagesCatalog_Inputter` |  |  |  |
| 29 | `OA.SGC.DATE.TIME` | `OaApplicationStagesCatalog_DateTime` |  |  |  |
| 30 | `OA.SGC.AUTHORISER` | `OaApplicationStagesCatalog_Authoriser` | String |  |  |
| 31 | `OA.SGC.CO.CODE` | `OaApplicationStagesCatalog_CoCode` | String |  |  |
| 32 | `OA.SGC.DEPT.CODE` | `OaApplicationStagesCatalog_DeptCode` | String |  |  |
| 33 | `OA.SGC.AUDITOR.CODE` | `OaApplicationStagesCatalog_AuditorCode` | String |  |  |
| 34 | `OA.SGC.AUDIT.DATE.TIME` | `OaApplicationStagesCatalog_AuditDateTime` | String |  |  |
