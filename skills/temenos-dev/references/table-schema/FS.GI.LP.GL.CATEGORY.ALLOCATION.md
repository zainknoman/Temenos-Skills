# FS.GI.LP.GL.CATEGORY.ALLOCATION — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.CATEGORY.ALLOCATION` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.PARENT.REF.ID` | `FsGiLpGlCategoryAllocation_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.ORA.ROWID` | `FsGiLpGlCategoryAllocation_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.TA.FUND.ID` | `FsGiLpGlCategoryAllocation_TaFundId` | TField |  | Fund Internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.SHARE.CLASS.CODE` | `FsGiLpGlCategoryAllocation_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 5 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.GL.CATEGORY.ID` | `FsGiLpGlCategoryAllocation_GlCategoryId` | TField |  | GL Internal code for GL External code. Multifonds DB Column is CATEGORY_ID. |
| 6 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.INCOME.ALLOCATION.CLASS` | `FsGiLpGlCategoryAllocation_IncomeAllocationClass` | TField |  | Income allocation criteria to partners based on GL category. Multifonds DB Column is CLASS_ID. |
| 7 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.UNEVEN.INCOME.ALLOCATION.FLAG` | `FsGiLpGlCategoryAllocation_UnevenIncomeAllocationFlag` | TField |  | Select the flag to define uneven income allocation. Multifonds DB Column is FLG_UNEVEN_ALLOC. |
| 8 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.OVERRIDE.FLAG` | `FsGiLpGlCategoryAllocation_OverrideFlag` | TField |  | Income allocation change is impacted the dash board process, flag updated to Y. Multifonds DB Column is FLG_OVERRIDE. |
| 9 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.FUND.ID` | `FsGiLpGlCategoryAllocation_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 10 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.CLASS.CURRENCY` | `FsGiLpGlCategoryAllocation_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 11 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.FLOW.TO.FEEDER.FLAG` | `FsGiLpGlCategoryAllocation_FlowToFeederFlag` | TField |  | Flag to control if a PL item should be carried in the feeder register PL interface to the feeder fund/class. Multifonds DB Column is FLG_FLOW_TO_FEEDER. |
| 12 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RESERVED10` | `FsGiLpGlCategoryAllocation_Reserved10` | TField |  |  |
| 13 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RESERVED9` | `FsGiLpGlCategoryAllocation_Reserved9` | TField |  |  |
| 14 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RESERVED8` | `FsGiLpGlCategoryAllocation_Reserved8` | TField |  |  |
| 15 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RESERVED7` | `FsGiLpGlCategoryAllocation_Reserved7` | TField |  |  |
| 16 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RESERVED6` | `FsGiLpGlCategoryAllocation_Reserved6` | TField |  |  |
| 17 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RESERVED5` | `FsGiLpGlCategoryAllocation_Reserved5` | TField |  |  |
| 18 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RESERVED4` | `FsGiLpGlCategoryAllocation_Reserved4` | TField |  |  |
| 19 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RESERVED3` | `FsGiLpGlCategoryAllocation_Reserved3` | TField |  |  |
| 20 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RESERVED2` | `FsGiLpGlCategoryAllocation_Reserved2` | TField |  |  |
| 21 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RESERVED1` | `FsGiLpGlCategoryAllocation_Reserved1` | TField |  |  |
| 22 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.LOCAL.REF` | `FsGiLpGlCategoryAllocation_LocalRef` |  |  |  |
| 23 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.OVERRIDE` | `FsGiLpGlCategoryAllocation_Override` |  |  |  |
| 24 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.RECORD.STATUS` | `FsGiLpGlCategoryAllocation_RecordStatus` | String |  |  |
| 25 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.CURR.NO` | `FsGiLpGlCategoryAllocation_CurrNo` | String |  |  |
| 26 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.INPUTTER` | `FsGiLpGlCategoryAllocation_Inputter` |  |  |  |
| 27 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.DATE.TIME` | `FsGiLpGlCategoryAllocation_DateTime` |  |  |  |
| 28 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.AUTHORISER` | `FsGiLpGlCategoryAllocation_Authoriser` | String |  |  |
| 29 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.CO.CODE` | `FsGiLpGlCategoryAllocation_CoCode` | String |  |  |
| 30 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.DEPT.CODE` | `FsGiLpGlCategoryAllocation_DeptCode` | String |  |  |
| 31 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.AUDITOR.CODE` | `FsGiLpGlCategoryAllocation_AuditorCode` | String |  |  |
| 32 | `FS.GI.LP.GL.CATEGORY.ALLOCATION.AUDIT.DATE.TIME` | `FsGiLpGlCategoryAllocation_AuditDateTime` | String |  |  |
