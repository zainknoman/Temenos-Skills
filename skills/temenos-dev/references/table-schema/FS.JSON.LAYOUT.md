# FS.JSON.LAYOUT — Table Schema

> Source: `INSERTS/I_F.FS.JSON.LAYOUT` in `FS_ApplicationFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.JL.JSON.LAYOUT` | `FsJsonLayout_JsonLayout` |  |  |  |
| 2 | `FS.JL.RESERVED5` | `FsJsonLayout_Reserved5` | TField |  |  |
| 3 | `FS.JL.RESERVED4` | `FsJsonLayout_Reserved4` | TField |  |  |
| 4 | `FS.JL.RESERVED3` | `FsJsonLayout_Reserved3` | TField |  |  |
| 5 | `FS.JL.RESERVED2` | `FsJsonLayout_Reserved2` | TField |  |  |
| 6 | `FS.JL.RESERVED1` | `FsJsonLayout_Reserved1` | TField |  |  |
| 7 | `FS.JL.LOCAL.REF` | `FsJsonLayout_LocalRef` |  |  |  |
| 8 | `FS.JL.OVERRIDE` | `FsJsonLayout_Override` |  |  |  |
| 9 | `FS.JL.RECORD.STATUS` | `FsJsonLayout_RecordStatus` | String |  |  |
| 10 | `FS.JL.CURR.NO` | `FsJsonLayout_CurrNo` | String |  |  |
| 11 | `FS.JL.INPUTTER` | `FsJsonLayout_Inputter` |  |  |  |
| 12 | `FS.JL.DATE.TIME` | `FsJsonLayout_DateTime` |  |  |  |
| 13 | `FS.JL.AUTHORISER` | `FsJsonLayout_Authoriser` | String |  |  |
| 14 | `FS.JL.CO.CODE` | `FsJsonLayout_CoCode` | String |  |  |
| 15 | `FS.JL.DEPT.CODE` | `FsJsonLayout_DeptCode` | String |  |  |
| 16 | `FS.JL.AUDITOR.CODE` | `FsJsonLayout_AuditorCode` | String |  |  |
| 17 | `FS.JL.AUDIT.DATE.TIME` | `FsJsonLayout_AuditDateTime` | String |  |  |
