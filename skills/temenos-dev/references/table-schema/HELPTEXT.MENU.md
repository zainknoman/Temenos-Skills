# HELPTEXT.MENU — Table Schema

> Source: `INSERTS/I_F.HELPTEXT.MENU` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MEN.APPLICATION` | `HelptextMenu_Application` |  |  |  |
| 2 | `EB.MEN.DESCRIPT` | `HelptextMenu_Descript` |  |  |  |
| 3 | `EB.MEN.DISPL.APPLICATION` | `HelptextMenu_DisplApplication` | TField |  | Allows the user to request the inclusion of the Application name when displaying the menu. Validation Rules: The following values will be accepted in this field: Y: to request the display of the Application name. blank when the Application entered in field GB TITLE must not be displayed in the menu. |
| 4 | `EB.MEN.OVERRIDE` | `HelptextMenu_Override` |  |  |  |
| 5 | `EB.MEN.RECORD.STATUS` | `HelptextMenu_RecordStatus` | String |  |  |
| 6 | `EB.MEN.CURR.NO` | `HelptextMenu_CurrNo` | String |  |  |
| 7 | `EB.MEN.INPUTTER` | `HelptextMenu_Inputter` |  |  |  |
| 8 | `EB.MEN.DATE.TIME` | `HelptextMenu_DateTime` |  |  |  |
| 9 | `EB.MEN.AUTHORISER` | `HelptextMenu_Authoriser` | String |  |  |
| 10 | `EB.MEN.CO.CODE` | `HelptextMenu_CoCode` | String |  |  |
| 11 | `EB.MEN.DEPT.CODE` | `HelptextMenu_DeptCode` | String |  |  |
| 12 | `EB.MEN.AUDITOR.CODE` | `HelptextMenu_AuditorCode` | String |  |  |
| 13 | `EB.MEN.AUDIT.DATE.TIME` | `HelptextMenu_AuditDateTime` | String |  |  |
