# OA.APPLICATION.STATUS.DEFINITION — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.STATUS.DEFINITION` in `OA_Status.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.AUSD.DESCRIPTION` | `OaApplicationStatusDefinition_Description` |  |  |  |
| 2 | `OA.AUSD.FULL.DESCRIPTION` | `OaApplicationStatusDefinition_FullDescription` |  |  |  |
| 3 | `OA.AUSD.APPLICATION.STATUS` | `OaApplicationStatusDefinition_ApplicationStatus` |  |  |  |
| 4 | `OA.AUSD.RESERVED.FIELD.17` | `OaApplicationStatusDefinition_ReservedField17` |  |  |  |
| 5 | `OA.AUSD.RESERVED.FIELD.16` | `OaApplicationStatusDefinition_ReservedField16` |  |  |  |
| 6 | `OA.AUSD.APPLICATION.PERIOD` | `OaApplicationStatusDefinition_ApplicationPeriod` |  |  |  |
| 7 | `OA.AUSD.RESERVED.FIELD.15` | `OaApplicationStatusDefinition_ReservedField15` |  |  |  |
| 8 | `OA.AUSD.RESERVED.FIELD.14` | `OaApplicationStatusDefinition_ReservedField14` |  |  |  |
| 9 | `OA.AUSD.LINKED.USER.STATUS` | `OaApplicationStatusDefinition_LinkedUserStatus` |  |  |  |
| 10 | `OA.AUSD.APP.STATUS.END.POINT` | `OaApplicationStatusDefinition_AppStatusEndPoint` |  |  |  |
| 11 | `OA.AUSD.ARCHIVAL.OPTION` | `OaApplicationStatusDefinition_ArchivalOption` |  |  |  |
| 12 | `OA.AUSD.RESERVED.FIELD.12` | `OaApplicationStatusDefinition_ReservedField12` | TField |  |  |
| 13 | `OA.AUSD.RESERVED.FIELD.11` | `OaApplicationStatusDefinition_ReservedField11` | TField |  |  |
| 14 | `OA.AUSD.INACTIVE.PERIOD` | `OaApplicationStatusDefinition_InactivePeriod` | TField |  |  |
| 15 | `OA.AUSD.ARCHIVAL.PERIOD` | `OaApplicationStatusDefinition_ArchivalPeriod` | TField |  |  |
| 16 | `OA.AUSD.DORM.STATUS.END.POINT` | `OaApplicationStatusDefinition_DormStatusEndPoint` |  |  |  |
| 17 | `OA.AUSD.RESERVED.FIELD.10` | `OaApplicationStatusDefinition_ReservedField10` | TField |  |  |
| 18 | `OA.AUSD.RESERVED.FIELD.9` | `OaApplicationStatusDefinition_ReservedField9` | TField |  |  |
| 19 | `OA.AUSD.RESERVED.FIELD.8` | `OaApplicationStatusDefinition_ReservedField8` | TField |  |  |
| 20 | `OA.AUSD.RESERVED.FIELD.7` | `OaApplicationStatusDefinition_ReservedField7` | TField |  |  |
| 21 | `OA.AUSD.ACTION` | `OaApplicationStatusDefinition_Action` | TField |  |  |
| 22 | `OA.AUSD.PUBLISH.STATUS` | `OaApplicationStatusDefinition_PublishStatus` | TField |  |  |
| 23 | `OA.AUSD.PUBLISH.DATE` | `OaApplicationStatusDefinition_PublishDate` | TField |  |  |
| 24 | `OA.AUSD.PUBLISH.ERROR` | `OaApplicationStatusDefinition_PublishError` |  |  |  |
| 25 | `OA.AUSD.ERROR.SUGGESTION` | `OaApplicationStatusDefinition_ErrorSuggestion` |  |  |  |
| 26 | `OA.AUSD.REFERENCE` | `OaApplicationStatusDefinition_Reference` | TField |  |  |
| 27 | `OA.AUSD.VERSION` | `OaApplicationStatusDefinition_Version` | TField |  |  |
| 28 | `OA.AUSD.RESERVED.FIELD.6` | `OaApplicationStatusDefinition_ReservedField6` | TField |  |  |
| 29 | `OA.AUSD.RESERVED.FIELD.5` | `OaApplicationStatusDefinition_ReservedField5` | TField |  |  |
| 30 | `OA.AUSD.RESERVED.FIELD.4` | `OaApplicationStatusDefinition_ReservedField4` | TField |  |  |
| 31 | `OA.AUSD.RESERVED.FIELD.3` | `OaApplicationStatusDefinition_ReservedField3` | TField |  |  |
| 32 | `OA.AUSD.RESERVED.FIELD.2` | `OaApplicationStatusDefinition_ReservedField2` | TField |  |  |
| 33 | `OA.AUSD.RESERVED.FIELD.1` | `OaApplicationStatusDefinition_ReservedField1` | TField |  |  |
| 34 | `OA.AUSD.LOCAL.REF` | `OaApplicationStatusDefinition_LocalRef` |  |  |  |
| 35 | `OA.AUSD.OVERRIDE` | `OaApplicationStatusDefinition_Override` |  |  |  |
| 36 | `OA.AUSD.RECORD.STATUS` | `OaApplicationStatusDefinition_RecordStatus` | String |  |  |
| 37 | `OA.AUSD.CURR.NO` | `OaApplicationStatusDefinition_CurrNo` | String |  |  |
| 38 | `OA.AUSD.INPUTTER` | `OaApplicationStatusDefinition_Inputter` |  |  |  |
| 39 | `OA.AUSD.DATE.TIME` | `OaApplicationStatusDefinition_DateTime` |  |  |  |
| 40 | `OA.AUSD.AUTHORISER` | `OaApplicationStatusDefinition_Authoriser` | String |  |  |
| 41 | `OA.AUSD.CO.CODE` | `OaApplicationStatusDefinition_CoCode` | String |  |  |
| 42 | `OA.AUSD.DEPT.CODE` | `OaApplicationStatusDefinition_DeptCode` | String |  |  |
| 43 | `OA.AUSD.AUDITOR.CODE` | `OaApplicationStatusDefinition_AuditorCode` | String |  |  |
| 44 | `OA.AUSD.AUDIT.DATE.TIME` | `OaApplicationStatusDefinition_AuditDateTime` | String |  |  |
