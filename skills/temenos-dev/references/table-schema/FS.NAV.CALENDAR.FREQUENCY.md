# FS.NAV.CALENDAR.FREQUENCY — Table Schema

> Source: `INSERTS/I_F.FS.NAV.CALENDAR.FREQUENCY` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.NAV.CALENDAR.FREQUENCY.DESCRIPTION` | `FsNavCalendarFrequency_Description` |  |  |  |
| 2 | `FS.NAV.CALENDAR.FREQUENCY.FILTER.KEY` | `FsNavCalendarFrequency_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.NAV.CALENDAR.FREQUENCY.RECORD.ID` | `FsNavCalendarFrequency_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.NAV.CALENDAR.FREQUENCY.RESERVED10` | `FsNavCalendarFrequency_Reserved10` | TField |  |  |
| 5 | `FS.NAV.CALENDAR.FREQUENCY.RESERVED9` | `FsNavCalendarFrequency_Reserved9` | TField |  |  |
| 6 | `FS.NAV.CALENDAR.FREQUENCY.RESERVED8` | `FsNavCalendarFrequency_Reserved8` | TField |  |  |
| 7 | `FS.NAV.CALENDAR.FREQUENCY.RESERVED7` | `FsNavCalendarFrequency_Reserved7` | TField |  |  |
| 8 | `FS.NAV.CALENDAR.FREQUENCY.RESERVED6` | `FsNavCalendarFrequency_Reserved6` | TField |  |  |
| 9 | `FS.NAV.CALENDAR.FREQUENCY.RESERVED5` | `FsNavCalendarFrequency_Reserved5` | TField |  |  |
| 10 | `FS.NAV.CALENDAR.FREQUENCY.RESERVED4` | `FsNavCalendarFrequency_Reserved4` | TField |  |  |
| 11 | `FS.NAV.CALENDAR.FREQUENCY.RESERVED3` | `FsNavCalendarFrequency_Reserved3` | TField |  |  |
| 12 | `FS.NAV.CALENDAR.FREQUENCY.RESERVED2` | `FsNavCalendarFrequency_Reserved2` | TField |  |  |
| 13 | `FS.NAV.CALENDAR.FREQUENCY.RESERVED1` | `FsNavCalendarFrequency_Reserved1` | TField |  |  |
| 14 | `FS.NAV.CALENDAR.FREQUENCY.LOCAL.REF` | `FsNavCalendarFrequency_LocalRef` |  |  |  |
| 15 | `FS.NAV.CALENDAR.FREQUENCY.OVERRIDE` | `FsNavCalendarFrequency_Override` |  |  |  |
| 16 | `FS.NAV.CALENDAR.FREQUENCY.RECORD.STATUS` | `FsNavCalendarFrequency_RecordStatus` | String |  |  |
| 17 | `FS.NAV.CALENDAR.FREQUENCY.CURR.NO` | `FsNavCalendarFrequency_CurrNo` | String |  |  |
| 18 | `FS.NAV.CALENDAR.FREQUENCY.INPUTTER` | `FsNavCalendarFrequency_Inputter` |  |  |  |
| 19 | `FS.NAV.CALENDAR.FREQUENCY.DATE.TIME` | `FsNavCalendarFrequency_DateTime` |  |  |  |
| 20 | `FS.NAV.CALENDAR.FREQUENCY.AUTHORISER` | `FsNavCalendarFrequency_Authoriser` | String |  |  |
| 21 | `FS.NAV.CALENDAR.FREQUENCY.CO.CODE` | `FsNavCalendarFrequency_CoCode` | String |  |  |
| 22 | `FS.NAV.CALENDAR.FREQUENCY.DEPT.CODE` | `FsNavCalendarFrequency_DeptCode` | String |  |  |
| 23 | `FS.NAV.CALENDAR.FREQUENCY.AUDITOR.CODE` | `FsNavCalendarFrequency_AuditorCode` | String |  |  |
| 24 | `FS.NAV.CALENDAR.FREQUENCY.AUDIT.DATE.TIME` | `FsNavCalendarFrequency_AuditDateTime` | String |  |  |
