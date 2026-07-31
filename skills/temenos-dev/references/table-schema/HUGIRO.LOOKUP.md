# HUGIRO.LOOKUP — Table Schema

> Source: `INSERTS/I_F.HUGIRO.LOOKUP` in `HUGIRO_Lookup.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LOOKUP.STATUS` | `HugiroLookup_Status` | TField |  | Shows success/error status of the received message |
| 2 | `LOOKUP.ADDITIONAL.INFORMATION` | `HugiroLookup_AdditionalInformation` | TField |  | Error information. |
| 3 | `LOOKUP.PROXY.TYPE` | `HugiroLookup_ProxyType` | TField |  | Type of Proxy Identifier. |
| 4 | `LOOKUP.PROXY.IDENTIFIER` | `HugiroLookup_ProxyIdentifier` | TField |  | Alias identifier. |
| 5 | `LOOKUP.IBAN` | `HugiroLookup_Iban` | TField |  | Alias linked IBAN number. |
| 6 | `LOOKUP.BIC` | `HugiroLookup_Bic` | TField |  | Alias linked BIC code |
| 7 | `LOOKUP.CUSTOMER.NAME` | `HugiroLookup_CustomerName` | TField |  | Alias linked Customer Name |
| 8 | `LOOKUP.CUSTOMER.SURNAME` | `HugiroLookup_CustomerSurname` | TField |  | Alias linked Customer Surname. |
| 9 | `LOOKUP.CUSTOMER.CATEGORY` | `HugiroLookup_CustomerCategory` | TField |  | Code to indicate whether the customer is a private person (P) or corporate (C). |
| 10 | `LOOKUP.CREATION.DATE.TIME` | `HugiroLookup_CreationDateTime` |  |  |  |
| 11 | `LOOKUP.REGISTRATION.DATE.TIME` | `HugiroLookup_RegistrationDateTime` |  |  |  |
| 12 | `LOOKUP.BUSINESS.ID` | `HugiroLookup_BusinessId` | TField |  | Business ID of Registration / Deletion request received from channel.. |
| 13 | `LOOKUP.SOURCE` | `HugiroLookup_Source` | TField |  | Source system where the request is generated. |
| 14 | `LOOKUP.PROCESS.ID` | `HugiroLookup_ProcessId` | TField |  | Process ID of Registration / Deletion request. |
| 15 | `LOOKUP.CUSTOMER.ID` | `HugiroLookup_CustomerId` | TField |  | Customer Identifier |
| 16 | `LOOKUP.SERVER.NODE` | `HugiroLookup_ServerNode` | TField |  | IP of request sending server. |
| 17 | `LOOKUP.LOCAL.REF` | `HugiroLookup_LocalRef` |  |  |  |
| 18 | `LOOKUP.RESERVED.5` | `HugiroLookup_Reserved5` | TField |  |  |
| 19 | `LOOKUP.RESERVED.4` | `HugiroLookup_Reserved4` | TField |  |  |
| 20 | `LOOKUP.RESERVED.3` | `HugiroLookup_Reserved3` | TField |  |  |
| 21 | `LOOKUP.RESERVED.2` | `HugiroLookup_Reserved2` | TField |  |  |
| 22 | `LOOKUP.RESERVED.1` | `HugiroLookup_Reserved1` | TField |  |  |
| 23 | `LOOKUP.OVERRIDE` | `HugiroLookup_Override` |  |  |  |
| 24 | `LOOKUP.RECORD.STATUS` | `HugiroLookup_RecordStatus` | String |  |  |
| 25 | `LOOKUP.CURR.NO` | `HugiroLookup_CurrNo` | String |  |  |
| 26 | `LOOKUP.INPUTTER` | `HugiroLookup_Inputter` |  |  |  |
| 27 | `LOOKUP.DATE.TIME` | `HugiroLookup_DateTime` |  |  |  |
| 28 | `LOOKUP.AUTHORISER` | `HugiroLookup_Authoriser` | String |  |  |
| 29 | `LOOKUP.CO.CODE` | `HugiroLookup_CoCode` | String |  |  |
| 30 | `LOOKUP.DEPT.CODE` | `HugiroLookup_DeptCode` | String |  |  |
| 31 | `LOOKUP.AUDITOR.CODE` | `HugiroLookup_AuditorCode` | String |  |  |
| 32 | `LOOKUP.AUDIT.DATE.TIME` | `HugiroLookup_AuditDateTime` | String |  |  |
