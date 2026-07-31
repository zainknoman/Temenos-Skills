# FS.GL.FLOW.ID — Table Schema

> Source: `INSERTS/I_F.FS.GL.FLOW.ID` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GL.FLOW.ID.DESCRIPTION` | `FsGlFlowId_Description` |  |  |  |
| 2 | `FS.GL.FLOW.ID.FILTER.KEY` | `FsGlFlowId_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.GL.FLOW.ID.RECORD.ID` | `FsGlFlowId_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.GL.FLOW.ID.RESERVED10` | `FsGlFlowId_Reserved10` | TField |  |  |
| 5 | `FS.GL.FLOW.ID.RESERVED9` | `FsGlFlowId_Reserved9` | TField |  |  |
| 6 | `FS.GL.FLOW.ID.RESERVED8` | `FsGlFlowId_Reserved8` | TField |  |  |
| 7 | `FS.GL.FLOW.ID.RESERVED7` | `FsGlFlowId_Reserved7` | TField |  |  |
| 8 | `FS.GL.FLOW.ID.RESERVED6` | `FsGlFlowId_Reserved6` | TField |  |  |
| 9 | `FS.GL.FLOW.ID.RESERVED5` | `FsGlFlowId_Reserved5` | TField |  |  |
| 10 | `FS.GL.FLOW.ID.RESERVED4` | `FsGlFlowId_Reserved4` | TField |  |  |
| 11 | `FS.GL.FLOW.ID.RESERVED3` | `FsGlFlowId_Reserved3` | TField |  |  |
| 12 | `FS.GL.FLOW.ID.RESERVED2` | `FsGlFlowId_Reserved2` | TField |  |  |
| 13 | `FS.GL.FLOW.ID.RESERVED1` | `FsGlFlowId_Reserved1` | TField |  |  |
| 14 | `FS.GL.FLOW.ID.LOCAL.REF` | `FsGlFlowId_LocalRef` |  |  |  |
| 15 | `FS.GL.FLOW.ID.OVERRIDE` | `FsGlFlowId_Override` |  |  |  |
| 16 | `FS.GL.FLOW.ID.RECORD.STATUS` | `FsGlFlowId_RecordStatus` | String |  |  |
| 17 | `FS.GL.FLOW.ID.CURR.NO` | `FsGlFlowId_CurrNo` | String |  |  |
| 18 | `FS.GL.FLOW.ID.INPUTTER` | `FsGlFlowId_Inputter` |  |  |  |
| 19 | `FS.GL.FLOW.ID.DATE.TIME` | `FsGlFlowId_DateTime` |  |  |  |
| 20 | `FS.GL.FLOW.ID.AUTHORISER` | `FsGlFlowId_Authoriser` | String |  |  |
| 21 | `FS.GL.FLOW.ID.CO.CODE` | `FsGlFlowId_CoCode` | String |  |  |
| 22 | `FS.GL.FLOW.ID.DEPT.CODE` | `FsGlFlowId_DeptCode` | String |  |  |
| 23 | `FS.GL.FLOW.ID.AUDITOR.CODE` | `FsGlFlowId_AuditorCode` | String |  |  |
| 24 | `FS.GL.FLOW.ID.AUDIT.DATE.TIME` | `FsGlFlowId_AuditDateTime` | String |  |  |
