# AUOBPZ.XAUOB.ATTRIBUTES — Table Schema

> Source: `INSERTS/I_F.AUOBPZ.XAUOB.ATTRIBUTES` in `AUOBPZ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUOBPZ.ATTRIBUTES.AUOBPZ.ALT.ID.TYPE` | `AuobpzXauobAttributes_AuobpzAltIdType` | TField |  | Specifies the alternate Id Type for the AUOBPZ. |
| 2 | `AUOBPZ.ATTRIBUTES.CDR.PRODUCT.CATEGORY` | `AuobpzXauobAttributes_CdrProductCategory` | TField |  | Specifies the product category for categorising products and accounts. Provided as ENUM value e.g. TERM_DEPOSITS, TRAVEL_CARDS |
| 3 | `AUOBPZ.ATTRIBUTES.SPECIFIC.ACCOUNT.UTYPE` | `AuobpzXauobAttributes_SpecificAccountUtype` | TField |  | Specifies the category to which a product or account belongs. Provided as ENUM value e.g. CREDIT.CARD, LOAN, TERM.DEPOSIT |
| 4 | `AUOBPZ.ATTRIBUTES.AU.CDR.FEATURE.TYPE` | `AuobpzXauobAttributes_AuCdrFeatureType` |  |  |  |
| 5 | `AUOBPZ.ATTRIBUTES.FEATURE.VALUE` | `AuobpzXauobAttributes_FeatureValue` |  |  |  |
| 6 | `AUOBPZ.ATTRIBUTES.FEATURE.INFO` | `AuobpzXauobAttributes_FeatureInfo` |  |  |  |
| 7 | `AUOBPZ.ATTRIBUTES.FEATURE.INFO.URI` | `AuobpzXauobAttributes_FeatureInfoUri` |  |  |  |
| 8 | `AUOBPZ.ATTRIBUTES.FEE` | `AuobpzXauobAttributes_Fee` |  |  |  |
| 9 | `AUOBPZ.ATTRIBUTES.FEE.TYPE` | `AuobpzXauobAttributes_FeeType` |  |  |  |
| 10 | `AUOBPZ.ATTRIBUTES.FEE.INFO.URI` | `AuobpzXauobAttributes_FeeInfoUri` |  |  |  |
| 11 | `AUOBPZ.ATTRIBUTES.DISCOUNT.INFO.URI` | `AuobpzXauobAttributes_DiscountInfoUri` | TField |  | Link to a web page with more information on this discount. |
| 12 | `AUOBPZ.ATTRIBUTES.DISCOUNTELIG.INFO.URI` | `AuobpzXauobAttributes_DiscounteligInfoUri` | TField |  | Link to a web page with more information on this eligibility constraint. |
| 13 | `AUOBPZ.ATTRIBUTES.ADDRESS.U.TYPE` | `AuobpzXauobAttributes_AddressUType` | TField |  | Specifies the type of address object present. Provided as ENUM value e.g. SIMPLE, PAF. |
| 14 | `AUOBPZ.ATTRIBUTES.DEPOSIT.RATE.INFO.URI` | `AuobpzXauobAttributes_DepositRateInfoUri` | TField |  | Link to a web page with more information on the discount rate. |
| 15 | `AUOBPZ.ATTRIBUTES.LENDING.RATE.INFO.URI` | `AuobpzXauobAttributes_LendingRateInfoUri` | TField |  | Link to a web page with more information on the discount rate. |
| 16 | `AUOBPZ.ATTRIBUTES.AU.CDR.DISCOUNT.TYPE` | `AuobpzXauobAttributes_AuCdrDiscountType` |  |  |  |
| 17 | `AUOBPZ.ATTRIBUTES.OVERRIDE` | `AuobpzXauobAttributes_Override` |  |  |  |
| 18 | `AUOBPZ.ATTRIBUTES.LOCAL.REF` | `AuobpzXauobAttributes_LocalRef` |  |  |  |
| 19 | `AUOBPZ.ATTRIBUTES.RECORD.STATUS` | `AuobpzXauobAttributes_RecordStatus` | String |  |  |
| 20 | `AUOBPZ.ATTRIBUTES.CURR.NO` | `AuobpzXauobAttributes_CurrNo` | String |  |  |
| 21 | `AUOBPZ.ATTRIBUTES.INPUTTER` | `AuobpzXauobAttributes_Inputter` |  |  |  |
| 22 | `AUOBPZ.ATTRIBUTES.DATE.TIME` | `AuobpzXauobAttributes_DateTime` |  |  |  |
| 23 | `AUOBPZ.ATTRIBUTES.AUTHORISER` | `AuobpzXauobAttributes_Authoriser` | String |  |  |
| 24 | `AUOBPZ.ATTRIBUTES.CO.CODE` | `AuobpzXauobAttributes_CoCode` | String |  |  |
| 25 | `AUOBPZ.ATTRIBUTES.DEPT.CODE` | `AuobpzXauobAttributes_DeptCode` | String |  |  |
| 26 | `AUOBPZ.ATTRIBUTES.AUDITOR.CODE` | `AuobpzXauobAttributes_AuditorCode` | String |  |  |
| 27 | `AUOBPZ.ATTRIBUTES.AUDIT.DATE.TIME` | `AuobpzXauobAttributes_AuditDateTime` | String |  |  |
| 28 | `AUOBPZ.ATTRIBUTES.FEE.ADDITIONAL.VALUE` | `AuobpzXauobAttributes_FeeAdditionalValue` |  |  |  |
| 29 | `AUOBPZ.ATTRIBUTES.FEE.ADDITIONAL.INFO` | `AuobpzXauobAttributes_FeeAdditionalInfo` |  |  |  |
| 30 | `AUOBPZ.ATTRIBUTES.DEPOSIT.RATE.TYPE` | `AuobpzXauobAttributes_DepositRateType` |  |  |  |
| 31 | `AUOBPZ.ATTRIBUTES.DEPOSIT.ADDITIONAL.VALUE` | `AuobpzXauobAttributes_DepositAdditionalValue` |  |  |  |
| 32 | `AUOBPZ.ATTRIBUTES.DEPOSIT.ADDITIONAL.INFO` | `AuobpzXauobAttributes_DepositAdditionalInfo` |  |  |  |
| 33 | `AUOBPZ.ATTRIBUTES.LENDING.RATE.TYPE` | `AuobpzXauobAttributes_LendingRateType` |  |  |  |
| 34 | `AUOBPZ.ATTRIBUTES.LENDING.ADDITIONAL.VALUE` | `AuobpzXauobAttributes_LendingAdditionalValue` |  |  |  |
| 35 | `AUOBPZ.ATTRIBUTES.LENDING.ADDITIONAL.INFO` | `AuobpzXauobAttributes_LendingAdditionalInfo` |  |  |  |
| 36 | `AUOBPZ.ATTRIBUTES.POSTING.RESTRICTION` | `AuobpzXauobAttributes_PostingRestriction` |  |  |  |
| 37 | `AUOBPZ.ATTRIBUTES.UNAVAILABLE.REASON` | `AuobpzXauobAttributes_UnavailableReason` |  |  |  |
| 38 | `AUOBPZ.ATTRIBUTES.PRIMARY.INTEREST.PROPERTY` | `AuobpzXauobAttributes_PrimaryInterestProperty` |  |  |  |
| 39 | `AUOBPZ.ATTRIBUTES.TRANSACT.RATE.TYPE` | `AuobpzXauobAttributes_TransactRateType` |  |  |  |
| 40 | `AUOBPZ.ATTRIBUTES.CDR.RATE.TYPE` | `AuobpzXauobAttributes_CdrRateType` |  |  |  |
| 41 | `AUOBPZ.ATTRIBUTES.SECONDARY.INTEREST` | `AuobpzXauobAttributes_SecondaryInterest` |  |  |  |
| 42 | `AUOBPZ.ATTRIBUTES.SEC.CDR.RATE.TYPE` | `AuobpzXauobAttributes_SecCdrRateType` |  |  |  |
