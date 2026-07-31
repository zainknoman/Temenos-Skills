# EB.API.ATTRIBUTE — Table Schema

> Source: `INSERTS/I_F.EB.API.ATTRIBUTE` in `AA_ProductAttribute.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.API.DESCRIPTION` | `EbApiAttribute_Description` |  |  |  |
| 2 | `EB.API.LONG.DESCRIPTION` | `EbApiAttribute_LongDescription` |  |  |  |
| 3 | `EB.API.ATTRIBUTE.TYPE` | `EbApiAttribute_AttributeType` | TField |  |  |
| 4 | `EB.API.APPLICATION.TYPE` | `EbApiAttribute_ApplicationType` | TField |  |  |
| 5 | `EB.API.APPLICATION.NAME` | `EbApiAttribute_ApplicationName` | TField |  |  |
| 6 | `EB.API.TYPE` | `EbApiAttribute_Type` |  |  |  |
| 7 | `EB.API.RESERVED3` | `EbApiAttribute_Reserved3` | TField |  |  |
| 8 | `EB.API.FIELD.NAME` | `EbApiAttribute_FieldName` |  |  |  |
| 9 | `EB.API.FIELD.LABEL` | `EbApiAttribute_FieldLabel` |  |  |  |
| 10 | `EB.API.FIELD.DESCRIPTION` | `EbApiAttribute_FieldDescription` |  |  |  |
| 11 | `EB.API.FIELD.TYPE` | `EbApiAttribute_FieldType` |  |  |  |
| 12 | `EB.API.LINKED.FIELD` | `EbApiAttribute_LinkedField` |  |  |  |
| 13 | `EB.API.LINKED.NEG.RULE` | `EbApiAttribute_LinkedNegRule` |  |  |  |
| 14 | `EB.API.FIELD.MAX.LENGTH` | `EbApiAttribute_FieldMaxLength` |  |  |  |
| 15 | `EB.API.FIELD.DATA.TYPE` | `EbApiAttribute_FieldDataType` |  |  |  |
| 16 | `EB.API.RESERVED8` | `EbApiAttribute_Reserved8` |  |  |  |
| 17 | `EB.API.OPTION.NAME` | `EbApiAttribute_OptionName` |  |  |  |
| 18 | `EB.API.OPTION.DESCRIPTION` | `EbApiAttribute_OptionDescription` |  |  |  |
| 19 | `EB.API.RESERVED9` | `EbApiAttribute_Reserved9` |  |  |  |
| 20 | `EB.API.DEFAULT.VALUE` | `EbApiAttribute_DefaultValue` |  |  |  |
| 21 | `EB.API.LINKED.ATTRIBUTE` | `EbApiAttribute_LinkedAttribute` |  |  |  |
| 22 | `EB.API.LINKED.ATTRIBUTE.RULE` | `EbApiAttribute_LinkedAttributeRule` |  |  |  |
| 23 | `EB.API.LOCAL.REF` | `EbApiAttribute_LocalRef` |  |  |  |
| 24 | `EB.API.STMT.NOS` | `EbApiAttribute_StmtNos` |  |  |  |
| 25 | `EB.API.OVERRIDE` | `EbApiAttribute_Override` |  |  |  |
| 26 | `EB.API.RECORD.STATUS` | `EbApiAttribute_RecordStatus` | String |  |  |
| 27 | `EB.API.CURR.NO` | `EbApiAttribute_CurrNo` | String |  |  |
| 28 | `EB.API.INPUTTER` | `EbApiAttribute_Inputter` |  |  |  |
| 29 | `EB.API.DATE.TIME` | `EbApiAttribute_DateTime` |  |  |  |
| 30 | `EB.API.AUTHORISER` | `EbApiAttribute_Authoriser` | String |  |  |
| 31 | `EB.API.CO.CODE` | `EbApiAttribute_CoCode` | String |  |  |
| 32 | `EB.API.DEPT.CODE` | `EbApiAttribute_DeptCode` | String |  |  |
| 33 | `EB.API.AUDITOR.CODE` | `EbApiAttribute_AuditorCode` | String |  |  |
| 34 | `EB.API.AUDIT.DATE.TIME` | `EbApiAttribute_AuditDateTime` | String |  |  |
| 35 | `EB.API.OPTION.FILTER` | `EbApiAttribute_OptionFilter` |  |  |  |
| 36 | `EB.API.FIELD.RULE` | `EbApiAttribute_FieldRule` |  |  |  |
| 37 | `EB.API.FIELD.PARAMETER` | `EbApiAttribute_FieldParameter` |  |  |  |
| 38 | `EB.API.FIELD.PARAMETER.VALUE` | `EbApiAttribute_FieldParameterValue` |  |  |  |
| 39 | `EB.API.FIELD.ENABLE.RULE` | `EbApiAttribute_FieldEnableRule` |  |  |  |
