# FS.GI.LP.GL.CATEGORY.SETUP — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.CATEGORY.SETUP` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.CATEGORY.SETUP.PARENT.REF.ID` | `FsGiLpGlCategorySetup_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.GL.CATEGORY.SETUP.ORA.ROWID` | `FsGiLpGlCategorySetup_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.GL.CATEGORY.SETUP.TA.FUND.ID` | `FsGiLpGlCategorySetup_TaFundId` | TField |  | Fund Internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.GL.CATEGORY.SETUP.GL.CATEGORY.ID` | `FsGiLpGlCategorySetup_GlCategoryId` | TField |  | GL Internal code for GL External code. Multifonds DB Column is CATEGORY_ID. |
| 5 | `FS.GI.LP.GL.CATEGORY.SETUP.GL.REPORTING.CATEGORY` | `FsGiLpGlCategorySetup_GlReportingCategory` | TField |  | Reporting category used to group the GL accounts. Multifonds DB Column is REP_CATEGORY. |
| 6 | `FS.GI.LP.GL.CATEGORY.SETUP.GL.ACCOUNT.TYPE` | `FsGiLpGlCategorySetup_GlAccountType` | TField |  | Account type for GL category. For example Income,Expense,Gain or Loss. Multifonds DB Column is ACCOUNT_TYPE. |
| 7 | `FS.GI.LP.GL.CATEGORY.SETUP.GL.INCOME.DISTRIBUTION.FLAG` | `FsGiLpGlCategorySetup_GlIncomeDistributionFlag` | TField |  | To define GL category is part of income distribution or not. Multifonds DB Column is FLG_INCOME_DIST. |
| 8 | `FS.GI.LP.GL.CATEGORY.SETUP.GL.INCOME.DIRECTION` | `FsGiLpGlCategorySetup_GlIncomeDirection` | TField |  | To define the direction for GL category to calculate income allocation. For example Income = + , Expense= - . Multifonds DB Column is EXPECTED_DIRECTION. |
| 9 | `FS.GI.LP.GL.CATEGORY.SETUP.CHANGED.FLAG` | `FsGiLpGlCategorySetup_ChangedFlag` | TField |  | GL category structure change is impacted the dash board process, Flag updated to Y. Multifonds DB Column is FLG_CHANGED. |
| 10 | `FS.GI.LP.GL.CATEGORY.SETUP.FUND.ID` | `FsGiLpGlCategorySetup_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 11 | `FS.GI.LP.GL.CATEGORY.SETUP.CLASS.CURRENCY` | `FsGiLpGlCategorySetup_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 12 | `FS.GI.LP.GL.CATEGORY.SETUP.RESERVED10` | `FsGiLpGlCategorySetup_Reserved10` | TField |  |  |
| 13 | `FS.GI.LP.GL.CATEGORY.SETUP.RESERVED9` | `FsGiLpGlCategorySetup_Reserved9` | TField |  |  |
| 14 | `FS.GI.LP.GL.CATEGORY.SETUP.RESERVED8` | `FsGiLpGlCategorySetup_Reserved8` | TField |  |  |
| 15 | `FS.GI.LP.GL.CATEGORY.SETUP.RESERVED7` | `FsGiLpGlCategorySetup_Reserved7` | TField |  |  |
| 16 | `FS.GI.LP.GL.CATEGORY.SETUP.RESERVED6` | `FsGiLpGlCategorySetup_Reserved6` | TField |  |  |
| 17 | `FS.GI.LP.GL.CATEGORY.SETUP.RESERVED5` | `FsGiLpGlCategorySetup_Reserved5` | TField |  |  |
| 18 | `FS.GI.LP.GL.CATEGORY.SETUP.RESERVED4` | `FsGiLpGlCategorySetup_Reserved4` | TField |  |  |
| 19 | `FS.GI.LP.GL.CATEGORY.SETUP.RESERVED3` | `FsGiLpGlCategorySetup_Reserved3` | TField |  |  |
| 20 | `FS.GI.LP.GL.CATEGORY.SETUP.RESERVED2` | `FsGiLpGlCategorySetup_Reserved2` | TField |  |  |
| 21 | `FS.GI.LP.GL.CATEGORY.SETUP.RESERVED1` | `FsGiLpGlCategorySetup_Reserved1` | TField |  |  |
| 22 | `FS.GI.LP.GL.CATEGORY.SETUP.LOCAL.REF` | `FsGiLpGlCategorySetup_LocalRef` |  |  |  |
| 23 | `FS.GI.LP.GL.CATEGORY.SETUP.OVERRIDE` | `FsGiLpGlCategorySetup_Override` |  |  |  |
| 24 | `FS.GI.LP.GL.CATEGORY.SETUP.RECORD.STATUS` | `FsGiLpGlCategorySetup_RecordStatus` | String |  |  |
| 25 | `FS.GI.LP.GL.CATEGORY.SETUP.CURR.NO` | `FsGiLpGlCategorySetup_CurrNo` | String |  |  |
| 26 | `FS.GI.LP.GL.CATEGORY.SETUP.INPUTTER` | `FsGiLpGlCategorySetup_Inputter` |  |  |  |
| 27 | `FS.GI.LP.GL.CATEGORY.SETUP.DATE.TIME` | `FsGiLpGlCategorySetup_DateTime` |  |  |  |
| 28 | `FS.GI.LP.GL.CATEGORY.SETUP.AUTHORISER` | `FsGiLpGlCategorySetup_Authoriser` | String |  |  |
| 29 | `FS.GI.LP.GL.CATEGORY.SETUP.CO.CODE` | `FsGiLpGlCategorySetup_CoCode` | String |  |  |
| 30 | `FS.GI.LP.GL.CATEGORY.SETUP.DEPT.CODE` | `FsGiLpGlCategorySetup_DeptCode` | String |  |  |
| 31 | `FS.GI.LP.GL.CATEGORY.SETUP.AUDITOR.CODE` | `FsGiLpGlCategorySetup_AuditorCode` | String |  |  |
| 32 | `FS.GI.LP.GL.CATEGORY.SETUP.AUDIT.DATE.TIME` | `FsGiLpGlCategorySetup_AuditDateTime` | String |  |  |
