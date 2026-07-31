# DE.I.HEADER.ARCH — Table Schema

> Source: `INSERTS/I_F.DE.I.HEADER.ARCH` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TYPE` | `type` |  |  |  |
| 2 | `FORMAT` | `format` |  |  |  |
| 3 | `DE.IARCH.APPLICATION` | `DeIHeaderArch_Application` | TField |  | Not used for inward Messages (see APPLICATION.QUEUE). Validation Rules: This is a NOINPUT field. |
| 4 | `DE.IARCH.DISPOSITION` | `DeIHeaderArch_Disposition` | TField |  | Describes the type of processing to be done on this Header. If an incoming message received in Inward Carrier Control is found to contain a testkey it is placed in the inward testkey queue with a disposition of 'ATK'. When the testkey is correctly verified the disposition changes to 'UNFORMATTED' and the message is placed on the unformatted queue for processing by inward formatting. Incorrect verification places the message in the inward repair file with a disposition of 'REPAIR'. The message will also go to repair if the message type as defined in DE.MESSAGE requires a testkey and one is not found in the received message. For incoming messages, if the error code is 'ERROR - TEST KEY MISSING' or 'ERROR - TEST KEY INVALID', the message may only be deleted. If a message received by Inward Carrier Control does not contain or require a testkey, the message has its Disposition set to Unformatted when first put on file by Inward Carrier Control. If Inward Formatting fails the message goes to the Inward Repair Queue with a Disposition of 'Repair' and a description of the error in the Error Code field. It can then either be changed to 'Delete' (put on file as 'Deleted') or 'Resubmit' (put on file as 'Unformatted'). On successful Inward Formatting the message is put onto the appropriate Application's Inward Message Queue and the Disposition set to 'formatted'. For incoming messages, if error code is 'ERROR - TEST KEY MISSING' or 'ERROR - TEST KEY INVALID', message can only be deleted. Validation Rules: Values that are stored on the file: 'UNFORMATTED' 'ATK' 'FORMATTED' 'SELECTED' 'REPAIR' 'DELETED' Values that may be input: 'DELETE' 'RESUBMIT' 'REPAIR' |
| 5 | `CODE` | `code` |  |  |  |
| 6 | `DE.IARCH.PRIORITY` | `DeIHeaderArch_Priority` | TField |  | The original Priority allocated to the message in Mapping, or from the Delivery Product file. For inward TELEX or SWIFT messages which contains a priority line this field is updated with the priority from the message. Default priority of 'N' is used if not present in the message except for inward EUCILD messages which take a priority of 'P' and inward EUCLID headers and trailers which take 'U'. Validation Rules: 'U' (Urgent) or 'P' (Priority) or 'N' (Normal) This is a NOINPUT field. |
| 7 | `DE.IARCH.STATUS` | `DeIHeaderArch_Status` | TField |  | No used for inward messages. Validation Rules: This is a NOINPUT field. |
| 9 | `ENTRY` | `entry` |  |  |  |
| 10 | `NUMBER` | `number` |  |  |  |
| 12 | `COMPANY` | `company` |  |  |  |
| 14 | `ADD.` | `add` |  |  |  |
| 15 | `CARRIER` | `carrier` |  |  |  |
| 16 | `DE.IARCH.LANGUAGE` | `DeIHeaderArch_Language` | TField |  | Not used for inward messages. Validation Rules: This is a NOINPUT field. |
| 17 | `DATE` | `date` |  |  |  |
| 18 | `DE.IARCH.CURRENCY` | `DeIHeaderArch_Currency` | TField |  | Specifies a Currency corresponding to the AMOUNT. Picked up from the inward message text when available or appropriate. Validation Rules: A SWIFT currency code. This is a NOINPUT field. |
| 19 | `DE.IARCH.AMOUNT` | `DeIHeaderArch_Amount` | TField |  | Specifies a value that characterises the message. Picked up from the inward message text when available or appropriate. Validation Rules: Numeric, with a decimal point if that is appropriate to the currency. This is a NOINPUT field. |
| 20 | `DE.IARCH.DEPARTMENT` | `DeIHeaderArch_Department` | TField |  | Specifies the Department designated in the DE.INWARD.ROUTING table to receive the message. For incoming messages Department may be used by the Banking Application to control which transactions are to be visible on any particular screen. Validation Rules: this is a NOINPUT field. |
| 21 | `REF` | `ref` |  |  |  |
| 22 | `QUEUE` | `queue` |  |  |  |
| 23 | `REQ.` | `req` |  |  |  |
| 25 | `NO` | `no` |  |  |  |
| 28 | `DE.IARCH.FORMAT` | `DeIHeaderArch_Format` |  |  |  |
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
| 48 | `DE.IARCH.STP.STATUS` | `DeIHeaderArch_StpStatus` |  |  |  |
| 49 | `DE.IARCH.IF.EVENT.TABLE.LINK` | `DeIHeaderArch_IfEventTableLink` |  |  |  |
| 50 | `DE.IARCH.UETR.REFERENCE` | `DeIHeaderArch_UetrReference` |  |  |  |
| 51 | `DE.IARCH.RESERVED.11` | `DeIHeaderArch_Reserved11` |  |  |  |
| 52 | `DE.IARCH.COPY.MSG` | `DeIHeaderArch_CopyMsg` |  |  |  |
| 54 | `DE.IARCH.MSG.CLASSIFICATION` | `DeIHeaderArch_MsgClassification` | TField |  | This field is used to Identify a Cover message. When there is an incoming SWIFT MT202 COV message or MT205 COV message, this field is updated with the value 'COVER' . Null otherwise. No input field. |
| 55 | `DE.IARCH.INW.HEAD.TRAIL` | `DeIHeaderArch_InwHeadTrail` |  |  |  |
| 56 | `DE.IARCH.OFS.REQ.DET.KEY` | `DeIHeaderArch_OfsReqDetKey` |  |  |  |
| 57 | `DE.IARCH.T24.INW.TRANS.REF` | `DeIHeaderArch_T24InwTransRef` |  |  |  |
| 58 | `DE.IARCH.MAPPING.KEY` | `DeIHeaderArch_MappingKey` | TField |  |  |
| 59 | `DE.IARCH.PORTFOLIO.ID` | `DeIHeaderArch_PortfolioId` | TField |  | Identifies Portfolio Reference Id(SEC.ACC.MASTER) |
| 60 | `DE.IARCH.RESERVED.9` | `DeIHeaderArch_Reserved9` | TField |  |  |
| 61 | `DE.IARCH.RESERVED.8` | `DeIHeaderArch_Reserved8` | TField |  |  |
| 62 | `DE.IARCH.RESERVED.7` | `DeIHeaderArch_Reserved7` | TField |  |  |
| 63 | `DE.IARCH.RESERVED.6` | `DeIHeaderArch_Reserved6` | TField |  |  |
| 64 | `DE.IARCH.RESERVED.5` | `DeIHeaderArch_Reserved5` | TField |  |  |
| 65 | `DE.IARCH.RESERVED.4` | `DeIHeaderArch_Reserved4` | TField |  |  |
| 66 | `DE.IARCH.RESERVED.3` | `DeIHeaderArch_Reserved3` | TField |  |  |
| 67 | `DE.IARCH.LOCAL.REF` | `DeIHeaderArch_LocalRef` |  |  |  |
| 68 | `DE.IARCH.OVERRIDE` | `DeIHeaderArch_Override` |  |  |  |
| 69 | `DE.IARCH.RECORD.STATUS` | `DeIHeaderArch_RecordStatus` | String |  |  |
| 70 | `DE.IARCH.CURR.NO` | `DeIHeaderArch_CurrNo` | String |  |  |
| 71 | `DE.IARCH.INPUTTER` | `DeIHeaderArch_Inputter` |  |  |  |
| 72 | `DE.IARCH.DATE.TIME` | `DeIHeaderArch_DateTime` |  |  |  |
| 73 | `DE.IARCH.AUTHORISER` | `DeIHeaderArch_Authoriser` | String |  |  |
| 74 | `DE.IARCH.CO.CODE` | `DeIHeaderArch_CoCode` | String |  |  |
| 75 | `DE.IARCH.DEPT.CODE` | `DeIHeaderArch_DeptCode` | String |  |  |
| 76 | `DE.IARCH.AUDITOR.CODE` | `DeIHeaderArch_AuditorCode` | String |  |  |
| 77 | `DE.IARCH.AUDIT.DATE.TIME` | `DeIHeaderArch_AuditDateTime` | String |  |  |
| 78 | `DE.IARCH.REQUESTER.DN` | `DeIHeaderArch_RequestorDn` |  |  |  |
| 79 | `DE.IARCH.RESPONDER.DN` | `DeIHeaderArch_ResponderDn` |  |  |  |
| 80 | `DE.IARCH.RESERVED.15` | `DeIHeaderArch_Reserverd15` |  |  |  |
| 81 | `DE.IARCH.RESERVED.14` | `DeIHeaderArch_Reserverd14` |  |  |  |
| 82 | `DE.IARCH.RESERVED.13` | `DeIHeaderArch_Reserverd13` |  |  |  |
| 83 | `DE.IARCH.RESERVED.12` | `DeIHeaderArch_Reserverd12` |  |  |  |
