# FS.RISK.CODE — Table Schema

> Source: `INSERTS/I_F.FS.RISK.CODE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.RISK.CODE.DESCRIPTION` | `FsRiskCode_Description` |  |  |  |
| 2 | `FS.RISK.CODE.FILTER.KEY` | `FsRiskCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.RISK.CODE.RECORD.ID` | `FsRiskCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.RISK.CODE.RESERVED10` | `FsRiskCode_Reserved10` | TField |  |  |
| 5 | `FS.RISK.CODE.RESERVED9` | `FsRiskCode_Reserved9` | TField |  |  |
| 6 | `FS.RISK.CODE.RESERVED8` | `FsRiskCode_Reserved8` | TField |  |  |
| 7 | `FS.RISK.CODE.RESERVED7` | `FsRiskCode_Reserved7` | TField |  |  |
| 8 | `FS.RISK.CODE.RESERVED6` | `FsRiskCode_Reserved6` | TField |  |  |
| 9 | `FS.RISK.CODE.RESERVED5` | `FsRiskCode_Reserved5` | TField |  |  |
| 10 | `FS.RISK.CODE.RESERVED4` | `FsRiskCode_Reserved4` | TField |  |  |
| 11 | `FS.RISK.CODE.RESERVED3` | `FsRiskCode_Reserved3` | TField |  |  |
| 12 | `FS.RISK.CODE.RESERVED2` | `FsRiskCode_Reserved2` | TField |  |  |
| 13 | `FS.RISK.CODE.RESERVED1` | `FsRiskCode_Reserved1` | TField |  |  |
| 14 | `FS.RISK.CODE.LOCAL.REF` | `FsRiskCode_LocalRef` |  |  |  |
| 15 | `FS.RISK.CODE.OVERRIDE` | `FsRiskCode_Override` |  |  |  |
| 16 | `FS.RISK.CODE.RECORD.STATUS` | `FsRiskCode_RecordStatus` | String |  |  |
| 17 | `FS.RISK.CODE.CURR.NO` | `FsRiskCode_CurrNo` | String |  |  |
| 18 | `FS.RISK.CODE.INPUTTER` | `FsRiskCode_Inputter` |  |  |  |
| 19 | `FS.RISK.CODE.DATE.TIME` | `FsRiskCode_DateTime` |  |  |  |
| 20 | `FS.RISK.CODE.AUTHORISER` | `FsRiskCode_Authoriser` | String |  |  |
| 21 | `FS.RISK.CODE.CO.CODE` | `FsRiskCode_CoCode` | String |  |  |
| 22 | `FS.RISK.CODE.DEPT.CODE` | `FsRiskCode_DeptCode` | String |  |  |
| 23 | `FS.RISK.CODE.AUDITOR.CODE` | `FsRiskCode_AuditorCode` | String |  |  |
| 24 | `FS.RISK.CODE.AUDIT.DATE.TIME` | `FsRiskCode_AuditDateTime` | String |  |  |
