# ST.PROXY.DIRECTORY — Table Schema

> Source: `INSERTS/I_F.ST.PROXY.DIRECTORY` in `ST_AliasManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.PRD.REGISTERED.ACCT.NO` | `StProxyDirectory_RegisteredAcctNo` | TField | Yes | To capture an account number or alternate account number for which proxy is created. Mandatory input. |
| 2 | `ST.PRD.ACCOUNT.NO` | `StProxyDirectory_AccountNo` | TField | Yes | A valid account in T24 derived based on the registered account number provided. Mandatory input. |
| 3 | `ST.PRD.PROXY.TYPE` | `StProxyDirectory_ProxyType` | TField | Yes | Type of proxy created for account. Currently supported types are mobile number, email ID and tax id. Mandatory input. |
| 4 | `ST.PRD.PROXY.IDENTIFIER` | `StProxyDirectory_ProxyIdentifier` | TField | Yes | A proxy identifier to be linked to an account based on the proxy type provided eg. Mobile number, email id and tax id. Mandatory input. |
| 5 | `ST.PRD.EXPOSED.PROXY` | `StProxyDirectory_ExposedProxy` | TField |  | Concatenation of proxy type and proxy link ID to ensure the uniqueness of the proxy links created. Will be populated if the current status of the proxy record is same as that of the status defined in the EXPOSED.PROXY.STATUS field in proxy parameter table Will be cleared off when the status is not same as EXPOSED.PROXY.STATUS anymore. |
| 6 | `ST.PRD.REGISTERED.CUSTOMER.ID` | `StProxyDirectory_RegisteredCustomerId` | TField |  | Customer to whom the registered account belongs to. Must be a valid record in customer table. |
| 7 | `ST.PRD.CUSTOMER.TYPE` | `StProxyDirectory_CustomerType` | TField |  | Type of customer - Private individual, corporate etc. |
| 8 | `ST.PRD.CUSTOMER.NAME` | `StProxyDirectory_CustomerName` | TField | Yes | Name of the customer. Mandatory input. |
| 9 | `ST.PRD.CUSTOMER.SURNAME` | `StProxyDirectory_CustomerSurname` | TField |  | Surname of the customer. |
| 10 | `ST.PRD.STATUS` | `StProxyDirectory_Status` | TField | Yes | Current status of the proxy directory. Mandatory input. |
| 11 | `ST.PRD.PRIOR.STATUS` | `StProxyDirectory_PriorStatus` |  |  |  |
| 12 | `ST.PRD.NOTES` | `StProxyDirectory_Notes` | TField |  | Field to capture notes. |
| 13 | `ST.PRD.INDICATOR` | `StProxyDirectory_Indicator` | TField |  | Indicator which points to the next status. If value defined here is available in proxy status table then the next status available in the proxy status table will be populated in the status field. |
| 14 | `ST.PRD.ACTIVATION.DATE` | `StProxyDirectory_ActivationDate` | TField |  | Indicates when the status is changed to active. |
| 15 | `ST.PRD.EXT.ACTIVATION.TIMESTAMP` | `StProxyDirectory_ExtActivationTimestamp` | TField |  | contains the date and time stamp populated by the external system. |
| 16 | `ST.PRD.CONFIRMATION.DATE` | `StProxyDirectory_ConfirmationDate` | TField |  | Contains the date when the proxy&apos;s validity has been confirmed. First confirmation date will be the activation date and later will be updated with the latest re-confirmed date. |
| 17 | `ST.PRD.NEXT.CONFIRMATION.DATE` | `StProxyDirectory_NextConfirmationDate` | TField |  | Contains the next date when the proxy has to be reconfirmed. Those proxies that are not reconfirmed within the date defined here will be marked as expired and moved to history. |
| 18 | `ST.PRD.PRE.NOTICE.CONFIRM.DATE` | `StProxyDirectory_PreNoticeConfirmDate` | TField |  | Contains the date when the notification regarding the proxy reconfirmation has to be sent out. |
| 19 | `ST.PRD.REQUEST.SOURCE` | `StProxyDirectory_RequestSource` | TField |  | Captures the source of the request eg. Channel, officer etc. |
| 20 | `ST.PRD.FORCED.REQUEST` | `StProxyDirectory_ForcedRequest` | TField |  | To indicate that the proxy has been created by force though the presence of another proxy with same details exist. |
| 21 | `ST.PRD.CONFLICTING.LINK` | `StProxyDirectory_ConflictingLink` | TField |  | Captures details of another existing Proxy Link which prevented current Proxy Link from registration. |
| 22 | `ST.PRD.SCHEME` | `StProxyDirectory_Scheme` | TField |  | Scheme field values are created in the EB.LOOKUP application for example USPAY,UKPAY |
| 23 | `ST.PRD.ROLE` | `StProxyDirectory_Role` | TField |  | Role field values are created in the EB.LOOKUP application for example PAYER , REQUESTOR , BOTH |
| 24 | `ST.PRD.RESERVED08` | `StProxyDirectory_Reserved08` | TField |  |  |
| 25 | `ST.PRD.RESERVED07` | `StProxyDirectory_Reserved07` | TField |  |  |
| 26 | `ST.PRD.RESERVED06` | `StProxyDirectory_Reserved06` | TField |  |  |
| 27 | `ST.PRD.RESERVED05` | `StProxyDirectory_Reserved05` | TField |  |  |
| 28 | `ST.PRD.RESERVED04` | `StProxyDirectory_Reserved04` | TField |  |  |
| 29 | `ST.PRD.RESERVED03` | `StProxyDirectory_Reserved03` | TField |  |  |
| 30 | `ST.PRD.RESERVED02` | `StProxyDirectory_Reserved02` | TField |  |  |
| 31 | `ST.PRD.RESERVED01` | `StProxyDirectory_Reserved01` | TField |  |  |
| 32 | `ST.PRD.LOCAL.REF` | `StProxyDirectory_LocalRef` |  |  |  |
| 33 | `ST.PRD.OVERRIDE` | `StProxyDirectory_Override` |  |  |  |
| 34 | `ST.PRD.RECORD.STATUS` | `StProxyDirectory_RecordStatus` | String |  |  |
| 35 | `ST.PRD.CURR.NO` | `StProxyDirectory_CurrNo` | String |  |  |
| 36 | `ST.PRD.INPUTTER` | `StProxyDirectory_Inputter` |  |  |  |
| 37 | `ST.PRD.DATE.TIME` | `StProxyDirectory_DateTime` |  |  |  |
| 38 | `ST.PRD.AUTHORISER` | `StProxyDirectory_Authoriser` | String |  |  |
| 39 | `ST.PRD.CO.CODE` | `StProxyDirectory_CoCode` | String |  |  |
| 40 | `ST.PRD.DEPT.CODE` | `StProxyDirectory_DeptCode` | String |  |  |
| 41 | `ST.PRD.AUDITOR.CODE` | `StProxyDirectory_AuditorCode` | String |  |  |
| 42 | `ST.PRD.AUDIT.DATE.TIME` | `StProxyDirectory_AuditDateTime` | String |  |  |
