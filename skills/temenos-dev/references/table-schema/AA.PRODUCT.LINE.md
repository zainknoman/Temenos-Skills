# AA.PRODUCT.LINE — Table Schema

> Source: `INSERTS/I_F.AA.PRODUCT.LINE` in `AA_ProductFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PL.DESCRIPTION` | `AaProductLine_Description` |  |  |  |
| 2 | `AA.PL.FULL.DESC` | `AaProductLine_FullDesc` |  |  |  |
| 3 | `AA.PL.PROPERTY.CLASS` | `AaProductLine_PropertyClass` |  |  |  |
| 4 | `AA.PL.MANDATORY` | `AaProductLine_Mandatory` |  |  |  |
| 5 | `AA.PL.LINE.ATTRIBUTE` | `AaProductLine_LineAttribute` |  |  |  |
| 6 | `AA.PL.BATCH.PRIORITY` | `AaProductLine_BatchPriority` | TField |  | When multiple Product line licenses are procured, this field indicates which processes run first and which run next. For example, by default the DEPOSITS schedule get processed before the LENDING schedules and ACCOUNTS run last. The field is system maintained and cannot be modified. Validations: Stores a number which indicates the priority of schedule processing System maintained and cannot be modified. |
| 7 | `AA.PL.SUB.BATCH.PRIORITY` | `AaProductLine_SubBatchPriority` |  |  |  |
| 8 | `AA.PL.GROUP` | `AaProductLine_Group` |  |  |  |
| 9 | `AA.PL.GROUP.CLASS` | `AaProductLine_GroupClass` |  |  |  |
| 10 | `AA.PL.ST.PROPERTY.CLASS` | `AaProductLine_StPropertyClass` |  |  |  |
| 11 | `AA.PL.STACKED` | `AaProductLine_Stacked` |  |  |  |
| 12 | `AA.PL.REBUILD.ACTIVITY.CLASS` | `AaProductLine_RebuildActivityClass` | TField |  | When field is set as Yes, activity classes must be created for all the soft property classes which are defined in the Product line. |
| 13 | `AA.PL.PARENT.LOOKUP` | `AaProductLine_ParentLookup` | TField |  | Field input allowed only for the REGIONAL.VARIATIONS variation product line. During the Product designer, table name defined this field will used to determine the Parent hierarchy. |
| 14 | `AA.PL.RESERVED01` | `AaProductLine_Reserved01` | TField |  |  |
| 15 | `AA.PL.RECORD.STATUS` | `AaProductLine_RecordStatus` | String |  |  |
| 16 | `AA.PL.CURR.NO` | `AaProductLine_CurrNo` | String |  |  |
| 17 | `AA.PL.INPUTTER` | `AaProductLine_Inputter` |  |  |  |
| 18 | `AA.PL.DATE.TIME` | `AaProductLine_DateTime` |  |  |  |
| 19 | `AA.PL.AUTHORISER` | `AaProductLine_Authoriser` | String |  |  |
| 20 | `AA.PL.CO.CODE` | `AaProductLine_CoCode` | String |  |  |
| 21 | `AA.PL.DEPT.CODE` | `AaProductLine_DeptCode` | String |  |  |
| 22 | `AA.PL.AUDITOR.CODE` | `AaProductLine_AuditorCode` | String |  |  |
| 23 | `AA.PL.AUDIT.DATE.TIME` | `AaProductLine_AuditDateTime` | String |  |  |
| 24 | `AA.PL.FEATURE` | `AaProductLine_Feature` |  |  |  |
| 25 | `AA.PL.FEATURE.MANDATORY` | `AaProductLine_FeatureMandatory` |  |  |  |
| 26 | `AA.PL.FEATURE.CLASS` | `AaProductLine_FeatureClass` |  |  |  |
| 27 | `AA.PL.EXCLUDE.FEATURE` | `AaProductLine_ExcludeFeature` |  |  |  |
