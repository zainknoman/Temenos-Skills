# FS.GI.FUND.CALENDAR.GENR.PROCESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.CALENDAR.GENR.PROCESS` in `FS_FundStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.PARENT.REF.ID` | `FsGiFundCalendarGenrProcess_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.ORA.ROWID` | `FsGiFundCalendarGenrProcess_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.FUND.ID` | `FsGiFundCalendarGenrProcess_FundId` | TField |  | Master Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.FROM.DATE` | `FsGiFundCalendarGenrProcess_FromDate` | TField |  | From date for generate calendar process. Multifonds DB Column is DATE_FROM. |
| 5 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.TO.DATE` | `FsGiFundCalendarGenrProcess_ToDate` | TField |  | To date for generate calendar process. Multifonds DB Column is DATE_TO. |
| 6 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RESERVED10` | `FsGiFundCalendarGenrProcess_Reserved10` | TField |  |  |
| 7 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RESERVED9` | `FsGiFundCalendarGenrProcess_Reserved9` | TField |  |  |
| 8 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RESERVED8` | `FsGiFundCalendarGenrProcess_Reserved8` | TField |  |  |
| 9 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RESERVED7` | `FsGiFundCalendarGenrProcess_Reserved7` | TField |  |  |
| 10 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RESERVED6` | `FsGiFundCalendarGenrProcess_Reserved6` | TField |  |  |
| 11 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RESERVED5` | `FsGiFundCalendarGenrProcess_Reserved5` | TField |  |  |
| 12 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RESERVED4` | `FsGiFundCalendarGenrProcess_Reserved4` | TField |  |  |
| 13 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RESERVED3` | `FsGiFundCalendarGenrProcess_Reserved3` | TField |  |  |
| 14 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RESERVED2` | `FsGiFundCalendarGenrProcess_Reserved2` | TField |  |  |
| 15 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RESERVED1` | `FsGiFundCalendarGenrProcess_Reserved1` | TField |  |  |
| 16 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.LOCAL.REF` | `FsGiFundCalendarGenrProcess_LocalRef` |  |  |  |
| 17 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.OVERRIDE` | `FsGiFundCalendarGenrProcess_Override` |  |  |  |
| 18 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.RECORD.STATUS` | `FsGiFundCalendarGenrProcess_RecordStatus` | String |  |  |
| 19 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.CURR.NO` | `FsGiFundCalendarGenrProcess_CurrNo` | String |  |  |
| 20 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.INPUTTER` | `FsGiFundCalendarGenrProcess_Inputter` |  |  |  |
| 21 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.DATE.TIME` | `FsGiFundCalendarGenrProcess_DateTime` |  |  |  |
| 22 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.AUTHORISER` | `FsGiFundCalendarGenrProcess_Authoriser` | String |  |  |
| 23 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.CO.CODE` | `FsGiFundCalendarGenrProcess_CoCode` | String |  |  |
| 24 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.DEPT.CODE` | `FsGiFundCalendarGenrProcess_DeptCode` | String |  |  |
| 25 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.AUDITOR.CODE` | `FsGiFundCalendarGenrProcess_AuditorCode` | String |  |  |
| 26 | `FS.GI.FUND.CALENDAR.GENR.PROCESS.AUDIT.DATE.TIME` | `FsGiFundCalendarGenrProcess_AuditDateTime` | String |  |  |
