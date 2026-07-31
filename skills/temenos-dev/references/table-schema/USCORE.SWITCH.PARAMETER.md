# USCORE.SWITCH.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USCORE.SWITCH.PARAMETER` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.SWITCH.DESCRIPTION` | `UscoreSwitchParameter_Description` | TField |  | Specify the brief description for the purpose of the record. |
| 2 | `USCORE.SWITCH.FEATURES` | `UscoreSwitchParameter_Features` |  |  |  |
| 3 | `USCORE.SWITCH.FEATURE.KEY` | `UscoreSwitchParameter_FeatureKey` |  |  |  |
| 4 | `USCORE.SWITCH.COMPONENT` | `UscoreSwitchParameter_Component` |  |  |  |
| 5 | `USCORE.SWITCH.RESERVED.18` | `UscoreSwitchParameter_Reserved18` |  |  |  |
| 6 | `USCORE.SWITCH.RESERVED.17` | `UscoreSwitchParameter_Reserved17` |  |  |  |
| 7 | `USCORE.SWITCH.RESERVED.16` | `UscoreSwitchParameter_Reserved16` |  |  |  |
| 8 | `USCORE.SWITCH.DEFAULT.COMPONENT` | `UscoreSwitchParameter_DefaultComponent` | TField |  | If none of the component specified in the field COMPONENT then the default component will be loaded. |
| 9 | `USCORE.SWITCH.ENQ.RTN` | `UscoreSwitchParameter_EnqRtn` |  |  |  |
| 10 | `USCORE.SWITCH.TAB.RTN` | `UscoreSwitchParameter_TabRtn` |  |  |  |
| 11 | `USCORE.SWITCH.VER.RTN` | `UscoreSwitchParameter_VerRtn` |  |  |  |
| 12 | `USCORE.SWITCH.MENU.RTN` | `UscoreSwitchParameter_MenuRtn` |  |  |  |
| 13 | `USCORE.SWITCH.COS.RTN` | `UscoreSwitchParameter_CosRtn` |  |  |  |
| 14 | `USCORE.SWITCH.RESERVED.9` | `UscoreSwitchParameter_Reserved9` | TField |  |  |
| 15 | `USCORE.SWITCH.RESERVED.8` | `UscoreSwitchParameter_Reserved8` | TField |  |  |
| 16 | `USCORE.SWITCH.RESERVED.7` | `UscoreSwitchParameter_Reserved7` | TField |  |  |
| 17 | `USCORE.SWITCH.RESERVED.6` | `UscoreSwitchParameter_Reserved6` | TField |  |  |
| 18 | `USCORE.SWITCH.RESERVED.5` | `UscoreSwitchParameter_Reserved5` | TField |  |  |
| 19 | `USCORE.SWITCH.RESERVED.4` | `UscoreSwitchParameter_Reserved4` | TField |  |  |
| 20 | `USCORE.SWITCH.RESERVED.3` | `UscoreSwitchParameter_Reserved3` | TField |  |  |
| 21 | `USCORE.SWITCH.RESERVED.2` | `UscoreSwitchParameter_Reserved2` | TField |  |  |
| 22 | `USCORE.SWITCH.RESERVED.1` | `UscoreSwitchParameter_Reserved1` | TField |  |  |
| 23 | `USCORE.SWITCH.RECORD.STATUS` | `UscoreSwitchParameter_RecordStatus` | String |  |  |
| 24 | `USCORE.SWITCH.CURR.NO` | `UscoreSwitchParameter_CurrNo` | String |  |  |
| 25 | `USCORE.SWITCH.INPUTTER` | `UscoreSwitchParameter_Inputter` |  |  |  |
| 26 | `USCORE.SWITCH.DATE.TIME` | `UscoreSwitchParameter_DateTime` |  |  |  |
| 27 | `USCORE.SWITCH.AUTHORISER` | `UscoreSwitchParameter_Authoriser` | String |  |  |
| 28 | `USCORE.SWITCH.CO.CODE` | `UscoreSwitchParameter_CoCode` | String |  |  |
| 29 | `USCORE.SWITCH.DEPT.CODE` | `UscoreSwitchParameter_DeptCode` | String |  |  |
| 30 | `USCORE.SWITCH.AUDITOR.CODE` | `UscoreSwitchParameter_AuditorCode` | String |  |  |
| 31 | `USCORE.SWITCH.AUDIT.DATE.TIME` | `UscoreSwitchParameter_AuditDateTime` | String |  |  |
