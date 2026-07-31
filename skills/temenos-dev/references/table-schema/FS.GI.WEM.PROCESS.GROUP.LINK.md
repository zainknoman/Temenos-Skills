# FS.GI.WEM.PROCESS.GROUP.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.PROCESS.GROUP.LINK` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.WEM.PROCESS.GROUP.LINK.PROCESS.GROUP` | `FsGiWemProcessGroupLink_ProcessGroup` | TField |  | WEM process group. Multifonds DB Column is PROCESS_GROUP. |
| 2 | `GI.WEM.PROCESS.GROUP.LINK.PROCESS` | `FsGiWemProcessGroupLink_Process` | TField |  | Control process to be linked to process group. Multifonds DB Column is CPROCESS. |
| 3 | `GI.WEM.PROCESS.GROUP.LINK.RESERVED10` | `FsGiWemProcessGroupLink_Reserved10` | TField |  |  |
| 4 | `GI.WEM.PROCESS.GROUP.LINK.RESERVED9` | `FsGiWemProcessGroupLink_Reserved9` | TField |  |  |
| 5 | `GI.WEM.PROCESS.GROUP.LINK.RESERVED8` | `FsGiWemProcessGroupLink_Reserved8` | TField |  |  |
| 6 | `GI.WEM.PROCESS.GROUP.LINK.RESERVED7` | `FsGiWemProcessGroupLink_Reserved7` | TField |  |  |
| 7 | `GI.WEM.PROCESS.GROUP.LINK.RESERVED6` | `FsGiWemProcessGroupLink_Reserved6` | TField |  |  |
| 8 | `GI.WEM.PROCESS.GROUP.LINK.RESERVED5` | `FsGiWemProcessGroupLink_Reserved5` | TField |  |  |
| 9 | `GI.WEM.PROCESS.GROUP.LINK.RESERVED4` | `FsGiWemProcessGroupLink_Reserved4` | TField |  |  |
| 10 | `GI.WEM.PROCESS.GROUP.LINK.RESERVED3` | `FsGiWemProcessGroupLink_Reserved3` | TField |  |  |
| 11 | `GI.WEM.PROCESS.GROUP.LINK.RESERVED2` | `FsGiWemProcessGroupLink_Reserved2` | TField |  |  |
| 12 | `GI.WEM.PROCESS.GROUP.LINK.RESERVED1` | `FsGiWemProcessGroupLink_Reserved1` | TField |  |  |
| 13 | `GI.WEM.PROCESS.GROUP.LINK.LOCAL.REF` | `FsGiWemProcessGroupLink_LocalRef` |  |  |  |
| 14 | `GI.WEM.PROCESS.GROUP.LINK.OVERRIDE` | `FsGiWemProcessGroupLink_Override` |  |  |  |
| 15 | `GI.WEM.PROCESS.GROUP.LINK.RECORD.STATUS` | `FsGiWemProcessGroupLink_RecordStatus` | String |  |  |
| 16 | `GI.WEM.PROCESS.GROUP.LINK.CURR.NO` | `FsGiWemProcessGroupLink_CurrNo` | String |  |  |
| 17 | `GI.WEM.PROCESS.GROUP.LINK.INPUTTER` | `FsGiWemProcessGroupLink_Inputter` |  |  |  |
| 18 | `GI.WEM.PROCESS.GROUP.LINK.DATE.TIME` | `FsGiWemProcessGroupLink_DateTime` |  |  |  |
| 19 | `GI.WEM.PROCESS.GROUP.LINK.AUTHORISER` | `FsGiWemProcessGroupLink_Authoriser` | String |  |  |
| 20 | `GI.WEM.PROCESS.GROUP.LINK.CO.CODE` | `FsGiWemProcessGroupLink_CoCode` | String |  |  |
| 21 | `GI.WEM.PROCESS.GROUP.LINK.DEPT.CODE` | `FsGiWemProcessGroupLink_DeptCode` | String |  |  |
| 22 | `GI.WEM.PROCESS.GROUP.LINK.AUDITOR.CODE` | `FsGiWemProcessGroupLink_AuditorCode` | String |  |  |
| 23 | `GI.WEM.PROCESS.GROUP.LINK.AUDIT.DATE.TIME` | `FsGiWemProcessGroupLink_AuditDateTime` | String |  |  |
