# FS.GI.LP.GL.UNEVENALLOCATION.DET.HT — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.UNEVENALLOCATION.DET.HT` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.FUND.ID` | `FsGiLpGlUnevenallocationDetHt_FundId` | TField |  | Fund Internal Id. Multifonds DB Column is NPTF. |
| 2 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.SHARE.CLASS.CODE` | `FsGiLpGlUnevenallocationDetHt_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 3 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.GL.CATEGORY.ID` | `FsGiLpGlUnevenallocationDetHt_GlCategoryId` | TField |  | GL category of GL account. Multifonds DB Column is CATEGORY_ID. |
| 4 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.INCOME.ALLOCATION.CLASS` | `FsGiLpGlUnevenallocationDetHt_IncomeAllocationClass` | TField |  | Allocation class ID for the uneven income allocation. Multifonds DB Column is CLASS_ID. |
| 5 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.BREAK.PERIOD.START.DATE` | `FsGiLpGlUnevenallocationDetHt_BreakPeriodStartDate` | TField |  | Uneven income allocation effective BP start date. Multifonds DB Column is BP_ST_DATE. |
| 6 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.BREAK.PERIOD.END.DATE` | `FsGiLpGlUnevenallocationDetHt_BreakPeriodEndDate` | TField |  | Uneven income allocation effective BP end date. Multifonds DB Column is BP_END_DATE. |
| 7 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.UNEVEN.ALLOCATION.METHOD` | `FsGiLpGlUnevenallocationDetHt_UnevenAllocationMethod` | TField |  | Uneven income allocation method. Multifonds DB Column is ALLOC_METHOD. |
| 8 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.REGISTER.ID` | `FsGiLpGlUnevenallocationDetHt_RegisterId` | TField |  | Register ID in case of uneven income allocation method is percentage. Multifonds DB Column is NREGISTER. |
| 9 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.CONTRACT.ID` | `FsGiLpGlUnevenallocationDetHt_ContractId` | TField |  | Tranche ID in case of uneven income allocation method is percentage. Multifonds DB Column is NCONTRACT. |
| 10 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.UNEVEN.ALLOCATION.PERCENTAGE` | `FsGiLpGlUnevenallocationDetHt_UnevenAllocationPercentage` | TField |  | Uneven income allocation percent. Multifonds DB Column is PCT_ALLOCATION. |
| 11 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.UNEVEN.ALLOCATION.AMOUNT` | `FsGiLpGlUnevenallocationDetHt_UnevenAllocationAmount` | TField |  | Uneven income allocation amount. Multifonds DB Column is AMT_ALLOCATION. |
| 12 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.UPDATE.DATE` | `FsGiLpGlUnevenallocationDetHt_UpdateDate` | TField |  | Uneven allocation details processed date. It used for historical enquiry purpose. Multifonds DB Column is DUPDATE. |
| 13 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RESERVED10` | `FsGiLpGlUnevenallocationDetHt_Reserved10` | TField |  |  |
| 14 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RESERVED9` | `FsGiLpGlUnevenallocationDetHt_Reserved9` | TField |  |  |
| 15 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RESERVED8` | `FsGiLpGlUnevenallocationDetHt_Reserved8` | TField |  |  |
| 16 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RESERVED7` | `FsGiLpGlUnevenallocationDetHt_Reserved7` | TField |  |  |
| 17 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RESERVED6` | `FsGiLpGlUnevenallocationDetHt_Reserved6` | TField |  |  |
| 18 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RESERVED5` | `FsGiLpGlUnevenallocationDetHt_Reserved5` | TField |  |  |
| 19 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RESERVED4` | `FsGiLpGlUnevenallocationDetHt_Reserved4` | TField |  |  |
| 20 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RESERVED3` | `FsGiLpGlUnevenallocationDetHt_Reserved3` | TField |  |  |
| 21 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RESERVED2` | `FsGiLpGlUnevenallocationDetHt_Reserved2` | TField |  |  |
| 22 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RESERVED1` | `FsGiLpGlUnevenallocationDetHt_Reserved1` | TField |  |  |
| 23 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.LOCAL.REF` | `FsGiLpGlUnevenallocationDetHt_LocalRef` |  |  |  |
| 24 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.OVERRIDE` | `FsGiLpGlUnevenallocationDetHt_Override` |  |  |  |
| 25 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.RECORD.STATUS` | `FsGiLpGlUnevenallocationDetHt_RecordStatus` | String |  |  |
| 26 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.CURR.NO` | `FsGiLpGlUnevenallocationDetHt_CurrNo` | String |  |  |
| 27 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.INPUTTER` | `FsGiLpGlUnevenallocationDetHt_Inputter` |  |  |  |
| 28 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.DATE.TIME` | `FsGiLpGlUnevenallocationDetHt_DateTime` |  |  |  |
| 29 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.AUTHORISER` | `FsGiLpGlUnevenallocationDetHt_Authoriser` | String |  |  |
| 30 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.CO.CODE` | `FsGiLpGlUnevenallocationDetHt_CoCode` | String |  |  |
| 31 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.DEPT.CODE` | `FsGiLpGlUnevenallocationDetHt_DeptCode` | String |  |  |
| 32 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.AUDITOR.CODE` | `FsGiLpGlUnevenallocationDetHt_AuditorCode` | String |  |  |
| 33 | `FS.GI.LP.GL.UNEVENALLOCATION.DET.HT.AUDIT.DATE.TIME` | `FsGiLpGlUnevenallocationDetHt_AuditDateTime` | String |  |  |
