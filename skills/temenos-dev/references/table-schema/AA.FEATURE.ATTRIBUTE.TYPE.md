# AA.FEATURE.ATTRIBUTE.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.FEATURE.ATTRIBUTE.TYPE` in `AA_Feature.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ATTR.DESCRIPTION` | `AaFeatureAttributeType_Description` |  |  |  |
| 2 | `AA.ATTR.LONG.DESCRIPTION` | `AaFeatureAttributeType_LongDescription` |  |  |  |
| 3 | `AA.ATTR.APPLICATION.TYPE` | `AaFeatureAttributeType_ApplicationType` | TField |  | Indicator for type of application.Valid options are NULL and PropertyClass. |
| 4 | `AA.ATTR.APPLICATION.NAME` | `AaFeatureAttributeType_ApplicationName` | TField |  | Name of the application where the fields exist. This should be a valid entry in PGM.FILE under H, W or V types. |
| 5 | `AA.ATTR.TYPE` | `AaFeatureAttributeType_Type` |  |  |  |
| 6 | `AA.ATTR.RESERVED1` | `AaFeatureAttributeType_Reserved1` | TField |  |  |
| 7 | `AA.ATTR.FIELD.NAME` | `AaFeatureAttributeType_FieldName` |  |  |  |
| 8 | `AA.ATTR.FIELD.APPLICATION` | `AaFeatureAttributeType_FieldApplication` |  |  |  |
| 9 | `AA.ATTR.FIELD.LABEL` | `AaFeatureAttributeType_FieldLabel` |  |  |  |
| 10 | `AA.ATTR.FIELD.DESCRIPTION` | `AaFeatureAttributeType_FieldDescription` |  |  |  |
| 11 | `AA.ATTR.FIELD.TYPE` | `AaFeatureAttributeType_FieldType` |  |  |  |
| 12 | `AA.ATTR.EXCLUSIVE.GROUP` | `AaFeatureAttributeType_ExclusiveGroup` |  |  |  |
| 13 | `AA.ATTR.LINKED.FIELD` | `AaFeatureAttributeType_LinkedField` |  |  |  |
| 14 | `AA.ATTR.LINKED.NEG.RULE` | `AaFeatureAttributeType_LinkedNegRule` |  |  |  |
| 15 | `AA.ATTR.FIELD.MAX.LENGTH` | `AaFeatureAttributeType_FieldMaxLength` |  |  |  |
| 16 | `AA.ATTR.FIELD.DATA.TYPE` | `AaFeatureAttributeType_FieldDataType` |  |  |  |
| 17 | `AA.ATTR.TOOLTIP` | `AaFeatureAttributeType_Tooltip` |  |  |  |
| 18 | `AA.ATTR.OPTION.NAME` | `AaFeatureAttributeType_OptionName` |  |  |  |
| 19 | `AA.ATTR.OPTION.DESCRIPTION` | `AaFeatureAttributeType_OptionDescription` |  |  |  |
| 20 | `AA.ATTR.RESERVED4` | `AaFeatureAttributeType_Reserved4` |  |  |  |
| 21 | `AA.ATTR.OPTION.TABLE` | `AaFeatureAttributeType_OptionTable` |  |  |  |
| 22 | `AA.ATTR.OPTION.FILTER` | `AaFeatureAttributeType_OptionFilter` |  |  |  |
| 23 | `AA.ATTR.DEFAULT.VALUE` | `AaFeatureAttributeType_DefaultValue` |  |  |  |
| 24 | `AA.ATTR.FIELD.PARAMETER` | `AaFeatureAttributeType_FieldParameter` |  |  |  |
| 25 | `AA.ATTR.FIELD.PARAMETER.VALUE` | `AaFeatureAttributeType_FieldParameterValue` |  |  |  |
| 26 | `AA.ATTR.FIELD.RULE` | `AaFeatureAttributeType_FieldRule` |  |  |  |
| 27 | `AA.ATTR.FIELD.ENABLE.RULE` | `AaFeatureAttributeType_FieldEnableRule` |  |  |  |
| 28 | `AA.ATTR.LINKED.ATTRIBUTE.TYPE` | `AaFeatureAttributeType_LinkedAttributeType` |  |  |  |
| 29 | `AA.ATTR.LINKED.ATTRIBUTE.TYPE.RULE` | `AaFeatureAttributeType_LinkedAttributeTypeRule` |  |  |  |
| 30 | `AA.ATTR.RESERVED6` | `AaFeatureAttributeType_Reserved6` | TField |  |  |
| 31 | `AA.ATTR.LOCAL.REF` | `AaFeatureAttributeType_LocalRef` |  |  |  |
| 32 | `AA.ATTR.STMT.NOS` | `AaFeatureAttributeType_StmtNos` |  |  |  |
| 33 | `AA.ATTR.OVERRIDE` | `AaFeatureAttributeType_Override` |  |  |  |
| 34 | `AA.ATTR.RECORD.STATUS` | `AaFeatureAttributeType_RecordStatus` | String |  |  |
| 35 | `AA.ATTR.CURR.NO` | `AaFeatureAttributeType_CurrNo` | String |  |  |
| 36 | `AA.ATTR.INPUTTER` | `AaFeatureAttributeType_Inputter` |  |  |  |
| 37 | `AA.ATTR.DATE.TIME` | `AaFeatureAttributeType_DateTime` |  |  |  |
| 38 | `AA.ATTR.AUTHORISER` | `AaFeatureAttributeType_Authoriser` | String |  |  |
| 39 | `AA.ATTR.CO.CODE` | `AaFeatureAttributeType_CoCode` | String |  |  |
| 40 | `AA.ATTR.DEPT.CODE` | `AaFeatureAttributeType_DeptCode` | String |  |  |
| 41 | `AA.ATTR.AUDITOR.CODE` | `AaFeatureAttributeType_AuditorCode` | String |  |  |
| 42 | `AA.ATTR.AUDIT.DATE.TIME` | `AaFeatureAttributeType_AuditDateTime` | String |  |  |
