# MV.CREDIT.POLICY — Table Schema

> Source: `INSERTS/I_F.MV.CREDIT.POLICY` in `MV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MV.CP.DESCRIPTION` | `MvCreditPolicy_Description` |  |  |  |
| 2 | `MV.CP.LTV.RULES` | `MvCreditPolicy_LtvRules` |  |  |  |
| 3 | `MV.CP.ASSET.CLASS` | `MvCreditPolicy_AssetClass` |  |  |  |
| 4 | `MV.CP.RESERVED.30` | `MvCreditPolicy_Reserved30` |  |  |  |
| 5 | `MV.CP.RESERVED.29` | `MvCreditPolicy_Reserved29` |  |  |  |
| 6 | `MV.CP.RESERVED.28` | `MvCreditPolicy_Reserved28` |  |  |  |
| 7 | `MV.CP.RESERVED.27` | `MvCreditPolicy_Reserved27` |  |  |  |
| 8 | `MV.CP.RESERVED.26` | `MvCreditPolicy_Reserved26` |  |  |  |
| 9 | `MV.CP.DEFAULT.MARGIN.RATE` | `MvCreditPolicy_DefaultMarginRate` | TField | Yes | This field specifies the Default Margin Rate / HAR to be applied when no rule is satisfied in MV.MARGIN.RULE for an asset. Validation rules: The Margin rate should be in the range 0 to 100.Mandatory Field. |
| 10 | `MV.CP.DEFAULT.ADJ.MARGIN.RATE` | `MvCreditPolicy_DefaultAdjMarginRate` | TField | Yes | This field specifies the Default Adj Margin Rate / LAR to be applied when no rule is satisfied in MV.MARGIN.RULE for an asset. Validation rules: The Margin rate should be in the range 0 to 100 both with variance (-) and without variance.Mandatory when CCY.PAIR is defined. |
| 11 | `MV.CP.DEFAULT.PREFNTL.MARGIN.RATE` | `MvCreditPolicy_DefaultPrefntlMarginRate` | TField | Yes | This field specifies the Default Preferential Margin to be applied when no rule is satisfied in MV.MARGIN.RULE for an asset. Validation rules: The Preferential Margin Rate should be in the range 0 to 100 or with a variance sign '+'. When it is defined with '+' sign then Margin Rate is Mandatory. The sum of the Preferential rate and Margin rate should not exceed 100. When the Preferential rate defined without variance is less than Margin rate, then override should be raised. |
| 12 | `MV.CP.DEFAULT.LOSS.MARGIN.RATE` | `MvCreditPolicy_DefaultLossMarginRate` | TField |  | This field specifies the Default Loss Margin to be applied when no rule is satisfied in MV.MARGIN.RULE for an asset. |
| 13 | `MV.CP.DEFAULT.TOP.UP.MARGIN.RATE` | `MvCreditPolicy_DefaultTopUpMarginRate` | TField |  | This field specifies the Default Top Up Margin to be applied when no rule is satisfied in MV.MARGIN.RULE for an asset. |
| 14 | `MV.CP.DEFAULT.SELL.OUT.MARGIN.RATE` | `MvCreditPolicy_DefaultSellOutMarginRate` | TField |  | This field specifies the Default Sell Out Margin to be applied when no rule is satisfied in MV.MARGIN.RULE for an asset. |
| 15 | `MV.CP.DEFAULT.CONC.CAP` | `MvCreditPolicy_DefaultConcCap` | TField |  | This field specifies the Default Single Concentration cap to be applied when no rule is satisfied in MV.MARGIN.RULE for an asset. Validation rules: The Percentage should be in the range 0 to 100. |
| 16 | `MV.CP.CCY.PAIR.PERC` | `MvCreditPolicy_CcyPairPerc` |  |  |  |
| 17 | `MV.CP.ASSET.CCY` | `MvCreditPolicy_AssetCcy` |  |  |  |
| 18 | `MV.CP.LIAB.CCY` | `MvCreditPolicy_LiabCcy` |  |  |  |
| 19 | `MV.CP.RESERVED.25` | `MvCreditPolicy_Reserved25` |  |  |  |
| 20 | `MV.CP.RESERVED.24` | `MvCreditPolicy_Reserved24` |  |  |  |
| 21 | `MV.CP.RESERVED.23` | `MvCreditPolicy_Reserved23` |  |  |  |
| 22 | `MV.CP.RESERVED.22` | `MvCreditPolicy_Reserved22` |  |  |  |
| 23 | `MV.CP.RESERVED.21` | `MvCreditPolicy_Reserved21` |  |  |  |
| 24 | `MV.CP.RESERVED.20` | `MvCreditPolicy_Reserved20` |  |  |  |
| 25 | `MV.CP.RESERVED.19` | `MvCreditPolicy_Reserved19` |  |  |  |
| 26 | `MV.CP.RESERVED.18` | `MvCreditPolicy_Reserved18` |  |  |  |
| 27 | `MV.CP.RESERVED.17` | `MvCreditPolicy_Reserved17` |  |  |  |
| 28 | `MV.CP.RESERVED.16` | `MvCreditPolicy_Reserved16` |  |  |  |
| 29 | `MV.CP.EFFECTIVE.DATE` | `MvCreditPolicy_EffectiveDate` |  |  |  |
| 30 | `MV.CP.NEW.DEF.MARGIN.RATE` | `MvCreditPolicy_NewDefMarginRate` |  |  |  |
| 31 | `MV.CP.NEW.DEF.ADJ.MARGIN.RATE` | `MvCreditPolicy_NewDefAdjMarginRate` |  |  |  |
| 32 | `MV.CP.NEW.DEF.PREF.MARGIN.RATE` | `MvCreditPolicy_NewDefPrefMarginRate` |  |  |  |
| 33 | `MV.CP.NEW.DEF.LOSS.MARGIN.RATE` | `MvCreditPolicy_NewDefLossMarginRate` |  |  |  |
| 34 | `MV.CP.NEW.DEF.TOP.UP.MARGIN.RATE` | `MvCreditPolicy_NewDefTopUpMarginRate` |  |  |  |
| 35 | `MV.CP.NEW.DEF.SELL.OUT.MARGIN.RATE` | `MvCreditPolicy_NewDefSellOutMarginRate` |  |  |  |
| 36 | `MV.CP.RESERVED.15` | `MvCreditPolicy_Reserved15` |  |  |  |
| 37 | `MV.CP.RESERVED.14` | `MvCreditPolicy_Reserved14` |  |  |  |
| 38 | `MV.CP.RESERVED.13` | `MvCreditPolicy_Reserved13` |  |  |  |
| 39 | `MV.CP.RESERVED.12` | `MvCreditPolicy_Reserved12` |  |  |  |
| 40 | `MV.CP.RESERVED.11` | `MvCreditPolicy_Reserved11` |  |  |  |
| 41 | `MV.CP.REPORTING.CCY` | `MvCreditPolicy_ReportingCcy` | TField |  | This field will hold the currency used for reporting the collateral deficit. If not defined then local currency will be used to report deficit. |
| 42 | `MV.CP.REVIEW.FREQUENCY` | `MvCreditPolicy_ReviewFrequency` | TField |  | This field defines the frequency when credit policy is to be reviewed |
| 43 | `MV.CP.START.DATE` | `MvCreditPolicy_StartDate` | TField |  | The Date from which Credit Policy will be effective Validation rules: Valid T24 date. Default to Today date if it is not defined. |
| 44 | `MV.CP.EXPIRY.DATE` | `MvCreditPolicy_ExpiryDate` | TField |  | The Date from which Credit Policy will expire Validation rules: Valid T24 date. Expiry Date cannot be less than or equal to Start Date or back dated. |
| 45 | `MV.CP.RESERVED.10` | `MvCreditPolicy_Reserved10` | TField |  |  |
| 46 | `MV.CP.RESERVED.9` | `MvCreditPolicy_Reserved9` | TField |  |  |
| 47 | `MV.CP.RESERVED.8` | `MvCreditPolicy_Reserved8` | TField |  |  |
| 48 | `MV.CP.RESERVED.7` | `MvCreditPolicy_Reserved7` | TField |  |  |
| 49 | `MV.CP.RESERVED.6` | `MvCreditPolicy_Reserved6` | TField |  |  |
| 50 | `MV.CP.RESERVED.5` | `MvCreditPolicy_Reserved5` | TField |  |  |
| 51 | `MV.CP.RESERVED.4` | `MvCreditPolicy_Reserved4` | TField |  |  |
| 52 | `MV.CP.RESERVED.3` | `MvCreditPolicy_Reserved3` | TField |  |  |
| 53 | `MV.CP.RESERVED.2` | `MvCreditPolicy_Reserved2` | TField |  |  |
| 54 | `MV.CP.RESERVED.1` | `MvCreditPolicy_Reserved1` | TField |  |  |
| 55 | `MV.CP.LOCAL.REF` | `MvCreditPolicy_LocalRef` |  |  |  |
| 56 | `MV.CP.OVERRIDE` | `MvCreditPolicy_Override` |  |  |  |
| 57 | `MV.CP.RECORD.STATUS` | `MvCreditPolicy_RecordStatus` | String |  |  |
| 58 | `MV.CP.CURR.NO` | `MvCreditPolicy_CurrNo` | String |  |  |
| 59 | `MV.CP.INPUTTER` | `MvCreditPolicy_Inputter` |  |  |  |
| 60 | `MV.CP.DATE.TIME` | `MvCreditPolicy_DateTime` |  |  |  |
| 61 | `MV.CP.AUTHORISER` | `MvCreditPolicy_Authoriser` | String |  |  |
| 62 | `MV.CP.CO.CODE` | `MvCreditPolicy_CoCode` | String |  |  |
| 63 | `MV.CP.DEPT.CODE` | `MvCreditPolicy_DeptCode` | String |  |  |
| 64 | `MV.CP.AUDITOR.CODE` | `MvCreditPolicy_AuditorCode` | String |  |  |
| 65 | `MV.CP.AUDIT.DATE.TIME` | `MvCreditPolicy_AuditDateTime` | String |  |  |
