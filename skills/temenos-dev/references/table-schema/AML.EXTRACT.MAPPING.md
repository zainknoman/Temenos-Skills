# AML.EXTRACT.MAPPING — Table Schema

> Source: `INSERTS/I_F.AML.EXTRACT.MAPPING` in `VP_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AML.EXT.DESCRIPTION` | `AmlExtractMapping_Description` |  |  |  |
| 2 | `AML.EXT.FIELD.TYPE` | `AmlExtractMapping_FieldType` |  |  |  |
| 3 | `AML.EXT.SYS.FIELD.NAME` | `AmlExtractMapping_SysFieldName` |  |  |  |
| 4 | `AML.EXT.FIELD.LENGTH` | `AmlExtractMapping_FieldLength` |  |  |  |
| 5 | `AML.EXT.RESERVED.10` | `AmlExtractMapping_Reserved10` | TField |  |  |
| 6 | `AML.EXT.RESERVED.9` | `AmlExtractMapping_Reserved9` | TField |  |  |
| 7 | `AML.EXT.RESERVED.8` | `AmlExtractMapping_Reserved8` | TField |  |  |
| 8 | `AML.EXT.RESERVED.7` | `AmlExtractMapping_Reserved7` | TField |  |  |
| 9 | `AML.EXT.RESERVED.6` | `AmlExtractMapping_Reserved6` | TField |  |  |
| 10 | `AML.EXT.RESERVED.5` | `AmlExtractMapping_Reserved5` | TField |  |  |
| 11 | `AML.EXT.RESERVED.4` | `AmlExtractMapping_Reserved4` | TField |  |  |
| 12 | `AML.EXT.RESERVED.3` | `AmlExtractMapping_Reserved3` | TField |  |  |
| 13 | `AML.EXT.RESERVED.2` | `AmlExtractMapping_Reserved2` | TField |  |  |
| 14 | `AML.EXT.RESERVED.1` | `AmlExtractMapping_Reserved1` | TField |  |  |
| 15 | `AML.EXT.OVERRIDE` | `AmlExtractMapping_Override` |  |  |  |
| 16 | `AML.EXT.RECORD.STATUS` | `AmlExtractMapping_RecordStatus` | String |  |  |
| 17 | `AML.EXT.CURR.NO` | `AmlExtractMapping_CurrNo` | String |  |  |
| 18 | `AML.EXT.INPUTTER` | `AmlExtractMapping_Inputter` |  |  |  |
| 19 | `AML.EXT.DATE.TIME` | `AmlExtractMapping_DateTime` |  |  |  |
| 20 | `AML.EXT.AUTHORISER` | `AmlExtractMapping_Authoriser` | String |  |  |
| 21 | `AML.EXT.CO.CODE` | `AmlExtractMapping_CoCode` | String |  |  |
| 22 | `AML.EXT.DEPT.CODE` | `AmlExtractMapping_DeptCode` | String |  |  |
| 23 | `AML.EXT.AUDITOR.CODE` | `AmlExtractMapping_AuditorCode` | String |  |  |
| 24 | `AML.EXT.AUDIT.DATE.TIME` | `AmlExtractMapping_AuditDateTime` | String |  |  |
