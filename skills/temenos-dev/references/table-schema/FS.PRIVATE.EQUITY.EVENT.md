# FS.PRIVATE.EQUITY.EVENT — Table Schema

> Source: `INSERTS/I_F.FS.PRIVATE.EQUITY.EVENT` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.PRIVATE.EQUITY.EVENT.DESCRIPTION` | `FsPrivateEquityEvent_Description` |  |  |  |
| 2 | `FS.PRIVATE.EQUITY.EVENT.FILTER.KEY` | `FsPrivateEquityEvent_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.PRIVATE.EQUITY.EVENT.RECORD.ID` | `FsPrivateEquityEvent_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.PRIVATE.EQUITY.EVENT.RESERVED10` | `FsPrivateEquityEvent_Reserved10` | TField |  |  |
| 5 | `FS.PRIVATE.EQUITY.EVENT.RESERVED9` | `FsPrivateEquityEvent_Reserved9` | TField |  |  |
| 6 | `FS.PRIVATE.EQUITY.EVENT.RESERVED8` | `FsPrivateEquityEvent_Reserved8` | TField |  |  |
| 7 | `FS.PRIVATE.EQUITY.EVENT.RESERVED7` | `FsPrivateEquityEvent_Reserved7` | TField |  |  |
| 8 | `FS.PRIVATE.EQUITY.EVENT.RESERVED6` | `FsPrivateEquityEvent_Reserved6` | TField |  |  |
| 9 | `FS.PRIVATE.EQUITY.EVENT.RESERVED5` | `FsPrivateEquityEvent_Reserved5` | TField |  |  |
| 10 | `FS.PRIVATE.EQUITY.EVENT.RESERVED4` | `FsPrivateEquityEvent_Reserved4` | TField |  |  |
| 11 | `FS.PRIVATE.EQUITY.EVENT.RESERVED3` | `FsPrivateEquityEvent_Reserved3` | TField |  |  |
| 12 | `FS.PRIVATE.EQUITY.EVENT.RESERVED2` | `FsPrivateEquityEvent_Reserved2` | TField |  |  |
| 13 | `FS.PRIVATE.EQUITY.EVENT.RESERVED1` | `FsPrivateEquityEvent_Reserved1` | TField |  |  |
| 14 | `FS.PRIVATE.EQUITY.EVENT.LOCAL.REF` | `FsPrivateEquityEvent_LocalRef` |  |  |  |
| 15 | `FS.PRIVATE.EQUITY.EVENT.OVERRIDE` | `FsPrivateEquityEvent_Override` |  |  |  |
| 16 | `FS.PRIVATE.EQUITY.EVENT.RECORD.STATUS` | `FsPrivateEquityEvent_RecordStatus` | String |  |  |
| 17 | `FS.PRIVATE.EQUITY.EVENT.CURR.NO` | `FsPrivateEquityEvent_CurrNo` | String |  |  |
| 18 | `FS.PRIVATE.EQUITY.EVENT.INPUTTER` | `FsPrivateEquityEvent_Inputter` |  |  |  |
| 19 | `FS.PRIVATE.EQUITY.EVENT.DATE.TIME` | `FsPrivateEquityEvent_DateTime` |  |  |  |
| 20 | `FS.PRIVATE.EQUITY.EVENT.AUTHORISER` | `FsPrivateEquityEvent_Authoriser` | String |  |  |
| 21 | `FS.PRIVATE.EQUITY.EVENT.CO.CODE` | `FsPrivateEquityEvent_CoCode` | String |  |  |
| 22 | `FS.PRIVATE.EQUITY.EVENT.DEPT.CODE` | `FsPrivateEquityEvent_DeptCode` | String |  |  |
| 23 | `FS.PRIVATE.EQUITY.EVENT.AUDITOR.CODE` | `FsPrivateEquityEvent_AuditorCode` | String |  |  |
| 24 | `FS.PRIVATE.EQUITY.EVENT.AUDIT.DATE.TIME` | `FsPrivateEquityEvent_AuditDateTime` | String |  |  |
