# FS.GI.FUND.TRNS.LIMIT.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.TRNS.LIMIT.MASTER` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.TRNS.LIMIT.MASTER.PARENT.REF.ID` | `FsGiFundTrnsLimitMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.TRNS.LIMIT.MASTER.ORA.ROWID` | `FsGiFundTrnsLimitMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.TRNS.LIMIT.MASTER.FUND.ID` | `FsGiFundTrnsLimitMaster_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.TRNS.LIMIT.MASTER.LIMIT.CURRENCY` | `FsGiFundTrnsLimitMaster_LimitCurrency` | TField |  | Transaction limit currency code (in 3 letter ISO code, Eg: EUR). Multifonds DB Column is CMON_LIMIT. |
| 5 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RESERVED10` | `FsGiFundTrnsLimitMaster_Reserved10` | TField |  |  |
| 6 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RESERVED9` | `FsGiFundTrnsLimitMaster_Reserved9` | TField |  |  |
| 7 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RESERVED8` | `FsGiFundTrnsLimitMaster_Reserved8` | TField |  |  |
| 8 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RESERVED7` | `FsGiFundTrnsLimitMaster_Reserved7` | TField |  |  |
| 9 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RESERVED6` | `FsGiFundTrnsLimitMaster_Reserved6` | TField |  |  |
| 10 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RESERVED5` | `FsGiFundTrnsLimitMaster_Reserved5` | TField |  |  |
| 11 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RESERVED4` | `FsGiFundTrnsLimitMaster_Reserved4` | TField |  |  |
| 12 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RESERVED3` | `FsGiFundTrnsLimitMaster_Reserved3` | TField |  |  |
| 13 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RESERVED2` | `FsGiFundTrnsLimitMaster_Reserved2` | TField |  |  |
| 14 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RESERVED1` | `FsGiFundTrnsLimitMaster_Reserved1` | TField |  |  |
| 15 | `FS.GI.FUND.TRNS.LIMIT.MASTER.LOCAL.REF` | `FsGiFundTrnsLimitMaster_LocalRef` |  |  |  |
| 16 | `FS.GI.FUND.TRNS.LIMIT.MASTER.OVERRIDE` | `FsGiFundTrnsLimitMaster_Override` |  |  |  |
| 17 | `FS.GI.FUND.TRNS.LIMIT.MASTER.RECORD.STATUS` | `FsGiFundTrnsLimitMaster_RecordStatus` | String |  |  |
| 18 | `FS.GI.FUND.TRNS.LIMIT.MASTER.CURR.NO` | `FsGiFundTrnsLimitMaster_CurrNo` | String |  |  |
| 19 | `FS.GI.FUND.TRNS.LIMIT.MASTER.INPUTTER` | `FsGiFundTrnsLimitMaster_Inputter` |  |  |  |
| 20 | `FS.GI.FUND.TRNS.LIMIT.MASTER.DATE.TIME` | `FsGiFundTrnsLimitMaster_DateTime` |  |  |  |
| 21 | `FS.GI.FUND.TRNS.LIMIT.MASTER.AUTHORISER` | `FsGiFundTrnsLimitMaster_Authoriser` | String |  |  |
| 22 | `FS.GI.FUND.TRNS.LIMIT.MASTER.CO.CODE` | `FsGiFundTrnsLimitMaster_CoCode` | String |  |  |
| 23 | `FS.GI.FUND.TRNS.LIMIT.MASTER.DEPT.CODE` | `FsGiFundTrnsLimitMaster_DeptCode` | String |  |  |
| 24 | `FS.GI.FUND.TRNS.LIMIT.MASTER.AUDITOR.CODE` | `FsGiFundTrnsLimitMaster_AuditorCode` | String |  |  |
| 25 | `FS.GI.FUND.TRNS.LIMIT.MASTER.AUDIT.DATE.TIME` | `FsGiFundTrnsLimitMaster_AuditDateTime` | String |  |  |
