# FS.DEAL.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.DEAL.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.DEAL.TYPE.DESCRIPTION` | `FsDealType_Description` |  |  |  |
| 2 | `FS.DEAL.TYPE.FILTER.KEY` | `FsDealType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.DEAL.TYPE.RECORD.ID` | `FsDealType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.DEAL.TYPE.RESERVED10` | `FsDealType_Reserved10` | TField |  |  |
| 5 | `FS.DEAL.TYPE.RESERVED9` | `FsDealType_Reserved9` | TField |  |  |
| 6 | `FS.DEAL.TYPE.RESERVED8` | `FsDealType_Reserved8` | TField |  |  |
| 7 | `FS.DEAL.TYPE.RESERVED7` | `FsDealType_Reserved7` | TField |  |  |
| 8 | `FS.DEAL.TYPE.RESERVED6` | `FsDealType_Reserved6` | TField |  |  |
| 9 | `FS.DEAL.TYPE.RESERVED5` | `FsDealType_Reserved5` | TField |  |  |
| 10 | `FS.DEAL.TYPE.RESERVED4` | `FsDealType_Reserved4` | TField |  |  |
| 11 | `FS.DEAL.TYPE.RESERVED3` | `FsDealType_Reserved3` | TField |  |  |
| 12 | `FS.DEAL.TYPE.RESERVED2` | `FsDealType_Reserved2` | TField |  |  |
| 13 | `FS.DEAL.TYPE.RESERVED1` | `FsDealType_Reserved1` | TField |  |  |
| 14 | `FS.DEAL.TYPE.LOCAL.REF` | `FsDealType_LocalRef` |  |  |  |
| 15 | `FS.DEAL.TYPE.OVERRIDE` | `FsDealType_Override` |  |  |  |
| 16 | `FS.DEAL.TYPE.RECORD.STATUS` | `FsDealType_RecordStatus` | String |  |  |
| 17 | `FS.DEAL.TYPE.CURR.NO` | `FsDealType_CurrNo` | String |  |  |
| 18 | `FS.DEAL.TYPE.INPUTTER` | `FsDealType_Inputter` |  |  |  |
| 19 | `FS.DEAL.TYPE.DATE.TIME` | `FsDealType_DateTime` |  |  |  |
| 20 | `FS.DEAL.TYPE.AUTHORISER` | `FsDealType_Authoriser` | String |  |  |
| 21 | `FS.DEAL.TYPE.CO.CODE` | `FsDealType_CoCode` | String |  |  |
| 22 | `FS.DEAL.TYPE.DEPT.CODE` | `FsDealType_DeptCode` | String |  |  |
| 23 | `FS.DEAL.TYPE.AUDITOR.CODE` | `FsDealType_AuditorCode` | String |  |  |
| 24 | `FS.DEAL.TYPE.AUDIT.DATE.TIME` | `FsDealType_AuditDateTime` | String |  |  |
