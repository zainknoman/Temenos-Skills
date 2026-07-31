# FS.GI.LP.GL.UNEVENALLOCATION.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.UNEVENALLOCATION.DETAIL` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.PARENT.REF.ID` | `FsGiLpGlUnevenallocationDetail_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.ORA.ROWID` | `FsGiLpGlUnevenallocationDetail_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.TA.FUND.ID` | `FsGiLpGlUnevenallocationDetail_TaFundId` | TField |  | Fund Internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.SHARE.CLASS.CODE` | `FsGiLpGlUnevenallocationDetail_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 5 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.GL.CATEGORY.ID` | `FsGiLpGlUnevenallocationDetail_GlCategoryId` | TField |  | GL Internal code for GL External code. Multifonds DB Column is CATEGORY_ID. |
| 6 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.INCOME.ALLOCATION.CLASS` | `FsGiLpGlUnevenallocationDetail_IncomeAllocationClass` | TField |  | Allocation class ID for the uneven income allocation. Multifonds DB Column is CLASS_ID. |
| 7 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.BREAK.PERIOD.START.DATE` | `FsGiLpGlUnevenallocationDetail_BreakPeriodStartDate` | TField |  | Uneven income allocation effective BP start date. Multifonds DB Column is BP_ST_DATE. |
| 8 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.BREAK.PERIOD.END.DATE` | `FsGiLpGlUnevenallocationDetail_BreakPeriodEndDate` | TField |  | Uneven income allocation effective BP end date. Multifonds DB Column is BP_END_DATE. |
| 9 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.UNEVEN.ALLOCATION.METHOD` | `FsGiLpGlUnevenallocationDetail_UnevenAllocationMethod` | TField |  | Uneven income allocation method. Multifonds DB Column is ALLOC_METHOD. |
| 10 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.REGISTER.ID` | `FsGiLpGlUnevenallocationDetail_RegisterId` | TField |  | Register ID in case of uneven income allocation method is percentage. Multifonds DB Column is NREGISTER. |
| 11 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.CONTRACT.ID` | `FsGiLpGlUnevenallocationDetail_ContractId` | TField |  | Tranche ID in case of uneven income allocation method is percentage. Multifonds DB Column is NCONTRACT. |
| 12 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.UNEVEN.ALLOCATION.PERCENTAGE` | `FsGiLpGlUnevenallocationDetail_UnevenAllocationPercentage` | TField |  | Uneven income allocation percent. Multifonds DB Column is PCT_ALLOCATION. |
| 13 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.UNEVEN.ALLOCATION.AMOUNT` | `FsGiLpGlUnevenallocationDetail_UnevenAllocationAmount` | TField |  | Uneven income allocation amount. Multifonds DB Column is AMT_ALLOCATION. |
| 14 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.PERSON.TYPE` | `FsGiLpGlUnevenallocationDetail_PersonType` | TField |  | Person type of the Partner. Multifonds DB Column is TYPE_PERSON. |
| 15 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.FUND.ID` | `FsGiLpGlUnevenallocationDetail_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 16 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.CLASS.CURRENCY` | `FsGiLpGlUnevenallocationDetail_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 17 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RESERVED10` | `FsGiLpGlUnevenallocationDetail_Reserved10` | TField |  |  |
| 18 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RESERVED9` | `FsGiLpGlUnevenallocationDetail_Reserved9` | TField |  |  |
| 19 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RESERVED8` | `FsGiLpGlUnevenallocationDetail_Reserved8` | TField |  |  |
| 20 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RESERVED7` | `FsGiLpGlUnevenallocationDetail_Reserved7` | TField |  |  |
| 21 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RESERVED6` | `FsGiLpGlUnevenallocationDetail_Reserved6` | TField |  |  |
| 22 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RESERVED5` | `FsGiLpGlUnevenallocationDetail_Reserved5` | TField |  |  |
| 23 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RESERVED4` | `FsGiLpGlUnevenallocationDetail_Reserved4` | TField |  |  |
| 24 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RESERVED3` | `FsGiLpGlUnevenallocationDetail_Reserved3` | TField |  |  |
| 25 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RESERVED2` | `FsGiLpGlUnevenallocationDetail_Reserved2` | TField |  |  |
| 26 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RESERVED1` | `FsGiLpGlUnevenallocationDetail_Reserved1` | TField |  |  |
| 27 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.LOCAL.REF` | `FsGiLpGlUnevenallocationDetail_LocalRef` |  |  |  |
| 28 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.OVERRIDE` | `FsGiLpGlUnevenallocationDetail_Override` |  |  |  |
| 29 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.RECORD.STATUS` | `FsGiLpGlUnevenallocationDetail_RecordStatus` | String |  |  |
| 30 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.CURR.NO` | `FsGiLpGlUnevenallocationDetail_CurrNo` | String |  |  |
| 31 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.INPUTTER` | `FsGiLpGlUnevenallocationDetail_Inputter` |  |  |  |
| 32 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.DATE.TIME` | `FsGiLpGlUnevenallocationDetail_DateTime` |  |  |  |
| 33 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.AUTHORISER` | `FsGiLpGlUnevenallocationDetail_Authoriser` | String |  |  |
| 34 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.CO.CODE` | `FsGiLpGlUnevenallocationDetail_CoCode` | String |  |  |
| 35 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.DEPT.CODE` | `FsGiLpGlUnevenallocationDetail_DeptCode` | String |  |  |
| 36 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.AUDITOR.CODE` | `FsGiLpGlUnevenallocationDetail_AuditorCode` | String |  |  |
| 37 | `FS.GI.LP.GL.UNEVENALLOCATION.DETAIL.AUDIT.DATE.TIME` | `FsGiLpGlUnevenallocationDetail_AuditDateTime` | String |  |  |
