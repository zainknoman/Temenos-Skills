# FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.PARENT.REF.ID` | `FsGiLpGlCustomAllocClassMast_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.ORA.ROWID` | `FsGiLpGlCustomAllocClassMast_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.TA.FUND.ID` | `FsGiLpGlCustomAllocClassMast_TaFundId` | TField |  | Fund Internal ID Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.SHARE.CLASS.CODE` | `FsGiLpGlCustomAllocClassMast_ShareClassCode` | TField |  | Fund share class code Multifonds DB Column is TPART. |
| 5 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.CUSTOM.INCOME.ALLOC.CLASS.ID` | `FsGiLpGlCustomAllocClassMast_CustomIncomeAllocClassId` | TField |  | To define unique custom income allocation class Id. Multifonds DB Column is IC_ALOC_CLASS_ID. |
| 6 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.CUSTOM.INCOME.ALLOC.CLASS.NAME` | `FsGiLpGlCustomAllocClassMast_CustomIncomeAllocClassName` | TField |  | To define unique custom income allocation class description Multifonds DB Column is CLASS_LIBELLE. |
| 7 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.FUND.ID` | `FsGiLpGlCustomAllocClassMast_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 8 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.CLASS.CURRENCY` | `FsGiLpGlCustomAllocClassMast_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 9 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RESERVED10` | `FsGiLpGlCustomAllocClassMast_Reserved10` | TField |  |  |
| 10 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RESERVED9` | `FsGiLpGlCustomAllocClassMast_Reserved9` | TField |  |  |
| 11 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RESERVED8` | `FsGiLpGlCustomAllocClassMast_Reserved8` | TField |  |  |
| 12 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RESERVED7` | `FsGiLpGlCustomAllocClassMast_Reserved7` | TField |  |  |
| 13 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RESERVED6` | `FsGiLpGlCustomAllocClassMast_Reserved6` | TField |  |  |
| 14 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RESERVED5` | `FsGiLpGlCustomAllocClassMast_Reserved5` | TField |  |  |
| 15 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RESERVED4` | `FsGiLpGlCustomAllocClassMast_Reserved4` | TField |  |  |
| 16 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RESERVED3` | `FsGiLpGlCustomAllocClassMast_Reserved3` | TField |  |  |
| 17 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RESERVED2` | `FsGiLpGlCustomAllocClassMast_Reserved2` | TField |  |  |
| 18 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RESERVED1` | `FsGiLpGlCustomAllocClassMast_Reserved1` | TField |  |  |
| 19 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.LOCAL.REF` | `FsGiLpGlCustomAllocClassMast_LocalRef` |  |  |  |
| 20 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.OVERRIDE` | `FsGiLpGlCustomAllocClassMast_Override` |  |  |  |
| 21 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.RECORD.STATUS` | `FsGiLpGlCustomAllocClassMast_RecordStatus` | String |  |  |
| 22 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.CURR.NO` | `FsGiLpGlCustomAllocClassMast_CurrNo` | String |  |  |
| 23 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.INPUTTER` | `FsGiLpGlCustomAllocClassMast_Inputter` |  |  |  |
| 24 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.DATE.TIME` | `FsGiLpGlCustomAllocClassMast_DateTime` |  |  |  |
| 25 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.AUTHORISER` | `FsGiLpGlCustomAllocClassMast_Authoriser` | String |  |  |
| 26 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.CO.CODE` | `FsGiLpGlCustomAllocClassMast_CoCode` | String |  |  |
| 27 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.DEPT.CODE` | `FsGiLpGlCustomAllocClassMast_DeptCode` | String |  |  |
| 28 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.AUDITOR.CODE` | `FsGiLpGlCustomAllocClassMast_AuditorCode` | String |  |  |
| 29 | `FS.GI.LP.GL.CUSTOM.ALLOC.CLASS.MAST.AUDIT.DATE.TIME` | `FsGiLpGlCustomAllocClassMast_AuditDateTime` | String |  |  |
