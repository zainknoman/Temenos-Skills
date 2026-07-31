# FS.INSTRUMENT.CODE — Table Schema

> Source: `INSERTS/I_F.FS.INSTRUMENT.CODE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.INSTRUMENT.CODE.DESCRIPTION` | `FsInstrumentCode_Description` |  |  |  |
| 2 | `FS.INSTRUMENT.CODE.FILTER.KEY` | `FsInstrumentCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.INSTRUMENT.CODE.RECORD.ID` | `FsInstrumentCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.INSTRUMENT.CODE.RESERVED10` | `FsInstrumentCode_Reserved10` | TField |  |  |
| 5 | `FS.INSTRUMENT.CODE.RESERVED9` | `FsInstrumentCode_Reserved9` | TField |  |  |
| 6 | `FS.INSTRUMENT.CODE.RESERVED8` | `FsInstrumentCode_Reserved8` | TField |  |  |
| 7 | `FS.INSTRUMENT.CODE.RESERVED7` | `FsInstrumentCode_Reserved7` | TField |  |  |
| 8 | `FS.INSTRUMENT.CODE.RESERVED6` | `FsInstrumentCode_Reserved6` | TField |  |  |
| 9 | `FS.INSTRUMENT.CODE.RESERVED5` | `FsInstrumentCode_Reserved5` | TField |  |  |
| 10 | `FS.INSTRUMENT.CODE.RESERVED4` | `FsInstrumentCode_Reserved4` | TField |  |  |
| 11 | `FS.INSTRUMENT.CODE.RESERVED3` | `FsInstrumentCode_Reserved3` | TField |  |  |
| 12 | `FS.INSTRUMENT.CODE.RESERVED2` | `FsInstrumentCode_Reserved2` | TField |  |  |
| 13 | `FS.INSTRUMENT.CODE.RESERVED1` | `FsInstrumentCode_Reserved1` | TField |  |  |
| 14 | `FS.INSTRUMENT.CODE.LOCAL.REF` | `FsInstrumentCode_LocalRef` |  |  |  |
| 15 | `FS.INSTRUMENT.CODE.OVERRIDE` | `FsInstrumentCode_Override` |  |  |  |
| 16 | `FS.INSTRUMENT.CODE.RECORD.STATUS` | `FsInstrumentCode_RecordStatus` | String |  |  |
| 17 | `FS.INSTRUMENT.CODE.CURR.NO` | `FsInstrumentCode_CurrNo` | String |  |  |
| 18 | `FS.INSTRUMENT.CODE.INPUTTER` | `FsInstrumentCode_Inputter` |  |  |  |
| 19 | `FS.INSTRUMENT.CODE.DATE.TIME` | `FsInstrumentCode_DateTime` |  |  |  |
| 20 | `FS.INSTRUMENT.CODE.AUTHORISER` | `FsInstrumentCode_Authoriser` | String |  |  |
| 21 | `FS.INSTRUMENT.CODE.CO.CODE` | `FsInstrumentCode_CoCode` | String |  |  |
| 22 | `FS.INSTRUMENT.CODE.DEPT.CODE` | `FsInstrumentCode_DeptCode` | String |  |  |
| 23 | `FS.INSTRUMENT.CODE.AUDITOR.CODE` | `FsInstrumentCode_AuditorCode` | String |  |  |
| 24 | `FS.INSTRUMENT.CODE.AUDIT.DATE.TIME` | `FsInstrumentCode_AuditDateTime` | String |  |  |
