# AA.PRODUCT.PROOF — Table Schema

> Source: `INSERTS/I_F.AA.PRODUCT.PROOF` in `AA_ProductManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PRD.DESCRIPTION` | `AaProductProof_Description` |  |  |  |
| 2 | `AA.PRD.FULL.DESC` | `AaProductProof_FullDesc` |  |  |  |
| 3 | `AA.PRD.PRODUCT.GROUP` | `AaProductProof_ProductGroup` |  |  |  |
| 4 | `AA.PRD.PARENT.PRODUCT` | `AaProductProof_ParentProduct` |  |  |  |
| 5 | `AA.PRD.CURRENCY` | `AaProductProof_Currency` |  |  |  |
| 6 | `AA.PRD.RECONSTRUCT.SETTLEMENT` | `AaProductProof_ReconstructSettlement` |  |  |  |
| 7 | `AA.PRD.PROPERTY` | `AaProductProof_Property` |  |  |  |
| 8 | `AA.PRD.EFFECTIVE.BASE` | `AaProductProof_EffectiveBase` |  |  |  |
| 9 | `AA.PRD.PROPERTY.VARIATION` | `AaProductProof_PropertyVariation` |  |  |  |
| 10 | `AA.PRD.RESERVED16` | `AaProductProof_Reserved16` |  |  |  |
| 11 | `AA.PRD.RESERVED15` | `AaProductProof_Reserved15` |  |  |  |
| 12 | `AA.PRD.RESERVED14` | `AaProductProof_Reserved14` |  |  |  |
| 13 | `AA.PRD.RESERVED13` | `AaProductProof_Reserved13` |  |  |  |
| 14 | `AA.PRD.PRD.PROPERTY` | `AaProductProof_PrdProperty` |  |  |  |
| 15 | `AA.PRD.PC.PRD.PR` | `AaProductProof_PcPrdPr` |  |  |  |
| 16 | `AA.PRD.ARR.LINK` | `AaProductProof_ArrLink` |  |  |  |
| 17 | `AA.PRD.RESERVED11` | `AaProductProof_Reserved11` |  |  |  |
| 18 | `AA.PRD.EFFECTIVE` | `AaProductProof_Effective` |  |  |  |
| 19 | `AA.PRD.INHERITANCE.ONLY` | `AaProductProof_InheritanceOnly` |  |  |  |
| 20 | `AA.PRD.DEFAULT.PRODUCT` | `AaProductProof_DefaultProduct` |  |  |  |
| 21 | `AA.PRD.AVAILABLE.COMPANY` | `AaProductProof_AvailableCompany` |  |  |  |
| 22 | `AA.PRD.OWNING.COMPANY` | `AaProductProof_OwningCompany` |  |  |  |
| 23 | `AA.PRD.CALC.PROPERTY` | `AaProductProof_CalcProperty` |  |  |  |
| 24 | `AA.PRD.SOURCE.TYPE` | `AaProductProof_SourceType` |  |  |  |
| 25 | `AA.PRD.SOURCE.BALANCE` | `AaProductProof_SourceBalance` |  |  |  |
| 26 | `AA.PRD.SOURCE.PROPERTY` | `AaProductProof_SourceProperty` |  |  |  |
| 27 | `AA.PRD.TIER.SOURCE.TYPE` | `AaProductProof_TierSourceType` |  |  |  |
| 28 | `AA.PRD.TIER.SOURCE.BALANCE` | `AaProductProof_TierSourceBalance` |  |  |  |
| 29 | `AA.PRD.TIER.SOURCE.PROPERTY` | `AaProductProof_TierSourceProperty` |  |  |  |
| 30 | `AA.PRD.LOCAL.REF` | `AaProductProof_LocalRef` |  |  |  |
| 31 | `AA.PRD.PRODUCT` | `AaProductProof_Product` |  |  |  |
| 32 | `AA.PRD.EFFECTIVE.DATE` | `AaProductProof_EffectiveDate` |  |  |  |
| 33 | `AA.PRD.VARIATION` | `AaProductProof_Variation` |  |  |  |
| 34 | `AA.PRD.VARIATION.DEFAULT` | `AaProductProof_VariationDefault` |  |  |  |
| 35 | `AA.PRD.ADVANCE.RATEFIX.PERIOD` | `AaProductProof_AdvanceRatefixPeriod` |  |  |  |
| 36 | `AA.PRD.PRODUCT.PURPOSE` | `AaProductProof_ProductPurpose` |  |  |  |
| 37 | `AA.PRD.INHERITANCE.CURRENCY` | `AaProductProof_InheritanceCurrency` |  |  |  |
| 38 | `AA.PRD.TRACK.EFF.PERIOD` | `AaProductProof_TrackEffPeriod` |  |  |  |
| 39 | `AA.PRD.TRACK.PROPERTY.CLASS` | `AaProductProof_TrackPropertyClass` |  |  |  |
| 40 | `AA.PRD.ORGANIZATION.LEVEL` | `AaProductProof_OrganizationLevel` |  |  |  |
| 41 | `AA.PRD.ORGANIZATION.CODE` | `AaProductProof_OrganizationCode` |  |  |  |
| 42 | `AA.PRD.LINE.OF.BUSINESS` | `AaProductProof_LineOfBusiness` |  |  |  |
| 43 | `AA.PRD.IN.PROPERTY` | `AaProductProof_InProperty` |  |  |  |
| 44 | `AA.PRD.IN.PRODUCT` | `AaProductProof_InProduct` |  |  |  |
| 45 | `AA.PRD.IN.EFF.BASE` | `AaProductProof_InEffBase` |  |  |  |
| 46 | `AA.PRD.IN.PR.VAR` | `AaProductProof_InPrVar` |  |  |  |
| 47 | `AA.PRD.IN.PRD.PR` | `AaProductProof_InPrdPr` |  |  |  |
| 48 | `AA.PRD.IN.PC.PRD.PR` | `AaProductProof_InPcPrdPr` |  |  |  |
| 49 | `AA.PRD.RESERVED04` | `AaProductProof_Reserved04` |  |  |  |
| 50 | `AA.PRD.RESERVED03` | `AaProductProof_Reserved03` |  |  |  |
| 51 | `AA.PRD.RESERVED02` | `AaProductProof_Reserved02` |  |  |  |
| 52 | `AA.PRD.RESERVED01` | `AaProductProof_Reserved01` |  |  |  |
| 53 | `AA.PRD.IN.ARR.LINK` | `AaProductProof_InArrLink` |  |  |  |
| 54 | `AA.PRD.IN.EFF` | `AaProductProof_InEff` |  |  |  |
| 55 | `AA.PRD.IN.PR.SOURCE` | `AaProductProof_InPrSource` |  |  |  |
| 56 | `AA.PRD.IN.CALC.PR` | `AaProductProof_InCalcPr` |  |  |  |
| 57 | `AA.PRD.IN.SR.TYPE` | `AaProductProof_InSrType` |  |  |  |
| 58 | `AA.PRD.IN.SR.BAL` | `AaProductProof_InSrBal` |  |  |  |
| 59 | `AA.PRD.IN.SR.PR` | `AaProductProof_InSrPr` |  |  |  |
| 60 | `AA.PRD.IN.SR.TR.TYPE` | `AaProductProof_InSrTrType` |  |  |  |
| 61 | `AA.PRD.IN.SR.TR.BAL` | `AaProductProof_InSrTrBal` |  |  |  |
| 62 | `AA.PRD.IN.SR.TR.PR` | `AaProductProof_InSrTrPr` |  |  |  |
| 63 | `AA.PRD.OVERRIDE` | `AaProductProof_Override` |  |  |  |
| 64 | `AA.PRD.RECORD.STATUS` | `AaProductProof_RecordStatus` |  |  |  |
| 65 | `AA.PRD.CURR.NO` | `AaProductProof_CurrNo` |  |  |  |
| 66 | `AA.PRD.INPUTTER` | `AaProductProof_Inputter` |  |  |  |
| 67 | `AA.PRD.DATE.TIME` | `AaProductProof_DateTime` |  |  |  |
| 68 | `AA.PRD.AUTHORISER` | `AaProductProof_Authoriser` |  |  |  |
| 69 | `AA.PRD.CO.CODE` | `AaProductProof_CoCode` |  |  |  |
| 70 | `AA.PRD.DEPT.CODE` | `AaProductProof_DeptCode` |  |  |  |
| 71 | `AA.PRD.AUDITOR.CODE` | `AaProductProof_AuditorCode` |  |  |  |
| 72 | `AA.PRD.AUDIT.DATE.TIME` | `AaProductProof_AuditDateTime` |  |  |  |
| 73 | `AA.PRD.CHANNEL` | `AaProductProof_Channel` |  |  |  |
| 74 | `AA.PRD.CHANNEL.EXCLUDE` | `AaProductProof_ChannelExclude` |  |  |  |
| 75 | `AA.PRD.ORGANISATION.EXCLUDE` | `AaProductProof_OrganisationExclude` |  |  |  |
| 76 | `AA.PRD.LINE.OF.BUSINESS.EXCLUDE` | `AaProductProof_LineOfBusinessExclude` |  |  |  |
| 77 | `AA.PRD.BUNDLE.ONLY` | `AaProductProof_BundleOnly` |  |  |  |
| 78 | `AA.PRD.PRODUCT.ATTRIBUTE` | `AaProductProof_ProductAttribute` |  |  |  |
| 79 | `AA.PRD.SOURCE.APPLICATION` | `AaProductProof_SourceApplication` |  |  |  |
| 80 | `AA.PRD.SOURCE.REFERENCE` | `AaProductProof_SourceReference` |  |  |  |
