# PP.ERRORCODE — Table Schema

> Source: `INSERTS/I_F.PP.ERRORCODE` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.ERC.ErrorType` | `PpErrorcode_Errortype` | TField |  | Option field, to input the value for error type. Possible values *, F or T |
| 2 | `PP.ERC.ErrorText` | `PpErrorcode_Errortext` |  |  |  |
| 3 | `PP.ERC.ErrorSeverity` | `PpErrorcode_Errorseverity` | TField |  | Text Field, to input the value for error severity. |
| 4 | `PP.ERC.StatusEventType` | `PpErrorcode_Statuseventtype` |  |  |  |
| 5 | `PP.ERC.RESERVED.4` | `PpErrorcode_Reserved4` | TField |  |  |
| 6 | `PP.ERC.RESERVED.3` | `PpErrorcode_Reserved3` | TField |  |  |
| 7 | `PP.ERC.RESERVED.2` | `PpErrorcode_Reserved2` | TField |  |  |
| 8 | `PP.ERC.RESERVED.1` | `PpErrorcode_Reserved1` | TField |  |  |
| 9 | `PP.ERC.LOCAL.REF` | `PpErrorcode_LocalRef` |  |  |  |
| 10 | `PP.ERC.OVERRIDE` | `PpErrorcode_Override` |  |  |  |
| 11 | `PP.ERC.RECORD.STATUS` | `PpErrorcode_RecordStatus` | String |  |  |
| 12 | `PP.ERC.CURR.NO` | `PpErrorcode_CurrNo` | String |  |  |
| 13 | `PP.ERC.INPUTTER` | `PpErrorcode_Inputter` |  |  |  |
| 14 | `PP.ERC.DATE.TIME` | `PpErrorcode_DateTime` |  |  |  |
| 15 | `PP.ERC.AUTHORISER` | `PpErrorcode_Authoriser` | String |  |  |
| 16 | `PP.ERC.CO.CODE` | `PpErrorcode_CoCode` | String |  |  |
| 17 | `PP.ERC.DEPT.CODE` | `PpErrorcode_DeptCode` | String |  |  |
| 18 | `PP.ERC.AUDITOR.CODE` | `PpErrorcode_AuditorCode` | String |  |  |
| 19 | `PP.ERC.AUDIT.DATE.TIME` | `PpErrorcode_AuditDateTime` | String |  |  |
