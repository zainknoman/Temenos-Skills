# FS.ACCRUAL.BASIS — Table Schema

> Source: `INSERTS/I_F.FS.ACCRUAL.BASIS` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.ACCRUAL.BASIS.DESCRIPTION` | `FsAccrualBasis_Description` |  |  |  |
| 2 | `FS.ACCRUAL.BASIS.FILTER.KEY` | `FsAccrualBasis_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.ACCRUAL.BASIS.RECORD.ID` | `FsAccrualBasis_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.ACCRUAL.BASIS.RESERVED10` | `FsAccrualBasis_Reserved10` | TField |  |  |
| 5 | `FS.ACCRUAL.BASIS.RESERVED9` | `FsAccrualBasis_Reserved9` | TField |  |  |
| 6 | `FS.ACCRUAL.BASIS.RESERVED8` | `FsAccrualBasis_Reserved8` | TField |  |  |
| 7 | `FS.ACCRUAL.BASIS.RESERVED7` | `FsAccrualBasis_Reserved7` | TField |  |  |
| 8 | `FS.ACCRUAL.BASIS.RESERVED6` | `FsAccrualBasis_Reserved6` | TField |  |  |
| 9 | `FS.ACCRUAL.BASIS.RESERVED5` | `FsAccrualBasis_Reserved5` | TField |  |  |
| 10 | `FS.ACCRUAL.BASIS.RESERVED4` | `FsAccrualBasis_Reserved4` | TField |  |  |
| 11 | `FS.ACCRUAL.BASIS.RESERVED3` | `FsAccrualBasis_Reserved3` | TField |  |  |
| 12 | `FS.ACCRUAL.BASIS.RESERVED2` | `FsAccrualBasis_Reserved2` | TField |  |  |
| 13 | `FS.ACCRUAL.BASIS.RESERVED1` | `FsAccrualBasis_Reserved1` | TField |  |  |
| 14 | `FS.ACCRUAL.BASIS.LOCAL.REF` | `FsAccrualBasis_LocalRef` |  |  |  |
| 15 | `FS.ACCRUAL.BASIS.OVERRIDE` | `FsAccrualBasis_Override` |  |  |  |
| 16 | `FS.ACCRUAL.BASIS.RECORD.STATUS` | `FsAccrualBasis_RecordStatus` | String |  |  |
| 17 | `FS.ACCRUAL.BASIS.CURR.NO` | `FsAccrualBasis_CurrNo` | String |  |  |
| 18 | `FS.ACCRUAL.BASIS.INPUTTER` | `FsAccrualBasis_Inputter` |  |  |  |
| 19 | `FS.ACCRUAL.BASIS.DATE.TIME` | `FsAccrualBasis_DateTime` |  |  |  |
| 20 | `FS.ACCRUAL.BASIS.AUTHORISER` | `FsAccrualBasis_Authoriser` | String |  |  |
| 21 | `FS.ACCRUAL.BASIS.CO.CODE` | `FsAccrualBasis_CoCode` | String |  |  |
| 22 | `FS.ACCRUAL.BASIS.DEPT.CODE` | `FsAccrualBasis_DeptCode` | String |  |  |
| 23 | `FS.ACCRUAL.BASIS.AUDITOR.CODE` | `FsAccrualBasis_AuditorCode` | String |  |  |
| 24 | `FS.ACCRUAL.BASIS.AUDIT.DATE.TIME` | `FsAccrualBasis_AuditDateTime` | String |  |  |
