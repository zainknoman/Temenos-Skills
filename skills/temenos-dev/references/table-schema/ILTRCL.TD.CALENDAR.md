# ILTRCL.TD.CALENDAR — Table Schema

> Source: `INSERTS/I_F.ILTRCL.TD.CALENDAR` in `ILTRCL_TradeCalendarAttributes.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILTRCL.TD.JANUARY` | `IltrclTdCalendar_January` | TField |  | Days of January month for which the trading holidays are configured. |
| 2 | `ILTRCL.TD.FEBRUARY` | `IltrclTdCalendar_February` | TField |  | Days of February month for which the trading holidays are configured. |
| 3 | `ILTRCL.TD.MARCH` | `IltrclTdCalendar_March` | TField |  | Days of March month for which the trading holidays are configured. |
| 4 | `ILTRCL.TD.APRIL` | `IltrclTdCalendar_April` | TField |  | Days of April month for which the trading holidays are configured. |
| 5 | `ILTRCL.TD.MAY` | `IltrclTdCalendar_May` | TField |  | Days of May month for which the trading holidays are configured. |
| 6 | `ILTRCL.TD.JUNE` | `IltrclTdCalendar_June` | TField |  | Days of June month for which the trading holidays are configured. |
| 7 | `ILTRCL.TD.JULY` | `IltrclTdCalendar_July` | TField |  | Days of July month for which the trading holidays are configured. |
| 8 | `ILTRCL.TD.AUGUST` | `IltrclTdCalendar_August` | TField |  | Days of August month for which the trading holidays are configured. |
| 9 | `ILTRCL.TD.SEPTEMBER` | `IltrclTdCalendar_September` | TField |  | Days of September month for which the trading holidays are configured. |
| 10 | `ILTRCL.TD.OCTOBER` | `IltrclTdCalendar_October` | TField |  | Days of October month for which the trading holidays are configured. |
| 11 | `ILTRCL.TD.NOVEMBER` | `IltrclTdCalendar_November` | TField |  | Days of November month for which the trading holidays are configured. |
| 12 | `ILTRCL.TD.DECEMBER` | `IltrclTdCalendar_December` | TField |  | Days of December month for which the trading holidays are configured. |
| 13 | `ILTRCL.TD.WEEKEND.DAYS` | `IltrclTdCalendar_WeekendDays` |  |  |  |
| 14 | `ILTRCL.TD.LOCAL.REF` | `IltrclTdCalendar_LocalRef` |  |  |  |
| 15 | `ILTRCL.TD.OVERRIDE` | `IltrclTdCalendar_Override` |  |  |  |
| 16 | `ILTRCL.TD.RECORD.STATUS` | `IltrclTdCalendar_RecordStatus` | String |  |  |
| 17 | `ILTRCL.TD.CURR.NO` | `IltrclTdCalendar_CurrNo` | String |  |  |
| 18 | `ILTRCL.TD.INPUTTER` | `IltrclTdCalendar_Inputter` |  |  |  |
| 19 | `ILTRCL.TD.DATE.TIME` | `IltrclTdCalendar_DateTime` |  |  |  |
| 20 | `ILTRCL.TD.AUTHORISER` | `IltrclTdCalendar_Authoriser` | String |  |  |
| 21 | `ILTRCL.TD.CO.CODE` | `IltrclTdCalendar_CoCode` | String |  |  |
| 22 | `ILTRCL.TD.DEPT.CODE` | `IltrclTdCalendar_DeptCode` | String |  |  |
| 23 | `ILTRCL.TD.AUDITOR.CODE` | `IltrclTdCalendar_AuditorCode` | String |  |  |
| 24 | `ILTRCL.TD.AUDIT.DATE.TIME` | `IltrclTdCalendar_AuditDateTime` | String |  |  |
