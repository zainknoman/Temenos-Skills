# FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM` in `FS_LimitedPartnershipStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.PARENT.REF.ID` | `FsGiFundPaAssetBasedFeeParam_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.ORA.ROWID` | `FsGiFundPaAssetBasedFeeParam_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.TA.FUND.ID` | `FsGiFundPaAssetBasedFeeParam_TaFundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.ASSET.BASED.FEE` | `FsGiFundPaAssetBasedFeeParam_AssetBasedFee` | TField |  | Asset based fee code linked to the parternship parameters. Multifonds DB Column is CASSET_FEE. |
| 5 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.PRIORITY.SEQUENCE` | `FsGiFundPaAssetBasedFeeParam_PrioritySequence` | TField |  | Priority sequence of the asset based fees linked to the parternship parameters. Multifonds DB Column is PRIORITY. |
| 6 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.INCL.CAP.BASIS.INCOME.ALLOC` | `FsGiFundPaAssetBasedFeeParam_InclCapBasisIncomeAlloc` | TField |  | Asset-based fee accrual to be excluded (gross basis) from the capital basis for income allocation. If not excluded, asset-based fee accruals are automatically included (net of accrual basis) in the capital basis. Multifonds DB Column is EXCL_CAP_ALLOC. |
| 7 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.EXCLUDE.FROM.NET.CALC` | `FsGiFundPaAssetBasedFeeParam_ExcludeFromNetCalc` | TField |  | Asset-based fees to be not netted out from the a Net ofa Performance Return Calcs. If not listed, asset-based fee types are automatically netted out. Multifonds DB Column is EXCL_NET_CALC. |
| 8 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.CHANGED.FLAG` | `FsGiFundPaAssetBasedFeeParam_ChangedFlag` | TField |  | Internal flag to indicate change in the record. Multifonds DB Column is FLG_CHANGED. |
| 9 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.FUND.ID` | `FsGiFundPaAssetBasedFeeParam_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 10 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.CLASS.CURRENCY` | `FsGiFundPaAssetBasedFeeParam_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 11 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RESERVED10` | `FsGiFundPaAssetBasedFeeParam_Reserved10` | TField |  |  |
| 12 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RESERVED9` | `FsGiFundPaAssetBasedFeeParam_Reserved9` | TField |  |  |
| 13 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RESERVED8` | `FsGiFundPaAssetBasedFeeParam_Reserved8` | TField |  |  |
| 14 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RESERVED7` | `FsGiFundPaAssetBasedFeeParam_Reserved7` | TField |  |  |
| 15 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RESERVED6` | `FsGiFundPaAssetBasedFeeParam_Reserved6` | TField |  |  |
| 16 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RESERVED5` | `FsGiFundPaAssetBasedFeeParam_Reserved5` | TField |  |  |
| 17 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RESERVED4` | `FsGiFundPaAssetBasedFeeParam_Reserved4` | TField |  |  |
| 18 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RESERVED3` | `FsGiFundPaAssetBasedFeeParam_Reserved3` | TField |  |  |
| 19 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RESERVED2` | `FsGiFundPaAssetBasedFeeParam_Reserved2` | TField |  |  |
| 20 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RESERVED1` | `FsGiFundPaAssetBasedFeeParam_Reserved1` | TField |  |  |
| 21 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.LOCAL.REF` | `FsGiFundPaAssetBasedFeeParam_LocalRef` |  |  |  |
| 22 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.OVERRIDE` | `FsGiFundPaAssetBasedFeeParam_Override` |  |  |  |
| 23 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.RECORD.STATUS` | `FsGiFundPaAssetBasedFeeParam_RecordStatus` | String |  |  |
| 24 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.CURR.NO` | `FsGiFundPaAssetBasedFeeParam_CurrNo` | String |  |  |
| 25 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.INPUTTER` | `FsGiFundPaAssetBasedFeeParam_Inputter` |  |  |  |
| 26 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.DATE.TIME` | `FsGiFundPaAssetBasedFeeParam_DateTime` |  |  |  |
| 27 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.AUTHORISER` | `FsGiFundPaAssetBasedFeeParam_Authoriser` | String |  |  |
| 28 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.CO.CODE` | `FsGiFundPaAssetBasedFeeParam_CoCode` | String |  |  |
| 29 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.DEPT.CODE` | `FsGiFundPaAssetBasedFeeParam_DeptCode` | String |  |  |
| 30 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.AUDITOR.CODE` | `FsGiFundPaAssetBasedFeeParam_AuditorCode` | String |  |  |
| 31 | `FS.GI.FUND.PA.ASSET.BASED.FEE.PARAM.AUDIT.DATE.TIME` | `FsGiFundPaAssetBasedFeeParam_AuditDateTime` | String |  |  |
