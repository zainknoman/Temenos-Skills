# HKBASE.GLOBAL.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.HKBASE.GLOBAL.CUSTOMER` in `HKBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HK.GCU.GLOBAL.CBRED` | `HkbaseGlobalCustomer_GlobalCbred` | TField |  | Global Customer Business Relationship End Date (CBRED) pertains to the closure date of the last account of the Customer among all countries and systems. Validation Rule: No Input field, value to be populated by a routine. |
| 2 | `HK.GCU.CUSTOMER.ID` | `HkbaseGlobalCustomer_CustomerId` |  |  |  |
| 3 | `HK.GCU.CUSTOMER.COMPANY` | `HkbaseGlobalCustomer_CustomerCompany` |  |  |  |
| 4 | `HK.GCU.CLOSURE.DATE` | `HkbaseGlobalCustomer_ClosureDate` |  |  |  |
| 5 | `HK.GCU.LOCAL.CBRED` | `HkbaseGlobalCustomer_LocalCbred` |  |  |  |
| 6 | `HK.GCU.EXTERNAL.CUS.ID` | `HkbaseGlobalCustomer_ExternalCusId` |  |  |  |
| 7 | `HK.GCU.EXT.CUSTOMER.BRANCH` | `HkbaseGlobalCustomer_ExtCustomerBranch` |  |  |  |
| 8 | `HK.GCU.EXT.CLOSURE.DATE` | `HkbaseGlobalCustomer_ExtClosureDate` |  |  |  |
| 9 | `HK.GCU.EXT.LOCAL.CBRED` | `HkbaseGlobalCustomer_ExtLocalCbred` |  |  |  |
| 10 | `HK.GCU.LOCAL.REF` | `HkbaseGlobalCustomer_LocalRef` |  |  |  |
| 11 | `HK.GCU.RESERVED.1` | `HkbaseGlobalCustomer_Reserved1` | TField |  | Reserved for future purpose. |
| 12 | `HK.GCU.RESERVED.2` | `HkbaseGlobalCustomer_Reserved2` | TField |  | Reserved for future purpose. |
| 13 | `HK.GCU.RESERVED.3` | `HkbaseGlobalCustomer_Reserved3` | TField |  | Reserved for future purpose. |
| 14 | `HK.GCU.RESERVED.4` | `HkbaseGlobalCustomer_Reserved4` | TField |  | Reserved for future purpose. |
| 15 | `HK.GCU.RESERVED.5` | `HkbaseGlobalCustomer_Reserved5` | TField |  | Reserved for future purpose. |
| 16 | `HK.GCU.RESERVED.6` | `HkbaseGlobalCustomer_Reserved6` | TField |  | Reserved for future purpose. |
| 17 | `HK.GCU.RESERVED.7` | `HkbaseGlobalCustomer_Reserved7` | TField |  | Reserved for future purpose. |
| 18 | `HK.GCU.RESERVED.8` | `HkbaseGlobalCustomer_Reserved8` | TField |  | Reserved for future purpose. |
| 19 | `HK.GCU.RESERVED.9` | `HkbaseGlobalCustomer_Reserved9` | TField |  | Reserved for future purpose. |
| 20 | `HK.GCU.RESERVED.10` | `HkbaseGlobalCustomer_Reserved10` | TField |  | Reserved for future purpose. |
| 21 | `HK.GCU.OVERRIDE` | `HkbaseGlobalCustomer_Override` |  |  |  |
| 22 | `HK.GCU.RECORD.STATUS` | `HkbaseGlobalCustomer_RecordStatus` | String |  |  |
| 23 | `HK.GCU.CURR.NO` | `HkbaseGlobalCustomer_CurrNo` | String |  |  |
| 24 | `HK.GCU.INPUTTER` | `HkbaseGlobalCustomer_Inputter` |  |  |  |
| 25 | `HK.GCU.DATE.TIME` | `HkbaseGlobalCustomer_DateTime` |  |  |  |
| 26 | `HK.GCU.AUTHORISER` | `HkbaseGlobalCustomer_Authoriser` | String |  |  |
| 27 | `HK.GCU.CO.CODE` | `HkbaseGlobalCustomer_CoCode` | String |  |  |
| 28 | `HK.GCU.DEPT.CODE` | `HkbaseGlobalCustomer_DeptCode` | String |  |  |
| 29 | `HK.GCU.AUDITOR.CODE` | `HkbaseGlobalCustomer_AuditorCode` | String |  |  |
| 30 | `HK.GCU.AUDIT.DATE.TIME` | `HkbaseGlobalCustomer_AuditDateTime` | String |  |  |
