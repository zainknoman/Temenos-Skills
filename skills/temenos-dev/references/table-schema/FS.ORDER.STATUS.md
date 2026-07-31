# FS.ORDER.STATUS — Table Schema

> Source: `INSERTS/I_F.FS.ORDER.STATUS` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ORDER.STATUS.DESCRIPTION` | `FsOrderStatus_Description` |  |  |  |
| 2 | `FS.ORDER.STATUS.FILTER.KEY` | `FsOrderStatus_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ORDER.STATUS.RECORD.ID` | `FsOrderStatus_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ORDER.STATUS.RESERVED10` | `FsOrderStatus_Reserved10` | TField |  |  |
| 5 | `FS.ORDER.STATUS.RESERVED9` | `FsOrderStatus_Reserved9` | TField |  |  |
| 6 | `FS.ORDER.STATUS.RESERVED8` | `FsOrderStatus_Reserved8` | TField |  |  |
| 7 | `FS.ORDER.STATUS.RESERVED7` | `FsOrderStatus_Reserved7` | TField |  |  |
| 8 | `FS.ORDER.STATUS.RESERVED6` | `FsOrderStatus_Reserved6` | TField |  |  |
| 9 | `FS.ORDER.STATUS.RESERVED5` | `FsOrderStatus_Reserved5` | TField |  |  |
| 10 | `FS.ORDER.STATUS.RESERVED4` | `FsOrderStatus_Reserved4` | TField |  |  |
| 11 | `FS.ORDER.STATUS.RESERVED3` | `FsOrderStatus_Reserved3` | TField |  |  |
| 12 | `FS.ORDER.STATUS.RESERVED2` | `FsOrderStatus_Reserved2` | TField |  |  |
| 13 | `FS.ORDER.STATUS.RESERVED1` | `FsOrderStatus_Reserved1` | TField |  |  |
| 14 | `FS.ORDER.STATUS.LOCAL.REF` | `FsOrderStatus_LocalRef` |  |  |  |
| 15 | `FS.ORDER.STATUS.OVERRIDE` | `FsOrderStatus_Override` |  |  |  |
| 16 | `FS.ORDER.STATUS.RECORD.STATUS` | `FsOrderStatus_RecordStatus` | String |  |  |
| 17 | `FS.ORDER.STATUS.CURR.NO` | `FsOrderStatus_CurrNo` | String |  |  |
| 18 | `FS.ORDER.STATUS.INPUTTER` | `FsOrderStatus_Inputter` |  |  |  |
| 19 | `FS.ORDER.STATUS.DATE.TIME` | `FsOrderStatus_DateTime` |  |  |  |
| 20 | `FS.ORDER.STATUS.AUTHORISER` | `FsOrderStatus_Authoriser` | String |  |  |
| 21 | `FS.ORDER.STATUS.CO.CODE` | `FsOrderStatus_CoCode` | String |  |  |
| 22 | `FS.ORDER.STATUS.DEPT.CODE` | `FsOrderStatus_DeptCode` | String |  |  |
| 23 | `FS.ORDER.STATUS.AUDITOR.CODE` | `FsOrderStatus_AuditorCode` | String |  |  |
| 24 | `FS.ORDER.STATUS.AUDIT.DATE.TIME` | `FsOrderStatus_AuditDateTime` | String |  |  |
