# CMBASE.TAX.EXEMPTION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CMBASE.TAX.EXEMPTION.PARAMETER` in `CMBASE_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAX.EXEMPT.PARAM.DESCRIPTION` | `CmbaseTaxExemptionParameter_Description` |  |  |  |
| 2 | `TAX.EXEMPT.PARAM.CONFIGURATION.STATUS` | `CmbaseTaxExemptionParameter_ConfigurationStatus` | TField |  | Status of the complete configuration for the Tax given in the ID. |
| 3 | `TAX.EXEMPT.PARAM.ACTIVITY` | `CmbaseTaxExemptionParameter_Activity` |  |  |  |
| 4 | `TAX.EXEMPT.PARAM.ACTIVITY.CLASS` | `CmbaseTaxExemptionParameter_ActivityClass` |  |  |  |
| 5 | `TAX.EXEMPT.PARAM.TAX.EXEMPT` | `CmbaseTaxExemptionParameter_TaxExempt` |  |  |  |
| 6 | `TAX.EXEMPT.PARAM.SCHEDULE.CHARGE` | `CmbaseTaxExemptionParameter_ScheduleCharge` |  |  |  |
| 7 | `TAX.EXEMPT.PARAM.CALCULATION.BASE` | `CmbaseTaxExemptionParameter_CalculationBase` |  |  |  |
| 8 | `TAX.EXEMPT.PARAM.BALANCE.TYPE` | `CmbaseTaxExemptionParameter_BalanceType` |  |  |  |
| 9 | `TAX.EXEMPT.PARAM.RATE.FREQUENCY` | `CmbaseTaxExemptionParameter_RateFrequency` |  |  |  |
| 10 | `TAX.EXEMPT.PARAM.SPECIAL.BASE.AMOUNT.ROUTINE` | `CmbaseTaxExemptionParameter_SpecialBaseAmountRoutine` |  |  |  |
| 11 | `TAX.EXEMPT.PARAM.SPECIAL.CALC.ROUTINE` | `CmbaseTaxExemptionParameter_SpecialCalcRoutine` |  |  |  |
| 12 | `TAX.EXEMPT.PARAM.ACTIVITY.HOLDERS` | `CmbaseTaxExemptionParameter_ActivityHolders` |  |  |  |
| 13 | `TAX.EXEMPT.PARAM.ACTIVITY.CLASS.HOLDERS` | `CmbaseTaxExemptionParameter_ActivityClassHolders` |  |  |  |
| 14 | `TAX.EXEMPT.PARAM.SCHEDULE.CHARGE.HOLDERS` | `CmbaseTaxExemptionParameter_ScheduleChargeHolders` |  |  |  |
| 15 | `TAX.EXEMPT.PARAM.HOLDERS.COMBINATION` | `CmbaseTaxExemptionParameter_HoldersCombination` |  |  |  |
| 16 | `TAX.EXEMPT.PARAM.TAX.EXEMPT.HOLDERS` | `CmbaseTaxExemptionParameter_TaxExemptHolders` |  |  |  |
| 17 | `TAX.EXEMPT.PARAM.TAX.APPLY.HOLDERS` | `CmbaseTaxExemptionParameter_TaxApplyHolders` |  |  |  |
| 18 | `TAX.EXEMPT.PARAM.JURISDICTION.APPLY.HOLDERS` | `CmbaseTaxExemptionParameter_JurisdictionApplyHolders` |  |  |  |
| 19 | `TAX.EXEMPT.PARAM.SPECIAL.RATE.ROUTINE` | `CmbaseTaxExemptionParameter_SpecialRateRoutine` |  |  |  |
| 20 | `TAX.EXEMPT.PARAM.TAX.RATE.FIELD` | `CmbaseTaxExemptionParameter_TaxRateField` |  |  |  |
| 21 | `TAX.EXEMPT.PARAM.TAX.EXEMPT.FIELD` | `CmbaseTaxExemptionParameter_TaxExemptField` |  |  |  |
| 22 | `TAX.EXEMPT.PARAM.ACTIVITY.TRANSACTIONAL` | `CmbaseTaxExemptionParameter_ActivityTransactional` |  |  |  |
| 23 | `TAX.EXEMPT.PARAM.ACTIVITY.CLASS.TRANSACTIONAL` | `CmbaseTaxExemptionParameter_ActivityClassTransactional` |  |  |  |
| 24 | `TAX.EXEMPT.PARAM.SCHEDULE.CHARGE.TRANSACTIONAL` | `CmbaseTaxExemptionParameter_ScheduleChargeTransactional` |  |  |  |
| 25 | `TAX.EXEMPT.PARAM.TRANSACTIONAL.APPLICATION` | `CmbaseTaxExemptionParameter_TransactionalApplication` |  |  |  |
| 26 | `TAX.EXEMPT.PARAM.FIELD.NAME` | `CmbaseTaxExemptionParameter_FieldName` |  |  |  |
| 27 | `TAX.EXEMPT.PARAM.FIELD.COMPARISON` | `CmbaseTaxExemptionParameter_FieldComparison` |  |  |  |
| 28 | `TAX.EXEMPT.PARAM.FIELD.VALUE` | `CmbaseTaxExemptionParameter_FieldValue` |  |  |  |
| 29 | `TAX.EXEMPT.PARAM.FIELD.VALUE.EXEMPT` | `CmbaseTaxExemptionParameter_FieldValueExempt` |  |  |  |
| 30 | `TAX.EXEMPT.PARAM.JURISDICTION.APPLY.FIELD` | `CmbaseTaxExemptionParameter_JurisdictionApplyField` |  |  |  |
| 31 | `TAX.EXEMPT.PARAM.ACTIVITY.FX` | `CmbaseTaxExemptionParameter_ActivityFx` |  |  |  |
| 32 | `TAX.EXEMPT.PARAM.ACTIVITY.CLASS.FX` | `CmbaseTaxExemptionParameter_ActivityClassFx` |  |  |  |
| 33 | `TAX.EXEMPT.PARAM.FX.CONVERSION` | `CmbaseTaxExemptionParameter_FxConversion` |  |  |  |
| 34 | `TAX.EXEMPT.PARAM.FX.DR.CR.CUSTOMER` | `CmbaseTaxExemptionParameter_FxDrCrCustomer` |  |  |  |
| 35 | `TAX.EXEMPT.PARAM.FX.TAX.EXEMPT` | `CmbaseTaxExemptionParameter_FxTaxExempt` |  |  |  |
| 36 | `TAX.EXEMPT.PARAM.ACTIVITY.THRESHOLDS` | `CmbaseTaxExemptionParameter_ActivityThresholds` |  |  |  |
| 37 | `TAX.EXEMPT.PARAM.ACTIVITY.CLASS.THRESHOLDS` | `CmbaseTaxExemptionParameter_ActivityClassThresholds` |  |  |  |
| 38 | `TAX.EXEMPT.PARAM.SCHEDULE.CHARGE.THRESHOLDS` | `CmbaseTaxExemptionParameter_ScheduleChargeThresholds` |  |  |  |
| 39 | `TAX.EXEMPT.PARAM.CURRENCY` | `CmbaseTaxExemptionParameter_Currency` |  |  |  |
| 40 | `TAX.EXEMPT.PARAM.EXCHANGE.TYPE` | `CmbaseTaxExemptionParameter_ExchangeType` |  |  |  |
| 41 | `TAX.EXEMPT.PARAM.COMPARISON.TYPE` | `CmbaseTaxExemptionParameter_ComparisonType` |  |  |  |
| 42 | `TAX.EXEMPT.PARAM.BASE.AMOUNT` | `CmbaseTaxExemptionParameter_BaseAmount` |  |  |  |
| 43 | `TAX.EXEMPT.PARAM.MINIMUM.AMOUNT` | `CmbaseTaxExemptionParameter_MinimumAmount` |  |  |  |
| 44 | `TAX.EXEMPT.PARAM.MAXIMUM.AMOUNT` | `CmbaseTaxExemptionParameter_MaximumAmount` |  |  |  |
| 45 | `TAX.EXEMPT.PARAM.MINIMUM.RATE` | `CmbaseTaxExemptionParameter_MinimumRate` |  |  |  |
| 46 | `TAX.EXEMPT.PARAM.MAXIMUM.RATE` | `CmbaseTaxExemptionParameter_MaximumRate` |  |  |  |
| 47 | `TAX.EXEMPT.PARAM.RESERVED.15` | `CmbaseTaxExemptionParameter_Reserved15` | TField |  | Reserved for future use. |
| 48 | `TAX.EXEMPT.PARAM.RESERVED.14` | `CmbaseTaxExemptionParameter_Reserved14` | TField |  | Reserved for future use. |
| 49 | `TAX.EXEMPT.PARAM.RESERVED.13` | `CmbaseTaxExemptionParameter_Reserved13` | TField |  | Reserved for future use. |
| 50 | `TAX.EXEMPT.PARAM.RESERVED.12` | `CmbaseTaxExemptionParameter_Reserved12` | TField |  | Reserved for future use. |
| 51 | `TAX.EXEMPT.PARAM.RESERVED.11` | `CmbaseTaxExemptionParameter_Reserved11` | TField |  | Reserved for future use. |
| 52 | `TAX.EXEMPT.PARAM.RESERVED.10` | `CmbaseTaxExemptionParameter_Reserved10` | TField |  | Reserved for future use. |
| 53 | `TAX.EXEMPT.PARAM.RESERVED.9` | `CmbaseTaxExemptionParameter_Reserved9` | TField |  | Reserved for future use. |
| 54 | `TAX.EXEMPT.PARAM.RESERVED.8` | `CmbaseTaxExemptionParameter_Reserved8` | TField |  | Reserved for future use. |
| 55 | `TAX.EXEMPT.PARAM.RESERVED.7` | `CmbaseTaxExemptionParameter_Reserved7` | TField |  | Reserved for future use. |
| 56 | `TAX.EXEMPT.PARAM.RESERVED.6` | `CmbaseTaxExemptionParameter_Reserved6` | TField |  | Reserved for future use. |
| 57 | `TAX.EXEMPT.PARAM.RESERVED.5` | `CmbaseTaxExemptionParameter_Reserved5` | TField |  | Reserved for future use. |
| 58 | `TAX.EXEMPT.PARAM.RESERVED.4` | `CmbaseTaxExemptionParameter_Reserved4` | TField |  | Reserved for future use. |
| 59 | `TAX.EXEMPT.PARAM.RESERVED.3` | `CmbaseTaxExemptionParameter_Reserved3` | TField |  | Reserved for future use. |
| 60 | `TAX.EXEMPT.PARAM.RESERVED.2` | `CmbaseTaxExemptionParameter_Reserved2` | TField |  | Reserved for future use. |
| 61 | `TAX.EXEMPT.PARAM.RESERVED.1` | `CmbaseTaxExemptionParameter_Reserved1` | TField |  | Reserved for future use. |
| 62 | `TAX.EXEMPT.PARAM.COUNTRY.COMPANY` | `CmbaseTaxExemptionParameter_CountryCompany` | TField |  | First component of the ID can hold Company or Country code. |
| 63 | `TAX.EXEMPT.PARAM.TAX.TYPE` | `CmbaseTaxExemptionParameter_TaxType` | TField |  | Second component of the ID can hold the tax type |
| 64 | `TAX.EXEMPT.PARAM.PROPERTY.NAME` | `CmbaseTaxExemptionParameter_PropertyName` | TField |  | Third component of the ID can hold the property name |
| 65 | `TAX.EXEMPT.PARAM.JURISDICTION` | `CmbaseTaxExemptionParameter_Jurisdiction` | TField |  | Fourth component of the ID can hold the jurisdiction value. |
| 66 | `TAX.EXEMPT.PARAM.PRODUCT.ID` | `CmbaseTaxExemptionParameter_ProductId` | TField |  | Fifth component of the ID can hold the product id. |
| 67 | `TAX.EXEMPT.PARAM.OWNER` | `CmbaseTaxExemptionParameter_Owner` | TField |  | Sixth component of the ID can hold the owner value as BANK or null (Temenos owner) |
| 68 | `TAX.EXEMPT.PARAM.LOCAL.REF` | `CmbaseTaxExemptionParameter_LocalRef` |  |  |  |
| 69 | `TAX.EXEMPT.PARAM.OVERRIDE` | `CmbaseTaxExemptionParameter_Override` |  |  |  |
| 70 | `TAX.EXEMPT.PARAM.RECORD.STATUS` | `CmbaseTaxExemptionParameter_RecordStatus` | String |  |  |
| 71 | `TAX.EXEMPT.PARAM.CURR.NO` | `CmbaseTaxExemptionParameter_CurrNo` | String |  |  |
| 72 | `TAX.EXEMPT.PARAM.INPUTTER` | `CmbaseTaxExemptionParameter_Inputter` |  |  |  |
| 73 | `TAX.EXEMPT.PARAM.DATE.TIME` | `CmbaseTaxExemptionParameter_DateTime` |  |  |  |
| 74 | `TAX.EXEMPT.PARAM.AUTHORISER` | `CmbaseTaxExemptionParameter_Authoriser` | String |  |  |
| 75 | `TAX.EXEMPT.PARAM.CO.CODE` | `CmbaseTaxExemptionParameter_CoCode` | String |  |  |
| 76 | `TAX.EXEMPT.PARAM.DEPT.CODE` | `CmbaseTaxExemptionParameter_DeptCode` | String |  |  |
| 77 | `TAX.EXEMPT.PARAM.AUDITOR.CODE` | `CmbaseTaxExemptionParameter_AuditorCode` | String |  |  |
| 78 | `TAX.EXEMPT.PARAM.AUDIT.DATE.TIME` | `CmbaseTaxExemptionParameter_AuditDateTime` | String |  |  |
