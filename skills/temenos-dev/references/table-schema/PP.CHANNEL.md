# PP.CHANNEL — Table Schema

> Source: `INSERTS/I_F.PP.CHANNEL` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CHL.ChannelDescription` | `PpChannel_Channeldescription` |  |  |  |
| 2 | `PP.CHL.LOCAL.REF` | `PpChannel_LocalRef` |  |  |  |
| 3 | `PP.CHL.RESERVED.5` | `PpChannel_Reserved5` | TField |  |  |
| 4 | `PP.CHL.RESERVED.4` | `PpChannel_Reserved4` | TField |  |  |
| 5 | `PP.CHL.RESERVED.3` | `PpChannel_Reserved3` | TField |  |  |
| 6 | `PP.CHL.RESERVED.2` | `PpChannel_Reserved2` | TField |  |  |
| 7 | `PP.CHL.RESERVED.1` | `PpChannel_Reserved1` | TField |  |  |
| 8 | `PP.CHL.OVERRIDE` | `PpChannel_Override` |  |  |  |
| 9 | `PP.CHL.RECORD.STATUS` | `PpChannel_RecordStatus` | String |  |  |
| 10 | `PP.CHL.CURR.NO` | `PpChannel_CurrNo` | String |  |  |
| 11 | `PP.CHL.INPUTTER` | `PpChannel_Inputter` |  |  |  |
| 12 | `PP.CHL.DATE.TIME` | `PpChannel_DateTime` |  |  |  |
| 13 | `PP.CHL.AUTHORISER` | `PpChannel_Authoriser` | String |  |  |
| 14 | `PP.CHL.CO.CODE` | `PpChannel_CoCode` | String |  |  |
| 15 | `PP.CHL.DEPT.CODE` | `PpChannel_DeptCode` | String |  |  |
| 16 | `PP.CHL.AUDITOR.CODE` | `PpChannel_AuditorCode` | String |  |  |
| 17 | `PP.CHL.AUDIT.DATE.TIME` | `PpChannel_AuditDateTime` | String |  |  |
