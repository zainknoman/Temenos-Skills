# IF.INWARD.DESIGN.LANDING — Table Schema

> Source: `INSERTS/I_F.IF.INWARD.DESIGN.LANDING` in `IF_InflowCatalog.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IF.ILT.PROCESS.NAME` | `IfInwardDesignLanding_ProcessName` | TField |  |  |
| 2 | `IF.ILT.INFLOW.ATTRIBUTES` | `IfInwardDesignLanding_InflowAttributes` |  |  |  |
| 3 | `IF.ILT.ACT.REFERENCE` | `IfInwardDesignLanding_ActReference` |  |  |  |
| 4 | `IF.ILT.ACT.XML.NAME` | `IfInwardDesignLanding_ActXmlName` |  |  |  |
| 5 | `IF.ILT.T24.OBJECT` | `IfInwardDesignLanding_T24Object` |  |  |  |
| 6 | `IF.ILT.T24.OBJECT.TYPE` | `IfInwardDesignLanding_T24ObjectType` |  |  |  |
| 7 | `IF.ILT.T24.FUNCTION` | `IfInwardDesignLanding_T24Function` |  |  |  |
| 8 | `IF.ILT.RESERVED.1` | `IfInwardDesignLanding_Reserved1` |  |  |  |
| 9 | `IF.ILT.RESERVED.2` | `IfInwardDesignLanding_Reserved2` |  |  |  |
| 10 | `IF.ILT.RESERVED.3` | `IfInwardDesignLanding_Reserved3` |  |  |  |
| 11 | `IF.ILT.RESERVED.4` | `IfInwardDesignLanding_Reserved4` |  |  |  |
| 12 | `IF.ILT.RESERVED.5` | `IfInwardDesignLanding_Reserved5` |  |  |  |
| 13 | `IF.ILT.SOURCE` | `IfInwardDesignLanding_Source` |  |  |  |
| 14 | `IF.ILT.FIELD.NAME` | `IfInwardDesignLanding_FieldName` |  |  |  |
| 15 | `IF.ILT.XML.FIELD.TYPE` | `IfInwardDesignLanding_XmlFieldType` |  |  |  |
| 16 | `IF.ILT.XML.FIELD.NAME` | `IfInwardDesignLanding_XmlFieldName` |  |  |  |
| 17 | `IF.ILT.IS.MANDATORY` | `IfInwardDesignLanding_IsMandatory` |  |  |  |
| 18 | `IF.ILT.MAPPER.ONLY.FIELD` | `IfInwardDesignLanding_MapperOnlyField` |  |  |  |
| 19 | `IF.ILT.MAPPING.DEFINITION` | `IfInwardDesignLanding_MappingDefinition` |  |  |  |
| 20 | `IF.ILT.FIELD.SOURCE` | `IfInwardDesignLanding_FieldSource` |  |  |  |
| 21 | `IF.ILT.RESERVED.6` | `IfInwardDesignLanding_Reserved6` |  |  |  |
| 22 | `IF.ILT.RESERVED.7` | `IfInwardDesignLanding_Reserved7` |  |  |  |
| 23 | `IF.ILT.RESERVED.8` | `IfInwardDesignLanding_Reserved8` |  |  |  |
| 24 | `IF.ILT.RESERVED.9` | `IfInwardDesignLanding_Reserved9` |  |  |  |
| 25 | `IF.ILT.RESERVED.10` | `IfInwardDesignLanding_Reserved10` |  |  |  |
| 26 | `IF.ILT.RESERVED.11` | `IfInwardDesignLanding_Reserved11` |  |  |  |
| 27 | `IF.ILT.RESERVED.12` | `IfInwardDesignLanding_Reserved12` | TField |  |  |
| 28 | `IF.ILT.RESERVED.13` | `IfInwardDesignLanding_Reserved13` | TField |  |  |
| 29 | `IF.ILT.RESERVED.14` | `IfInwardDesignLanding_Reserved14` | TField |  |  |
| 30 | `IF.ILT.RESERVED.15` | `IfInwardDesignLanding_Reserved15` | TField |  |  |
| 31 | `IF.ILT.RESERVED.16` | `IfInwardDesignLanding_Reserved16` | TField |  |  |
| 32 | `IF.ILT.RESERVED.17` | `IfInwardDesignLanding_Reserved17` | TField |  |  |
| 33 | `IF.ILT.RESERVED.18` | `IfInwardDesignLanding_Reserved18` | TField |  |  |
| 34 | `IF.ILT.RESERVED.19` | `IfInwardDesignLanding_Reserved19` | TField |  |  |
| 35 | `IF.ILT.RESERVED.20` | `IfInwardDesignLanding_Reserved20` | TField |  |  |
| 36 | `IF.ILT.AA.PROPERTIES` | `IfInwardDesignLanding_AaProperties` |  |  |  |
| 37 | `IF.ILT.AA.VERSIONS` | `IfInwardDesignLanding_AaVersions` |  |  |  |
| 38 | `IF.ILT.OVERRIDE` | `IfInwardDesignLanding_Override` |  |  |  |
| 39 | `IF.ILT.RECORD.STATUS` | `IfInwardDesignLanding_RecordStatus` | String |  |  |
| 40 | `IF.ILT.CURR.NO` | `IfInwardDesignLanding_CurrNo` | String |  |  |
| 41 | `IF.ILT.INPUTTER` | `IfInwardDesignLanding_Inputter` |  |  |  |
| 42 | `IF.ILT.DATE.TIME` | `IfInwardDesignLanding_DateTime` |  |  |  |
| 43 | `IF.ILT.AUTHORISER` | `IfInwardDesignLanding_Authoriser` | String |  |  |
| 44 | `IF.ILT.CO.CODE` | `IfInwardDesignLanding_CoCode` | String |  |  |
| 45 | `IF.ILT.DEPT.CODE` | `IfInwardDesignLanding_DeptCode` | String |  |  |
| 46 | `IF.ILT.AUDITOR.CODE` | `IfInwardDesignLanding_AuditorCode` | String |  |  |
| 47 | `IF.ILT.AUDIT.DATE.TIME` | `IfInwardDesignLanding_AuditDateTime` | String |  |  |
