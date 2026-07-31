# FS.GA.FUND.CALENDAR — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUND.CALENDAR` in `FS_FundMaster.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUND.CALENDAR.PARENT.REF.ID` | `FsGaFundCalendar_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUND.CALENDAR.ORA.ROWID` | `FsGaFundCalendar_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUND.CALENDAR.FUND.ID` | `FsGaFundCalendar_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.FUND.CALENDAR.FREQUENCY` | `FsGaFundCalendar_Frequency` | TField |  | Frequency code for processing Multifonds DB Column is CFREQ. |
| 5 | `FS.GA.FUND.CALENDAR.FIXED.NAV.DAY` | `FsGaFundCalendar_FixedNavDay` | TField |  | This field displays fixed NAV day information provided in calendar button of fund master setup Multifonds DB Column is FIXED_NAV_DAY. |
| 6 | `FS.GA.FUND.CALENDAR.FIXED.WEEK` | `FsGaFundCalendar_FixedWeek` | TField |  | This field displays fixed week information provided in calendar button of fund master setup Multifonds DB Column is FIXED_WEEK. |
| 7 | `FS.GA.FUND.CALENDAR.WEEK.DAY` | `FsGaFundCalendar_WeekDay` | TField |  | This field displays week day information provided in calendar button of fund master setup Multifonds DB Column is WEEK_DAY. |
| 8 | `FS.GA.FUND.CALENDAR.SEQUENCE.NUMBER` | `FsGaFundCalendar_SequenceNumber` | TField |  | Sequence Number Multifonds DB Column is SEQ_NO. |
| 9 | `FS.GA.FUND.CALENDAR.RESERVED10` | `FsGaFundCalendar_Reserved10` | TField |  |  |
| 10 | `FS.GA.FUND.CALENDAR.RESERVED9` | `FsGaFundCalendar_Reserved9` | TField |  |  |
| 11 | `FS.GA.FUND.CALENDAR.RESERVED8` | `FsGaFundCalendar_Reserved8` | TField |  |  |
| 12 | `FS.GA.FUND.CALENDAR.RESERVED7` | `FsGaFundCalendar_Reserved7` | TField |  |  |
| 13 | `FS.GA.FUND.CALENDAR.RESERVED6` | `FsGaFundCalendar_Reserved6` | TField |  |  |
| 14 | `FS.GA.FUND.CALENDAR.RESERVED5` | `FsGaFundCalendar_Reserved5` | TField |  |  |
| 15 | `FS.GA.FUND.CALENDAR.RESERVED4` | `FsGaFundCalendar_Reserved4` | TField |  |  |
| 16 | `FS.GA.FUND.CALENDAR.RESERVED3` | `FsGaFundCalendar_Reserved3` | TField |  |  |
| 17 | `FS.GA.FUND.CALENDAR.RESERVED2` | `FsGaFundCalendar_Reserved2` | TField |  |  |
| 18 | `FS.GA.FUND.CALENDAR.RESERVED1` | `FsGaFundCalendar_Reserved1` | TField |  |  |
| 19 | `FS.GA.FUND.CALENDAR.LOCAL.REF` | `FsGaFundCalendar_LocalRef` |  |  |  |
| 20 | `FS.GA.FUND.CALENDAR.OVERRIDE` | `FsGaFundCalendar_Override` |  |  |  |
| 21 | `FS.GA.FUND.CALENDAR.RECORD.STATUS` | `FsGaFundCalendar_RecordStatus` | String |  |  |
| 22 | `FS.GA.FUND.CALENDAR.CURR.NO` | `FsGaFundCalendar_CurrNo` | String |  |  |
| 23 | `FS.GA.FUND.CALENDAR.INPUTTER` | `FsGaFundCalendar_Inputter` |  |  |  |
| 24 | `FS.GA.FUND.CALENDAR.DATE.TIME` | `FsGaFundCalendar_DateTime` |  |  |  |
| 25 | `FS.GA.FUND.CALENDAR.AUTHORISER` | `FsGaFundCalendar_Authoriser` | String |  |  |
| 26 | `FS.GA.FUND.CALENDAR.CO.CODE` | `FsGaFundCalendar_CoCode` | String |  |  |
| 27 | `FS.GA.FUND.CALENDAR.DEPT.CODE` | `FsGaFundCalendar_DeptCode` | String |  |  |
| 28 | `FS.GA.FUND.CALENDAR.AUDITOR.CODE` | `FsGaFundCalendar_AuditorCode` | String |  |  |
| 29 | `FS.GA.FUND.CALENDAR.AUDIT.DATE.TIME` | `FsGaFundCalendar_AuditDateTime` | String |  |  |
