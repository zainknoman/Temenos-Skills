# FS.GI.FUND.CALENDAR.DELAY.DAYS — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.CALENDAR.DELAY.DAYS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.PARENT.REF.ID` | `FsGiFundCalendarDelayDays_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.ORA.ROWID` | `FsGiFundCalendarDelayDays_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.FUND.ID` | `FsGiFundCalendarDelayDays_FundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.SHARE.CLASS.CODE` | `FsGiFundCalendarDelayDays_ShareClassCode` | TField |  | Fund share class. Multifonds DB Column is TPART. |
| 5 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.OPERATION.CODE` | `FsGiFundCalendarDelayDays_OperationCode` | TField |  | Operation code for which the delay days are applicable. Multifonds DB Column is COPERATION. |
| 6 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.DELAY.DAYS` | `FsGiFundCalendarDelayDays_DelayDays` | TField |  | Delay days to be taken into account when calculating the trade date. Multifonds DB Column is DELAY_DAYS. |
| 7 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.TYPE.OF.DAYS` | `FsGiFundCalendarDelayDays_TypeOfDays` | TField |  | Type of days. The avaialble options are 0001-Business days, 0002-Calendar days. Multifonds DB Column is TYPE_DAYS. |
| 8 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RESERVED10` | `FsGiFundCalendarDelayDays_Reserved10` | TField |  |  |
| 9 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RESERVED9` | `FsGiFundCalendarDelayDays_Reserved9` | TField |  |  |
| 10 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RESERVED8` | `FsGiFundCalendarDelayDays_Reserved8` | TField |  |  |
| 11 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RESERVED7` | `FsGiFundCalendarDelayDays_Reserved7` | TField |  |  |
| 12 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RESERVED6` | `FsGiFundCalendarDelayDays_Reserved6` | TField |  |  |
| 13 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RESERVED5` | `FsGiFundCalendarDelayDays_Reserved5` | TField |  |  |
| 14 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RESERVED4` | `FsGiFundCalendarDelayDays_Reserved4` | TField |  |  |
| 15 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RESERVED3` | `FsGiFundCalendarDelayDays_Reserved3` | TField |  |  |
| 16 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RESERVED2` | `FsGiFundCalendarDelayDays_Reserved2` | TField |  |  |
| 17 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RESERVED1` | `FsGiFundCalendarDelayDays_Reserved1` | TField |  |  |
| 18 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.LOCAL.REF` | `FsGiFundCalendarDelayDays_LocalRef` |  |  |  |
| 19 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.OVERRIDE` | `FsGiFundCalendarDelayDays_Override` |  |  |  |
| 20 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.RECORD.STATUS` | `FsGiFundCalendarDelayDays_RecordStatus` | String |  |  |
| 21 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.CURR.NO` | `FsGiFundCalendarDelayDays_CurrNo` | String |  |  |
| 22 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.INPUTTER` | `FsGiFundCalendarDelayDays_Inputter` |  |  |  |
| 23 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.DATE.TIME` | `FsGiFundCalendarDelayDays_DateTime` |  |  |  |
| 24 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.AUTHORISER` | `FsGiFundCalendarDelayDays_Authoriser` | String |  |  |
| 25 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.CO.CODE` | `FsGiFundCalendarDelayDays_CoCode` | String |  |  |
| 26 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.DEPT.CODE` | `FsGiFundCalendarDelayDays_DeptCode` | String |  |  |
| 27 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.AUDITOR.CODE` | `FsGiFundCalendarDelayDays_AuditorCode` | String |  |  |
| 28 | `FS.GI.FUND.CALENDAR.DELAY.DAYS.AUDIT.DATE.TIME` | `FsGiFundCalendarDelayDays_AuditDateTime` | String |  |  |
