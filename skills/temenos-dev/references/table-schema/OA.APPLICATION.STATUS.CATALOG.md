# OA.APPLICATION.STATUS.CATALOG — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.STATUS.CATALOG` in `OA_Status.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.AUSC.DESCRIPTION` | `OaApplicationStatusCatalog_Description` |  |  |  |
| 2 | `OA.AUSC.FULL.DESCRIPTION` | `OaApplicationStatusCatalog_FullDescription` |  |  |  |
| 3 | `OA.AUSC.APPLICATION.STATUS` | `OaApplicationStatusCatalog_ApplicationStatus` |  |  |  |
| 4 | `OA.AUSC.RESERVED.FIELD.17` | `OaApplicationStatusCatalog_ReservedField17` |  |  |  |
| 5 | `OA.AUSC.RESERVED.FIELD.16` | `OaApplicationStatusCatalog_ReservedField16` |  |  |  |
| 6 | `OA.AUSC.APPLICATION.PERIOD` | `OaApplicationStatusCatalog_ApplicationPeriod` |  |  |  |
| 7 | `OA.AUSC.RESERVED.FIELD.15` | `OaApplicationStatusCatalog_ReservedField15` |  |  |  |
| 8 | `OA.AUSC.RESERVED.FIELD.14` | `OaApplicationStatusCatalog_ReservedField14` |  |  |  |
| 9 | `OA.AUSC.LINKED.USER.STATUS` | `OaApplicationStatusCatalog_LinkedUserStatus` |  |  |  |
| 10 | `OA.AUSC.APP.STATUS.END.POINT` | `OaApplicationStatusCatalog_AppStatusEndPoint` |  |  |  |
| 11 | `OA.AUSC.ARCHIVAL.OPTION` | `OaApplicationStatusCatalog_ArchivalOption` |  |  |  |
| 12 | `OA.AUSC.RESERVED.FIELD.12` | `OaApplicationStatusCatalog_ReservedField12` | TField |  |  |
| 13 | `OA.AUSC.RESERVED.FIELD.11` | `OaApplicationStatusCatalog_ReservedField11` | TField |  |  |
| 14 | `OA.AUSC.INACTIVE.PERIOD` | `OaApplicationStatusCatalog_InactivePeriod` | TField |  |  |
| 15 | `OA.AUSC.ARCHIVAL.PERIOD` | `OaApplicationStatusCatalog_ArchivalPeriod` | TField |  |  |
| 16 | `OA.AUSC.DORM.STATUS.END.POINT` | `OaApplicationStatusCatalog_DormStatusEndPoint` |  |  |  |
| 17 | `OA.AUSC.RESERVED.FIELD.10` | `OaApplicationStatusCatalog_ReservedField10` | TField |  |  |
| 18 | `OA.AUSC.RESERVED.FIELD.9` | `OaApplicationStatusCatalog_ReservedField9` | TField |  |  |
| 19 | `OA.AUSC.RESERVED.FIELD.8` | `OaApplicationStatusCatalog_ReservedField8` | TField |  |  |
| 20 | `OA.AUSC.RESERVED.FIELD.7` | `OaApplicationStatusCatalog_ReservedField7` | TField |  |  |
| 21 | `OA.AUSC.ACTION` | `OaApplicationStatusCatalog_Action` | TField |  |  |
| 22 | `OA.AUSC.PUBLISH.STATUS` | `OaApplicationStatusCatalog_PublishStatus` | TField |  |  |
| 23 | `OA.AUSC.PUBLISH.DATE` | `OaApplicationStatusCatalog_PublishDate` | TField |  |  |
| 24 | `OA.AUSC.PUBLISH.ERROR` | `OaApplicationStatusCatalog_PublishError` |  |  |  |
| 25 | `OA.AUSC.ERROR.SUGGESTION` | `OaApplicationStatusCatalog_ErrorSuggestion` |  |  |  |
| 26 | `OA.AUSC.REFERENCE` | `OaApplicationStatusCatalog_Reference` | TField |  |  |
| 27 | `OA.AUSC.VERSION` | `OaApplicationStatusCatalog_Version` | TField |  |  |
| 28 | `OA.AUSC.RESERVED.FIELD.6` | `OaApplicationStatusCatalog_ReservedField6` | TField |  |  |
| 29 | `OA.AUSC.RESERVED.FIELD.5` | `OaApplicationStatusCatalog_ReservedField5` | TField |  |  |
| 30 | `OA.AUSC.RESERVED.FIELD.4` | `OaApplicationStatusCatalog_ReservedField4` | TField |  |  |
| 31 | `OA.AUSC.RESERVED.FIELD.3` | `OaApplicationStatusCatalog_ReservedField3` | TField |  |  |
| 32 | `OA.AUSC.RESERVED.FIELD.2` | `OaApplicationStatusCatalog_ReservedField2` | TField |  |  |
| 33 | `OA.AUSC.RESERVED.FIELD.1` | `OaApplicationStatusCatalog_ReservedField1` | TField |  |  |
| 34 | `OA.AUSC.LOCAL.REF` | `OaApplicationStatusCatalog_LocalRef` |  |  |  |
| 35 | `OA.AUSC.OVERRIDE` | `OaApplicationStatusCatalog_Override` |  |  |  |
| 36 | `OA.AUSC.RECORD.STATUS` | `OaApplicationStatusCatalog_RecordStatus` | String |  |  |
| 37 | `OA.AUSC.CURR.NO` | `OaApplicationStatusCatalog_CurrNo` | String |  |  |
| 38 | `OA.AUSC.INPUTTER` | `OaApplicationStatusCatalog_Inputter` |  |  |  |
| 39 | `OA.AUSC.DATE.TIME` | `OaApplicationStatusCatalog_DateTime` |  |  |  |
| 40 | `OA.AUSC.AUTHORISER` | `OaApplicationStatusCatalog_Authoriser` | String |  |  |
| 41 | `OA.AUSC.CO.CODE` | `OaApplicationStatusCatalog_CoCode` | String |  |  |
| 42 | `OA.AUSC.DEPT.CODE` | `OaApplicationStatusCatalog_DeptCode` | String |  |  |
| 43 | `OA.AUSC.AUDITOR.CODE` | `OaApplicationStatusCatalog_AuditorCode` | String |  |  |
| 44 | `OA.AUSC.AUDIT.DATE.TIME` | `OaApplicationStatusCatalog_AuditDateTime` | String |  |  |
