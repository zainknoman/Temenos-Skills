# BROWSER.MULTI.APP.PARAM — Table Schema

> Source: `INSERTS/I_F.BROWSER.MULTI.APP.PARAM` in `FS_ApplicationFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BROWSER.MULTI.CHILD.APP.NAME` | `BrowserMultiAppParam_ChildAppName` |  |  |  |
| 2 | `BROWSER.MULTI.RECORD.STATUS` | `BrowserMultiAppParam_RecordStatus` | String |  |  |
| 3 | `BROWSER.MULTI.CURR.NO` | `BrowserMultiAppParam_CurrNo` | String |  |  |
| 4 | `BROWSER.MULTI.INPUTTER` | `BrowserMultiAppParam_Inputter` |  |  |  |
| 5 | `BROWSER.MULTI.DATE.TIME` | `BrowserMultiAppParam_DateTime` |  |  |  |
| 6 | `BROWSER.MULTI.AUTHORISER` | `BrowserMultiAppParam_Authoriser` | String |  |  |
| 7 | `BROWSER.MULTI.CO.CODE` | `BrowserMultiAppParam_CoCode` | String |  |  |
| 8 | `BROWSER.MULTI.DEPT.CODE` | `BrowserMultiAppParam_DeptCode` | String |  |  |
| 9 | `BROWSER.MULTI.AUDITOR.CODE` | `BrowserMultiAppParam_AuditorCode` | String |  |  |
| 10 | `BROWSER.MULTI.AUDIT.DATE.TIME` | `BrowserMultiAppParam_AuditDateTime` | String |  |  |
