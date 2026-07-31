# FS.GI.LP.DASHBOARD.PURGE.OVERRIDE — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.DASHBOARD.PURGE.OVERRIDE` in `FS_LimitedPartnershipProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.PARENT.REF.ID` | `FsGiLpDashboardPurgeOverride_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.ORA.ROWID` | `FsGiLpDashboardPurgeOverride_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.FUND.ID` | `FsGiLpDashboardPurgeOverride_FundId` | TField |  | Master fund ID. Multifonds DB Column is MULTIFONDS_ID. |
| 4 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.CLASS.CURRENCY` | `FsGiLpDashboardPurgeOverride_ClassCurrency` | TField |  | Fund Share Class Currency Multifonds DB Column is CLASS_CURRENCY. |
| 5 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.GL.INPUTS` | `FsGiLpDashboardPurgeOverride_GlInputs` | TField |  | Flag to select GL inputs for purge. Multifonds DB Column is FLG_GL_INPUTS. |
| 6 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.GL.OVERRIDE` | `FsGiLpDashboardPurgeOverride_GlOverride` | TField |  | Flag to select GL overrides for purge. Multifonds DB Column is FLG_GL_OVERRIDES. |
| 7 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.INCOME.ALLOCATION.OVERRIDE` | `FsGiLpDashboardPurgeOverride_IncomeAllocationOverride` | TField |  | Flag to select income allocation override for purge. Multifonds DB Column is FLG_INCOME_ALLOC_OVR. |
| 8 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.ASSET.BASED.FEE.OVERRIDE` | `FsGiLpDashboardPurgeOverride_AssetBasedFeeOverride` | TField |  | Flag to select Asset Based Fee Override for purge. Multifonds DB Column is FLG_ASSET_FEE_OVR. |
| 9 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.INCENTIVE.FEE.OVERRIDE` | `FsGiLpDashboardPurgeOverride_IncentiveFeeOverride` | TField |  | Flag to select incentive fee override for purge. Multifonds DB Column is FLG_INCENTIVE_FEE_OVR. |
| 10 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.ENDING.UNITS.OVERRIDE` | `FsGiLpDashboardPurgeOverride_EndingUnitsOverride` | TField |  | Flag to select units override for purge. Multifonds DB Column is FLG_ENDING_UNITS_OVR. |
| 11 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.ORDER.OVERRIDE` | `FsGiLpDashboardPurgeOverride_OrderOverride` | TField |  | Flag to select order override for purge. Multifonds DB Column is FLG_ORDER_OVR. |
| 12 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.ROR.OVERRIDE` | `FsGiLpDashboardPurgeOverride_RorOverride` | TField |  | Flag to select GL inputs for purge. Multifonds DB Column is FLG_ROR_OVR. |
| 13 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.BREAK.PERIOD.START.DATE` | `FsGiLpDashboardPurgeOverride_BreakPeriodStartDate` | TField |  | Break period start date. Multifonds DB Column is BP_START_DATE. |
| 14 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.BREAK.PERIOD.END.DATE` | `FsGiLpDashboardPurgeOverride_BreakPeriodEndDate` | TField |  | Break period end date. Multifonds DB Column is BP_END_DATE. |
| 15 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.TA.FUND.ID` | `FsGiLpDashboardPurgeOverride_TaFundId` | TField |  | TA Fund is an Internal ID with combination of Fund ID and Class Currency. Multifonds DB Column is NPTF. |
| 16 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RESERVED10` | `FsGiLpDashboardPurgeOverride_Reserved10` | TField |  |  |
| 17 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RESERVED9` | `FsGiLpDashboardPurgeOverride_Reserved9` | TField |  |  |
| 18 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RESERVED8` | `FsGiLpDashboardPurgeOverride_Reserved8` | TField |  |  |
| 19 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RESERVED7` | `FsGiLpDashboardPurgeOverride_Reserved7` | TField |  |  |
| 20 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RESERVED6` | `FsGiLpDashboardPurgeOverride_Reserved6` | TField |  |  |
| 21 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RESERVED5` | `FsGiLpDashboardPurgeOverride_Reserved5` | TField |  |  |
| 22 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RESERVED4` | `FsGiLpDashboardPurgeOverride_Reserved4` | TField |  |  |
| 23 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RESERVED3` | `FsGiLpDashboardPurgeOverride_Reserved3` | TField |  |  |
| 24 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RESERVED2` | `FsGiLpDashboardPurgeOverride_Reserved2` | TField |  |  |
| 25 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RESERVED1` | `FsGiLpDashboardPurgeOverride_Reserved1` | TField |  |  |
| 26 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.LOCAL.REF` | `FsGiLpDashboardPurgeOverride_LocalRef` |  |  |  |
| 27 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.OVERRIDE` | `FsGiLpDashboardPurgeOverride_Override` |  |  |  |
| 28 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.RECORD.STATUS` | `FsGiLpDashboardPurgeOverride_RecordStatus` | String |  |  |
| 29 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.CURR.NO` | `FsGiLpDashboardPurgeOverride_CurrNo` | String |  |  |
| 30 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.INPUTTER` | `FsGiLpDashboardPurgeOverride_Inputter` |  |  |  |
| 31 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.DATE.TIME` | `FsGiLpDashboardPurgeOverride_DateTime` |  |  |  |
| 32 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.AUTHORISER` | `FsGiLpDashboardPurgeOverride_Authoriser` | String |  |  |
| 33 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.CO.CODE` | `FsGiLpDashboardPurgeOverride_CoCode` | String |  |  |
| 34 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.DEPT.CODE` | `FsGiLpDashboardPurgeOverride_DeptCode` | String |  |  |
| 35 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.AUDITOR.CODE` | `FsGiLpDashboardPurgeOverride_AuditorCode` | String |  |  |
| 36 | `FS.GI.LP.DASHBOARD.PURGE.OVERRIDE.AUDIT.DATE.TIME` | `FsGiLpDashboardPurgeOverride_AuditDateTime` | String |  |  |
