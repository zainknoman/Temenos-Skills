# IFRS.IMPAIRMENT.CODE — Table Schema

> Source: `INSERTS/I_F.IFRS.IMPAIRMENT.CODE` in `IA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IIC.SHORT.DESCRIPTION` | `IfrsImpairmentCode_ShortDescription` | TField | Yes | This field holds short description of impairment evidence. Validation Rules: 15 Alphanumeric Characters, free format description. Mandatory input. |
| 2 | `IIC.DESCRIPTION` | `IfrsImpairmentCode_Description` |  |  |  |
| 3 | `IIC.RESERVED.10` | `IfrsImpairmentCode_Reserved10` | TField |  |  |
| 4 | `IIC.RESERVED.9` | `IfrsImpairmentCode_Reserved9` | TField |  |  |
| 5 | `IIC.RESERVED.8` | `IfrsImpairmentCode_Reserved8` | TField |  |  |
| 6 | `IIC.RESERVED.7` | `IfrsImpairmentCode_Reserved7` | TField |  |  |
| 7 | `IIC.RESERVED.6` | `IfrsImpairmentCode_Reserved6` | TField |  |  |
| 8 | `IIC.RESERVED.5` | `IfrsImpairmentCode_Reserved5` | TField |  |  |
| 9 | `IIC.RESERVED.4` | `IfrsImpairmentCode_Reserved4` | TField |  |  |
| 10 | `IIC.RESERVED.3` | `IfrsImpairmentCode_Reserved3` | TField |  |  |
| 11 | `IIC.LOCAL.REF` | `IfrsImpairmentCode_LocalRef` |  |  |  |
| 12 | `IIC.OVERRIDE` | `IfrsImpairmentCode_Override` |  |  |  |
| 13 | `IIC.RECORD.STATUS` | `IfrsImpairmentCode_RecordStatus` | String |  |  |
| 14 | `IIC.CURR.NO` | `IfrsImpairmentCode_CurrNo` | String |  |  |
| 15 | `IIC.INPUTTER` | `IfrsImpairmentCode_Inputter` |  |  |  |
| 16 | `IIC.DATE.TIME` | `IfrsImpairmentCode_DateTime` |  |  |  |
| 17 | `IIC.AUTHORISER` | `IfrsImpairmentCode_Authoriser` | String |  |  |
| 18 | `IIC.CO.CODE` | `IfrsImpairmentCode_CoCode` | String |  |  |
| 19 | `IIC.DEPT.CODE` | `IfrsImpairmentCode_DeptCode` | String |  |  |
| 20 | `IIC.AUDITOR.CODE` | `IfrsImpairmentCode_AuditorCode` | String |  |  |
| 21 | `IIC.AUDIT.DATE.TIME` | `IfrsImpairmentCode_AuditDateTime` | String |  |  |
