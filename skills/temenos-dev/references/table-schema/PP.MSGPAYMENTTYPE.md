# PP.MSGPAYMENTTYPE — Table Schema

> Source: `INSERTS/I_F.PP.MSGPAYMENTTYPE` in `PP_MessageMappingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.MPT.MessagePaymentTypeDesc` | `PpMsgpaymenttype_Messagepaymenttypedesc` |  |  |  |
| 2 | `PP.MPT.OrderEntryFlag` | `PpMsgpaymenttype_Orderentryflag` | TField |  | This field will allow users to configure MessageTypes which are allowed in the Manual Order Entry screen. These flag signifies if the message type can be selected for an Order Entry Payment. |
| 3 | `PP.MPT.RESERVED.5` | `PpMsgpaymenttype_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.MPT.RESERVED.4` | `PpMsgpaymenttype_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.MPT.RESERVED.3` | `PpMsgpaymenttype_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.MPT.RESERVED.2` | `PpMsgpaymenttype_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.MPT.RESERVED.1` | `PpMsgpaymenttype_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.MPT.LOCAL.REF` | `PpMsgpaymenttype_LocalRef` |  |  |  |
| 9 | `PP.MPT.OVERRIDE` | `PpMsgpaymenttype_Override` |  |  |  |
| 10 | `PP.MPT.RECORD.STATUS` | `PpMsgpaymenttype_RecordStatus` | String |  |  |
| 11 | `PP.MPT.CURR.NO` | `PpMsgpaymenttype_CurrNo` | String |  |  |
| 12 | `PP.MPT.INPUTTER` | `PpMsgpaymenttype_Inputter` |  |  |  |
| 13 | `PP.MPT.DATE.TIME` | `PpMsgpaymenttype_DateTime` |  |  |  |
| 14 | `PP.MPT.AUTHORISER` | `PpMsgpaymenttype_Authoriser` | String |  |  |
| 15 | `PP.MPT.CO.CODE` | `PpMsgpaymenttype_CoCode` | String |  |  |
| 16 | `PP.MPT.DEPT.CODE` | `PpMsgpaymenttype_DeptCode` | String |  |  |
| 17 | `PP.MPT.AUDITOR.CODE` | `PpMsgpaymenttype_AuditorCode` | String |  |  |
| 18 | `PP.MPT.AUDIT.DATE.TIME` | `PpMsgpaymenttype_AuditDateTime` | String |  |  |
