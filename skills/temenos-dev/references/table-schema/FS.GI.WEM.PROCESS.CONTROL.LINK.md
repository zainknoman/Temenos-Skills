# FS.GI.WEM.PROCESS.CONTROL.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.PROCESS.CONTROL.LINK` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.PROCESS.CONTROL.LINK.PROCESS` | `FsGiWemProcessControlLink_Process` | TField |  | Control process to be linked to Control ID. Multifonds DB Column is CPROCESS. |
| 2 | `FS.GI.WEM.PROCESS.CONTROL.LINK.CONTROL.ID` | `FsGiWemProcessControlLink_ControlId` | TField |  | Unique control identification number. Multifonds DB Column is TYP_CTRL_ID. |
| 3 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RESERVED10` | `FsGiWemProcessControlLink_Reserved10` | TField |  |  |
| 4 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RESERVED9` | `FsGiWemProcessControlLink_Reserved9` | TField |  |  |
| 5 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RESERVED8` | `FsGiWemProcessControlLink_Reserved8` | TField |  |  |
| 6 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RESERVED7` | `FsGiWemProcessControlLink_Reserved7` | TField |  |  |
| 7 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RESERVED6` | `FsGiWemProcessControlLink_Reserved6` | TField |  |  |
| 8 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RESERVED5` | `FsGiWemProcessControlLink_Reserved5` | TField |  |  |
| 9 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RESERVED4` | `FsGiWemProcessControlLink_Reserved4` | TField |  |  |
| 10 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RESERVED3` | `FsGiWemProcessControlLink_Reserved3` | TField |  |  |
| 11 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RESERVED2` | `FsGiWemProcessControlLink_Reserved2` | TField |  |  |
| 12 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RESERVED1` | `FsGiWemProcessControlLink_Reserved1` | TField |  |  |
| 13 | `FS.GI.WEM.PROCESS.CONTROL.LINK.LOCAL.REF` | `FsGiWemProcessControlLink_LocalRef` |  |  |  |
| 14 | `FS.GI.WEM.PROCESS.CONTROL.LINK.OVERRIDE` | `FsGiWemProcessControlLink_Override` |  |  |  |
| 15 | `FS.GI.WEM.PROCESS.CONTROL.LINK.RECORD.STATUS` | `FsGiWemProcessControlLink_RecordStatus` | String |  |  |
| 16 | `FS.GI.WEM.PROCESS.CONTROL.LINK.CURR.NO` | `FsGiWemProcessControlLink_CurrNo` | String |  |  |
| 17 | `FS.GI.WEM.PROCESS.CONTROL.LINK.INPUTTER` | `FsGiWemProcessControlLink_Inputter` |  |  |  |
| 18 | `FS.GI.WEM.PROCESS.CONTROL.LINK.DATE.TIME` | `FsGiWemProcessControlLink_DateTime` |  |  |  |
| 19 | `FS.GI.WEM.PROCESS.CONTROL.LINK.AUTHORISER` | `FsGiWemProcessControlLink_Authoriser` | String |  |  |
| 20 | `FS.GI.WEM.PROCESS.CONTROL.LINK.CO.CODE` | `FsGiWemProcessControlLink_CoCode` | String |  |  |
| 21 | `FS.GI.WEM.PROCESS.CONTROL.LINK.DEPT.CODE` | `FsGiWemProcessControlLink_DeptCode` | String |  |  |
| 22 | `FS.GI.WEM.PROCESS.CONTROL.LINK.AUDITOR.CODE` | `FsGiWemProcessControlLink_AuditorCode` | String |  |  |
| 23 | `FS.GI.WEM.PROCESS.CONTROL.LINK.AUDIT.DATE.TIME` | `FsGiWemProcessControlLink_AuditDateTime` | String |  |  |
