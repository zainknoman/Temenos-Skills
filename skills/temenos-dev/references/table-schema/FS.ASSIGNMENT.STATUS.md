# FS.ASSIGNMENT.STATUS — Table Schema

> Source: `INSERTS/I_F.FS.ASSIGNMENT.STATUS` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ASSIGNMENT.STATUS.DESCRIPTION` | `FsAssignmentStatus_Description` |  |  |  |
| 2 | `FS.ASSIGNMENT.STATUS.FILTER.KEY` | `FsAssignmentStatus_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ASSIGNMENT.STATUS.RECORD.ID` | `FsAssignmentStatus_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ASSIGNMENT.STATUS.RESERVED10` | `FsAssignmentStatus_Reserved10` | TField |  |  |
| 5 | `FS.ASSIGNMENT.STATUS.RESERVED9` | `FsAssignmentStatus_Reserved9` | TField |  |  |
| 6 | `FS.ASSIGNMENT.STATUS.RESERVED8` | `FsAssignmentStatus_Reserved8` | TField |  |  |
| 7 | `FS.ASSIGNMENT.STATUS.RESERVED7` | `FsAssignmentStatus_Reserved7` | TField |  |  |
| 8 | `FS.ASSIGNMENT.STATUS.RESERVED6` | `FsAssignmentStatus_Reserved6` | TField |  |  |
| 9 | `FS.ASSIGNMENT.STATUS.RESERVED5` | `FsAssignmentStatus_Reserved5` | TField |  |  |
| 10 | `FS.ASSIGNMENT.STATUS.RESERVED4` | `FsAssignmentStatus_Reserved4` | TField |  |  |
| 11 | `FS.ASSIGNMENT.STATUS.RESERVED3` | `FsAssignmentStatus_Reserved3` | TField |  |  |
| 12 | `FS.ASSIGNMENT.STATUS.RESERVED2` | `FsAssignmentStatus_Reserved2` | TField |  |  |
| 13 | `FS.ASSIGNMENT.STATUS.RESERVED1` | `FsAssignmentStatus_Reserved1` | TField |  |  |
| 14 | `FS.ASSIGNMENT.STATUS.LOCAL.REF` | `FsAssignmentStatus_LocalRef` |  |  |  |
| 15 | `FS.ASSIGNMENT.STATUS.OVERRIDE` | `FsAssignmentStatus_Override` |  |  |  |
| 16 | `FS.ASSIGNMENT.STATUS.RECORD.STATUS` | `FsAssignmentStatus_RecordStatus` | String |  |  |
| 17 | `FS.ASSIGNMENT.STATUS.CURR.NO` | `FsAssignmentStatus_CurrNo` | String |  |  |
| 18 | `FS.ASSIGNMENT.STATUS.INPUTTER` | `FsAssignmentStatus_Inputter` |  |  |  |
| 19 | `FS.ASSIGNMENT.STATUS.DATE.TIME` | `FsAssignmentStatus_DateTime` |  |  |  |
| 20 | `FS.ASSIGNMENT.STATUS.AUTHORISER` | `FsAssignmentStatus_Authoriser` | String |  |  |
| 21 | `FS.ASSIGNMENT.STATUS.CO.CODE` | `FsAssignmentStatus_CoCode` | String |  |  |
| 22 | `FS.ASSIGNMENT.STATUS.DEPT.CODE` | `FsAssignmentStatus_DeptCode` | String |  |  |
| 23 | `FS.ASSIGNMENT.STATUS.AUDITOR.CODE` | `FsAssignmentStatus_AuditorCode` | String |  |  |
| 24 | `FS.ASSIGNMENT.STATUS.AUDIT.DATE.TIME` | `FsAssignmentStatus_AuditDateTime` | String |  |  |
