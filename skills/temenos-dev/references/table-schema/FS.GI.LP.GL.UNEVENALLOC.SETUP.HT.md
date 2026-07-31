# FS.GI.LP.GL.UNEVENALLOC.SETUP.HT — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.UNEVENALLOC.SETUP.HT` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.FUND.ID` | `FsGiLpGlUnevenallocSetupHt_FundId` | TField |  | Fund Internal Id. Multifonds DB Column is NPTF. |
| 2 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.SHARE.CLASS.CODE` | `FsGiLpGlUnevenallocSetupHt_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 3 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.GL.CATEGORY.ID` | `FsGiLpGlUnevenallocSetupHt_GlCategoryId` | TField |  | GL category of GL account. Multifonds DB Column is CATEGORY_ID. |
| 4 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.INCOME.ALLOCATION.CLASS` | `FsGiLpGlUnevenallocSetupHt_IncomeAllocationClass` | TField |  | Allocation class ID for the uneven income allocation. Multifonds DB Column is CLASS_ID. |
| 5 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.BREAK.PERIOD.START.DATE` | `FsGiLpGlUnevenallocSetupHt_BreakPeriodStartDate` | TField |  | Uneven income allocation effective BP start date. Multifonds DB Column is BP_ST_DATE. |
| 6 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.BREAK.PERIOD.END.DATE` | `FsGiLpGlUnevenallocSetupHt_BreakPeriodEndDate` | TField |  | Uneven income allocation effective BP end date. Multifonds DB Column is BP_END_DATE. |
| 7 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.UNEVEN.ALLOCATION.METHOD` | `FsGiLpGlUnevenallocSetupHt_UnevenAllocationMethod` | TField |  | Uneven income allocation method. Multifonds DB Column is ALLOC_METHOD. |
| 8 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.UPDATE.DATE` | `FsGiLpGlUnevenallocSetupHt_UpdateDate` | TField |  | Uneven allocation setup processed date. It used for Historical enquiry purpose. Multifonds DB Column is DUPDATE. |
| 9 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RESERVED10` | `FsGiLpGlUnevenallocSetupHt_Reserved10` | TField |  |  |
| 10 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RESERVED9` | `FsGiLpGlUnevenallocSetupHt_Reserved9` | TField |  |  |
| 11 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RESERVED8` | `FsGiLpGlUnevenallocSetupHt_Reserved8` | TField |  |  |
| 12 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RESERVED7` | `FsGiLpGlUnevenallocSetupHt_Reserved7` | TField |  |  |
| 13 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RESERVED6` | `FsGiLpGlUnevenallocSetupHt_Reserved6` | TField |  |  |
| 14 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RESERVED5` | `FsGiLpGlUnevenallocSetupHt_Reserved5` | TField |  |  |
| 15 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RESERVED4` | `FsGiLpGlUnevenallocSetupHt_Reserved4` | TField |  |  |
| 16 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RESERVED3` | `FsGiLpGlUnevenallocSetupHt_Reserved3` | TField |  |  |
| 17 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RESERVED2` | `FsGiLpGlUnevenallocSetupHt_Reserved2` | TField |  |  |
| 18 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RESERVED1` | `FsGiLpGlUnevenallocSetupHt_Reserved1` | TField |  |  |
| 19 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.LOCAL.REF` | `FsGiLpGlUnevenallocSetupHt_LocalRef` |  |  |  |
| 20 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.OVERRIDE` | `FsGiLpGlUnevenallocSetupHt_Override` |  |  |  |
| 21 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.RECORD.STATUS` | `FsGiLpGlUnevenallocSetupHt_RecordStatus` | String |  |  |
| 22 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.CURR.NO` | `FsGiLpGlUnevenallocSetupHt_CurrNo` | String |  |  |
| 23 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.INPUTTER` | `FsGiLpGlUnevenallocSetupHt_Inputter` |  |  |  |
| 24 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.DATE.TIME` | `FsGiLpGlUnevenallocSetupHt_DateTime` |  |  |  |
| 25 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.AUTHORISER` | `FsGiLpGlUnevenallocSetupHt_Authoriser` | String |  |  |
| 26 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.CO.CODE` | `FsGiLpGlUnevenallocSetupHt_CoCode` | String |  |  |
| 27 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.DEPT.CODE` | `FsGiLpGlUnevenallocSetupHt_DeptCode` | String |  |  |
| 28 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.AUDITOR.CODE` | `FsGiLpGlUnevenallocSetupHt_AuditorCode` | String |  |  |
| 29 | `FS.GI.LP.GL.UNEVENALLOC.SETUP.HT.AUDIT.DATE.TIME` | `FsGiLpGlUnevenallocSetupHt_AuditDateTime` | String |  |  |
