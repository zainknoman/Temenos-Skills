# ASSET.BY.CATEG — Table Schema

> Source: `INSERTS/I_F.ASSET.BY.CATEG` in `ST_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ABC.SUB.ASSET.TYPE` | `AssetByCateg_SubAssetType` | TField | Yes | Specifies the sub-asset type relating to the product category specified in the ID of this record. Example: Assuming that category code 1000 is for current accounts, 2000 is deposits/savings accounts, 21050 is for loans etc, the data may be set up as: Record 1 ID = 1000 Sub asset type = 310 (financial accounts) Record 2 ID = 2000 Sub asset type = 310 (financial accounts) Record 3 ID = 21050 Sub asset type = 320 (commercial loans) Validation Rules: 1-10 alpha characters. Mandatory for default records. Input not allowed for company specific records. Must exist on the SUB.ASSET.TYPE file. |
| 2 | `SC.ABC.MARGIN.RATE` | `AssetByCateg_MarginRate` | TField | No | Specifies the percentage of the asset/liability as defined by the category code to be used in portfolio valuations. This is the first level of checking when Securities programs value Accounts, Deposits or Forex deals. Depending upon whether a valuation should include/exclude liabilities, either this field or LOSS.MARGIN.RATE will be used to calculate the margin value. The method of calculation is defined in the field MARGIN.VALUE in SC.PARAMETER If a value is not found on the ASSET.BY.CATEG file then the SUB.ASSET.TYPE and ASSET.TYPE files are examined to locate either a MARGIN.RATE or LOSS.MARGIN.RATE If no value is found on either file then a margin rate of 0% is assumed. Validation Rules: 0 to 10 numeric characters (Optional input) |
| 3 | `SC.ABC.LOSS.MARGIN.RATE` | `AssetByCateg_LossMarginRate` | TField | No | Specifies the percentage of the asset/liability as defined by the category code to be used in portfolio valuations. This is the first level of checking when Securities programs value Accounts, Deposits or Forex deals. Depending upon whether a valuation should include/exclude liabilities, either this field or MARGIN.RATE will be used to calculate the margin value. The method of calculation is defined in the field MARGIN.VALUE in SC.PARAMETER If a value is not found on the ASSET.BY.CATEG file then the SUB.ASSET.TYPE and ASSET.TYPE files are examined to locate either a MARGIN.RATE or LOSS.MARGIN.RATE If no value is found on either file then a margin rate of 0% is assumed. Validation Rules: 0 to 10 numeric characters (Optional input) |
| 4 | `SC.ABC.TOP.UP.MARGIN` | `AssetByCateg_TopUpMargin` | TField |  | Margin rate for calculating top-up margin amount Validation Rules: Maximum of 9 numeric characters is allowed |
| 5 | `SC.ABC.SELL.OUT.MARGIN` | `AssetByCateg_SellOutMargin` | TField |  | Margin rate for calculating sell-out margin amount Validation Rules: Maximum of 9 numeric characters is allowed |
| 6 | `SC.ABC.CURRENCY` | `AssetByCateg_Currency` |  |  |  |
| 7 | `SC.ABC.CCY.SEC.MGN.RATE` | `AssetByCateg_CcySecMgnRate` |  |  |  |
| 8 | `SC.ABC.CCY.LOSS.MGN.RATE` | `AssetByCateg_CcyLossMgnRate` |  |  |  |
| 9 | `SC.ABC.ADJ.MARGIN` | `AssetByCateg_AdjMargin` | TField |  | This field is used to specify the Adjusted margin rate for calculating ADJ.MARGIN.AMT in SC.POS.ASSET. This field can either be used to specify the Low Advance Ratio for collateral calculations in Advance Collateral process or to specify the Diversified Margins for portfolios flagged for Diversification. If the field &quot;CO.MV.CHECK&quot; in SC.PARAMETER is set to &quot;YES&quot; to enable Preferential LTV functionality, Adj Margin will be used only as Low Advance Ratio in Advance Collateral process and will not be used for calculating Diversified Margin. In this case ideally Adj Margin should be lesser than the Margin Rate. Thus an override will be raised if Adj Margin is greater than Margin Rate. |
| 10 | `SC.ABC.CONCENTRATION.CAP` | `AssetByCateg_ConcentrationCap` | TField |  | Specifies the Concentration cap to be considered for the sub asset type. Concentration cap is a cap value defined for a collateral, with respect to total collateral value, to ensure that a single asset is not used extensively. Validation Rules: 1. Standard T24 Rate field with the values ranging from 0 to 100. |
| 11 | `SC.ABC.EFFECTIVE.DATE` | `AssetByCateg_EffectiveDate` |  |  |  |
| 12 | `SC.ABC.NEW.MARGIN.RATE` | `AssetByCateg_NewMarginRate` |  |  |  |
| 13 | `SC.ABC.NEW.LOSS.MARGIN.RATE` | `AssetByCateg_NewLossMarginRate` |  |  |  |
| 14 | `SC.ABC.NEW.TOP.UP.MARGIN` | `AssetByCateg_NewTopUpMargin` |  |  |  |
| 15 | `SC.ABC.NEW.SELL.OUT.MARGIN` | `AssetByCateg_NewSellOutMargin` |  |  |  |
| 16 | `SC.ABC.NEW.ADJ.MARGIN` | `AssetByCateg_NewAdjMargin` |  |  |  |
| 17 | `SC.ABC.NEW.CURRENCY` | `AssetByCateg_NewCurrency` |  |  |  |
| 18 | `SC.ABC.NEW.CCY.SEC.MGN.RATE` | `AssetByCateg_NewCcySecMgnRate` |  |  |  |
| 19 | `SC.ABC.NEW.CCY.LOSS.MGN.RATE` | `AssetByCateg_NewCcyLossMgnRate` |  |  |  |
| 20 | `SC.ABC.NEW.CCY.RESERVED.3` | `AssetByCateg_NewCcyReserved3` |  |  |  |
| 21 | `SC.ABC.NEW.CCY.RESERVED.2` | `AssetByCateg_NewCcyReserved2` |  |  |  |
| 22 | `SC.ABC.NEW.CCY.RESERVED.1` | `AssetByCateg_NewCcyReserved1` |  |  |  |
| 23 | `SC.ABC.NEW.HAIRCUT.PERC` | `AssetByCateg_NewHaircutPerc` |  |  |  |
| 24 | `SC.ABC.RESERVED.14` | `AssetByCateg_Reserved14` |  |  |  |
| 25 | `SC.ABC.RESERVED.13` | `AssetByCateg_Reserved13` |  |  |  |
| 26 | `SC.ABC.RESERVED.12` | `AssetByCateg_Reserved12` |  |  |  |
| 27 | `SC.ABC.RESERVED.11` | `AssetByCateg_Reserved11` |  |  |  |
| 28 | `SC.ABC.CCY.HAIRCUT.PERC` | `AssetByCateg_CcyHaircutPerc` | TField |  | Specifies cross currency haircut percentage to be applied on Margin Rate or Preferential Margin Rate (as applicable) and to that extent reduce the Margin Rate or Preferential Margin Rate to calculate the Low Advance Ratio that will be applied for collateral calculations in Advance Collateral process when the collateral currency and limit currency are different. Validation Rules: Standard T24 Rate field with values ranging from 0 to 100. Either Currency Haircut or Adj Margin Rate will used for LAR and thus both cannot be defined. The hierarchy in which the Currency Haircut Percentage will be considered is the same as existing Adj Margin Rate determination hierarchy. |
| 29 | `SC.ABC.RESERVED.9` | `AssetByCateg_Reserved9` | TField |  |  |
| 30 | `SC.ABC.RESERVED.8` | `AssetByCateg_Reserved8` | TField |  |  |
| 31 | `SC.ABC.RESERVED.7` | `AssetByCateg_Reserved7` | TField |  |  |
| 32 | `SC.ABC.RESERVED.6` | `AssetByCateg_Reserved6` | TField |  |  |
| 33 | `SC.ABC.RESERVED.5` | `AssetByCateg_Reserved5` | TField |  |  |
| 34 | `SC.ABC.RESERVED.4` | `AssetByCateg_Reserved4` | TField |  |  |
| 35 | `SC.ABC.RESERVED.3` | `AssetByCateg_Reserved3` | TField |  |  |
| 36 | `SC.ABC.RESERVED.2` | `AssetByCateg_Reserved2` | TField |  |  |
| 37 | `SC.ABC.OVERRIDE` | `AssetByCateg_Override` |  |  |  |
| 38 | `SC.ABC.RECORD.STATUS` | `AssetByCateg_RecordStatus` | String |  |  |
| 39 | `SC.ABC.CURR.NO` | `AssetByCateg_CurrNo` | String |  |  |
| 40 | `SC.ABC.INPUTTER` | `AssetByCateg_Inputter` |  |  |  |
| 41 | `SC.ABC.DATE.TIME` | `AssetByCateg_DateTime` |  |  |  |
| 42 | `SC.ABC.AUTHORISER` | `AssetByCateg_Authoriser` | String |  |  |
| 43 | `SC.ABC.CO.CODE` | `AssetByCateg_CoCode` | String |  |  |
| 44 | `SC.ABC.DEPT.CODE` | `AssetByCateg_DeptCode` | String |  |  |
| 45 | `SC.ABC.AUDITOR.CODE` | `AssetByCateg_AuditorCode` | String |  |  |
| 46 | `SC.ABC.AUDIT.DATE.TIME` | `AssetByCateg_AuditDateTime` | String |  |  |
