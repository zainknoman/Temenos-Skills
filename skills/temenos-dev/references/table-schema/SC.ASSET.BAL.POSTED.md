# SC.ASSET.BAL.POSTED — Table Schema

> Source: `INSERTS/I_F.SC.ASSET.BAL.POSTED` in `AM_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ABP.CUSTOMER` | `ScAssetBalPosted_Customer` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `SC.ABP.REFERENCE.CCY` | `ScAssetBalPosted_ReferenceCcy` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `SC.ABP.EXT.DATE` | `ScAssetBalPosted_ExtDate` |  |  |  |
| 4 | `SC.ABP.SUB.AST.TYPE` | `ScAssetBalPosted_SubAstType` |  |  |  |
| 5 | `SC.ABP.NOMINAL` | `ScAssetBalPosted_Nominal` |  |  |  |
| 6 | `SC.ABP.NOMINAL.LCY` | `ScAssetBalPosted_NominalLcy` |  |  |  |
| 7 | `SC.ABP.ASSET.BAL` | `ScAssetBalPosted_AssetBal` |  |  |  |
| 8 | `SC.ABP.AST.BAL.SCY` | `ScAssetBalPosted_AstBalScy` |  |  |  |
| 9 | `SC.ABP.SECURITY.CCY` | `ScAssetBalPosted_SecurityCcy` |  |  |  |
| 10 | `SC.ABP.PRODUCT` | `ScAssetBalPosted_Product` |  |  |  |
| 11 | `SC.ABP.ASSET.ID` | `ScAssetBalPosted_AssetId` |  |  |  |
| 12 | `SC.ABP.SV.RES.3` | `ScAssetBalPosted_SvRes3` |  |  |  |
| 13 | `SC.ABP.SV.RES.2` | `ScAssetBalPosted_SvRes2` |  |  |  |
| 14 | `SC.ABP.SV.RES.1` | `ScAssetBalPosted_SvRes1` |  |  |  |
| 15 | `SC.ABP.TOT.ASSET.BAL` | `ScAssetBalPosted_TotAssetBal` |  |  |  |
| 16 | `SC.ABP.TOT.AVG.NOMINAL` | `ScAssetBalPosted_TotAvgNominal` |  |  |  |
| 17 | `SC.ABP.TOT.AVG.NOM.LCY` | `ScAssetBalPosted_TotAvgNomLcy` |  |  |  |
| 18 | `SC.ABP.TOT.AVG.AST.BAL` | `ScAssetBalPosted_TotAvgAstBal` |  |  |  |
| 19 | `SC.ABP.TOT.AST.BAL.SCY` | `ScAssetBalPosted_TotAstBalScy` |  |  |  |
| 20 | `SC.ABP.TOT.AV.AS.BL.SC` | `ScAssetBalPosted_TotAvAsBlSc` |  |  |  |
| 21 | `SC.ABP.MV.RES.5` | `ScAssetBalPosted_MvRes5` |  |  |  |
| 22 | `SC.ABP.MV.RES.4` | `ScAssetBalPosted_MvRes4` |  |  |  |
| 23 | `SC.ABP.MV.RES.3` | `ScAssetBalPosted_MvRes3` |  |  |  |
| 24 | `SC.ABP.MV.RES.2` | `ScAssetBalPosted_MvRes2` |  |  |  |
| 25 | `SC.ABP.MV.RES.1` | `ScAssetBalPosted_MvRes1` |  |  |  |
| 26 | `SC.ABP.PORTFOLIO` | `ScAssetBalPosted_Portfolio` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 27 | `SC.ABP.SECURITY.CODE` | `ScAssetBalPosted_SecurityCode` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 28 | `SC.ABP.RESERVED.5` | `ScAssetBalPosted_Reserved5` | TField |  |  |
| 29 | `SC.ABP.RESERVED.4` | `ScAssetBalPosted_Reserved4` | TField |  |  |
| 30 | `SC.ABP.RESERVED.3` | `ScAssetBalPosted_Reserved3` | TField |  |  |
| 31 | `SC.ABP.RESERVED.2` | `ScAssetBalPosted_Reserved2` | TField |  |  |
| 32 | `SC.ABP.RESERVED.1` | `ScAssetBalPosted_Reserved1` | TField |  |  |
| 33 | `SC.ABP.LOCAL.REF` | `ScAssetBalPosted_LocalRef` |  |  |  |
| 34 | `SC.ABP.RECORD.STATUS` | `ScAssetBalPosted_RecordStatus` | String |  |  |
| 35 | `SC.ABP.CURR.NO` | `ScAssetBalPosted_CurrNo` | String |  |  |
| 36 | `SC.ABP.INPUTTER` | `ScAssetBalPosted_Inputter` |  |  |  |
| 37 | `SC.ABP.DATE.TIME` | `ScAssetBalPosted_DateTime` |  |  |  |
| 38 | `SC.ABP.AUTHORISER` | `ScAssetBalPosted_Authoriser` | String |  |  |
| 39 | `SC.ABP.CO.CODE` | `ScAssetBalPosted_CoCode` | String |  |  |
| 40 | `SC.ABP.DEPT.CODE` | `ScAssetBalPosted_DeptCode` | String |  |  |
| 41 | `SC.ABP.AUDITOR.CODE` | `ScAssetBalPosted_AuditorCode` | String |  |  |
| 42 | `SC.ABP.AUDIT.DATE.TIME` | `ScAssetBalPosted_AuditDateTime` | String |  |  |
