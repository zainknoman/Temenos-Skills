# FS.GA.FUNDVIEW.DASHBOARD — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUNDVIEW.DASHBOARD` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUNDVIEW.DASH.FUNDVIEW.DASHBOARD` | `FsGaFundviewDashboard_FundviewDashboard` |  |  |  |
| 2 | `FS.GA.FUNDVIEW.DASH.RECORD.STATUS` | `FsGaFundviewDashboard_RecordStatus` |  |  |  |
| 3 | `FS.GA.FUNDVIEW.DASH.CURR.NO` | `FsGaFundviewDashboard_CurrNo` |  |  |  |
| 4 | `FS.GA.FUNDVIEW.DASH.INPUTTER` | `FsGaFundviewDashboard_Inputter` |  |  |  |
| 5 | `FS.GA.FUNDVIEW.DASH.DATE.TIME` | `FsGaFundviewDashboard_DateTime` |  |  |  |
| 6 | `FS.GA.FUNDVIEW.DASH.AUTHORISER` | `FsGaFundviewDashboard_Authoriser` |  |  |  |
| 7 | `FS.GA.FUNDVIEW.DASH.CO.CODE` | `FsGaFundviewDashboard_CoCode` |  |  |  |
| 8 | `FS.GA.FUNDVIEW.DASH.DEPT.CODE` | `FsGaFundviewDashboard_DeptCode` |  |  |  |
| 9 | `FS.GA.FUNDVIEW.DASH.AUDITOR.CODE` | `FsGaFundviewDashboard_AuditorCode` |  |  |  |
| 10 | `FS.GA.FUNDVIEW.DASH.AUDIT.DATE.TIME` | `FsGaFundviewDashboard_AuditDateTime` |  |  |  |
