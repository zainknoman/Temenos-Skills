# IF.INFLOW.CATALOG — Table Schema

> Source: `INSERTS/I_F.IF.INFLOW.CATALOG` in `IF_InflowCatalog.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IF.IN.INFLOW.NAME` | `IfInflowCatalog_InflowName` | TField |  | Overview This field holds the name of the flow that would be executed by the inflow. Validation Rules This is a no-input field. |
| 2 | `IF.IN.INFLOW.ATTRIBUTES` | `IfInflowCatalog_InflowAttributes` |  |  |  |
| 3 | `IF.IN.RESERVED.1` | `IfInflowCatalog_Reserved1` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 4 | `IF.IN.RESERVED.2` | `IfInflowCatalog_Reserved2` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 5 | `IF.IN.RESERVED.3` | `IfInflowCatalog_Reserved3` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 6 | `IF.IN.RESERVED.4` | `IfInflowCatalog_Reserved4` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 7 | `IF.IN.RESERVED.5` | `IfInflowCatalog_Reserved5` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 8 | `IF.IN.ACTIVITY.REFERENCE` | `IfInflowCatalog_ActivityReference` |  |  |  |
| 9 | `IF.IN.ACT.XML.NAME` | `IfInflowCatalog_ActXmlName` |  |  |  |
| 10 | `IF.IN.T24.OBJECT` | `IfInflowCatalog_T24Object` |  |  |  |
| 11 | `IF.IN.T24.OBJECT.TYPE` | `IfInflowCatalog_T24ObjectType` |  |  |  |
| 12 | `IF.IN.T24.FUNCTION` | `IfInflowCatalog_T24Function` |  |  |  |
| 13 | `IF.IN.RESERVED.11` | `IfInflowCatalog_Reserved11` |  |  |  |
| 14 | `IF.IN.RESERVED.12` | `IfInflowCatalog_Reserved12` |  |  |  |
| 15 | `IF.IN.RESERVED.13` | `IfInflowCatalog_Reserved13` |  |  |  |
| 16 | `IF.IN.RESERVED.14` | `IfInflowCatalog_Reserved14` |  |  |  |
| 17 | `IF.IN.RESERVED.15` | `IfInflowCatalog_Reserved15` |  |  |  |
| 18 | `IF.IN.T24.FIELD.NAME` | `IfInflowCatalog_T24FieldName` |  |  |  |
| 19 | `IF.IN.T24.FIELD.TYPE` | `IfInflowCatalog_T24FieldType` |  |  |  |
| 20 | `IF.IN.XML.FIELD.TYPE` | `IfInflowCatalog_XmlFieldType` |  |  |  |
| 21 | `IF.IN.XML.FIELD.NAME` | `IfInflowCatalog_XmlFieldName` |  |  |  |
| 22 | `IF.IN.IS.MANDATORY` | `IfInflowCatalog_IsMandatory` |  |  |  |
| 23 | `IF.IN.MAPPER.ONLY.FIELD` | `IfInflowCatalog_MapperOnlyField` |  |  |  |
| 24 | `IF.IN.MAPPING.DEFINITION` | `IfInflowCatalog_MappingDefinition` |  |  |  |
| 25 | `IF.IN.IS.RESPONSE.FIELD` | `IfInflowCatalog_IsResponseField` |  |  |  |
| 26 | `IF.IN.RESERVED.22` | `IfInflowCatalog_Reserved22` |  |  |  |
| 27 | `IF.IN.RESERVED.23` | `IfInflowCatalog_Reserved23` |  |  |  |
| 28 | `IF.IN.RESERVED.24` | `IfInflowCatalog_Reserved24` |  |  |  |
| 29 | `IF.IN.RESERVED.25` | `IfInflowCatalog_Reserved25` |  |  |  |
| 30 | `IF.IN.INFLOW.SCHEMA` | `IfInflowCatalog_InflowSchema` | TField |  | Overview This field holds the inflow schema. Validation Rules This is a no-input field. |
| 31 | `IF.IN.IMPORTED.NAME` | `IfInflowCatalog_ImportedName` |  |  |  |
| 32 | `IF.IN.IMPORTED.SCHEMA` | `IfInflowCatalog_ImportedResponseSchema` |  |  |  |
| 33 | `IF.IN.INFLOW.RESPONSE.SCHEMA` | `IfInflowCatalog_InflowSchema` | TField |  | Overview This field holds the inflow schema. Validation Rules This is a no-input field. |
| 34 | `IF.IN.IMPORTED.RESPONSE.NAME` | `IfInflowCatalog_ImportedResponseName` |  |  |  |
| 35 | `IF.IN.IMPORTED.RESPONSE.SCHEMA` | `IfInflowCatalog_ImportedResponseSchema` |  |  |  |
| 36 | `IF.IN.RESERVED.33` | `IfInflowCatalog_Reserved33` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 37 | `IF.IN.RESERVED.34` | `IfInflowCatalog_Reserved34` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 38 | `IF.IN.RESERVED.35` | `IfInflowCatalog_Reserved35` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 39 | `IF.IN.RESERVED.36` | `IfInflowCatalog_Reserved36` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 40 | `IF.IN.RESERVED.37` | `IfInflowCatalog_Reserved37` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 41 | `IF.IN.RESERVED.38` | `IfInflowCatalog_Reserved38` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 42 | `IF.IN.RESERVED.39` | `IfInflowCatalog_Reserved39` | TField |  | Overview This field is reserved for future purpose. Validation Rules This is a no-input field. |
| 43 | `IF.IN.RECORD.STATUS` | `IfInflowCatalog_RecordStatus` | String |  |  |
| 44 | `IF.IN.CURR.NO` | `IfInflowCatalog_CurrNo` | String |  |  |
| 45 | `IF.IN.INPUTTER` | `IfInflowCatalog_Inputter` |  |  |  |
| 46 | `IF.IN.DATE.TIME` | `IfInflowCatalog_DateTime` |  |  |  |
| 47 | `IF.IN.AUTHORISER` | `IfInflowCatalog_Authoriser` | String |  |  |
| 48 | `IF.IN.CO.CODE` | `IfInflowCatalog_CoCode` | String |  |  |
| 49 | `IF.IN.DEPT.CODE` | `IfInflowCatalog_DeptCode` | String |  |  |
| 50 | `IF.IN.AUDITOR.CODE` | `IfInflowCatalog_AuditorCode` | String |  |  |
| 51 | `IF.IN.AUDIT.DATE.TIME` | `IfInflowCatalog_AuditDateTime` | String |  |  |
