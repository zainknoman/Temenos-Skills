# FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE` in `FS_LimitedPartnership.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.PARENT.REF.ID` | `FsGiLpFeeExcludeAssetBasedfee_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.ORA.ROWID` | `FsGiLpFeeExcludeAssetBasedfee_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.ASSET.BASED.FEE.EXCLUSION` | `FsGiLpFeeExcludeAssetBasedfee_AssetBasedFeeExclusion` | TField |  | Allows specifying a list of asset-based fee types (other asset-based fee accruals to-date) to be excluded from the capital basis before calculating the asset-based. Multifonds DB Column is FEE_EXCL. |
| 4 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.TA.FUND.ID` | `FsGiLpFeeExcludeAssetBasedfee_TaFundId` | TField |  | Fund Internal ID. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.SHARE.CLASS.CODE` | `FsGiLpFeeExcludeAssetBasedfee_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 6 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.FEE.SEQUENCE.NO` | `FsGiLpFeeExcludeAssetBasedfee_FeeSequenceNo` | TField |  | Asset based fee unique sequence number automatically assigned by the system. Multifonds DB Column is FEE_SEQ_NO. |
| 7 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.FEE.TYPE.FLAG` | `FsGiLpFeeExcludeAssetBasedfee_FeeTypeFlag` | TField |  | Specifies the applied asset based fee type. Multifonds DB Column is FLG_FEE_TYPE. |
| 8 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.FUND.ID` | `FsGiLpFeeExcludeAssetBasedfee_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.CLASS.CURRENCY` | `FsGiLpFeeExcludeAssetBasedfee_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RESERVED10` | `FsGiLpFeeExcludeAssetBasedfee_Reserved10` | TField |  |  |
| 11 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RESERVED9` | `FsGiLpFeeExcludeAssetBasedfee_Reserved9` | TField |  |  |
| 12 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RESERVED8` | `FsGiLpFeeExcludeAssetBasedfee_Reserved8` | TField |  |  |
| 13 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RESERVED7` | `FsGiLpFeeExcludeAssetBasedfee_Reserved7` | TField |  |  |
| 14 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RESERVED6` | `FsGiLpFeeExcludeAssetBasedfee_Reserved6` | TField |  |  |
| 15 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RESERVED5` | `FsGiLpFeeExcludeAssetBasedfee_Reserved5` | TField |  |  |
| 16 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RESERVED4` | `FsGiLpFeeExcludeAssetBasedfee_Reserved4` | TField |  |  |
| 17 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RESERVED3` | `FsGiLpFeeExcludeAssetBasedfee_Reserved3` | TField |  |  |
| 18 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RESERVED2` | `FsGiLpFeeExcludeAssetBasedfee_Reserved2` | TField |  |  |
| 19 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RESERVED1` | `FsGiLpFeeExcludeAssetBasedfee_Reserved1` | TField |  |  |
| 20 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.LOCAL.REF` | `FsGiLpFeeExcludeAssetBasedfee_LocalRef` |  |  |  |
| 21 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.OVERRIDE` | `FsGiLpFeeExcludeAssetBasedfee_Override` |  |  |  |
| 22 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.RECORD.STATUS` | `FsGiLpFeeExcludeAssetBasedfee_RecordStatus` | String |  |  |
| 23 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.CURR.NO` | `FsGiLpFeeExcludeAssetBasedfee_CurrNo` | String |  |  |
| 24 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.INPUTTER` | `FsGiLpFeeExcludeAssetBasedfee_Inputter` |  |  |  |
| 25 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.DATE.TIME` | `FsGiLpFeeExcludeAssetBasedfee_DateTime` |  |  |  |
| 26 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.AUTHORISER` | `FsGiLpFeeExcludeAssetBasedfee_Authoriser` | String |  |  |
| 27 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.CO.CODE` | `FsGiLpFeeExcludeAssetBasedfee_CoCode` | String |  |  |
| 28 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.DEPT.CODE` | `FsGiLpFeeExcludeAssetBasedfee_DeptCode` | String |  |  |
| 29 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.AUDITOR.CODE` | `FsGiLpFeeExcludeAssetBasedfee_AuditorCode` | String |  |  |
| 30 | `FS.GI.LP.FEE.EXCLUDE.ASSET.BASEDFEE.AUDIT.DATE.TIME` | `FsGiLpFeeExcludeAssetBasedfee_AuditDateTime` | String |  |  |
