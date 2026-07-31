# FS.GI.LP.ROR.ABF.EXCLUSION — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.ROR.ABF.EXCLUSION` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.ROR.ABF.EXCLUSION.PARENT.REF.ID` | `FsGiLpRorAbfExclusion_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.ROR.ABF.EXCLUSION.ORA.ROWID` | `FsGiLpRorAbfExclusion_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.ROR.ABF.EXCLUSION.TA.FUND.ID` | `FsGiLpRorAbfExclusion_TaFundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.LP.ROR.ABF.EXCLUSION.ROR.CALC.BASIS` | `FsGiLpRorAbfExclusion_RorCalcBasis` | TField |  | ROR calculation basis code. Multifonds DB Column is ROR_CALC_BASIS. |
| 5 | `FS.GI.LP.ROR.ABF.EXCLUSION.ASSET.BASED.FEE` | `FsGiLpRorAbfExclusion_AssetBasedFee` | TField |  | Asset based fee type. Multifonds DB Column is CASSET_FEE. |
| 6 | `FS.GI.LP.ROR.ABF.EXCLUSION.EXCL.ABF.ACCRUAL.FLAG` | `FsGiLpRorAbfExclusion_ExclAbfAccrualFlag` | TField |  | Flag to exclude asset based fee accrual from ROR calculation. Multifonds DB Column is FLG_EXCL_ABF_ACCRUAL. |
| 7 | `FS.GI.LP.ROR.ABF.EXCLUSION.EXCL.ABF.CRYST.FLAG` | `FsGiLpRorAbfExclusion_ExclAbfCrystFlag` | TField |  | Flag to exclude asset based fee crystallized from RoR calculation. Multifonds DB Column is FLG_EXCL_ABF_CRYST. |
| 8 | `FS.GI.LP.ROR.ABF.EXCLUSION.FUND.ID` | `FsGiLpRorAbfExclusion_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.LP.ROR.ABF.EXCLUSION.CLASS.CURRENCY` | `FsGiLpRorAbfExclusion_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.LP.ROR.ABF.EXCLUSION.RESERVED10` | `FsGiLpRorAbfExclusion_Reserved10` | TField |  |  |
| 11 | `FS.GI.LP.ROR.ABF.EXCLUSION.RESERVED9` | `FsGiLpRorAbfExclusion_Reserved9` | TField |  |  |
| 12 | `FS.GI.LP.ROR.ABF.EXCLUSION.RESERVED8` | `FsGiLpRorAbfExclusion_Reserved8` | TField |  |  |
| 13 | `FS.GI.LP.ROR.ABF.EXCLUSION.RESERVED7` | `FsGiLpRorAbfExclusion_Reserved7` | TField |  |  |
| 14 | `FS.GI.LP.ROR.ABF.EXCLUSION.RESERVED6` | `FsGiLpRorAbfExclusion_Reserved6` | TField |  |  |
| 15 | `FS.GI.LP.ROR.ABF.EXCLUSION.RESERVED5` | `FsGiLpRorAbfExclusion_Reserved5` | TField |  |  |
| 16 | `FS.GI.LP.ROR.ABF.EXCLUSION.RESERVED4` | `FsGiLpRorAbfExclusion_Reserved4` | TField |  |  |
| 17 | `FS.GI.LP.ROR.ABF.EXCLUSION.RESERVED3` | `FsGiLpRorAbfExclusion_Reserved3` | TField |  |  |
| 18 | `FS.GI.LP.ROR.ABF.EXCLUSION.RESERVED2` | `FsGiLpRorAbfExclusion_Reserved2` | TField |  |  |
| 19 | `FS.GI.LP.ROR.ABF.EXCLUSION.RESERVED1` | `FsGiLpRorAbfExclusion_Reserved1` | TField |  |  |
| 20 | `FS.GI.LP.ROR.ABF.EXCLUSION.LOCAL.REF` | `FsGiLpRorAbfExclusion_LocalRef` |  |  |  |
| 21 | `FS.GI.LP.ROR.ABF.EXCLUSION.OVERRIDE` | `FsGiLpRorAbfExclusion_Override` |  |  |  |
| 22 | `FS.GI.LP.ROR.ABF.EXCLUSION.RECORD.STATUS` | `FsGiLpRorAbfExclusion_RecordStatus` | String |  |  |
| 23 | `FS.GI.LP.ROR.ABF.EXCLUSION.CURR.NO` | `FsGiLpRorAbfExclusion_CurrNo` | String |  |  |
| 24 | `FS.GI.LP.ROR.ABF.EXCLUSION.INPUTTER` | `FsGiLpRorAbfExclusion_Inputter` |  |  |  |
| 25 | `FS.GI.LP.ROR.ABF.EXCLUSION.DATE.TIME` | `FsGiLpRorAbfExclusion_DateTime` |  |  |  |
| 26 | `FS.GI.LP.ROR.ABF.EXCLUSION.AUTHORISER` | `FsGiLpRorAbfExclusion_Authoriser` | String |  |  |
| 27 | `FS.GI.LP.ROR.ABF.EXCLUSION.CO.CODE` | `FsGiLpRorAbfExclusion_CoCode` | String |  |  |
| 28 | `FS.GI.LP.ROR.ABF.EXCLUSION.DEPT.CODE` | `FsGiLpRorAbfExclusion_DeptCode` | String |  |  |
| 29 | `FS.GI.LP.ROR.ABF.EXCLUSION.AUDITOR.CODE` | `FsGiLpRorAbfExclusion_AuditorCode` | String |  |  |
| 30 | `FS.GI.LP.ROR.ABF.EXCLUSION.AUDIT.DATE.TIME` | `FsGiLpRorAbfExclusion_AuditDateTime` | String |  |  |
