# EB.MDAL.ENTITIES — Table Schema

> Source: `INSERTS/I_F.EB.MDAL.ENTITIES` in `EB_MdalFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDL.EXTERNAL.ENTS` | `EbMdalEntities_ExternalEnts` |  |  |  |
| 2 | `MDL.ENTITY` | `EbMdalEntities_Entity` |  |  |  |
| 3 | `MDL.COMPONENT` | `EbMdalEntities_Component` |  |  |  |
| 4 | `MDL.APPLICATION` | `EbMdalEntities_Application` |  |  |  |
| 5 | `MDL.ENRI.COMPONENT` | `EbMdalEntities_EnriComponent` |  |  |  |
| 6 | `MDL.ENRI.METHOD` | `EbMdalEntities_EnriMethod` |  |  |  |
| 7 | `MDL.LOCAL.REF` | `EbMdalEntities_LocalRef` |  |  |  |
| 8 | `MDL.OVERRIDE` | `EbMdalEntities_Override` |  |  |  |
| 9 | `MDL.RECORD.STATUS` | `EbMdalEntities_RecordStatus` | String |  |  |
| 10 | `MDL.CURR.NO` | `EbMdalEntities_CurrNo` | String |  |  |
| 11 | `MDL.INPUTTER` | `EbMdalEntities_Inputter` |  |  |  |
| 12 | `MDL.DATE.TIME` | `EbMdalEntities_DateTime` |  |  |  |
| 13 | `MDL.AUTHORISER` | `EbMdalEntities_Authoriser` | String |  |  |
| 14 | `MDL.CO.CODE` | `EbMdalEntities_CoCode` | String |  |  |
| 15 | `MDL.DEPT.CODE` | `EbMdalEntities_DeptCode` | String |  |  |
| 16 | `MDL.AUDITOR.CODE` | `EbMdalEntities_AuditorCode` | String |  |  |
| 17 | `MDL.AUDIT.DATE.TIME` | `EbMdalEntities_AuditDateTime` | String |  |  |
| 18 | `MDL.PRECOMPOSE.ALLOW.INLINE` | `EbMdalEntities_PrecomposeAllowInline` |  |  |  |
| 19 | `MDL.COMP.METHOD` | `EbMdalEntities_CompMethod` |  |  |  |
| 20 | `MDL.MDAL.LOG.DIR` | `EbMdalEntities_MdalLogDir` | TField |  | Denotes log directory name. Validation Rules: Input allowed only for SYSTEM record in EB.MDAL.ENTITIES and when SPF>SITE.NAME is 'EBS.LONDON.', i.e internal developer system. EB.MDAL.ENTITIES SYSTEM record authorisation will create this log directory This is for internal Temenos developer usage to store or identify list of MDAL methods invoked in underlying JBC routines during MDAL API request flow. EXTERNAL.ENTS field should be empty to enable this simulation mode to update log directory with list of MDAL methods invoked. ID of this log directory is transaction id, content will be list of MDAL methods. This will help to decide and configure COMP.METHOD and also API .properties file i.e MDAL API's request registry to setup path param for each operationIds (MDAL component methods). |
