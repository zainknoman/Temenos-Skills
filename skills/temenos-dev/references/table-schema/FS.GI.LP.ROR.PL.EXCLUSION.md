# FS.GI.LP.ROR.PL.EXCLUSION — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.ROR.PL.EXCLUSION` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.ROR.PL.EXCLUSION.PARENT.REF.ID` | `FsGiLpRorPlExclusion_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.ROR.PL.EXCLUSION.ORA.ROWID` | `FsGiLpRorPlExclusion_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.ROR.PL.EXCLUSION.TA.FUND.ID` | `FsGiLpRorPlExclusion_TaFundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.ROR.PL.EXCLUSION.ROR.CALC.BASIS` | `FsGiLpRorPlExclusion_RorCalcBasis` | TField |  | ROR calculation basis. Multifonds DB Column is ROR_CALC_BASIS. |
| 5 | `FS.GI.LP.ROR.PL.EXCLUSION.GL.CATEGORY.ID` | `FsGiLpRorPlExclusion_GlCategoryId` | TField |  | GL internal code for GL external code. Multifonds DB Column is GL_EXCL. |
| 6 | `FS.GI.LP.ROR.PL.EXCLUSION.GL.CATEGORY.ID.DESC` | `FsGiLpRorPlExclusion_GlCategoryIdDesc` | TField |  | GL Internal code description. Multifonds DB Column is LIBELLE. |
| 7 | `FS.GI.LP.ROR.PL.EXCLUSION.FUND.ID` | `FsGiLpRorPlExclusion_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 8 | `FS.GI.LP.ROR.PL.EXCLUSION.CLASS.CURRENCY` | `FsGiLpRorPlExclusion_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 9 | `FS.GI.LP.ROR.PL.EXCLUSION.RESERVED10` | `FsGiLpRorPlExclusion_Reserved10` | TField |  |  |
| 10 | `FS.GI.LP.ROR.PL.EXCLUSION.RESERVED9` | `FsGiLpRorPlExclusion_Reserved9` | TField |  |  |
| 11 | `FS.GI.LP.ROR.PL.EXCLUSION.RESERVED8` | `FsGiLpRorPlExclusion_Reserved8` | TField |  |  |
| 12 | `FS.GI.LP.ROR.PL.EXCLUSION.RESERVED7` | `FsGiLpRorPlExclusion_Reserved7` | TField |  |  |
| 13 | `FS.GI.LP.ROR.PL.EXCLUSION.RESERVED6` | `FsGiLpRorPlExclusion_Reserved6` | TField |  |  |
| 14 | `FS.GI.LP.ROR.PL.EXCLUSION.RESERVED5` | `FsGiLpRorPlExclusion_Reserved5` | TField |  |  |
| 15 | `FS.GI.LP.ROR.PL.EXCLUSION.RESERVED4` | `FsGiLpRorPlExclusion_Reserved4` | TField |  |  |
| 16 | `FS.GI.LP.ROR.PL.EXCLUSION.RESERVED3` | `FsGiLpRorPlExclusion_Reserved3` | TField |  |  |
| 17 | `FS.GI.LP.ROR.PL.EXCLUSION.RESERVED2` | `FsGiLpRorPlExclusion_Reserved2` | TField |  |  |
| 18 | `FS.GI.LP.ROR.PL.EXCLUSION.RESERVED1` | `FsGiLpRorPlExclusion_Reserved1` | TField |  |  |
| 19 | `FS.GI.LP.ROR.PL.EXCLUSION.LOCAL.REF` | `FsGiLpRorPlExclusion_LocalRef` |  |  |  |
| 20 | `FS.GI.LP.ROR.PL.EXCLUSION.OVERRIDE` | `FsGiLpRorPlExclusion_Override` |  |  |  |
| 21 | `FS.GI.LP.ROR.PL.EXCLUSION.RECORD.STATUS` | `FsGiLpRorPlExclusion_RecordStatus` | String |  |  |
| 22 | `FS.GI.LP.ROR.PL.EXCLUSION.CURR.NO` | `FsGiLpRorPlExclusion_CurrNo` | String |  |  |
| 23 | `FS.GI.LP.ROR.PL.EXCLUSION.INPUTTER` | `FsGiLpRorPlExclusion_Inputter` |  |  |  |
| 24 | `FS.GI.LP.ROR.PL.EXCLUSION.DATE.TIME` | `FsGiLpRorPlExclusion_DateTime` |  |  |  |
| 25 | `FS.GI.LP.ROR.PL.EXCLUSION.AUTHORISER` | `FsGiLpRorPlExclusion_Authoriser` | String |  |  |
| 26 | `FS.GI.LP.ROR.PL.EXCLUSION.CO.CODE` | `FsGiLpRorPlExclusion_CoCode` | String |  |  |
| 27 | `FS.GI.LP.ROR.PL.EXCLUSION.DEPT.CODE` | `FsGiLpRorPlExclusion_DeptCode` | String |  |  |
| 28 | `FS.GI.LP.ROR.PL.EXCLUSION.AUDITOR.CODE` | `FsGiLpRorPlExclusion_AuditorCode` | String |  |  |
| 29 | `FS.GI.LP.ROR.PL.EXCLUSION.AUDIT.DATE.TIME` | `FsGiLpRorPlExclusion_AuditDateTime` | String |  |  |
