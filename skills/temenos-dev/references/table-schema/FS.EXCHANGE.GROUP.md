# FS.EXCHANGE.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.EXCHANGE.GROUP` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.EXCHANGE.GROUP.DESCRIPTION` | `FsExchangeGroup_Description` |  |  |  |
| 2 | `FS.EXCHANGE.GROUP.FILTER.KEY` | `FsExchangeGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.EXCHANGE.GROUP.RECORD.ID` | `FsExchangeGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.EXCHANGE.GROUP.RESERVED10` | `FsExchangeGroup_Reserved10` | TField |  |  |
| 5 | `FS.EXCHANGE.GROUP.RESERVED9` | `FsExchangeGroup_Reserved9` | TField |  |  |
| 6 | `FS.EXCHANGE.GROUP.RESERVED8` | `FsExchangeGroup_Reserved8` | TField |  |  |
| 7 | `FS.EXCHANGE.GROUP.RESERVED7` | `FsExchangeGroup_Reserved7` | TField |  |  |
| 8 | `FS.EXCHANGE.GROUP.RESERVED6` | `FsExchangeGroup_Reserved6` | TField |  |  |
| 9 | `FS.EXCHANGE.GROUP.RESERVED5` | `FsExchangeGroup_Reserved5` | TField |  |  |
| 10 | `FS.EXCHANGE.GROUP.RESERVED4` | `FsExchangeGroup_Reserved4` | TField |  |  |
| 11 | `FS.EXCHANGE.GROUP.RESERVED3` | `FsExchangeGroup_Reserved3` | TField |  |  |
| 12 | `FS.EXCHANGE.GROUP.RESERVED2` | `FsExchangeGroup_Reserved2` | TField |  |  |
| 13 | `FS.EXCHANGE.GROUP.RESERVED1` | `FsExchangeGroup_Reserved1` | TField |  |  |
| 14 | `FS.EXCHANGE.GROUP.LOCAL.REF` | `FsExchangeGroup_LocalRef` |  |  |  |
| 15 | `FS.EXCHANGE.GROUP.OVERRIDE` | `FsExchangeGroup_Override` |  |  |  |
| 16 | `FS.EXCHANGE.GROUP.RECORD.STATUS` | `FsExchangeGroup_RecordStatus` | String |  |  |
| 17 | `FS.EXCHANGE.GROUP.CURR.NO` | `FsExchangeGroup_CurrNo` | String |  |  |
| 18 | `FS.EXCHANGE.GROUP.INPUTTER` | `FsExchangeGroup_Inputter` |  |  |  |
| 19 | `FS.EXCHANGE.GROUP.DATE.TIME` | `FsExchangeGroup_DateTime` |  |  |  |
| 20 | `FS.EXCHANGE.GROUP.AUTHORISER` | `FsExchangeGroup_Authoriser` | String |  |  |
| 21 | `FS.EXCHANGE.GROUP.CO.CODE` | `FsExchangeGroup_CoCode` | String |  |  |
| 22 | `FS.EXCHANGE.GROUP.DEPT.CODE` | `FsExchangeGroup_DeptCode` | String |  |  |
| 23 | `FS.EXCHANGE.GROUP.AUDITOR.CODE` | `FsExchangeGroup_AuditorCode` | String |  |  |
| 24 | `FS.EXCHANGE.GROUP.AUDIT.DATE.TIME` | `FsExchangeGroup_AuditDateTime` | String |  |  |
