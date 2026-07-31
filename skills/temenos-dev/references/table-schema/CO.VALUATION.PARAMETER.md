# CO.VALUATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CO.VALUATION.PARAMETER` in `MV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COVP.USE.ADVANCE.RATIO` | `CoValuationParameter_UseAdvanceRatio` | TField |  | When this field is set to Yes, Collateral execution value will be calculated based on the MARGIN.RATE defined for the linked asset at various levels. If the user doesn't wish to calculate the margin rates, this field can be set to No. |
| 2 | `COVP.ACCOUNT.AS.LIAB` | `CoValuationParameter_AccountAsLiab` | TField |  | Accounts linked to Limits with negative balance will be considered as Liabilities when calculating the Collateral deficit value if this field is set to Yes. |
| 3 | `COVP.UPDATE.ONLINE` | `CoValuationParameter_UpdateOnline` | TField |  | An options field, if set to "YES" - Advance Ratio setup will be considered while calculating collateral value online. If set to "NO" - Advance ratio processing will be considered only during COB. |
| 4 | `COVP.CONC.CAP.LEVEL` | `CoValuationParameter_ConcCapLevel` |  |  |  |
| 5 | `COVP.STD.MAX.CONC.CAP` | `CoValuationParameter_StdMaxConcCap` | TField | No | A standard single concentration cap which will be applied when single cap is not defined at the asset level. Validation Rules: New optional field. Any input should be a number from 0 to 100. Any other input is be allowed. |
| 6 | `COVP.BOND.RANKING` | `CoValuationParameter_BondRanking` |  |  |  |
| 7 | `COVP.BOND.CAP` | `CoValuationParameter_BondCap` |  |  |  |
| 8 | `COVP.NO.CONC.CAP` | `CoValuationParameter_NoConcCap` |  |  |  |
| 9 | `COVP.AR.DROP.ALERT` | `CoValuationParameter_ArDropAlert` | TField |  | An options field to define whether an alert is required when there is reduction in collateral value due to change in the Margin rate and Adj Margin rates (High Advance ratio and Low Advance ratio) Validation Rules: 1. Valid values are YES_NO |
| 10 | `COVP.APPLY.GROUP.CAP` | `CoValuationParameter_ApplyGroupCap` | TField |  | An options field to define whether the group cap has to be applied before allocation or after allocation. Validation Rules: 1. Valid values are BEFORE ALLOC_AFTER ALLOC |
| 11 | `COVP.DISC.PORTFOLIO` | `CoValuationParameter_DiscPortfolio` |  |  |  |
| 12 | `COVP.CO.ALLOCATION` | `CoValuationParameter_CoAllocation` | TField | No | Specifies if the collaterals have to be allocated against the Limits or Liabilities. If &quot;LIMITS&quot; is specified in this field, then the collaterals will be allocated against each Limit specific to the Customer. If Null or &quot;CONTRACTS&quot; is specified in this field, then the collaterals will be allocated against each Liability linked to the Limits specific to the Customer Validation Rules: Optional field. Valid values are Null, LIMITS and CONTRACTS. |
| 13 | `COVP.EXCL.COLLATERAL.TYPE` | `CoValuationParameter_ExclCollateralType` |  |  |  |
| 14 | `COVP.NO.PORT.VALUATION` | `CoValuationParameter_NoPortValuation` | TField |  | Flag to indicate if Collaterals to which a portfolio is pledged should be excluded from Advance Collateral process. Validation Rules: Valid values are &quot;YES&quot; and NULL |
| 15 | `COVP.PF.QUAL.CCY` | `CoValuationParameter_PfQualCcy` | TField |  | Defines the Currency in which the Threshold value for applying concentartion cap is given. Validation Rules: Input allowed only when INCL.CLV.CAP field is set in SC.PARAMETER. |
| 16 | `COVP.LOCAL.REF` | `CoValuationParameter_LocalRef` |  |  |  |
| 17 | `COVP.OVERRIDE` | `CoValuationParameter_Override` |  |  |  |
| 18 | `COVP.RECORD.STATUS` | `CoValuationParameter_RecordStatus` | String |  |  |
| 19 | `COVP.CURR.NO` | `CoValuationParameter_CurrNo` | String |  |  |
| 20 | `COVP.INPUTTER` | `CoValuationParameter_Inputter` |  |  |  |
| 21 | `COVP.DATE.TIME` | `CoValuationParameter_DateTime` |  |  |  |
| 22 | `COVP.AUTHORISER` | `CoValuationParameter_Authoriser` | String |  |  |
| 23 | `COVP.CO.CODE` | `CoValuationParameter_CoCode` | String |  |  |
| 24 | `COVP.DEPT.CODE` | `CoValuationParameter_DeptCode` | String |  |  |
| 25 | `COVP.AUDITOR.CODE` | `CoValuationParameter_AuditorCode` | String |  |  |
| 26 | `COVP.AUDIT.DATE.TIME` | `CoValuationParameter_AuditDateTime` | String |  |  |
| 27 | `COVP.PF.QUAL.VALUE` | `CoValuationParameter_PfQualValue` | TField |  | It is the threshold value,based on which whether the portfolio is eligible for applying Concentration cap will be determined. Validation Rules: Input allowed only when INCL.CLV.CAP field is set in SC.PARAMETER. |
| 28 | `COVP.ALLOCATION.TYPE` | `CoValuationParameter_AllocationType` | TField | No | Specifies if the collaterals have to be allocated against the Limits or Liabilities based on CUSTOMER or LIMIT.COL.ALLOC.WORK. If &quot;ALLOC.WORK&quot; is specified in this field, then allocation happens based on the limits and collaterals in LIMIT.COL.ALLOC.WORK structure. If Null or &quot;CUSTOMER&quot; is specified in this field,then allocation happens based on the limits and collaterals of the CUSTOMER. Validation Rules: Optional field. Valid values are Null, CUSTOMER and ALLOC.WORK. |
| 29 | `COVP.ALLOCATION.VALUE` | `CoValuationParameter_AllocationValue` | TField | No | Specifies if the collaterals have to be allocated against the limits based on the maximum total or outstanding amount of the limits. If &quot;MAXIMUM.TOTAL&quot; is specified in this field, then the maximum total value specified in the limits linked to the collateral right will be considered as the value to be allocated. If Null or &quot;TOTAL.OS&quot; is specified in this field,then the total outstanding value of the limits linked to the collateral right will be considered as the value to be allocated. The total outstanding will be calculated by adding the TOTAL.OS value of the limit and balance of the account linked to the limit, if account balance is in debit(less than zero) and ACCOUNT.AS.LIAB flag is set as YES. Or else the total outstanding will be the value specified in TOTAL.OS field of the limit. Validation Rules: Optional field. Valid values are Null, TOTAL.OS and MAXIMUM.TOTAL. |
| 30 | `COVP.EXCLUDE.CONC.CAP.POOL` | `CoValuationParameter_ExcludeConcCapPool` |  |  |  |
| 31 | `COVP.INCLUDE.CONC.CAP.POOL` | `CoValuationParameter_IncludeConcCapPool` |  |  |  |
| 32 | `COVP.APPLY.CREDIT.POLICY` | `CoValuationParameter_ApplyCreditPolicy` | TField | Yes | When this field is set to Yes, then the system will use the Credit policy hierarchy to fetch the margin rates from MV.MARGIN.RULES or default rates from MV.CREDIT.POLICY which will be used to calculate the margin value of the assets. When this field is set to No, then the margin rates will be applied using the default hierarchy. Validation Rules: This field will be allowed for input and it is mandatory for SYSTEM Id and it is blocked for input for Company Id. |
| 33 | `COVP.RULE.EVALUATION` | `CoValuationParameter_RuleEvaluation` | TField |  |  |
