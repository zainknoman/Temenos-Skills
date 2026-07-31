# FS.GA.NAV.PERIOD — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.PERIOD` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.PERIOD.PARENT.REF.ID` | `FsGaNavPeriod_ParentRefId` |  |  |  |
| 2 | `FS.GA.NAV.PERIOD.ORA.ROWID` | `FsGaNavPeriod_OraRowid` |  |  |  |
| 3 | `FS.GA.NAV.PERIOD.NAV.GROUP.CODE` | `FsGaNavPeriod_NavGroupCode` |  |  |  |
| 4 | `FS.GA.NAV.PERIOD.FROM.DATE` | `FsGaNavPeriod_FromDate` |  |  |  |
| 5 | `FS.GA.NAV.PERIOD.DATE.TO` | `FsGaNavPeriod_DateTo` |  |  |  |
| 6 | `FS.GA.NAV.PERIOD.RESERVED10` | `FsGaNavPeriod_Reserved10` |  |  |  |
| 7 | `FS.GA.NAV.PERIOD.RESERVED9` | `FsGaNavPeriod_Reserved9` |  |  |  |
| 8 | `FS.GA.NAV.PERIOD.RESERVED8` | `FsGaNavPeriod_Reserved8` |  |  |  |
| 9 | `FS.GA.NAV.PERIOD.RESERVED7` | `FsGaNavPeriod_Reserved7` |  |  |  |
| 10 | `FS.GA.NAV.PERIOD.RESERVED6` | `FsGaNavPeriod_Reserved6` |  |  |  |
| 11 | `FS.GA.NAV.PERIOD.RESERVED5` | `FsGaNavPeriod_Reserved5` |  |  |  |
| 12 | `FS.GA.NAV.PERIOD.RESERVED4` | `FsGaNavPeriod_Reserved4` |  |  |  |
| 13 | `FS.GA.NAV.PERIOD.RESERVED3` | `FsGaNavPeriod_Reserved3` |  |  |  |
| 14 | `FS.GA.NAV.PERIOD.RESERVED2` | `FsGaNavPeriod_Reserved2` |  |  |  |
| 15 | `FS.GA.NAV.PERIOD.RESERVED1` | `FsGaNavPeriod_Reserved1` |  |  |  |
| 16 | `FS.GA.NAV.PERIOD.LOCAL.REF` | `FsGaNavPeriod_LocalRef` |  |  |  |
| 17 | `FS.GA.NAV.PERIOD.OVERRIDE` | `FsGaNavPeriod_Override` |  |  |  |
| 18 | `FS.GA.NAV.PERIOD.RECORD.STATUS` | `FsGaNavPeriod_RecordStatus` |  |  |  |
| 19 | `FS.GA.NAV.PERIOD.CURR.NO` | `FsGaNavPeriod_CurrNo` |  |  |  |
| 20 | `FS.GA.NAV.PERIOD.INPUTTER` | `FsGaNavPeriod_Inputter` |  |  |  |
| 21 | `FS.GA.NAV.PERIOD.DATE.TIME` | `FsGaNavPeriod_DateTime` |  |  |  |
| 22 | `FS.GA.NAV.PERIOD.AUTHORISER` | `FsGaNavPeriod_Authoriser` |  |  |  |
| 23 | `FS.GA.NAV.PERIOD.CO.CODE` | `FsGaNavPeriod_CoCode` |  |  |  |
| 24 | `FS.GA.NAV.PERIOD.DEPT.CODE` | `FsGaNavPeriod_DeptCode` |  |  |  |
| 25 | `FS.GA.NAV.PERIOD.AUDITOR.CODE` | `FsGaNavPeriod_AuditorCode` |  |  |  |
| 26 | `FS.GA.NAV.PERIOD.AUDIT.DATE.TIME` | `FsGaNavPeriod_AuditDateTime` |  |  |  |
