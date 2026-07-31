# ST.CALENDAR — Table Schema

> Source: `INSERTS/I_F.ST.CALENDAR` in `ST_Calendar.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CAL.DESCRIPTION` | `StCalendar_Description` |  |  |  |
| 2 | `ST.CAL.DAY.ABBREV` | `StCalendar_DayAbbrev` |  |  |  |
| 3 | `ST.CAL.DAY.NAME` | `StCalendar_DayName` |  |  |  |
| 4 | `ST.CAL.MONTH.ABBREV` | `StCalendar_MonthAbbrev` |  |  |  |
| 5 | `ST.CAL.MONTH.NAME` | `StCalendar_MonthName` |  |  |  |
| 6 | `ST.CAL.MONTH.DAYS` | `StCalendar_MonthDays` |  |  |  |
| 7 | `ST.CAL.LEAP.MONTH.NO` | `StCalendar_LeapMonthNo` | TField |  |  |
| 8 | `ST.CAL.LEAP.MONTH.DAYS` | `StCalendar_LeapMonthDays` | TField |  |  |
| 9 | `ST.CAL.WEEKEND.DAYS` | `StCalendar_WeekendDays` |  |  |  |
| 10 | `ST.CAL.RESERVED.22` | `StCalendar_Reserved22` | TField |  |  |
| 11 | `ST.CAL.RESERVED.21` | `StCalendar_Reserved21` | TField |  |  |
| 12 | `ST.CAL.RESERVED.20` | `StCalendar_Reserved20` | TField |  |  |
| 13 | `ST.CAL.RESERVED.19` | `StCalendar_Reserved19` | TField |  |  |
| 14 | `ST.CAL.RESERVED.18` | `StCalendar_Reserved18` | TField |  |  |
| 15 | `ST.CAL.RESERVED.17` | `StCalendar_Reserved17` | TField |  |  |
| 16 | `ST.CAL.RESERVED.16` | `StCalendar_Reserved16` | TField |  |  |
| 17 | `ST.CAL.RESERVED.15` | `StCalendar_Reserved15` | TField |  |  |
| 18 | `ST.CAL.RESERVED.14` | `StCalendar_Reserved14` | TField |  |  |
| 19 | `ST.CAL.RESERVED.13` | `StCalendar_Reserved13` | TField |  |  |
| 20 | `ST.CAL.RESERVED.12` | `StCalendar_Reserved12` | TField |  |  |
| 21 | `ST.CAL.RESERVED.11` | `StCalendar_Reserved11` | TField |  |  |
| 22 | `ST.CAL.RESERVED.10` | `StCalendar_Reserved10` | TField |  |  |
| 23 | `ST.CAL.RESERVED.9` | `StCalendar_Reserved9` | TField |  |  |
| 24 | `ST.CAL.RESERVED.8` | `StCalendar_Reserved8` | TField |  |  |
| 25 | `ST.CAL.RESERVED.7` | `StCalendar_Reserved7` | TField |  |  |
| 26 | `ST.CAL.RESERVED.6` | `StCalendar_Reserved6` | TField |  |  |
| 27 | `ST.CAL.RESERVED.5` | `StCalendar_Reserved5` | TField |  |  |
| 28 | `ST.CAL.RESERVED.4` | `StCalendar_Reserved4` | TField |  |  |
| 29 | `ST.CAL.RESERVED.3` | `StCalendar_Reserved3` | TField |  |  |
| 30 | `ST.CAL.RESERVED.2` | `StCalendar_Reserved2` | TField |  |  |
| 31 | `ST.CAL.RESERVED.1` | `StCalendar_Reserved1` | TField |  |  |
| 32 | `ST.CAL.LOCAL.REF` | `StCalendar_LocalRef` |  |  |  |
| 33 | `ST.CAL.OVERRIDE` | `StCalendar_Override` |  |  |  |
| 34 | `ST.CAL.RECORD.STATUS` | `StCalendar_RecordStatus` | String |  |  |
| 35 | `ST.CAL.CURR.NO` | `StCalendar_CurrNo` | String |  |  |
| 36 | `ST.CAL.INPUTTER` | `StCalendar_Inputter` |  |  |  |
| 37 | `ST.CAL.DATE.TIME` | `StCalendar_DateTime` |  |  |  |
| 38 | `ST.CAL.AUTHORISER` | `StCalendar_Authoriser` | String |  |  |
| 39 | `ST.CAL.CO.CODE` | `StCalendar_CoCode` | String |  |  |
| 40 | `ST.CAL.DEPT.CODE` | `StCalendar_DeptCode` | String |  |  |
| 41 | `ST.CAL.AUDITOR.CODE` | `StCalendar_AuditorCode` | String |  |  |
| 42 | `ST.CAL.AUDIT.DATE.TIME` | `StCalendar_AuditDateTime` | String |  |  |
