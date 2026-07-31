# IL.PRODUCT — Table Schema

> Source: `INSERTS/I_F.IL.PRODUCT` in `IL_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IL.PRODUCT.DESCRIPTION` | `IlProduct_Description` |  |  |  |
| 2 | `IL.PRODUCT.RESERVED.10` | `IlProduct_Reserved10` | TField |  |  |
| 3 | `IL.PRODUCT.RESERVED.9` | `IlProduct_Reserved9` | TField |  |  |
| 4 | `IL.PRODUCT.RESERVED.8` | `IlProduct_Reserved8` | TField |  |  |
| 5 | `IL.PRODUCT.RESERVED.7` | `IlProduct_Reserved7` | TField |  |  |
| 6 | `IL.PRODUCT.RESERVED.6` | `IlProduct_Reserved6` | TField |  |  |
| 7 | `IL.PRODUCT.RESERVED.5` | `IlProduct_Reserved5` | TField |  |  |
| 8 | `IL.PRODUCT.RESERVED.4` | `IlProduct_Reserved4` | TField |  |  |
| 9 | `IL.PRODUCT.RESERVED.3` | `IlProduct_Reserved3` | TField |  |  |
| 10 | `IL.PRODUCT.RESERVED.2` | `IlProduct_Reserved2` | TField |  |  |
| 11 | `IL.PRODUCT.RESERVED.1` | `IlProduct_Reserved1` | TField |  |  |
| 12 | `IL.PRODUCT.LOCAL.REF` | `IlProduct_LocalRef` |  |  |  |
| 13 | `IL.PRODUCT.OVERRIDE` | `IlProduct_Override` |  |  |  |
| 14 | `IL.PRODUCT.RECORD.STATUS` | `IlProduct_RecordStatus` | String |  |  |
| 15 | `IL.PRODUCT.CURR.NO` | `IlProduct_CurrNo` | String |  |  |
| 16 | `IL.PRODUCT.INPUTTER` | `IlProduct_Inputter` |  |  |  |
| 17 | `IL.PRODUCT.DATE.TIME` | `IlProduct_DateTime` |  |  |  |
| 18 | `IL.PRODUCT.AUTHORISER` | `IlProduct_Authoriser` | String |  |  |
| 19 | `IL.PRODUCT.CO.CODE` | `IlProduct_CoCode` | String |  |  |
| 20 | `IL.PRODUCT.DEPT.CODE` | `IlProduct_DeptCode` | String |  |  |
| 21 | `IL.PRODUCT.AUDITOR.CODE` | `IlProduct_AuditorCode` | String |  |  |
| 22 | `IL.PRODUCT.AUDIT.DATE.TIME` | `IlProduct_AuditDateTime` | String |  |  |
