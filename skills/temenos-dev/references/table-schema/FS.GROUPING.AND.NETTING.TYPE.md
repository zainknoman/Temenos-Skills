# FS.GROUPING.AND.NETTING.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.GROUPING.AND.NETTING.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GROUPING.AND.NETTING.TYPE.DESCRIPTION` | `FsGroupingAndNettingType_Description` |  |  |  |
| 2 | `FS.GROUPING.AND.NETTING.TYPE.FILTER.KEY` | `FsGroupingAndNettingType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.GROUPING.AND.NETTING.TYPE.RECORD.ID` | `FsGroupingAndNettingType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.GROUPING.AND.NETTING.TYPE.RESERVED10` | `FsGroupingAndNettingType_Reserved10` | TField |  |  |
| 5 | `FS.GROUPING.AND.NETTING.TYPE.RESERVED9` | `FsGroupingAndNettingType_Reserved9` | TField |  |  |
| 6 | `FS.GROUPING.AND.NETTING.TYPE.RESERVED8` | `FsGroupingAndNettingType_Reserved8` | TField |  |  |
| 7 | `FS.GROUPING.AND.NETTING.TYPE.RESERVED7` | `FsGroupingAndNettingType_Reserved7` | TField |  |  |
| 8 | `FS.GROUPING.AND.NETTING.TYPE.RESERVED6` | `FsGroupingAndNettingType_Reserved6` | TField |  |  |
| 9 | `FS.GROUPING.AND.NETTING.TYPE.RESERVED5` | `FsGroupingAndNettingType_Reserved5` | TField |  |  |
| 10 | `FS.GROUPING.AND.NETTING.TYPE.RESERVED4` | `FsGroupingAndNettingType_Reserved4` | TField |  |  |
| 11 | `FS.GROUPING.AND.NETTING.TYPE.RESERVED3` | `FsGroupingAndNettingType_Reserved3` | TField |  |  |
| 12 | `FS.GROUPING.AND.NETTING.TYPE.RESERVED2` | `FsGroupingAndNettingType_Reserved2` | TField |  |  |
| 13 | `FS.GROUPING.AND.NETTING.TYPE.RESERVED1` | `FsGroupingAndNettingType_Reserved1` | TField |  |  |
| 14 | `FS.GROUPING.AND.NETTING.TYPE.LOCAL.REF` | `FsGroupingAndNettingType_LocalRef` |  |  |  |
| 15 | `FS.GROUPING.AND.NETTING.TYPE.OVERRIDE` | `FsGroupingAndNettingType_Override` |  |  |  |
| 16 | `FS.GROUPING.AND.NETTING.TYPE.RECORD.STATUS` | `FsGroupingAndNettingType_RecordStatus` | String |  |  |
| 17 | `FS.GROUPING.AND.NETTING.TYPE.CURR.NO` | `FsGroupingAndNettingType_CurrNo` | String |  |  |
| 18 | `FS.GROUPING.AND.NETTING.TYPE.INPUTTER` | `FsGroupingAndNettingType_Inputter` |  |  |  |
| 19 | `FS.GROUPING.AND.NETTING.TYPE.DATE.TIME` | `FsGroupingAndNettingType_DateTime` |  |  |  |
| 20 | `FS.GROUPING.AND.NETTING.TYPE.AUTHORISER` | `FsGroupingAndNettingType_Authoriser` | String |  |  |
| 21 | `FS.GROUPING.AND.NETTING.TYPE.CO.CODE` | `FsGroupingAndNettingType_CoCode` | String |  |  |
| 22 | `FS.GROUPING.AND.NETTING.TYPE.DEPT.CODE` | `FsGroupingAndNettingType_DeptCode` | String |  |  |
| 23 | `FS.GROUPING.AND.NETTING.TYPE.AUDITOR.CODE` | `FsGroupingAndNettingType_AuditorCode` | String |  |  |
| 24 | `FS.GROUPING.AND.NETTING.TYPE.AUDIT.DATE.TIME` | `FsGroupingAndNettingType_AuditDateTime` | String |  |  |
