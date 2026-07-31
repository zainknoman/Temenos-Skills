# INTERFACE.MAPPING — Table Schema

> Source: `INSERTS/I_F.INTERFACE.MAPPING` in `CABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INT.MAP.PAR.INTF.FIELD.NAME` | `InterfaceMapping_IntfFieldName` |  |  |  |
| 2 | `INT.MAP.PAR.APPL.FIELD.NAME` | `InterfaceMapping_ApplFieldName` |  |  |  |
| 3 | `INT.MAP.PAR.CONV.PARAM` | `InterfaceMapping_ConvParam` |  |  |  |
| 4 | `INT.MAP.PAR.CONV.FUNC` | `InterfaceMapping_ConvFunc` |  |  |  |
| 5 | `INT.MAP.PAR.RESERVED.8` | `InterfaceMapping_Reserved8` | TField |  |  |
| 6 | `INT.MAP.PAR.RESERVED.7` | `InterfaceMapping_Reserved7` | TField |  |  |
| 7 | `INT.MAP.PAR.RESERVED.6` | `InterfaceMapping_Reserved6` | TField |  |  |
| 8 | `INT.MAP.PAR.RESERVED.5` | `InterfaceMapping_Reserved5` | TField |  |  |
| 9 | `INT.MAP.PAR.RESERVED.4` | `InterfaceMapping_Reserved4` | TField |  |  |
| 10 | `INT.MAP.PAR.RESERVED.3` | `InterfaceMapping_Reserved3` | TField |  |  |
| 11 | `INT.MAP.PAR.RESERVED.2` | `InterfaceMapping_Reserved2` | TField |  |  |
| 12 | `INT.MAP.PAR.RESERVED.1` | `InterfaceMapping_Reserved1` | TField |  |  |
| 13 | `INT.MAP.PAR.OVERRIDE` | `InterfaceMapping_Override` |  |  |  |
| 14 | `INT.MAP.PAR.RECORD.STATUS` | `InterfaceMapping_RecordStatus` | String |  |  |
| 15 | `INT.MAP.PAR.CURR.NO` | `InterfaceMapping_CurrNo` | String |  |  |
| 16 | `INT.MAP.PAR.INPUTTER` | `InterfaceMapping_Inputter` |  |  |  |
| 17 | `INT.MAP.PAR.DATE.TIME` | `InterfaceMapping_DateTime` |  |  |  |
| 18 | `INT.MAP.PAR.AUTHORISER` | `InterfaceMapping_Authoriser` | String |  |  |
| 19 | `INT.MAP.PAR.CO.CODE` | `InterfaceMapping_CoCode` | String |  |  |
| 20 | `INT.MAP.PAR.DEPT.CODE` | `InterfaceMapping_DeptCode` | String |  |  |
| 21 | `INT.MAP.PAR.AUDITOR.CODE` | `InterfaceMapping_AuditorCode` | String |  |  |
| 22 | `INT.MAP.PAR.AUDIT.DATE.TIME` | `InterfaceMapping_AuditDateTime` | String |  |  |
