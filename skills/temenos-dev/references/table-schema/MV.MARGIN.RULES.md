# MV.MARGIN.RULES — Table Schema

> Source: `INSERTS/I_F.MV.MARGIN.RULES` in `MV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MV.MAR.DESCRIPTION` | `MvMarginRules_Description` |  |  |  |
| 2 | `MV.MAR.CRITERIA` | `MvMarginRules_Criteria` |  |  |  |
| 3 | `MV.MAR.CRITERIA.TYPE` | `MvMarginRules_CriteriaType` |  |  |  |
| 4 | `MV.MAR.OPERATION` | `MvMarginRules_Operation` |  |  |  |
| 5 | `MV.MAR.VALUE` | `MvMarginRules_Value` |  |  |  |
| 6 | `MV.MAR.VALUE.CCY` | `MvMarginRules_ValueCcy` |  |  |  |
| 7 | `MV.MAR.RESERVED.45` | `MvMarginRules_Reserved45` |  |  |  |
| 8 | `MV.MAR.RESERVED.44` | `MvMarginRules_Reserved44` |  |  |  |
| 9 | `MV.MAR.RESERVED.43` | `MvMarginRules_Reserved43` |  |  |  |
| 10 | `MV.MAR.RESERVED.42` | `MvMarginRules_Reserved42` |  |  |  |
| 11 | `MV.MAR.RESERVED.41` | `MvMarginRules_Reserved41` |  |  |  |
| 12 | `MV.MAR.JOINTS` | `MvMarginRules_Joints` |  |  |  |
| 13 | `MV.MAR.LEVEL` | `MvMarginRules_Level` |  |  |  |
| 14 | `MV.MAR.MARGIN.RATE` | `MvMarginRules_MarginRate` |  |  |  |
| 15 | `MV.MAR.ADJ.MARGIN.RATE` | `MvMarginRules_AdjMarginRate` |  |  |  |
| 16 | `MV.MAR.PREFNTL.MARGIN.RATE` | `MvMarginRules_PrefntlMarginRate` |  |  |  |
| 17 | `MV.MAR.RESERVED.40` | `MvMarginRules_Reserved40` |  |  |  |
| 18 | `MV.MAR.RESERVED.39` | `MvMarginRules_Reserved39` |  |  |  |
| 19 | `MV.MAR.EFFECTIVE.DATE` | `MvMarginRules_EffectiveDate` |  |  |  |
| 20 | `MV.MAR.NEW.MARGIN.RATE` | `MvMarginRules_NewMarginRate` |  |  |  |
| 21 | `MV.MAR.NEW.ADJ.MARGIN.RATE` | `MvMarginRules_NewAdjMarginRate` |  |  |  |
| 22 | `MV.MAR.NEW.PREFNTL.MARGIN.RATE` | `MvMarginRules_NewPrefntlMarginRate` |  |  |  |
| 23 | `MV.MAR.RESERVED.38` | `MvMarginRules_Reserved38` |  |  |  |
| 24 | `MV.MAR.RESERVED.37` | `MvMarginRules_Reserved37` |  |  |  |
| 25 | `MV.MAR.RESERVED.36` | `MvMarginRules_Reserved36` |  |  |  |
| 26 | `MV.MAR.RESERVED.35` | `MvMarginRules_Reserved35` |  |  |  |
| 27 | `MV.MAR.RESERVED.34` | `MvMarginRules_Reserved34` |  |  |  |
| 28 | `MV.MAR.RESERVED.33` | `MvMarginRules_Reserved33` |  |  |  |
| 29 | `MV.MAR.RESERVED.32` | `MvMarginRules_Reserved32` |  |  |  |
| 30 | `MV.MAR.RESERVED.31` | `MvMarginRules_Reserved31` |  |  |  |
| 31 | `MV.MAR.CAP.TYPE` | `MvMarginRules_CapType` |  |  |  |
| 32 | `MV.MAR.RESERVED.46` | `MvMarginRules_Reserved46` |  |  |  |
| 33 | `MV.MAR.CAP.VALUE` | `MvMarginRules_CapValue` |  |  |  |
| 34 | `MV.MAR.CAP.VALUE.CCY` | `MvMarginRules_CapValueCcy` |  |  |  |
| 35 | `MV.MAR.RESERVED.30` | `MvMarginRules_Reserved30` |  |  |  |
| 36 | `MV.MAR.RESERVED.29` | `MvMarginRules_Reserved29` |  |  |  |
| 37 | `MV.MAR.RESERVED.28` | `MvMarginRules_Reserved28` |  |  |  |
| 38 | `MV.MAR.RESERVED.27` | `MvMarginRules_Reserved27` |  |  |  |
| 39 | `MV.MAR.RESERVED.26` | `MvMarginRules_Reserved26` |  |  |  |
| 40 | `MV.MAR.CRITERIA.NAME` | `MvMarginRules_CriteriaName` |  |  |  |
| 41 | `MV.MAR.CRITERIA.APPLN` | `MvMarginRules_CriteriaAppln` |  |  |  |
| 42 | `MV.MAR.CRITERIA.FIELD` | `MvMarginRules_CriteriaField` |  |  |  |
| 43 | `MV.MAR.ADDL.CRITERIA.FIELD` | `MvMarginRules_AddlCriteriaField` |  |  |  |
| 44 | `MV.MAR.MULTI.VAL.CRITERIA.HOOK` | `MvMarginRules_MultiValCriteriaHook` |  |  |  |
| 45 | `MV.MAR.RESERVED.25` | `MvMarginRules_Reserved25` |  |  |  |
| 46 | `MV.MAR.RESERVED.24` | `MvMarginRules_Reserved24` |  |  |  |
| 47 | `MV.MAR.RESERVED.23` | `MvMarginRules_Reserved23` |  |  |  |
| 48 | `MV.MAR.RESERVED.22` | `MvMarginRules_Reserved22` |  |  |  |
| 49 | `MV.MAR.RESERVED.21` | `MvMarginRules_Reserved21` |  |  |  |
| 50 | `MV.MAR.RESERVED.20` | `MvMarginRules_Reserved20` |  |  |  |
| 51 | `MV.MAR.RESERVED.19` | `MvMarginRules_Reserved19` |  |  |  |
| 52 | `MV.MAR.RESERVED.18` | `MvMarginRules_Reserved18` |  |  |  |
| 53 | `MV.MAR.RESERVED.17` | `MvMarginRules_Reserved17` |  |  |  |
| 54 | `MV.MAR.RESERVED.16` | `MvMarginRules_Reserved16` |  |  |  |
| 55 | `MV.MAR.DEFAULT.MARGIN.RATE` | `MvMarginRules_DefaultMarginRate` | TField |  | This field will specify the default Margin Rate(HAR) in case the criteria defined does not satisfy for a given asset. Validation Rules: The Rate should be in the range 0 to 100. |
| 56 | `MV.MAR.DEFAULT.ADJ.MARGIN.RATE` | `MvMarginRules_DefaultAdjMarginRate` | TField | Yes | This field will specify the default Adjusted Margin Rate(LAR) in case the criteria defined does not satisfy a given asset. Validation Rules: Allow the option '-' .When the Default Adjusted Margin Rate is defined with '-' then MARGIN.RATE / DEFAULT.MARGIN.RATE is mandatory. The Rate should be in the range 0 to 100. |
| 57 | `MV.MAR.DEFAULT.PREFNTL.MARGIN.RATE` | `MvMarginRules_DefaultPrefntlMarginRate` | TField | Yes | This field will specify the default Preferential Margin Rate in case the criteria(s) defined does not match/satisfy for a given asset. Validation Rules: Should be in the range 0 to 100 or with a variance sign '+'. When it is defined with '+' sign then Default margin Rate or margin rate within the criteria is Mandatory. The sum of the Default preferential rate and Default margin rate or Margin rate within the criteria should not exceed 100. When the Default preferential rate defined without variance is less than Default margin rate or margin rate within criteria, then override should be raised. |
| 58 | `MV.MAR.DEFAULT.LOSS.MARGIN.RATE` | `MvMarginRules_DefaultLossMarginRate` | TField |  | This field will specify the Default Loss Margin Rate. |
| 59 | `MV.MAR.DEFAULT.TOP.UP.MARGIN` | `MvMarginRules_DefaultTopUpMargin` | TField |  | This field will specify the Default Top Up Margin rate. |
| 60 | `MV.MAR.DEFAULT.SELL.OUT.MARGIN` | `MvMarginRules_DefaultSellOutMargin` | TField |  | This field will specify the Default Sell Out Margin Rate. |
| 61 | `MV.MAR.DEFAULT.CONC.CAP` | `MvMarginRules_DefaultConcCap` | TField |  | This field will specify the Default Concentration Cap for the given asset. Validation Rules: The Rate should be in the range 0 to 100. |
| 62 | `MV.MAR.DEF.RATES.EFFECT.DATE` | `MvMarginRules_DefRatesEffectDate` |  |  |  |
| 63 | `MV.MAR.NEW.DEF.MARGIN.RATE` | `MvMarginRules_NewDefMarginRate` |  |  |  |
| 64 | `MV.MAR.NEW.DEF.ADJ.MARGIN.RATE` | `MvMarginRules_NewDefAdjMarginRate` |  |  |  |
| 65 | `MV.MAR.NEW.DEF.PREF.MARGIN.RATE` | `MvMarginRules_NewDefPrefMarginRate` |  |  |  |
| 66 | `MV.MAR.NEW.DEF.LOSS.MARGIN.RATE` | `MvMarginRules_NewDefLossMarginRate` |  |  |  |
| 67 | `MV.MAR.NEW.DEF.TOP.UP.MARGIN` | `MvMarginRules_NewDefTopUpMargin` |  |  |  |
| 68 | `MV.MAR.NEW.DEF.SELL.OUT.MARGIN` | `MvMarginRules_NewDefSellOutMargin` |  |  |  |
| 69 | `MV.MAR.RESERVED.15` | `MvMarginRules_Reserved15` |  |  |  |
| 70 | `MV.MAR.RESERVED.14` | `MvMarginRules_Reserved14` |  |  |  |
| 71 | `MV.MAR.RESERVED.13` | `MvMarginRules_Reserved13` |  |  |  |
| 72 | `MV.MAR.RESERVED.12` | `MvMarginRules_Reserved12` |  |  |  |
| 73 | `MV.MAR.RESERVED.11` | `MvMarginRules_Reserved11` |  |  |  |
| 74 | `MV.MAR.START.DATE` | `MvMarginRules_StartDate` | TField |  | Date from which the Margin Rules record is effective. Validation Rules: Valid T24 date. Default to Today date if it is not defined. |
| 75 | `MV.MAR.EXPIRY.DATE` | `MvMarginRules_ExpiryDate` | TField |  | Date at which the Margin Rule record will expire. Validation Rules: Valid T24 date. Expiry Date cannot be less than or equal to Start Date and cannot be less than Today. Override check , Expiry date is equal to today's date |
| 76 | `MV.MAR.CREDIT.POLICY.ID` | `MvMarginRules_CreditPolicyId` |  |  |  |
| 77 | `MV.MAR.RESERVED.10` | `MvMarginRules_Reserved10` | TField |  |  |
| 78 | `MV.MAR.RESERVED.9` | `MvMarginRules_Reserved9` | TField |  |  |
| 79 | `MV.MAR.RESERVED.8` | `MvMarginRules_Reserved8` | TField |  |  |
| 80 | `MV.MAR.RESERVED.7` | `MvMarginRules_Reserved7` | TField |  |  |
| 81 | `MV.MAR.RESERVED.6` | `MvMarginRules_Reserved6` | TField |  |  |
| 82 | `MV.MAR.RESERVED.5` | `MvMarginRules_Reserved5` | TField |  |  |
| 83 | `MV.MAR.RESERVED.4` | `MvMarginRules_Reserved4` | TField |  |  |
| 84 | `MV.MAR.RESERVED.3` | `MvMarginRules_Reserved3` | TField |  |  |
| 85 | `MV.MAR.RESERVED.2` | `MvMarginRules_Reserved2` | TField |  |  |
| 86 | `MV.MAR.RESERVED.1` | `MvMarginRules_Reserved1` | TField |  |  |
| 87 | `MV.MAR.LOCAL.REF` | `MvMarginRules_LocalRef` |  |  |  |
| 88 | `MV.MAR.OVERRIDE` | `MvMarginRules_Override` |  |  |  |
| 89 | `MV.MAR.RECORD.STATUS` | `MvMarginRules_RecordStatus` | String |  |  |
| 90 | `MV.MAR.CURR.NO` | `MvMarginRules_CurrNo` | String |  |  |
| 91 | `MV.MAR.INPUTTER` | `MvMarginRules_Inputter` |  |  |  |
| 92 | `MV.MAR.DATE.TIME` | `MvMarginRules_DateTime` |  |  |  |
| 93 | `MV.MAR.AUTHORISER` | `MvMarginRules_Authoriser` | String |  |  |
| 94 | `MV.MAR.CO.CODE` | `MvMarginRules_CoCode` | String |  |  |
| 95 | `MV.MAR.DEPT.CODE` | `MvMarginRules_DeptCode` | String |  |  |
| 96 | `MV.MAR.AUDITOR.CODE` | `MvMarginRules_AuditorCode` | String |  |  |
| 97 | `MV.MAR.AUDIT.DATE.TIME` | `MvMarginRules_AuditDateTime` | String |  |  |
