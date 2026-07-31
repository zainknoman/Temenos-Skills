# SUB.ASSET.TYPE — Table Schema

> Source: `INSERTS/I_F.SUB.ASSET.TYPE` in `ST_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CSG.DESCRIPTION` | `SubAssetType_Description` |  |  |  |
| 2 | `SC.CSG.SHORT.DESCR` | `SubAssetType_ShortDescr` |  |  |  |
| 3 | `SC.CSG.ASSET.TYPE.CODE` | `SubAssetType_AssetTypeCode` | TField | Yes | Specifies the Asset.Type that this SUB ASSET TYPE is a sub-classification of. For a new company specific record, input to this field will not be allowed. In case of after an upgrade, for an existing Company specific record, on validation the existing value will be defaulted to Null. It will not allow to input other values except Null. Validation Rules: 1 to 3 numeric character Asset.Type code. Mandatory for default records. Must exist as a valid ASSET TYPE. |
| 4 | `SC.CSG.KASSENOBLIGATIONEN` | `SubAssetType_Kassenobligationen` | TField | No | Indicates whether or not the SUB.ASSET.TYPE is a Kassenobligationen. If a new security masterfile record is being set-up and the specified SUB.ASSET.TYPE contains "YES" in this field, then the user is able to leave the MATURITY.DATE blank. Usage of this facility will necessitate your being forced to enter any Kassenobligationen trade maturity date directly onto the SEC.TRADE or other T24 security transaction. Only input of 'KASBON', 'YES' or 'NO' allowed. Optional Input. Default is NULL (meaning NO) (Optional Input) |
| 5 | `SC.CSG.YEAR.BREAKS` | `SubAssetType_YearBreaks` |  |  |  |
| 6 | `SC.CSG.SEC.MARGIN.RATE` | `SubAssetType_SecMarginRate` | TField | No | Specifies the percentage of the asset/liability as defined by the SUB.ASSET.TYPE to be used in portfolio valuations. This is the second level of checking when Securities programs value other (non securities) assets. If a value is not found on the ASSET.BY.CATEG file then this percentage rate is applied to the value of the sub-asset involved. Depending upon whether a valuation should include/exclude liabilities, either this field or LOSS.MARGIN.RATE will be used to calculate the margin value. The method of calculation is defined in the field MARGIN.VALUE in SC.PARAMETER If no value is found on either file then a margin rate of 0% is assumed. 1-5 characters Standard Rate format. Optional Input. If entered, must identify a record on the MARGIN.CONTROL file. |
| 7 | `SC.CSG.VAR.INTEREST.BONDS` | `SubAssetType_VarInterestBonds` | TField |  | Reserved for future use. |
| 8 | `SC.CSG.PRICE.TOLERANCE` | `SubAssetType_PriceTolerance` | TField |  | This is Noinputtable field. Reserved for future use. |
| 9 | `SC.CSG.CAPITAL.BOND` | `SubAssetType_CapitalBond` | TField |  | Field to indicate whether or not this SUB.ASSET.TYPE refers to capitalisation bonds. Currently this field is only used by the Bon De Caisse regional development. Only input of 'YES' or 'NO' allowed. Must be 'NO' or left blank except when the KASSENOBLIGATIONEN field is set to 'KASBON' when this can be 'YES', 'NO' of left blank. |
| 10 | `SC.CSG.LOSS.MARGIN.RATE` | `SubAssetType_LossMarginRate` | TField | No | Specifies the percentage of the asset/liability as defined by the SUB.ASSET.TYPE to be used in portfolio valuations. This is the second level of checking when Securities programs value other (non securities) assets. If a value is not found on the ASSET.BY.CATEG file then this percentage rate is applied to the value of the sub-asset involved. Depending upon whether a valuation should include/exclude liabilities, either this field or MARGIN.RATE will be used to calculate the margin value. The method of calculation is defined in the field MARGIN.VALUE in SC.PARAMETER If no value is found on either file then a margin rate of 0% is assumed. 1-5 characters Standard Rate format. Optional Input. If entered, must identify a record on the MARGIN.CONTROL file. |
| 11 | `SC.CSG.CGT.BASE.PERC` | `SubAssetType_CgtBasePerc` | TField | No | This field signifies the percentage of the CGT Base amount that will be included in the tax calculation. Optional Input Must be a percentage |
| 12 | `SC.CSG.GRP1.GRP2.METHOD` | `SubAssetType_Grp1Grp2Method` | TField | No | This field will select what gets defaulted into a SECURITY.MASTER record in the GRP1.GRP2.METHOD field. LIFO, FIFO or SUMLIFO Optional Input |
| 13 | `SC.CSG.TAX.BASIS` | `SubAssetType_TaxBasis` | TField |  | Supports EU Saving directives. LIFO, FIFO or AVERAGE |
| 14 | `SC.CSG.MF.ROUNDING.PARAM` | `SubAssetType_MfRoundingParam` | TField |  | Defines the rounding parameters for subscription, redemption and NAV Must be a valid MF.ROUNDING.PARAM record id. |
| 15 | `SC.CSG.MIN.INIT.SUBS` | `SubAssetType_MinInitSubs` | TField | No | Defines the minimum initial subscription if any in terms of amount. Optional Input.Standard T24 Amount format |
| 16 | `SC.CSG.MIN.INIT.ACTION` | `SubAssetType_MinInitAction` | TField | No | Defines whether error or override needs to be raised when minimum condition as above is not met. If MIN.INIT.SUBS is specified and this field is left blank,the system would raise override when the condition is not met. Optional Input. Allowed values are 'ERROR' or 'OVERRIDE'. Would be defauled to 'OVERRIDE' when left blank and MIN.INIT.SUBS is specified. |
| 17 | `SC.CSG.MIN.ENSUING.SUBS` | `SubAssetType_MinEnsuingSubs` | TField | No | Defines the minimum amount of subscription if customer already has a holding in the fund. Optional Input.Standard T24 Amount format |
| 18 | `SC.CSG.MIN.ENS.ACTION` | `SubAssetType_MinEnsAction` | TField | No | Defines whether error or override needs to be raised when minimum condition as above is not met. If MIN.ENSUING.SUBS is specified and this field is left blank,the system would raise override when the condition is not met. Optional Input. Allowed values are 'ERROR' or 'OVERRIDE'. Would be defauled to 'OVERRIDE' when left blank and MIN.ENSUING.SUBS is specified. |
| 19 | `SC.CSG.MINIMUM.HOLDING` | `SubAssetType_MinimumHolding` | TField | No | The minimum units that needs to be held at any point of time. While redeeming, the system would check the units being redeemed against the current holding to see whether the condition is met. Optional Input. Standard T24 nominal / amount ( NOMAMT ) format. |
| 20 | `SC.CSG.MIN.HLDG.ACTION` | `SubAssetType_MinHldgAction` | TField | No | Defines whether error or override needs to be raised when minimum condition as above is not met. If MINIMUM.HOLDING is specified and this field is left blank,the system would raise override when the condition is not met. Optional Input. Allowed values are 'ERROR' or 'OVERRIDE'. Would be defauled to 'OVERRIDE' when left blank and MINIMUM.HOLDING is specified. |
| 21 | `SC.CSG.MIN.HLDG.PERIOD` | `SubAssetType_MinHldgPeriod` | TField | No | The minimum holding period in days, months or years. At the time of redemption, the system would check whether the units being redeemed have been held for the period specified in this field. The system would check against the holdings being allocated towards the redemption Optional Input.Could be nD, nW, nM or nY where n is the number of calender days, Working days, Months or Years |
| 22 | `SC.CSG.MIN.PERIOD.ACTION` | `SubAssetType_MinPeriodAction` | TField | No | Defines whether error or override needs to be raised when minimum condition as above is not met. If MIN.HLDG.PERIOD is specified and this field is left blank,the system would raise override when the condition is not met. Optional Input. Allowed values are 'ERROR' or 'OVERRIDE'. Would be defauled to 'OVERRIDE' when left blank and MIN.HLDG.PERIOD is specified. |
| 23 | `SC.CSG.MIN.REDEMPTION` | `SubAssetType_MinRedemption` | TField | No | The minimum amount or number of units that could be redeemed at any point of time. If the holdings are less than the minimum specified here, the transaction would be allowed without any checks Optional Input. Standard T24 nominal / amount ( NOMAMT ) format. |
| 24 | `SC.CSG.MIN.REDEM.UNIT.VAL` | `SubAssetType_MinRedemUnitVal` | TField | No | Defines whether the Minimum redemption specified is in terms of value or units. If VALUE is defined here and the redemption is in terms of units, the system would convert the units into value terms at order / trade stage based on prevailing NAV and raise override/error as the case may be and vice versa. Optional Input. Allowed values are 'UNITS' or 'VALUE' |
| 25 | `SC.CSG.MIN.REDEM.ACTION` | `SubAssetType_MinRedemAction` | TField | No | Defines whether error or override needs to be raised when minimum condition as above is not met. If MIN.REDEMPTION is specified and this field is left blank,the system would raise override when the condition is not met. Optional Input. Allowed values are 'ERROR' or 'OVERRIDE'. Would be defauled to 'OVERRIDE' when left blank and MIN.REDEMPTION is specified. |
| 26 | `SC.CSG.TRANS.TYPE` | `SubAssetType_TransType` |  |  |  |
| 27 | `SC.CSG.CHARGE.CODE` | `SubAssetType_ChargeCode` |  |  |  |
| 28 | `SC.CSG.DISC.TYPE` | `SubAssetType_DiscType` |  |  |  |
| 29 | `SC.CSG.DISC.AMT` | `SubAssetType_DiscAmt` |  |  |  |
| 30 | `SC.CSG.COMP.LEVEL.ATTRIB` | `SubAssetType_CompLevelAttrib` |  |  |  |
| 31 | `SC.CSG.RISK.LEVEL` | `SubAssetType_RiskLevel` |  |  |  |
| 32 | `SC.CSG.ALLOWED.INVESTOR` | `SubAssetType_AllowedInvestor` |  |  |  |
| 33 | `SC.CSG.TOP.UP.MARGIN` | `SubAssetType_TopUpMargin` | TField |  | Margin rate for calculating top-up margin amount Maximum of 9 numeric characters is allowed |
| 34 | `SC.CSG.SELL.OUT.MARGIN` | `SubAssetType_SellOutMargin` | TField |  | Margin rate for calculating sell-out margin amount Maximum of 9 numeric characters is allowed |
| 35 | `SC.CSG.CURRENCY` | `SubAssetType_Currency` |  |  |  |
| 36 | `SC.CSG.CCY.SEC.MGN.RATE` | `SubAssetType_CcySecMgnRate` |  |  |  |
| 37 | `SC.CSG.CCY.LOSS.MGN.RATE` | `SubAssetType_CcyLossMgnRate` |  |  |  |
| 38 | `SC.CSG.ALERT.PRICE.PERC` | `SubAssetType_AlertPricePerc` | TField |  | This field accepts two numeric values. When the percentage of price change, for the security is greater than ALERT.PRICE.PERC, then an alert will be sent to the portfolio owner, if the portfolio has subscribed for price movement alert. A check will be made to this field, only when ALERT.PRICE.PERC is not defined in SECURITY.MASTER. |
| 39 | `SC.CSG.ADJ.MARGIN` | `SubAssetType_AdjMargin` | TField |  | This field is used to specify the Adjusted margin rate for calculating ADJ.MARGIN.AMT in SC.POS.ASSET. This field can either be used to specify the Low Advance Ratio for collateral calculations in Advance Collateral process or to specify the Diversified Margins for portfolios flagged for Diversification. If the field &quot;CO.MV.CHECK&quot; in SC.PARAMETER is set to &quot;YES&quot; to enable Preferential LTV functionality, Adj Margin will be used only as Low Advance Ratio in Advance Collateral process and will not be used for calculating Diversified Margin. In this case ideally Adj Margin should be lesser than the Margin Rate. Thus an override will be raised if Adj Margin is greater than Preferential Margin Rate/Standard Margin Rate. |
| 40 | `SC.CSG.STRUCTURE.NOTES` | `SubAssetType_StructureNotes` | TField |  | A value of 'YES' indicates that all instruments linked to this SUB.ASSET.TYPE are structured notes. Allowed Value - Yes, default value is NULL |
| 41 | `SC.CSG.PAY.OUT.ROUTINE` | `SubAssetType_PayOutRoutine` | TField | Yes | Specifies the enhanced margin rate that will override any standard margin (MARGIN.RATE) applicable for portfolios flagged for Diversification. Validation Rules: Standard T24 Rate field. This field is allowed for input only when &quot;CO.MV.CHECK&quot; field in SC.PARAMETER is set to &quot;YES&quot; that enables the Preferential LTV functionality. Value can be specified as an absolute value ranging from 0 to 100 or as a variance with &quot;+&quot; sign. A variance indicates the incremental value to be added to the Standrad Margin Rate to arrive at the enhanced rate. Thus Margin Rate becomes mandatory if Preferential Rate is defined as a variance. The sum of Preferential Rate defined as a variance and Standard Margin Rate cannot exceed 100. Ideally Preferential Rate should always be greater than the Standard Margin Rate. Thus an override will be raised if the Preferential Rate defined as an absolute value is lesser than the Standard Margin Rate. The hierarchy in which the Preferential Rate will be considered is the same as existing margin rate determination hierarchy. |
| 42 | `SC.CSG.CONCENTRATION.CAP` | `SubAssetType_ConcentrationCap` | TField |  | Specifies the Concentration cap to be considered for the sub asset type. Concentration cap is a cap value defined for a collateral, with respect to total collateral value, to ensure that a single asset is not used extensively. Validation Rules: 1. Standard T24 Rate field with the values ranging from 0 to 100. |
| 43 | `SC.CSG.INVEST.OBJECTIVE` | `SubAssetType_InvestObjective` |  |  |  |
| 44 | `SC.CSG.INVEST.TENOR` | `SubAssetType_InvestTenor` | TField |  | This field specifies the investment time horizon of this class of instruments Validation Rules: Input to this field is got from EB.LOOKUP table records with ID starting with TENOR*Text Input allowed up to 35 characters from EB.LOOKUP table |
| 45 | `SC.CSG.ISLAMIC.COMPLIANCE` | `SubAssetType_IslamicCompliance` | TField |  | This field indicates if this class of instruments is compliant with Islamic Sharia law Validation Rules: Allowed inputs are Yes, NO |
| 46 | `SC.CSG.INSTRUMENT.TYPE` | `SubAssetType_InstrumentType` |  |  |  |
| 47 | `SC.CSG.INST.CLASSIFICATION` | `SubAssetType_InstClassification` |  |  |  |
| 48 | `SC.CSG.EFFECTIVE.DATE` | `SubAssetType_EffectiveDate` |  |  |  |
| 49 | `SC.CSG.NEW.SEC.MARGIN.RATE` | `SubAssetType_NewSecMarginRate` |  |  |  |
| 50 | `SC.CSG.NEW.LOSS.MARGIN.RATE` | `SubAssetType_NewLossMarginRate` |  |  |  |
| 51 | `SC.CSG.NEW.TOP.UP.MARGIN` | `SubAssetType_NewTopUpMargin` |  |  |  |
| 52 | `SC.CSG.NEW.SELL.OUT.MARGIN` | `SubAssetType_NewSellOutMargin` |  |  |  |
| 53 | `SC.CSG.NEW.ADJ.MARGIN` | `SubAssetType_NewAdjMargin` |  |  |  |
| 54 | `SC.CSG.NEW.CURRENCY` | `SubAssetType_NewCurrency` |  |  |  |
| 55 | `SC.CSG.NEW.CCY.SEC.MGN.RATE` | `SubAssetType_NewCcySecMgnRate` |  |  |  |
| 56 | `SC.CSG.NEW.CCY.LOSS.MGN.RATE` | `SubAssetType_NewCcyLossMgnRate` |  |  |  |
| 57 | `SC.CSG.RESERVED10` | `SubAssetType_Reserved10` |  |  |  |
| 58 | `SC.CSG.RESERVED9` | `SubAssetType_Reserved9` |  |  |  |
| 59 | `SC.CSG.NEW.PREFNTL.MARGIN.RATE` | `SubAssetType_NewPrefntlMarginRate` |  |  |  |
| 60 | `SC.CSG.NEW.HAIRCUT.PERC` | `SubAssetType_NewHaircutPerc` |  |  |  |
| 61 | `SC.CSG.RESERVED6` | `SubAssetType_Reserved6` |  |  |  |
| 62 | `SC.CSG.RESERVED5` | `SubAssetType_Reserved5` |  |  |  |
| 63 | `SC.CSG.PREFNTL.MARGIN.RATE` | `SubAssetType_PrefntlMarginRate` | TField |  |  |
| 64 | `SC.CSG.CCY.HAIRCUT.PERC` | `SubAssetType_CcyHaircutPerc` | TField |  | Specifies cross currency haircut percentage to be applied on Margin Rate or Preferential Margin Rate (as applicable) and to that extent reduce the Margin Rate or Preferential Margin Rate to calculate the Low Advance Ratio that will be applied in the computation of CLV of collaterals when the collateral currency and limit currency are different. Validation Rules: Standard T24 Rate field with values ranging from 0 to 100. Either Currency Haircut or Adj Margin Rate will used for LAR and thus both cannot be defined. The hierarchy in which the Currency Haircut Percentage will be considered is the same as existing Adj Margin Rate determination hierarchy. |
| 65 | `SC.CSG.PERSONAL.ASSET` | `SubAssetType_PersonalAsset` | TField |  |  |
| 66 | `SC.CSG.RESERVED1` | `SubAssetType_Reserved1` |  |  |  |
| 67 | `SC.CSG.RESERVED0` | `SubAssetType_Reserved0` | TField |  |  |
| 68 | `SC.CSG.LOCAL.REF` | `SubAssetType_LocalRef` |  |  |  |
| 69 | `SC.CSG.OVERRIDE` | `SubAssetType_Override` |  |  |  |
| 70 | `SC.CSG.RECORD.STATUS` | `SubAssetType_RecordStatus` | String |  |  |
| 71 | `SC.CSG.CURR.NO` | `SubAssetType_CurrNo` | String |  |  |
| 72 | `SC.CSG.INPUTTER` | `SubAssetType_Inputter` |  |  |  |
| 73 | `SC.CSG.DATE.TIME` | `SubAssetType_DateTime` |  |  |  |
| 74 | `SC.CSG.AUTHORISER` | `SubAssetType_Authoriser` | String |  |  |
| 75 | `SC.CSG.CO.CODE` | `SubAssetType_CoCode` | String |  |  |
| 76 | `SC.CSG.DEPT.CODE` | `SubAssetType_DeptCode` | String |  |  |
| 77 | `SC.CSG.AUDITOR.CODE` | `SubAssetType_AuditorCode` | String |  |  |
| 78 | `SC.CSG.AUDIT.DATE.TIME` | `SubAssetType_AuditDateTime` | String |  |  |
