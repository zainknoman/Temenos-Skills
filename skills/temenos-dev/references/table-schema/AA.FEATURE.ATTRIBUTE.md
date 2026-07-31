# AA.FEATURE.ATTRIBUTE — Table Schema

> Source: `INSERTS/I_F.AA.FEATURE.ATTRIBUTE` in `AA_Feature.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ATTR.DESCRIPTION` | `AaFeatureAttribute_Description` |  |  |  |
| 2 | `AA.ATTR.LONG.DESCRIPTION` | `AaFeatureAttribute_LongDescription` |  |  |  |
| 3 | `AA.ATTR.ATTRIBUTE.TYPE` | `AaFeatureAttribute_AttributeType` | TField |  |  |
| 4 | `AA.ATTR.APPLICATION.TYPE` | `AaFeatureAttribute_ApplicationType` | TField |  | Indicator for type of application.Valid options are NULL and PropertyClass. |
| 5 | `AA.ATTR.APPLICATION.NAME` | `AaFeatureAttribute_ApplicationName` | TField |  | Name of the application where the fields exist. This should be a valid entry in PGM.FILE under H, W or V types. |
| 6 | `AA.ATTR.TYPE` | `AaFeatureAttribute_Type` |  |  |  |
| 7 | `AA.ATTR.RESERVED3` | `AaFeatureAttribute_Reserved3` | TField |  |  |
| 8 | `AA.ATTR.FIELD.NAME` | `AaFeatureAttribute_FieldName` |  |  |  |
| 9 | `AA.ATTR.FIELD.LABEL` | `AaFeatureAttribute_FieldLabel` |  |  |  |
| 10 | `AA.ATTR.FIELD.DESCRIPTION` | `AaFeatureAttribute_FieldDescription` |  |  |  |
| 11 | `AA.ATTR.FIELD.TYPE` | `AaFeatureAttribute_FieldType` |  |  |  |
| 12 | `AA.ATTR.LINKED.FIELD` | `AaFeatureAttribute_LinkedField` |  |  |  |
| 13 | `AA.ATTR.LINKED.NEG.RULE` | `AaFeatureAttribute_LinkedNegRule` |  |  |  |
| 14 | `AA.ATTR.FIELD.MAX.LENGTH` | `AaFeatureAttribute_FieldMaxLength` |  |  |  |
| 15 | `AA.ATTR.FIELD.DATA.TYPE` | `AaFeatureAttribute_FieldDataType` |  |  |  |
| 16 | `AA.ATTR.TOOLTIP` | `AaFeatureAttribute_Tooltip` |  |  |  |
| 17 | `AA.ATTR.OPTION.NAME` | `AaFeatureAttribute_OptionName` |  |  |  |
| 18 | `AA.ATTR.OPTION.DESCRIPTION` | `AaFeatureAttribute_OptionDescription` |  |  |  |
| 19 | `AA.ATTR.RESERVED9` | `AaFeatureAttribute_Reserved9` |  |  |  |
| 20 | `AA.ATTR.OPTION.FILTER` | `AaFeatureAttribute_OptionFilter` |  |  |  |
| 21 | `AA.ATTR.DEFAULT.VALUE` | `AaFeatureAttribute_DefaultValue` |  |  |  |
| 22 | `AA.ATTR.FIELD.PARAMETER` | `AaFeatureAttribute_FieldParameter` |  |  |  |
| 23 | `AA.ATTR.FIELD.PARAMETER.VALUE` | `AaFeatureAttribute_FieldParameterValue` |  |  |  |
| 24 | `AA.ATTR.FIELD.RULE` | `AaFeatureAttribute_FieldRule` |  |  |  |
| 25 | `AA.ATTR.FIELD.ENABLE.RULE` | `AaFeatureAttribute_FieldEnableRule` |  |  |  |
| 26 | `AA.ATTR.LINKED.ATTRIBUTE` | `AaFeatureAttribute_LinkedAttribute` |  |  |  |
| 27 | `AA.ATTR.LINKED.ATTRIBUTE.RULE` | `AaFeatureAttribute_LinkedAttributeRule` |  |  |  |
| 28 | `AA.ATTR.LOCAL.REF` | `AaFeatureAttribute_LocalRef` |  |  |  |
| 29 | `AA.ATTR.STMT.NOS` | `AaFeatureAttribute_StmtNos` |  |  |  |
| 30 | `AA.ATTR.OVERRIDE` | `AaFeatureAttribute_Override` |  |  |  |
| 31 | `AA.ATTR.RECORD.STATUS` | `AaFeatureAttribute_RecordStatus` | String |  |  |
| 32 | `AA.ATTR.CURR.NO` | `AaFeatureAttribute_CurrNo` | String |  |  |
| 33 | `AA.ATTR.INPUTTER` | `AaFeatureAttribute_Inputter` |  |  |  |
| 34 | `AA.ATTR.DATE.TIME` | `AaFeatureAttribute_DateTime` |  |  |  |
| 35 | `AA.ATTR.AUTHORISER` | `AaFeatureAttribute_Authoriser` | String |  |  |
| 36 | `AA.ATTR.CO.CODE` | `AaFeatureAttribute_CoCode` | String |  |  |
| 37 | `AA.ATTR.DEPT.CODE` | `AaFeatureAttribute_DeptCode` | String |  |  |
| 38 | `AA.ATTR.AUDITOR.CODE` | `AaFeatureAttribute_AuditorCode` | String |  |  |
| 39 | `AA.ATTR.AUDIT.DATE.TIME` | `AaFeatureAttribute_AuditDateTime` | String |  |  |
| 40 | `AA.ATTR.FIELD.APPLICATION` | `AaFeatureAttribute_FieldApplication` |  |  |  |
