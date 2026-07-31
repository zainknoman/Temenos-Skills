# FS.GROUP.COMMISSION — Table Schema

> Source: `INSERTS/I_F.FS.GROUP.COMMISSION` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GROUP.COMMISSION.DESCRIPTION` | `FsGroupCommission_Description` |  |  |  |
| 2 | `FS.GROUP.COMMISSION.FILTER.KEY` | `FsGroupCommission_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.GROUP.COMMISSION.RECORD.ID` | `FsGroupCommission_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.GROUP.COMMISSION.RESERVED10` | `FsGroupCommission_Reserved10` | TField |  |  |
| 5 | `FS.GROUP.COMMISSION.RESERVED9` | `FsGroupCommission_Reserved9` | TField |  |  |
| 6 | `FS.GROUP.COMMISSION.RESERVED8` | `FsGroupCommission_Reserved8` | TField |  |  |
| 7 | `FS.GROUP.COMMISSION.RESERVED7` | `FsGroupCommission_Reserved7` | TField |  |  |
| 8 | `FS.GROUP.COMMISSION.RESERVED6` | `FsGroupCommission_Reserved6` | TField |  |  |
| 9 | `FS.GROUP.COMMISSION.RESERVED5` | `FsGroupCommission_Reserved5` | TField |  |  |
| 10 | `FS.GROUP.COMMISSION.RESERVED4` | `FsGroupCommission_Reserved4` | TField |  |  |
| 11 | `FS.GROUP.COMMISSION.RESERVED3` | `FsGroupCommission_Reserved3` | TField |  |  |
| 12 | `FS.GROUP.COMMISSION.RESERVED2` | `FsGroupCommission_Reserved2` | TField |  |  |
| 13 | `FS.GROUP.COMMISSION.RESERVED1` | `FsGroupCommission_Reserved1` | TField |  |  |
| 14 | `FS.GROUP.COMMISSION.LOCAL.REF` | `FsGroupCommission_LocalRef` |  |  |  |
| 15 | `FS.GROUP.COMMISSION.OVERRIDE` | `FsGroupCommission_Override` |  |  |  |
| 16 | `FS.GROUP.COMMISSION.RECORD.STATUS` | `FsGroupCommission_RecordStatus` | String |  |  |
| 17 | `FS.GROUP.COMMISSION.CURR.NO` | `FsGroupCommission_CurrNo` | String |  |  |
| 18 | `FS.GROUP.COMMISSION.INPUTTER` | `FsGroupCommission_Inputter` |  |  |  |
| 19 | `FS.GROUP.COMMISSION.DATE.TIME` | `FsGroupCommission_DateTime` |  |  |  |
| 20 | `FS.GROUP.COMMISSION.AUTHORISER` | `FsGroupCommission_Authoriser` | String |  |  |
| 21 | `FS.GROUP.COMMISSION.CO.CODE` | `FsGroupCommission_CoCode` | String |  |  |
| 22 | `FS.GROUP.COMMISSION.DEPT.CODE` | `FsGroupCommission_DeptCode` | String |  |  |
| 23 | `FS.GROUP.COMMISSION.AUDITOR.CODE` | `FsGroupCommission_AuditorCode` | String |  |  |
| 24 | `FS.GROUP.COMMISSION.AUDIT.DATE.TIME` | `FsGroupCommission_AuditDateTime` | String |  |  |
