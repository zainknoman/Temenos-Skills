# ASSET.MAINTENANCE — Table Schema

> Source: `INSERTS/I_F.ASSET.MAINTENANCE` in `FIXAMT_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FX.AM.ASSET.ID` | `AssetMaintenance_AssetId` | TField | Yes | Auto-generated unique Identifier allotted for the Asset as a result of registering an asset. This is a mandatory field. |
| 2 | `FX.AM.ACTIVITY` | `AssetMaintenance_Activity` | TField | Yes | List of Activities involved in the Life-Cycle of an Asset. Possible values are 1. Register 2. Capital WIP 3. Purchase 4. Depreciation 5. Capital Improvement 6. Transfer 7.Dispose 8. Write-Off This is a mandatory field |
| 3 | `FX.AM.ASSET.CLASS` | `AssetMaintenance_AssetClass` | TField | Conditional | Reference to the ASSET.CLASS table. Identifies the Class of the Asset being registered. Optional Input, if not keyed-in will be determined based on Asset Type. This is a mandatory field. |
| 4 | `FX.AM.ASSET.TYPE` | `AssetMaintenance_AssetType` | TField | Yes | Reference to the FIXED.ASSET.TYPE table. Identifies the Type of the Asset being registered under respective Asset Class. This is a mandatory field. |
| 5 | `FX.AM.OWNERSHIP.TYPE` | `AssetMaintenance_OwnershipType` | TField | No | Reference to EB.LOOKUP. Following are the lookup value, 1. Leasehold 2. Freehold 3. Other. Optional Input. |
| 6 | `FX.AM.DEPRECIATION.ALLOWED` | `AssetMaintenance_DepreciationAllowed` | TField | Yes | Identifies if the Depreciation Calculation and Posting is applicable for the asset or not. Allowed values are Yes / No. Mandatory Input, If not keyed-in defaulted from Asset Type or Asset Class table |
| 7 | `FX.AM.DEPRECIATION.METHOD` | `AssetMaintenance_DepreciationMethod` | TField | Yes | Depreciation Method applicable for the Asset. Possible values are 1.SL - Straight Line 2.RB - Reducing Balance 3.FS - Flexible Schedules 4.DDB (Double Declining Balance) 5.SYD (Sum of Years Digit). Mandatory Input when depreciation allowed is Yes. If not keyed-in, defaulted from Asset Type. |
| 8 | `FX.AM.DEPRECIATION.FREQ` | `AssetMaintenance_DepreciationFreq` |  |  |  |
| 9 | `FX.AM.DEPRECIATION.FINAL.SCHED` | `AssetMaintenance_DepreciationFinalSched` |  |  |  |
| 10 | `FX.AM.DEPRECIATION.RATE` | `AssetMaintenance_DepreciationRate` |  |  |  |
| 11 | `FX.AM.ECONOMIC.LIFE` | `AssetMaintenance_EconomicLife` | TField | Yes | Economic life of the asset expressed as a number of years or months. Years will be converted to months. Years is entered by entering the years followed by a 'Y' Mandatory Input, If not keyed-in defaulted from Asset Type. |
| 12 | `FX.AM.DATE.OF.PURCHASE` | `AssetMaintenance_DateOfPurchase` | TField | No | Date of Invoice, Date from which the asset is considered for depreciation. Optional Input, If not keyed-in defaulted to today. Value can be back dated if within one backward cycle of depreciation frequency. Future date is not allowed. |
| 13 | `FX.AM.CURRENCY.OF.ASSET` | `AssetMaintenance_CurrencyOfAsset` | TField | No | Reference to CURRENCY table. Identifies the currency in which the asset is purchased or reported in the books. Optional Input, If not keyed-in defaulted to local currency. |
| 14 | `FX.AM.ORIGINAL.VAL.OF.ASSET` | `AssetMaintenance_OriginalValOfAsset` | TField | Yes | The initial or the original value of the asset expressed in Currency of the Asset. This is a mandatory field. |
| 15 | `FX.AM.COST.OF.ASSET` | `AssetMaintenance_CostOfAsset` | TField | No | The original value of the asset plus any additional cost incurred. Will be defaulted to Original Value of the Asset if not Keyed-In. Optional Input. |
| 16 | `FX.AM.RESIDUAL.VALUE` | `AssetMaintenance_ResidualValue` | TField | No | The salvage value of the asset at the end of its economic life. Optional Input. |
| 17 | `FX.AM.COST.TYPE` | `AssetMaintenance_CostType` |  |  |  |
| 18 | `FX.AM.COST.TYPE.AMT` | `AssetMaintenance_CostTypeAmt` |  |  |  |
| 19 | `FX.AM.ASSET.ENTITY` | `AssetMaintenance_AssetEntity` | TField | Yes | Reference to ASSET.ENTITY table. Identifies the Organisation Unit where the asset is being deployed. Mandatory Input. |
| 20 | `FX.AM.THIRD.PARTY.BENE.REF` | `AssetMaintenance_ThirdPartyBeneRef` | TField | Yes | Reference to BENEFICIARY application. All payments to supplier will be made to the account details given in the respective BENEFICIARY record. Mandatory Input for Register and Capital Improvement activities. |
| 21 | `FX.AM.CWIP.AMOUNT` | `AssetMaintenance_CwipAmount` | TField | Yes | Transaction Amount for the current WIP (Work-in-Progress) payment to be made to the supplier. Expressed in the Currency of the Asset. Mandatory Input for Capital WIP activity. |
| 22 | `FX.AM.TRANSFER.TO.ENTITY` | `AssetMaintenance_TransferToEntity` | TField | Yes | Reference to ASSET.ENTITY table. Identifies the Organisation Unit to which the Asset is being transferred to. Mandatory Input for Transfer activity. |
| 23 | `FX.AM.SALE.VALUE` | `AssetMaintenance_SaleValue` | TField | Yes | Amount at which the asset is sold. Sale Value should always be expressed in the Asset Currency. Mandatory Input for Dispose activity. |
| 24 | `FX.AM.DATE.OF.CAPITAL.IMPROVEMENT` | `AssetMaintenance_DateOfCapitalImprovement` | TField | Yes | Date from which the Capital Improvement Cost will be considered for Depreciation calculation. Restricted to be a date within the current depreciation period. Mandatory Input for Capital Improvement activity. Value can be back dated if within one backward cycle of depreciation frequency. Future date is not allowed. |
| 25 | `FX.AM.CAPITAL.IMPROVEMENT.COST` | `AssetMaintenance_CapitalImprovementCost` | TField | Yes | Total cost of improvement which will be added to the Original Cost of the Asset. Improvement Cost should be expressed only in Asset Currency. Mandatory Input for Capital Improvement activity. |
| 26 | `FX.AM.ECONOMIC.LIFE.EXTENSION` | `AssetMaintenance_EconomicLifeExtension` | TField | No | The number of months the economic life of asset is increased as a result of improvement, which will be added theeconomic life of the asset. Expressed as a number of years or months. Years will be converted to months. Years is entered by entering the years followed by a 'Y'. Optional Input. Applicable for Capital Improvement activity |
| 27 | `FX.AM.DEP.PERIOD.START` | `AssetMaintenance_DepPeriodStart` | TField |  | Start date for depreciation. |
| 28 | `FX.AM.DEP.PERIOD.END` | `AssetMaintenance_DepPeriodEnd` | TField |  | End date for depreciation. |
| 29 | `FX.AM.POSTING.DATE` | `AssetMaintenance_PostingDate` | TField |  | Date on which depreciation calculated and posted. |
| 30 | `FX.AM.AMOUNT` | `AssetMaintenance_Amount` | TField |  | Depreciation amount calculated. |
| 31 | `FX.AM.ASSET.DESCRIPTION` | `AssetMaintenance_AssetDescription` |  |  |  |
| 32 | `FX.AM.RESERVED09` | `AssetMaintenance_Reserved09` |  |  |  |
| 33 | `FX.AM.RESERVED08` | `AssetMaintenance_Reserved08` |  |  |  |
| 34 | `FX.AM.RESERVED07` | `AssetMaintenance_Reserved07` |  |  |  |
| 35 | `FX.AM.RESERVED06` | `AssetMaintenance_Reserved06` |  |  |  |
| 36 | `FX.AM.RESERVED05` | `AssetMaintenance_Reserved05` |  |  |  |
| 37 | `FX.AM.RESERVED04` | `AssetMaintenance_Reserved04` |  |  |  |
| 38 | `FX.AM.RESERVED03` | `AssetMaintenance_Reserved03` |  |  |  |
| 39 | `FX.AM.RESERVED02` | `AssetMaintenance_Reserved02` |  |  |  |
| 40 | `FX.AM.RESERVED01` | `AssetMaintenance_Reserved01` |  |  |  |
| 41 | `FX.AM.LOCAL.REF` | `AssetMaintenance_LocalRef` |  |  |  |
| 42 | `FX.AM.ENTRY.IDS` | `AssetMaintenance_EntryIds` |  |  |  |
| 43 | `FX.AM.OVERRIDE` | `AssetMaintenance_Override` |  |  |  |
| 44 | `FX.AM.RECORD.STATUS` | `AssetMaintenance_RecordStatus` | String |  |  |
| 45 | `FX.AM.CURR.NO` | `AssetMaintenance_CurrNo` | String |  |  |
| 46 | `FX.AM.INPUTTER` | `AssetMaintenance_Inputter` |  |  |  |
| 47 | `FX.AM.DATE.TIME` | `AssetMaintenance_DateTime` |  |  |  |
| 48 | `FX.AM.AUTHORISER` | `AssetMaintenance_Authoriser` | String |  |  |
| 49 | `FX.AM.CO.CODE` | `AssetMaintenance_CoCode` | String |  |  |
| 50 | `FX.AM.DEPT.CODE` | `AssetMaintenance_DeptCode` | String |  |  |
| 51 | `FX.AM.AUDITOR.CODE` | `AssetMaintenance_AuditorCode` | String |  |  |
| 52 | `FX.AM.AUDIT.DATE.TIME` | `AssetMaintenance_AuditDateTime` | String |  |  |
