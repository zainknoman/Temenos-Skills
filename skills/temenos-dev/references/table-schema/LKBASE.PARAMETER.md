# LKBASE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LKBASE.PARAMETER` in `LKBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LKBASE.PARAMETER.CUSTOMER.STATUS` | `LkbaseParameter_CustomerStatus` |  |  |  |
| 2 | `LKBASE.PARAMETER.AGE` | `LkbaseParameter_Age` |  |  |  |
| 3 | `LKBASE.PARAMETER.CORPORATE.CUSTOMER.STATUS` | `LkbaseParameter_CorporateCustomerStatus` | TField |  | Defines the customer status for the corporate customer. |
| 4 | `LKBASE.PARAMETER.FUTURE.DATED.COMMISSION` | `LkbaseParameter_FutureDatedCommission` |  |  |  |
| 5 | `LKBASE.PARAMETER.FUTURE.DATED.TAX` | `LkbaseParameter_FutureDatedTax` |  |  |  |
| 6 | `LKBASE.PARAMETER.RESERVED.4` | `LkbaseParameter_Reserved4` | TField |  |  |
| 7 | `LKBASE.PARAMETER.RESERVED.5` | `LkbaseParameter_Reserved5` | TField |  |  |
| 8 | `LKBASE.PARAMETER.RESERVED.6` | `LkbaseParameter_Reserved6` | TField |  |  |
| 9 | `LKBASE.PARAMETER.RESERVED.7` | `LkbaseParameter_Reserved7` | TField |  |  |
| 10 | `LKBASE.PARAMETER.RESERVED.8` | `LkbaseParameter_Reserved8` | TField |  |  |
| 11 | `LKBASE.PARAMETER.RESERVED.9` | `LkbaseParameter_Reserved9` | TField |  |  |
| 12 | `LKBASE.PARAMETER.RESERVED.10` | `LkbaseParameter_Reserved10` | TField |  |  |
| 13 | `LKBASE.PARAMETER.LOCAL.REF` | `LkbaseParameter_LocalRef` |  |  |  |
| 14 | `LKBASE.PARAMETER.OVERRIDE` | `LkbaseParameter_Override` |  |  |  |
| 15 | `LKBASE.PARAMETER.RECORD.STATUS` | `LkbaseParameter_RecordStatus` | String |  |  |
| 16 | `LKBASE.PARAMETER.CURR.NO` | `LkbaseParameter_CurrNo` | String |  |  |
| 17 | `LKBASE.PARAMETER.INPUTTER` | `LkbaseParameter_Inputter` |  |  |  |
| 18 | `LKBASE.PARAMETER.DATE.TIME` | `LkbaseParameter_DateTime` |  |  |  |
| 19 | `LKBASE.PARAMETER.AUTHORISER` | `LkbaseParameter_Authoriser` | String |  |  |
| 20 | `LKBASE.PARAMETER.CO.CODE` | `LkbaseParameter_CoCode` | String |  |  |
| 21 | `LKBASE.PARAMETER.DEPT.CODE` | `LkbaseParameter_DeptCode` | String |  |  |
| 22 | `LKBASE.PARAMETER.AUDITOR.CODE` | `LkbaseParameter_AuditorCode` | String |  |  |
| 23 | `LKBASE.PARAMETER.AUDIT.DATE.TIME` | `LkbaseParameter_AuditDateTime` | String |  |  |
