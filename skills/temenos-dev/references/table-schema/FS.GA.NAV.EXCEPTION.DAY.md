# FS.GA.NAV.EXCEPTION.DAY — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.EXCEPTION.DAY` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.EXCEPTION.DAY.FUND.ID` | `FsGaNavExceptionDay_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.NAV.EXCEPTION.DAY.NAV.EXCEPTIONAL.DAYS` | `FsGaNavExceptionDay_NavExceptionalDays` | TField |  | NAV ExceptionalL Days Multifonds DB Column is EXCEP_DAY. |
| 3 | `FS.GA.NAV.EXCEPTION.DAY.RESERVED10` | `FsGaNavExceptionDay_Reserved10` | TField |  |  |
| 4 | `FS.GA.NAV.EXCEPTION.DAY.RESERVED9` | `FsGaNavExceptionDay_Reserved9` | TField |  |  |
| 5 | `FS.GA.NAV.EXCEPTION.DAY.RESERVED8` | `FsGaNavExceptionDay_Reserved8` | TField |  |  |
| 6 | `FS.GA.NAV.EXCEPTION.DAY.RESERVED7` | `FsGaNavExceptionDay_Reserved7` | TField |  |  |
| 7 | `FS.GA.NAV.EXCEPTION.DAY.RESERVED6` | `FsGaNavExceptionDay_Reserved6` | TField |  |  |
| 8 | `FS.GA.NAV.EXCEPTION.DAY.RESERVED5` | `FsGaNavExceptionDay_Reserved5` | TField |  |  |
| 9 | `FS.GA.NAV.EXCEPTION.DAY.RESERVED4` | `FsGaNavExceptionDay_Reserved4` | TField |  |  |
| 10 | `FS.GA.NAV.EXCEPTION.DAY.RESERVED3` | `FsGaNavExceptionDay_Reserved3` | TField |  |  |
| 11 | `FS.GA.NAV.EXCEPTION.DAY.RESERVED2` | `FsGaNavExceptionDay_Reserved2` | TField |  |  |
| 12 | `FS.GA.NAV.EXCEPTION.DAY.RESERVED1` | `FsGaNavExceptionDay_Reserved1` | TField |  |  |
| 13 | `FS.GA.NAV.EXCEPTION.DAY.RECORD.STATUS` | `FsGaNavExceptionDay_RecordStatus` | String |  |  |
| 14 | `FS.GA.NAV.EXCEPTION.DAY.CURR.NO` | `FsGaNavExceptionDay_CurrNo` | String |  |  |
| 15 | `FS.GA.NAV.EXCEPTION.DAY.INPUTTER` | `FsGaNavExceptionDay_Inputter` |  |  |  |
| 16 | `FS.GA.NAV.EXCEPTION.DAY.DATE.TIME` | `FsGaNavExceptionDay_DateTime` |  |  |  |
| 17 | `FS.GA.NAV.EXCEPTION.DAY.AUTHORISER` | `FsGaNavExceptionDay_Authoriser` | String |  |  |
| 18 | `FS.GA.NAV.EXCEPTION.DAY.CO.CODE` | `FsGaNavExceptionDay_CoCode` | String |  |  |
| 19 | `FS.GA.NAV.EXCEPTION.DAY.DEPT.CODE` | `FsGaNavExceptionDay_DeptCode` | String |  |  |
| 20 | `FS.GA.NAV.EXCEPTION.DAY.AUDITOR.CODE` | `FsGaNavExceptionDay_AuditorCode` | String |  |  |
| 21 | `FS.GA.NAV.EXCEPTION.DAY.AUDIT.DATE.TIME` | `FsGaNavExceptionDay_AuditDateTime` | String |  |  |
