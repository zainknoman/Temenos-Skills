# FS.DEAL.STATUS — Table Schema

> Source: `INSERTS/I_F.FS.DEAL.STATUS` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.DEAL.STATUS.DESCRIPTION` | `FsDealStatus_Description` |  |  |  |
| 2 | `FS.DEAL.STATUS.FILTER.KEY` | `FsDealStatus_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.DEAL.STATUS.RECORD.ID` | `FsDealStatus_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.DEAL.STATUS.RESERVED10` | `FsDealStatus_Reserved10` | TField |  |  |
| 5 | `FS.DEAL.STATUS.RESERVED9` | `FsDealStatus_Reserved9` | TField |  |  |
| 6 | `FS.DEAL.STATUS.RESERVED8` | `FsDealStatus_Reserved8` | TField |  |  |
| 7 | `FS.DEAL.STATUS.RESERVED7` | `FsDealStatus_Reserved7` | TField |  |  |
| 8 | `FS.DEAL.STATUS.RESERVED6` | `FsDealStatus_Reserved6` | TField |  |  |
| 9 | `FS.DEAL.STATUS.RESERVED5` | `FsDealStatus_Reserved5` | TField |  |  |
| 10 | `FS.DEAL.STATUS.RESERVED4` | `FsDealStatus_Reserved4` | TField |  |  |
| 11 | `FS.DEAL.STATUS.RESERVED3` | `FsDealStatus_Reserved3` | TField |  |  |
| 12 | `FS.DEAL.STATUS.RESERVED2` | `FsDealStatus_Reserved2` | TField |  |  |
| 13 | `FS.DEAL.STATUS.RESERVED1` | `FsDealStatus_Reserved1` | TField |  |  |
| 14 | `FS.DEAL.STATUS.LOCAL.REF` | `FsDealStatus_LocalRef` |  |  |  |
| 15 | `FS.DEAL.STATUS.OVERRIDE` | `FsDealStatus_Override` |  |  |  |
| 16 | `FS.DEAL.STATUS.RECORD.STATUS` | `FsDealStatus_RecordStatus` | String |  |  |
| 17 | `FS.DEAL.STATUS.CURR.NO` | `FsDealStatus_CurrNo` | String |  |  |
| 18 | `FS.DEAL.STATUS.INPUTTER` | `FsDealStatus_Inputter` |  |  |  |
| 19 | `FS.DEAL.STATUS.DATE.TIME` | `FsDealStatus_DateTime` |  |  |  |
| 20 | `FS.DEAL.STATUS.AUTHORISER` | `FsDealStatus_Authoriser` | String |  |  |
| 21 | `FS.DEAL.STATUS.CO.CODE` | `FsDealStatus_CoCode` | String |  |  |
| 22 | `FS.DEAL.STATUS.DEPT.CODE` | `FsDealStatus_DeptCode` | String |  |  |
| 23 | `FS.DEAL.STATUS.AUDITOR.CODE` | `FsDealStatus_AuditorCode` | String |  |  |
| 24 | `FS.DEAL.STATUS.AUDIT.DATE.TIME` | `FsDealStatus_AuditDateTime` | String |  |  |
