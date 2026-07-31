# ASSET.DETAILS — Table Schema

> Source: `INSERTS/I_F.ASSET.DETAILS` in `FIXAMT_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AS.DET.ACTIVITY` | `AssetDetails_Activity` | TField |  | Activities involved in the Life-Cycle of an Asset. Possible values: Register Capital WIP Purchase Depreciation Capital Improvement Transfer Dispose Write-Off Recognise Write Off Update Market Value Update Disposal Cost Change Economic Life Increase/Decrease Lease Out Repossess Migrate Update Static Details Update Cost Details Latest activity performed for the asset is updated. |
| 2 | `AS.DET.ASSET.TYPE` | `AssetDetails_AssetType` | TField |  | Reference to the FIXED.ASSET.TYPE table. Identifies the Type of the Asset being registered under respective Asset Class. |
| 3 | `AS.DET.OWNERSHIP.TYPE` | `AssetDetails_OwnershipType` | TField |  |  |
| 4 | `AS.DET.COST.TYPE` | `AssetDetails_CostType` |  |  |  |
| 5 | `AS.DET.COST.TYPE.AMOUNT` | `AssetDetails_CostTypeAmount` |  |  |  |
| 6 | `AS.DET.ASSET.ENTITY` | `AssetDetails_AssetEntity` | TField |  | Reference to ASSET.ENTITY table. Identifies the Organisation Unit where the asset is being deployed. |
| 7 | `AS.DET.THIRD.PTY.BEN.REF` | `AssetDetails_ThirdPtyBenRef` | TField |  | Reference to BENEFICIARY application. All payments to supplier will be made to the account details given in therespective BENEFICIARY record. |
| 8 | `AS.DET.CWIP.AMOUNT` | `AssetDetails_CwipAmount` | TField |  | Transaction Amount for the current WIP payment to be made to the supplier. Expressed in the Currency of theAsset. |
| 9 | `AS.DET.OTHER.BEN.REF` | `AssetDetails_OtherBenRef` | TField |  | Reference to BENEFICIARY application. If a BENEFICIARY that is different from the one that was used in register is usedfor Capital Improvement activity, then this field is updated with the used BENEFICIARY. |
| 10 | `AS.DET.SALE.VALUE` | `AssetDetails_SaleValue` | TField |  | Amount at which the asset is sold. Sale Value should always be expressed in the Asset Currency. |
| 11 | `AS.DET.DATE.OF.CAPITAL.IMP` | `AssetDetails_DateOfCapitalImp` | TField |  | Date from which the Capital Improvement Cost will be considered for Depreciation calculation. Restricted to be adate within the current depreciation period. |
| 12 | `AS.DET.CAPITAL.IMP.COST` | `AssetDetails_CapitalImpCost` | TField |  | Total cost of improvement which has been added to the Original Cost of the Asset. Improvement Cost should beexpressed only in Asset Currency. |
| 13 | `AS.DET.ECONOMIC.LIFE.EXTEN` | `AssetDetails_EconomicLifeExten` | TField |  | The number of months the economic life of asset was increased as a result of capital improvement, which will be added theeconomic life of the asset. Expressed as a number of years or months. Years will be converted to months. Years isentered by entering the years followed by a 'Y'. |
| 14 | `AS.DET.TRANSFER.DATE` | `AssetDetails_TransferDate` |  |  |  |
| 15 | `AS.DET.TRANSFERRED.FROM.ENTITY` | `AssetDetails_TransferredFromEntity` |  |  |  |
| 16 | `AS.DET.STATUS.ASSET` | `AssetDetails_StatusAsset` | TField |  | Field which defines the status of the asset. |
| 17 | `AS.DET.CURRENCY` | `AssetDetails_Currency` | TField |  | Field which defines the currency of the asset. |
| 18 | `AS.DET.ASSET.CLASS` | `AssetDetails_AssetClass` | TField |  |  |
| 19 | `AS.DET.RESERVED.8` | `AssetDetails_Reserved8` |  |  |  |
| 20 | `AS.DET.RESERVED.7` | `AssetDetails_Reserved7` |  |  |  |
| 21 | `AS.DET.RESERVED.6` | `AssetDetails_Reserved6` |  |  |  |
| 22 | `AS.DET.RESERVED.5` | `AssetDetails_Reserved5` |  |  |  |
| 23 | `AS.DET.RESERVED.4` | `AssetDetails_Reserved4` |  |  |  |
| 24 | `AS.DET.RESERVED.3` | `AssetDetails_Reserved3` |  |  |  |
| 25 | `AS.DET.RESERVED.2` | `AssetDetails_Reserved2` |  |  |  |
| 26 | `AS.DET.RESERVED.1` | `AssetDetails_Reserved1` |  |  |  |
