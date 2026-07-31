# FS.GI.PRIVATE.EQUITY.DASHBOARD — Table Schema

> Source: `INSERTS/I_F.FS.GI.PRIVATE.EQUITY.DASHBOARD` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.PRIVATE.EQUITY.DASH.PRIVATE.EQUITY.DASHBOARD` | `FsGiPrivateEquityDashboard_PrivateEquityDashboard` |  |  |  |
| 2 | `FS.GA.PRIVATE.EQUITY.DASH.RECORD.STATUS` | `FsGiPrivateEquityDashboard_RecordStatus` |  |  |  |
| 3 | `FS.GA.PRIVATE.EQUITY.DASH.CURR.NO` | `FsGiPrivateEquityDashboard_CurrNo` |  |  |  |
| 4 | `FS.GA.PRIVATE.EQUITY.DASH.INPUTTER` | `FsGiPrivateEquityDashboard_Inputter` |  |  |  |
| 5 | `FS.GA.PRIVATE.EQUITY.DASH.DATE.TIME` | `FsGiPrivateEquityDashboard_DateTime` |  |  |  |
| 6 | `FS.GA.PRIVATE.EQUITY.DASH.AUTHORISER` | `FsGiPrivateEquityDashboard_Authoriser` |  |  |  |
| 7 | `FS.GA.PRIVATE.EQUITY.DASH.CO.CODE` | `FsGiPrivateEquityDashboard_CoCode` |  |  |  |
| 8 | `FS.GA.PRIVATE.EQUITY.DASH.DEPT.CODE` | `FsGiPrivateEquityDashboard_DeptCode` |  |  |  |
| 9 | `FS.GA.PRIVATE.EQUITY.DASH.AUDITOR.CODE` | `FsGiPrivateEquityDashboard_AuditorCode` |  |  |  |
| 10 | `FS.GA.PRIVATE.EQUITY.DASH.AUDIT.DATE.TIME` | `FsGiPrivateEquityDashboard_AuditDateTime` |  |  |  |
