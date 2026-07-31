# OC.CLEARING.HOUSE — Table Schema

> Source: `INSERTS/I_F.OC.CLEARING.HOUSE` in `OC_Parameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OC.CLR.HS.REGION` | `OcClearingHouse_Region` | TField | No | Denotes customer's region code. Validation Rules: Optional field Default value is country followed by '00'. |
| 2 | `OC.CLR.HS.INI.MARGIN.CALC` | `OcClearingHouse_IniMarginCalc` | TField | No | Denotes the initial margin method for the clearing house. Reserved for future use. Validation Rules: Optional field. |
| 3 | `OC.CLR.HS.VAR.MARGIN.CALC` | `OcClearingHouse_VarMarginCalc` | TField | No | Denotes the variation margin method for the clearing house. Reserved for future use. Validation Rules: Optional field. |
| 4 | `OC.CLR.HS.INTERFACE` | `OcClearingHouse_Interface` | TField | No | Denotes the interface type. Reserved for future use. Validation Rules: Optional field. Valid values are Auto and Manual. |
| 5 | `OC.CLR.HS.RESERVED10` | `OcClearingHouse_Reserved10` | TField |  |  |
| 6 | `OC.CLR.HS.RESERVED9` | `OcClearingHouse_Reserved9` | TField |  |  |
| 7 | `OC.CLR.HS.RESERVED8` | `OcClearingHouse_Reserved8` | TField |  |  |
| 8 | `OC.CLR.HS.RESERVED7` | `OcClearingHouse_Reserved7` | TField |  |  |
| 9 | `OC.CLR.HS.RESERVED6` | `OcClearingHouse_Reserved6` | TField |  |  |
| 10 | `OC.CLR.HS.RESERVED5` | `OcClearingHouse_Reserved5` | TField |  |  |
| 11 | `OC.CLR.HS.RESERVED4` | `OcClearingHouse_Reserved4` | TField |  |  |
| 12 | `OC.CLR.HS.RESERVED3` | `OcClearingHouse_Reserved3` | TField |  |  |
| 13 | `OC.CLR.HS.RESERVED2` | `OcClearingHouse_Reserved2` | TField |  |  |
| 14 | `OC.CLR.HS.RESERVED1` | `OcClearingHouse_Reserved1` | TField |  |  |
| 15 | `OC.CLR.HS.LOCAL.REF` | `OcClearingHouse_LocalRef` |  |  |  |
| 16 | `OC.CLR.HS.RECORD.STATUS` | `OcClearingHouse_RecordStatus` | String |  |  |
| 17 | `OC.CLR.HS.CURR.NO` | `OcClearingHouse_CurrNo` | String |  |  |
| 18 | `OC.CLR.HS.INPUTTER` | `OcClearingHouse_Inputter` |  |  |  |
| 19 | `OC.CLR.HS.DATE.TIME` | `OcClearingHouse_DateTime` |  |  |  |
| 20 | `OC.CLR.HS.AUTHORISER` | `OcClearingHouse_Authoriser` | String |  |  |
| 21 | `OC.CLR.HS.CO.CODE` | `OcClearingHouse_CoCode` | String |  |  |
| 22 | `OC.CLR.HS.DEPT.CODE` | `OcClearingHouse_DeptCode` | String |  |  |
| 23 | `OC.CLR.HS.AUDITOR.CODE` | `OcClearingHouse_AuditorCode` | String |  |  |
| 24 | `OC.CLR.HS.AUDIT.DATE.TIME` | `OcClearingHouse_AuditDateTime` | String |  |  |
