# SC.CUSTOMER.MARGIN — Table Schema

> Source: `INSERTS/I_F.SC.CUSTOMER.MARGIN` in `ST_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CUS.MAR.ASSET.CODE` | `ScCustomerMargin_AssetCode` |  |  |  |
| 2 | `SC.CUS.MAR.MARGIN.RATE` | `ScCustomerMargin_MarginRate` |  |  |  |
| 3 | `SC.CUS.MAR.LOSS.MARGIN.RAT` | `ScCustomerMargin_LossMarginRat` |  |  |  |
| 4 | `SC.CUS.MAR.TOP.UP.MARGIN` | `ScCustomerMargin_TopUpMargin` |  |  |  |
| 5 | `SC.CUS.MAR.SELL.OUT.MARGIN` | `ScCustomerMargin_SellOutMargin` |  |  |  |
| 6 | `SC.CUS.MAR.ADJ.MARGIN` | `ScCustomerMargin_AdjMargin` |  |  |  |
| 7 | `SC.CUS.MAR.HOLDING.LEVEL` | `ScCustomerMargin_HoldingLevel` |  |  |  |
| 8 | `SC.CUS.MAR.TIER.MARGIN.RATE` | `ScCustomerMargin_TierMarginRate` |  |  |  |
| 9 | `SC.CUS.MAR.TIER.ADJ.MARGIN.RATE` | `ScCustomerMargin_TierAdjMarginRate` |  |  |  |
| 10 | `SC.CUS.MAR.CONCENTRATION.CAP` | `ScCustomerMargin_ConcentrationCap` |  |  |  |
| 11 | `SC.CUS.MAR.EXPIRY.DATE` | `ScCustomerMargin_ExpiryDate` |  |  |  |
| 12 | `SC.CUS.MAR.EFFECTIVE.DATE` | `ScCustomerMargin_EffectiveDate` |  |  |  |
| 13 | `SC.CUS.MAR.NEW.MARGIN.RATE` | `ScCustomerMargin_NewMarginRate` |  |  |  |
| 14 | `SC.CUS.MAR.NEW.LOSS.MARGIN.RATE` | `ScCustomerMargin_NewLossMarginRate` |  |  |  |
| 15 | `SC.CUS.MAR.NEW.TOP.UP.MARGIN` | `ScCustomerMargin_NewTopUpMargin` |  |  |  |
| 16 | `SC.CUS.MAR.NEW.SELL.OUT.MARGIN` | `ScCustomerMargin_NewSellOutMargin` |  |  |  |
| 17 | `SC.CUS.MAR.NEW.ADJ.MARGIN` | `ScCustomerMargin_NewAdjMargin` |  |  |  |
| 18 | `SC.CUS.MAR.NEW.PREFNTL.MARGIN.RATE` | `ScCustomerMargin_NewPrefntlMarginRate` |  |  |  |
| 19 | `SC.CUS.MAR.NEW.CCY.HAIRCUT.PERC` | `ScCustomerMargin_NewCcyHaircutPerc` |  |  |  |
| 20 | `SC.CUS.MAR.RESERVED.12` | `ScCustomerMargin_Reserved12` |  |  |  |
| 21 | `SC.CUS.MAR.RESERVED.11` | `ScCustomerMargin_Reserved11` |  |  |  |
| 22 | `SC.CUS.MAR.RESERVED.10` | `ScCustomerMargin_Reserved10` |  |  |  |
| 23 | `SC.CUS.MAR.PREFNTL.MARGIN.RATE` | `ScCustomerMargin_PrefntlMarginRate` |  |  |  |
| 24 | `SC.CUS.MAR.CCY.HAIRCUT.PERC` | `ScCustomerMargin_CcyHaircutPerc` |  |  |  |
| 25 | `SC.CUS.MAR.RESERVED.7` | `ScCustomerMargin_Reserved7` |  |  |  |
| 26 | `SC.CUS.MAR.RESERVED.6` | `ScCustomerMargin_Reserved6` |  |  |  |
| 27 | `SC.CUS.MAR.RESERVED.5` | `ScCustomerMargin_Reserved5` |  |  |  |
| 28 | `SC.CUS.MAR.CUSTOMER.CCY` | `ScCustomerMargin_CustomerCcy` | TField |  | Currency in which Deficit/Surplus has to be reported. Validation Rules: A valid record from CURRENCY table. |
| 29 | `SC.CUS.MAR.CREDIT.POLICY` | `ScCustomerMargin_CreditPolicy` | TField |  | This field is used to link customer/ portfolio to rule based evaluation criteria via MV.CREDIT.POLICY to fetch the rates. When Credit Policy Id is linked, then rates for the assets will be taken from MV.CREDIT.POLICY or MV.MARGIN.RULES depending on success of rule evaluation. Validation Rules: Must be valid record in MV.CREDIT.POLICY Other fields not allowed when this field is inputted. It will be allowed for input only when APPLY.CREDIT.POLICY is set to Yes in CO.VALUATION.PARAMETER During history restore, if Credit Policy defined in this field, does not exist in MV.CREDIT.POLICY, then override will be raised |
| 30 | `SC.CUS.MAR.RESERVED3` | `ScCustomerMargin_Reserved3` | TField |  |  |
| 31 | `SC.CUS.MAR.RESERVED2` | `ScCustomerMargin_Reserved2` | TField |  |  |
| 32 | `SC.CUS.MAR.RESERVED1` | `ScCustomerMargin_Reserved1` | TField |  |  |
| 33 | `SC.CUS.MAR.LOCAL.REF` | `ScCustomerMargin_LocalRef` |  |  |  |
| 34 | `SC.CUS.MAR.OVERRIDE` | `ScCustomerMargin_Override` |  |  |  |
| 35 | `SC.CUS.MAR.RECORD.STATUS` | `ScCustomerMargin_RecordStatus` | String |  |  |
| 36 | `SC.CUS.MAR.CURR.NO` | `ScCustomerMargin_CurrNo` | String |  |  |
| 37 | `SC.CUS.MAR.INPUTTER` | `ScCustomerMargin_Inputter` |  |  |  |
| 38 | `SC.CUS.MAR.DATE.TIME` | `ScCustomerMargin_DateTime` |  |  |  |
| 39 | `SC.CUS.MAR.AUTHORISER` | `ScCustomerMargin_Authoriser` | String |  |  |
| 40 | `SC.CUS.MAR.CO.CODE` | `ScCustomerMargin_CoCode` | String |  |  |
| 41 | `SC.CUS.MAR.DEPT.CODE` | `ScCustomerMargin_DeptCode` | String |  |  |
| 42 | `SC.CUS.MAR.AUDITOR.CODE` | `ScCustomerMargin_AuditorCode` | String |  |  |
| 43 | `SC.CUS.MAR.AUDIT.DATE.TIME` | `ScCustomerMargin_AuditDateTime` | String |  |  |
