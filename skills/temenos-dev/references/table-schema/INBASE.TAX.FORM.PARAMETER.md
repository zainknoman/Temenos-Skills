# INBASE.TAX.FORM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.INBASE.TAX.FORM.PARAMETER` in `INBASE_CustomerValidations.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INBASE.TAX.DOC.WITH.EXP.DATE` | `InbaseTaxFormParameter_DocWithExpDate` |  |  |  |
| 2 | `INBASE.TAX.TAX.FORM.VALUE` | `InbaseTaxFormParameter_TaxFormValue` | TField |  | Tax Form After year End - This will be a drop down value from TAX.FORM field of CUSTOMER application to which the value has to be reset after the Tax form Expires. |
| 3 | `INBASE.TAX.RESERVED.10` | `InbaseTaxFormParameter_Reserved10` | TField |  | This field is reserved for future purpose |
| 4 | `INBASE.TAX.RESERVED.9` | `InbaseTaxFormParameter_Reserved9` | TField |  | This field is reserved for future purpose |
| 5 | `INBASE.TAX.RESERVED.8` | `InbaseTaxFormParameter_Reserved8` | TField |  | This field is reserved for future purpose |
| 6 | `INBASE.TAX.RESERVED.7` | `InbaseTaxFormParameter_Reserved7` | TField |  | This field is reserved for future purpose |
| 7 | `INBASE.TAX.RESERVED.6` | `InbaseTaxFormParameter_Reserved6` | TField |  | This field is reserved for future purpose |
| 8 | `INBASE.TAX.RESERVED.5` | `InbaseTaxFormParameter_Reserved5` | TField |  | This field is reserved for future purpose |
| 9 | `INBASE.TAX.RESERVED.4` | `InbaseTaxFormParameter_Reserved4` | TField |  | This field is reserved for future purpose |
| 10 | `INBASE.TAX.RESERVED.3` | `InbaseTaxFormParameter_Reserved3` | TField |  | This field is reserved for future purpose |
| 11 | `INBASE.TAX.RESERVED.2` | `InbaseTaxFormParameter_Reserved2` | TField |  | This field is reserved for future purpose |
| 12 | `INBASE.TAX.RESERVED.1` | `InbaseTaxFormParameter_Reserved1` | TField |  | This field is reserved for future purpose |
| 13 | `INBASE.TAX.LOCAL.REF` | `InbaseTaxFormParameter_LocalRef` |  |  |  |
| 14 | `INBASE.TAX.OVERRIDE` | `InbaseTaxFormParameter_Override` |  |  |  |
| 15 | `INBASE.TAX.RECORD.STATUS` | `InbaseTaxFormParameter_RecordStatus` | String |  |  |
| 16 | `INBASE.TAX.CURR.NO` | `InbaseTaxFormParameter_CurrNo` | String |  |  |
| 17 | `INBASE.TAX.INPUTTER` | `InbaseTaxFormParameter_Inputter` |  |  |  |
| 18 | `INBASE.TAX.DATE.TIME` | `InbaseTaxFormParameter_DateTime` |  |  |  |
| 19 | `INBASE.TAX.AUTHORISER` | `InbaseTaxFormParameter_Authoriser` | String |  |  |
| 20 | `INBASE.TAX.CO.CODE` | `InbaseTaxFormParameter_CoCode` | String |  |  |
| 21 | `INBASE.TAX.DEPT.CODE` | `InbaseTaxFormParameter_DeptCode` | String |  |  |
| 22 | `INBASE.TAX.AUDITOR.CODE` | `InbaseTaxFormParameter_AuditorCode` | String |  |  |
| 23 | `INBASE.TAX.AUDIT.DATE.TIME` | `InbaseTaxFormParameter_AuditDateTime` | String |  |  |
