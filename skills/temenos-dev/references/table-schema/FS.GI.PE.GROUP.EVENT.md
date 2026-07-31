# FS.GI.PE.GROUP.EVENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.PE.GROUP.EVENT` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.PE.GROUP.EVENT.GROUP.TYPE` | `FsGiPeGroupEvent_GroupType` |  |  |  |
| 2 | `GI.PE.GROUP.EVENT.EVENT.TYPE` | `FsGiPeGroupEvent_EventType` |  |  |  |
| 3 | `GI.PE.GROUP.EVENT.MULTI.EVENTS.FLAG` | `FsGiPeGroupEvent_MultiEventsFlag` |  |  |  |
| 4 | `GI.PE.GROUP.EVENT.RESERVED10` | `FsGiPeGroupEvent_Reserved10` |  |  |  |
| 5 | `GI.PE.GROUP.EVENT.RESERVED9` | `FsGiPeGroupEvent_Reserved9` |  |  |  |
| 6 | `GI.PE.GROUP.EVENT.RESERVED8` | `FsGiPeGroupEvent_Reserved8` |  |  |  |
| 7 | `GI.PE.GROUP.EVENT.RESERVED7` | `FsGiPeGroupEvent_Reserved7` |  |  |  |
| 8 | `GI.PE.GROUP.EVENT.RESERVED6` | `FsGiPeGroupEvent_Reserved6` |  |  |  |
| 9 | `GI.PE.GROUP.EVENT.RESERVED5` | `FsGiPeGroupEvent_Reserved5` |  |  |  |
| 10 | `GI.PE.GROUP.EVENT.RESERVED4` | `FsGiPeGroupEvent_Reserved4` |  |  |  |
| 11 | `GI.PE.GROUP.EVENT.RESERVED3` | `FsGiPeGroupEvent_Reserved3` |  |  |  |
| 12 | `GI.PE.GROUP.EVENT.RESERVED2` | `FsGiPeGroupEvent_Reserved2` |  |  |  |
| 13 | `GI.PE.GROUP.EVENT.RESERVED1` | `FsGiPeGroupEvent_Reserved1` |  |  |  |
| 14 | `GI.PE.GROUP.EVENT.LOCAL.REF` | `FsGiPeGroupEvent_LocalRef` |  |  |  |
| 15 | `GI.PE.GROUP.EVENT.OVERRIDE` | `FsGiPeGroupEvent_Override` |  |  |  |
| 16 | `GI.PE.GROUP.EVENT.RECORD.STATUS` | `FsGiPeGroupEvent_RecordStatus` |  |  |  |
| 17 | `GI.PE.GROUP.EVENT.CURR.NO` | `FsGiPeGroupEvent_CurrNo` |  |  |  |
| 18 | `GI.PE.GROUP.EVENT.INPUTTER` | `FsGiPeGroupEvent_Inputter` |  |  |  |
| 19 | `GI.PE.GROUP.EVENT.DATE.TIME` | `FsGiPeGroupEvent_DateTime` |  |  |  |
| 20 | `GI.PE.GROUP.EVENT.AUTHORISER` | `FsGiPeGroupEvent_Authoriser` |  |  |  |
| 21 | `GI.PE.GROUP.EVENT.CO.CODE` | `FsGiPeGroupEvent_CoCode` |  |  |  |
| 22 | `GI.PE.GROUP.EVENT.DEPT.CODE` | `FsGiPeGroupEvent_DeptCode` |  |  |  |
| 23 | `GI.PE.GROUP.EVENT.AUDITOR.CODE` | `FsGiPeGroupEvent_AuditorCode` |  |  |  |
| 24 | `GI.PE.GROUP.EVENT.AUDIT.DATE.TIME` | `FsGiPeGroupEvent_AuditDateTime` |  |  |  |
