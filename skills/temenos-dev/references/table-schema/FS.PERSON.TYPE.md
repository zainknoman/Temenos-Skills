# FS.PERSON.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.PERSON.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.PERSON.TYPE.DESCRIPTION` | `FsPersonType_Description` |  |  |  |
| 2 | `FS.PERSON.TYPE.FILTER.KEY` | `FsPersonType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.PERSON.TYPE.RECORD.ID` | `FsPersonType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.PERSON.TYPE.RESERVED10` | `FsPersonType_Reserved10` | TField |  |  |
| 5 | `FS.PERSON.TYPE.RESERVED9` | `FsPersonType_Reserved9` | TField |  |  |
| 6 | `FS.PERSON.TYPE.RESERVED8` | `FsPersonType_Reserved8` | TField |  |  |
| 7 | `FS.PERSON.TYPE.RESERVED7` | `FsPersonType_Reserved7` | TField |  |  |
| 8 | `FS.PERSON.TYPE.RESERVED6` | `FsPersonType_Reserved6` | TField |  |  |
| 9 | `FS.PERSON.TYPE.RESERVED5` | `FsPersonType_Reserved5` | TField |  |  |
| 10 | `FS.PERSON.TYPE.RESERVED4` | `FsPersonType_Reserved4` | TField |  |  |
| 11 | `FS.PERSON.TYPE.RESERVED3` | `FsPersonType_Reserved3` | TField |  |  |
| 12 | `FS.PERSON.TYPE.RESERVED2` | `FsPersonType_Reserved2` | TField |  |  |
| 13 | `FS.PERSON.TYPE.RESERVED1` | `FsPersonType_Reserved1` | TField |  |  |
| 14 | `FS.PERSON.TYPE.LOCAL.REF` | `FsPersonType_LocalRef` |  |  |  |
| 15 | `FS.PERSON.TYPE.OVERRIDE` | `FsPersonType_Override` |  |  |  |
| 16 | `FS.PERSON.TYPE.RECORD.STATUS` | `FsPersonType_RecordStatus` | String |  |  |
| 17 | `FS.PERSON.TYPE.CURR.NO` | `FsPersonType_CurrNo` | String |  |  |
| 18 | `FS.PERSON.TYPE.INPUTTER` | `FsPersonType_Inputter` |  |  |  |
| 19 | `FS.PERSON.TYPE.DATE.TIME` | `FsPersonType_DateTime` |  |  |  |
| 20 | `FS.PERSON.TYPE.AUTHORISER` | `FsPersonType_Authoriser` | String |  |  |
| 21 | `FS.PERSON.TYPE.CO.CODE` | `FsPersonType_CoCode` | String |  |  |
| 22 | `FS.PERSON.TYPE.DEPT.CODE` | `FsPersonType_DeptCode` | String |  |  |
| 23 | `FS.PERSON.TYPE.AUDITOR.CODE` | `FsPersonType_AuditorCode` | String |  |  |
| 24 | `FS.PERSON.TYPE.AUDIT.DATE.TIME` | `FsPersonType_AuditDateTime` | String |  |  |
