# CO.CURRENCY — Table Schema

> Source: `INSERTS/I_F.CO.CURRENCY` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COCU.MARGIN.RATE` | `CoCurrency_MarginRate` | TField | No | Optional field to allow the modification of the Advance Ratio based on the currency of the asset. It will allow + or minus followed by a number between 0 and 100. This will amend the Advance Ratio for assets valued in the currency by the number of percentage points either increasing �+� or decreasing �-� depending on the sign of the number. So the input into this field should be �+� or �-� followed by a number between 0 and 100. Validation Rules: Value needs to be between 0 to 100 |
| 2 | `COCU.ADJ.MARGIN.RATE` | `CoCurrency_AdjMarginRate` | TField | No | Optional field to allow the modification of the Lower Advance Ratio based on the currency of the asset. It will allow + or minus followed by a number between 0 and 100. This will amend the Lower Advance Ratio for assets valued in the currency by the number of percentage points either increasing �+� or decreasing �-� depending on the sign of the number. So the input into this field should be �+� or �-� followed by a number between 0 and 100. Validation Rules: Value needs to be between 0 to 100 |
| 3 | `COCU.PRODUCT` | `CoCurrency_Product` |  |  |  |
| 4 | `COCU.PRD.MARGIN.RATE` | `CoCurrency_PrdMarginRate` |  |  |  |
| 5 | `COCU.PRD.ADJ.MARGIN.RATE` | `CoCurrency_PrdAdjMarginRate` |  |  |  |
| 6 | `COCU.RESERVED.15` | `CoCurrency_Reserved15` |  |  |  |
| 7 | `COCU.RESERVED.14` | `CoCurrency_Reserved14` |  |  |  |
| 8 | `COCU.RESERVED.13` | `CoCurrency_Reserved13` |  |  |  |
| 9 | `COCU.RESERVED.12` | `CoCurrency_Reserved12` |  |  |  |
| 10 | `COCU.RESERVED.11` | `CoCurrency_Reserved11` |  |  |  |
| 11 | `COCU.CONCENTRATION.CAP` | `CoCurrency_ConcentrationCap` | TField | No | Optional field to hold the currency level concentration cap definition. Cap value defined at an individual or group of collateral, with respect to total collateral value, to ensure that a single asset is not used extensively, for example: each individual collateral asset value must not be greater than 30% of total customer collateral value. Value provided here will be applied to all the collateral assets valued in that specific currency held by the customer. Validation rules: 1. Optional field. If left blank, system will not do any Concentration Cap processing at this level. 2. Standard T24 Rate field with the values ranging from 0 to 100. |
| 12 | `COCU.EFFECTIVE.DATE` | `CoCurrency_EffectiveDate` |  |  |  |
| 13 | `COCU.NEW.MARGIN.RATE` | `CoCurrency_NewMarginRate` |  |  |  |
| 14 | `COCU.NEW.ADJ.MARGIN.RATE` | `CoCurrency_NewAdjMarginRate` |  |  |  |
| 15 | `COCU.NEW.PRODUCT` | `CoCurrency_NewProduct` |  |  |  |
| 16 | `COCU.NEW.PRD.MARGIN.RATE` | `CoCurrency_NewPrdMarginRate` |  |  |  |
| 17 | `COCU.NEW.PRD.ADJ.MARGIN.RATE` | `CoCurrency_NewPrdAdjMarginRate` |  |  |  |
| 18 | `COCU.RESERVED.4` | `CoCurrency_Reserved4` | TField |  |  |
| 19 | `COCU.RESERVED.3` | `CoCurrency_Reserved3` | TField |  |  |
| 20 | `COCU.RESERVED.2` | `CoCurrency_Reserved2` | TField |  |  |
| 21 | `COCU.RESERVED.1` | `CoCurrency_Reserved1` | TField |  |  |
| 22 | `COCU.NOTES` | `CoCurrency_Notes` |  |  |  |
| 23 | `COCU.LOCAL.REF` | `CoCurrency_LocalRef` |  |  |  |
| 24 | `COCU.OVERRIDE` | `CoCurrency_Override` |  |  |  |
| 25 | `COCU.RECORD.STATUS` | `CoCurrency_RecordStatus` | String |  |  |
| 26 | `COCU.CURR.NO` | `CoCurrency_CurrNo` | String |  |  |
| 27 | `COCU.INPUTTER` | `CoCurrency_Inputter` |  |  |  |
| 28 | `COCU.DATE.TIME` | `CoCurrency_DateTime` |  |  |  |
| 29 | `COCU.AUTHORISER` | `CoCurrency_Authoriser` | String |  |  |
| 30 | `COCU.CO.CODE` | `CoCurrency_CoCode` | String |  |  |
| 31 | `COCU.DEPT.CODE` | `CoCurrency_DeptCode` | String |  |  |
| 32 | `COCU.AUDITOR.CODE` | `CoCurrency_AuditorCode` | String |  |  |
| 33 | `COCU.AUDIT.DATE.TIME` | `CoCurrency_AuditDateTime` | String |  |  |
