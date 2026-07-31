# FS.GI.TRANSACTION.DASHBOARD — Table Schema

> Source: `INSERTS/I_F.FS.GI.TRANSACTION.DASHBOARD` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TRANSACTION.DASH.TRANSACTION.DASHBOARD` | `FsGiTransactionDashboard_TransactionDashboard` |  |  |  |
| 2 | `FS.GI.TRANSACTION.DASH.RECORD.STATUS` | `FsGiTransactionDashboard_RecordStatus` |  |  |  |
| 3 | `FS.GI.TRANSACTION.DASH.CURR.NO` | `FsGiTransactionDashboard_CurrNo` |  |  |  |
| 4 | `FS.GI.TRANSACTION.DASH.INPUTTER` | `FsGiTransactionDashboard_Inputter` |  |  |  |
| 5 | `FS.GI.TRANSACTION.DASH.DATE.TIME` | `FsGiTransactionDashboard_DateTime` |  |  |  |
| 6 | `FS.GI.TRANSACTION.DASH.AUTHORISER` | `FsGiTransactionDashboard_Authoriser` |  |  |  |
| 7 | `FS.GI.TRANSACTION.DASH.CO.CODE` | `FsGiTransactionDashboard_CoCode` |  |  |  |
| 8 | `FS.GI.TRANSACTION.DASH.DEPT.CODE` | `FsGiTransactionDashboard_DeptCode` |  |  |  |
| 9 | `FS.GI.TRANSACTION.DASH.AUDITOR.CODE` | `FsGiTransactionDashboard_AuditorCode` |  |  |  |
| 10 | `FS.GI.TRANSACTION.DASH.AUDIT.DATE.TIME` | `FsGiTransactionDashboard_AuditDateTime` |  |  |  |
