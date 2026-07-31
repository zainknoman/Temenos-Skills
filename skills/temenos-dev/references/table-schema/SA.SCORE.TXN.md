# SA.SCORE.TXN — Table Schema

> Source: `INSERTS/I_F.SA.SCORE.TXN` in `SA_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SA.ST.DESCRIPTION` | `SaScoreTxn_Description` |  |  |  |
| 2 | `SA.ST.CUSTOMER.ID` | `SaScoreTxn_CustomerId` | TField |  | Identifies the customer for whom credit scoring is done. If multiple score cards for the same product were defined, system would select the appropriate score card based on the attribute of the customer entered in this field. Validation Rules: Should be a valid record in CUSTOMER table. |
| 3 | `SA.ST.CURRENCY` | `SaScoreTxn_Currency` | TField |  | Indicates the currency in which data is gathered (in respect of amount type data) and also the currency in which exposure limit is assigned. Validation Rules: Valid record in CURRENCY table. |
| 4 | `SA.ST.SCORE.DATA` | `SaScoreTxn_ScoreData` | TField | Yes | Identifies the product for which scoring needs to be done. Based on the product selected, the data required for scoring would be defaulted by the system (as defined in SA.SCORE.DATA). Validation Rules: Only a record ID in SA.SCORE.DATA table can be input Mandatory Input |
| 5 | `SA.ST.DATA.TYPES` | `SaScoreTxn_DataTypes` |  |  |  |
| 6 | `SA.ST.DATA.VAL` | `SaScoreTxn_DataVal` |  |  |  |
| 7 | `SA.ST.DATA.TYPE.SCORE` | `SaScoreTxn_DataTypeScore` |  |  |  |
| 8 | `SA.ST.DATA.GRP` | `SaScoreTxn_DataGrp` |  |  |  |
| 9 | `SA.ST.GRP.DESC` | `SaScoreTxn_GrpDesc` |  |  |  |
| 10 | `SA.ST.GRP.VAL` | `SaScoreTxn_GrpVal` |  |  |  |
| 11 | `SA.ST.GRP.ELMT.SCORE` | `SaScoreTxn_GrpElmtScore` |  |  |  |
| 12 | `SA.ST.GRP.TOTAL` | `SaScoreTxn_GrpTotal` |  |  |  |
| 13 | `SA.ST.GRP.TYPE.SCORE` | `SaScoreTxn_GrpTypeScore` |  |  |  |
| 14 | `SA.ST.PERFORM.CALC` | `SaScoreTxn_PerformCalc` | TField | Yes | Once all the values pertaining to the customer have been entered this field may be set to YES. System would then calculate the data group totals, perform ratio calculation, select the appropriate score card, arrive at the score and assign a limit (if defined). User may change the amounts of the financial items and re-calculate the ratios each time by hitting YES in this field. Validation Rules: Only allowed values are YES and NO Mandatory Input |
| 15 | `SA.ST.ZERO.CHECK` | `SaScoreTxn_ZeroCheck` | TField |  | This field merely indicates whether the assets and liabilities match. To ensure data integrity for corporate applicants, it may be desirable to check if values for asset data types and values for liability data types match. Whether the data type is an asset or liability is indicated in SA.DATA.TYPES. System would perform this check for those data types Validation Rules: Only allowed values are BALANCED and IMBALANCE System written - no input allowed |
| 16 | `SA.ST.SA.RATIO` | `SaScoreTxn_SaRatio` |  |  |  |
| 17 | `SA.ST.RATIO.VAL` | `SaScoreTxn_RatioVal` |  |  |  |
| 18 | `SA.ST.RATIO.TYPE.SCORE` | `SaScoreTxn_RatioTypeScore` |  |  |  |
| 19 | `SA.ST.AGG.SCORE` | `SaScoreTxn_AggScore` | TField |  | The aggregate score based on the ratio values that the system has derived is written in this field. Validation Rules: System written |
| 20 | `SA.ST.LIMIT.CURRENCY` | `SaScoreTxn_LimitCurrency` | TField |  | If SASCORE.LIMIT has been defined, system would default the limit based on the score in field REC.LIMIT. The amount expressed in this field is in the currency indicated in field CURRENCY. Should the limit be granted in a different currency, the currency ID may be input in this field. Validation Rules: Must be a valid record in CURRENCY table. |
| 21 | `SA.ST.EXCH.RATE` | `SaScoreTxn_ExchRate` | TField | No | If the limit is to be granted in a different currency the exchange rate at which the system defaulted exposure or user input exposure (in field GRANT.LIMIT) must be converted must be input here. Validation Rules: Optional input. System would apply MID rate if exchange rate is not input. |
| 22 | `SA.ST.REC.LIMIT.LCY` | `SaScoreTxn_RecLimitLcy` | TField |  | Recommended limit for the aggregate score in AGG.SCORE field. Validation Rules: System Maintained Noinput field |
| 23 | `SA.ST.REC.LIMIT.FCY` | `SaScoreTxn_RecLimitFcy` | TField |  | Holds the recommeded limit in score limit currency Validation Rules: System Maintained Noinput field |
| 24 | `SA.ST.GRANT.LIMIT.LCY` | `SaScoreTxn_GrantLimitLcy` | TField | No | If the decision is to override the system defaulted exposure or input an exposure amount if no rules for limit assignment have been defined, the exposure value may be entered in this field. The value entered in this field is expressed in the currency indicated in field CURRENCY. Validation Rules: Optional input. Negative values not permitted |
| 25 | `SA.ST.GRANT.LIMIT.FCY` | `SaScoreTxn_GrantLimitFcy` | TField |  | Identifies the limit value in the currency in which limit is to be granted (as defined in field LIMIT.CURRENCY). Validation Rules: System populated. No input allowed. |
| 26 | `SA.ST.LOCAL.REF` | `SaScoreTxn_LocalRef` |  |  |  |
| 27 | `SA.ST.REC.INT.SPREAD` | `SaScoreTxn_RecIntSpread` | TField |  | Defaulted from corresponding field in SA.SCORE.LIMIT based on credit scoring Validation Rules: NOINPUT field |
| 28 | `SA.ST.REC.PRE.PAY.PERC` | `SaScoreTxn_RecPrePayPerc` | TField |  | Defaulted from corresponding field in SA.SCORE.LIMIT based on credit scoring Validation Rules: NOINPUT field |
| 29 | `SA.ST.REC.SCORE.STATUS` | `SaScoreTxn_RecScoreStatus` | TField |  | Defaulted from corresponding field in SA.SCORE.LIMIT based on credit scoring Validation Rules: NOINPUT field |
| 30 | `SA.ST.REC.EB.RATING` | `SaScoreTxn_RecEbRating` | TField |  | Defaulted from corresponding field in SA.SCORE.LIMIT based on credit scoring Validation Rules: NOINPUT field |
| 31 | `SA.ST.INTEREST.SPREAD` | `SaScoreTxn_InterestSpread` | TField |  | Used to record the Spread which could be negotiated and granted to the customer |
| 32 | `SA.ST.PRE.PAYMENT.PERC` | `SaScoreTxn_PrePaymentPerc` | TField |  | Used to record the granted Pre-payment percentage allowed |
| 33 | `SA.ST.SCORE.STATUS` | `SaScoreTxn_ScoreStatus` | TField |  | Used to record the negotiated the Score status for customers |
| 34 | `SA.ST.EB.RATING` | `SaScoreTxn_EbRating` | TField |  | Used to record the negotiated rating for the customer based on credit score |
| 35 | `SA.ST.RESERVED2` | `SaScoreTxn_Reserved2` | TField |  |  |
| 36 | `SA.ST.OVERRIDE` | `SaScoreTxn_Override` |  |  |  |
| 37 | `SA.ST.RECORD.STATUS` | `SaScoreTxn_RecordStatus` | String |  |  |
| 38 | `SA.ST.CURR.NO` | `SaScoreTxn_CurrNo` | String |  |  |
| 39 | `SA.ST.INPUTTER` | `SaScoreTxn_Inputter` |  |  |  |
| 40 | `SA.ST.DATE.TIME` | `SaScoreTxn_DateTime` |  |  |  |
| 41 | `SA.ST.AUTHORISER` | `SaScoreTxn_Authoriser` | String |  |  |
| 42 | `SA.ST.CO.CODE` | `SaScoreTxn_CoCode` | String |  |  |
| 43 | `SA.ST.DEPT.CODE` | `SaScoreTxn_DeptCode` | String |  |  |
| 44 | `SA.ST.AUDITOR.CODE` | `SaScoreTxn_AuditorCode` | String |  |  |
| 45 | `SA.ST.AUDIT.DATE.TIME` | `SaScoreTxn_AuditDateTime` | String |  |  |
