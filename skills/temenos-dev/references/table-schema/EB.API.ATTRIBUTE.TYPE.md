# EB.API.ATTRIBUTE.TYPE — Table Schema

> Source: `INSERTS/I_F.EB.API.ATTRIBUTE.TYPE` in `AA_ProductAttribute.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.API.DESCRIPTION` | `EbApiAttributeType_Description` |  |  |  |
| 2 | `EB.API.LONG.DESCRIPTION` | `EbApiAttributeType_LongDescription` |  |  |  |
| 3 | `EB.API.APPLICATION.TYPE` | `EbApiAttributeType_ApplicationType` | TField |  |  |
| 4 | `EB.API.APPLICATION.NAME` | `EbApiAttributeType_ApplicationName` | TField |  |  |
| 5 | `EB.API.TYPE` | `EbApiAttributeType_Type` |  |  |  |
| 6 | `EB.API.RESERVED1` | `EbApiAttributeType_Reserved1` | TField |  |  |
| 7 | `EB.API.FIELD.NAME` | `EbApiAttributeType_FieldName` |  |  |  |
| 8 | `EB.API.RESERVED2` | `EbApiAttributeType_Reserved2` |  |  |  |
| 9 | `EB.API.FIELD.LABEL` | `EbApiAttributeType_FieldLabel` |  |  |  |
| 10 | `EB.API.FIELD.DESCRIPTION` | `EbApiAttributeType_FieldDescription` |  |  |  |
| 11 | `EB.API.FIELD.TYPE` | `EbApiAttributeType_FieldType` |  |  |  |
| 12 | `EB.API.RESERVED7` | `EbApiAttributeType_Reserved7` |  |  |  |
| 13 | `EB.API.LINKED.FIELD` | `EbApiAttributeType_LinkedField` |  |  |  |
| 14 | `EB.API.LINKED.NEG.RULE` | `EbApiAttributeType_LinkedNegRule` |  |  |  |
| 15 | `EB.API.FIELD.MAX.LENGTH` | `EbApiAttributeType_FieldMaxLength` |  |  |  |
| 16 | `EB.API.FIELD.DATA.TYPE` | `EbApiAttributeType_FieldDataType` |  |  |  |
| 17 | `EB.API.RESERVED3` | `EbApiAttributeType_Reserved3` |  |  |  |
| 18 | `EB.API.OPTION.NAME` | `EbApiAttributeType_OptionName` |  |  |  |
| 19 | `EB.API.OPTION.DESCRIPTION` | `EbApiAttributeType_OptionDescription` |  |  |  |
| 20 | `EB.API.RESERVED4` | `EbApiAttributeType_Reserved4` |  |  |  |
| 21 | `EB.API.OPTION.TABLE` | `EbApiAttributeType_OptionTable` |  |  |  |
| 22 | `EB.API.DEFAULT.VALUE` | `EbApiAttributeType_DefaultValue` |  |  |  |
| 23 | `EB.API.LINKED.ATTRIBUTE.TYPE` | `EbApiAttributeType_LinkedAttributeType` |  |  |  |
| 24 | `EB.API.LINKED.ATTRIBUTE.TYPE.RULE` | `EbApiAttributeType_LinkedAttributeTypeRule` |  |  |  |
| 25 | `EB.API.RESERVED6` | `EbApiAttributeType_Reserved6` | TField |  |  |
| 26 | `EB.API.LOCAL.REF` | `EbApiAttributeType_LocalRef` |  |  |  |
| 27 | `EB.API.STMT.NOS` | `EbApiAttributeType_StmtNos` |  |  |  |
| 28 | `EB.API.OVERRIDE` | `EbApiAttributeType_Override` |  |  |  |
| 29 | `EB.API.RECORD.STATUS` | `EbApiAttributeType_RecordStatus` | String |  |  |
| 30 | `EB.API.CURR.NO` | `EbApiAttributeType_CurrNo` | String |  |  |
| 31 | `EB.API.INPUTTER` | `EbApiAttributeType_Inputter` |  |  |  |
| 32 | `EB.API.DATE.TIME` | `EbApiAttributeType_DateTime` |  |  |  |
| 33 | `EB.API.AUTHORISER` | `EbApiAttributeType_Authoriser` | String |  |  |
| 34 | `EB.API.CO.CODE` | `EbApiAttributeType_CoCode` | String |  |  |
| 35 | `EB.API.DEPT.CODE` | `EbApiAttributeType_DeptCode` | String |  |  |
| 36 | `EB.API.AUDITOR.CODE` | `EbApiAttributeType_AuditorCode` | String |  |  |
| 37 | `EB.API.AUDIT.DATE.TIME` | `EbApiAttributeType_AuditDateTime` | String |  |  |
| 38 | `EB.API.OPTION.FILTER` | `EbApiAttributeType_OptionFilter` |  |  |  |
| 39 | `EB.API.FIELD.RULE` | `EbApiAttributeType_FieldRule` |  |  |  |
| 40 | `EB.API.FIELD.PARAMETER` | `EbApiAttributeType_FieldParameter` |  |  |  |
| 41 | `EB.API.FIELD.PARAMETER.VALUE` | `EbApiAttributeType_FieldParameterValue` |  |  |  |
| 42 | `EB.API.FIELD.ENABLE.RULE` | `EbApiAttributeType_FieldEnableRule` |  |  |  |
