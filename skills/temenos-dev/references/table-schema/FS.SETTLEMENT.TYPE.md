# FS.SETTLEMENT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.SETTLEMENT.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.SETTLEMENT.TYPE.DESCRIPTION` | `FsSettlementType_Description` |  |  |  |
| 2 | `FS.SETTLEMENT.TYPE.FILTER.KEY` | `FsSettlementType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.SETTLEMENT.TYPE.RECORD.ID` | `FsSettlementType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.SETTLEMENT.TYPE.RESERVED10` | `FsSettlementType_Reserved10` | TField |  |  |
| 5 | `FS.SETTLEMENT.TYPE.RESERVED9` | `FsSettlementType_Reserved9` | TField |  |  |
| 6 | `FS.SETTLEMENT.TYPE.RESERVED8` | `FsSettlementType_Reserved8` | TField |  |  |
| 7 | `FS.SETTLEMENT.TYPE.RESERVED7` | `FsSettlementType_Reserved7` | TField |  |  |
| 8 | `FS.SETTLEMENT.TYPE.RESERVED6` | `FsSettlementType_Reserved6` | TField |  |  |
| 9 | `FS.SETTLEMENT.TYPE.RESERVED5` | `FsSettlementType_Reserved5` | TField |  |  |
| 10 | `FS.SETTLEMENT.TYPE.RESERVED4` | `FsSettlementType_Reserved4` | TField |  |  |
| 11 | `FS.SETTLEMENT.TYPE.RESERVED3` | `FsSettlementType_Reserved3` | TField |  |  |
| 12 | `FS.SETTLEMENT.TYPE.RESERVED2` | `FsSettlementType_Reserved2` | TField |  |  |
| 13 | `FS.SETTLEMENT.TYPE.RESERVED1` | `FsSettlementType_Reserved1` | TField |  |  |
| 14 | `FS.SETTLEMENT.TYPE.LOCAL.REF` | `FsSettlementType_LocalRef` |  |  |  |
| 15 | `FS.SETTLEMENT.TYPE.OVERRIDE` | `FsSettlementType_Override` |  |  |  |
| 16 | `FS.SETTLEMENT.TYPE.RECORD.STATUS` | `FsSettlementType_RecordStatus` | String |  |  |
| 17 | `FS.SETTLEMENT.TYPE.CURR.NO` | `FsSettlementType_CurrNo` | String |  |  |
| 18 | `FS.SETTLEMENT.TYPE.INPUTTER` | `FsSettlementType_Inputter` |  |  |  |
| 19 | `FS.SETTLEMENT.TYPE.DATE.TIME` | `FsSettlementType_DateTime` |  |  |  |
| 20 | `FS.SETTLEMENT.TYPE.AUTHORISER` | `FsSettlementType_Authoriser` | String |  |  |
| 21 | `FS.SETTLEMENT.TYPE.CO.CODE` | `FsSettlementType_CoCode` | String |  |  |
| 22 | `FS.SETTLEMENT.TYPE.DEPT.CODE` | `FsSettlementType_DeptCode` | String |  |  |
| 23 | `FS.SETTLEMENT.TYPE.AUDITOR.CODE` | `FsSettlementType_AuditorCode` | String |  |  |
| 24 | `FS.SETTLEMENT.TYPE.AUDIT.DATE.TIME` | `FsSettlementType_AuditDateTime` | String |  |  |
