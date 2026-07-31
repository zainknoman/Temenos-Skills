# TAX.CODE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.TAX.CODE.PARAMETER` in `CG_ChargeConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TCP.PROPORTIONAL.CALC` | `TaxCodeParameter_ProportionalCalc` | TField |  | Will tax be calculated proportionally? Possible field values are Yes or No. Validation Rules:Yes,No |
| 2 | `TCP.UPDATE.TAX.DETAILS` | `TaxCodeParameter_UpdateTaxDetails` | TField |  | If this field is set to Yes then the file ST.TAX.CALC.DETAILS will be updated with the details. If this is set to No then this file will not be updated. Validation Rules:Yes,No |
| 3 | `TCP.TAX.BASE.TYPE` | `TaxCodeParameter_TaxBaseType` | TField |  | The New attribute will have the below 3 options: 1. Both (Default): Specifies both Positive and Negative Accruals will be considered for Tax calculation i.e. Net of Positive and Negative accruals (Current Functionality). 2. Positive: Denotes, only positive accrual amount will be considered for Tax Calculation. 3. Negative: Denotes, only Negative accrual amount will be considered for Tax Calculation. The field will be a �No Change� field, once an option is chosen, it cannot be changed at a later stage. |
| 4 | `TCP.RESERVED09` | `TaxCodeParameter_Reserved09` | TField |  |  |
| 5 | `TCP.RESERVED08` | `TaxCodeParameter_Reserved08` | TField |  |  |
| 6 | `TCP.RESERVED07` | `TaxCodeParameter_Reserved07` | TField |  |  |
| 7 | `TCP.RESERVED06` | `TaxCodeParameter_Reserved06` | TField |  |  |
| 8 | `TCP.RESERVED05` | `TaxCodeParameter_Reserved05` | TField |  |  |
| 9 | `TCP.RESERVED04` | `TaxCodeParameter_Reserved04` | TField |  |  |
| 10 | `TCP.RESERVED03` | `TaxCodeParameter_Reserved03` | TField |  |  |
| 11 | `TCP.RESERVED02` | `TaxCodeParameter_Reserved02` | TField |  |  |
| 12 | `TCP.RESERVED01` | `TaxCodeParameter_Reserved01` | TField |  |  |
| 13 | `TCP.LOCAL.REF` | `TaxCodeParameter_LocalRef` |  |  |  |
| 14 | `TCP.OVERRIDE` | `TaxCodeParameter_Override` |  |  |  |
| 15 | `TCP.RECORD.STATUS` | `TaxCodeParameter_RecordStatus` | String |  |  |
| 16 | `TCP.CURR.NO` | `TaxCodeParameter_CurrNo` | String |  |  |
| 17 | `TCP.INPUTTER` | `TaxCodeParameter_Inputter` |  |  |  |
| 18 | `TCP.DATE.TIME` | `TaxCodeParameter_DateTime` |  |  |  |
| 19 | `TCP.AUTHORISER` | `TaxCodeParameter_Authoriser` | String |  |  |
| 20 | `TCP.CO.CODE` | `TaxCodeParameter_CoCode` | String |  |  |
| 21 | `TCP.DEPT.CODE` | `TaxCodeParameter_DeptCode` | String |  |  |
| 22 | `TCP.AUDITOR.CODE` | `TaxCodeParameter_AuditorCode` | String |  |  |
| 23 | `TCP.AUDIT.DATE.TIME` | `TaxCodeParameter_AuditDateTime` | String |  |  |
