# FS.GI.FUND.CALENDAR.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.CALENDAR.EXCEPTION` in `FS_FundCalendar.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.CALENDAR.EXCEPTION.PARENT.REF.ID` | `FsGiFundCalendarException_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.CALENDAR.EXCEPTION.ORA.ROWID` | `FsGiFundCalendarException_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.CALENDAR.EXCEPTION.FUND.ID` | `FsGiFundCalendarException_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.CALENDAR.EXCEPTION.OPERATION.CODE` | `FsGiFundCalendarException_OperationCode` | TField |  | Operation code for which fund calendar exception in scope. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.FUND.CALENDAR.EXCEPTION.SHARE.CLASS.CODE` | `FsGiFundCalendarException_ShareClassCode` | TField |  | Fund share class. Multifonds DB Column is TPART. |
| 6 | `FS.GI.FUND.CALENDAR.EXCEPTION.RECEPTION.DATE.TIME` | `FsGiFundCalendarException_ReceptionDateTime` |  |  |  |
| 7 | `FS.GI.FUND.CALENDAR.EXCEPTION.TRADE.DATE` | `FsGiFundCalendarException_TradeDate` | TField |  | Trade date of the transaction. Multifonds DB Column is DOPER. |
| 8 | `FS.GI.FUND.CALENDAR.EXCEPTION.SOS.CLASS.CODE` | `FsGiFundCalendarException_SosClassCode` | TField |  | Series share class. Multifonds DB Column is TPART_SOS. |
| 9 | `FS.GI.FUND.CALENDAR.EXCEPTION.NEW.ISSUE.FLAG` | `FsGiFundCalendarException_NewIssueFlag` | TField |  | New issue eligible flag. Multifonds DB Column is FLG_NEW_ISSUE. |
| 10 | `FS.GI.FUND.CALENDAR.EXCEPTION.SOS.EXCEPT.FLAG` | `FsGiFundCalendarException_SosExceptFlag` | TField |  | Series of shares exception flag. Multifonds DB Column is FLG_SOS_EXCEPT. |
| 11 | `FS.GI.FUND.CALENDAR.EXCEPTION.SERIES.NAME` | `FsGiFundCalendarException_SeriesName` | TField |  | Series name. Multifonds DB Column is SERIES_NAME. |
| 12 | `FS.GI.FUND.CALENDAR.EXCEPTION.SOS.INCREMENT.ID` | `FsGiFundCalendarException_SosIncrementId` | TField |  | SOS incremented ID. Multifonds DB Column is SOS_INCREMENT_ID. |
| 13 | `FS.GI.FUND.CALENDAR.EXCEPTION.TEMPLATE.ID` | `FsGiFundCalendarException_TemplateId` | TField |  | Template ID. Multifonds DB Column is TEMPLATE_ID. |
| 14 | `FS.GI.FUND.CALENDAR.EXCEPTION.SECURITY.ID` | `FsGiFundCalendarException_SecurityId` | TField |  | Security for which fund exception applies. Multifonds DB Column is NOVAL. |
| 15 | `FS.GI.FUND.CALENDAR.EXCEPTION.EXCEPTIONAL.SIDE.POCKET.FLAG` | `FsGiFundCalendarException_ExceptionalSidePocketFlag` | TField |  | Exceptional side pocketed series flag. Multifonds DB Column is FLG_SERIES_SP. |
| 16 | `FS.GI.FUND.CALENDAR.EXCEPTION.EXCEPTIONAL.ORIGINAL.SERIES` | `FsGiFundCalendarException_ExceptionalOriginalSeries` | TField |  | Exception original series for side pocketed shares. Multifonds DB Column is ORIGINAL_SERIES_SP. |
| 17 | `FS.GI.FUND.CALENDAR.EXCEPTION.EXCEPTION.MERGE.FLAG` | `FsGiFundCalendarException_ExceptionMergeFlag` | TField |  | Exception merge flag. Multifonds DB Column is FLG_MERGE. |
| 18 | `FS.GI.FUND.CALENDAR.EXCEPTION.RESERVED10` | `FsGiFundCalendarException_Reserved10` | TField |  |  |
| 19 | `FS.GI.FUND.CALENDAR.EXCEPTION.RESERVED9` | `FsGiFundCalendarException_Reserved9` | TField |  |  |
| 20 | `FS.GI.FUND.CALENDAR.EXCEPTION.RESERVED8` | `FsGiFundCalendarException_Reserved8` | TField |  |  |
| 21 | `FS.GI.FUND.CALENDAR.EXCEPTION.RESERVED7` | `FsGiFundCalendarException_Reserved7` | TField |  |  |
| 22 | `FS.GI.FUND.CALENDAR.EXCEPTION.RESERVED6` | `FsGiFundCalendarException_Reserved6` | TField |  |  |
| 23 | `FS.GI.FUND.CALENDAR.EXCEPTION.RESERVED5` | `FsGiFundCalendarException_Reserved5` | TField |  |  |
| 24 | `FS.GI.FUND.CALENDAR.EXCEPTION.RESERVED4` | `FsGiFundCalendarException_Reserved4` | TField |  |  |
| 25 | `FS.GI.FUND.CALENDAR.EXCEPTION.RESERVED3` | `FsGiFundCalendarException_Reserved3` | TField |  |  |
| 26 | `FS.GI.FUND.CALENDAR.EXCEPTION.RESERVED2` | `FsGiFundCalendarException_Reserved2` | TField |  |  |
| 27 | `FS.GI.FUND.CALENDAR.EXCEPTION.RESERVED1` | `FsGiFundCalendarException_Reserved1` | TField |  |  |
| 28 | `FS.GI.FUND.CALENDAR.EXCEPTION.LOCAL.REF` | `FsGiFundCalendarException_LocalRef` |  |  |  |
| 29 | `FS.GI.FUND.CALENDAR.EXCEPTION.OVERRIDE` | `FsGiFundCalendarException_Override` |  |  |  |
| 30 | `FS.GI.FUND.CALENDAR.EXCEPTION.RECORD.STATUS` | `FsGiFundCalendarException_RecordStatus` | String |  |  |
| 31 | `FS.GI.FUND.CALENDAR.EXCEPTION.CURR.NO` | `FsGiFundCalendarException_CurrNo` | String |  |  |
| 32 | `FS.GI.FUND.CALENDAR.EXCEPTION.INPUTTER` | `FsGiFundCalendarException_Inputter` |  |  |  |
| 33 | `FS.GI.FUND.CALENDAR.EXCEPTION.DATE.TIME` | `FsGiFundCalendarException_DateTime` |  |  |  |
| 34 | `FS.GI.FUND.CALENDAR.EXCEPTION.AUTHORISER` | `FsGiFundCalendarException_Authoriser` | String |  |  |
| 35 | `FS.GI.FUND.CALENDAR.EXCEPTION.CO.CODE` | `FsGiFundCalendarException_CoCode` | String |  |  |
| 36 | `FS.GI.FUND.CALENDAR.EXCEPTION.DEPT.CODE` | `FsGiFundCalendarException_DeptCode` | String |  |  |
| 37 | `FS.GI.FUND.CALENDAR.EXCEPTION.AUDITOR.CODE` | `FsGiFundCalendarException_AuditorCode` | String |  |  |
| 38 | `FS.GI.FUND.CALENDAR.EXCEPTION.AUDIT.DATE.TIME` | `FsGiFundCalendarException_AuditDateTime` | String |  |  |
