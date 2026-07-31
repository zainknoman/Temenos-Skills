# FS.GI.PE.GROUP.EVENT.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GI.PE.GROUP.EVENT.DETAIL` in `FS_PrivateEquity.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.PE.GROUP.EVENT.DETAIL.GROUP.ID` | `FsGiPeGroupEventDetail_GroupId` | TField |  | Event group identification. Multifonds DB Column is GRP_ID. |
| 2 | `FS.GI.PE.GROUP.EVENT.DETAIL.EVENT.TYPE` | `FsGiPeGroupEventDetail_EventType` | TField |  | Type of the PE/RE event. Multifonds DB Column is EVENT_TYPE. |
| 3 | `FS.GI.PE.GROUP.EVENT.DETAIL.EVENTS.EXPECTED` | `FsGiPeGroupEventDetail_EventsExpected` | TField |  | Number of events of the event type that can be consolidated in the reporting. Multifonds DB Column is EVENTS_EXPECTED. |
| 4 | `FS.GI.PE.GROUP.EVENT.DETAIL.EVENTS.PROCESSED` | `FsGiPeGroupEventDetail_EventsProcessed` | TField |  | Number of events linked to the group that have been processed. Multifonds DB Column is EVENTS_PROCESSED. |
| 5 | `FS.GI.PE.GROUP.EVENT.DETAIL.EVENT.STATUS` | `FsGiPeGroupEventDetail_EventStatus` | TField |  | Status of the event placed in the bulked order or distribution screen. Multifonds DB Column is BLK_ORD_STATUS. |
| 6 | `FS.GI.PE.GROUP.EVENT.DETAIL.RESERVED10` | `FsGiPeGroupEventDetail_Reserved10` | TField |  |  |
| 7 | `FS.GI.PE.GROUP.EVENT.DETAIL.RESERVED9` | `FsGiPeGroupEventDetail_Reserved9` | TField |  |  |
| 8 | `FS.GI.PE.GROUP.EVENT.DETAIL.RESERVED8` | `FsGiPeGroupEventDetail_Reserved8` | TField |  |  |
| 9 | `FS.GI.PE.GROUP.EVENT.DETAIL.RESERVED7` | `FsGiPeGroupEventDetail_Reserved7` | TField |  |  |
| 10 | `FS.GI.PE.GROUP.EVENT.DETAIL.RESERVED6` | `FsGiPeGroupEventDetail_Reserved6` | TField |  |  |
| 11 | `FS.GI.PE.GROUP.EVENT.DETAIL.RESERVED5` | `FsGiPeGroupEventDetail_Reserved5` | TField |  |  |
| 12 | `FS.GI.PE.GROUP.EVENT.DETAIL.RESERVED4` | `FsGiPeGroupEventDetail_Reserved4` | TField |  |  |
| 13 | `FS.GI.PE.GROUP.EVENT.DETAIL.RESERVED3` | `FsGiPeGroupEventDetail_Reserved3` | TField |  |  |
| 14 | `FS.GI.PE.GROUP.EVENT.DETAIL.RESERVED2` | `FsGiPeGroupEventDetail_Reserved2` | TField |  |  |
| 15 | `FS.GI.PE.GROUP.EVENT.DETAIL.RESERVED1` | `FsGiPeGroupEventDetail_Reserved1` | TField |  |  |
| 16 | `FS.GI.PE.GROUP.EVENT.DETAIL.LOCAL.REF` | `FsGiPeGroupEventDetail_LocalRef` |  |  |  |
| 17 | `FS.GI.PE.GROUP.EVENT.DETAIL.OVERRIDE` | `FsGiPeGroupEventDetail_Override` |  |  |  |
| 18 | `FS.GI.PE.GROUP.EVENT.DETAIL.RECORD.STATUS` | `FsGiPeGroupEventDetail_RecordStatus` | String |  |  |
| 19 | `FS.GI.PE.GROUP.EVENT.DETAIL.CURR.NO` | `FsGiPeGroupEventDetail_CurrNo` | String |  |  |
| 20 | `FS.GI.PE.GROUP.EVENT.DETAIL.INPUTTER` | `FsGiPeGroupEventDetail_Inputter` |  |  |  |
| 21 | `FS.GI.PE.GROUP.EVENT.DETAIL.DATE.TIME` | `FsGiPeGroupEventDetail_DateTime` |  |  |  |
| 22 | `FS.GI.PE.GROUP.EVENT.DETAIL.AUTHORISER` | `FsGiPeGroupEventDetail_Authoriser` | String |  |  |
| 23 | `FS.GI.PE.GROUP.EVENT.DETAIL.CO.CODE` | `FsGiPeGroupEventDetail_CoCode` | String |  |  |
| 24 | `FS.GI.PE.GROUP.EVENT.DETAIL.DEPT.CODE` | `FsGiPeGroupEventDetail_DeptCode` | String |  |  |
| 25 | `FS.GI.PE.GROUP.EVENT.DETAIL.AUDITOR.CODE` | `FsGiPeGroupEventDetail_AuditorCode` | String |  |  |
| 26 | `FS.GI.PE.GROUP.EVENT.DETAIL.AUDIT.DATE.TIME` | `FsGiPeGroupEventDetail_AuditDateTime` | String |  |  |
