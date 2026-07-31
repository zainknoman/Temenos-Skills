# LIMIT.CUSTOMER.CHANGE — Table Schema

> Source: `INSERTS/I_F.LIMIT.CUSTOMER.CHANGE` in `LI_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LCC.DESCRIPTION` | `LimitCustomerChange_Description` |  |  |  |
| 2 | `LCC.CUSTOMER.NUMBER` | `LimitCustomerChange_CustomerNumber` |  |  |  |
| 3 | `LCC.LIABILITY.NUMBER` | `LimitCustomerChange_LiabilityNumber` |  |  |  |
| 4 | `LCC.RESERVED.25` | `LimitCustomerChange_Reserved25` |  |  |  |
| 5 | `LCC.RESERVED.24` | `LimitCustomerChange_Reserved24` |  |  |  |
| 6 | `LCC.RESERVED.23` | `LimitCustomerChange_Reserved23` |  |  |  |
| 7 | `LCC.RESERVED.22` | `LimitCustomerChange_Reserved22` |  |  |  |
| 8 | `LCC.RESERVED.21` | `LimitCustomerChange_Reserved21` |  |  |  |
| 9 | `LCC.SHARING.GROUP.KEY` | `LimitCustomerChange_SharingGroupKey` |  |  |  |
| 10 | `LCC.REMOVE.CUSTOMER` | `LimitCustomerChange_RemoveCustomer` |  |  |  |
| 11 | `LCC.REMOVE.PRODUCT` | `LimitCustomerChange_RemoveProduct` |  |  |  |
| 12 | `LCC.RESERVED.20` | `LimitCustomerChange_Reserved20` |  |  |  |
| 13 | `LCC.RESERVED.19` | `LimitCustomerChange_Reserved19` |  |  |  |
| 14 | `LCC.RESERVED.18` | `LimitCustomerChange_Reserved18` |  |  |  |
| 15 | `LCC.RESERVED.17` | `LimitCustomerChange_Reserved17` |  |  |  |
| 16 | `LCC.RESERVED.16` | `LimitCustomerChange_Reserved16` |  |  |  |
| 17 | `LCC.RESERVED.15` | `LimitCustomerChange_Reserved15` |  |  |  |
| 18 | `LCC.RESERVED.14` | `LimitCustomerChange_Reserved14` |  |  |  |
| 19 | `LCC.RESERVED.13` | `LimitCustomerChange_Reserved13` |  |  |  |
| 20 | `LCC.RESERVED.12` | `LimitCustomerChange_Reserved12` |  |  |  |
| 21 | `LCC.RESERVED.11` | `LimitCustomerChange_Reserved11` |  |  |  |
| 22 | `LCC.RESERVED.10` | `LimitCustomerChange_Reserved10` |  |  |  |
| 23 | `LCC.RESERVED.9` | `LimitCustomerChange_Reserved9` |  |  |  |
| 24 | `LCC.RESERVED.8` | `LimitCustomerChange_Reserved8` |  |  |  |
| 25 | `LCC.RESERVED.7` | `LimitCustomerChange_Reserved7` |  |  |  |
| 26 | `LCC.RESERVED.6` | `LimitCustomerChange_Reserved6` |  |  |  |
| 27 | `LCC.RESERVED.5` | `LimitCustomerChange_Reserved5` |  |  |  |
| 28 | `LCC.RESERVED.4` | `LimitCustomerChange_Reserved4` |  |  |  |
| 29 | `LCC.RESERVED.3` | `LimitCustomerChange_Reserved3` |  |  |  |
| 30 | `LCC.RESERVED.2` | `LimitCustomerChange_Reserved2` |  |  |  |
| 31 | `LCC.RESERVED.1` | `LimitCustomerChange_Reserved1` |  |  |  |
| 32 | `LCC.LOCAL.REF` | `LimitCustomerChange_LocalRef` |  |  |  |
| 33 | `LCC.OVERRIDE` | `LimitCustomerChange_Override` |  |  |  |
| 34 | `LCC.RECORD.STATUS` | `LimitCustomerChange_RecordStatus` | String |  |  |
| 35 | `LCC.CURR.NO` | `LimitCustomerChange_CurrNo` | String |  |  |
| 36 | `LCC.INPUTTER` | `LimitCustomerChange_Inputter` |  |  |  |
| 37 | `LCC.DATE.TIME` | `LimitCustomerChange_DateTime` |  |  |  |
| 38 | `LCC.AUTHORISER` | `LimitCustomerChange_Authoriser` | String |  |  |
| 39 | `LCC.CO.CODE` | `LimitCustomerChange_CoCode` | String |  |  |
| 40 | `LCC.DEPT.CODE` | `LimitCustomerChange_DeptCode` | String |  |  |
| 41 | `LCC.AUDITOR.CODE` | `LimitCustomerChange_AuditorCode` | String |  |  |
| 42 | `LCC.AUDIT.DATE.TIME` | `LimitCustomerChange_AuditDateTime` | String |  |  |
