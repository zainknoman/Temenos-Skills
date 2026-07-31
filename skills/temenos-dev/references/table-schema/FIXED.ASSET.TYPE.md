# FIXED.ASSET.TYPE — Table Schema

> Source: `INSERTS/I_F.FIXED.ASSET.TYPE` in `FIXAMT_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AST.TYPE.SHORT.DESCRIPTION` | `FixedAssetType_ShortDescription` | TField |  | This field tells the description of Asset Type to be used for enrichment purpose. |
| 2 | `AST.TYPE.ASSET.CLASS` | `FixedAssetType_AssetClass` | TField |  | This field denotes the asset class under which the respective ASSET.TYPE can be classified. |
| 3 | `AST.TYPE.DEPR.ALLOWED` | `FixedAssetType_DeprAllowed` | TField |  | This field identifies if depreciation calculation and posting is applicable for the Asset Type. Can be negotiated at individual asset level . Allowed Values are YES , NO |
| 4 | `AST.TYPE.DEPR.METHOD` | `FixedAssetType_DeprMethod` | TField |  | This field decides how the depreciation method applicable for the Asset Type. Allowed values are SL (Straight Line), RB (Reducing Balance), FS (Flexible Schedules), DDB (Double Declining Balance) and SYD (Sum of Years Digit). |
| 5 | `AST.TYPE.DEPR.FREQUENCY` | `FixedAssetType_DeprFrequency` |  |  |  |
| 6 | `AST.TYPE.DEPRECIATION.TERM` | `FixedAssetType_DepreciationTerm` |  |  |  |
| 7 | `AST.TYPE.DEPRECIATION.RATE` | `FixedAssetType_DepreciationRate` |  |  |  |
| 8 | `AST.TYPE.ECONOMIC.LIFE` | `FixedAssetType_EconomicLife` | TField |  | This field decides how the value of an assets under this Asset Type. Expressed as a number of years or months. Years will be converted to months.Years is entered by entering the years followed by a 'Y'. |
| 9 | `AST.TYPE.OWNERSHIP.TYPE` | `FixedAssetType_OwnershipType` |  |  |  |
| 10 | `AST.TYPE.MAND.COST.TYPES` | `FixedAssetType_MandCostTypes` |  |  |  |
| 11 | `AST.TYPE.OPT.COST.TYPES` | `FixedAssetType_OptCostTypes` |  |  |  |
| 12 | `AST.TYPE.RESERVED.10` | `FixedAssetType_Reserved10` |  |  |  |
| 13 | `AST.TYPE.RESERVED.9` | `FixedAssetType_Reserved9` |  |  |  |
| 14 | `AST.TYPE.RESERVED.8` | `FixedAssetType_Reserved8` |  |  |  |
| 15 | `AST.TYPE.RESERVED.7` | `FixedAssetType_Reserved7` |  |  |  |
| 16 | `AST.TYPE.RESERVED.6` | `FixedAssetType_Reserved6` |  |  |  |
| 17 | `AST.TYPE.RESERVED.5` | `FixedAssetType_Reserved5` |  |  |  |
| 18 | `AST.TYPE.RESERVED.4` | `FixedAssetType_Reserved4` |  |  |  |
| 19 | `AST.TYPE.RESERVED.3` | `FixedAssetType_Reserved3` | TField |  |  |
| 20 | `AST.TYPE.RESERVED.2` | `FixedAssetType_Reserved2` | TField |  |  |
| 21 | `AST.TYPE.RESERVED.1` | `FixedAssetType_Reserved1` | TField |  |  |
| 22 | `AST.TYPE.LOCAL.REF` | `FixedAssetType_LocalRef` |  |  |  |
| 23 | `AST.TYPE.OVERRIDE` | `FixedAssetType_Override` |  |  |  |
| 24 | `AST.TYPE.RECORD.STATUS` | `FixedAssetType_RecordStatus` | String |  |  |
| 25 | `AST.TYPE.CURR.NO` | `FixedAssetType_CurrNo` | String |  |  |
| 26 | `AST.TYPE.INPUTTER` | `FixedAssetType_Inputter` |  |  |  |
| 27 | `AST.TYPE.DATE.TIME` | `FixedAssetType_DateTime` |  |  |  |
| 28 | `AST.TYPE.AUTHORISER` | `FixedAssetType_Authoriser` | String |  |  |
| 29 | `AST.TYPE.CO.CODE` | `FixedAssetType_CoCode` | String |  |  |
| 30 | `AST.TYPE.DEPT.CODE` | `FixedAssetType_DeptCode` | String |  |  |
| 31 | `AST.TYPE.AUDITOR.CODE` | `FixedAssetType_AuditorCode` | String |  |  |
| 32 | `AST.TYPE.AUDIT.DATE.TIME` | `FixedAssetType_AuditDateTime` | String |  |  |
