# MARGIN.CONTROL — Table Schema

> Source: `INSERTS/I_F.MARGIN.CONTROL` in `SC_ScvConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.MAR.DESCRIPTION` | `MarginControl_Description` |  |  |  |
| 2 | `SC.MAR.SHORT.DESCR` | `MarginControl_ShortDescr` |  |  |  |
| 3 | `SC.MAR.MARGIN.RATE` | `MarginControl_MarginRate` | TField | Yes | Specifies the MARGIN.RATE that will apply to a Security, where the ID of this record is entered in the MARGIN.CONTROL field of the SECURITY.MASTER record. It is envisaged for example that an ID of say 75 indicates to the user and the system that approx.75% of the market estimation of the holding in a given security is sufficient "Collateral" for lending purposes. On a client's "Margin Valuation" this estimation will be displayed against the market estimation for comparison purposes. It will be further evaluated at the summary page, where an internal limit can be entered and available or excess funds illustrated. Validation Rules: 1-5 numeric or "." characters. (Mandatory Input) |
| 4 | `SC.MAR.TOP.UP.MARGIN` | `MarginControl_TopUpMargin` | TField |  | Margin rate for calculating top-up margin amount Validation Rules: Maximum of 9 numeric characters is allowed |
| 5 | `SC.MAR.SELL.OUT.MARGIN` | `MarginControl_SellOutMargin` | TField |  | Margin rate for calculating sell-out margin amount Validation Rules: Maximum of 9 numeric characters is allowed |
| 6 | `SC.MAR.ADJ.MARGIN` | `MarginControl_AdjMargin` | TField |  | This field is used to specify the Adjusted margin rate for calculating ADJ.MARGIN.AMT in SC.POS.ASSET. This field can either be used to specify the Low Advance Ratio for collateral calculations in Advance Collateral process or to specify the Diversified Margins for portfolios flagged for Diversification. If the field &quot;CO.MV.CHECK&quot; in SC.PARAMETER is set to &quot;YES&quot; to enable Preferential LTV functionality, Adj Margin will be used only as Low Advance Ratio in Advance Collateral process and will not be used for calculating Diversified Margin. In this case ideally Adj Margin should be lesser than the Margin Rate. Thus an override will be raised if Adj Margin is greater than Preferential Margin Rate/Standard Margin Rate. a. If ADJ.MARGIN is used for diversification purpose and bank wants to use both concentration and portfolio diversification functionality then, it will require a process change configurationso as to setup and use ADJ.MARGIN.RATE for concentration and PREFNTL.MARGIN.RATE for diversification and also set the field CO.MV.CHECK in SC.PARAMETER as YES. b. If ADJ.MARGIN is used for concentration purpose and bank wants to use portfolio diversification functionality then, it will require configuring field CO.MV.CHECK in SC.PARAMETER as YESand setup PREFNTL.MARGIN.RATE to be used for diversification. |
| 7 | `SC.MAR.LOSS.MARGIN.RATE` | `MarginControl_LossMarginRate` | TField |  |  |
| 8 | `SC.MAR.EFFECTIVE.DATE` | `MarginControl_EffectiveDate` |  |  |  |
| 9 | `SC.MAR.NEW.MARGIN.RATE` | `MarginControl_NewMarginRate` |  |  |  |
| 10 | `SC.MAR.NEW.TOP.UP.MARGIN` | `MarginControl_NewTopUpMargin` |  |  |  |
| 11 | `SC.MAR.NEW.SELL.OUT.MARGIN` | `MarginControl_NewSellOutMargin` |  |  |  |
| 12 | `SC.MAR.NEW.ADJ.MARGIN` | `MarginControl_NewAdjMargin` |  |  |  |
| 13 | `SC.MAR.NEW.LOSS.MARGIN.RATE` | `MarginControl_NewLossMarginRate` |  |  |  |
| 14 | `SC.MAR.NEW.PREFNTL.MARGIN.RATE` | `MarginControl_NewPrefntlMarginRate` |  |  |  |
| 15 | `SC.MAR.NEW.CCY.HAIRCUT.PERC` | `MarginControl_NewCcyHaircutPerc` |  |  |  |
| 16 | `SC.MAR.RESERVED.13` | `MarginControl_Reserved13` |  |  |  |
| 17 | `SC.MAR.RESERVED.12` | `MarginControl_Reserved12` |  |  |  |
| 18 | `SC.MAR.RESERVED.11` | `MarginControl_Reserved11` |  |  |  |
| 19 | `SC.MAR.PREFNTL.MARGIN.RATE` | `MarginControl_PrefntlMarginRate` | TField | Yes | Specifies the enhanced margin rate that will override any standard margin (MARGIN.RATE) applicable for portfolios flagged for Diversification. Validation Rules: Standard T24 Rate field. This field is allowed for input only when &quot;CO.MV.CHECK&quot; field in SC.PARAMETER is set to "YES" that enables the Preferential LTV functionality. Value can be specified as an absolute value ranging from 0 to 100 or as a variance with &quot;+&quot; sign. A variance indicates the incremental value to be added to the Standrad Margin Rate to arrive at the enhanced rate. Thus Margin Rate becomes mandatory if Preferential Rate is defined as a variance. The sum of Preferential Rate defined as a variance and Standard Margin Rate cannot exceed 100. Ideally Preferential Rate should always be greater than the Standard Margin Rate. Thus an override will be raised if the Preferential Rate defined as an absolute value is lesser than the Standard Margin Rate. The hierarchy in which the Preferential Rate will be considered is the same as existing margin rate determination hierarchy. |
| 20 | `SC.MAR.CCY.HAIRCUT.PERC` | `MarginControl_CcyHaircutPerc` | TField |  | Specifies cross currency haircut percentage to be applied on Margin Rate or Preferential Margin Rate (as applicable) and to that extent reduce the Margin Rate or Preferential Margin Rate to calculate the Low Advance Ratio that will be applied for collateral calculations in Advance Collateral process when the collateral currency and limit currency are different. Validation Rules: Standard T24 Rate field with values ranging from 0 to 100. Either Currency Haircut or Adj Margin Rate will used for LAR and thus both cannot be defined. The hierarchy in which the Currency Haircut Percentage will be considered is the same as existing Adj Margin Rate determination hierarchy. |
| 21 | `SC.MAR.RESERVED8` | `MarginControl_Reserved8` | TField |  |  |
| 22 | `SC.MAR.RESERVED7` | `MarginControl_Reserved7` | TField |  |  |
| 23 | `SC.MAR.RESERVED6` | `MarginControl_Reserved6` | TField |  |  |
| 24 | `SC.MAR.RESERVED5` | `MarginControl_Reserved5` | TField |  |  |
| 25 | `SC.MAR.RESERVED4` | `MarginControl_Reserved4` | TField |  |  |
| 26 | `SC.MAR.RESERVED3` | `MarginControl_Reserved3` | TField |  |  |
| 27 | `SC.MAR.LOCAL.REF` | `MarginControl_LocalRef` |  |  |  |
| 28 | `SC.MAR.OVERRIDE` | `MarginControl_Override` |  |  |  |
| 29 | `SC.MAR.RECORD.STATUS` | `MarginControl_RecordStatus` | String |  |  |
| 30 | `SC.MAR.CURR.NO` | `MarginControl_CurrNo` | String |  |  |
| 31 | `SC.MAR.INPUTTER` | `MarginControl_Inputter` |  |  |  |
| 32 | `SC.MAR.DATE.TIME` | `MarginControl_DateTime` |  |  |  |
| 33 | `SC.MAR.AUTHORISER` | `MarginControl_Authoriser` | String |  |  |
| 34 | `SC.MAR.CO.CODE` | `MarginControl_CoCode` | String |  |  |
| 35 | `SC.MAR.DEPT.CODE` | `MarginControl_DeptCode` | String |  |  |
| 36 | `SC.MAR.AUDITOR.CODE` | `MarginControl_AuditorCode` | String |  |  |
| 37 | `SC.MAR.AUDIT.DATE.TIME` | `MarginControl_AuditDateTime` | String |  |  |
