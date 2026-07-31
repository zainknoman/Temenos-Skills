# AA.PRICING.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.PRICING.DETAILS` in `AA_PricingRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PRID.ARRANGEMENT.ID` | `AaPricingDetails_ArrangementId` | TField |  | This field identifies the main Arrangement Contract number. |
| 2 | `AA.PRID.ACTIVITY.ID` | `AaPricingDetails_ActivityId` | TField |  | The activity that was performed on this EFFECTIVE.DATE |
| 3 | `AA.PRID.DATE` | `AaPricingDetails_Date` | TField |  | The effective date on which the activities were performed |
| 4 | `AA.PRID.CURRENCY` | `AaPricingDetails_Currency` | TField |  | Currency of the Arrangement contract |
| 5 | `AA.PRID.PRICING.CLASS` | `AaPricingDetails_PricingClass` | TField |  | The Property class of the pricing property that triggered the calculation |
| 6 | `AA.PRID.PROPERTY` | `AaPricingDetails_Property` | TField |  | Pricing Property which triggered the calculation. |
| 7 | `AA.PRID.PRICING.TYPE` | `AaPricingDetails_PricingType` | TField |  | Defines the property type,CREDIT or DEBIT are possible values |
| 8 | `AA.PRID.BASE.VALUE` | `AaPricingDetails_BaseValue` | TField |  | The base charge or rate either calculated by EPP or the legacy core and passed into EPP. |
| 9 | `AA.PRID.ADJUST.VALUE` | `AaPricingDetails_AdjustValue` | TField |  | The total signed adjustment amount or rate |
| 10 | `AA.PRID.NET.VALUE` | `AaPricingDetails_NetValue` | TField |  | Difference between basevalue , adjustmentvalue |
| 11 | `AA.PRID.VALUE.MIN` | `AaPricingDetails_ValueMin` | TField |  | Minimum charge amount can be specified for associated currency attribute |
| 12 | `AA.PRID.VALUE.MAX` | `AaPricingDetails_ValueMax` | TField |  | Maximum charge amount can be specified for associated currency attribute |
| 13 | `AA.PRID.APPLICATION.METHOD` | `AaPricingDetails_ApplicationMethod` | TField |  | This field denotes the application method that needs to be applied to the charges |
| 14 | `AA.PRID.PRICING.PROGRAM` | `AaPricingDetails_PricingProgram` |  |  |  |
| 15 | `AA.PRID.BENEFIT` | `AaPricingDetails_Benefit` |  |  |  |
| 16 | `AA.PRID.BENEFIT.TYPE` | `AaPricingDetails_BenefitType` |  |  |  |
| 17 | `AA.PRID.BENEFIT.VALUE` | `AaPricingDetails_BenefitValue` |  |  |  |
| 18 | `AA.PRID.EVALUATION.REF` | `AaPricingDetails_EvaluationRef` |  |  |  |
| 19 | `AA.PRID.I.PROPERTY` | `AaPricingDetails_IProperty` |  |  |  |
| 20 | `AA.PRID.I.PRICING.TYPE` | `AaPricingDetails_IPricingType` |  |  |  |
| 21 | `AA.PRID.I.BASE.VALUE` | `AaPricingDetails_IBaseValue` |  |  |  |
| 22 | `AA.PRID.I.ADJUST.VALUE` | `AaPricingDetails_IAdjustValue` |  |  |  |
| 23 | `AA.PRID.I.NET.VALUE` | `AaPricingDetails_INetValue` |  |  |  |
| 24 | `AA.PRID.I.PRICING.PROGRAM` | `AaPricingDetails_IPricingProgram` |  |  |  |
| 25 | `AA.PRID.I.BENEFIT` | `AaPricingDetails_IBenefit` |  |  |  |
| 26 | `AA.PRID.I.BENEFIT.TYPE` | `AaPricingDetails_IBenefitType` |  |  |  |
| 27 | `AA.PRID.I.BENEFIT.VALUE` | `AaPricingDetails_IBenefitValue` |  |  |  |
| 28 | `AA.PRID.I.EVALUATION.REF` | `AaPricingDetails_IEvaluationRef` |  |  |  |
| 29 | `AA.PRID.EVENT.SYSTEM.REF` | `AaPricingDetails_EventSystemRef` | TField |  | Identifies the System Reference of the core system. |
| 30 | `AA.PRID.EVENT.CONTRACT.REF` | `AaPricingDetails_EventContractRef` | TField |  | Identifies the Contract Reference of the core system. |
| 31 | `AA.PRID.EVENT.REFERENCE` | `AaPricingDetails_EventReference` | TField |  | Identifies the unique reference of the event. |
| 32 | `AA.PRID.EVENT.IDENTIFIER` | `AaPricingDetails_EventIdentifier` | TField |  |  |
| 33 | `AA.PRID.EVENT.TYPE` | `AaPricingDetails_EventType` | TField |  | Identifies Event Type identifier of the core system. |
| 34 | `AA.PRID.EVENT.PRICING.NAME` | `AaPricingDetails_EventPricingName` | TField |  | Pricing Name of the core system which is passed in only if the core has calculated the base value. |
| 35 | `AA.PRID.EVENT.BASE.VALUE` | `AaPricingDetails_EventBaseValue` | TField |  | Base value from the core system |
| 36 | `AA.PRID.EVENT.BASE.VALUE.CCY` | `AaPricingDetails_EventBaseValueCcy` | TField |  | Currency of the base value. |
| 37 | `AA.PRID.EVENT.ADJUST.VALUE` | `AaPricingDetails_EventAdjustValue` | TField |  | Contains the amount which can be manually adjusted by passing values through context |
| 38 | `AA.PRID.EVENT.ADJUST.REASON` | `AaPricingDetails_EventAdjustReason` | TField |  | Contains the reason for adjustment. The values is passed through context name |
| 39 | `AA.PRID.SETTLE.ARRANGEMENT` | `AaPricingDetails_SettleArrangement` | TField |  | Contains the arrangement settling the charges mentioned in the bundle contract. |
| 40 | `AA.PRID.SETTLE.SYSTEM.REF` | `AaPricingDetails_SettleSystemRef` | TField |  | Identifier for external arrangement, this is the system reference |
| 41 | `AA.PRID.SETTLE.CONTRACT.REF` | `AaPricingDetails_SettleContractRef` | TField |  | Identifier for an external arrangement, this is the contract reference |
| 42 | `AA.PRID.TIER.FINAL.RATE` | `AaPricingDetails_TierFinalRate` |  |  |  |
| 43 | `AA.PRID.TIER.VALUE` | `AaPricingDetails_TierValue` |  |  |  |
| 44 | `AA.PRID.TIER.TYPE` | `AaPricingDetails_TierType` | TField |  | Specifies the type of tiered interest definition i.e., level or band. |
| 45 | `AA.PRID.TIER.SPREAD` | `AaPricingDetails_TierSpread` |  |  |  |
| 46 | `AA.PRID.TIER.BASE.RATE` | `AaPricingDetails_TierBaseRate` |  |  |  |
| 47 | `AA.PRID.CONTEXT.EXPRESSION` | `AaPricingDetails_ContextExpression` | TField |  | To define the multiple context type with AND/OR condition. For example, (Merchan*Walmart OR MerchantIndustry*Electronic) AND CHANNEL*MOBILE Where Merchant, MerchantIndustry and Channel are record IDs of AA.Context.type Table. And Walmart, Electronic and MOBILE are the dynamic values for the respective context type. |
| 48 | `AA.PRID.CONTEXT.ACTUAL.VALUE` | `AaPricingDetails_ContextActualValue` | TField |  | When pricing is evaluated, this field gets updated with the possible context name value pair which are matched between context expression and incoming activity context. |
| 49 | `AA.PRID.CONTEXT.QUALIFIED.VALUE` | `AaPricingDetails_ContextQualifiedValue` | TField |  | Child context name value pair that are qualified the above context expression. Parent context value pair also gets updated when there is no child context value pair available in the expression. |
| 50 | `AA.PRID.REGIONAL.ADJUST.VALUE` | `AaPricingDetails_PridRegionalAdjustValue` |  |  |  |
| 51 | `AA.PRID.PRODUCT.PRICING.VALUE` | `AaPricingDetails_PridProductPricingValue` |  |  |  |
| 52 | `AA.PRID.I.REGIONAL.ADJUST.VALUE` | `AaPricingDetails_PridIRegionalAdjustValue` |  |  |  |
| 53 | `AA.PRID.I.PRODUCT.PRICING.VALUE` | `AaPricingDetails_PridIProductPricingValue` |  |  |  |
