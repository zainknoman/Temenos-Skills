# FS.INTERFACE.MODE.RECD — Table Schema

> Source: `INSERTS/I_F.FS.INTERFACE.MODE.RECD` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.INTERFACE.MODE.RECD.DESCRIPTION` | `FsInterfaceModeRecd_Description` |  |  |  |
| 2 | `FS.INTERFACE.MODE.RECD.FILTER.KEY` | `FsInterfaceModeRecd_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.INTERFACE.MODE.RECD.RECORD.ID` | `FsInterfaceModeRecd_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.INTERFACE.MODE.RECD.RESERVED10` | `FsInterfaceModeRecd_Reserved10` | TField |  |  |
| 5 | `FS.INTERFACE.MODE.RECD.RESERVED9` | `FsInterfaceModeRecd_Reserved9` | TField |  |  |
| 6 | `FS.INTERFACE.MODE.RECD.RESERVED8` | `FsInterfaceModeRecd_Reserved8` | TField |  |  |
| 7 | `FS.INTERFACE.MODE.RECD.RESERVED7` | `FsInterfaceModeRecd_Reserved7` | TField |  |  |
| 8 | `FS.INTERFACE.MODE.RECD.RESERVED6` | `FsInterfaceModeRecd_Reserved6` | TField |  |  |
| 9 | `FS.INTERFACE.MODE.RECD.RESERVED5` | `FsInterfaceModeRecd_Reserved5` | TField |  |  |
| 10 | `FS.INTERFACE.MODE.RECD.RESERVED4` | `FsInterfaceModeRecd_Reserved4` | TField |  |  |
| 11 | `FS.INTERFACE.MODE.RECD.RESERVED3` | `FsInterfaceModeRecd_Reserved3` | TField |  |  |
| 12 | `FS.INTERFACE.MODE.RECD.RESERVED2` | `FsInterfaceModeRecd_Reserved2` | TField |  |  |
| 13 | `FS.INTERFACE.MODE.RECD.RESERVED1` | `FsInterfaceModeRecd_Reserved1` | TField |  |  |
| 14 | `FS.INTERFACE.MODE.RECD.LOCAL.REF` | `FsInterfaceModeRecd_LocalRef` |  |  |  |
| 15 | `FS.INTERFACE.MODE.RECD.OVERRIDE` | `FsInterfaceModeRecd_Override` |  |  |  |
| 16 | `FS.INTERFACE.MODE.RECD.RECORD.STATUS` | `FsInterfaceModeRecd_RecordStatus` | String |  |  |
| 17 | `FS.INTERFACE.MODE.RECD.CURR.NO` | `FsInterfaceModeRecd_CurrNo` | String |  |  |
| 18 | `FS.INTERFACE.MODE.RECD.INPUTTER` | `FsInterfaceModeRecd_Inputter` |  |  |  |
| 19 | `FS.INTERFACE.MODE.RECD.DATE.TIME` | `FsInterfaceModeRecd_DateTime` |  |  |  |
| 20 | `FS.INTERFACE.MODE.RECD.AUTHORISER` | `FsInterfaceModeRecd_Authoriser` | String |  |  |
| 21 | `FS.INTERFACE.MODE.RECD.CO.CODE` | `FsInterfaceModeRecd_CoCode` | String |  |  |
| 22 | `FS.INTERFACE.MODE.RECD.DEPT.CODE` | `FsInterfaceModeRecd_DeptCode` | String |  |  |
| 23 | `FS.INTERFACE.MODE.RECD.AUDITOR.CODE` | `FsInterfaceModeRecd_AuditorCode` | String |  |  |
| 24 | `FS.INTERFACE.MODE.RECD.AUDIT.DATE.TIME` | `FsInterfaceModeRecd_AuditDateTime` | String |  |  |
