# LUCUPI.ISANOTE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LUCUPI.ISANOTE.PARAMETER` in `LUCUPI_MultilineExtract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LUCUPI.ISANOTE.PARAM.BANK.PROTOCOL.NUMBER` | `LucupiIsanoteParameter_BankProtocolNumber` | TField |  | Bank Protocol Number which reflected in the ISANOTE message. Defaulted to 123 |
| 2 | `BANKING.USER.ID` | `bankingUserId` |  |  |  |
| 3 | `LUCUPI.ISANOTE.PARAM.RESERVED.1` | `LucupiIsanoteParameter_Reserved1` | TField |  |  |
| 4 | `LUCUPI.ISANOTE.PARAM.RESERVED.2` | `LucupiIsanoteParameter_Reserved2` | TField |  |  |
| 5 | `LUCUPI.ISANOTE.PARAM.RESERVED.3` | `LucupiIsanoteParameter_Reserved3` | TField |  |  |
| 6 | `LUCUPI.ISANOTE.PARAM.RESERVED.4` | `LucupiIsanoteParameter_Reserved4` | TField |  |  |
| 7 | `LUCUPI.ISANOTE.PARAM.RESERVED.5` | `LucupiIsanoteParameter_Reserved5` | TField |  |  |
| 8 | `LUCUPI.ISANOTE.PARAM.RESERVED.6` | `LucupiIsanoteParameter_Reserved6` | TField |  |  |
| 9 | `LUCUPI.ISANOTE.PARAM.RESERVED.7` | `LucupiIsanoteParameter_Reserved7` | TField |  |  |
| 10 | `LUCUPI.ISANOTE.PARAM.RESERVED.8` | `LucupiIsanoteParameter_Reserved8` | TField |  |  |
| 11 | `LUCUPI.ISANOTE.PARAM.RESERVED.9` | `LucupiIsanoteParameter_Reserved9` | TField |  |  |
| 12 | `LUCUPI.ISANOTE.PARAM.RESERVED.10` | `LucupiIsanoteParameter_Reserved10` | TField |  |  |
| 13 | `LUCUPI.ISANOTE.PARAM.OVERRIDE` | `LucupiIsanoteParameter_Override` |  |  |  |
| 14 | `LUCUPI.ISANOTE.PARAM.RECORD.STATUS` | `LucupiIsanoteParameter_RecordStatus` | String |  |  |
| 15 | `LUCUPI.ISANOTE.PARAM.CURR.NO` | `LucupiIsanoteParameter_CurrNo` | String |  |  |
| 16 | `LUCUPI.ISANOTE.PARAM.INPUTTER` | `LucupiIsanoteParameter_Inputter` |  |  |  |
| 17 | `LUCUPI.ISANOTE.PARAM.DATE.TIME` | `LucupiIsanoteParameter_DateTime` |  |  |  |
| 18 | `LUCUPI.ISANOTE.PARAM.AUTHORISER` | `LucupiIsanoteParameter_Authoriser` | String |  |  |
| 19 | `LUCUPI.ISANOTE.PARAM.CO.CODE` | `LucupiIsanoteParameter_CoCode` | String |  |  |
| 20 | `LUCUPI.ISANOTE.PARAM.DEPT.CODE` | `LucupiIsanoteParameter_DeptCode` | String |  |  |
| 21 | `LUCUPI.ISANOTE.PARAM.AUDITOR.CODE` | `LucupiIsanoteParameter_AuditorCode` | String |  |  |
| 22 | `LUCUPI.ISANOTE.PARAM.AUDIT.DATE.TIME` | `LucupiIsanoteParameter_AuditDateTime` | String |  |  |
