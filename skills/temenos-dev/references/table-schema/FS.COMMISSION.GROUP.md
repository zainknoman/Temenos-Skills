# FS.COMMISSION.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.COMMISSION.GROUP` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.COMMISSION.GROUP.DESCRIPTION` | `FsCommissionGroup_Description` |  |  |  |
| 2 | `FS.COMMISSION.GROUP.FILTER.KEY` | `FsCommissionGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.COMMISSION.GROUP.RECORD.ID` | `FsCommissionGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.COMMISSION.GROUP.RESERVED10` | `FsCommissionGroup_Reserved10` | TField |  |  |
| 5 | `FS.COMMISSION.GROUP.RESERVED9` | `FsCommissionGroup_Reserved9` | TField |  |  |
| 6 | `FS.COMMISSION.GROUP.RESERVED8` | `FsCommissionGroup_Reserved8` | TField |  |  |
| 7 | `FS.COMMISSION.GROUP.RESERVED7` | `FsCommissionGroup_Reserved7` | TField |  |  |
| 8 | `FS.COMMISSION.GROUP.RESERVED6` | `FsCommissionGroup_Reserved6` | TField |  |  |
| 9 | `FS.COMMISSION.GROUP.RESERVED5` | `FsCommissionGroup_Reserved5` | TField |  |  |
| 10 | `FS.COMMISSION.GROUP.RESERVED4` | `FsCommissionGroup_Reserved4` | TField |  |  |
| 11 | `FS.COMMISSION.GROUP.RESERVED3` | `FsCommissionGroup_Reserved3` | TField |  |  |
| 12 | `FS.COMMISSION.GROUP.RESERVED2` | `FsCommissionGroup_Reserved2` | TField |  |  |
| 13 | `FS.COMMISSION.GROUP.RESERVED1` | `FsCommissionGroup_Reserved1` | TField |  |  |
| 14 | `FS.COMMISSION.GROUP.LOCAL.REF` | `FsCommissionGroup_LocalRef` |  |  |  |
| 15 | `FS.COMMISSION.GROUP.OVERRIDE` | `FsCommissionGroup_Override` |  |  |  |
| 16 | `FS.COMMISSION.GROUP.RECORD.STATUS` | `FsCommissionGroup_RecordStatus` | String |  |  |
| 17 | `FS.COMMISSION.GROUP.CURR.NO` | `FsCommissionGroup_CurrNo` | String |  |  |
| 18 | `FS.COMMISSION.GROUP.INPUTTER` | `FsCommissionGroup_Inputter` |  |  |  |
| 19 | `FS.COMMISSION.GROUP.DATE.TIME` | `FsCommissionGroup_DateTime` |  |  |  |
| 20 | `FS.COMMISSION.GROUP.AUTHORISER` | `FsCommissionGroup_Authoriser` | String |  |  |
| 21 | `FS.COMMISSION.GROUP.CO.CODE` | `FsCommissionGroup_CoCode` | String |  |  |
| 22 | `FS.COMMISSION.GROUP.DEPT.CODE` | `FsCommissionGroup_DeptCode` | String |  |  |
| 23 | `FS.COMMISSION.GROUP.AUDITOR.CODE` | `FsCommissionGroup_AuditorCode` | String |  |  |
| 24 | `FS.COMMISSION.GROUP.AUDIT.DATE.TIME` | `FsCommissionGroup_AuditDateTime` | String |  |  |
