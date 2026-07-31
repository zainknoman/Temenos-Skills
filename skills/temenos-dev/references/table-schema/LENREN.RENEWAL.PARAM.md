# LENREN.RENEWAL.PARAM — Table Schema

> Source: `INSERTS/I_F.LENREN.RENEWAL.PARAM` in `LENREN_Renewal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REN.PARAM.RENEWAL.REJECTS` | `LenrenRenewalParam_RenewalRejects` |  |  |  |
| 2 | `REN.PARAM.PROVINCE.TAX` | `LenrenRenewalParam_ProvinceTax` | TField |  | This field is used to define the province tax applicable for the loan renewal or not.The value defined in this field will be applicable for province tax calculation during the loan renewal.Valid tax percentage to be defined here. Modified |
| 3 | `REN.PARAM.FEDERAL.TAX` | `LenrenRenewalParam_FederalTax` | TField |  | This field is used to define the federal tax applicable for the loan renewal or not.The value defined in this field will be applicable for federal tax calculation during the loan renewal.Valid tax percentage to be defined here. |
| 4 | `REN.PARAM.QUOTATION.CONDITION` | `LenrenRenewalParam_QuotationCondition` | TField |  | The purpose of this field is used to define the quotation condition for loan renewal.Valid record AA.DEFINITION.MANAGER |
| 5 | `REN.PARAM.QUOTATION.VERSION` | `LenrenRenewalParam_QuotationVersion` | TField |  |  |
| 6 | `REN.PARAM.RESERVED.10` | `LenrenRenewalParam_Reserved10` | TField |  |  |
| 7 | `REN.PARAM.RESERVED.9` | `LenrenRenewalParam_Reserved9` | TField |  |  |
| 8 | `REN.PARAM.RESERVED.8` | `LenrenRenewalParam_Reserved8` | TField |  |  |
| 9 | `REN.PARAM.RESERVED.7` | `LenrenRenewalParam_Reserved7` | TField |  |  |
| 10 | `REN.PARAM.RESERVED.6` | `LenrenRenewalParam_Reserved6` | TField |  |  |
| 11 | `REN.PARAM.RESERVED.5` | `LenrenRenewalParam_Reserved5` | TField |  |  |
| 12 | `REN.PARAM.RESERVED.4` | `LenrenRenewalParam_Reserved4` | TField |  |  |
| 13 | `REN.PARAM.RESERVED.3` | `LenrenRenewalParam_Reserved3` | TField |  |  |
| 14 | `REN.PARAM.RESERVED.2` | `LenrenRenewalParam_Reserved2` | TField |  |  |
| 15 | `REN.PARAM.RESERVED.1` | `LenrenRenewalParam_Reserved1` | TField |  |  |
| 16 | `REN.PARAM.LOCAL.REF` | `LenrenRenewalParam_LocalRef` |  |  |  |
| 17 | `REN.PARAM.OVERRIDE` | `LenrenRenewalParam_Override` |  |  |  |
| 18 | `REN.PARAM.RECORD.STATUS` | `LenrenRenewalParam_RecordStatus` | String |  |  |
| 19 | `REN.PARAM.CURR.NO` | `LenrenRenewalParam_CurrNo` | String |  |  |
| 20 | `REN.PARAM.INPUTTER` | `LenrenRenewalParam_Inputter` |  |  |  |
| 21 | `REN.PARAM.DATE.TIME` | `LenrenRenewalParam_DateTime` |  |  |  |
| 22 | `REN.PARAM.AUTHORISER` | `LenrenRenewalParam_Authoriser` | String |  |  |
| 23 | `REN.PARAM.CO.CODE` | `LenrenRenewalParam_CoCode` | String |  |  |
| 24 | `REN.PARAM.DEPT.CODE` | `LenrenRenewalParam_DeptCode` | String |  |  |
| 25 | `REN.PARAM.AUDITOR.CODE` | `LenrenRenewalParam_AuditorCode` | String |  |  |
| 26 | `REN.PARAM.AUDIT.DATE.TIME` | `LenrenRenewalParam_AuditDateTime` | String |  |  |
