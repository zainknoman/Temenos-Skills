# AA.PRODUCT.CATALOG — Table Schema

> Source: `INSERTS/I_F.AA.PRODUCT.CATALOG` in `AA_ProductManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PRD.DESCRIPTION` | `AaProductCatalog_Description` |  |  |  |
| 2 | `AA.PRD.FULL.DESC` | `AaProductCatalog_FullDesc` |  |  |  |
| 3 | `AA.PRD.PRODUCT.GROUP` | `AaProductCatalog_ProductGroup` | TField | Yes | This field indicates which product group the current product belongs to. Product group defines a higher level of product definition which groups the classes and its properties whilst also deciding on the mandatory properties of the group. To create a new product, the user must specify either the PRODUCT.GROUP when defining a top-level product or the PARENT.PRODUCT when defining a sub-product. |
| 4 | `AA.PRD.PARENT.PRODUCT` | `AaProductCatalog_ParentProduct` | TField |  | Indicates whether the product will inherit properties from a parent product. If a product is selected in this field, the new product will inherit all properties that have not been specifially defined within it. |
| 5 | `AA.PRD.CURRENCY` | `AaProductCatalog_Currency` |  |  |  |
| 6 | `AA.PRD.RECONSTRUCT.SETTLEMENT` | `AaProductCatalog_ReconstructSettlement` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `AA.PRD.PROPERTY` | `AaProductCatalog_Property` |  |  |  |
| 8 | `AA.PRD.EFFECTIVE.BASE` | `AaProductCatalog_EffectiveBase` |  |  |  |
| 9 | `AA.PRD.PROPERTY.VARIATION` | `AaProductCatalog_PropertyVariation` |  |  |  |
| 10 | `AA.PRD.PROPERTY.INHERITANCE` | `AaProductCatalog_PropertyInheritance` |  |  |  |
| 11 | `AA.PRD.AVAILABLE.CONDITIONS` | `AaProductCatalog_AvailableConditions` |  |  |  |
| 12 | `AA.PRD.PROPERTY.TYPE` | `AaProductCatalog_PropertyType` |  |  |  |
| 13 | `AA.PRD.RESERVED13` | `AaProductCatalog_Reserved13` |  |  |  |
| 14 | `AA.PRD.PRD.PROPERTY` | `AaProductCatalog_PrdProperty` |  |  |  |
| 15 | `AA.PRD.PC.PRD.PR` | `AaProductCatalog_PcPrdPr` |  |  |  |
| 16 | `AA.PRD.ARR.LINK` | `AaProductCatalog_ArrLink` |  |  |  |
| 17 | `AA.PRD.RESERVED11` | `AaProductCatalog_Reserved11` |  |  |  |
| 18 | `AA.PRD.EFFECTIVE` | `AaProductCatalog_Effective` |  |  |  |
| 19 | `AA.PRD.INHERITANCE.ONLY` | `AaProductCatalog_InheritanceOnly` | TField |  | This field determines whether the product is defined for inheritance purposes only and will not be available for sale. |
| 20 | `AA.PRD.DEFAULT.PRODUCT` | `AaProductCatalog_DefaultProduct` | TField | Yes | Used only when the financial institution uses ELIGIBILITY property. For example, in ELIGIBILITY condition, there is an option to move to a default product if certain eligibility rules are not met. It is mandatory that such default products do not have any Eligibility checks themselves. So, when a product is flagged as DEFAULT.PRODUCT, it is mandatory that the product should NOT have any ELIGIBILITY property defined under it. This is checked when the product is proofed/published. Options : YES - indicates this product could be used as a Default product for Eligibility rule failure. |
| 21 | `AA.PRD.AVAILABLE.COMPANY` | `AaProductCatalog_AvailableCompany` |  |  |  |
| 22 | `AA.PRD.OWNING.COMPANY` | `AaProductCatalog_OwningCompany` |  |  |  |
| 23 | `AA.PRD.CALC.PROPERTY` | `AaProductCatalog_CalcProperty` |  |  |  |
| 24 | `AA.PRD.SOURCE.TYPE` | `AaProductCatalog_SourceType` |  |  |  |
| 25 | `AA.PRD.SOURCE.BALANCE` | `AaProductCatalog_SourceBalance` |  |  |  |
| 26 | `AA.PRD.SOURCE.PROPERTY` | `AaProductCatalog_SourceProperty` |  |  |  |
| 27 | `AA.PRD.TIER.SOURCE.TYPE` | `AaProductCatalog_TierSourceType` |  |  |  |
| 28 | `AA.PRD.TIER.SOURCE.BALANCE` | `AaProductCatalog_TierSourceBalance` |  |  |  |
| 29 | `AA.PRD.TIER.SOURCE.PROPERTY` | `AaProductCatalog_TierSourceProperty` |  |  |  |
| 30 | `AA.PRD.LOCAL.REF` | `AaProductCatalog_LocalRef` |  |  |  |
| 31 | `AA.PRD.PRODUCT` | `AaProductCatalog_Product` | TField |  | Indicates the name of the product which is being defined. |
| 32 | `AA.PRD.EFFECTIVE.DATE` | `AaProductCatalog_EffectiveDate` | TField |  | This field represents the effective date from which the product change comes into force. |
| 33 | `AA.PRD.VARIATION` | `AaProductCatalog_Variation` |  |  |  |
| 34 | `AA.PRD.VARIATION.DEFAULT` | `AaProductCatalog_VariationDefault` | TField |  | If the customer is not eligible for a variation this field will determine if there is a "non-variation" version of the product (i.e. the default). If this is checked then the default configuration cannot have ELIGIBILITY, as all customers would be eligible. Validation rules: Accepts a YES and default is NULL. |
| 35 | `AA.PRD.ADVANCE.RATEFIX.PERIOD` | `AaProductCatalog_AdvanceRatefixPeriod` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Indicates the period before which the rate could be fixed and modified schedules could be sent upfront. For example, if the periodic rate is getting reviewed on 01-July. The user could state a 5D here and system finds the new rate on 26-June itself and fixes that rate on the contract. Schedules based on the new rate could also be sent upfront. Please be noted that the rate applied on 26-June is the rate 'effective' on that date - but it would be applied on the arrangement from the review date. This is applicable only for Periodic reviews and also for forward dated conditions which have fixed rate stated. Does not apply for Floating rates. Validation: A T24 period could be stated like 5D, 1W, 1M etc. Valid ONLY for LENDING products |
| 36 | `AA.PRD.PRODUCT.PURPOSE` | `AaProductCatalog_ProductPurpose` |  |  |  |
| 37 | `AA.PRD.INHERITANCE.CURRENCY` | `AaProductCatalog_InheritanceCurrency` |  |  |  |
| 38 | `AA.PRD.TRACK.EFF.PERIOD` | `AaProductCatalog_TrackEffPeriod` |  |  |  |
| 39 | `AA.PRD.TRACK.PROPERTY.CLASS` | `AaProductCatalog_TrackPropertyClass` |  |  |  |
| 40 | `AA.PRD.ORGANIZATION.LEVEL` | `AaProductCatalog_OrganizationLevel` |  |  |  |
| 41 | `AA.PRD.ORGANIZATION.CODE` | `AaProductCatalog_OrganizationCode` |  |  |  |
| 42 | `AA.PRD.LINE.OF.BUSINESS` | `AaProductCatalog_LineOfBusiness` |  |  |  |
| 43 | `AA.PRD.IN.PROPERTY` | `AaProductCatalog_InProperty` |  |  |  |
| 44 | `AA.PRD.IN.PRODUCT` | `AaProductCatalog_InProduct` |  |  |  |
| 45 | `AA.PRD.IN.EFF.BASE` | `AaProductCatalog_InEffBase` |  |  |  |
| 46 | `AA.PRD.IN.PR.VAR` | `AaProductCatalog_InPrVar` |  |  |  |
| 47 | `AA.PRD.IN.PRD.PR` | `AaProductCatalog_InPrdPr` |  |  |  |
| 48 | `AA.PRD.IN.PC.PRD.PR` | `AaProductCatalog_InPcPrdPr` |  |  |  |
| 49 | `AA.PRD.RESERVED04` | `AaProductCatalog_Reserved04` |  |  |  |
| 50 | `AA.PRD.RESERVED03` | `AaProductCatalog_Reserved03` |  |  |  |
| 51 | `AA.PRD.RESERVED02` | `AaProductCatalog_Reserved02` |  |  |  |
| 52 | `AA.PRD.RESERVED01` | `AaProductCatalog_Reserved01` |  |  |  |
| 53 | `AA.PRD.IN.ARR.LINK` | `AaProductCatalog_InArrLink` |  |  |  |
| 54 | `AA.PRD.IN.EFF` | `AaProductCatalog_InEff` |  |  |  |
| 55 | `AA.PRD.IN.PR.SOURCE` | `AaProductCatalog_InPrSource` |  |  |  |
| 56 | `AA.PRD.IN.CALC.PR` | `AaProductCatalog_InCalcPr` |  |  |  |
| 57 | `AA.PRD.IN.SR.TYPE` | `AaProductCatalog_InSrType` |  |  |  |
| 58 | `AA.PRD.IN.SR.BAL` | `AaProductCatalog_InSrBal` |  |  |  |
| 59 | `AA.PRD.IN.SR.PR` | `AaProductCatalog_InSrPr` |  |  |  |
| 60 | `AA.PRD.IN.SR.TR.TYPE` | `AaProductCatalog_InSrTrType` |  |  |  |
| 61 | `AA.PRD.IN.SR.TR.BAL` | `AaProductCatalog_InSrTrBal` |  |  |  |
| 62 | `AA.PRD.IN.SR.TR.PR` | `AaProductCatalog_InSrTrPr` |  |  |  |
| 63 | `AA.PRD.OVERRIDE` | `AaProductCatalog_Override` |  |  |  |
| 64 | `AA.PRD.RECORD.STATUS` | `AaProductCatalog_RecordStatus` | String |  |  |
| 65 | `AA.PRD.CURR.NO` | `AaProductCatalog_CurrNo` | String |  |  |
| 66 | `AA.PRD.INPUTTER` | `AaProductCatalog_Inputter` |  |  |  |
| 67 | `AA.PRD.DATE.TIME` | `AaProductCatalog_DateTime` |  |  |  |
| 68 | `AA.PRD.AUTHORISER` | `AaProductCatalog_Authoriser` | String |  |  |
| 69 | `AA.PRD.CO.CODE` | `AaProductCatalog_CoCode` | String |  |  |
| 70 | `AA.PRD.DEPT.CODE` | `AaProductCatalog_DeptCode` | String |  |  |
| 71 | `AA.PRD.AUDITOR.CODE` | `AaProductCatalog_AuditorCode` | String |  |  |
| 72 | `AA.PRD.AUDIT.DATE.TIME` | `AaProductCatalog_AuditDateTime` | String |  |  |
| 73 | `AA.PRD.CHANNEL` | `AaProductCatalog_Channel` |  |  |  |
| 74 | `AA.PRD.CHANNEL.EXCLUDE` | `AaProductCatalog_ChannelExclude` |  |  |  |
| 75 | `AA.PRD.ORGANISATION.EXCLUDE` | `AaProductCatalog_OrganisationExclude` |  |  |  |
| 76 | `AA.PRD.LINE.OF.BUSINESS.EXCLUDE` | `AaProductCatalog_LineOfBusinessExclude` |  |  |  |
| 77 | `AA.PRD.BUNDLE.ONLY` | `AaProductCatalog_BundleOnly` | TField |  | Indicator to check if the product is created in restricted mode Options : YES - Whenever a transaction or user activity is initiated is run on such an Arrangement, system would raise an override that this Arrangement is not yet part of a Bundle |
| 78 | `AA.PRD.PRODUCT.ATTRIBUTE` | `AaProductCatalog_ProductAttribute` |  |  |  |
| 79 | `AA.PRD.SOURCE.APPLICATION` | `AaProductCatalog_SourceApplication` |  |  |  |
| 80 | `AA.PRD.SOURCE.REFERENCE` | `AaProductCatalog_SourceReference` |  |  |  |
| 81 | `AA.PRD.MEMO` | `AaProductCatalog_Memo` | TField |  | It is used to denote if the arrangement is Memo in nature. Validation Rules: 1. If this flag is enabled, then property should contain MEMO-ENABLED as property type. 2. This flag is allowed only for Lending product line. |
| 82 | `AA.PRD.PROD.TYPE` | `AaProductCatalog_ProdType` | TField |  | This field is used to identify if the product is created by Temenos or client in Saas environment. The field accepts two values Internal(Temenos created products) and Null(client created products). The field value is defaulted to internal in Temenos Saas environment. The field is no input in client environment. |
| 83 | `AA.PRD.AVAILABLE.COUNTRY` | `AaProductCatalog_AvailableCountry` |  |  |  |
| 84 | `AA.PRD.AVAILABLE.REGION` | `AaProductCatalog_AvailableRegion` |  |  |  |
| 85 | `AA.PRD.BASE.PRODUCT.TYPE` | `AaProductCatalog_BaseProductType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 86 | `AA.PRD.EPP.PRODUCT.GROUP` | `AaProductCatalog_EppProductGroup` | TField | Yes | This field is allowed for a product group which begins with EPP to be specified. Only used when PRODUCT.GROUP is EPP.Mandatory when PRODUCT.GROUP is EPP. |
| 87 | `AA.PRD.ACT.THRESHOLD.PERIOD` | `AaProductCatalog_ActThresholdPeriod` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 88 | `AA.PRD.ACT.RETAIN.PERIOD` | `AaProductCatalog_ActRetainPeriod` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 89 | `AA.PRD.PRODUCT.ONLY` | `AaProductCatalog_ProductOnly` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 90 | `AA.PRD.EPP.PRODUCT.LINE` | `AaProductCatalog_EppProductLine` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
