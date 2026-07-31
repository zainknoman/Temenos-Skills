# ARTAXS.EXEMPTION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ARTAXS.EXEMPTION.PARAMETER` in `ARTAXS_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXEMPT.PARAM.DESCRIPTION` | `ArtaxsExemptionParameter_Description` |  |  |  |
| 2 | `EXEMPT.PARAM.CONFIGURATION.STATUS` | `ArtaxsExemptionParameter_ConfigurationStatus` | TField |  | Status of the complete configuration for the Tax given in the ID. |
| 3 | `EXEMPT.PARAM.ACTIVITY` | `ArtaxsExemptionParameter_Activity` |  |  |  |
| 4 | `EXEMPT.PARAM.ACTIVITY.CLASS` | `ArtaxsExemptionParameter_ActivityClass` |  |  |  |
| 5 | `EXEMPT.PARAM.TAX.EXEMPT` | `ArtaxsExemptionParameter_TaxExempt` |  |  |  |
| 6 | `EXEMPT.PARAM.SCHEDULE.CHARGE` | `ArtaxsExemptionParameter_ScheduleCharge` |  |  |  |
| 7 | `EXEMPT.PARAM.CALCULATION.BASE` | `ArtaxsExemptionParameter_CalculationBase` |  |  |  |
| 8 | `EXEMPT.PARAM.BALANCE.TYPE` | `ArtaxsExemptionParameter_BalanceType` |  |  |  |
| 9 | `EXEMPT.PARAM.RATE.FREQUENCY` | `ArtaxsExemptionParameter_RateFrequency` |  |  |  |
| 10 | `EXEMPT.PARAM.SPECIAL.BASE.AMOUNT.ROUTINE` | `ArtaxsExemptionParameter_SpecialBaseAmountRoutine` |  |  |  |
| 11 | `EXEMPT.PARAM.SPECIAL.CALC.ROUTINE` | `ArtaxsExemptionParameter_SpecialCalcRoutine` |  |  |  |
| 12 | `EXEMPT.PARAM.ACTIVITY.HOLDERS` | `ArtaxsExemptionParameter_ActivityHolders` |  |  |  |
| 13 | `EXEMPT.PARAM.ACTIVITY.CLASS.HOLDERS` | `ArtaxsExemptionParameter_ActivityClassHolders` |  |  |  |
| 14 | `EXEMPT.PARAM.SCHEDULE.CHARGE.HOLDERS` | `ArtaxsExemptionParameter_ScheduleChargeHolders` |  |  |  |
| 15 | `EXEMPT.PARAM.HOLDERS.COMBINATION` | `ArtaxsExemptionParameter_HoldersCombination` |  |  |  |
| 16 | `EXEMPT.PARAM.TAX.EXEMPT.HOLDERS` | `ArtaxsExemptionParameter_TaxExemptHolders` |  |  |  |
| 17 | `EXEMPT.PARAM.TAX.APPLY.HOLDERS` | `ArtaxsExemptionParameter_TaxApplyHolders` |  |  |  |
| 18 | `EXEMPT.PARAM.JURISDICTION.APPLY.HOLDERS` | `ArtaxsExemptionParameter_JurisdictionApplyHolders` |  |  |  |
| 19 | `EXEMPT.PARAM.SPECIAL.RATE.ROUTINE` | `ArtaxsExemptionParameter_SpecialRateRoutine` |  |  |  |
| 20 | `EXEMPT.PARAM.TAX.RATE.FIELD` | `ArtaxsExemptionParameter_TaxRateField` |  |  |  |
| 21 | `EXEMPT.PARAM.TAX.EXEMPT.FIELD` | `ArtaxsExemptionParameter_TaxExemptField` |  |  |  |
| 22 | `EXEMPT.PARAM.TRANSACTIONAL.APPLICATION` | `ArtaxsExemptionParameter_TransactionalApplication` |  |  |  |
| 23 | `EXEMPT.PARAM.FIELD.NAME` | `ArtaxsExemptionParameter_FieldName` |  |  |  |
| 24 | `EXEMPT.PARAM.FIELD.COMPARISON` | `ArtaxsExemptionParameter_FieldComparison` |  |  |  |
| 25 | `EXEMPT.PARAM.FIELD.VALUE` | `ArtaxsExemptionParameter_FieldValue` |  |  |  |
| 26 | `EXEMPT.PARAM.FIELD.VALUE.EXEMPT` | `ArtaxsExemptionParameter_FieldValueExempt` |  |  |  |
| 27 | `EXEMPT.PARAM.JURISDICTION.APPLY.FIELD` | `ArtaxsExemptionParameter_JurisdictionApplyField` |  |  |  |
| 28 | `EXEMPT.PARAM.ACTIVITY.THRESHOLDS` | `ArtaxsExemptionParameter_ActivityThresholds` |  |  |  |
| 29 | `EXEMPT.PARAM.ACTIVITY.CLASS.THRESHOLDS` | `ArtaxsExemptionParameter_ActivityClassThresholds` |  |  |  |
| 30 | `EXEMPT.PARAM.SCHEDULE.CHARGE.THRESHOLDS` | `ArtaxsExemptionParameter_ScheduleChargeThresholds` |  |  |  |
| 31 | `EXEMPT.PARAM.CURRENCY` | `ArtaxsExemptionParameter_Currency` |  |  |  |
| 32 | `EXEMPT.PARAM.EXCHANGE.TYPE` | `ArtaxsExemptionParameter_ExchangeType` |  |  |  |
| 33 | `EXEMPT.PARAM.COMPARISON.TYPE` | `ArtaxsExemptionParameter_ComparisonType` |  |  |  |
| 34 | `EXEMPT.PARAM.BASE.AMOUNT` | `ArtaxsExemptionParameter_BaseAmount` |  |  |  |
| 35 | `EXEMPT.PARAM.MINIMUM.AMOUNT` | `ArtaxsExemptionParameter_MinimumAmount` |  |  |  |
| 36 | `EXEMPT.PARAM.MAXIMUM.AMOUNT` | `ArtaxsExemptionParameter_MaximumAmount` |  |  |  |
| 37 | `EXEMPT.PARAM.MINIMUM.RATE` | `ArtaxsExemptionParameter_MinimumRate` |  |  |  |
| 38 | `EXEMPT.PARAM.MAXIMUM.RATE` | `ArtaxsExemptionParameter_MaximumRate` |  |  |  |
| 39 | `EXEMPT.PARAM.RESERVED.15` | `ArtaxsExemptionParameter_Reserved15` | TField |  | Reserved for future use. |
| 40 | `EXEMPT.PARAM.RESERVED.14` | `ArtaxsExemptionParameter_Reserved14` | TField |  | Reserved for future use. |
| 41 | `EXEMPT.PARAM.RESERVED.13` | `ArtaxsExemptionParameter_Reserved13` | TField |  | Reserved for future use. |
| 42 | `EXEMPT.PARAM.RESERVED.12` | `ArtaxsExemptionParameter_Reserved12` | TField |  | Reserved for future use. |
| 43 | `EXEMPT.PARAM.RESERVED.11` | `ArtaxsExemptionParameter_Reserved11` | TField |  | Reserved for future use. |
| 44 | `EXEMPT.PARAM.RESERVED.10` | `ArtaxsExemptionParameter_Reserved10` | TField |  | Reserved for future use. |
| 45 | `EXEMPT.PARAM.RESERVED.9` | `ArtaxsExemptionParameter_Reserved9` | TField |  | Reserved for future use. |
| 46 | `EXEMPT.PARAM.RESERVED.8` | `ArtaxsExemptionParameter_Reserved8` | TField |  | Reserved for future use. |
| 47 | `EXEMPT.PARAM.RESERVED.7` | `ArtaxsExemptionParameter_Reserved7` | TField |  | Reserved for future use. |
| 48 | `EXEMPT.PARAM.RESERVED.6` | `ArtaxsExemptionParameter_Reserved6` | TField |  | Reserved for future use. |
| 49 | `EXEMPT.PARAM.RESERVED.5` | `ArtaxsExemptionParameter_Reserved5` | TField |  | Reserved for future use. |
| 50 | `EXEMPT.PARAM.RESERVED.4` | `ArtaxsExemptionParameter_Reserved4` | TField |  | Reserved for future use. |
| 51 | `EXEMPT.PARAM.RESERVED.3` | `ArtaxsExemptionParameter_Reserved3` | TField |  | Reserved for future use. |
| 52 | `EXEMPT.PARAM.RESERVED.2` | `ArtaxsExemptionParameter_Reserved2` | TField |  | Reserved for future use. |
| 53 | `EXEMPT.PARAM.RESERVED.1` | `ArtaxsExemptionParameter_Reserved1` | TField |  | Reserved for future use. |
| 54 | `EXEMPT.PARAM.COUNTRY.COMPANY` | `ArtaxsExemptionParameter_CountryCompany` | TField |  | First component of the ID can hold Company or Country code. |
| 55 | `EXEMPT.PARAM.TAX.TYPE` | `ArtaxsExemptionParameter_TaxType` | TField |  | Second component of the ID can hold the tax type |
| 56 | `EXEMPT.PARAM.PROPERTY.NAME` | `ArtaxsExemptionParameter_PropertyName` | TField |  | Third component of the ID can hold the property name |
| 57 | `EXEMPT.PARAM.JURISDICTION` | `ArtaxsExemptionParameter_Jurisdiction` | TField |  | Fourth component of the ID can hold the jurisdiction value. |
| 58 | `EXEMPT.PARAM.PRODUCT.ID` | `ArtaxsExemptionParameter_ProductId` | TField |  | Fifth component of the ID can hold the product id. |
| 59 | `EXEMPT.PARAM.OWNER` | `ArtaxsExemptionParameter_Owner` | TField |  | Sixth component of the ID can hold the owner value as BANK or null (Temenos owner) |
| 60 | `EXEMPT.PARAM.LOCAL.REF` | `ArtaxsExemptionParameter_LocalRef` |  |  |  |
| 61 | `EXEMPT.PARAM.OVERRIDE` | `ArtaxsExemptionParameter_Override` |  |  |  |
| 62 | `EXEMPT.PARAM.RECORD.STATUS` | `ArtaxsExemptionParameter_RecordStatus` | String |  |  |
| 63 | `EXEMPT.PARAM.CURR.NO` | `ArtaxsExemptionParameter_CurrNo` | String |  |  |
| 64 | `EXEMPT.PARAM.INPUTTER` | `ArtaxsExemptionParameter_Inputter` |  |  |  |
| 65 | `EXEMPT.PARAM.DATE.TIME` | `ArtaxsExemptionParameter_DateTime` |  |  |  |
| 66 | `EXEMPT.PARAM.AUTHORISER` | `ArtaxsExemptionParameter_Authoriser` | String |  |  |
| 67 | `EXEMPT.PARAM.CO.CODE` | `ArtaxsExemptionParameter_CoCode` | String |  |  |
| 68 | `EXEMPT.PARAM.DEPT.CODE` | `ArtaxsExemptionParameter_DeptCode` | String |  |  |
| 69 | `EXEMPT.PARAM.AUDITOR.CODE` | `ArtaxsExemptionParameter_AuditorCode` | String |  |  |
| 70 | `EXEMPT.PARAM.AUDIT.DATE.TIME` | `ArtaxsExemptionParameter_AuditDateTime` | String |  |  |
| 71 | `EXEMPT.PARAM.FX.CONVERSION` | `ArtaxsExemptionParameter_FxConversion` |  |  |  |
| 72 | `EXEMPT.PARAM.FX.DR.CR.CUSTOMER` | `ArtaxsExemptionParameter_FxDrCrCustomer` |  |  |  |
| 73 | `EXEMPT.PARAM.FX.TAX.EXEMPT` | `ArtaxsExemptionParameter_FxTaxExempt` |  |  |  |
| 74 | `EXEMPT.PARAM.FX.ACTIVITY.CCY` | `ArtaxsExemptionParameter_FxActivityCcy` |  |  |  |
| 75 | `EXEMPT.PARAM.FX.OPPOSITE.CCY` | `ArtaxsExemptionParameter_FxOppositeCcy` |  |  |  |
| 76 | `EXEMPT.PARAM.FX.JURISDICTION` | `ArtaxsExemptionParameter_FxJurisdiction` |  |  |  |
| 77 | `EXEMPT.PARAM.FX.JURIS.OPERAND` | `ArtaxsExemptionParameter_FxJurisOperand` |  |  |  |
| 78 | `EXEMPT.PARAM.EXEMPTION.CODE.HOLDERS` | `ArtaxsExemptionParameter_ExemptionCodeHolders` |  |  |  |
| 79 | `EXEMPT.PARAM.EXEMPTION.CODE.FIELD` | `ArtaxsExemptionParameter_ExemptionCodeField` |  |  |  |
