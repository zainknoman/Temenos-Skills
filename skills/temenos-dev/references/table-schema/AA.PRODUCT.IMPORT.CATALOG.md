# AA.PRODUCT.IMPORT.CATALOG — Table Schema

> Source: `INSERTS/I_F.AA.PRODUCT.IMPORT.CATALOG` in `AA_ProductImporter.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PIC.DESCRIPTION` | `AaProductImportCatalog_Description` | TField |  | Description of the Product taken from the original definition in Product import catalog. |
| 2 | `AA.PIC.FULL.DESCRIPTION` | `AaProductImportCatalog_FullDescription` |  |  |  |
| 3 | `AA.PIC.RESERVED.12` | `AaProductImportCatalog_Reserved12` | TField |  | Standard Reserved field |
| 4 | `AA.PIC.RESERVED.11` | `AaProductImportCatalog_Reserved11` | TField |  | Standard Reserved field |
| 5 | `AA.PIC.API.SYSTEM.ATTRIBUTE` | `AaProductImportCatalog_ApiSystemAttribute` |  |  |  |
| 6 | `AA.PIC.API.USER.ATTRIBUTE` | `AaProductImportCatalog_ApiUserAttribute` |  |  |  |
| 7 | `AA.PIC.SOURCE.PROPERTY` | `AaProductImportCatalog_SourceProperty` |  |  |  |
| 8 | `AA.PIC.SOURCE.ATTRIBUTE` | `AaProductImportCatalog_SourceAttribute` |  |  |  |
| 9 | `AA.PIC.SOURCE.NEG.RULE` | `AaProductImportCatalog_SourceNegRule` |  |  |  |
| 10 | `AA.PIC.SOURCE.PERIODIC.RULE` | `AaProductImportCatalog_SourcePeriodicRule` |  |  |  |
| 11 | `AA.PIC.SOURCE.PERIOD` | `AaProductImportCatalog_SourcePeriod` |  |  |  |
| 12 | `AA.PIC.MAXIMUM.CHARACTER` | `AaProductImportCatalog_MaximumCharacter` |  |  |  |
| 13 | `AA.PIC.RESERVED` | `AaProductImportCatalog_Reserved` |  |  |  |
| 14 | `AA.PIC.DATA.TYPE` | `AaProductImportCatalog_DataType` |  |  |  |
| 15 | `AA.PIC.VETTING.TABLE` | `AaProductImportCatalog_VettingTable` |  |  |  |
| 16 | `AA.PIC.APPLICATION.VET` | `AaProductImportCatalog_ApplicationVet` |  |  |  |
| 17 | `AA.PIC.DEFAULT.VALUE` | `AaProductImportCatalog_DefaultValue` |  |  |  |
| 18 | `AA.PIC.VIRTUAL.TABLE` | `AaProductImportCatalog_VirtualTable` |  |  |  |
| 19 | `AA.PIC.SUB.ASSOC.CODE` | `AaProductImportCatalog_SubAssocCode` |  |  |  |
| 20 | `AA.PIC.RESERVED.10` | `AaProductImportCatalog_Reserved10` | TField |  | Standard Reserved field |
| 21 | `AA.PIC.RESERVED.9` | `AaProductImportCatalog_Reserved9` | TField |  | Standard Reserved field |
| 22 | `AA.PIC.RESERVED.8` | `AaProductImportCatalog_Reserved8` | TField |  | Standard Reserved field |
| 23 | `AA.PIC.RESERVED.7` | `AaProductImportCatalog_Reserved7` | TField |  | Standard Reserved field |
| 24 | `AA.PIC.RESERVED.6` | `AaProductImportCatalog_Reserved6` | TField |  | Standard Reserved field |
| 25 | `AA.PIC.RESERVED.5` | `AaProductImportCatalog_Reserved5` | TField |  | Standard Reserved field |
| 26 | `AA.PIC.RESERVED.4` | `AaProductImportCatalog_Reserved4` | TField |  | Standard Reserved field |
| 27 | `AA.PIC.RESERVED.3` | `AaProductImportCatalog_Reserved3` | TField |  | Standard Reserved field |
| 28 | `AA.PIC.RESERVED.2` | `AaProductImportCatalog_Reserved2` | TField |  | Standard Reserved field |
| 29 | `AA.PIC.RESERVED.1` | `AaProductImportCatalog_Reserved1` | TField |  | Standard Reserved field |
| 30 | `AA.PIC.ACTION` | `AaProductImportCatalog_Action` | TField |  | This field indicates which action will be performed after the record is authorised. Allowed values are Null or PUBLISH. If action is null, the definition is simply being saved on file after authorization. If PUBLISH is specified, system would initiate a 'publish' mechanism of this record. |
| 31 | `AA.PIC.PUBLISH.STATUS` | `AaProductImportCatalog_PublishStatus` | TField |  | This field indicates whether current definition has published or not. If the definition was published successfully then status will get updated as COMPLETED SUCCESSFULLY |
| 32 | `AA.PIC.PUBLISH.ERROR` | `AaProductImportCatalog_PublishError` |  |  |  |
| 33 | `AA.PIC.ERROR.SUGGESTION` | `AaProductImportCatalog_ErrorSuggestion` |  |  |  |
| 34 | `AA.PIC.ID.COMP.1` | `AaProductImportCatalog_IdComp1` | TField |  | It is a standard id component field. which will store the 1st of the id |
| 35 | `AA.PIC.ID.COMP.2` | `AaProductImportCatalog_IdComp2` | TField |  | It is standard id component field. which will store the 2nd of the id |
| 36 | `AA.PIC.ID.COMP.3` | `AaProductImportCatalog_IdComp3` | TField |  | It is standard id component field. which will store the 3rd of the id |
| 37 | `AA.PIC.LOCAL.REF` | `AaProductImportCatalog_LocalRef` |  |  |  |
| 38 | `AA.PIC.OVERRIDE` | `AaProductImportCatalog_Override` |  |  |  |
| 39 | `AA.PIC.RECORD.STATUS` | `AaProductImportCatalog_RecordStatus` | String |  |  |
| 40 | `AA.PIC.CURR.NO` | `AaProductImportCatalog_CurrNo` | String |  |  |
| 41 | `AA.PIC.INPUTTER` | `AaProductImportCatalog_Inputter` |  |  |  |
| 42 | `AA.PIC.DATE.TIME` | `AaProductImportCatalog_DateTime` |  |  |  |
| 43 | `AA.PIC.AUTHORISER` | `AaProductImportCatalog_Authoriser` | String |  |  |
| 44 | `AA.PIC.CO.CODE` | `AaProductImportCatalog_CoCode` | String |  |  |
| 45 | `AA.PIC.DEPT.CODE` | `AaProductImportCatalog_DeptCode` | String |  |  |
| 46 | `AA.PIC.AUDITOR.CODE` | `AaProductImportCatalog_AuditorCode` | String |  |  |
| 47 | `AA.PIC.AUDIT.DATE.TIME` | `AaProductImportCatalog_AuditDateTime` | String |  |  |
