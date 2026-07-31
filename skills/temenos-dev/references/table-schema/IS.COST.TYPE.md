# IS.COST.TYPE — Table Schema

> Source: `INSERTS/I_F.IS.COST.TYPE` in `IS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.COS.DESCRIPTION` | `IsCostType_Description` |  |  |  |
| 2 | `IS.COS.STATUS` | `IsCostType_Status` | TField | Yes | Defines the status of the cost. The values to the field are defined in the EB.LOOKUP table with prefix &quot;IS.STATUS*&quot;. Validation Rules: 1. Valid values like Active, Inactive are defined in the EB.LOOKUP table with prefix &quot;IS.STATUS*&quot;. 2. Mandatory field. |
| 3 | `IS.COS.CHARGE.CODE` | `IsCostType_ChargeCode` | TField | Yes | The FT.CHARGE.TYPE or FT.COMMISSION.TYPE can be specified in order to default the charge amount for the cost in the Purchase contract. Validation Rules: 1. Valid values are FT.CHARGE.TYPE or FT.COMMISSION.TYPE codes. 2. Mandatory field. |
| 4 | `IS.COS.RESERVED.5` | `IsCostType_Reserved5` | TField |  |  |
| 5 | `IS.COS.RESERVED.4` | `IsCostType_Reserved4` | TField |  |  |
| 6 | `IS.COS.RESERVED.3` | `IsCostType_Reserved3` | TField |  |  |
| 7 | `IS.COS.RESERVED.2` | `IsCostType_Reserved2` | TField |  |  |
| 8 | `IS.COS.RESERVED.1` | `IsCostType_Reserved1` | TField |  |  |
| 9 | `IS.COS.LOCAL.REF` | `IsCostType_LocalRef` |  |  |  |
| 10 | `IS.COS.OVERRIDE` | `IsCostType_Override` |  |  |  |
| 11 | `IS.COS.RECORD.STATUS` | `IsCostType_RecordStatus` | String |  |  |
| 12 | `IS.COS.CURR.NO` | `IsCostType_CurrNo` | String |  |  |
| 13 | `IS.COS.INPUTTER` | `IsCostType_Inputter` |  |  |  |
| 14 | `IS.COS.DATE.TIME` | `IsCostType_DateTime` |  |  |  |
| 15 | `IS.COS.AUTHORISER` | `IsCostType_Authoriser` | String |  |  |
| 16 | `IS.COS.CO.CODE` | `IsCostType_CoCode` | String |  |  |
| 17 | `IS.COS.DEPT.CODE` | `IsCostType_DeptCode` | String |  |  |
| 18 | `IS.COS.AUDITOR.CODE` | `IsCostType_AuditorCode` | String |  |  |
| 19 | `IS.COS.AUDIT.DATE.TIME` | `IsCostType_AuditDateTime` | String |  |  |
