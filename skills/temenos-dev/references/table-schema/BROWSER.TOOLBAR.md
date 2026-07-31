# BROWSER.TOOLBAR — Table Schema

> Source: `INSERTS/I_F.BROWSER.TOOLBAR` in `EB_Browser.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BRTB.TOOL.ID` | `BrowserToolbar_ToolId` |  |  |  |
| 2 | `BRTB.TOOLBAR.TEXT` | `BrowserToolbar_ToolbarText` |  |  |  |
| 3 | `BRTB.ORIENTATION` | `BrowserToolbar_Orientation` | TField |  |  |
| 4 | `BRTB.STYLE` | `BrowserToolbar_Style` | TField |  |  |
| 5 | `BRTB.RESERVED3` | `BrowserToolbar_Reserved3` | TField |  |  |
| 6 | `BRTB.RESERVED4` | `BrowserToolbar_Reserved4` | TField |  |  |
| 7 | `BRTB.RESERVED5` | `BrowserToolbar_Reserved5` | TField |  |  |
| 8 | `BRTB.RESERVED6` | `BrowserToolbar_Reserved6` | TField |  |  |
| 9 | `BRTB.RESERVED7` | `BrowserToolbar_Reserved7` | TField |  |  |
| 10 | `BRTB.RESERVED8` | `BrowserToolbar_Reserved8` | TField |  |  |
| 11 | `BRTB.RESERVED9` | `BrowserToolbar_Reserved9` | TField |  |  |
| 12 | `BRTB.RESERVED10` | `BrowserToolbar_Reserved10` | TField |  |  |
| 13 | `BRTB.RECORD.STATUS` | `BrowserToolbar_RecordStatus` | String |  |  |
| 14 | `BRTB.CURR.NO` | `BrowserToolbar_CurrNo` | String |  |  |
| 15 | `BRTB.INPUTTER` | `BrowserToolbar_Inputter` |  |  |  |
| 16 | `BRTB.DATE.TIME` | `BrowserToolbar_DateTime` |  |  |  |
| 17 | `BRTB.AUTHORISER` | `BrowserToolbar_Authoriser` | String |  |  |
| 18 | `BRTB.CO.CODE` | `BrowserToolbar_CoCode` | String |  |  |
| 19 | `BRTB.DEPT.CODE` | `BrowserToolbar_DeptCode` | String |  |  |
| 20 | `BRTB.AUDITOR.CODE` | `BrowserToolbar_AuditorCode` | String |  |  |
| 21 | `BRTB.AUDIT.DATE.TIME` | `BrowserToolbar_AuditDateTime` | String |  |  |
