# PROTOCOL.DETAILS — Table Schema

> Source: `INSERTS/I_F.PROTOCOL.DETAILS` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRO.DET.PROCESS.DATE` | `ProtocolDetails_ProcessDate` | TField |  | Identifies the date of business which was being processed on the System at the time the activity was recorded. his is normally, but not necessarily, the same date as the System date in the Record ID (Field 0). Sometimes the System may be being used to process work for another date, e.g. finishing Friday's work on Saturday. When this date is displayed it is reformatted - DD MMM YYYY e.g. 19 FEB 1985 Validation Rules: YYYYMMDD |
| 2 | `PRO.DET.TIME.MSECS` | `ProtocolDetails_TimeMsecs` | TField |  | Specifies the time of recorded event in milli seconds. Validation Rules: 1)1-15 numeric characters HHMMSSMSS 2)Time is reformatted HH:MM:SS:MSS |
| 3 | `PRO.DET.TERMINAL.ID` | `ProtocolDetails_TerminalId` | A (alphanumeric) |  | Identifies the terminal at which the recorded activity took place. The terminal id is in two parts separated by a space eg. NN XX. Where NN is the Universe user number and XX is the last two characters of the UNIX terminal id. This provides the ability to trace the user both at Universe and UNIX levels. Validation Rules: 0-15 type A (alphanumeric) characters. |
| 4 | `PRO.DET.COMPANY.ID` | `ProtocolDetails_CompanyId` | A (alphanumeric) |  | Identifies the Company whose records were being accessed by the User who performed the recorded activity. his is the Company name held in Field 1 of the COMPANY record (Ref: General Tables). The Company accessed is determined by the Company Code(s) held in the COMPANY field (Field 5) of the USER record. If no User is Signed On, this field is not used (e.g. if the recorded activity was an attempt to SIGN.ON using an unknown SIGN.ON.NAME). Validation Rules: 0-25 type A (alphanumeric) characters. |
| 5 | `PRO.DET.USER` | `ProtocolDetails_User` | TField |  | Identifies the User who had signed on at the terminal where the recorded activity was performed. his is the USER ID (Field 0) of the USER record. If the User was not Signed On at the time of the recorded activity, this field will not be used (e.g. if recorded activity was an attempt to Sign On using an unknown Sign On Name). Validation Rules: 0-16 type AA (alphanumeric, first character alpha) characters. |
| 6 | `PRO.DET.APPLICATION` | `ProtocolDetails_Application` | TField |  | Validation Rules: 0-25 type SSS (uppercase alpha) characters. |
| 7 | `PRO.DET.LEVEL.FUNCTION` | `ProtocolDetails_LevelFunction` | TField |  | his field is not used when logging permitted activities except for Users with FUNCTION ID LOG (Field 28 in USER) equal to Y. Level 1 indicates that the Application was accessed directly. Level 2 indicates that the Application was accessed from another Application via '!' mark. Validation Rules: 1 numeric character (Level) and 1 type AAA (alpha) character (Function) |
| 8 | `PRO.DET.APP.ID` | `ProtocolDetails_AppId` | TField |  | Respective application record id |
| 9 | `PRO.DET.REMARK` | `ProtocolDetails_Remark` | A (alphanumeric) |  | Used when security violations are recorded, to explain why the System would not allow the attempted activity. Also, below values gets updated, 1. TRANSACTION.SUCCESSFUL.COMMIT - When successful transaction committed to disk. 2. ENQUIRY.SELECTION.DETAILS - Enquiry executed with selection criteria, this is when APPLICATION.LOG = Y in user profile as followed for normal enquiry request Validation Rules: 0-35 type A (alphanumeric) characters. |
| 10 | `PRO.DET.FIELD.NAME` | `ProtocolDetails_FieldName` |  |  |  |
| 11 | `PRO.DET.FIELD.OLD.VALUE` | `ProtocolDetails_FieldOldValue` |  |  |  |
| 12 | `PRO.DET.FIELD.NEW.VALUE` | `ProtocolDetails_FieldNewValue` |  |  |  |
| 13 | `PRO.DET.CURR.NO` | `ProtocolDetails_CurrNo` | String |  | Curr no of the application |
| 14 | `PRO.DET.FIN.TYPE` | `ProtocolDetails_FinType` | TField |  | Possible values are YES or NO |
| 15 | `PRO.DET.RESERVED.2` | `ProtocolDetails_Reserved2` | TField |  |  |
| 16 | `PRO.DET.RESERVED.3` | `ProtocolDetails_Reserved3` | TField |  |  |
| 17 | `PRO.DET.RESERVED.4` | `ProtocolDetails_Reserved4` | TField |  |  |
| 18 | `PRO.DET.RESERVED.5` | `ProtocolDetails_Reserved5` | TField |  |  |
| 19 | `PRO.DET.RESERVED.6` | `ProtocolDetails_Reserved6` | TField |  |  |
| 20 | `PRO.DET.RESERVED.7` | `ProtocolDetails_Reserved7` | TField |  |  |
| 21 | `PRO.DET.RESERVED.8` | `ProtocolDetails_Reserved8` | TField |  |  |
| 22 | `PRO.DET.RESERVED.9` | `ProtocolDetails_Reserved9` | TField |  |  |
| 23 | `PRO.DET.RESERVED.10` | `ProtocolDetails_Reserved10` | TField |  |  |
