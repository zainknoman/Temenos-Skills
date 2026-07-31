# FS.GI.REG.DASHBOARD — Table Schema

> Source: `INSERTS/I_F.FS.GI.REG.DASHBOARD` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.REG.DASH.REGISTRATION.DASHBOARD` | `FsGiRegDashboard_RegistrationDashboard` |  |  |  |
| 2 | `FS.GI.REG.DASH.RECORD.STATUS` | `FsGiRegDashboard_RecordStatus` |  |  |  |
| 3 | `FS.GI.REG.DASH.CURR.NO` | `FsGiRegDashboard_CurrNo` |  |  |  |
| 4 | `FS.GI.REG.DASH.INPUTTER` | `FsGiRegDashboard_Inputter` |  |  |  |
| 5 | `FS.GI.REG.DASH.DATE.TIME` | `FsGiRegDashboard_DateTime` |  |  |  |
| 6 | `FS.GI.REG.DASH.AUTHORISER` | `FsGiRegDashboard_Authoriser` |  |  |  |
| 7 | `FS.GI.REG.DASH.CO.CODE` | `FsGiRegDashboard_CoCode` |  |  |  |
| 8 | `FS.GI.REG.DASH.DEPT.CODE` | `FsGiRegDashboard_DeptCode` |  |  |  |
| 9 | `FS.GI.REG.DASH.AUDITOR.CODE` | `FsGiRegDashboard_AuditorCode` |  |  |  |
| 10 | `FS.GI.REG.DASH.AUDIT.DATE.TIME` | `FsGiRegDashboard_AuditDateTime` |  |  |  |
