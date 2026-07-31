# AM.VAL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AM.VAL.PARAMETER` in `AM_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.PRT.LANGUAGE` | `AmValParameter_Language` | TField |  | Will contain English for the SYSTEM record and the user language for any other ID. |
| 2 | `AM.PRT.DISP.ASSET.TYPE` | `AmValParameter_DispAssetType` | TField |  | Sort order for the ASSET.TYPE. Can be Ascending, Descending or New List. If set to New List the field ASSET.TYPE will be inputable and will allow the user to specify how he wants the list to be set. |
| 3 | `AM.PRT.ASSET.TYPE` | `AmValParameter_AssetType` |  |  |  |
| 4 | `AM.PRT.DISP.SUBASSET.TYPE` | `AmValParameter_DispSubassetType` | TField |  | Sort order for the SUB.ASSET.TYPE. Can be Ascending, Descending or New List. If set to New List the field Sub Asset Type will be inputable and will allow the user to specify how he wants the list to be set. |
| 5 | `AM.PRT.SUB.ASSET.TYPE` | `AmValParameter_SubAssetType` |  |  |  |
| 6 | `AM.PRT.DISP.CURRENCY` | `AmValParameter_DispCurrency` | TField |  | Sort order for the Currency. Can be Ascending, Descending, Ascending Amount, Descending Amount or New List. If set to New List the field Currency will be inputable and will allow the user to specify how he wants the list to be set. |
| 7 | `AM.PRT.CURRENCY` | `AmValParameter_Currency` |  |  |  |
| 8 | `AM.PRT.FX.DISPLAY` | `AmValParameter_FxDisplay` | TField |  | Forex creates two entries in SC.VALUATION.EXTRACT (One for the Asset side and one for the Liability side). Should you want to see just the valuated part then you have to specify 1leg. The option 2leg will show both legs of the forex transaction. |
| 9 | `AM.PRT.GRP.CODE` | `AmValParameter_GrpCode` |  |  |  |
| 10 | `AM.PRT.GRP.DESC` | `AmValParameter_GrpDesc` |  |  |  |
| 11 | `AM.PRT.ASSET.NO` | `AmValParameter_AssetNo` |  |  |  |
| 12 | `AM.PRT.FOR.MEMORY` | `AmValParameter_ForMemory` |  |  |  |
| 13 | `AM.PRT.MNEMONIC` | `AmValParameter_Mnemonic` |  |  |  |
| 14 | `AM.PRT.DD.LABEL` | `AmValParameter_DdLabel` |  |  |  |
| 15 | `AM.PRT.ENQ.VER.ID` | `AmValParameter_EnqVerId` |  |  |  |
| 16 | `AM.PRT.RESERVED20` | `AmValParameter_Reserved20` |  |  |  |
| 17 | `AM.PRT.VER.FUNCTION` | `AmValParameter_VerFunction` |  |  |  |
| 18 | `AM.PRT.DD.ID.FIELD` | `AmValParameter_DdIdField` |  |  |  |
| 19 | `AM.PRT.RESERVED19` | `AmValParameter_Reserved19` |  |  |  |
| 20 | `AM.PRT.RESERVED18` | `AmValParameter_Reserved18` |  |  |  |
| 21 | `AM.PRT.RESERVED17` | `AmValParameter_Reserved17` |  |  |  |
| 22 | `AM.PRT.RESERVED16` | `AmValParameter_Reserved16` |  |  |  |
| 23 | `AM.PRT.ENQ.MNEMONIC` | `AmValParameter_EnqMnemonic` |  |  |  |
| 24 | `AM.PRT.ENQUIRY.ID` | `AmValParameter_EnquiryId` |  |  |  |
| 25 | `AM.PRT.VERSION.ID` | `AmValParameter_VersionId` |  |  |  |
| 26 | `AM.PRT.SEL.FIELD` | `AmValParameter_SelField` |  |  |  |
| 27 | `AM.PRT.SEL.OPERAND` | `AmValParameter_SelOperand` |  |  |  |
| 28 | `AM.PRT.SEL.VALUE` | `AmValParameter_SelValue` |  |  |  |
| 29 | `AM.PRT.RESERVED15` | `AmValParameter_Reserved15` |  |  |  |
| 30 | `AM.PRT.RESERVED14` | `AmValParameter_Reserved14` |  |  |  |
| 31 | `AM.PRT.RESERVED13` | `AmValParameter_Reserved13` |  |  |  |
| 32 | `AM.PRT.SUB.ASSET.NO` | `AmValParameter_SubAssetNo` |  |  |  |
| 33 | `AM.PRT.RESERVED11` | `AmValParameter_Reserved11` |  |  |  |
| 34 | `AM.PRT.AST.SUBAST.TYPE` | `AmValParameter_AstSubastType` |  |  |  |
| 35 | `AM.PRT.APPLICATION` | `AmValParameter_Application` |  |  |  |
| 36 | `AM.PRT.DISP.FIELDS` | `AmValParameter_DispFields` |  |  |  |
| 37 | `AM.PRT.VIEW` | `AmValParameter_View` |  |  |  |
| 38 | `AM.PRT.LAUNCH.AT.OPEN` | `AmValParameter_LaunchAtOpen` |  |  |  |
| 39 | `AM.PRT.LAUNCH.VAL.AT.OPEN` | `AmValParameter_LaunchValAtOpen` | TField |  | Not Supported in T24 Browser |
| 40 | `AM.PRT.VAL.EXPIRY` | `AmValParameter_ValExpiry` | TField |  | Time in seconds within which Valuation will not be recalculated for the same enquiry when refreshed or repeated. If ONLINE.YNO set to 'Y' for an enquiry or enquiries in a composite screen, and valuations are requested by the enquiry(ies) using the same parameters within the VAL.EXPIRY period, revaluation will not occur, however, outside that period revaluation will occur. |
| 41 | `AM.PRT.SEGMENT` | `AmValParameter_Segment` | TField |  | Defines the default segmentation scheme to use when selected in an online valation request. |
| 42 | `AM.PRT.HIER.SEP` | `AmValParameter_HierSep` | TField |  | Defines the seperator to be used in generating hierarchical keys in the valuation workfile. |
| 43 | `AM.PRT.FRWK.ENQ` | `AmValParameter_FrwkEnq` |  |  |  |
| 44 | `AM.PRT.FRWK.TOOL` | `AmValParameter_FrwkTool` |  |  |  |
| 45 | `AM.PRT.HIERARCHY` | `AmValParameter_Hierarchy` | TField |  | Defines the default hierarchy scheme to use when selected in an online valation request. |
| 46 | `AM.PRT.VAL.OO.AT.LIMIT` | `AmValParameter_ValOoAtLimit` | TField |  | If set to 'YES', valuation of open limit orders will be at limit price instead of at market price. The default setting of this field is blank, in which case valuation of all open orders is at market price. |
| 47 | `AM.PRT.RECORD.STATUS` | `AmValParameter_RecordStatus` | String |  |  |
| 48 | `AM.PRT.CURR.NO` | `AmValParameter_CurrNo` | String |  |  |
| 49 | `AM.PRT.INPUTTER` | `AmValParameter_Inputter` |  |  |  |
| 50 | `AM.PRT.DATE.TIME` | `AmValParameter_DateTime` |  |  |  |
| 51 | `AM.PRT.AUTHORISER` | `AmValParameter_Authoriser` | String |  |  |
| 52 | `AM.PRT.CO.CODE` | `AmValParameter_CoCode` | String |  |  |
| 53 | `AM.PRT.DEPT.CODE` | `AmValParameter_DeptCode` | String |  |  |
| 54 | `AM.PRT.AUDITOR.CODE` | `AmValParameter_AuditorCode` | String |  |  |
| 55 | `AM.PRT.AUDIT.DATE.TIME` | `AmValParameter_AuditDateTime` | String |  |  |
