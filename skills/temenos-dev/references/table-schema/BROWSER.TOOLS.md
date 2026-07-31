# BROWSER.TOOLS — Table Schema

> Source: `INSERTS/I_F.BROWSER.TOOLS` in `EB_Browser.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BRTL.TOOLTIP` | `BrowserTools_Tooltip` |  |  |  |
| 2 | `BRTL.TYPE` | `BrowserTools_Type` | TField | Yes | This field defines the type of tool that is being defined. There are 4 types of tool. ACTION: This type of button does a commit using the function defined in the FUNCTION field for the tool. The value of the ITEM field is also returned to the T24 application and is set in common for the application use. COMMIT: This type of button does a commit using the function defined in the FUNCTION field for the tool. DO.API: This type of button does a call to the API: the value of TARGET is passed into the API as the parameter DO.DEAL: This type of button runs the command line defined in the TARGET field Validation Rules: either ACTION, COMMIT, DO.API or DO.DEAL Mandatory |
| 3 | `BRTL.TEXT` | `BrowserTools_Text` |  |  |  |
| 4 | `BRTL.ATTRIBUTES` | `BrowserTools_Attributes` |  |  |  |
| 5 | `BRTL.IMAGE` | `BrowserTools_Image` | TField |  | This is the name of an image file to display on the button. The filename should be the name of a file stored in the /plaf/images directory on the web server Validation Rules: Any text up to 35 chars |
| 6 | `BRTL.ITEM` | `BrowserTools_Item` |  |  |  |
| 7 | `BRTL.ENABLED` | `BrowserTools_Enabled` | TField | Yes | This field specifies whether the tool is enabled for use. YES or NO Validation Rules: YES or NO Mandatory |
| 8 | `BRTL.SHORTCUT.KEY` | `BrowserTools_ShortcutKey` | TField |  | This field specifies a shortcut to be used on the browser screen Validation Rules: Any Text, one character |
| 9 | `BRTL.FUNCTION` | `BrowserTools_Function` | TField |  | This field specifies what function the tool uses if it is required to perform a commit on the current deal Validation Rules: A, D, R or I |
| 10 | `BRTL.PROV.CONF.PROMPT` | `BrowserTools_ProvConfPrompt` | TField |  | Whether a confirmation message should be displayed when the tool is pressed. The message displayed is that defined by the PROMPT.TEXT field. |
| 11 | `BRTL.PROMPT.TEXT` | `BrowserTools_PromptText` |  |  |  |
| 12 | `BRTL.DISPLAY.TYPE` | `BrowserTools_DisplayType` | TField |  | Determines how the tool should be displayed. The default option is as a button. The tool can also be displayed as an image, as a text hyperline Validation Rules: Image Text Text Image - Future Use |
| 13 | `BRTL.TARGET` | `BrowserTools_Target` | TField |  | This field holds the data that will be used in different ways for different button types ACTION: The contents of this field will be passed back to T24 with a commit. This feature is currently unavailable. DO.DEAL: The contents of this field will be used as the basis for a command line operation DO.API: The contents of this field will be used as the parameter to be passed to the API Target is the destination frame or window in which the output of the action performed is launched. Validation Rules: Any Text up to 35 characters |
| 14 | `BRTL.DEFAULT.TOOL` | `BrowserTools_DefaultTool` | TField |  | Whether the tool should be marked as the default tool on a toolbar. The use of the Return key will activate the default tool. |
| 15 | `BRTL.NAME` | `BrowserTools_Name` | TField |  | The name of the tool. |
| 16 | `BRTL.STYLE` | `BrowserTools_Style` | TField |  |  |
| 17 | `BRTL.RESERVED.5` | `BrowserTools_Reserved5` | TField |  |  |
| 18 | `BRTL.RESERVED.4` | `BrowserTools_Reserved4` | TField |  |  |
| 19 | `BRTL.RESERVED.3` | `BrowserTools_Reserved3` | TField |  |  |
| 20 | `BRTL.RESERVED.2` | `BrowserTools_Reserved2` | TField |  |  |
| 21 | `BRTL.RESERVED.1` | `BrowserTools_Reserved1` | TField |  |  |
| 22 | `BRTL.RECORD.STATUS` | `BrowserTools_RecordStatus` | String |  |  |
| 23 | `BRTL.CURR.NO` | `BrowserTools_CurrNo` | String |  |  |
| 24 | `BRTL.INPUTTER` | `BrowserTools_Inputter` |  |  |  |
| 25 | `BRTL.DATE.TIME` | `BrowserTools_DateTime` |  |  |  |
| 26 | `BRTL.AUTHORISER` | `BrowserTools_Authoriser` | String |  |  |
| 27 | `BRTL.CO.CODE` | `BrowserTools_CoCode` | String |  |  |
| 28 | `BRTL.DEPT.CODE` | `BrowserTools_DeptCode` | String |  |  |
| 29 | `BRTL.AUDITOR.CODE` | `BrowserTools_AuditorCode` | String |  |  |
| 30 | `BRTL.AUDIT.DATE.TIME` | `BrowserTools_AuditDateTime` | String |  |  |
