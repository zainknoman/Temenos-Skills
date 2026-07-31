# DW.PRODUCT — Table Schema

> Source: `INSERTS/I_F.DW.PRODUCT` in `DW_BiExportFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.PR.DESCRIPTION` | `DwProduct_Description` |  |  |  |
| 2 | `DW.PR.RESERVED.10` | `DwProduct_Reserved10` | TField |  |  |
| 3 | `DW.PR.RESERVED.9` | `DwProduct_Reserved9` | TField |  |  |
| 4 | `DW.PR.RESERVED.8` | `DwProduct_Reserved8` | TField |  |  |
| 5 | `DW.PR.RESERVED.7` | `DwProduct_Reserved7` | TField |  |  |
| 6 | `DW.PR.RESERVED.6` | `DwProduct_Reserved6` | TField |  |  |
| 7 | `DW.PR.RESERVED.5` | `DwProduct_Reserved5` | TField |  |  |
| 8 | `DW.PR.RESERVED.4` | `DwProduct_Reserved4` | TField |  |  |
| 9 | `DW.PR.RESERVED.3` | `DwProduct_Reserved3` | TField |  |  |
| 10 | `DW.PR.RESERVED.2` | `DwProduct_Reserved2` | TField |  |  |
| 11 | `DW.PR.RESERVED.1` | `DwProduct_Reserved1` | TField |  |  |
| 12 | `DW.PR.OVERRIDE` | `DwProduct_Override` |  |  |  |
| 13 | `DW.PR.LOCAL.REF` | `DwProduct_LocalRef` |  |  |  |
| 14 | `DW.PR.RECORD.STATUS` | `DwProduct_RecordStatus` | String |  |  |
| 15 | `DW.PR.CURR.NO` | `DwProduct_CurrNo` | String |  |  |
| 16 | `DW.PR.INPUTTER` | `DwProduct_Inputter` |  |  |  |
| 17 | `DW.PR.DATE.TIME` | `DwProduct_DateTime` |  |  |  |
| 18 | `DW.PR.AUTHORISER` | `DwProduct_Authoriser` | String |  |  |
| 19 | `DW.PR.CO.CODE` | `DwProduct_CoCode` | String |  |  |
| 20 | `DW.PR.DEPT.CODE` | `DwProduct_DeptCode` | String |  |  |
| 21 | `DW.PR.AUDITOR.CODE` | `DwProduct_AuditorCode` | String |  |  |
| 22 | `DW.PR.AUDIT.DATE.TIME` | `DwProduct_AuditDateTime` | String |  |  |
