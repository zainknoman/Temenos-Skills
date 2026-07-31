# AA.MARKETING.CATALOGUE.DESIGNER — Table Schema

> Source: `INSERTS/I_F.AA.MARKETING.CATALOGUE.DESIGNER` in `AA_MarketingCatalogue.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.MC.DESCRIPTION` | `AaMarketingCatalogueDesigner_Description` |  |  |  |
| 2 | `AA.MC.FULL.DESCRIPTION` | `AaMarketingCatalogueDesigner_FullDescription` |  |  |  |
| 3 | `AA.MC.RESERVED.12` | `AaMarketingCatalogueDesigner_Reserved12` | TField |  |  |
| 4 | `AA.MC.RESERVED.11` | `AaMarketingCatalogueDesigner_Reserved11` | TField |  |  |
| 5 | `AA.MC.FIELD.NAME` | `AaMarketingCatalogueDesigner_FieldName` |  |  |  |
| 6 | `AA.MC.RESERVED.14` | `AaMarketingCatalogueDesigner_Reserved14` |  |  |  |
| 7 | `AA.MC.SOURCE.TABLE` | `AaMarketingCatalogueDesigner_SourceTable` |  |  |  |
| 8 | `AA.MC.SOURCE.PROPERTY` | `AaMarketingCatalogueDesigner_SourceProperty` |  |  |  |
| 9 | `AA.MC.SOURCE.FIELD` | `AaMarketingCatalogueDesigner_SourceField` |  |  |  |
| 10 | `AA.MC.SRC.FLD.LOOKUP` | `AaMarketingCatalogueDesigner_SrcFldLookup` |  |  |  |
| 11 | `AA.MC.SRC.FLD.RULE.TYPE` | `AaMarketingCatalogueDesigner_SrcFldRuleType` |  |  |  |
| 12 | `AA.MC.SRC.FLD.RULE` | `AaMarketingCatalogueDesigner_SrcFldRule` |  |  |  |
| 13 | `AA.MC.SOURCE.DATA.TYPE` | `AaMarketingCatalogueDesigner_SourceDataType` |  |  |  |
| 14 | `AA.MC.SOURCE.VALUE` | `AaMarketingCatalogueDesigner_SourceValue` |  |  |  |
| 15 | `AA.MC.SOURCE.API` | `AaMarketingCatalogueDesigner_SourceApi` |  |  |  |
| 16 | `AA.MC.ATTRIBS` | `AaMarketingCatalogueDesigner_Attribs` |  |  |  |
| 17 | `AA.MC.SOURCE.NULL.VALUE` | `AaMarketingCatalogueDesigner_SourceNullValue` |  |  |  |
| 18 | `AA.MC.ROUTINE` | `AaMarketingCatalogueDesigner_Routine` |  |  |  |
| 19 | `AA.MC.PARAMETER` | `AaMarketingCatalogueDesigner_Parameter` |  |  |  |
| 20 | `AA.MC.MAPPED.FIELD` | `AaMarketingCatalogueDesigner_MappedField` |  |  |  |
| 21 | `AA.MC.RESERVED.15` | `AaMarketingCatalogueDesigner_Reserved15` |  |  |  |
| 22 | `AA.MC.RESERVED.6` | `AaMarketingCatalogueDesigner_Reserved6` | TField |  |  |
| 23 | `AA.MC.ACTION` | `AaMarketingCatalogueDesigner_Action` | TField |  | It will accepts only one option PUBLISH. In order to maintain a separate design and run-time, when the marketing catalogue definition is ready for production, using the action within the Table AA.MARKETING.CATALOGUE.DESIGNER the record can be moved to AA.MARKETING.CATALOGUE with PUBLISH action |
| 24 | `AA.MC.PG.GROUP.FIELD.NAME` | `AaMarketingCatalogueDesigner_PgGroupFieldName` |  |  |  |
| 25 | `AA.MC.FLD.PG.GROUP.ID` | `AaMarketingCatalogueDesigner_FldPgGroupId` |  |  |  |
| 26 | `AA.MC.PG.GROUP.ROUTINE.NAME` | `AaMarketingCatalogueDesigner_PgGroupRoutineName` |  |  |  |
| 27 | `AA.MC.RTN.PG.GROUP.ID` | `AaMarketingCatalogueDesigner_RtnPgGroupId` |  |  |  |
| 28 | `AA.MC.RECORD.TYPE` | `AaMarketingCatalogueDesigner_RecordType` | TField |  |  |
| 29 | `AA.MC.RECORD.KEY` | `AaMarketingCatalogueDesigner_RecordKey` | TField |  |  |
| 30 | `AA.MC.RESERVED.5` | `AaMarketingCatalogueDesigner_Reserved5` | TField |  |  |
| 31 | `AA.MC.RESERVED.4` | `AaMarketingCatalogueDesigner_Reserved4` | TField |  |  |
| 32 | `AA.MC.RESERVED.3` | `AaMarketingCatalogueDesigner_Reserved3` | TField |  |  |
| 33 | `AA.MC.RESERVED.2` | `AaMarketingCatalogueDesigner_Reserved2` | TField |  |  |
| 34 | `AA.MC.RESERVED.1` | `AaMarketingCatalogueDesigner_Reserved1` | TField |  |  |
| 35 | `AA.MC.LOCAL.REF` | `AaMarketingCatalogueDesigner_LocalRef` |  |  |  |
| 36 | `AA.MC.OVERRIDE` | `AaMarketingCatalogueDesigner_Override` |  |  |  |
| 37 | `AA.MC.RECORD.STATUS` | `AaMarketingCatalogueDesigner_RecordStatus` | String |  |  |
| 38 | `AA.MC.CURR.NO` | `AaMarketingCatalogueDesigner_CurrNo` | String |  |  |
| 39 | `AA.MC.INPUTTER` | `AaMarketingCatalogueDesigner_Inputter` |  |  |  |
| 40 | `AA.MC.DATE.TIME` | `AaMarketingCatalogueDesigner_DateTime` |  |  |  |
| 41 | `AA.MC.AUTHORISER` | `AaMarketingCatalogueDesigner_Authoriser` | String |  |  |
| 42 | `AA.MC.CO.CODE` | `AaMarketingCatalogueDesigner_CoCode` | String |  |  |
| 43 | `AA.MC.DEPT.CODE` | `AaMarketingCatalogueDesigner_DeptCode` | String |  |  |
| 44 | `AA.MC.AUDITOR.CODE` | `AaMarketingCatalogueDesigner_AuditorCode` | String |  |  |
| 45 | `AA.MC.AUDIT.DATE.TIME` | `AaMarketingCatalogueDesigner_AuditDateTime` | String |  |  |
