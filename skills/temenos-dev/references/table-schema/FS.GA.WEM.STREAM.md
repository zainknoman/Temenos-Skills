# FS.GA.WEM.STREAM — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.STREAM` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.STREAM.PARENT.REF.ID` | `FsGaWemStream_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.STREAM.ORA.ROWID` | `FsGaWemStream_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.STREAM.STREAM.ID` | `FsGaWemStream_StreamId` | TField |  | Stream ID Multifonds DB Column is STREAM_ID. |
| 4 | `FS.GA.WEM.STREAM.NAME` | `FsGaWemStream_Name` | TField |  | Name Multifonds DB Column is NAME. |
| 5 | `FS.GA.WEM.STREAM.DESCRIPTION` | `FsGaWemStream_Description` | TField |  | Field Description Multifonds DB Column is DESCRIPTION. |
| 6 | `FS.GA.WEM.STREAM.RESERVED10` | `FsGaWemStream_Reserved10` | TField |  |  |
| 7 | `FS.GA.WEM.STREAM.RESERVED9` | `FsGaWemStream_Reserved9` | TField |  |  |
| 8 | `FS.GA.WEM.STREAM.RESERVED8` | `FsGaWemStream_Reserved8` | TField |  |  |
| 9 | `FS.GA.WEM.STREAM.RESERVED7` | `FsGaWemStream_Reserved7` | TField |  |  |
| 10 | `FS.GA.WEM.STREAM.RESERVED6` | `FsGaWemStream_Reserved6` | TField |  |  |
| 11 | `FS.GA.WEM.STREAM.RESERVED5` | `FsGaWemStream_Reserved5` | TField |  |  |
| 12 | `FS.GA.WEM.STREAM.RESERVED4` | `FsGaWemStream_Reserved4` | TField |  |  |
| 13 | `FS.GA.WEM.STREAM.RESERVED3` | `FsGaWemStream_Reserved3` | TField |  |  |
| 14 | `FS.GA.WEM.STREAM.RESERVED2` | `FsGaWemStream_Reserved2` | TField |  |  |
| 15 | `FS.GA.WEM.STREAM.RESERVED1` | `FsGaWemStream_Reserved1` | TField |  |  |
| 16 | `FS.GA.WEM.STREAM.LOCAL.REF` | `FsGaWemStream_LocalRef` |  |  |  |
| 17 | `FS.GA.WEM.STREAM.OVERRIDE` | `FsGaWemStream_Override` |  |  |  |
| 18 | `FS.GA.WEM.STREAM.RECORD.STATUS` | `FsGaWemStream_RecordStatus` | String |  |  |
| 19 | `FS.GA.WEM.STREAM.CURR.NO` | `FsGaWemStream_CurrNo` | String |  |  |
| 20 | `FS.GA.WEM.STREAM.INPUTTER` | `FsGaWemStream_Inputter` |  |  |  |
| 21 | `FS.GA.WEM.STREAM.DATE.TIME` | `FsGaWemStream_DateTime` |  |  |  |
| 22 | `FS.GA.WEM.STREAM.AUTHORISER` | `FsGaWemStream_Authoriser` | String |  |  |
| 23 | `FS.GA.WEM.STREAM.CO.CODE` | `FsGaWemStream_CoCode` | String |  |  |
| 24 | `FS.GA.WEM.STREAM.DEPT.CODE` | `FsGaWemStream_DeptCode` | String |  |  |
| 25 | `FS.GA.WEM.STREAM.AUDITOR.CODE` | `FsGaWemStream_AuditorCode` | String |  |  |
| 26 | `FS.GA.WEM.STREAM.AUDIT.DATE.TIME` | `FsGaWemStream_AuditDateTime` | String |  |  |
