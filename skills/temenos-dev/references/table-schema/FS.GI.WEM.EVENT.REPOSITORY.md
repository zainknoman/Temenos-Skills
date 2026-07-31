# FS.GI.WEM.EVENT.REPOSITORY — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.EVENT.REPOSITORY` in `FS_WEMEngine.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.EVENT.REPOSITORY.EVENT.ID` | `FsGiWemEventRepository_EventId` | TField |  | Unique event ID. Multifonds DB Column is EVENT.ID. |
| 2 | `FS.GI.WEM.EVENT.REPOSITORY.EVENT.NAME` | `FsGiWemEventRepository_EventName` | TField |  | Name of the event. Multifonds DB Column is EVENT.NAME. |
| 3 | `FS.GI.WEM.EVENT.REPOSITORY.CREATE.FLAG` | `FsGiWemEventRepository_CreateFlag` | TField |  | flag to indiate the event will able to create a new workflow occurrence. Multifonds DB Column is CREATE.FLAG. |
| 4 | `FS.GI.WEM.EVENT.REPOSITORY.CREATE.STEP.FLAG` | `FsGiWemEventRepository_CreateStepFlag` | TField |  | Flag to indiate the event will able to create a new workflow steps Multifonds DB Column is CREATE.STEP.FLAG. |
| 5 | `FS.GI.WEM.EVENT.REPOSITORY.ACTION` | `FsGiWemEventRepository_Action` | TField |  | Action that the event can perform on the workflow. Multifonds DB Column is ACTION. |
| 6 | `FS.GI.WEM.EVENT.REPOSITORY.EVENT.TYPE` | `FsGiWemEventRepository_EventType` | TField |  | Type of event Multifonds DB Column is EVENT.TYPE. |
| 7 | `FS.GI.WEM.EVENT.REPOSITORY.RESERVED10` | `FsGiWemEventRepository_Reserved10` | TField |  |  |
| 8 | `FS.GI.WEM.EVENT.REPOSITORY.RESERVED9` | `FsGiWemEventRepository_Reserved9` | TField |  |  |
| 9 | `FS.GI.WEM.EVENT.REPOSITORY.RESERVED8` | `FsGiWemEventRepository_Reserved8` | TField |  |  |
| 10 | `FS.GI.WEM.EVENT.REPOSITORY.RESERVED7` | `FsGiWemEventRepository_Reserved7` | TField |  |  |
| 11 | `FS.GI.WEM.EVENT.REPOSITORY.RESERVED6` | `FsGiWemEventRepository_Reserved6` | TField |  |  |
| 12 | `FS.GI.WEM.EVENT.REPOSITORY.RESERVED5` | `FsGiWemEventRepository_Reserved5` | TField |  |  |
| 13 | `FS.GI.WEM.EVENT.REPOSITORY.RESERVED4` | `FsGiWemEventRepository_Reserved4` | TField |  |  |
| 14 | `FS.GI.WEM.EVENT.REPOSITORY.RESERVED3` | `FsGiWemEventRepository_Reserved3` | TField |  |  |
| 15 | `FS.GI.WEM.EVENT.REPOSITORY.RESERVED2` | `FsGiWemEventRepository_Reserved2` | TField |  |  |
| 16 | `FS.GI.WEM.EVENT.REPOSITORY.RESERVED1` | `FsGiWemEventRepository_Reserved1` | TField |  |  |
| 17 | `FS.GI.WEM.EVENT.REPOSITORY.LOCAL.REF` | `FsGiWemEventRepository_LocalRef` |  |  |  |
| 18 | `FS.GI.WEM.EVENT.REPOSITORY.OVERRIDE` | `FsGiWemEventRepository_Override` |  |  |  |
| 19 | `FS.GI.WEM.EVENT.REPOSITORY.RECORD.STATUS` | `FsGiWemEventRepository_RecordStatus` | String |  |  |
| 20 | `FS.GI.WEM.EVENT.REPOSITORY.CURR.NO` | `FsGiWemEventRepository_CurrNo` | String |  |  |
| 21 | `FS.GI.WEM.EVENT.REPOSITORY.INPUTTER` | `FsGiWemEventRepository_Inputter` |  |  |  |
| 22 | `FS.GI.WEM.EVENT.REPOSITORY.DATE.TIME` | `FsGiWemEventRepository_DateTime` |  |  |  |
| 23 | `FS.GI.WEM.EVENT.REPOSITORY.AUTHORISER` | `FsGiWemEventRepository_Authoriser` | String |  |  |
| 24 | `FS.GI.WEM.EVENT.REPOSITORY.CO.CODE` | `FsGiWemEventRepository_CoCode` | String |  |  |
| 25 | `FS.GI.WEM.EVENT.REPOSITORY.DEPT.CODE` | `FsGiWemEventRepository_DeptCode` | String |  |  |
| 26 | `FS.GI.WEM.EVENT.REPOSITORY.AUDITOR.CODE` | `FsGiWemEventRepository_AuditorCode` | String |  |  |
| 27 | `FS.GI.WEM.EVENT.REPOSITORY.AUDIT.DATE.TIME` | `FsGiWemEventRepository_AuditDateTime` | String |  |  |
