# HKBASE.CUSTOMER.RELATED.GC — Table Schema

> Source: `INSERTS/I_F.HKBASE.CUSTOMER.RELATED.GC` in `HKBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HK.CRGC.GLOBAL.CUSTOMER` | `HkbaseCustomerRelatedGc_GlobalCustomer` | TField |  | Indicates the global customer of the Customer. Validation Rule: Vetted against a HKBASE.GLOBAL.CUSTOMER record in T24 |
| 2 | `HK.CRGC.INTERNAL.ACCOUNTS` | `HkbaseCustomerRelatedGc_InternalAccounts` | TField |  | This field indicates current number of active accounts in T24 for the @ID Customer. |
| 3 | `HK.CRGC.EXTERNAL.ACCOUNTS` | `HkbaseCustomerRelatedGc_ExternalAccounts` | TField |  | This field indicates current number of active external accounts outside T24 for the @ID Customer. |
| 4 | `HK.CRGC.LOCAL.REF` | `HkbaseCustomerRelatedGc_LocalRef` |  |  |  |
| 5 | `HK.CRGC.RESERVED.1` | `HkbaseCustomerRelatedGc_Reserved1` | TField |  | Reserved for future purpose. |
| 6 | `HK.CRGC.RESERVED.2` | `HkbaseCustomerRelatedGc_Reserved2` | TField |  | Reserved for future purpose. |
| 7 | `HK.CRGC.RESERVED.3` | `HkbaseCustomerRelatedGc_Reserved3` | TField |  | Reserved for future purpose. |
| 8 | `HK.CRGC.RESERVED.4` | `HkbaseCustomerRelatedGc_Reserved4` | TField |  | Reserved for future purpose. |
| 9 | `HK.CRGC.RESERVED.5` | `HkbaseCustomerRelatedGc_Reserved5` | TField |  | Reserved for future purpose. |
| 10 | `HK.CRGC.RESERVED.6` | `HkbaseCustomerRelatedGc_Reserved6` | TField |  | Reserved for future purpose. |
| 11 | `HK.CRGC.RESERVED.7` | `HkbaseCustomerRelatedGc_Reserved7` | TField |  | Reserved for future purpose. |
| 12 | `HK.CRGC.RESERVED.8` | `HkbaseCustomerRelatedGc_Reserved8` | TField |  | Reserved for future purpose. |
| 13 | `HK.CRGC.RESERVED.9` | `HkbaseCustomerRelatedGc_Reserved9` | TField |  | Reserved for future purpose. |
| 14 | `HK.CRGC.RESERVED.10` | `HkbaseCustomerRelatedGc_Reserved10` | TField |  | Reserved for future purpose. |
