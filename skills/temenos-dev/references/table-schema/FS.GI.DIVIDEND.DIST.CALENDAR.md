# FS.GI.DIVIDEND.DIST.CALENDAR — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIVIDEND.DIST.CALENDAR` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.DIV.DISTRIB.CALENDAR.FUND.ID` | `FsGiDividendDistCalendar_FundId` |  |  |  |
| 2 | `GI.DIV.DISTRIB.CALENDAR.RECORD.DATE` | `FsGiDividendDistCalendar_RecordDate` |  |  |  |
| 3 | `GI.DIV.DISTRIB.CALENDAR.EXECUTION.DATE` | `FsGiDividendDistCalendar_ExecutionDate` |  |  |  |
| 4 | `GI.DIV.DISTRIB.CALENDAR.TRADE.DATE` | `FsGiDividendDistCalendar_TradeDate` |  |  |  |
| 5 | `GI.DIV.DISTRIB.CALENDAR.VALUE.DATE` | `FsGiDividendDistCalendar_ValueDate` |  |  |  |
| 6 | `GI.DIV.DISTRIB.CALENDAR.DIVIDEND.FREQUENCY` | `FsGiDividendDistCalendar_DividendFrequency` |  |  |  |
| 7 | `GI.DIV.DISTRIB.CALENDAR.RESERVED10` | `FsGiDividendDistCalendar_Reserved10` |  |  |  |
| 8 | `GI.DIV.DISTRIB.CALENDAR.RESERVED9` | `FsGiDividendDistCalendar_Reserved9` |  |  |  |
| 9 | `GI.DIV.DISTRIB.CALENDAR.RESERVED8` | `FsGiDividendDistCalendar_Reserved8` |  |  |  |
| 10 | `GI.DIV.DISTRIB.CALENDAR.RESERVED7` | `FsGiDividendDistCalendar_Reserved7` |  |  |  |
| 11 | `GI.DIV.DISTRIB.CALENDAR.RESERVED6` | `FsGiDividendDistCalendar_Reserved6` |  |  |  |
| 12 | `GI.DIV.DISTRIB.CALENDAR.RESERVED5` | `FsGiDividendDistCalendar_Reserved5` |  |  |  |
| 13 | `GI.DIV.DISTRIB.CALENDAR.RESERVED4` | `FsGiDividendDistCalendar_Reserved4` |  |  |  |
| 14 | `GI.DIV.DISTRIB.CALENDAR.RESERVED3` | `FsGiDividendDistCalendar_Reserved3` |  |  |  |
| 15 | `GI.DIV.DISTRIB.CALENDAR.RESERVED2` | `FsGiDividendDistCalendar_Reserved2` |  |  |  |
| 16 | `GI.DIV.DISTRIB.CALENDAR.RESERVED1` | `FsGiDividendDistCalendar_Reserved1` |  |  |  |
| 17 | `GI.DIV.DISTRIB.CALENDAR.LOCAL.REF` | `FsGiDividendDistCalendar_LocalRef` |  |  |  |
| 18 | `GI.DIV.DISTRIB.CALENDAR.OVERRIDE` | `FsGiDividendDistCalendar_Override` |  |  |  |
| 19 | `GI.DIV.DISTRIB.CALENDAR.RECORD.STATUS` | `FsGiDividendDistCalendar_RecordStatus` |  |  |  |
| 20 | `GI.DIV.DISTRIB.CALENDAR.CURR.NO` | `FsGiDividendDistCalendar_CurrNo` |  |  |  |
| 21 | `GI.DIV.DISTRIB.CALENDAR.INPUTTER` | `FsGiDividendDistCalendar_Inputter` |  |  |  |
| 22 | `GI.DIV.DISTRIB.CALENDAR.DATE.TIME` | `FsGiDividendDistCalendar_DateTime` |  |  |  |
| 23 | `GI.DIV.DISTRIB.CALENDAR.AUTHORISER` | `FsGiDividendDistCalendar_Authoriser` |  |  |  |
| 24 | `GI.DIV.DISTRIB.CALENDAR.CO.CODE` | `FsGiDividendDistCalendar_CoCode` |  |  |  |
| 25 | `GI.DIV.DISTRIB.CALENDAR.DEPT.CODE` | `FsGiDividendDistCalendar_DeptCode` |  |  |  |
| 26 | `GI.DIV.DISTRIB.CALENDAR.AUDITOR.CODE` | `FsGiDividendDistCalendar_AuditorCode` |  |  |  |
| 27 | `GI.DIV.DISTRIB.CALENDAR.AUDIT.DATE.TIME` | `FsGiDividendDistCalendar_AuditDateTime` |  |  |  |
