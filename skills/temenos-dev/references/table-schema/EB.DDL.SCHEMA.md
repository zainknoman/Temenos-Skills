# EB.DDL.SCHEMA — Table Schema

> Source: `INSERTS/I_F.EB.DDL.SCHEMA` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DDL.XSD.SHORT.DESC` | `EbDdlSchema_ShortDesc` | TField | Yes | This field contains a short description of the record. Validation Rules: 1. Mandatory field 2. Length: Maximum of 35 and minimum of 3 |
| 2 | `EB.DDL.XSD.DESCRIPTION` | `EbDdlSchema_Description` |  |  |  |
| 3 | `EB.DDL.XSD.DDL` | `EbDdlSchema_Ddl` |  |  |  |
| 4 | `EB.DDL.XSD.SCHEMA` | `EbDdlSchema_Schema` |  |  |  |
| 5 | `EB.DDL.XSD.TABLE.TYPE` | `EbDdlSchema_TableType` | TField |  | This field contains the External DataWarehouse table type. Possible values FACT , DIMENSION or null Validation Rules: 1. If the field is null, it is understood as DIMENSION table. |
| 6 | `EB.DDL.XSD.RESERVED.8` | `EbDdlSchema_Reserved8` | TField |  |  |
| 7 | `EB.DDL.XSD.RESERVED.7` | `EbDdlSchema_Reserved7` | TField |  |  |
| 8 | `EB.DDL.XSD.RESERVED.6` | `EbDdlSchema_Reserved6` | TField |  |  |
| 9 | `EB.DDL.XSD.RESERVED.5` | `EbDdlSchema_Reserved5` | TField |  |  |
| 10 | `EB.DDL.XSD.RESERVED.4` | `EbDdlSchema_Reserved4` | TField |  |  |
| 11 | `EB.DDL.XSD.RESERVED.3` | `EbDdlSchema_Reserved3` | TField |  |  |
| 12 | `EB.DDL.XSD.RESERVED.2` | `EbDdlSchema_Reserved2` | TField |  |  |
| 13 | `EB.DDL.XSD.RESERVED.1` | `EbDdlSchema_Reserved1` | TField |  |  |
| 14 | `EB.DDL.XSD.LOCAL.REF` | `EbDdlSchema_LocalRef` |  |  |  |
| 15 | `EB.DDL.XSD.RECORD.STATUS` | `EbDdlSchema_RecordStatus` | String |  |  |
| 16 | `EB.DDL.XSD.CURR.NO` | `EbDdlSchema_CurrNo` | String |  |  |
| 17 | `EB.DDL.XSD.INPUTTER` | `EbDdlSchema_Inputter` |  |  |  |
| 18 | `EB.DDL.XSD.DATE.TIME` | `EbDdlSchema_DateTime` |  |  |  |
| 19 | `EB.DDL.XSD.AUTHORISER` | `EbDdlSchema_Authoriser` | String |  |  |
| 20 | `EB.DDL.XSD.CO.CODE` | `EbDdlSchema_CoCode` | String |  |  |
| 21 | `EB.DDL.XSD.DEPT.CODE` | `EbDdlSchema_DeptCode` | String |  |  |
| 22 | `EB.DDL.XSD.AUDITOR.CODE` | `EbDdlSchema_AuditorCode` | String |  |  |
| 23 | `EB.DDL.XSD.AUDIT.DATE.TIME` | `EbDdlSchema_AuditDateTime` | String |  |  |
