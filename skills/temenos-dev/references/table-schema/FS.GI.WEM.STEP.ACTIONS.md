# FS.GI.WEM.STEP.ACTIONS — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.STEP.ACTIONS` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STEP.ACTIONS.FUND.GROUP` | `FsGiWemStepActions_FundGroup` | TField |  | Fund Group Multifonds DB Column is P_CGROUPE_COURS. |
| 2 | `STEP.ACTIONS.TRADE.DATE` | `FsGiWemStepActions_TradeDate` | TField |  | Trade Date Multifonds DB Column is P_DOPER. |
| 3 | `STEP.ACTIONS.ACCOUNTING.DATE` | `FsGiWemStepActions_AccountingDate` | TField |  | Accoutning Date Multifonds DB Column is P_DCTA. |
| 4 | `STEP.ACTIONS.STEP` | `FsGiWemStepActions_Step` | TField |  | Step Multifonds DB Column is P_PROCESS. |
| 5 | `STEP.ACTIONS.ACTION` | `FsGiWemStepActions_Action` | TField |  | Action Multifonds DB Column is P_ACTION. |
| 6 | `STEP.ACTIONS.RECORD.STATUS` | `FsGiWemStepActions_RecordStatus` | String |  |  |
| 7 | `STEP.ACTIONS.CURR.NO` | `FsGiWemStepActions_CurrNo` | String |  |  |
| 8 | `STEP.ACTIONS.INPUTTER` | `FsGiWemStepActions_Inputter` |  |  |  |
| 9 | `STEP.ACTIONS.DATE.TIME` | `FsGiWemStepActions_DateTime` |  |  |  |
| 10 | `STEP.ACTIONS.AUTHORISER` | `FsGiWemStepActions_Authoriser` | String |  |  |
| 11 | `STEP.ACTIONS.CO.CODE` | `FsGiWemStepActions_CoCode` | String |  |  |
| 12 | `STEP.ACTIONS.DEPT.CODE` | `FsGiWemStepActions_DeptCode` | String |  |  |
| 13 | `STEP.ACTIONS.AUDITOR.CODE` | `FsGiWemStepActions_AuditorCode` | String |  |  |
| 14 | `STEP.ACTIONS.AUDIT.DATE.TIME` | `FsGiWemStepActions_AuditDateTime` | String |  |  |
