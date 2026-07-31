# AUOBPI.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AUOBPI.PARAMETER` in `AUOBPI_ProductsAPI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUOBPI.ELIGIBILITY.RULE` | `AuobpiParameter_EligibilityRule` |  |  |  |
| 2 | `AUOBPI.CDR.ELIGIBILITY.TYPE` | `AuobpiParameter_CdrEligibilityType` |  |  |  |
| 3 | `AUOBPI.ELIGIBILITY.VALUE` | `AuobpiParameter_EligibilityValue` |  |  |  |
| 4 | `AUOBPI.PERIODIC.ATTRIBUTE` | `AuobpiParameter_PeriodicAttribute` |  |  |  |
| 5 | `AUOBPI.CDR.CONSTRAINT.TYPE.ACT.RES` | `AuobpiParameter_CdrConstraintTypeActRes` |  |  |  |
| 6 | `AUOBPI.NEGOTIATED.PROPERTY.CLASS` | `AuobpiParameter_NegotiatedPropertyClass` |  |  |  |
| 7 | `AUOBPI.NEGOTIATION.TYPE` | `AuobpiParameter_NegotiationType` |  |  |  |
| 8 | `AUOBPI.CDR.CONSTRAINT.TYPE.ACT.NR` | `AuobpiParameter_CdrConstraintTypeActNr` |  |  |  |
| 9 | `AUOBPI.CDR.FEE.TYPE` | `AuobpiParameter_CdrFeeType` |  |  |  |
| 10 | `AUOBPI.CHARGE.PROPERTY` | `AuobpiParameter_ChargeProperty` |  |  |  |
| 11 | `AUOBPI.VARIATION` | `AuobpiParameter_Variation` |  |  |  |
| 12 | `AUOBPI.CDR.DISCOUNT.TYPE` | `AuobpiParameter_CdrDiscountType` |  |  |  |
| 13 | `AUOBPI.CDR.DISCOUNT.ELIG.TYPE` | `AuobpiParameter_CdrDiscountEligType` |  |  |  |
| 14 | `AUOBPI.INTEREST.PROPERTY` | `AuobpiParameter_InterestProperty` |  |  |  |
| 15 | `AUOBPI.PRIMARY.INTEREST.RATE` | `AuobpiParameter_PrimaryInterestRate` |  |  |  |
| 16 | `AUOBPI.CDR.RATE.TYPE` | `AuobpiParameter_CdrRateType` |  |  |  |
| 17 | `AUOBPI.RATE.TIER.TYPE` | `AuobpiParameter_RateTierType` |  |  |  |
| 18 | `AUOBPI.RATE.TIER.APP.METHOD` | `AuobpiParameter_RateTierAppMethod` |  |  |  |
| 19 | `AUOBPI.CDR.PRODUCT.CATEGORY` | `AuobpiParameter_CdrProductCategory` | TField |  | This field Contains Product classification among any one of the AU CDR product categories |
| 20 | `AUOBPI.CDR.FEATURE.TYPE` | `AuobpiParameter_CdrFeatureType` |  |  |  |
| 21 | `AUOBPI.FEATURE.VALUE` | `AuobpiParameter_FeatureValue` |  |  |  |
| 22 | `AUOBPI.FEATURE.INFO` | `AuobpiParameter_FeatureInfo` |  |  |  |
| 23 | `AUOBPI.FEATURE.INFO.URI` | `AuobpiParameter_FeatureInfoUri` |  |  |  |
| 24 | `AUOBPI.PRODUCT.APP.URI` | `AuobpiParameter_ProductAppUri` |  |  |  |
| 25 | `AUOBPI.PRODUCT.OVERVIEW.URI` | `AuobpiParameter_ProductOverviewUri` |  |  |  |
| 26 | `AUOBPI.PRODUCT.TERMS.URI` | `AuobpiParameter_ProductTermsUri` |  |  |  |
| 27 | `AUOBPI.PRODUCT.ELIG.URI` | `AuobpiParameter_ProductEligUri` |  |  |  |
| 28 | `AUOBPI.PRODUCT.FEES.URI` | `AuobpiParameter_ProductFeesUri` |  |  |  |
| 29 | `AUOBPI.PRODUCT.BUNDLE.URI` | `AuobpiParameter_ProductBundleUri` |  |  |  |
| 30 | `AUOBPI.BUNDLE.INFO.URI` | `AuobpiParameter_BundleInfoUri` |  |  |  |
| 31 | `AUOBPI.CONSTRAINT.INFO.URI` | `AuobpiParameter_ConstraintInfoUri` |  |  |  |
| 32 | `AUOBPI.ELIGIBILITY.INFO.URI` | `AuobpiParameter_EligibilityInfoUri` |  |  |  |
| 33 | `AUOBPI.FEE.INFO.URI` | `AuobpiParameter_FeeInfoUri` |  |  |  |
| 34 | `AUOBPI.DISCOUNT.LINFO.URI` | `AuobpiParameter_DiscountLinfoUri` |  |  |  |
| 35 | `AUOBPI.DISCOUNT.ELIG.INFO.URI` | `AuobpiParameter_DiscountEligInfoUri` |  |  |  |
| 36 | `AUOBPI.DEPOSIT.RATE.TIER.INFO.URI` | `AuobpiParameter_DepositRateTierInfoUri` |  |  |  |
| 37 | `AUOBPI.DEPOSIT.RATE.INFO.URI` | `AuobpiParameter_DepositRateInfoUri` |  |  |  |
| 38 | `AUOBPI.LENDING.RATE.TIER.INFO.URI` | `AuobpiParameter_LendingRateTierInfoUri` |  |  |  |
| 39 | `AUOBPI.LENDING.RATE.INFO.URI` | `AuobpiParameter_LendingRateInfoUri` |  |  |  |
| 40 | `AUOBPI.LOCAL.REF` | `AuobpiParameter_LocalRef` |  |  |  |
| 41 | `AUOBPI.CARDART.TITLE` | `AuobpiParameter_CardArtTitle` |  |  |  |
| 42 | `AUOBPI.CARDART.IMAGE.URI` | `AuobpiParameter_CardArtImageUri` |  |  |  |
| 43 | `AUOBPI.RESERVED.3` | `AuobpiParameter_Reserved3` | TField |  | This field is reserved for future use |
| 44 | `AUOBPI.RESERVED.2` | `AuobpiParameter_Reserved2` | TField |  | This field is reserved for future use |
| 45 | `AUOBPI.RESERVED.1` | `AuobpiParameter_Reserved1` | TField |  | This field is reserved for future use |
| 46 | `AUOBPI.OVERRIDE` | `AuobpiParameter_Override` |  |  |  |
| 47 | `AUOBPI.RECORD.STATUS` | `AuobpiParameter_RecordStatus` | String |  |  |
| 48 | `AUOBPI.CURR.NO` | `AuobpiParameter_CurrNo` | String |  |  |
| 49 | `AUOBPI.INPUTTER` | `AuobpiParameter_Inputter` |  |  |  |
| 50 | `AUOBPI.DATE.TIME` | `AuobpiParameter_DateTime` |  |  |  |
| 51 | `AUOBPI.AUTHORISER` | `AuobpiParameter_Authoriser` | String |  |  |
| 52 | `AUOBPI.CO.CODE` | `AuobpiParameter_CoCode` | String |  |  |
| 53 | `AUOBPI.DEPT.CODE` | `AuobpiParameter_DeptCode` | String |  |  |
| 54 | `AUOBPI.AUDITOR.CODE` | `AuobpiParameter_AuditorCode` | String |  |  |
| 55 | `AUOBPI.AUDIT.DATE.TIME` | `AuobpiParameter_AuditDateTime` | String |  |  |
