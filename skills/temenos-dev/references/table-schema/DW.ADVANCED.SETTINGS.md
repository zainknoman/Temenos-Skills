# DW.ADVANCED.SETTINGS — Table Schema

> Source: `INSERTS/I_F.DW.ADVANCED.SETTINGS` in `DW_BiExportFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DW.AS.ENABLE` | `DwAdvancedSettings_Enable` | TField |  | Supports options YES and NO If YES, then the feature is enabled else it is disabled |
| 2 | `DW.AS.DESCRIPTION` | `DwAdvancedSettings_Description` |  |  |  |
| 3 | `DW.AS.OVERRIDABLE` | `DwAdvancedSettings_Overridable` | TField |  | This is a no input field with values released by core product. Contains value as 'YES' for settings which are eligible for overriding |
| 4 | `DW.AS.ENABLE.DEPENDENT.FEATURES` | `DwAdvancedSettings_EnableDependentFeatures` |  |  |  |
| 5 | `DW.AS.DISABLE.DEPENDENT.FEATURES` | `DwAdvancedSettings_DisableDependentFeatures` |  |  |  |
| 6 | `DW.AS.EFFECTIVE.DATE` | `DwAdvancedSettings_EffectiveDate` | TField |  | This is a date field and can be set with a value from which the enabled feature will be effective. Value can be set only for specific valid features. |
| 7 | `DW.AS.RESERVED.10` | `DwAdvancedSettings_Reserved10` |  |  |  |
| 8 | `DW.AS.RESERVED.9` | `DwAdvancedSettings_Reserved9` |  |  |  |
| 9 | `DW.AS.RESERVED.8` | `DwAdvancedSettings_Reserved8` |  |  |  |
| 10 | `DW.AS.RESERVED.7` | `DwAdvancedSettings_Reserved7` | TField |  |  |
| 11 | `DW.AS.RESERVED.6` | `DwAdvancedSettings_Reserved6` | TField |  |  |
| 12 | `DW.AS.RESERVED.5` | `DwAdvancedSettings_Reserved5` | TField |  |  |
| 13 | `DW.AS.RESERVED.4` | `DwAdvancedSettings_Reserved4` | TField |  |  |
| 14 | `DW.AS.RESERVED.3` | `DwAdvancedSettings_Reserved3` | TField |  |  |
| 15 | `DW.AS.RESERVED.2` | `DwAdvancedSettings_Reserved2` | TField |  |  |
| 16 | `DW.AS.RESERVED.1` | `DwAdvancedSettings_Reserved1` | TField |  |  |
| 17 | `DW.AS.LOCAL.REF` | `DwAdvancedSettings_LocalRef` |  |  |  |
| 18 | `DW.AS.OVERRIDE` | `DwAdvancedSettings_Override` |  |  |  |
| 19 | `DW.AS.RECORD.STATUS` | `DwAdvancedSettings_RecordStatus` | String |  |  |
| 20 | `DW.AS.CURR.NO` | `DwAdvancedSettings_CurrNo` | String |  |  |
| 21 | `DW.AS.INPUTTER` | `DwAdvancedSettings_Inputter` |  |  |  |
| 22 | `DW.AS.DATE.TIME` | `DwAdvancedSettings_DateTime` |  |  |  |
| 23 | `DW.AS.AUTHORISER` | `DwAdvancedSettings_Authoriser` | String |  |  |
| 24 | `DW.AS.CO.CODE` | `DwAdvancedSettings_CoCode` | String |  |  |
| 25 | `DW.AS.DEPT.CODE` | `DwAdvancedSettings_DeptCode` | String |  |  |
| 26 | `DW.AS.AUDITOR.CODE` | `DwAdvancedSettings_AuditorCode` | String |  |  |
| 27 | `DW.AS.AUDIT.DATE.TIME` | `DwAdvancedSettings_AuditDateTime` | String |  |  |
