# AA.PRODUCT.DESIGNER — Table Schema

> Source: `INSERTS/I_F.AA.PRODUCT.DESIGNER` in `AA_ProductManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PRD.DESCRIPTION` | `AaProductDesigner_Description` |  |  |  |
| 2 | `AA.PRD.FULL.DESC` | `AaProductDesigner_FullDesc` |  |  |  |
| 3 | `AA.PRD.PRODUCT.GROUP` | `AaProductDesigner_ProductGroup` | TField | Yes | This field indicates which product group the current product belongs to. Product group defines a higher level of product definition which groups the classes and its properties whilst also deciding on the mandatory properties of the group. To create a new product, the user must specify either the PRODUCT.GROUP when defining a top-level product or the PARENT.PRODUCT when defining a sub-product. Validation rule: Maximum of 30 Alphanumeric characters Must contain a valid entry in AA.PRODUCT.GROUP. NOCHANGE field. |
| 4 | `AA.PRD.PARENT.PRODUCT` | `AaProductDesigner_ParentProduct` | TField |  | A key feature of the Product Builder is Product inheritance. This allows for the creation of product families where derivatives of a generic product or sub-product can be quickly created by simply defining the delta (in terms of product conditions) between the new and existing product. This means that where a Defined Property is not specifically defined it will be inherited from the parent product, grandparent product, etc. When a product is a derivative of another product, its immediate product may be stated in this field. The resolving of hierarchy would only happen during Proofing process and the resultant published record would have the full product structure of both the parent and the current conditions. Validation rule: Should be a valid id in AA.PRODUCT. The field cannot be changed for subsequent dated records. |
| 5 | `AA.PRD.CURRENCY` | `AaProductDesigner_Currency` |  |  |  |
| 6 | `AA.PRD.RECONSTRUCT.SETTLEMENT` | `AaProductDesigner_ReconstructSettlement` | TField |  | This field is moved to product Group level.So it is Reserved for future use. |
| 7 | `AA.PRD.PROPERTY` | `AaProductDesigner_Property` |  |  |  |
| 8 | `AA.PRD.EFFECTIVE.BASE` | `AaProductDesigner_EffectiveBase` |  |  |  |
| 9 | `AA.PRD.PROPERTY.VARIATION` | `AaProductDesigner_PropertyVariation` |  |  |  |
| 10 | `AA.PRD.PROPERTY.INHERITANCE` | `AaProductDesigner_PropertyInheritance` |  |  |  |
| 11 | `AA.PRD.AVAILABLE.CONDITIONS` | `AaProductDesigner_AvailableConditions` |  |  |  |
| 12 | `AA.PRD.PROPERTY.TYPE` | `AaProductDesigner_PropertyType` |  |  |  |
| 13 | `AA.PRD.RESERVED13` | `AaProductDesigner_Reserved13` |  |  |  |
| 14 | `AA.PRD.PRD.PROPERTY` | `AaProductDesigner_PrdProperty` |  |  |  |
| 15 | `AA.PRD.PC.PRD.PR` | `AaProductDesigner_PcPrdPr` |  |  |  |
| 16 | `AA.PRD.ARR.LINK` | `AaProductDesigner_ArrLink` |  |  |  |
| 17 | `AA.PRD.EFFECTIVE.PHASE` | `AaProductDesigner_EffectivePhase` |  |  |  |
| 18 | `AA.PRD.EFFECTIVE` | `AaProductDesigner_Effective` |  |  |  |
| 19 | `AA.PRD.INHERITANCE.ONLY` | `AaProductDesigner_InheritanceOnly` | TField |  | T24 product builder follows a structured way of defining products. In addition to this structural hierarchy, the Product Builder enables the definition of families of products through Product Inheritance. This allows for a derivative of a product to be defined by simply specifying a "parent" product and any different conditions. Inheritance Only products do not undergo full proofing validations nor are they available for sale on their own. They are only abstract definition of a product which should be derived down the hierarchy to define the product in its entirety. Validation Rule: Accepts a value of YES/NO. |
| 20 | `AA.PRD.DEFAULT.PRODUCT` | `AaProductDesigner_DefaultProduct` | TField | Yes | Used only when the financial institution uses ELIGIBILITY property. For example, in ELIGIBILITY condition, there is an option to move to a default product if certain eligibility rules are not met. It is mandatory that such default products do not have any Eligibility checks themselves. So, when a product is flagged as DEFAULT.PRODUCT, it is mandatory that the product should NOT have any ELIGIBILITY property defined under it. This is checked when the product is proofed/published. Options : YES - indicates this product could be used as a Default product for Eligibility rule failure. |
| 21 | `AA.PRD.AVAILABLE.COMPANY` | `AaProductDesigner_AvailableCompany` |  |  |  |
| 22 | `AA.PRD.OWNING.COMPANY` | `AaProductDesigner_OwningCompany` |  |  |  |
| 23 | `AA.PRD.CALC.PROPERTY` | `AaProductDesigner_CalcProperty` |  |  |  |
| 24 | `AA.PRD.SOURCE.TYPE` | `AaProductDesigner_SourceType` |  |  |  |
| 25 | `AA.PRD.SOURCE.BALANCE` | `AaProductDesigner_SourceBalance` |  |  |  |
| 26 | `AA.PRD.SOURCE.PROPERTY` | `AaProductDesigner_SourceProperty` |  |  |  |
| 27 | `AA.PRD.TIER.SOURCE.TYPE` | `AaProductDesigner_TierSourceType` |  |  |  |
| 28 | `AA.PRD.TIER.SOURCE.BALANCE` | `AaProductDesigner_TierSourceBalance` |  |  |  |
| 29 | `AA.PRD.TIER.SOURCE.PROPERTY` | `AaProductDesigner_TierSourceProperty` |  |  |  |
| 30 | `AA.PRD.LOCAL.REF` | `AaProductDesigner_LocalRef` |  |  |  |
| 31 | `AA.PRD.PRODUCT` | `AaProductDesigner_Product` | TField |  | Indicates the name of the product which is being defined. NOINPUT, System maintained field. Used for Indexing on the product record. |
| 32 | `AA.PRD.EFFECTIVE.DATE` | `AaProductDesigner_EffectiveDate` | TField |  | This field represents the effective date from which these product conditions come into force. Noinput -System maintained field. Valid date field. |
| 33 | `AA.PRD.VARIATION` | `AaProductDesigner_Variation` |  |  |  |
| 34 | `AA.PRD.VARIATION.DEFAULT` | `AaProductDesigner_VariationDefault` | TField |  | If the customer is not eligible for a variation this field will determine if there is a non-variation version of the product (i.e. the default). If this is checked then the default configuration cannot have ELIGIBILITY, as all customers would be eligible. Validation rules: Accepts a YES and default is NULL. |
| 35 | `AA.PRD.ADVANCE.RATEFIX.PERIOD` | `AaProductDesigner_AdvanceRatefixPeriod` | TField |  | Indicates the period before which the rate could be fixed and modified schedules could be sent upfront. For example, if the periodic rate is getting reviewed on 01-July. The user could state a 5D here and system finds the new rate on 26-June itself and fixes that rate on the contract. Schedules based on the new rate could also be sent upfront. Please be noted that the rate applied on 26-June is the rate 'effective' on that date - but it would be applied on the arrangement from the review date. This is applicable only for Periodic reviews and also for forward dated conditions which have fixed rate stated. Does not apply for Floating rates. Validation: A T24 period could be stated like 5D, 1W, 1M etc. Valid ONLY for LENDING products |
| 36 | `AA.PRD.PRODUCT.PURPOSE` | `AaProductDesigner_ProductPurpose` |  |  |  |
| 37 | `AA.PRD.INHERITANCE.CURRENCY` | `AaProductDesigner_InheritanceCurrency` |  |  |  |
| 38 | `AA.PRD.TRACK.EFF.PERIOD` | `AaProductDesigner_TrackEffPeriod` |  |  |  |
| 39 | `AA.PRD.TRACK.PROPERTY.CLASS` | `AaProductDesigner_TrackPropertyClass` |  |  |  |
| 40 | `AA.PRD.ORGANIZATION.LEVEL` | `AaProductDesigner_OrganizationLevel` |  |  |  |
| 41 | `AA.PRD.ORGANIZATION.CODE` | `AaProductDesigner_OrganizationCode` |  |  |  |
| 42 | `AA.PRD.LINE.OF.BUSINESS` | `AaProductDesigner_LineOfBusiness` |  |  |  |
| 43 | `AA.PRD.IN.PROPERTY` | `AaProductDesigner_InProperty` |  |  |  |
| 44 | `AA.PRD.IN.PRODUCT` | `AaProductDesigner_InProduct` |  |  |  |
| 45 | `AA.PRD.IN.EFF.BASE` | `AaProductDesigner_InEffBase` |  |  |  |
| 46 | `AA.PRD.IN.PR.VAR` | `AaProductDesigner_InPrVar` |  |  |  |
| 47 | `AA.PRD.IN.PRD.PR` | `AaProductDesigner_InPrdPr` |  |  |  |
| 48 | `AA.PRD.IN.PC.PRD.PR` | `AaProductDesigner_InPcPrdPr` |  |  |  |
| 49 | `AA.PRD.RESERVED04` | `AaProductDesigner_Reserved04` |  |  |  |
| 50 | `AA.PRD.RESERVED03` | `AaProductDesigner_Reserved03` |  |  |  |
| 51 | `AA.PRD.RESERVED02` | `AaProductDesigner_Reserved02` |  |  |  |
| 52 | `AA.PRD.RESERVED01` | `AaProductDesigner_Reserved01` |  |  |  |
| 53 | `AA.PRD.IN.ARR.LINK` | `AaProductDesigner_InArrLink` |  |  |  |
| 54 | `AA.PRD.IN.EFF` | `AaProductDesigner_InEff` |  |  |  |
| 55 | `AA.PRD.IN.PR.SOURCE` | `AaProductDesigner_InPrSource` |  |  |  |
| 56 | `AA.PRD.IN.CALC.PR` | `AaProductDesigner_InCalcPr` |  |  |  |
| 57 | `AA.PRD.IN.SR.TYPE` | `AaProductDesigner_InSrType` |  |  |  |
| 58 | `AA.PRD.IN.SR.BAL` | `AaProductDesigner_InSrBal` |  |  |  |
| 59 | `AA.PRD.IN.SR.PR` | `AaProductDesigner_InSrPr` |  |  |  |
| 60 | `AA.PRD.IN.SR.TR.TYPE` | `AaProductDesigner_InSrTrType` |  |  |  |
| 61 | `AA.PRD.IN.SR.TR.BAL` | `AaProductDesigner_InSrTrBal` |  |  |  |
| 62 | `AA.PRD.IN.SR.TR.PR` | `AaProductDesigner_InSrTrPr` |  |  |  |
| 63 | `AA.PRD.OVERRIDE` | `AaProductDesigner_Override` |  |  |  |
| 64 | `AA.PRD.RECORD.STATUS` | `AaProductDesigner_RecordStatus` | String |  |  |
| 65 | `AA.PRD.CURR.NO` | `AaProductDesigner_CurrNo` | String |  |  |
| 66 | `AA.PRD.INPUTTER` | `AaProductDesigner_Inputter` |  |  |  |
| 67 | `AA.PRD.DATE.TIME` | `AaProductDesigner_DateTime` |  |  |  |
| 68 | `AA.PRD.AUTHORISER` | `AaProductDesigner_Authoriser` | String |  |  |
| 69 | `AA.PRD.CO.CODE` | `AaProductDesigner_CoCode` | String |  |  |
| 70 | `AA.PRD.DEPT.CODE` | `AaProductDesigner_DeptCode` | String |  |  |
| 71 | `AA.PRD.AUDITOR.CODE` | `AaProductDesigner_AuditorCode` | String |  |  |
| 72 | `AA.PRD.AUDIT.DATE.TIME` | `AaProductDesigner_AuditDateTime` | String |  |  |
| 73 | `AA.PRD.CHANNEL` | `AaProductDesigner_Channel` |  |  |  |
| 74 | `AA.PRD.CHANNEL.EXCLUDE` | `AaProductDesigner_ChannelExclude` |  |  |  |
| 75 | `AA.PRD.ORGANISATION.EXCLUDE` | `AaProductDesigner_OrganisationExclude` |  |  |  |
| 76 | `AA.PRD.LINE.OF.BUSINESS.EXCLUDE` | `AaProductDesigner_LineOfBusinessExclude` |  |  |  |
| 77 | `AA.PRD.BUNDLE.ONLY` | `AaProductDesigner_BundleOnly` | TField |  | Indicator to check if the product is created in restricted mode Options : YES - Whenever a transaction or user activity is initiated is run on such an Arrangement, system would raise an override that this Arrangement is not yet part of a Bundle |
| 78 | `AA.PRD.PRODUCT.ATTRIBUTE` | `AaProductDesigner_ProductAttribute` |  |  |  |
| 79 | `AA.PRD.SOURCE.APPLICATION` | `AaProductDesigner_SourceApplication` |  |  |  |
| 80 | `AA.PRD.SOURCE.REFERENCE` | `AaProductDesigner_SourceReference` |  |  |  |
| 81 | `AA.PRD.MEMO` | `AaProductDesigner_Memo` | TField |  | It is used to denote if the arrangement is Memo in nature. Validation Rules: 1. If this flag is enabled, then property should contain MEMO-ENABLED as property type. 2. This flag is allowed only for Lending product line. |
| 82 | `AA.PRD.PROD.TYPE` | `AaProductDesigner_ProdType` | TField |  | This field is used to identify if the product is created by Temenos or client in Saas environment. The field accepts two values Internal(Temenos created products) and Null(client created products). The field value is defaulted to internal in Temenos Saas environment. The field is no input in client environment. |
| 83 | `AA.PRD.AVAILABLE.COUNTRY` | `AaProductDesigner_AvailableCountry` |  |  |  |
| 84 | `AA.PRD.AVAILABLE.REGION` | `AaProductDesigner_AvailableRegion` |  |  |  |
| 85 | `AA.PRD.BASE.PRODUCT.TYPE` | `AaProductDesigner_BaseProductType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 86 | `AA.PRD.EPP.PRODUCT.GROUP` | `AaProductDesigner_EppProductGroup` | TField |  | Specifies an EPP Product Group. Validation Rules: Contains a free text value of the group name. |
| 87 | `AA.PRD.ACT.THRESHOLD.PERIOD` | `AaProductDesigner_ActThresholdPeriod` | TField |  | New field to define period values so that the activity history is moved to .HIST on reaching the threshold period. Valid Period field. Valid Suffixes are W- Week, M-Month, Y- Year and D-Days |
| 88 | `AA.PRD.ACT.RETAIN.PERIOD` | `AaProductDesigner_ActRetainPeriod` | TField |  | New field to define period value that needs to be retained when the archiving is performed. Valid Period field. Valid Suffixes are W- Week, M-Month, Y- Year and D-Days for e.g: Current system date is 23 Dec 2020.New arrangement is triggered on 13 Dec 2020 Threshold Period is defined as 10D and Retain period is defined as 1D For the above setup,system will move the activities from 13 Dec 2020 to 22 Dec 2020 to .HIST. |
| 89 | `AA.PRD.PRODUCT.ONLY` | `AaProductDesigner_ProductOnly` | TField |  | If PRODUCT.ONLY field defined as MCY, then the product cannot be created as a standalone ACCOUNTS contract. Only if PRODUCT.ONLY set to MCY, then the contract created under the product can act as a sub arrangement for MCY arrangement. |
| 90 | `AA.PRD.EPP.PRODUCT.LINE` | `AaProductDesigner_EppProductLine` | TField |  | Specifies an EPP Product Line. Validation Rules: Contains a free text value of the product line name. |
| 91 | `AA.PRD.PHASE` | `AaProductDesigner_Phase` |  |  |  |
| 92 | `AA.PRD.PHASE.START` | `AaProductDesigner_PhaseStart` |  |  |  |
| 93 | `AA.PRD.RESET.BASE.DATE` | `AaProductDesigner_ResetBaseDate` | TField |  | This field indicates which date has to be considered as a base during renewal activities for deriving the forward condition date Option: RENEWAL - will take the new product effective date as the base date. NULL - will continue with the previous product base date. |
