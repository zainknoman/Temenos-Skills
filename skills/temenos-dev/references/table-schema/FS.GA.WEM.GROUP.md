# FS.GA.WEM.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.GROUP` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.GROUP.PARENT.REF.ID` | `FsGaWemGroup_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.GROUP.ORA.ROWID` | `FsGaWemGroup_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.GROUP.GROUP.ID` | `FsGaWemGroup_GroupId` | TField |  | ID of the group Multifonds DB Column is GROUP_ID. |
| 4 | `FS.GA.WEM.GROUP.NAME` | `FsGaWemGroup_Name` | TField |  | Name Multifonds DB Column is NAME. |
| 5 | `FS.GA.WEM.GROUP.DESCRIPTION` | `FsGaWemGroup_Description` | TField |  | Field Description Multifonds DB Column is DESCRIPTION. |
| 6 | `FS.GA.WEM.GROUP.RESERVED10` | `FsGaWemGroup_Reserved10` | TField |  |  |
| 7 | `FS.GA.WEM.GROUP.RESERVED9` | `FsGaWemGroup_Reserved9` | TField |  |  |
| 8 | `FS.GA.WEM.GROUP.RESERVED8` | `FsGaWemGroup_Reserved8` | TField |  |  |
| 9 | `FS.GA.WEM.GROUP.RESERVED7` | `FsGaWemGroup_Reserved7` | TField |  |  |
| 10 | `FS.GA.WEM.GROUP.RESERVED6` | `FsGaWemGroup_Reserved6` | TField |  |  |
| 11 | `FS.GA.WEM.GROUP.RESERVED5` | `FsGaWemGroup_Reserved5` | TField |  |  |
| 12 | `FS.GA.WEM.GROUP.RESERVED4` | `FsGaWemGroup_Reserved4` | TField |  |  |
| 13 | `FS.GA.WEM.GROUP.RESERVED3` | `FsGaWemGroup_Reserved3` | TField |  |  |
| 14 | `FS.GA.WEM.GROUP.RESERVED2` | `FsGaWemGroup_Reserved2` | TField |  |  |
| 15 | `FS.GA.WEM.GROUP.RESERVED1` | `FsGaWemGroup_Reserved1` | TField |  |  |
| 16 | `FS.GA.WEM.GROUP.LOCAL.REF` | `FsGaWemGroup_LocalRef` |  |  |  |
| 17 | `FS.GA.WEM.GROUP.OVERRIDE` | `FsGaWemGroup_Override` |  |  |  |
| 18 | `FS.GA.WEM.GROUP.RECORD.STATUS` | `FsGaWemGroup_RecordStatus` | String |  |  |
| 19 | `FS.GA.WEM.GROUP.CURR.NO` | `FsGaWemGroup_CurrNo` | String |  |  |
| 20 | `FS.GA.WEM.GROUP.INPUTTER` | `FsGaWemGroup_Inputter` |  |  |  |
| 21 | `FS.GA.WEM.GROUP.DATE.TIME` | `FsGaWemGroup_DateTime` |  |  |  |
| 22 | `FS.GA.WEM.GROUP.AUTHORISER` | `FsGaWemGroup_Authoriser` | String |  |  |
| 23 | `FS.GA.WEM.GROUP.CO.CODE` | `FsGaWemGroup_CoCode` | String |  |  |
| 24 | `FS.GA.WEM.GROUP.DEPT.CODE` | `FsGaWemGroup_DeptCode` | String |  |  |
| 25 | `FS.GA.WEM.GROUP.AUDITOR.CODE` | `FsGaWemGroup_AuditorCode` | String |  |  |
| 26 | `FS.GA.WEM.GROUP.AUDIT.DATE.TIME` | `FsGaWemGroup_AuditDateTime` | String |  |  |
