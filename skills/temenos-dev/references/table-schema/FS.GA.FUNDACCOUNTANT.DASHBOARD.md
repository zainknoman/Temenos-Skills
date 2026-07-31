# FS.GA.FUNDACCOUNTANT.DASHBOARD — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUNDACCOUNTANT.DASHBOARD` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUNDACCOUNTANT.DASH.FUNDACCOUNTANT.DASHBOARD` | `FsGaFundaccountantDashboard_FundaccountantDashboard` |  |  |  |
| 2 | `FS.GA.FUNDACCOUNTANT.DASH.RECORD.STATUS` | `FsGaFundaccountantDashboard_RecordStatus` |  |  |  |
| 3 | `FS.GA.FUNDACCOUNTANT.DASH.CURR.NO` | `FsGaFundaccountantDashboard_CurrNo` |  |  |  |
| 4 | `FS.GA.FUNDACCOUNTANT.DASH.INPUTTER` | `FsGaFundaccountantDashboard_Inputter` |  |  |  |
| 5 | `FS.GA.FUNDACCOUNTANT.DASH.DATE.TIME` | `FsGaFundaccountantDashboard_DateTime` |  |  |  |
| 6 | `FS.GA.FUNDACCOUNTANT.DASH.AUTHORISER` | `FsGaFundaccountantDashboard_Authoriser` |  |  |  |
| 7 | `FS.GA.FUNDACCOUNTANT.DASH.CO.CODE` | `FsGaFundaccountantDashboard_CoCode` |  |  |  |
| 8 | `FS.GA.FUNDACCOUNTANT.DASH.DEPT.CODE` | `FsGaFundaccountantDashboard_DeptCode` |  |  |  |
| 9 | `FS.GA.FUNDACCOUNTANT.DASH.AUDITOR.CODE` | `FsGaFundaccountantDashboard_AuditorCode` |  |  |  |
| 10 | `FS.GA.FUNDACCOUNTANT.DASH.AUDIT.DATE.TIME` | `FsGaFundaccountantDashboard_AuditDateTime` |  |  |  |
