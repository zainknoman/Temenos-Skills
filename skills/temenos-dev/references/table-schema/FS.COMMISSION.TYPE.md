# FS.COMMISSION.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.COMMISSION.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.COMMISSION.TYPE.DESCRIPTION` | `FsCommissionType_Description` |  |  |  |
| 2 | `FS.COMMISSION.TYPE.FILTER.KEY` | `FsCommissionType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.COMMISSION.TYPE.RECORD.ID` | `FsCommissionType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.COMMISSION.TYPE.RESERVED10` | `FsCommissionType_Reserved10` | TField |  |  |
| 5 | `FS.COMMISSION.TYPE.RESERVED9` | `FsCommissionType_Reserved9` | TField |  |  |
| 6 | `FS.COMMISSION.TYPE.RESERVED8` | `FsCommissionType_Reserved8` | TField |  |  |
| 7 | `FS.COMMISSION.TYPE.RESERVED7` | `FsCommissionType_Reserved7` | TField |  |  |
| 8 | `FS.COMMISSION.TYPE.RESERVED6` | `FsCommissionType_Reserved6` | TField |  |  |
| 9 | `FS.COMMISSION.TYPE.RESERVED5` | `FsCommissionType_Reserved5` | TField |  |  |
| 10 | `FS.COMMISSION.TYPE.RESERVED4` | `FsCommissionType_Reserved4` | TField |  |  |
| 11 | `FS.COMMISSION.TYPE.RESERVED3` | `FsCommissionType_Reserved3` | TField |  |  |
| 12 | `FS.COMMISSION.TYPE.RESERVED2` | `FsCommissionType_Reserved2` | TField |  |  |
| 13 | `FS.COMMISSION.TYPE.RESERVED1` | `FsCommissionType_Reserved1` | TField |  |  |
| 14 | `FS.COMMISSION.TYPE.LOCAL.REF` | `FsCommissionType_LocalRef` |  |  |  |
| 15 | `FS.COMMISSION.TYPE.OVERRIDE` | `FsCommissionType_Override` |  |  |  |
| 16 | `FS.COMMISSION.TYPE.RECORD.STATUS` | `FsCommissionType_RecordStatus` | String |  |  |
| 17 | `FS.COMMISSION.TYPE.CURR.NO` | `FsCommissionType_CurrNo` | String |  |  |
| 18 | `FS.COMMISSION.TYPE.INPUTTER` | `FsCommissionType_Inputter` |  |  |  |
| 19 | `FS.COMMISSION.TYPE.DATE.TIME` | `FsCommissionType_DateTime` |  |  |  |
| 20 | `FS.COMMISSION.TYPE.AUTHORISER` | `FsCommissionType_Authoriser` | String |  |  |
| 21 | `FS.COMMISSION.TYPE.CO.CODE` | `FsCommissionType_CoCode` | String |  |  |
| 22 | `FS.COMMISSION.TYPE.DEPT.CODE` | `FsCommissionType_DeptCode` | String |  |  |
| 23 | `FS.COMMISSION.TYPE.AUDITOR.CODE` | `FsCommissionType_AuditorCode` | String |  |  |
| 24 | `FS.COMMISSION.TYPE.AUDIT.DATE.TIME` | `FsCommissionType_AuditDateTime` | String |  |  |
