# FS.GI.LP.DASHBOARD.ROLLBACK — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.DASHBOARD.ROLLBACK` in `FS_LimitedPartnershipProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.DASHBOARD.ROLLBACK.PARENT.REF.ID` | `FsGiLpDashboardRollback_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.DASHBOARD.ROLLBACK.ORA.ROWID` | `FsGiLpDashboardRollback_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.DASHBOARD.ROLLBACK.TA.FUND.ID` | `FsGiLpDashboardRollback_TaFundId` | TField |  | Fund Internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.DASHBOARD.ROLLBACK.BREAK.PERIOD.START.DATE` | `FsGiLpDashboardRollback_BreakPeriodStartDate` | TField |  | Break period start date for limited partnership dashboard processing. Multifonds DB Column is BP_START_DATE. |
| 5 | `FS.GI.LP.DASHBOARD.ROLLBACK.BREAK.PERIOD.END.DATE` | `FsGiLpDashboardRollback_BreakPeriodEndDate` | TField |  | Break period end date for limited partnership dashboard processing. Multifonds DB Column is BP_END_DATE. |
| 6 | `FS.GI.LP.DASHBOARD.ROLLBACK.BREAK.PERIOD.STATUS` | `FsGiLpDashboardRollback_BreakPeriodStatus` | TField |  | Break period dashboard status. In this version, it displays the status of each processed break periods. Automatically populated on accessing the screen. Multifonds DB Column is BP_STATUS. |
| 7 | `FS.GI.LP.DASHBOARD.ROLLBACK.ROLLBACK.FLAG` | `FsGiLpDashboardRollback_RollbackFlag` | TField |  | flag to select the corresponding break period of the partnership fund to which the system will initiate rollback process . Multifonds DB Column is FLG_ROLLBACK. |
| 8 | `FS.GI.LP.DASHBOARD.ROLLBACK.ROLLBACK.OPTION` | `FsGiLpDashboardRollback_RollbackOption` | TField |  | Rollback to prior break periods from the current break period processing . The available options are &apos;0001-Roll back to BP End- Rolls back the break period selected to status &apos;70-Closing order batched&apos; and &apos;0002-Roll back to BP Start- Rolls back the break period selected to status 10-New break period created. Multifonds DB Column is CTYPE_ROLLBACK. |
| 9 | `FS.GI.LP.DASHBOARD.ROLLBACK.ROLLBACK.COMMENTS` | `FsGiLpDashboardRollback_RollbackComments` | TField |  | Free text field that allows upto 400 alpha numerical characters for generic comments Multifonds DB Column is COMMENTS. |
| 10 | `FS.GI.LP.DASHBOARD.ROLLBACK.FUND.ID` | `FsGiLpDashboardRollback_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 11 | `FS.GI.LP.DASHBOARD.ROLLBACK.CLASS.CURRENCY` | `FsGiLpDashboardRollback_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 12 | `FS.GI.LP.DASHBOARD.ROLLBACK.RESERVED10` | `FsGiLpDashboardRollback_Reserved10` | TField |  |  |
| 13 | `FS.GI.LP.DASHBOARD.ROLLBACK.RESERVED9` | `FsGiLpDashboardRollback_Reserved9` | TField |  |  |
| 14 | `FS.GI.LP.DASHBOARD.ROLLBACK.RESERVED8` | `FsGiLpDashboardRollback_Reserved8` | TField |  |  |
| 15 | `FS.GI.LP.DASHBOARD.ROLLBACK.RESERVED7` | `FsGiLpDashboardRollback_Reserved7` | TField |  |  |
| 16 | `FS.GI.LP.DASHBOARD.ROLLBACK.RESERVED6` | `FsGiLpDashboardRollback_Reserved6` | TField |  |  |
| 17 | `FS.GI.LP.DASHBOARD.ROLLBACK.RESERVED5` | `FsGiLpDashboardRollback_Reserved5` | TField |  |  |
| 18 | `FS.GI.LP.DASHBOARD.ROLLBACK.RESERVED4` | `FsGiLpDashboardRollback_Reserved4` | TField |  |  |
| 19 | `FS.GI.LP.DASHBOARD.ROLLBACK.RESERVED3` | `FsGiLpDashboardRollback_Reserved3` | TField |  |  |
| 20 | `FS.GI.LP.DASHBOARD.ROLLBACK.RESERVED2` | `FsGiLpDashboardRollback_Reserved2` | TField |  |  |
| 21 | `FS.GI.LP.DASHBOARD.ROLLBACK.RESERVED1` | `FsGiLpDashboardRollback_Reserved1` | TField |  |  |
| 22 | `FS.GI.LP.DASHBOARD.ROLLBACK.LOCAL.REF` | `FsGiLpDashboardRollback_LocalRef` |  |  |  |
| 23 | `FS.GI.LP.DASHBOARD.ROLLBACK.OVERRIDE` | `FsGiLpDashboardRollback_Override` |  |  |  |
| 24 | `FS.GI.LP.DASHBOARD.ROLLBACK.RECORD.STATUS` | `FsGiLpDashboardRollback_RecordStatus` | String |  |  |
| 25 | `FS.GI.LP.DASHBOARD.ROLLBACK.CURR.NO` | `FsGiLpDashboardRollback_CurrNo` | String |  |  |
| 26 | `FS.GI.LP.DASHBOARD.ROLLBACK.INPUTTER` | `FsGiLpDashboardRollback_Inputter` |  |  |  |
| 27 | `FS.GI.LP.DASHBOARD.ROLLBACK.DATE.TIME` | `FsGiLpDashboardRollback_DateTime` |  |  |  |
| 28 | `FS.GI.LP.DASHBOARD.ROLLBACK.AUTHORISER` | `FsGiLpDashboardRollback_Authoriser` | String |  |  |
| 29 | `FS.GI.LP.DASHBOARD.ROLLBACK.CO.CODE` | `FsGiLpDashboardRollback_CoCode` | String |  |  |
| 30 | `FS.GI.LP.DASHBOARD.ROLLBACK.DEPT.CODE` | `FsGiLpDashboardRollback_DeptCode` | String |  |  |
| 31 | `FS.GI.LP.DASHBOARD.ROLLBACK.AUDITOR.CODE` | `FsGiLpDashboardRollback_AuditorCode` | String |  |  |
| 32 | `FS.GI.LP.DASHBOARD.ROLLBACK.AUDIT.DATE.TIME` | `FsGiLpDashboardRollback_AuditDateTime` | String |  |  |
