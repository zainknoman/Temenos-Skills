# FS.DEAL.RECEIVED.MODE — Table Schema

> Source: `INSERTS/I_F.FS.DEAL.RECEIVED.MODE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.DEAL.RECEIVED.MODE.DESCRIPTION` | `FsDealReceivedMode_Description` |  |  |  |
| 2 | `FS.DEAL.RECEIVED.MODE.FILTER.KEY` | `FsDealReceivedMode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.DEAL.RECEIVED.MODE.RECORD.ID` | `FsDealReceivedMode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.DEAL.RECEIVED.MODE.RESERVED10` | `FsDealReceivedMode_Reserved10` | TField |  |  |
| 5 | `FS.DEAL.RECEIVED.MODE.RESERVED9` | `FsDealReceivedMode_Reserved9` | TField |  |  |
| 6 | `FS.DEAL.RECEIVED.MODE.RESERVED8` | `FsDealReceivedMode_Reserved8` | TField |  |  |
| 7 | `FS.DEAL.RECEIVED.MODE.RESERVED7` | `FsDealReceivedMode_Reserved7` | TField |  |  |
| 8 | `FS.DEAL.RECEIVED.MODE.RESERVED6` | `FsDealReceivedMode_Reserved6` | TField |  |  |
| 9 | `FS.DEAL.RECEIVED.MODE.RESERVED5` | `FsDealReceivedMode_Reserved5` | TField |  |  |
| 10 | `FS.DEAL.RECEIVED.MODE.RESERVED4` | `FsDealReceivedMode_Reserved4` | TField |  |  |
| 11 | `FS.DEAL.RECEIVED.MODE.RESERVED3` | `FsDealReceivedMode_Reserved3` | TField |  |  |
| 12 | `FS.DEAL.RECEIVED.MODE.RESERVED2` | `FsDealReceivedMode_Reserved2` | TField |  |  |
| 13 | `FS.DEAL.RECEIVED.MODE.RESERVED1` | `FsDealReceivedMode_Reserved1` | TField |  |  |
| 14 | `FS.DEAL.RECEIVED.MODE.LOCAL.REF` | `FsDealReceivedMode_LocalRef` |  |  |  |
| 15 | `FS.DEAL.RECEIVED.MODE.OVERRIDE` | `FsDealReceivedMode_Override` |  |  |  |
| 16 | `FS.DEAL.RECEIVED.MODE.RECORD.STATUS` | `FsDealReceivedMode_RecordStatus` | String |  |  |
| 17 | `FS.DEAL.RECEIVED.MODE.CURR.NO` | `FsDealReceivedMode_CurrNo` | String |  |  |
| 18 | `FS.DEAL.RECEIVED.MODE.INPUTTER` | `FsDealReceivedMode_Inputter` |  |  |  |
| 19 | `FS.DEAL.RECEIVED.MODE.DATE.TIME` | `FsDealReceivedMode_DateTime` |  |  |  |
| 20 | `FS.DEAL.RECEIVED.MODE.AUTHORISER` | `FsDealReceivedMode_Authoriser` | String |  |  |
| 21 | `FS.DEAL.RECEIVED.MODE.CO.CODE` | `FsDealReceivedMode_CoCode` | String |  |  |
| 22 | `FS.DEAL.RECEIVED.MODE.DEPT.CODE` | `FsDealReceivedMode_DeptCode` | String |  |  |
| 23 | `FS.DEAL.RECEIVED.MODE.AUDITOR.CODE` | `FsDealReceivedMode_AuditorCode` | String |  |  |
| 24 | `FS.DEAL.RECEIVED.MODE.AUDIT.DATE.TIME` | `FsDealReceivedMode_AuditDateTime` | String |  |  |
