# TAX.TYPE — Table Schema

> Source: `INSERTS/I_F.TAX.TYPE` in `CG_ChargeConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAX.TTY.DESCRIPTION` | `TaxType_Description` |  |  |  |
| 2 | `TAX.TTY.EFFECTIVE.DATE` | `TaxType_EffectiveDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `TAX.TTY.LOCAL.TAX.PARAM` | `TaxType_LocalTaxParam` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `TAX.TTY.CUST.CHK.RTN` | `TaxType_CustChkRtn` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `TAX.TTY.HIGHEST.TAX` | `TaxType_HighestTax` | TField | No | When performing tax calculation based on Joint customer relationship definition, would pick the tax which has highest percentage and apply that to all customers of the group Can be set to YES or NO or None When set to YES � calculation should consider the highest tax % for calculating the tax for all the customers of a customer relationship When set to NO/None � calculation would not consider the highest tax % logic and would calculate tax for individual customers based on the individual customer tax % Optional field. Default value is none |
| 6 | `TAX.TTY.APPLY.SPLIT` | `TaxType_ApplySplit` | TField | No | This field is used to parameterize whether tax split can be applied for a specific tax type or not .Can be set to either YES or No or left blank Validation Rules YES - Tax split is allowed for a tax type . NO / None � Tax would not be split although joint customer are part of the transaction .Optional field.Default value is none |
| 7 | `TAX.TTY.RESERVED5` | `TaxType_Reserved5` | TField |  |  |
| 8 | `TAX.TTY.RESERVED4` | `TaxType_Reserved4` | TField |  |  |
| 9 | `TAX.TTY.RESERVED3` | `TaxType_Reserved3` | TField |  |  |
| 10 | `TAX.TTY.LOCAL.REF` | `TaxType_LocalRef` |  |  |  |
| 11 | `TAX.TTY.RESERVED1` | `TaxType_Reserved1` | TField |  |  |
| 12 | `TAX.TTY.RECORD.STATUS` | `TaxType_RecordStatus` | String |  |  |
| 13 | `TAX.TTY.CURR.NO` | `TaxType_CurrNo` | String |  |  |
| 14 | `TAX.TTY.INPUTTER` | `TaxType_Inputter` |  |  |  |
| 15 | `TAX.TTY.DATE.TIME` | `TaxType_DateTime` |  |  |  |
| 16 | `TAX.TTY.AUTHORISER` | `TaxType_Authoriser` | String |  |  |
| 17 | `TAX.TTY.CO.CODE` | `TaxType_CoCode` | String |  |  |
| 18 | `TAX.TTY.DEPT.CODE` | `TaxType_DeptCode` | String |  |  |
| 19 | `TAX.TTY.AUDITOR.CODE` | `TaxType_AuditorCode` | String |  |  |
| 20 | `TAX.TTY.AUDIT.DATE.TIME` | `TaxType_AuditDateTime` | String |  |  |
