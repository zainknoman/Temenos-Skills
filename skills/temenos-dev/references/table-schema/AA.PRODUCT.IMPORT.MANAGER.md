# AA.PRODUCT.IMPORT.MANAGER — Table Schema

> Source: `INSERTS/I_F.AA.PRODUCT.IMPORT.MANAGER` in `AA_ProductImporter.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PIM.DESCRIPTION` | `AaProductImportManager_Description` | TField |  | Description of the Product taken from the original definition in Product import catalog. |
| 2 | `AA.PIM.FULL.DESCRIPTION` | `AaProductImportManager_FullDescription` |  |  |  |
| 3 | `AA.PIM.RESERVED.12` | `AaProductImportManager_Reserved12` | TField |  | Standard Reserved field |
| 4 | `AA.PIM.RESERVED.11` | `AaProductImportManager_Reserved11` | TField |  | Standard Reserved field |
| 5 | `AA.PIM.API.SYSTEM.ATTRIBUTE` | `AaProductImportManager_ApiSystemAttribute` |  |  |  |
| 6 | `AA.PIM.API.USER.ATTRIBUTE` | `AaProductImportManager_ApiUserAttribute` |  |  |  |
| 7 | `AA.PIM.SOURCE.PROPERTY` | `AaProductImportManager_SourceProperty` |  |  |  |
| 8 | `AA.PIM.SOURCE.ATTRIBUTE` | `AaProductImportManager_SourceAttribute` |  |  |  |
| 9 | `AA.PIM.SOURCE.NEG.RULE` | `AaProductImportManager_SourceNegRule` |  |  |  |
| 10 | `AA.PIM.SOURCE.PERIODIC.RULE` | `AaProductImportManager_SourcePeriodicRule` |  |  |  |
| 11 | `AA.PIM.SOURCE.PERIOD` | `AaProductImportManager_SourcePeriod` |  |  |  |
| 12 | `AA.PIM.MAXIMUM.CHARACTER` | `AaProductImportManager_MaximumCharacter` |  |  |  |
| 13 | `AA.PIM.RESERVED` | `AaProductImportManager_Reserved` |  |  |  |
| 14 | `AA.PIM.DATA.TYPE` | `AaProductImportManager_DataType` |  |  |  |
| 15 | `AA.PIM.VETTING.TABLE` | `AaProductImportManager_VettingTable` |  |  |  |
| 16 | `AA.PIM.APPLICATION.VET` | `AaProductImportManager_ApplicationVet` |  |  |  |
| 17 | `AA.PIM.DEFAULT.VALUE` | `AaProductImportManager_DefaultValue` |  |  |  |
| 18 | `AA.PIM.VIRTUAL.TABLE` | `AaProductImportManager_VirtualTable` |  |  |  |
| 19 | `AA.PIM.SUB.ASSOC.CODE` | `AaProductImportManager_SubAssocCode` |  |  |  |
| 20 | `AA.PIM.RESERVED.10` | `AaProductImportManager_Reserved10` | TField |  | Standard Reserved field |
| 21 | `AA.PIM.RESERVED.9` | `AaProductImportManager_Reserved9` | TField |  | Standard Reserved field |
| 22 | `AA.PIM.RESERVED.8` | `AaProductImportManager_Reserved8` | TField |  | Standard Reserved field |
| 23 | `AA.PIM.RESERVED.7` | `AaProductImportManager_Reserved7` | TField |  | Standard Reserved field |
| 24 | `AA.PIM.RESERVED.6` | `AaProductImportManager_Reserved6` | TField |  | Standard Reserved field |
| 25 | `AA.PIM.RESERVED.5` | `AaProductImportManager_Reserved5` | TField |  | Standard Reserved field |
| 26 | `AA.PIM.RESERVED.4` | `AaProductImportManager_Reserved4` | TField |  | Standard Reserved field |
| 27 | `AA.PIM.RESERVED.3` | `AaProductImportManager_Reserved3` | TField |  | Standard Reserved field |
| 28 | `AA.PIM.RESERVED.2` | `AaProductImportManager_Reserved2` | TField |  | Standard Reserved field |
| 29 | `AA.PIM.RESERVED.1` | `AaProductImportManager_Reserved1` | TField |  | Standard Reserved field |
| 30 | `AA.PIM.ACTION` | `AaProductImportManager_Action` | TField |  | This field indicates which action will be performed after the record is authorised. Allowed values are Null or PUBLISH. If action is null, the definition is simply being saved on file after authorization. If PUBLISH is specified, system would initiate a 'publish' mechanism of this record. |
| 31 | `AA.PIM.PUBLISH.STATUS` | `AaProductImportManager_PublishStatus` | TField |  | This field indicates whether current definition has published or not. If the definition was published successfully then status will get updated as COMPLETED SUCCESSFULLY |
| 32 | `AA.PIM.PUBLISH.ERROR` | `AaProductImportManager_PublishError` |  |  |  |
| 33 | `AA.PIM.ERROR.SUGGESTION` | `AaProductImportManager_ErrorSuggestion` |  |  |  |
| 34 | `AA.PIM.ID.COMP.1` | `AaProductImportManager_IdComp1` | TField |  | It is a standard id component field. which will store the 1st of the id |
| 35 | `AA.PIM.ID.COMP.2` | `AaProductImportManager_IdComp2` | TField |  | It is standard id component field. which will store the 2nd of the id |
| 36 | `AA.PIM.ID.COMP.3` | `AaProductImportManager_IdComp3` | TField |  | It is standard id component field. which will store the 3rd of the id |
| 37 | `AA.PIM.LOCAL.REF` | `AaProductImportManager_LocalRef` |  |  |  |
| 38 | `AA.PIM.OVERRIDE` | `AaProductImportManager_Override` |  |  |  |
| 39 | `AA.PIM.RECORD.STATUS` | `AaProductImportManager_RecordStatus` | String |  |  |
| 40 | `AA.PIM.CURR.NO` | `AaProductImportManager_CurrNo` | String |  |  |
| 41 | `AA.PIM.INPUTTER` | `AaProductImportManager_Inputter` |  |  |  |
| 42 | `AA.PIM.DATE.TIME` | `AaProductImportManager_DateTime` |  |  |  |
| 43 | `AA.PIM.AUTHORISER` | `AaProductImportManager_Authoriser` | String |  |  |
| 44 | `AA.PIM.CO.CODE` | `AaProductImportManager_CoCode` | String |  |  |
| 45 | `AA.PIM.DEPT.CODE` | `AaProductImportManager_DeptCode` | String |  |  |
| 46 | `AA.PIM.AUDITOR.CODE` | `AaProductImportManager_AuditorCode` | String |  |  |
| 47 | `AA.PIM.AUDIT.DATE.TIME` | `AaProductImportManager_AuditDateTime` | String |  |  |
