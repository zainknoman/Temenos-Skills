# INBASE.CUSTOMER.INDUSTRY — Table Schema

> Source: `INSERTS/I_F.INBASE.CUSTOMER.INDUSTRY` in `INBASE_CustomerValidations.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INBASE.INDUSTRY.CODE` | `InbaseCustomerIndustry_IndustryCode` | TField |  | Valid @id of ESBASE.INDUSTRY.CODES, Drop down field |
| 2 | `INBASE.MAIN.CODE` | `InbaseCustomerIndustry_MainCode` | TField |  | Drop-down field, should display all MAIN.CODE records for selected INDUSTRY.CODE |
| 3 | `INBASE.SUB.CODE` | `InbaseCustomerIndustry_SubCode` | TField |  | Drop-down field, should display all SUB.CODE records of MAIN.CODE as selected above |
| 4 | `INBASE.INDUSTRY.CODE.LEVELS` | `InbaseCustomerIndustry_IndustryCodeLevels` | TField |  | Invisible field |
| 5 | `INBASE.RESERVED.10` | `InbaseCustomerIndustry_Reserved10` | TField |  | Reserved for future purpose |
| 6 | `INBASE.RESERVED.9` | `InbaseCustomerIndustry_Reserved9` | TField |  | Reserved for future purpose |
| 7 | `INBASE.RESERVED.8` | `InbaseCustomerIndustry_Reserved8` | TField |  | Reserved for future purpose |
| 8 | `INBASE.RESERVED.7` | `InbaseCustomerIndustry_Reserved7` | TField |  | Reserved for future purpose |
| 9 | `INBASE.RESERVED.6` | `InbaseCustomerIndustry_Reserved6` | TField |  | Reserved for future purpose |
| 10 | `INBASE.RESERVED.5` | `InbaseCustomerIndustry_Reserved5` | TField |  | Reserved for future purpose |
| 11 | `INBASE.RESERVED.4` | `InbaseCustomerIndustry_Reserved4` | TField |  | Reserved for future purpose |
| 12 | `INBASE.RESERVED.3` | `InbaseCustomerIndustry_Reserved3` | TField |  | Reserved for future purpose |
| 13 | `INBASE.RESERVED.2` | `InbaseCustomerIndustry_Reserved2` | TField |  | Reserved for future purpose |
| 14 | `INBASE.RESERVED.1` | `InbaseCustomerIndustry_Reserved1` | TField |  | Reserved for future purpose |
| 15 | `INBASE.LOCAL.REF` | `InbaseCustomerIndustry_LocalRef` |  |  |  |
| 16 | `INBASE.OVERRIDE` | `InbaseCustomerIndustry_Override` |  |  |  |
| 17 | `INBASE.RECORD.STATUS` | `InbaseCustomerIndustry_RecordStatus` | String |  |  |
| 18 | `INBASE.CURR.NO` | `InbaseCustomerIndustry_CurrNo` | String |  |  |
| 19 | `INBASE.INPUTTER` | `InbaseCustomerIndustry_Inputter` |  |  |  |
| 20 | `INBASE.DATE.TIME` | `InbaseCustomerIndustry_DateTime` |  |  |  |
| 21 | `INBASE.AUTHORISER` | `InbaseCustomerIndustry_Authoriser` | String |  |  |
| 22 | `INBASE.CO.CODE` | `InbaseCustomerIndustry_CoCode` | String |  |  |
| 23 | `INBASE.DEPT.CODE` | `InbaseCustomerIndustry_DeptCode` | String |  |  |
| 24 | `INBASE.AUDITOR.CODE` | `InbaseCustomerIndustry_AuditorCode` | String |  |  |
| 25 | `INBASE.AUDIT.DATE.TIME` | `InbaseCustomerIndustry_AuditDateTime` | String |  |  |
