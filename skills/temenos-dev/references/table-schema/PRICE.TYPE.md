# PRICE.TYPE — Table Schema

> Source: `INSERTS/I_F.PRICE.TYPE` in `SC_SctPriceTypeUpdateAndProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PRT.DESCRIPTION` | `PriceType_Description` |  |  |  |
| 2 | `SC.PRT.SHORT.DESCR` | `PriceType_ShortDescr` |  |  |  |
| 3 | `SC.PRT.PERCENTAGE` | `PriceType_Percentage` | TField | Yes | Specifies whether the price quoted on a security with this PRICE.TYPE is expressed as a percentage or a multiple of the nominal value. Validation Rules: Y = Yes (a percentage), or N(O) = No (a multiple). (Mandatory Input) |
| 4 | `SC.PRT.MULTIPLY.FACTOR` | `PriceType_MultiplyFactor` | TField | Yes | Specifies the weighting attached to the price quoted on a security with this PRICE.TYPE. Where (as in the case of options) the nominal is a contract representing a given number of shares per unit, (of nominal). The user may use this field to indicate this value. Example: Where each unit of the nominal amount represents an option on 1000 shares the MULTIPLY.FACTOR would be 1000. Validation Rules: 1-9 numeric or "." characters. (Mandatory Input) The default value for this field is 1. |
| 5 | `SC.PRT.CALCULATION.METHOD` | `PriceType_CalculationMethod` | TField | Yes | Defines the formula used to calculate the consideration. This field is used to define the formula used to calculate the consideration. Examples: Where C = Consideration N = Nominal amount P = Price F = 1 or 100 (depending on the "PERCENTAGE" field) T = Tenor in days D = Number of interest days (360 or 365) (N * P * T) DISCOUNT C = N - --------------- D * 100 N * P PRICE C = ------- F N YIELD C = ---------------------- ( T x P ) 1 + ------------- (D x 100) Validation Rules: DISCOUNT, PRICE, YIELD (Mandatory Input) If "CALCULATION.METHOD" is YIELD or DISCOUNT the "PERCENTAGE" field must be YES. |
| 6 | `SC.PRT.DISC.INSTRUMENT` | `PriceType_DiscInstrument` | TField | Yes | Specifies whether or not the securities are discount instruments. In order to accrue or amortise the discount amount when a security is traded this flag must be st to "Y". This process will only be carried out for the banks own portfolios. Validation Rules: Values allowed are "Y" or "NO". (Mandatory Input) For "Y" to be entered the PERCENTAGE field must be set to "Y" and the CALCULATION.METHOD field cannot be set to "PRICE". For "NO" to be entered the CALCULATION.METHOD must be set to "PRICE". |
| 7 | `SC.PRT.PRICE.BASIS` | `PriceType_PriceBasis` | TField | No | Indicates which Price Basis is to be used. Indicates whether the price quoted for a Bond, includes or excludes interest accrued. Validation Rules: I = INC.ACCR, E = EXC.ACCR. (Optional Input.) If this field is null, the system assumes EXC.ACCR |
| 8 | `SC.PRT.RECORD.STATUS` | `PriceType_RecordStatus` | String |  | Insert text here Validation Rules: Rule 1 Rule 2 |
| 9 | `SC.PRT.CURR.NO` | `PriceType_CurrNo` | String |  |  |
| 10 | `SC.PRT.INPUTTER` | `PriceType_Inputter` |  |  |  |
| 11 | `SC.PRT.DATE.TIME` | `PriceType_DateTime` |  |  |  |
| 12 | `SC.PRT.AUTHORISER` | `PriceType_Authoriser` | String |  |  |
| 13 | `SC.PRT.CO.CODE` | `PriceType_CoCode` | String |  |  |
| 14 | `SC.PRT.DEPT.CODE` | `PriceType_DeptCode` | String |  |  |
| 15 | `SC.PRT.AUDITOR.CODE` | `PriceType_AuditorCode` | String |  |  |
| 16 | `SC.PRT.AUDIT.DATE.TIME` | `PriceType_AuditDateTime` | String |  |  |
| 17 | `SC.PRT.YLD.PRICE.ROUNDING` | `PriceType_YldPriceRounding` | TField |  |  |
