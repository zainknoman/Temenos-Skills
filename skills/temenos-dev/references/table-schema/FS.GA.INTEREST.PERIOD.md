# FS.GA.INTEREST.PERIOD — Table Schema

> Source: `INSERTS/I_F.FS.GA.INTEREST.PERIOD` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.INTEREST.PERIOD.PARENT.REF.ID` | `FsGaInterestPeriod_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.INTEREST.PERIOD.ORA.ROWID` | `FsGaInterestPeriod_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.INTEREST.PERIOD.SEQ.NUMBER` | `FsGaInterestPeriod_SeqNumber` | TField |  | Sequence Number Multifonds DB Column is NOTXFLT. |
| 4 | `FS.GA.INTEREST.PERIOD.INTERNAL.SECURITY.ID` | `FsGaInterestPeriod_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.INTEREST.PERIOD.FROM.DT` | `FsGaInterestPeriod_FromDt` | TField |  | From Date Multifonds DB Column is DDEBUT. |
| 6 | `FS.GA.INTEREST.PERIOD.TO.DATE` | `FsGaInterestPeriod_ToDate` | TField |  | To Date Multifonds DB Column is DFIN. |
| 7 | `FS.GA.INTEREST.PERIOD.RESERVED10` | `FsGaInterestPeriod_Reserved10` | TField |  |  |
| 8 | `FS.GA.INTEREST.PERIOD.RESERVED9` | `FsGaInterestPeriod_Reserved9` | TField |  |  |
| 9 | `FS.GA.INTEREST.PERIOD.RESERVED8` | `FsGaInterestPeriod_Reserved8` | TField |  |  |
| 10 | `FS.GA.INTEREST.PERIOD.RESERVED7` | `FsGaInterestPeriod_Reserved7` | TField |  |  |
| 11 | `FS.GA.INTEREST.PERIOD.RESERVED6` | `FsGaInterestPeriod_Reserved6` | TField |  |  |
| 12 | `FS.GA.INTEREST.PERIOD.RESERVED5` | `FsGaInterestPeriod_Reserved5` | TField |  |  |
| 13 | `FS.GA.INTEREST.PERIOD.RESERVED4` | `FsGaInterestPeriod_Reserved4` | TField |  |  |
| 14 | `FS.GA.INTEREST.PERIOD.RESERVED3` | `FsGaInterestPeriod_Reserved3` | TField |  |  |
| 15 | `FS.GA.INTEREST.PERIOD.RESERVED2` | `FsGaInterestPeriod_Reserved2` | TField |  |  |
| 16 | `FS.GA.INTEREST.PERIOD.RESERVED1` | `FsGaInterestPeriod_Reserved1` | TField |  |  |
| 17 | `FS.GA.INTEREST.PERIOD.LOCAL.REF` | `FsGaInterestPeriod_LocalRef` |  |  |  |
| 18 | `FS.GA.INTEREST.PERIOD.OVERRIDE` | `FsGaInterestPeriod_Override` |  |  |  |
| 19 | `FS.GA.INTEREST.PERIOD.RECORD.STATUS` | `FsGaInterestPeriod_RecordStatus` | String |  |  |
| 20 | `FS.GA.INTEREST.PERIOD.CURR.NO` | `FsGaInterestPeriod_CurrNo` | String |  |  |
| 21 | `FS.GA.INTEREST.PERIOD.INPUTTER` | `FsGaInterestPeriod_Inputter` |  |  |  |
| 22 | `FS.GA.INTEREST.PERIOD.DATE.TIME` | `FsGaInterestPeriod_DateTime` |  |  |  |
| 23 | `FS.GA.INTEREST.PERIOD.AUTHORISER` | `FsGaInterestPeriod_Authoriser` | String |  |  |
| 24 | `FS.GA.INTEREST.PERIOD.CO.CODE` | `FsGaInterestPeriod_CoCode` | String |  |  |
| 25 | `FS.GA.INTEREST.PERIOD.DEPT.CODE` | `FsGaInterestPeriod_DeptCode` | String |  |  |
| 26 | `FS.GA.INTEREST.PERIOD.AUDITOR.CODE` | `FsGaInterestPeriod_AuditorCode` | String |  |  |
| 27 | `FS.GA.INTEREST.PERIOD.AUDIT.DATE.TIME` | `FsGaInterestPeriod_AuditDateTime` | String |  |  |
