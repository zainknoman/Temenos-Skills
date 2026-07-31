# EB.TABBED.SCREEN — Table Schema

> Source: `INSERTS/I_F.EB.TABBED.SCREEN` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TS.TITLE` | `EbTabbedScreen_Title` |  |  |  |
| 2 | `EB.TS.CONTENT.TYPE` | `EbTabbedScreen_ContentType` |  |  |  |
| 3 | `EB.TS.TAB.TITLE` | `EbTabbedScreen_TabTitle` |  |  |  |
| 4 | `EB.TS.SOURCE` | `EbTabbedScreen_Source` |  |  |  |
| 5 | `EB.TS.SELECT.FROM` | `EbTabbedScreen_SelectFrom` |  |  |  |
| 6 | `EB.TS.SELECT.TO` | `EbTabbedScreen_SelectTo` |  |  |  |
| 7 | `EB.TS.SOURCE.ARGS` | `EbTabbedScreen_SourceArgs` |  |  |  |
| 8 | `EB.TS.RESERVED.10` | `EbTabbedScreen_Reserved10` | TField |  |  |
| 9 | `EB.TS.RESERVED.9` | `EbTabbedScreen_Reserved9` | TField |  |  |
| 10 | `EB.TS.RESERVED.8` | `EbTabbedScreen_Reserved8` | TField |  |  |
| 11 | `EB.TS.RESERVED.7` | `EbTabbedScreen_Reserved7` | TField |  |  |
| 12 | `EB.TS.RESERVED.6` | `EbTabbedScreen_Reserved6` | TField |  |  |
| 13 | `EB.TS.RESERVED.5` | `EbTabbedScreen_Reserved5` | TField |  |  |
| 14 | `EB.TS.RESERVED.4` | `EbTabbedScreen_Reserved4` | TField |  |  |
| 15 | `EB.TS.RESERVED.3` | `EbTabbedScreen_Reserved3` | TField |  |  |
| 16 | `EB.TS.RESERVED.2` | `EbTabbedScreen_Reserved2` | TField |  |  |
| 17 | `EB.TS.OVERRIDE` | `EbTabbedScreen_Override` |  |  |  |
| 18 | `EB.TS.RECORD.STATUS` | `EbTabbedScreen_RecordStatus` | String |  |  |
| 19 | `EB.TS.CURR.NO` | `EbTabbedScreen_CurrNo` | String |  |  |
| 20 | `EB.TS.INPUTTER` | `EbTabbedScreen_Inputter` |  |  |  |
| 21 | `EB.TS.DATE.TIME` | `EbTabbedScreen_DateTime` |  |  |  |
| 22 | `EB.TS.AUTHORISER` | `EbTabbedScreen_Authoriser` | String |  |  |
| 23 | `EB.TS.CO.CODE` | `EbTabbedScreen_CoCode` | String |  |  |
| 24 | `EB.TS.DEPT.CODE` | `EbTabbedScreen_DeptCode` | String |  |  |
| 25 | `EB.TS.AUDITOR.CODE` | `EbTabbedScreen_AuditorCode` | String |  |  |
| 26 | `EB.TS.AUDIT.DATE.TIME` | `EbTabbedScreen_AuditDateTime` | String |  |  |
