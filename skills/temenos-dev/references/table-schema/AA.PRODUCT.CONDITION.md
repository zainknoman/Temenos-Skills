# AA.PRODUCT.CONDITION — Table Schema

> Source: `INSERTS/I_F.AA.PRODUCT.CONDITION` in `AA_ProductManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PRD.COND.DESCRIPTION` | `AaProductCondition_Description` |  |  |  |
| 2 | `AA.PRD.COND.FULL.DESCRIPTION` | `AaProductCondition_FullDescription` |  |  |  |
| 3 | `AA.PRD.COND.CONTEXT.TYPE` | `AaProductCondition_ContextType` |  |  |  |
| 4 | `AA.PRD.COND.CONTEXT` | `AaProductCondition_Context` |  |  |  |
| 5 | `AA.PRD.COND.PROPERTY.CLASS` | `AaProductCondition_PropertyClass` | TField |  | Denotes the property class for which the product condition is associated. |
| 6 | `AA.PRD.COND.CONDITION.KEY` | `AaProductCondition_ConditionKey` | TField |  | Describes the second part of the record key o this Table, AA.PRODUCT.CONDITION, may be used for selecting the records from this table by "Conditon name" |
| 7 | `AA.PRD.COND.EPD.ATTRIBUTE.EXCLUDE` | `AaProductCondition_EpdAttributeExclude` |  |  |  |
| 8 | `AA.PRD.COND.EPD.FIELD.HIDDEN` | `AaProductCondition_EpdFieldHidden` |  |  |  |
| 9 | `AA.PRD.COND.EPD.DEFAULT.EDITABLE` | `AaProductCondition_EpdDefaultEditable` | TField |  |  |
| 10 | `AA.PRD.COND.RECORD.STATUS` | `AaProductCondition_RecordStatus` | String |  |  |
| 11 | `AA.PRD.COND.CURR.NO` | `AaProductCondition_CurrNo` | String |  |  |
| 12 | `AA.PRD.COND.INPUTTER` | `AaProductCondition_Inputter` |  |  |  |
| 13 | `AA.PRD.COND.DATE.TIME` | `AaProductCondition_DateTime` |  |  |  |
| 14 | `AA.PRD.COND.AUTHORISER` | `AaProductCondition_Authoriser` | String |  |  |
| 15 | `AA.PRD.COND.CO.CODE` | `AaProductCondition_CoCode` | String |  |  |
| 16 | `AA.PRD.COND.DEPT.CODE` | `AaProductCondition_DeptCode` | String |  |  |
| 17 | `AA.PRD.COND.AUDITOR.CODE` | `AaProductCondition_AuditorCode` | String |  |  |
| 18 | `AA.PRD.COND.AUDIT.DATE.TIME` | `AaProductCondition_AuditDateTime` | String |  |  |
| 19 | `AA.PRD.COND.CONTEXT.DESCRIPTION` | `AaProductCondition_ContextDescription` | TField |  |  |
| 20 | `AA.PRD.COND.API.ATTRIBUTE` | `AaProductCondition_ApiAttribute` |  |  |  |
| 21 | `AA.PRD.COND.API.FIELD.NAME` | `AaProductCondition_ApiFieldName` |  |  |  |
| 22 | `AA.PRD.COND.FIELD.LABEL` | `AaProductCondition_FieldLabel` |  |  |  |
| 23 | `AA.PRD.COND.FIELD.DESCRIPTION` | `AaProductCondition_FieldDescription` |  |  |  |
| 24 | `AA.PRD.COND.OPTION.NAME` | `AaProductCondition_OptionName` |  |  |  |
| 25 | `AA.PRD.COND.OPTION.DESC` | `AaProductCondition_OptionDesc` |  |  |  |
| 26 | `AA.PRD.COND.DEFAULT.VALUE` | `AaProductCondition_DefaultValue` |  |  |  |
| 27 | `AA.PRD.COND.EPD.FIELD` | `AaProductCondition_EpdField` |  |  |  |
| 28 | `AA.PRD.COND.EPD.FIELD.RULE` | `AaProductCondition_EpdFieldRule` |  |  |  |
| 29 | `AA.PRD.COND.EPD.FIELD.OPTION` | `AaProductCondition_EpdFieldOption` |  |  |  |
| 30 | `AA.PRD.COND.LIFECYCLE.STATUS` | `AaProductCondition_LifecycleStatus` | TField |  |  |
| 31 | `AA.PRD.COND.AVAILABLE.DATE` | `AaProductCondition_AvailableDate` | TField |  |  |
