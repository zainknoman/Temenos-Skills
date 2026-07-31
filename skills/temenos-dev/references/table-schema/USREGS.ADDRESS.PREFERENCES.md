# USREGS.ADDRESS.PREFERENCES — Table Schema

> Source: `INSERTS/I_F.USREGS.ADDRESS.PREFERENCES` in `USREGS_AddressChange.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ADDCHN.CARRIER.ADDR.NO` | `UsregsAddressPreferences_CarrierAddrNo` |  |  |  |
| 2 | `ADDCHN.START.PERIOD` | `UsregsAddressPreferences_StartPeriod` |  |  |  |
| 3 | `ADDCHN.END.PERIOD` | `UsregsAddressPreferences_EndPeriod` |  |  |  |
| 4 | `ADDCHN.RESERVED.1` | `UsregsAddressPreferences_Reserved1` |  |  |  |
| 5 | `ADDCHN.RESERVED.2` | `UsregsAddressPreferences_Reserved2` |  |  |  |
| 6 | `ADDCHN.RESERVED.3` | `UsregsAddressPreferences_Reserved3` |  |  |  |
| 7 | `ADDCHN.REVIEW.DATE` | `UsregsAddressPreferences_ReviewDate` | TField |  | This field is used to indicate the end of current address period. Validation Rules: Calculated by the System. No Input field. |
| 8 | `ADDCHN.DELIVERY.REF` | `UsregsAddressPreferences_DeliveryRef` |  |  |  |
| 9 | `ADDCHN.DEFAULT.CARRIER.NO` | `UsregsAddressPreferences_DefaultCarrierNo` | TField |  | This field is inputted when the customer requires to send the communication letter to the different address from PRINT.1 (default to PRINT.1 in DE.PRODUCT) when the seasonal address for that period is not defined in the table USREGS.ADDRESS.PREFERENCES Validation Rules: Should be a valid PRINT carrier from DE.ADDRESS table. |
| 10 | `ADDCHN.RESERVED.5` | `UsregsAddressPreferences_Reserved5` | TField |  |  |
| 11 | `ADDCHN.RESERVED.6` | `UsregsAddressPreferences_Reserved6` | TField |  |  |
| 12 | `ADDCHN.RESERVED.7` | `UsregsAddressPreferences_Reserved7` | TField |  |  |
| 13 | `ADDCHN.RESERVED.8` | `UsregsAddressPreferences_Reserved8` | TField |  |  |
| 14 | `ADDCHN.RESERVED.9` | `UsregsAddressPreferences_Reserved9` | TField |  |  |
| 15 | `ADDCHN.RESERVED.10` | `UsregsAddressPreferences_Reserved10` | TField |  |  |
| 16 | `ADDCHN.RESERVED.11` | `UsregsAddressPreferences_Reserved11` | TField |  |  |
| 17 | `ADDCHN.RESERVED.12` | `UsregsAddressPreferences_Reserved12` | TField |  |  |
| 18 | `ADDCHN.RESERVED.13` | `UsregsAddressPreferences_Reserved13` | TField |  |  |
| 19 | `ADDCHN.RESERVED.14` | `UsregsAddressPreferences_Reserved14` | TField |  |  |
| 20 | `ADDCHN.OVERRIDE` | `UsregsAddressPreferences_Override` |  |  |  |
| 21 | `ADDCHN.RECORD.STATUS` | `UsregsAddressPreferences_RecordStatus` | String |  |  |
| 22 | `ADDCHN.CURR.NO` | `UsregsAddressPreferences_CurrNo` | String |  |  |
| 23 | `ADDCHN.INPUTTER` | `UsregsAddressPreferences_Inputter` |  |  |  |
| 24 | `ADDCHN.DATE.TIME` | `UsregsAddressPreferences_DateTime` |  |  |  |
| 25 | `ADDCHN.AUTHORISER` | `UsregsAddressPreferences_Authoriser` | String |  |  |
| 26 | `ADDCHN.CO.CODE` | `UsregsAddressPreferences_CoCode` | String |  |  |
| 27 | `ADDCHN.DEPT.CODE` | `UsregsAddressPreferences_DeptCode` | String |  |  |
| 28 | `ADDCHN.AUDITOR.CODE` | `UsregsAddressPreferences_AuditorCode` | String |  |  |
| 29 | `ADDCHN.AUDIT.DATE.TIME` | `UsregsAddressPreferences_AuditDateTime` | String |  |  |
