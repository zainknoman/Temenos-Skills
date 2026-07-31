# PP.MSG.FORMAT.PER.CHANNEL — Table Schema

> Source: `INSERTS/I_F.PP.MSG.FORMAT.PER.CHANNEL` in `PP_MessageAcceptanceService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.MFC.MessageForward` | `PpMsgFormatPerChannel_Messageforward` | TField |  | Indicates if the message is to be forwarded by the payments hub. Possible values: Y - Yes N or Blank - No |
| 2 | `PP.MFC.StoreMessageContent` | `PpMsgFormatPerChannel_Storemessagecontent` | TField |  | Indicates if the Outgoing message is to be logged in PSM.BLOB Table Possible values: Y - Yes N or Blank - No |
| 3 | `PP.MFC.RESERVED.4` | `PpMsgFormatPerChannel_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.MFC.RESERVED.3` | `PpMsgFormatPerChannel_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.MFC.RESERVED.2` | `PpMsgFormatPerChannel_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.MFC.RESERVED.1` | `PpMsgFormatPerChannel_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.MFC.LOCAL.REF` | `PpMsgFormatPerChannel_LocalRef` |  |  |  |
| 8 | `PP.MFC.OVERRIDE` | `PpMsgFormatPerChannel_Override` |  |  |  |
| 9 | `PP.MFC.RECORD.STATUS` | `PpMsgFormatPerChannel_RecordStatus` | String |  |  |
| 10 | `PP.MFC.CURR.NO` | `PpMsgFormatPerChannel_CurrNo` | String |  |  |
| 11 | `PP.MFC.INPUTTER` | `PpMsgFormatPerChannel_Inputter` |  |  |  |
| 12 | `PP.MFC.DATE.TIME` | `PpMsgFormatPerChannel_DateTime` |  |  |  |
| 13 | `PP.MFC.AUTHORISER` | `PpMsgFormatPerChannel_Authoriser` | String |  |  |
| 14 | `PP.MFC.CO.CODE` | `PpMsgFormatPerChannel_CoCode` | String |  |  |
| 15 | `PP.MFC.DEPT.CODE` | `PpMsgFormatPerChannel_DeptCode` | String |  |  |
| 16 | `PP.MFC.AUDITOR.CODE` | `PpMsgFormatPerChannel_AuditorCode` | String |  |  |
| 17 | `PP.MFC.AUDIT.DATE.TIME` | `PpMsgFormatPerChannel_AuditDateTime` | String |  |  |
