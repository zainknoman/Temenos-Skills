# CO.COUNTRY.GROUP — Table Schema

> Source: `INSERTS/I_F.CO.COUNTRY.GROUP` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.CG.DESCRIPTION` | `CoCountryGroup_Description` |  |  |  |
| 2 | `CO.CG.CONCENTRATION.CAP` | `CoCountryGroup_ConcentrationCap` | TField | No | Specifies the concentration cap definition to the countries that are grouped together based on the 'EMERGING.MARKET' setup defined in CO.COUNTRY. Once defined for the countries in the group, this concentration cap value will be used for assets in the same country in the same way as an individually defined country cap. If the assets associated with the country group exceeds the concentration cap then the concentration cap will be applied to reduce the collateral value of the customer and produce a concentration cap alert. Validation rules: 1. Optional field. If left blank, system will not do any Concentration Cap processing at this level. 2. Standard T24 Rate field with the values ranging from 0 to 100. |
| 3 | `CO.CG.COUNTRY` | `CoCountryGroup_Country` |  |  |  |
| 4 | `CO.CG.RESERVED.7` | `CoCountryGroup_Reserved7` | TField |  |  |
| 5 | `CO.CG.RESERVED.6` | `CoCountryGroup_Reserved6` | TField |  |  |
| 6 | `CO.CG.RESERVED.5` | `CoCountryGroup_Reserved5` | TField |  |  |
| 7 | `CO.CG.RESERVED.4` | `CoCountryGroup_Reserved4` | TField |  |  |
| 8 | `CO.CG.RESERVED.3` | `CoCountryGroup_Reserved3` | TField |  |  |
| 9 | `CO.CG.RESERVED.2` | `CoCountryGroup_Reserved2` | TField |  |  |
| 10 | `CO.CG.RESERVED.1` | `CoCountryGroup_Reserved1` | TField |  |  |
| 11 | `CO.CG.LOCAL.REF` | `CoCountryGroup_LocalRef` |  |  |  |
| 12 | `CO.CG.OVERRIDE` | `CoCountryGroup_Override` |  |  |  |
| 13 | `CO.CG.RECORD.STATUS` | `CoCountryGroup_RecordStatus` | String |  |  |
| 14 | `CO.CG.CURR.NO` | `CoCountryGroup_CurrNo` | String |  |  |
| 15 | `CO.CG.INPUTTER` | `CoCountryGroup_Inputter` |  |  |  |
| 16 | `CO.CG.DATE.TIME` | `CoCountryGroup_DateTime` |  |  |  |
| 17 | `CO.CG.AUTHORISER` | `CoCountryGroup_Authoriser` | String |  |  |
| 18 | `CO.CG.CO.CODE` | `CoCountryGroup_CoCode` | String |  |  |
| 19 | `CO.CG.DEPT.CODE` | `CoCountryGroup_DeptCode` | String |  |  |
| 20 | `CO.CG.AUDITOR.CODE` | `CoCountryGroup_AuditorCode` | String |  |  |
| 21 | `CO.CG.AUDIT.DATE.TIME` | `CoCountryGroup_AuditDateTime` | String |  |  |
