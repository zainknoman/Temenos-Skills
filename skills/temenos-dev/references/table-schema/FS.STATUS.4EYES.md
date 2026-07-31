# FS.STATUS.4EYES — Table Schema

> Source: `INSERTS/I_F.FS.STATUS.4EYES` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.STATUS.4EYES.DESCRIPTION` | `FsStatus4eyes_Description` |  |  |  |
| 2 | `FS.STATUS.4EYES.FILTER.KEY` | `FsStatus4eyes_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.STATUS.4EYES.RECORD.ID` | `FsStatus4eyes_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.STATUS.4EYES.RESERVED10` | `FsStatus4eyes_Reserved10` | TField |  |  |
| 5 | `FS.STATUS.4EYES.RESERVED9` | `FsStatus4eyes_Reserved9` | TField |  |  |
| 6 | `FS.STATUS.4EYES.RESERVED8` | `FsStatus4eyes_Reserved8` | TField |  |  |
| 7 | `FS.STATUS.4EYES.RESERVED7` | `FsStatus4eyes_Reserved7` | TField |  |  |
| 8 | `FS.STATUS.4EYES.RESERVED6` | `FsStatus4eyes_Reserved6` | TField |  |  |
| 9 | `FS.STATUS.4EYES.RESERVED5` | `FsStatus4eyes_Reserved5` | TField |  |  |
| 10 | `FS.STATUS.4EYES.RESERVED4` | `FsStatus4eyes_Reserved4` | TField |  |  |
| 11 | `FS.STATUS.4EYES.RESERVED3` | `FsStatus4eyes_Reserved3` | TField |  |  |
| 12 | `FS.STATUS.4EYES.RESERVED2` | `FsStatus4eyes_Reserved2` | TField |  |  |
| 13 | `FS.STATUS.4EYES.RESERVED1` | `FsStatus4eyes_Reserved1` | TField |  |  |
| 14 | `FS.STATUS.4EYES.LOCAL.REF` | `FsStatus4eyes_LocalRef` |  |  |  |
| 15 | `FS.STATUS.4EYES.OVERRIDE` | `FsStatus4eyes_Override` |  |  |  |
| 16 | `FS.STATUS.4EYES.RECORD.STATUS` | `FsStatus4eyes_RecordStatus` | String |  |  |
| 17 | `FS.STATUS.4EYES.CURR.NO` | `FsStatus4eyes_CurrNo` | String |  |  |
| 18 | `FS.STATUS.4EYES.INPUTTER` | `FsStatus4eyes_Inputter` |  |  |  |
| 19 | `FS.STATUS.4EYES.DATE.TIME` | `FsStatus4eyes_DateTime` |  |  |  |
| 20 | `FS.STATUS.4EYES.AUTHORISER` | `FsStatus4eyes_Authoriser` | String |  |  |
| 21 | `FS.STATUS.4EYES.CO.CODE` | `FsStatus4eyes_CoCode` | String |  |  |
| 22 | `FS.STATUS.4EYES.DEPT.CODE` | `FsStatus4eyes_DeptCode` | String |  |  |
| 23 | `FS.STATUS.4EYES.AUDITOR.CODE` | `FsStatus4eyes_AuditorCode` | String |  |  |
| 24 | `FS.STATUS.4EYES.AUDIT.DATE.TIME` | `FsStatus4eyes_AuditDateTime` | String |  |  |
