# DE.DELIVERY.REQUEST.LISTENER — Table Schema

> Source: `INSERTS/I_F.DE.DELIVERY.REQUEST.LISTENER` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.DERL.COMPANY.CODE` | `DeDeliveryRequestListener_CompanyCode` | TField |  | The Company code under which the message is processed. |
| 2 | `DE.DERL.SOURCE.UNIQUE.ID` | `DeDeliveryRequestListener_SourceUniqueId` | TField |  | This represents the unique message id allocated by the source. Mapped from CARRIER SEQ NO field of DE.O.HEADER. |
| 3 | `DE.DERL.SOURCE.COMPANY` | `DeDeliveryRequestListener_SourceCompany` | TField |  | This represents the source company if supplied in the incoming message. If Delivery MX Translation is on a different platform this could be different from the processing company. |
| 4 | `DE.DERL.SOURCE.CARRIER` | `DeDeliveryRequestListener_SourceCarrier` | TField |  | The carrier associated to the incoming message by the source system, if any. |
| 5 | `DE.DERL.SOURCE.APPLICATION` | `DeDeliveryRequestListener_SourceApplication` | TField |  | The Business module which produced the incoming message in the source system, if any. |
| 6 | `DE.DERL.SOURCE.MESSAGE.TYPE` | `DeDeliveryRequestListener_SourceMessageType` | TField |  | The type of the message associated with the incoming message. |
| 7 | `DE.DERL.SOURCE.TIMESTAMP` | `DeDeliveryRequestListener_SourceTimestamp` | TField |  | TimeStamp when message has been emitted from the source. |
| 8 | `DE.DERL.SOURCE.TRANS.REF` | `DeDeliveryRequestListener_SourceTransRef` | TField |  | The transaction reference associated by the source system/application. |
| 9 | `DE.DERL.SOURCE.COMMON.REF` | `DeDeliveryRequestListener_SourceCommonRef` | TField |  | The common reference allocated by the source. |
| 10 | `DE.DERL.SOURCE.PRIORITY` | `DeDeliveryRequestListener_SourcePriority` | TField |  | Priority defined in the source message. |
| 11 | `DE.DERL.CUSTOMER.NO` | `DeDeliveryRequestListener_CustomerNo` | TField |  | Customer number passed in the request message. |
| 12 | `DE.DERL.FROM.ADDRESS` | `DeDeliveryRequestListener_FromAddress` | TField |  | The From Address indicated by the source system/ extracted from the message. |
| 13 | `DE.DERL.TO.ADDRESS` | `DeDeliveryRequestListener_ToAddress` | TField |  | The To Address indicated by the source system/ extracted from the message. |
| 14 | `DE.DERL.TARGET.CARRIER` | `DeDeliveryRequestListener_TargetCarrier` | TField |  | The Target Carrier determined by the MX Translation Layer for the request. |
| 15 | `DE.DERL.TARGET.MESSAGE.TYPE` | `DeDeliveryRequestListener_TargetMessageType` | TField |  | If not supplied, for XMLISO carriers this is identified based on the message variant set in the Delivery Carrier. |
| 16 | `DE.DERL.ORIGINAL.PAYLOAD` | `DeDeliveryRequestListener_OriginalPayload` | TField |  | Original PayLoad from request message. |
| 17 | `DE.DERL.PAYLOAD` | `DeDeliveryRequestListener_Payload` | TField |  | The payLoad that will be routed to the Delivery Transformation Layer - should be encoded in base64. |
| 18 | `DE.DERL.PAYLOAD.FORMAT` | `DeDeliveryRequestListener_PayloadFormat` | TField |  | The format indicated of the original request. |
| 19 | `DE.DERL.ACCOUNT.NUMBER` | `DeDeliveryRequestListener_AccountNumber` | TField |  | Account for the message. |
| 20 | `DE.DERL.MESSAGE.CURRENCY` | `DeDeliveryRequestListener_MessageCurrency` | TField |  | Currency picked from the request message. |
| 21 | `DE.DERL.MESSAGE.AMOUNT` | `DeDeliveryRequestListener_MessageAmount` | TField |  | Amount picked from the request message. |
| 22 | `DE.DERL.MESSAGE.VALUE.DATE` | `DeDeliveryRequestListener_MessageValueDate` | TField |  | The value date, if indicated in the request. |
| 23 | `DE.DERL.PROCESSING.DATE` | `DeDeliveryRequestListener_ProcessingDate` | TField |  | This will be automatically set with the date when the message has been processed. |
| 24 | `DE.DERL.DELIVERY.OUT.HEADER.ID` | `DeDeliveryRequestListener_DeliveryOutHeaderId` | TField |  |  |
| 25 | `DE.DERL.STATUS` | `DeDeliveryRequestListener_Status` | TField |  | Indicates the processing status of the request Options: Blank - new request that must be routed ROUTED - indicates the message has been routed to Delivery Transformation Layer REPAIR - indicates the message has not been routed to Delivery Transformation Layer ,e .g the Target Delivery Carrier is not an XMLISO. AWAITING.ENRICHMENT - indicates that the received page should be further processed to determine Transaction Summary and fetch additional enrichment in case of Payment transaction. The status 'AWAITING ENRICHMENT' is applicable only for the message types MT940/950/941/942. |
| 26 | `DE.DERL.CREATE.DATE.TIME` | `DeDeliveryRequestListener_DeDerlCreateDateTime` |  |  |  |
| 27 | `DE.DERL.ACCOUNT.CURRENCY` | `DeDeliveryRequestListener_AccountCurrency` | TField |  | Currency for the Account . |
| 28 | `DE.DERL.STATEMENT.ID` | `DeDeliveryRequestListener_StatementId` | TField |  | Unique value of a statement. In case of Paginated statement, this value will be common for all the pages of the statement. This field will be updated during authorization of Delivery listener record for the message types MT940/950/941/942. Format - DE.O.HEADER Id of MT message without sequence number |
| 29 | `DE.DERL.PAGE.NUMBER` | `DeDeliveryRequestListener_PageNumber` | TField |  |  |
| 30 | `DE.DERL.LAST.PAGE.INDICATOR` | `DeDeliveryRequestListener_LastPageIndicator` | TField |  | Options field to indicate that the last page has been received. This field will be set to "YES" to indicate that the current page is the last page of the MT message. |
| 31 | `DE.DERL.RESERVED.15` | `DeDeliveryRequestListener_Reserved15` | TField |  |  |
| 32 | `DE.DERL.RESERVED.14` | `DeDeliveryRequestListener_Reserved14` | TField |  |  |
| 33 | `DE.DERL.RESERVED.13` | `DeDeliveryRequestListener_Reserved13` | TField |  |  |
| 34 | `DE.DERL.RESERVED.12` | `DeDeliveryRequestListener_Reserved12` | TField |  |  |
| 35 | `DE.DERL.RESERVED.11` | `DeDeliveryRequestListener_Reserved11` | TField |  |  |
| 36 | `DE.DERL.RESERVED.10` | `DeDeliveryRequestListener_Reserved10` | TField |  |  |
| 37 | `DE.DERL.RESERVED.9` | `DeDeliveryRequestListener_Reserved9` | TField |  |  |
| 38 | `DE.DERL.RESERVED.8` | `DeDeliveryRequestListener_Reserved8` | TField |  |  |
| 39 | `DE.DERL.RESERVED.7` | `DeDeliveryRequestListener_Reserved7` | TField |  |  |
| 40 | `DE.DERL.RESERVED.6` | `DeDeliveryRequestListener_Reserved6` | TField |  |  |
| 41 | `DE.DERL.RESERVED.5` | `DeDeliveryRequestListener_Reserved5` | TField |  |  |
| 42 | `DE.DERL.RESERVED.4` | `DeDeliveryRequestListener_Reserved4` | TField |  |  |
| 43 | `DE.DERL.RESERVED.3` | `DeDeliveryRequestListener_Reserved3` | TField |  |  |
| 44 | `DE.DERL.RESERVED.2` | `DeDeliveryRequestListener_Reserved2` | TField |  |  |
| 45 | `DE.DERL.RESERVED.1` | `DeDeliveryRequestListener_Reserved1` | TField |  |  |
| 46 | `DE.DERL.LOCAL.REF` | `DeDeliveryRequestListener_LocalRef` |  |  |  |
| 47 | `DE.DERL.OVERRIDE` | `DeDeliveryRequestListener_Override` |  |  |  |
| 48 | `DE.DERL.RECORD.STATUS` | `DeDeliveryRequestListener_RecordStatus` | String |  |  |
| 49 | `DE.DERL.CURR.NO` | `DeDeliveryRequestListener_CurrNo` | String |  |  |
| 50 | `DE.DERL.INPUTTER` | `DeDeliveryRequestListener_Inputter` |  |  |  |
| 51 | `DE.DERL.DATE.TIME` | `DeDeliveryRequestListener_DateTime` |  |  |  |
| 52 | `DE.DERL.AUTHORISER` | `DeDeliveryRequestListener_Authoriser` | String |  |  |
| 53 | `DE.DERL.CO.CODE` | `DeDeliveryRequestListener_CoCode` | String |  |  |
| 54 | `DE.DERL.DEPT.CODE` | `DeDeliveryRequestListener_DeptCode` | String |  |  |
| 55 | `DE.DERL.AUDITOR.CODE` | `DeDeliveryRequestListener_AuditorCode` | String |  |  |
| 56 | `DE.DERL.AUDIT.DATE.TIME` | `DeDeliveryRequestListener_AuditDateTime` | String |  |  |
