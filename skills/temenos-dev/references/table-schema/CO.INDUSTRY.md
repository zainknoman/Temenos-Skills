# CO.INDUSTRY — Table Schema

> Source: `INSERTS/I_F.CO.INDUSTRY` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.IN.CONCENTRATION.CAP` | `CoIndustry_ConcentrationCap` | TField |  | Specifies the Concentration cap to be considered for the SC.INDUSTRY. Concentration cap is a cap value defined for a collateral, with respect to total collateral value, to ensure that a single asset is not used extensively. Validation Rules: 1. Standard T24 Rate field with the values ranging from 0 to 100. |
| 2 | `CO.IN.RESERVED.9` | `CoIndustry_Reserved9` | TField |  |  |
| 3 | `CO.IN.RESERVED.8` | `CoIndustry_Reserved8` | TField |  |  |
| 4 | `CO.IN.RESERVED.7` | `CoIndustry_Reserved7` | TField |  |  |
| 5 | `CO.IN.RESERVED.6` | `CoIndustry_Reserved6` | TField |  |  |
| 6 | `CO.IN.RESERVED.5` | `CoIndustry_Reserved5` | TField |  |  |
| 7 | `CO.IN.RESERVED.4` | `CoIndustry_Reserved4` | TField |  |  |
| 8 | `CO.IN.RESERVED.3` | `CoIndustry_Reserved3` | TField |  |  |
| 9 | `CO.IN.RESERVED.2` | `CoIndustry_Reserved2` | TField |  |  |
| 10 | `CO.IN.RESERVED.1` | `CoIndustry_Reserved1` | TField |  |  |
| 11 | `CO.IN.LOCAL.REF` | `CoIndustry_LocalRef` |  |  |  |
| 12 | `CO.IN.OVERRIDE` | `CoIndustry_Override` |  |  |  |
| 13 | `CO.IN.RECORD.STATUS` | `CoIndustry_RecordStatus` | String |  |  |
| 14 | `CO.IN.CURR.NO` | `CoIndustry_CurrNo` | String |  |  |
| 15 | `CO.IN.INPUTTER` | `CoIndustry_Inputter` |  |  |  |
| 16 | `CO.IN.DATE.TIME` | `CoIndustry_DateTime` |  |  |  |
| 17 | `CO.IN.AUTHORISER` | `CoIndustry_Authoriser` | String |  |  |
| 18 | `CO.IN.CO.CODE` | `CoIndustry_CoCode` | String |  |  |
| 19 | `CO.IN.DEPT.CODE` | `CoIndustry_DeptCode` | String |  |  |
| 20 | `CO.IN.AUDITOR.CODE` | `CoIndustry_AuditorCode` | String |  |  |
| 21 | `CO.IN.AUDIT.DATE.TIME` | `CoIndustry_AuditDateTime` | String |  |  |
