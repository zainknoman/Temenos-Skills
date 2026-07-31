# AA.CONDITION.GENERATOR — Table Schema

> Source: `INSERTS/I_F.AA.CONDITION.GENERATOR` in `AA_ProductAttribute.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CDG.DESCRIPTION` | `AaConditionGenerator_Description` |  |  |  |
| 2 | `AA.CDG.LONG.DESCRIPTION` | `AaConditionGenerator_LongDescription` |  |  |  |
| 3 | `AA.CDG.FEATURE.PROPERTY` | `AaConditionGenerator_FeatureProperty` | TField |  |  |
| 4 | `AA.CDG.EFFECTIVE.DATE` | `AaConditionGenerator_EffectiveDate` | TField |  |  |
| 5 | `AA.CDG.PRODUCT.CONDITION` | `AaConditionGenerator_ProductCondition` |  |  |  |
| 6 | `AA.CDG.API.ATTRIBUTE` | `AaConditionGenerator_ApiAttribute` |  |  |  |
| 7 | `AA.CDG.FIELD.NAME` | `AaConditionGenerator_FieldName` |  |  |  |
| 8 | `AA.CDG.FIELD.VALUE` | `AaConditionGenerator_FieldValue` |  |  |  |
| 9 | `AA.CDG.LOCAL.REF` | `AaConditionGenerator_LocalRef` |  |  |  |
| 10 | `AA.CDG.OVERRIDE` | `AaConditionGenerator_Override` |  |  |  |
| 11 | `AA.CDG.RECORD.STATUS` | `AaConditionGenerator_RecordStatus` | String |  |  |
| 12 | `AA.CDG.CURR.NO` | `AaConditionGenerator_CurrNo` | String |  |  |
| 13 | `AA.CDG.INPUTTER` | `AaConditionGenerator_Inputter` |  |  |  |
| 14 | `AA.CDG.DATE.TIME` | `AaConditionGenerator_DateTime` |  |  |  |
| 15 | `AA.CDG.AUTHORISER` | `AaConditionGenerator_Authoriser` | String |  |  |
| 16 | `AA.CDG.CO.CODE` | `AaConditionGenerator_CoCode` | String |  |  |
| 17 | `AA.CDG.DEPT.CODE` | `AaConditionGenerator_DeptCode` | String |  |  |
| 18 | `AA.CDG.AUDITOR.CODE` | `AaConditionGenerator_AuditorCode` | String |  |  |
| 19 | `AA.CDG.AUDIT.DATE.TIME` | `AaConditionGenerator_AuditDateTime` | String |  |  |
| 20 | `AA.CDG.IMPORT.STATUS` | `AaConditionGenerator_ImportStatus` | TField |  |  |
| 21 | `AA.CDG.IMPORT.ERROR.TYPE` | `AaConditionGenerator_ImportErrorType` |  |  |  |
| 22 | `AA.CDG.IMPORT.ERROR.SOURCE` | `AaConditionGenerator_ImportErrorSource` |  |  |  |
| 23 | `AA.CDG.IMPORT.ERROR` | `AaConditionGenerator_ImportError` |  |  |  |
| 24 | `AA.CDG.ATTRIBUTE.PATH` | `AaConditionGenerator_AttributePath` |  |  |  |
| 25 | `AA.CDG.CONDITION.VERSION` | `AaConditionGenerator_ConditionVersion` | TField |  |  |
| 26 | `AA.CDG.VARIATION` | `AaConditionGenerator_Variation` |  |  |  |
