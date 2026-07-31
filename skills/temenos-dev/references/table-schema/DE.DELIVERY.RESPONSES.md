# DE.DELIVERY.RESPONSES — Table Schema

> Source: `INSERTS/I_F.DE.DELIVERY.RESPONSES` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.DER.RESPONSE.SENDER.REF` | `DeDeliveryResponses_ResponseSenderRef` | TField |  | The reference allocated by the Sender to the response, if any |
| 2 | `DE.DER.RESPONSE.TYPE` | `DeDeliveryResponses_ResponseType` | TField |  | Indicates the type of response.Valid Options are Negative, Warning, Positive |
| 3 | `DE.DER.RESPONSE.CLASS` | `DeDeliveryResponses_ResponseClass` | TField |  | Indicates the class of the response.Valid options are Interface,�Network, DLN |
| 4 | `DE.DER.RESPONSE.SOURCE` | `DeDeliveryResponses_ResponseSource` | TField |  | Indicates the source of the response,For info only. Eg: SWIFT |
| 5 | `DE.DER.ERROR.CODES` | `DeDeliveryResponses_ErrorCodes` |  |  |  |
| 6 | `DE.DER.ERROR.DESCRIPTION` | `DeDeliveryResponses_ErrorDescription` |  |  |  |
| 7 | `DE.DER.ORIG.REQUEST.REF` | `DeDeliveryResponses_OrigRequestRef` | TField |  | The unique reference of the outward message |
| 8 | `DE.DER.RESPONSE.MSG` | `DeDeliveryResponses_ResponseMsg` | TField |  | The original response message. |
| 9 | `DE.DER.RESPONSE.STATUS` | `DeDeliveryResponses_ResponseStatus` | TField |  | The status of the response message.Valid Options are Error, Matched, Unmatched,Hold |
| 10 | `DE.DER.DE.O.HEADER.ID` | `DeDeliveryResponses_DeOHeaderId` | TField |  | Stores the Id of the corresponding Delivery Outward Header, if the Response has been matched with thecorresponding outward message. |
| 11 | `DE.DER.COMMENTS` | `DeDeliveryResponses_Comments` | TField |  | can be used to capture some info when an Unmatched response is manually matched. |
| 12 | `DE.DER.ORIG.TRANSACTION.REF` | `DeDeliveryResponses_OrigTransactionRef` | TField |  | This will be the Transaction Reference (e.g.TPH ID) from the Delivery Outward Header. |
| 13 | `DE.DER.ORIG.BULK.REF` | `DeDeliveryResponses_OrigBulkRef` | TField |  | Stores the original Bulk Reference (e.g.TPH Bulk Reference) from the Delivery Outward Header. |
| 14 | `DE.DER.LAST.UPDATED.DATE` | `DeDeliveryResponses_LastUpdatedDate` | TField |  | The date when the record was last updated. |
| 15 | `DE.DER.RESPONSE.FORMAT` | `DeDeliveryResponses_ResponseFormat` | TField |  | This field is used to identify whether the response is stored for MT (FIN) messages or for ISO messages. If its for FIN messages the field will be updated as FIN, if its ISO message then field will be empty. Possible values are FIN or blank. |
| 16 | `DE.DER.RESERVED.9` | `DeDeliveryResponses_Reserved9` | TField |  |  |
| 17 | `DE.DER.RESERVED.8` | `DeDeliveryResponses_Reserved8` | TField |  |  |
| 18 | `DE.DER.RESERVED.7` | `DeDeliveryResponses_Reserved7` | TField |  |  |
| 19 | `DE.DER.RESERVED.6` | `DeDeliveryResponses_Reserved6` | TField |  |  |
| 20 | `DE.DER.RESERVED.5` | `DeDeliveryResponses_Reserved5` | TField |  |  |
| 21 | `DE.DER.RESERVED.4` | `DeDeliveryResponses_Reserved4` | TField |  |  |
| 22 | `DE.DER.RESERVED.3` | `DeDeliveryResponses_Reserved3` | TField |  |  |
| 23 | `DE.DER.RESERVED.2` | `DeDeliveryResponses_Reserved2` | TField |  |  |
| 24 | `DE.DER.RESERVED.1` | `DeDeliveryResponses_Reserved1` | TField |  |  |
| 25 | `DE.DER.LOCAL.REF` | `DeDeliveryResponses_LocalRef` |  |  |  |
| 26 | `DE.DER.OVERRIDE` | `DeDeliveryResponses_Override` |  |  |  |
| 27 | `DE.DER.RECORD.STATUS` | `DeDeliveryResponses_RecordStatus` | String |  |  |
| 28 | `DE.DER.CURR.NO` | `DeDeliveryResponses_CurrNo` | String |  |  |
| 29 | `DE.DER.INPUTTER` | `DeDeliveryResponses_Inputter` |  |  |  |
| 30 | `DE.DER.DATE.TIME` | `DeDeliveryResponses_DateTime` |  |  |  |
| 31 | `DE.DER.AUTHORISER` | `DeDeliveryResponses_Authoriser` | String |  |  |
| 32 | `DE.DER.CO.CODE` | `DeDeliveryResponses_CoCode` | String |  |  |
| 33 | `DE.DER.DEPT.CODE` | `DeDeliveryResponses_DeptCode` | String |  |  |
| 34 | `DE.DER.AUDITOR.CODE` | `DeDeliveryResponses_AuditorCode` | String |  |  |
| 35 | `DE.DER.AUDIT.DATE.TIME` | `DeDeliveryResponses_AuditDateTime` | String |  |  |
