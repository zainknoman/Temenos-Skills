# DE.MSG.CHARS.RULE — Table Schema

> Source: `INSERTS/I_F.DE.MSG.CHARS.RULE` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.CHRUL.DESCRIPTION` | `DeMsgCharsRule_Description` | TField |  | Captures the description which explain the purpose of this record |
| 2 | `DE.CHRUL.FIELD.NAME` | `DeMsgCharsRule_FieldName` |  |  |  |
| 3 | `DE.CHRUL.ALT.CHAR.ID` | `DeMsgCharsRule_AltCharId` |  |  |  |
| 4 | `DE.CHRUL.RESERVED.5` | `DeMsgCharsRule_Reserved5` | TField |  |  |
| 5 | `DE.CHRUL.RESERVED.4` | `DeMsgCharsRule_Reserved4` | TField |  |  |
| 6 | `DE.CHRUL.RESERVED.3` | `DeMsgCharsRule_Reserved3` | TField |  |  |
| 7 | `DE.CHRUL.RESERVED.2` | `DeMsgCharsRule_Reserved2` | TField |  |  |
| 8 | `DE.CHRUL.RESERVED.1` | `DeMsgCharsRule_Reserved1` | TField |  |  |
| 9 | `DE.CHRUL.LOCAL.REF` | `DeMsgCharsRule_LocalRef` |  |  |  |
| 10 | `DE.CHRUL.OVERRIDE` | `DeMsgCharsRule_Override` |  |  |  |
| 11 | `DE.CHRUL.RECORD.STATUS` | `DeMsgCharsRule_RecordStatus` | String |  |  |
| 12 | `DE.CHRUL.CURR.NO` | `DeMsgCharsRule_CurrNo` | String |  |  |
| 13 | `DE.CHRUL.INPUTTER` | `DeMsgCharsRule_Inputter` |  |  |  |
| 14 | `DE.CHRUL.DATE.TIME` | `DeMsgCharsRule_DateTime` |  |  |  |
| 15 | `DE.CHRUL.AUTHORISER` | `DeMsgCharsRule_Authoriser` | String |  |  |
| 16 | `DE.CHRUL.CO.CODE` | `DeMsgCharsRule_CoCode` | String |  |  |
| 17 | `DE.CHRUL.DEPT.CODE` | `DeMsgCharsRule_DeptCode` | String |  |  |
| 18 | `DE.CHRUL.AUDITOR.CODE` | `DeMsgCharsRule_AuditorCode` | String |  |  |
| 19 | `DE.CHRUL.AUDIT.DATE.TIME` | `DeMsgCharsRule_AuditDateTime` | String |  |  |
