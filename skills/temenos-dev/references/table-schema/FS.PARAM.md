# FS.PARAM — Table Schema

> Source: `INSERTS/I_F.FS.PARAM` in `FS_ApplicationFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.PM.CONNECTION` | `FsParam_Connection` | TField | Yes | This field defines if MF db Connection is setup or Mockup connection Valid inputs are MOCKUP and MF By default Value will be MOCKUP Mandatory Input |
| 2 | `FS.PM.PRODUCT` | `FsParam_Product` |  |  |  |
| 3 | `FS.PM.RESERVED10` | `FsParam_Reserved10` | TField |  |  |
| 4 | `FS.PM.RESERVED9` | `FsParam_Reserved9` | TField |  |  |
| 5 | `FS.PM.RESERVED8` | `FsParam_Reserved8` | TField |  |  |
| 6 | `FS.PM.RESERVED7` | `FsParam_Reserved7` | TField |  |  |
| 7 | `FS.PM.RESERVED6` | `FsParam_Reserved6` | TField |  |  |
| 8 | `FS.PM.RESERVED5` | `FsParam_Reserved5` | TField |  |  |
| 9 | `FS.PM.RESERVED4` | `FsParam_Reserved4` | TField |  |  |
| 10 | `FS.PM.RESERVED3` | `FsParam_Reserved3` | TField |  |  |
| 11 | `FS.PM.RESERVED2` | `FsParam_Reserved2` | TField |  |  |
| 12 | `FS.PM.RESERVED1` | `FsParam_Reserved1` | TField |  |  |
| 13 | `FS.PM.LOCAL.REF` | `FsParam_LocalRef` |  |  |  |
| 14 | `FS.PM.OVERRIDE` | `FsParam_Override` |  |  |  |
| 15 | `FS.PM.RECORD.STATUS` | `FsParam_RecordStatus` | String |  |  |
| 16 | `FS.PM.CURR.NO` | `FsParam_CurrNo` | String |  |  |
| 17 | `FS.PM.INPUTTER` | `FsParam_Inputter` |  |  |  |
| 18 | `FS.PM.DATE.TIME` | `FsParam_DateTime` |  |  |  |
| 19 | `FS.PM.AUTHORISER` | `FsParam_Authoriser` | String |  |  |
| 20 | `FS.PM.CO.CODE` | `FsParam_CoCode` | String |  |  |
| 21 | `FS.PM.DEPT.CODE` | `FsParam_DeptCode` | String |  |  |
| 22 | `FS.PM.AUDITOR.CODE` | `FsParam_AuditorCode` | String |  |  |
| 23 | `FS.PM.AUDIT.DATE.TIME` | `FsParam_AuditDateTime` | String |  |  |
