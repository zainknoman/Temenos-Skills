# DE.O.HEADER.ARCH — Table Schema

> Source: `INSERTS/I_F.DE.O.HEADER.ARCH` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TYPE` | `type` |  |  |  |
| 2 | `FORMAT` | `format` |  |  |  |
| 3 | `DE.OARCH.APPLICATION` | `DeOHeaderArch_Application` | TField |  | Specifies the Banking Application that originated the message. This field may contain an application code or may be in the format xxyy, where xx is the application code and yy is the Funds Transfer product code. If this field contains a product code, it will not have been used as part of the application code when reading the Mapping file. Validation Rules: This is a NOINPUT field. It is picked up from the Mapping key when an outward message is created. |
| 4 | `DE.OARCH.DISPOSITION` | `DeOHeaderArch_Disposition` | TField |  | Describes the type of processing to be done on this Header. (Each Message copy also has its own Msg Disposition field.) When the raw data received by APPLICATION.HANDOFF is mapped, the Outward Header is generated with a Disposition of 'Unformatted'. Message fields are also extracted from the raw data and put into the basic Message Type format as defined in the DE.MESSAGE table. If mapping fails then 'Disposition' is set to 'Repair'. The Disposition must then be set to 'Delete' because Mapping cannot be tried again. ('Resubmit' puts a message onto the Unformatted Queue for a second attempt at Formatting, not Mapping, but such is not the case with Mapping.) After being successfully Mapped, Messages on the Unformatted Queue are selected in Priority order to be formatted. During formatting the Disposition is temporarily set to 'Selected' before being reset to 'formatted'. This Disposition field refers to the message as a whole and is set to 'formatted', even though individual copies of a message may be in repair. Formatting causes the Header record to be expanded to include a multivalue set of data for each copy of a message, each with its own 'Msg Disposition' field. If a problem prevents the expansion of a message, such as a missing DE.PRODUCT record, then the Disposition will be set to 'Repair'. However, problems that relate to the detailed formatting of Message fields result in this Disposition field being set to 'formatted' and a Msg Disposition of 'Repair' being set in the appropriate place in the multivalue fields at the end of the record. A Disposition of 'Repair' can be changed to Either 'Resubmit' (which is put on file as 'Unformatted') Or 'Delete' (which is put on file as 'Deleted') If the required Delivery Product record is missing, add the record and change Disposition to RESUBMIT. In an exceptional case where the Disposition of a particular message is 'Selected', but some special circumstance such as a program error is preventing it from being processed by the Formatting routine, then it may be set to 'Repair' in order to be able to continue with the processing of other messages. Validation Rules: Values that are stored on the file: 'UNFORMATTED' 'ATK' 'FORMATTED' 'SELECTED' 'REPAIR' 'DELETED' Values that may be input: 'DELETE' 'RESUBMIT' 'REPAIR' |
| 5 | `CODE` | `code` |  |  |  |
| 6 | `DE.OARCH.PRIORITY` | `DeOHeaderArch_Priority` | TField |  | The original Priority allocated to the message in Mapping, or from the Delivery Product file. Priority is generally set from the Product record that is used during the Formatting of the Message. It can alternatively be specifically set up by the Banking Application and then put into the Header during Mapping. A Priority set by the Banking Application may be increased by the Delivery System during formatting but cannot be reduced, i.e. it may only be changed from Normal to Priority or Urgent, or from Priority to Urgent. However, the priority of a message may be increased or decreased by the user by entering 'U', 'P' or 'N' in this field. During formatting, the Header record is expanded to include a multivalue set of data for each copy of the message. Priority can only be amended if the multivalue set (fields CARRIER ADDRESS NO to FORM TYPE) is not present; if the multivalue set is present, MSG PRIORITY must be used. Validation Rules: 'U' (Urgent) or 'P' (Priority) or 'N' (Normal) |
| 7 | `DE.OARCH.STATUS` | `DeOHeaderArch_Status` | TField |  | Specifies whether a message is to be 'Held', or to wait for a period of time. Status can only be entered before the record is expanded, when the disposition will be 'Unformatted' or 'Repair'. When the record is expanded the Msg Status will be set to the value in Status. 'HOLD' will cause the message, once formatted, to stay on the Hold Queue until Msg Status is changed to 'Release'. 'HOLD hh:mm' and 'WAIT hh:mm' will cause message, once formatted, to stay in the Hold Queue until that time. (For WAIT hh:mm, the time to wait (hh:mm) will be added to the current time to produce a status of HOLD hh:mm.) 'RELEASE' will remove a Status of 'HOLD' or 'HOLD hh:mm'. If batching is required and a message is to be held, the message will wait in the hold queue before being released to the batching file. Messages which require testkeys will be placed on the hold queue until realeased and will then be passed on to the testkey queue. Validation Rules: 1 'HOLD' (Hold indefinitely) 2 'HOLD' Hours ':' Minutes (Hold until a time of day.) 3 'WAIT' Hours ':' Minutes (Wait for a period of time.) 4 'RELEASE' Can only be entered if the Outward Header has not been expanded. |
| 9 | `ENTRY` | `entry` |  |  |  |
| 10 | `NUMBER` | `number` |  |  |  |
| 12 | `COMPANY` | `company` |  |  |  |
| 14 | `ADD` | `add` |  |  |  |
| 15 | `CARRIER` | `carrier` |  |  |  |
| 16 | `DE.OARCH.LANGUAGE` | `DeOHeaderArch_Language` | TField |  | Specifies the Language that should be used for a printed message. This Language field will usually be picked up during Mapping from a field set up by the Banking Application and will therefore contain the Language of the Customer who is to receive the message. Validation Rules: 2 type AAA (Alpha) characters. This is a NOINPUT field - picked up in Mapping, or defaults to the first Language code. |
| 17 | `DATE` | `date` |  |  |  |
| 18 | `DE.OARCH.CURRENCY` | `DeOHeaderArch_Currency` | TField |  | Specifies a Currency corresponding to the AMOUNT. Used for Statistics and Disposition Control. Validation Rules: A SWIFT currency code. This is a NOINPUT field. |
| 19 | `DE.OARCH.AMOUNT` | `DeOHeaderArch_Amount` | TField |  | Specifies a value that characterises the message. Used for Disposition Control and statistical reporting. Validation Rules: Numeric, with a decimal point if that is appropriate to the currency. This is a NOINPUT field. |
| 20 | `DE.OARCH.DEPARTMENT` | `DeOHeaderArch_Department` | TField | Yes | Specifies the Department where the message originated. Department is used if only messages for a particular department are to be printed. It is also used for management information, accounting and statistics. In the Mapping of outgoing Messages this is a mandatory field. Validation Rules: This is a NOINPUT field. |
| 21 | `REF` | `ref` |  |  |  |
| 22 | `QUEUE` | `queue` |  |  |  |
| 23 | `REQ.` | `req` |  |  |  |
| 25 | `NO` | `no` |  |  |  |
| 28 | `DE.OARCH.FORMAT` | `DeOHeaderArch_Format` |  |  |  |
| 29 | `LANGUAGE` | `language` |  |  |  |
| 30 | `PRIORITY` | `priority` |  |  |  |
| 31 | `STATUS` | `status` |  |  |  |
| 32 | `DISPOSITION` | `disposition` |  |  |  |
| 34 | `NAME` | `name` |  |  |  |
| 36 | `ADDRESS` | `address` |  |  |  |
| 37 | `STAMP` | `stamp` |  |  |  |
| 39 | `ADR` | `adr` |  |  |  |
| 42 | `PDE` | `pde` |  |  |  |
| 45 | `VER` | `ver` |  |  |  |
| 46 | `AUTH.` | `auth` |  |  |  |
| 47 | `NO.` | `no` |  |  |  |
| 48 | `DE.OARCH.STP.STATUS` | `DeOHeaderArch_StpStatus` |  |  |  |
| 49 | `DE.OARCH.IF.EVENT.TABLE.LINK` | `DeOHeaderArch_IfEventTableLink` |  |  |  |
| 50 | `DE.OARCH.UETR.REFERENCE` | `DeOHeaderArch_UetrReference` |  |  |  |
| 51 | `DE.OARCH.RESERVED.11` | `DeOHeaderArch_Reserved11` |  |  |  |
| 52 | `DE.OARCH.COPY.MSG` | `DeOHeaderArch_CopyMsg` |  |  |  |
| 54 | `DE.OARCH.MSG.CLASSIFICATION` | `DeOHeaderArch_MsgClassification` | TField |  | This field is used to Identify a Cover message. Example, to identify a MT202 COV message and MT205 COV message. Holds the value 'COVER' when processing cover messages. Null otherwise. No input field. |
| 55 | `DE.OARCH.INW.HEAD.TRAIL` | `DeOHeaderArch_InwHeadTrail` |  |  |  |
| 56 | `DE.OARCH.OFS.REQ.DET.KEY` | `DeOHeaderArch_OfsReqDetKey` |  |  |  |
| 57 | `DE.OARCH.T24.INW.TRANS.REF` | `DeOHeaderArch_T24InwTransRef` |  |  |  |
| 58 | `DE.OARCH.MAPPING.KEY` | `DeOHeaderArch_MappingKey` | TField |  | Specifies the DE.MAPPING of the message generated Validation Rules: This is a NOINPUT field. It is system populated when an outward message is created. |
| 59 | `DE.OARCH.PORTFOLIO.ID` | `DeOHeaderArch_PortfolioId` | TField |  | Identifies Portfolio Reference Id(SEC.ACC.MASTER) |
| 60 | `DE.OARCH.PAYLOAD.FILE.NAME` | `DeOHeaderArch_PayloadFileName` | TField |  | Stores the name of the payload file. Incase of large payload messages, the payload will be stored in the file system. So that by referring this field the payload file can be located under the file system. |
| 61 | `DE.OARCH.RESERVED.8` | `DeOHeaderArch_Reserved8` | TField |  |  |
| 62 | `DE.OARCH.RESERVED.7` | `DeOHeaderArch_Reserved7` | TField |  |  |
| 63 | `DE.OARCH.RESERVED.6` | `DeOHeaderArch_Reserved6` | TField |  |  |
| 64 | `DE.OARCH.RESERVED.5` | `DeOHeaderArch_Reserved5` | TField |  |  |
| 65 | `DE.OARCH.RESERVED.4` | `DeOHeaderArch_Reserved4` | TField |  |  |
| 66 | `DE.OARCH.RESERVED.3` | `DeOHeaderArch_Reserved3` | TField |  |  |
| 67 | `DE.OARCH.LOCAL.REF` | `DeOHeaderArch_LocalRef` |  |  |  |
| 68 | `DE.OARCH.OVERRIDE` | `DeOHeaderArch_Override` |  |  |  |
| 69 | `DE.OARCH.RECORD.STATUS` | `DeOHeaderArch_RecordStatus` | String |  |  |
| 70 | `DE.OARCH.CURR.NO` | `DeOHeaderArch_CurrNo` | String |  |  |
| 71 | `DE.OARCH.INPUTTER` | `DeOHeaderArch_Inputter` |  |  |  |
| 72 | `DE.OARCH.DATE.TIME` | `DeOHeaderArch_DateTime` |  |  |  |
| 73 | `DE.OARCH.AUTHORISER` | `DeOHeaderArch_Authoriser` | String |  |  |
| 74 | `DE.OARCH.CO.CODE` | `DeOHeaderArch_CoCode` | String |  |  |
| 75 | `DE.OARCH.DEPT.CODE` | `DeOHeaderArch_DeptCode` | String |  |  |
| 76 | `DE.OARCH.AUDITOR.CODE` | `DeOHeaderArch_AuditorCode` | String |  |  |
| 77 | `DE.OARCH.AUDIT.DATE.TIME` | `DeOHeaderArch_AuditDateTime` | String |  |  |
| 78 | `DE.OARCH.REQUESTER.DN` | `DeOHeaderArch_RequestorDn` |  |  |  |
| 79 | `DE.OARCH.RESPONDER.DN` | `DeOHeaderArch_ResponderDn` |  |  |  |
| 80 | `DE.OARCH.RESPONSE.ID` | `DeOHeaderArch_ResponseId` |  |  |  |
| 81 | `DE.OARCH.DLN.REQUESTED` | `DeOHeaderArch_DlnRequested` |  |  |  |
| 82 | `DE.OARCH.DELIVERY.MASTER.ID` | `DeOHeaderArch_DeliveryMasterId` | TField |  | The delivery id of the first message will be passed by the CAMT module as a Master Reference and will be stored as part of each Delivery Outward Header. |
| 83 | `DE.OARCH.BULK.REFERENCE` | `DeOHeaderArch_BulkReference` | TField |  | This will store the Bulk Reference is supplied by the Business Application if the message passed to Delivery is already bulked. |
