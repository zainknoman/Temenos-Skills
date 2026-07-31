# UI.SCENARIOS — Table Schema

> Source: `INSERTS/I_F.UI.SCENARIOS` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UI.SCE.DESCRIPTION` | `UiScenarios_Description` |  |  |  |
| 2 | `UI.SCE.SHORT.DESC` | `UiScenarios_ShortDesc` | TField |  |  |
| 3 | `UI.SCE.RESERVED.10` | `UiScenarios_Reserved10` | TField |  |  |
| 4 | `UI.SCE.RESERVED.9` | `UiScenarios_Reserved9` | TField |  |  |
| 5 | `UI.SCE.RESERVED.8` | `UiScenarios_Reserved8` | TField |  |  |
| 6 | `UI.SCE.RESERVED.7` | `UiScenarios_Reserved7` | TField |  |  |
| 7 | `UI.SCE.RESERVED.6` | `UiScenarios_Reserved6` | TField |  |  |
| 8 | `UI.SCE.RESERVED.5` | `UiScenarios_Reserved5` | TField |  |  |
| 9 | `UI.SCE.RESERVED.4` | `UiScenarios_Reserved4` | TField |  |  |
| 10 | `UI.SCE.RESERVED.3` | `UiScenarios_Reserved3` | TField |  |  |
| 11 | `UI.SCE.RESERVED.2` | `UiScenarios_Reserved2` | TField |  |  |
| 12 | `UI.SCE.RESERVED.1` | `UiScenarios_Reserved1` | TField |  |  |
| 13 | `UI.SCE.RECORD.STATUS` | `UiScenarios_RecordStatus` | String |  |  |
| 14 | `UI.SCE.CURR.NO` | `UiScenarios_CurrNo` | String |  |  |
| 15 | `UI.SCE.INPUTTER` | `UiScenarios_Inputter` |  |  |  |
| 16 | `UI.SCE.DATE.TIME` | `UiScenarios_DateTime` |  |  |  |
| 17 | `UI.SCE.AUTHORISER` | `UiScenarios_Authoriser` | String |  |  |
| 18 | `UI.SCE.CO.CODE` | `UiScenarios_CoCode` | String |  |  |
| 19 | `UI.SCE.DEPT.CODE` | `UiScenarios_DeptCode` | String |  |  |
| 20 | `UI.SCE.AUDITOR.CODE` | `UiScenarios_AuditorCode` | String |  |  |
| 21 | `UI.SCE.AUDIT.DATE.TIME` | `UiScenarios_AuditDateTime` | String |  |  |
