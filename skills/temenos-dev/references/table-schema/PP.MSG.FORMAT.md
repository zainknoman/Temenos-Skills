# PP.MSG.FORMAT — Table Schema

> Source: `INSERTS/I_F.PP.MSG.FORMAT` in `PP_MessageAcceptanceService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.MF.MessageFormatDescription` | `PpMsgFormat_Messageformatdescription` |  |  |  |
| 2 | `PP.MF.MessageForward` | `PpMsgFormat_Messageforward` | TField |  | Indicates if the message is to be forwarded or not. Possible values: Y - Yes Blank - No |
| 3 | `PP.MF.RESERVED.5` | `PpMsgFormat_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.MF.RESERVED.4` | `PpMsgFormat_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.MF.RESERVED.3` | `PpMsgFormat_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.MF.RESERVED.2` | `PpMsgFormat_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.MF.RESERVED.1` | `PpMsgFormat_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.MF.LOCAL.REF` | `PpMsgFormat_LocalRef` |  |  |  |
| 9 | `PP.MF.OVERRIDE` | `PpMsgFormat_Override` |  |  |  |
| 10 | `PP.MF.RECORD.STATUS` | `PpMsgFormat_RecordStatus` | String |  |  |
| 11 | `PP.MF.CURR.NO` | `PpMsgFormat_CurrNo` | String |  |  |
| 12 | `PP.MF.INPUTTER` | `PpMsgFormat_Inputter` |  |  |  |
| 13 | `PP.MF.DATE.TIME` | `PpMsgFormat_DateTime` |  |  |  |
| 14 | `PP.MF.AUTHORISER` | `PpMsgFormat_Authoriser` | String |  |  |
| 15 | `PP.MF.CO.CODE` | `PpMsgFormat_CoCode` | String |  |  |
| 16 | `PP.MF.DEPT.CODE` | `PpMsgFormat_DeptCode` | String |  |  |
| 17 | `PP.MF.AUDITOR.CODE` | `PpMsgFormat_AuditorCode` | String |  |  |
| 18 | `PP.MF.AUDIT.DATE.TIME` | `PpMsgFormat_AuditDateTime` | String |  |  |
