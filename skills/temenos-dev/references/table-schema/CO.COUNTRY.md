# CO.COUNTRY — Table Schema

> Source: `INSERTS/I_F.CO.COUNTRY` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.COU.CONCENTRATION.CAP` | `CoCountry_ConcentrationCap` | TField | No | Optional field to hold the country level concentration cap definition. Cap value defined at an individual or group of collateral, with respect to total collateral value, to ensure that a single asset is not used extensively, for example: each individual collateral asset value must not be greater than 30% of total customer collateral value. Value provided here will be applied to all the collateral assets linked to that Country held be the customer. Validation rules: 1. Optional field. If left blank, system will not do any Concentration Cap processing at this level. 2. Standard T24 Rate field with the values ranging from 0 to 100. |
| 2 | `CO.COU.EMERGING.MARKET` | `CoCountry_EmergingMarket` | TField |  | An options field to control whether the country will be considered an emerging market. If set to "YES" then the specific country will be considered as an emerging market and the country will be updated in the EMERGING.MAEKRT record of CO.COUNTRY.GROUP. Validation Rules: 1. Valid values - YES_NO |
| 3 | `CO.COU.RESERVED.8` | `CoCountry_Reserved8` | TField |  |  |
| 4 | `CO.COU.RESERVED.7` | `CoCountry_Reserved7` | TField |  |  |
| 5 | `CO.COU.RESERVED.6` | `CoCountry_Reserved6` | TField |  |  |
| 6 | `CO.COU.RESERVED.5` | `CoCountry_Reserved5` | TField |  |  |
| 7 | `CO.COU.RESERVED.4` | `CoCountry_Reserved4` | TField |  |  |
| 8 | `CO.COU.RESERVED.3` | `CoCountry_Reserved3` | TField |  |  |
| 9 | `CO.COU.RESERVED.2` | `CoCountry_Reserved2` | TField |  |  |
| 10 | `CO.COU.RESERVED.1` | `CoCountry_Reserved1` | TField |  |  |
| 11 | `CO.COU.NOTES` | `CoCountry_Notes` |  |  |  |
| 12 | `CO.COU.LOCAL.REF` | `CoCountry_LocalRef` |  |  |  |
| 13 | `CO.COU.OVERRIDE` | `CoCountry_Override` |  |  |  |
| 14 | `CO.COU.RECORD.STATUS` | `CoCountry_RecordStatus` | String |  |  |
| 15 | `CO.COU.CURR.NO` | `CoCountry_CurrNo` | String |  |  |
| 16 | `CO.COU.INPUTTER` | `CoCountry_Inputter` |  |  |  |
| 17 | `CO.COU.DATE.TIME` | `CoCountry_DateTime` |  |  |  |
| 18 | `CO.COU.AUTHORISER` | `CoCountry_Authoriser` | String |  |  |
| 19 | `CO.COU.CO.CODE` | `CoCountry_CoCode` | String |  |  |
| 20 | `CO.COU.DEPT.CODE` | `CoCountry_DeptCode` | String |  |  |
| 21 | `CO.COU.AUDITOR.CODE` | `CoCountry_AuditorCode` | String |  |  |
| 22 | `CO.COU.AUDIT.DATE.TIME` | `CoCountry_AuditDateTime` | String |  |  |
