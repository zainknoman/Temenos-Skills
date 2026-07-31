# CM.MESSAGE — Table Schema

> Source: `INSERTS/I_F.CM.MESSAGE` in `CM_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CM.MES.MESSAGE.TYPE` | `CmMessage_MessageType` | A (alphanumeric) |  | Specifies the SWIFT type of message as taken from the header of the message. This field is generated automatically by the system. Validation Rules: 1-5 type A (alphanumeric) characters. This is a NOINPUT field. |
| 2 | `CM.MES.SENDER` | `CmMessage_Sender` | A (alphanumeric) |  | The S.W.I.F.T. address of the sender of the message. This field is generated automatically by the system. Validation Rules: 12 type A (alphanumeric) characters. This is a NOINPUT field. |
| 3 | `CM.MES.RECEIVER` | `CmMessage_Receiver` | A (alphanumeric) |  | Specifies the receiver of the message. This field is generated automatically by the System. No access to this field will be permitted to the User. Validation Rules: 12 type A (alphanumeric) characters. This is a NOINPUT field. |
| 4 | `CM.MES.TXN.REF` | `CmMessage_TxnRef` | A (alphanumeric) |  | Specifies the transaction reference of the message if this is an outbound message. This field is generated automatically by the system. Validation Rules: 30 type A (alphanumeric) characters. This is a NOINPUT field |
| 5 | `CM.MES.DATE.TIME.STAMP` | `CmMessage_DateTimeStamp` | A (alphanumeric) |  | Specifies the date and time the message entered the confirmation matching system. Format DD MMM YY HH:MM This field is generated automatically by the system. Validation Rules: 16 type A (alphanumeric) characters. This is a NOINPUT field. |
| 6 | `CM.MES.MATCH` | `CmMessage_Match` | A (alphanumeric) |  | Specifies the key of the matching message. It may be completed by the system where the messages are automatically matched or may be input when matching is done manually. For maunal input this will normally be completed by selecting from an enquiry display or by drag-and-drop.. Validation Rules: 23-30 type A (alphanumeric) characters. Must be a valid message key selected from the CM.MESSAGE application. |
| 7 | `CM.MES.STATUS` | `CmMessage_Status` | TField |  | Specifies the status of the message. It can be one of the following selections. "WFM" Wait for matching, "MAT" Matched, "POS" Possible match "WOF" Write off . Validation Rules: 3 Alphabetic character. "WFM" Wait for matching, "MAT" Matched, "POS" Possible match or "WOF" Write off file. |
| 8 | `CM.MES.RESERVED11` | `CmMessage_Reserved11` | TField |  |  |
| 9 | `CM.MES.MATCH.DATE` | `CmMessage_MatchDate` | TField |  | Specifies the date on which a match was found. This field will be used in the end of day routine to select messages that have matured and to remove them from the live file to the history file. Validation Rules: Standard date format. |
| 10 | `CM.MES.SWIFT.TAG` | `CmMessage_SwiftTag` |  |  |  |
| 11 | `CM.MES.SWIFT.BODY` | `CmMessage_SwiftBody` |  |  |  |
| 12 | `CM.MES.LOCAL.REF` | `CmMessage_LocalRef` |  |  |  |
| 13 | `CM.MES.RESERVED10` | `CmMessage_Reserved10` | TField |  |  |
| 14 | `CM.MES.RESERVED9` | `CmMessage_Reserved9` | TField |  |  |
| 15 | `CM.MES.RESERVED8` | `CmMessage_Reserved8` | TField |  |  |
| 16 | `CM.MES.RESERVED7` | `CmMessage_Reserved7` | TField |  |  |
| 17 | `CM.MES.RESERVED6` | `CmMessage_Reserved6` | TField |  |  |
| 18 | `CM.MES.RESERVED5` | `CmMessage_Reserved5` | TField |  |  |
| 19 | `CM.MES.RESERVED4` | `CmMessage_Reserved4` | TField |  |  |
| 20 | `CM.MES.RESERVED3` | `CmMessage_Reserved3` | TField |  |  |
| 21 | `CM.MES.RESERVED2` | `CmMessage_Reserved2` | TField |  |  |
| 22 | `CM.MES.RESERVED1` | `CmMessage_Reserved1` | TField |  |  |
| 23 | `CM.MES.OVERRIDE` | `CmMessage_Override` |  |  |  |
| 24 | `CM.MES.RECORD.STATUS` | `CmMessage_RecordStatus` | String |  |  |
| 25 | `CM.MES.CURR.NO` | `CmMessage_CurrNo` | String |  |  |
| 26 | `CM.MES.INPUTTER` | `CmMessage_Inputter` |  |  |  |
| 27 | `CM.MES.DATE.TIME` | `CmMessage_DateTime` |  |  |  |
| 28 | `CM.MES.AUTHORISER` | `CmMessage_Authoriser` | String |  |  |
| 29 | `CM.MES.CO.CODE` | `CmMessage_CoCode` | String |  |  |
| 30 | `CM.MES.DEPT.CODE` | `CmMessage_DeptCode` | String |  |  |
| 31 | `CM.MES.AUDITOR.CODE` | `CmMessage_AuditorCode` | String |  |  |
| 32 | `CM.MES.AUDIT.DATE.TIME` | `CmMessage_AuditDateTime` | String |  |  |
