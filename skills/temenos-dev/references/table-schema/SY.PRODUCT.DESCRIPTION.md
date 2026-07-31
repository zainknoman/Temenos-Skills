# SY.PRODUCT.DESCRIPTION — Table Schema

> Source: `INSERTS/I_F.SY.PRODUCT.DESCRIPTION` in `SY_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.PS.PRODUCT.DESCRIPTION` | `SyProductDescription_ProductDescription` | TField |  | The Name/ID of the product. |
| 2 | `SY.PS.PRODUCT.DEFINITION` | `SyProductDescription_ProductDefinition` | TField |  | The product defintion (for existing products) of this product. |
| 3 | `SY.PS.SHORT.NAME` | `SyProductDescription_ShortName` |  |  |  |
| 4 | `SY.PS.DESCRIPTION` | `SyProductDescription_Description` |  |  |  |
| 5 | `SY.PS.RESERVED.10` | `SyProductDescription_Reserved10` | TField |  |  |
| 6 | `SY.PS.RESERVED.9` | `SyProductDescription_Reserved9` | TField |  |  |
| 7 | `SY.PS.RESERVED.8` | `SyProductDescription_Reserved8` | TField |  |  |
| 8 | `SY.PS.RESERVED.7` | `SyProductDescription_Reserved7` | TField |  |  |
| 9 | `SY.PS.RESERVED.6` | `SyProductDescription_Reserved6` | TField |  |  |
| 10 | `SY.PS.RESERVED.5` | `SyProductDescription_Reserved5` | TField |  |  |
| 11 | `SY.PS.RESERVED.4` | `SyProductDescription_Reserved4` | TField |  |  |
| 12 | `SY.PS.RESERVED.3` | `SyProductDescription_Reserved3` | TField |  |  |
| 13 | `SY.PS.RESERVED.2` | `SyProductDescription_Reserved2` | TField |  |  |
| 14 | `SY.PS.RESERVED.1` | `SyProductDescription_Reserved1` | TField |  |  |
| 15 | `SY.PS.LOCAL.REF` | `SyProductDescription_LocalRef` |  |  |  |
| 16 | `SY.PS.OVERRIDE` | `SyProductDescription_Override` |  |  |  |
| 17 | `SY.PS.RECORD.STATUS` | `SyProductDescription_RecordStatus` | String |  |  |
| 18 | `SY.PS.CURR.NO` | `SyProductDescription_CurrNo` | String |  |  |
| 19 | `SY.PS.INPUTTER` | `SyProductDescription_Inputter` |  |  |  |
| 20 | `SY.PS.DATE.TIME` | `SyProductDescription_DateTime` |  |  |  |
| 21 | `SY.PS.AUTHORISER` | `SyProductDescription_Authoriser` | String |  |  |
| 22 | `SY.PS.CO.CODE` | `SyProductDescription_CoCode` | String |  |  |
| 23 | `SY.PS.DEPT.CODE` | `SyProductDescription_DeptCode` | String |  |  |
| 24 | `SY.PS.AUDITOR.CODE` | `SyProductDescription_AuditorCode` | String |  |  |
| 25 | `SY.PS.AUDIT.DATE.TIME` | `SyProductDescription_AuditDateTime` | String |  |  |
