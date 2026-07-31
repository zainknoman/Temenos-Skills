# BRBASE.JD.INTERFACE.MESSAGE — Table Schema

> Source: `INSERTS/I_F.BRBASE.JD.INTERFACE.MESSAGE` in `BRBASE_InterfaceConnector.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IN.MSG.INTERFACE.ID.TAG` | `BrbaseJdInterfaceMessage_InterfaceIdTag` |  |  |  |
| 2 | `IN.MSG.OUTGOING.MESSAGE.ID` | `BrbaseJdInterfaceMessage_OutgoingMessageId` |  |  |  |
| 3 | `IN.MSG.TABLE.NAME` | `BrbaseJdInterfaceMessage_TableName` |  |  |  |
| 4 | `IN.MSG.FIELD.NAME` | `BrbaseJdInterfaceMessage_FieldName` |  |  |  |
| 5 | `IN.MSG.RESPONSE.TYPE` | `BrbaseJdInterfaceMessage_ResponseType` |  |  |  |
| 6 | `IN.MSG.MESSAGE.TYPE.TAG` | `BrbaseJdInterfaceMessage_MessageTypeTag` |  |  |  |
| 7 | `IN.MSG.INCOMING.MESSAGES` | `BrbaseJdInterfaceMessage_IncomingMessages` |  |  |  |
| 8 | `IN.MSG.MAPPING.ID` | `BrbaseJdInterfaceMessage_MappingId` |  |  |  |
| 9 | `IN.MSG.RESERVED.1` | `BrbaseJdInterfaceMessage_Reserved1` |  |  |  |
| 10 | `IN.MSG.RESERVED.2` | `BrbaseJdInterfaceMessage_Reserved2` |  |  |  |
| 11 | `IN.MSG.RESERVED.3` | `BrbaseJdInterfaceMessage_Reserved3` |  |  |  |
| 12 | `IN.MSG.RETURN.TAG` | `BrbaseJdInterfaceMessage_ReturnTag` |  |  |  |
| 13 | `IN.MSG.INCOMING.MESSAGE.DETAIL` | `BrbaseJdInterfaceMessage_IncomingMessageDetail` |  |  |  |
| 14 | `IN.MSG.POST.UPDATE.ROUTINE` | `BrbaseJdInterfaceMessage_PostUpdateRoutine` |  |  |  |
| 15 | `IN.MSG.IDENTIFIER` | `BrbaseJdInterfaceMessage_Identifier` |  |  |  |
| 16 | `IN.MSG.RESERVED.4` | `BrbaseJdInterfaceMessage_Reserved4` |  |  |  |
| 17 | `IN.MSG.RESERVED.5` | `BrbaseJdInterfaceMessage_Reserved5` |  |  |  |
| 18 | `IN.MSG.RESERVED.6` | `BrbaseJdInterfaceMessage_Reserved6` |  |  |  |
| 19 | `IN.MSG.ERROR.TAG` | `BrbaseJdInterfaceMessage_ErrorTag` |  |  |  |
| 20 | `IN.MSG.OUTGOING.MESSAGE` | `BrbaseJdInterfaceMessage_OutgoingMessage` | TField |  | Message type that is processed in external system, for example SCG0011. This field is populated once the execution request is sent. It should be a valid BRBASE.JD.INTERFACE.MAPPING record. |
| 21 | `IN.MSG.T24.RECORD.ID` | `BrbaseJdInterfaceMessage_T24RecordId` |  |  |  |
| 22 | `IN.MSG.INCOMING.MESSAGE` | `BrbaseJdInterfaceMessage_IncomingMessage` | TField |  | Message type of the received message response, for example SCG0011R1.This field is populated once the incoming message is received. It should be a valid BRBASE.JD.INTERFACE.MAPPING record. |
| 23 | `IN.MSG.XML.RESPONSE` | `BrbaseJdInterfaceMessage_XmlResponse` |  |  |  |
| 24 | `IN.MSG.STATUS.RESPONSE` | `BrbaseJdInterfaceMessage_StatusResponse` | TField |  | Status of the message response, this field indicates if the process was successful or rejected based on the returned code. |
| 25 | `IN.MSG.REQUEST.DATE` | `BrbaseJdInterfaceMessage_RequestDate` | TField |  | Date on which the request was performed. |
| 26 | `IN.MSG.RESPONSE.DATE` | `BrbaseJdInterfaceMessage_ResponseDate` | TField |  | Date on which the incoming response was received. |
| 27 | `IN.MSG.PENDING.RESPONSE` | `BrbaseJdInterfaceMessage_PendingResponse` |  |  |  |
| 28 | `IN.MSG.ERROR.CODE` | `BrbaseJdInterfaceMessage_ErrorCode` |  |  |  |
| 29 | `IN.MSG.DESCRIPTION` | `BrbaseJdInterfaceMessage_Description` |  |  |  |
| 30 | `IN.MSG.RESERVED.7` | `BrbaseJdInterfaceMessage_Reserved7` |  |  |  |
| 31 | `IN.MSG.RESERVED.8` | `BrbaseJdInterfaceMessage_Reserved8` |  |  |  |
| 32 | `IN.MSG.RESERVED.9` | `BrbaseJdInterfaceMessage_Reserved9` |  |  |  |
| 33 | `IN.MSG.BEHAVIOR` | `BrbaseJdInterfaceMessage_Behavior` |  |  |  |
| 34 | `IN.MSG.RESERVED.10` | `BrbaseJdInterfaceMessage_Reserved10` | TField |  | Reserved field for future use. |
| 35 | `IN.MSG.RESERVED.11` | `BrbaseJdInterfaceMessage_Reserved11` | TField |  | Reserved field for future use. |
| 36 | `IN.MSG.RESERVED.12` | `BrbaseJdInterfaceMessage_Reserved12` | TField |  | Reserved field for future use. |
| 37 | `IN.MSG.RESERVED.13` | `BrbaseJdInterfaceMessage_Reserved13` | TField |  | Reserved field for future use. |
| 38 | `IN.MSG.RESERVED.14` | `BrbaseJdInterfaceMessage_Reserved14` | TField |  | Reserved field for future use. |
| 39 | `IN.MSG.RESERVED.15` | `BrbaseJdInterfaceMessage_Reserved15` | TField |  | Reserved field for future use. |
| 40 | `IN.MSG.RESERVED.16` | `BrbaseJdInterfaceMessage_Reserved16` | TField |  | Reserved field for future use. |
| 41 | `IN.MSG.RESERVED.17` | `BrbaseJdInterfaceMessage_Reserved17` | TField |  | Reserved field for future use. |
| 42 | `IN.MSG.RESERVED.18` | `BrbaseJdInterfaceMessage_Reserved18` | TField |  | Reserved field for future use. |
| 43 | `IN.MSG.RESERVED.19` | `BrbaseJdInterfaceMessage_Reserved19` | TField |  | Reserved field for future use. |
| 44 | `IN.MSG.RESERVED.20` | `BrbaseJdInterfaceMessage_Reserved20` | TField |  | Reserved field for future use. |
| 45 | `IN.MSG.RECORD.STATUS` | `BrbaseJdInterfaceMessage_RecordStatus` | String |  |  |
| 46 | `IN.MSG.CURR.NO` | `BrbaseJdInterfaceMessage_CurrNo` | String |  |  |
| 47 | `IN.MSG.INPUTTER` | `BrbaseJdInterfaceMessage_Inputter` |  |  |  |
| 48 | `IN.MSG.DATE.TIME` | `BrbaseJdInterfaceMessage_DateTime` |  |  |  |
| 49 | `IN.MSG.AUTHORISER` | `BrbaseJdInterfaceMessage_Authoriser` | String |  |  |
| 50 | `IN.MSG.CO.CODE` | `BrbaseJdInterfaceMessage_CoCode` | String |  |  |
| 51 | `IN.MSG.DEPT.CODE` | `BrbaseJdInterfaceMessage_DeptCode` | String |  |  |
| 52 | `IN.MSG.AUDITOR.CODE` | `BrbaseJdInterfaceMessage_AuditorCode` | String |  |  |
| 53 | `IN.MSG.AUDIT.DATE.TIME` | `BrbaseJdInterfaceMessage_AuditDateTime` | String |  |  |
