# CP.MESSAGE — Table Schema

> Source: `INSERTS/I_F.CP.MESSAGE` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.MSG.MESSAGE` | `CpMessage_Message` |  |  |  |
| 2 | `CP.MSG.MSG.TYPE` | `CpMessage_MsgType` | TField | Yes | This field stores the type of the message. Validation Rules :Mandatory field, 75 string characters.This field stores the values parametrized in EB.Lookup - CP.MSG.TYPE: Confirmation Message, Tooltip Message. |
| 3 | `CP.MSG.RESERVED.20` | `CpMessage_Reserved20` | TField |  |  |
| 4 | `CP.MSG.RESERVED.19` | `CpMessage_Reserved19` | TField |  |  |
| 5 | `CP.MSG.RESERVED.18` | `CpMessage_Reserved18` | TField |  |  |
| 6 | `CP.MSG.RESERVED.17` | `CpMessage_Reserved17` | TField |  |  |
| 7 | `CP.MSG.RESERVED.16` | `CpMessage_Reserved16` | TField |  |  |
| 8 | `CP.MSG.RESERVED.15` | `CpMessage_Reserved15` | TField |  |  |
| 9 | `CP.MSG.RESERVED.14` | `CpMessage_Reserved14` | TField |  |  |
| 10 | `CP.MSG.RESERVED.13` | `CpMessage_Reserved13` | TField |  |  |
| 11 | `CP.MSG.RESERVED.12` | `CpMessage_Reserved12` | TField |  |  |
| 12 | `CP.MSG.RESERVED.11` | `CpMessage_Reserved11` | TField |  |  |
| 13 | `CP.MSG.RESERVED.10` | `CpMessage_Reserved10` | TField |  |  |
| 14 | `CP.MSG.RESERVED.9` | `CpMessage_Reserved9` | TField |  |  |
| 15 | `CP.MSG.RESERVED.8` | `CpMessage_Reserved8` | TField |  |  |
| 16 | `CP.MSG.RESERVED.7` | `CpMessage_Reserved7` | TField |  |  |
| 17 | `CP.MSG.RESERVED.6` | `CpMessage_Reserved6` | TField |  |  |
| 18 | `CP.MSG.RESERVED.5` | `CpMessage_Reserved5` | TField |  |  |
| 19 | `CP.MSG.RESERVED.4` | `CpMessage_Reserved4` | TField |  |  |
| 20 | `CP.MSG.RESERVED.3` | `CpMessage_Reserved3` | TField |  |  |
| 21 | `CP.MSG.RESERVED.2` | `CpMessage_Reserved2` | TField |  |  |
| 22 | `CP.MSG.RESERVED.1` | `CpMessage_Reserved1` | TField |  |  |
| 23 | `CP.MSG.LOCAL.REF` | `CpMessage_LocalRef` |  |  |  |
| 24 | `CP.MSG.OVERRIDE` | `CpMessage_Override` |  |  |  |
| 25 | `CP.MSG.RECORD.STATUS` | `CpMessage_RecordStatus` | String |  |  |
| 26 | `CP.MSG.CURR.NO` | `CpMessage_CurrNo` | String |  |  |
| 27 | `CP.MSG.INPUTTER` | `CpMessage_Inputter` |  |  |  |
| 28 | `CP.MSG.DATE.TIME` | `CpMessage_DateTime` |  |  |  |
| 29 | `CP.MSG.AUTHORISER` | `CpMessage_Authoriser` | String |  |  |
| 30 | `CP.MSG.CO.CODE` | `CpMessage_CoCode` | String |  |  |
| 31 | `CP.MSG.DEPT.CODE` | `CpMessage_DeptCode` | String |  |  |
| 32 | `CP.MSG.AUDITOR.CODE` | `CpMessage_AuditorCode` | String |  |  |
| 33 | `CP.MSG.AUDIT.DATE.TIME` | `CpMessage_AuditDateTime` | String |  |  |
