# FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.PARENT.REF.ID` | `FsGiLpFeeExcludeGlCategory_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.ORA.ROWID` | `FsGiLpFeeExcludeGlCategory_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.GL.CATEGORY.ID.EXCLUSION` | `FsGiLpFeeExcludeGlCategory_GlCategoryIdExclusion` | TField |  | Allows specifying a list of GL categories to be excluded from the capital basis before calculating the asset-based fee. Multifonds DB Column is GL_EXCL. |
| 4 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.TA.FUND.ID` | `FsGiLpFeeExcludeGlCategory_TaFundId` | TField |  | Fund Internal ID. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.SHARE.CLASS.CODE` | `FsGiLpFeeExcludeGlCategory_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 6 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.FEE.SEQUENCE.NO` | `FsGiLpFeeExcludeGlCategory_FeeSequenceNo` | TField |  | Asset based fee unique sequence number automatically assigned by the system. Multifonds DB Column is FEE_SEQ_NO. |
| 7 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.FEE.TYPE.FLAG` | `FsGiLpFeeExcludeGlCategory_FeeTypeFlag` | TField |  | Specifies the applied asset based fee type. Multifonds DB Column is FLG_FEE_TYPE. |
| 8 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.FUND.ID` | `FsGiLpFeeExcludeGlCategory_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.CLASS.CURRENCY` | `FsGiLpFeeExcludeGlCategory_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RESERVED10` | `FsGiLpFeeExcludeGlCategory_Reserved10` | TField |  |  |
| 11 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RESERVED9` | `FsGiLpFeeExcludeGlCategory_Reserved9` | TField |  |  |
| 12 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RESERVED8` | `FsGiLpFeeExcludeGlCategory_Reserved8` | TField |  |  |
| 13 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RESERVED7` | `FsGiLpFeeExcludeGlCategory_Reserved7` | TField |  |  |
| 14 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RESERVED6` | `FsGiLpFeeExcludeGlCategory_Reserved6` | TField |  |  |
| 15 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RESERVED5` | `FsGiLpFeeExcludeGlCategory_Reserved5` | TField |  |  |
| 16 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RESERVED4` | `FsGiLpFeeExcludeGlCategory_Reserved4` | TField |  |  |
| 17 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RESERVED3` | `FsGiLpFeeExcludeGlCategory_Reserved3` | TField |  |  |
| 18 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RESERVED2` | `FsGiLpFeeExcludeGlCategory_Reserved2` | TField |  |  |
| 19 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RESERVED1` | `FsGiLpFeeExcludeGlCategory_Reserved1` | TField |  |  |
| 20 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.LOCAL.REF` | `FsGiLpFeeExcludeGlCategory_LocalRef` |  |  |  |
| 21 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.OVERRIDE` | `FsGiLpFeeExcludeGlCategory_Override` |  |  |  |
| 22 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.RECORD.STATUS` | `FsGiLpFeeExcludeGlCategory_RecordStatus` | String |  |  |
| 23 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.CURR.NO` | `FsGiLpFeeExcludeGlCategory_CurrNo` | String |  |  |
| 24 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.INPUTTER` | `FsGiLpFeeExcludeGlCategory_Inputter` |  |  |  |
| 25 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.DATE.TIME` | `FsGiLpFeeExcludeGlCategory_DateTime` |  |  |  |
| 26 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.AUTHORISER` | `FsGiLpFeeExcludeGlCategory_Authoriser` | String |  |  |
| 27 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.CO.CODE` | `FsGiLpFeeExcludeGlCategory_CoCode` | String |  |  |
| 28 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.DEPT.CODE` | `FsGiLpFeeExcludeGlCategory_DeptCode` | String |  |  |
| 29 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.AUDITOR.CODE` | `FsGiLpFeeExcludeGlCategory_AuditorCode` | String |  |  |
| 30 | `FS.GI.LP.FEE.EXCLUDE.GL.CATEGORY.AUDIT.DATE.TIME` | `FsGiLpFeeExcludeGlCategory_AuditDateTime` | String |  |  |
