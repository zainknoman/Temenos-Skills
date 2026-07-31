# FS.IBOR.ECONOMIC.BUCKETS — Table Schema

> Source: `INSERTS/I_F.FS.IBOR.ECONOMIC.BUCKETS` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.IBOR.ECONOMIC.BUCKETS.DESCRIPTION` | `FsIborEconomicBuckets_Description` |  |  |  |
| 2 | `FS.IBOR.ECONOMIC.BUCKETS.FILTER.KEY` | `FsIborEconomicBuckets_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.IBOR.ECONOMIC.BUCKETS.RECORD.ID` | `FsIborEconomicBuckets_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.IBOR.ECONOMIC.BUCKETS.RESERVED10` | `FsIborEconomicBuckets_Reserved10` | TField |  |  |
| 5 | `FS.IBOR.ECONOMIC.BUCKETS.RESERVED9` | `FsIborEconomicBuckets_Reserved9` | TField |  |  |
| 6 | `FS.IBOR.ECONOMIC.BUCKETS.RESERVED8` | `FsIborEconomicBuckets_Reserved8` | TField |  |  |
| 7 | `FS.IBOR.ECONOMIC.BUCKETS.RESERVED7` | `FsIborEconomicBuckets_Reserved7` | TField |  |  |
| 8 | `FS.IBOR.ECONOMIC.BUCKETS.RESERVED6` | `FsIborEconomicBuckets_Reserved6` | TField |  |  |
| 9 | `FS.IBOR.ECONOMIC.BUCKETS.RESERVED5` | `FsIborEconomicBuckets_Reserved5` | TField |  |  |
| 10 | `FS.IBOR.ECONOMIC.BUCKETS.RESERVED4` | `FsIborEconomicBuckets_Reserved4` | TField |  |  |
| 11 | `FS.IBOR.ECONOMIC.BUCKETS.RESERVED3` | `FsIborEconomicBuckets_Reserved3` | TField |  |  |
| 12 | `FS.IBOR.ECONOMIC.BUCKETS.RESERVED2` | `FsIborEconomicBuckets_Reserved2` | TField |  |  |
| 13 | `FS.IBOR.ECONOMIC.BUCKETS.RESERVED1` | `FsIborEconomicBuckets_Reserved1` | TField |  |  |
| 14 | `FS.IBOR.ECONOMIC.BUCKETS.LOCAL.REF` | `FsIborEconomicBuckets_LocalRef` |  |  |  |
| 15 | `FS.IBOR.ECONOMIC.BUCKETS.OVERRIDE` | `FsIborEconomicBuckets_Override` |  |  |  |
| 16 | `FS.IBOR.ECONOMIC.BUCKETS.RECORD.STATUS` | `FsIborEconomicBuckets_RecordStatus` | String |  |  |
| 17 | `FS.IBOR.ECONOMIC.BUCKETS.CURR.NO` | `FsIborEconomicBuckets_CurrNo` | String |  |  |
| 18 | `FS.IBOR.ECONOMIC.BUCKETS.INPUTTER` | `FsIborEconomicBuckets_Inputter` |  |  |  |
| 19 | `FS.IBOR.ECONOMIC.BUCKETS.DATE.TIME` | `FsIborEconomicBuckets_DateTime` |  |  |  |
| 20 | `FS.IBOR.ECONOMIC.BUCKETS.AUTHORISER` | `FsIborEconomicBuckets_Authoriser` | String |  |  |
| 21 | `FS.IBOR.ECONOMIC.BUCKETS.CO.CODE` | `FsIborEconomicBuckets_CoCode` | String |  |  |
| 22 | `FS.IBOR.ECONOMIC.BUCKETS.DEPT.CODE` | `FsIborEconomicBuckets_DeptCode` | String |  |  |
| 23 | `FS.IBOR.ECONOMIC.BUCKETS.AUDITOR.CODE` | `FsIborEconomicBuckets_AuditorCode` | String |  |  |
| 24 | `FS.IBOR.ECONOMIC.BUCKETS.AUDIT.DATE.TIME` | `FsIborEconomicBuckets_AuditDateTime` | String |  |  |
