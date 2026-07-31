# FS.TA.TASKNAME — Table Schema

> Source: `INSERTS/I_F.FS.TA.TASKNAME` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.TA.TASKNAME.DESCRIPTION` | `FsTaTaskname_Description` |  |  |  |
| 2 | `FS.TA.TASKNAME.FILTER.KEY` | `FsTaTaskname_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.TA.TASKNAME.RECORD.ID` | `FsTaTaskname_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.TA.TASKNAME.RESERVED10` | `FsTaTaskname_Reserved10` | TField |  |  |
| 5 | `FS.TA.TASKNAME.RESERVED9` | `FsTaTaskname_Reserved9` | TField |  |  |
| 6 | `FS.TA.TASKNAME.RESERVED8` | `FsTaTaskname_Reserved8` | TField |  |  |
| 7 | `FS.TA.TASKNAME.RESERVED7` | `FsTaTaskname_Reserved7` | TField |  |  |
| 8 | `FS.TA.TASKNAME.RESERVED6` | `FsTaTaskname_Reserved6` | TField |  |  |
| 9 | `FS.TA.TASKNAME.RESERVED5` | `FsTaTaskname_Reserved5` | TField |  |  |
| 10 | `FS.TA.TASKNAME.RESERVED4` | `FsTaTaskname_Reserved4` | TField |  |  |
| 11 | `FS.TA.TASKNAME.RESERVED3` | `FsTaTaskname_Reserved3` | TField |  |  |
| 12 | `FS.TA.TASKNAME.RESERVED2` | `FsTaTaskname_Reserved2` | TField |  |  |
| 13 | `FS.TA.TASKNAME.RESERVED1` | `FsTaTaskname_Reserved1` | TField |  |  |
| 14 | `FS.TA.TASKNAME.LOCAL.REF` | `FsTaTaskname_LocalRef` |  |  |  |
| 15 | `FS.TA.TASKNAME.OVERRIDE` | `FsTaTaskname_Override` |  |  |  |
| 16 | `FS.TA.TASKNAME.RECORD.STATUS` | `FsTaTaskname_RecordStatus` | String |  |  |
| 17 | `FS.TA.TASKNAME.CURR.NO` | `FsTaTaskname_CurrNo` | String |  |  |
| 18 | `FS.TA.TASKNAME.INPUTTER` | `FsTaTaskname_Inputter` |  |  |  |
| 19 | `FS.TA.TASKNAME.DATE.TIME` | `FsTaTaskname_DateTime` |  |  |  |
| 20 | `FS.TA.TASKNAME.AUTHORISER` | `FsTaTaskname_Authoriser` | String |  |  |
| 21 | `FS.TA.TASKNAME.CO.CODE` | `FsTaTaskname_CoCode` | String |  |  |
| 22 | `FS.TA.TASKNAME.DEPT.CODE` | `FsTaTaskname_DeptCode` | String |  |  |
| 23 | `FS.TA.TASKNAME.AUDITOR.CODE` | `FsTaTaskname_AuditorCode` | String |  |  |
| 24 | `FS.TA.TASKNAME.AUDIT.DATE.TIME` | `FsTaTaskname_AuditDateTime` | String |  |  |
