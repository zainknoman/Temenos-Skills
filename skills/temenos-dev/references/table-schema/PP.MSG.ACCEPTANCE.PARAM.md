# PP.MSG.ACCEPTANCE.PARAM — Table Schema

> Source: `INSERTS/I_F.PP.MSG.ACCEPTANCE.PARAM` in `PP_MessageAcceptanceService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.MAP.IncomingMsgDirectory` | `PpMsgAcceptanceParam_Incomingmsgdirectory` | TField |  | Specifies the directory over which the payment file is received. Validation Rules: The field can hold upto 128 alphanumeric characters. |
| 2 | `PP.MAP.OriginatingChannel` | `PpMsgAcceptanceParam_Originatingchannel` | TField |  | Specifies the channel through which a message is received. Possible values: SWIFT PMTROUTER EMZ BACS CEC HKICL Validation Rules: Value can be upto 10 alphabetic characters. The value in this field links to field 'ChannelName' in PPT.CHANNEL. |
| 3 | `PP.MAP.SingleMultipleIndicator` | `PpMsgAcceptanceParam_Singlemultipleindicator` | TField |  | Indicates the type of a message. Possible values: "S" � Single "C" � Clearing "B" � Bulk Validation Rules: 1 alphanumeric character. |
| 4 | `PP.MAP.ValidateAPI` | `PpMsgAcceptanceParam_Validateapi` | TField |  | API used to validate an incoming message. Validation Rules:Valid EB.API record of type 'Basic', if the hook is of JBCroutine An EB.API record of type METHOD which implements an interface defined in the EB.API record MESSAGE.PARAM.VALIDATE.API.HOOK. There are five interfaces being implemented based on the channels which message process and implements the correct interfce. The field can hold upto 128 alphanumeric characters. Specify either A jBC subroutine name If originating channel is either of these - AAB_BACS, AUTOREPAIR, HKCLG, PMROUTER, CHQCLG, CCI, SOFIE, USMB_ACH and STOT24 -The routine has 3 passed parameters and enables the implementer to update the message information based on the validation done on message information and message content. For java implementations: An EB.API record of type METHOD which implements an interface defined in the EB.API record PP.MSG.ACC.PARAM.Validateapi.HOOK. This field supports the Message.updateMessageStatus() method. The Message class is in the com.temenos.t24.api.hook.payments package which is in PP_MessageAcceptanceParamHook.jar shipped with T24. |
| 5 | `PP.MAP.CheckDuplicateIndicator` | `PpMsgAcceptanceParam_Checkduplicateindicator` | TField |  | Indicates if a check for duplicate messages is to be performed by the system. Possible values: "Y" - Yes "N" - No Validation Rules: User can modify the content of the field with possible values only. |
| 6 | `PP.MAP.ACKRequiredIndicator` | `PpMsgAcceptanceParam_Ackrequiredindicator` | TField |  | Indicates if a ACK/NACK message is to be sent across, once the message is validated. Possible values: "Y" - Yes "N" - No Validation Rules: User can modify the content of the field with possible values only. |
| 7 | `PP.MAP.ACKAPI` | `PpMsgAcceptanceParam_Ackapi` | TField |  | API used to send a ACK/NACK message. Validation Rules:Valid EB.API record of type 'Basic', if the hook is of JBCroutine An EB.API record of type METHOD which implements an interface defined in the EB.API record MESSAGE.PARAM.ACK.API.HOOK. The field can hold upto 128 alphanumeric characters. |
| 8 | `PP.MAP.ACKNACKQueue` | `PpMsgAcceptanceParam_Acknackqueue` | TField |  | Name of the file used to store ACK/NACK message prior to sending it to an external system. Validation Rules: The field can hold upto 128 alphanumeric characters. |
| 9 | `PP.MAP.MessageConversionFormat` | `PpMsgAcceptanceParam_Messageconversionformat` | TField |  | For future use. |
| 10 | `PP.MAP.ReadMessageAPI` | `PpMsgAcceptanceParam_Readmessageapi` | TField |  | For future use. Validation Rules: The field can hold upto 128 alphanumeric characters. |
| 11 | `PP.MAP.InterpretAPI` | `PpMsgAcceptanceParam_Interpretapi` | TField |  | API used to interpret an incoming SWIFT message. Validation Rules: The field can hold upto 128 alphanumeric characters. |
| 12 | `PP.MAP.MessageForwardAPI` | `PpMsgAcceptanceParam_Messageforwardapi` | TField |  | API used to forward a message which is not intended for processing in payments hub. Validation Rules:Valid EB.API record of type 'Basic', if the hook is of JBCroutine An EB.API record of type METHOD which implements an interface defined in the EB.API record MESSAGE.PARAM.MSG.FORWARD.API.HOOK. This implementation is done at the other local routine "T24SwiftServiceImpl.interpretSwift" from interpretApi field which should be JBC routine. The field can hold upto 128 alphanumeric characters. |
| 13 | `PP.MAP.MessageForwardQueue` | `PpMsgAcceptanceParam_Messageforwardqueue` | TField |  | Local directory path to which a message needs to be forwarded in case the message is not intended for processing in the payments hub. Validation Rules: The field can hold upto 128 alphanumeric characters. |
| 14 | `PP.MAP.LOCAL.REF` | `PpMsgAcceptanceParam_LocalRef` |  |  |  |
| 15 | `PP.MAP.DebulkAPI` | `PpMsgAcceptanceParam_Debulkapi` | TField |  | API to be used to debulk a clearing/batch message. Validation Rules:Valid EB.API record of type 'Basic', if the hook is of JBCroutine An EB.API record of type METHOD which implements an interface defined in the EB.API record MESSAGE.PARAM.DEBULK.API.HOOK. 255 alphanumeric characters. |
| 16 | `PP.MAP.FileACKMessageType` | `PpMsgAcceptanceParam_Fileackmessagetype` | TField |  | This field hold the name of status report message to be send to submitter of original transaction when a status report is created for a received file (File level acceptance) |
| 17 | `PP.MAP.BulkFormat` | `PpMsgAcceptanceParam_Bulkformat` |  |  |  |
| 18 | `PP.MAP.AcceptanceEnrichAPI` | `PpMsgAcceptanceParam_Acceptanceenrichapi` |  |  |  |
| 19 | `PP.MAP.FileDuplicateCheckID` | `PpMsgAcceptanceParam_Fileduplicatecheckid` | TField |  | This dropdown lists the records defined in the EB.DUPLICATE.TYPE If duplicate check must be performed then it must be populated with ID from EB.DUPLICATE.TYPE Validation Rules: The value in this field should be a valid definition in the table EB.DUPLICATE.TYPE |
| 20 | `PP.MAP.OVERRIDE` | `PpMsgAcceptanceParam_Override` |  |  |  |
| 21 | `PP.MAP.RECORD.STATUS` | `PpMsgAcceptanceParam_RecordStatus` | String |  |  |
| 22 | `PP.MAP.CURR.NO` | `PpMsgAcceptanceParam_CurrNo` | String |  |  |
| 23 | `PP.MAP.INPUTTER` | `PpMsgAcceptanceParam_Inputter` |  |  |  |
| 24 | `PP.MAP.DATE.TIME` | `PpMsgAcceptanceParam_DateTime` |  |  |  |
| 25 | `PP.MAP.AUTHORISER` | `PpMsgAcceptanceParam_Authoriser` | String |  |  |
| 26 | `PP.MAP.CO.CODE` | `PpMsgAcceptanceParam_CoCode` | String |  |  |
| 27 | `PP.MAP.DEPT.CODE` | `PpMsgAcceptanceParam_DeptCode` | String |  |  |
| 28 | `PP.MAP.AUDITOR.CODE` | `PpMsgAcceptanceParam_AuditorCode` | String |  |  |
| 29 | `PP.MAP.AUDIT.DATE.TIME` | `PpMsgAcceptanceParam_AuditDateTime` | String |  |  |
