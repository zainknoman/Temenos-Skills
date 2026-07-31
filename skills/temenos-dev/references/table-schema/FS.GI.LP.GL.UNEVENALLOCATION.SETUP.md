# FS.GI.LP.GL.UNEVENALLOCATION.SETUP — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.UNEVENALLOCATION.SETUP` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.PARENT.REF.ID` | `FsGiLpGlUnevenallocationSetup_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.ORA.ROWID` | `FsGiLpGlUnevenallocationSetup_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.TA.FUND.ID` | `FsGiLpGlUnevenallocationSetup_TaFundId` | TField |  | Fund Internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.SHARE.CLASS.CODE` | `FsGiLpGlUnevenallocationSetup_ShareClassCode` | TField |  | Fund share class code Multifonds DB Column is TPART. |
| 5 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.INCOME.ALLOCATION.CLASS` | `FsGiLpGlUnevenallocationSetup_IncomeAllocationClass` | TField |  | Allocation class ID for the uneven income allocation Multifonds DB Column is CLASS_ID. |
| 6 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.GL.CATEGORY.ID` | `FsGiLpGlUnevenallocationSetup_GlCategoryId` | TField |  | GL Internal code for GL External code. Multifonds DB Column is CATEGORY_ID. |
| 7 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.BREAK.PERIOD.START.DATE` | `FsGiLpGlUnevenallocationSetup_BreakPeriodStartDate` | TField |  | Uneven income allocation effective BP start date Multifonds DB Column is BP_ST_DATE. |
| 8 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.BREAK.PERIOD.END.DATE` | `FsGiLpGlUnevenallocationSetup_BreakPeriodEndDate` | TField |  | Uneven income allocation effective BP end date Multifonds DB Column is BP_END_DATE. |
| 9 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.UNEVEN.ALLOCATION.METHOD` | `FsGiLpGlUnevenallocationSetup_UnevenAllocationMethod` | TField |  | Uneven income allocation method Multifonds DB Column is ALLOC_METHOD. |
| 10 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.PROCESSED.FLAG` | `FsGiLpGlUnevenallocationSetup_ProcessedFlag` | TField |  | Uneven allocation change is impacted the dash board process, flag updated to N, upon dash board re-process flag updated to Y Multifonds DB Column is FLG_PROCESSED. |
| 11 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.FUND.ID` | `FsGiLpGlUnevenallocationSetup_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 12 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.CLASS.CURRENCY` | `FsGiLpGlUnevenallocationSetup_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 13 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RESERVED10` | `FsGiLpGlUnevenallocationSetup_Reserved10` | TField |  |  |
| 14 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RESERVED9` | `FsGiLpGlUnevenallocationSetup_Reserved9` | TField |  |  |
| 15 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RESERVED8` | `FsGiLpGlUnevenallocationSetup_Reserved8` | TField |  |  |
| 16 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RESERVED7` | `FsGiLpGlUnevenallocationSetup_Reserved7` | TField |  |  |
| 17 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RESERVED6` | `FsGiLpGlUnevenallocationSetup_Reserved6` | TField |  |  |
| 18 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RESERVED5` | `FsGiLpGlUnevenallocationSetup_Reserved5` | TField |  |  |
| 19 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RESERVED4` | `FsGiLpGlUnevenallocationSetup_Reserved4` | TField |  |  |
| 20 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RESERVED3` | `FsGiLpGlUnevenallocationSetup_Reserved3` | TField |  |  |
| 21 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RESERVED2` | `FsGiLpGlUnevenallocationSetup_Reserved2` | TField |  |  |
| 22 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RESERVED1` | `FsGiLpGlUnevenallocationSetup_Reserved1` | TField |  |  |
| 23 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.LOCAL.REF` | `FsGiLpGlUnevenallocationSetup_LocalRef` |  |  |  |
| 24 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.OVERRIDE` | `FsGiLpGlUnevenallocationSetup_Override` |  |  |  |
| 25 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.RECORD.STATUS` | `FsGiLpGlUnevenallocationSetup_RecordStatus` | String |  |  |
| 26 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.CURR.NO` | `FsGiLpGlUnevenallocationSetup_CurrNo` | String |  |  |
| 27 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.INPUTTER` | `FsGiLpGlUnevenallocationSetup_Inputter` |  |  |  |
| 28 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.DATE.TIME` | `FsGiLpGlUnevenallocationSetup_DateTime` |  |  |  |
| 29 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.AUTHORISER` | `FsGiLpGlUnevenallocationSetup_Authoriser` | String |  |  |
| 30 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.CO.CODE` | `FsGiLpGlUnevenallocationSetup_CoCode` | String |  |  |
| 31 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.DEPT.CODE` | `FsGiLpGlUnevenallocationSetup_DeptCode` | String |  |  |
| 32 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.AUDITOR.CODE` | `FsGiLpGlUnevenallocationSetup_AuditorCode` | String |  |  |
| 33 | `FS.GI.LP.GL.UNEVENALLOCATION.SETUP.AUDIT.DATE.TIME` | `FsGiLpGlUnevenallocationSetup_AuditDateTime` | String |  |  |
