# FS.SHAREHOLDER.COMMISSION.CODE — Table Schema

> Source: `INSERTS/I_F.FS.SHAREHOLDER.COMMISSION.CODE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.SHAREHOLDER.COMMISSION.CODE.DESCRIPTION` | `FsShareholderCommissionCode_Description` |  |  |  |
| 2 | `FS.SHAREHOLDER.COMMISSION.CODE.FILTER.KEY` | `FsShareholderCommissionCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.SHAREHOLDER.COMMISSION.CODE.RECORD.ID` | `FsShareholderCommissionCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.SHAREHOLDER.COMMISSION.CODE.RESERVED10` | `FsShareholderCommissionCode_Reserved10` | TField |  |  |
| 5 | `FS.SHAREHOLDER.COMMISSION.CODE.RESERVED9` | `FsShareholderCommissionCode_Reserved9` | TField |  |  |
| 6 | `FS.SHAREHOLDER.COMMISSION.CODE.RESERVED8` | `FsShareholderCommissionCode_Reserved8` | TField |  |  |
| 7 | `FS.SHAREHOLDER.COMMISSION.CODE.RESERVED7` | `FsShareholderCommissionCode_Reserved7` | TField |  |  |
| 8 | `FS.SHAREHOLDER.COMMISSION.CODE.RESERVED6` | `FsShareholderCommissionCode_Reserved6` | TField |  |  |
| 9 | `FS.SHAREHOLDER.COMMISSION.CODE.RESERVED5` | `FsShareholderCommissionCode_Reserved5` | TField |  |  |
| 10 | `FS.SHAREHOLDER.COMMISSION.CODE.RESERVED4` | `FsShareholderCommissionCode_Reserved4` | TField |  |  |
| 11 | `FS.SHAREHOLDER.COMMISSION.CODE.RESERVED3` | `FsShareholderCommissionCode_Reserved3` | TField |  |  |
| 12 | `FS.SHAREHOLDER.COMMISSION.CODE.RESERVED2` | `FsShareholderCommissionCode_Reserved2` | TField |  |  |
| 13 | `FS.SHAREHOLDER.COMMISSION.CODE.RESERVED1` | `FsShareholderCommissionCode_Reserved1` | TField |  |  |
| 14 | `FS.SHAREHOLDER.COMMISSION.CODE.LOCAL.REF` | `FsShareholderCommissionCode_LocalRef` |  |  |  |
| 15 | `FS.SHAREHOLDER.COMMISSION.CODE.OVERRIDE` | `FsShareholderCommissionCode_Override` |  |  |  |
| 16 | `FS.SHAREHOLDER.COMMISSION.CODE.RECORD.STATUS` | `FsShareholderCommissionCode_RecordStatus` | String |  |  |
| 17 | `FS.SHAREHOLDER.COMMISSION.CODE.CURR.NO` | `FsShareholderCommissionCode_CurrNo` | String |  |  |
| 18 | `FS.SHAREHOLDER.COMMISSION.CODE.INPUTTER` | `FsShareholderCommissionCode_Inputter` |  |  |  |
| 19 | `FS.SHAREHOLDER.COMMISSION.CODE.DATE.TIME` | `FsShareholderCommissionCode_DateTime` |  |  |  |
| 20 | `FS.SHAREHOLDER.COMMISSION.CODE.AUTHORISER` | `FsShareholderCommissionCode_Authoriser` | String |  |  |
| 21 | `FS.SHAREHOLDER.COMMISSION.CODE.CO.CODE` | `FsShareholderCommissionCode_CoCode` | String |  |  |
| 22 | `FS.SHAREHOLDER.COMMISSION.CODE.DEPT.CODE` | `FsShareholderCommissionCode_DeptCode` | String |  |  |
| 23 | `FS.SHAREHOLDER.COMMISSION.CODE.AUDITOR.CODE` | `FsShareholderCommissionCode_AuditorCode` | String |  |  |
| 24 | `FS.SHAREHOLDER.COMMISSION.CODE.AUDIT.DATE.TIME` | `FsShareholderCommissionCode_AuditDateTime` | String |  |  |
