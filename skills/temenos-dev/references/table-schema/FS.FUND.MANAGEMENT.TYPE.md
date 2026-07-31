# FS.FUND.MANAGEMENT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.FUND.MANAGEMENT.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.FUND.MANAGEMENT.TYPE.DESCRIPTION` | `FsFundManagementType_Description` |  |  |  |
| 2 | `FS.FUND.MANAGEMENT.TYPE.FILTER.KEY` | `FsFundManagementType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.FUND.MANAGEMENT.TYPE.RECORD.ID` | `FsFundManagementType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.FUND.MANAGEMENT.TYPE.RESERVED10` | `FsFundManagementType_Reserved10` | TField |  |  |
| 5 | `FS.FUND.MANAGEMENT.TYPE.RESERVED9` | `FsFundManagementType_Reserved9` | TField |  |  |
| 6 | `FS.FUND.MANAGEMENT.TYPE.RESERVED8` | `FsFundManagementType_Reserved8` | TField |  |  |
| 7 | `FS.FUND.MANAGEMENT.TYPE.RESERVED7` | `FsFundManagementType_Reserved7` | TField |  |  |
| 8 | `FS.FUND.MANAGEMENT.TYPE.RESERVED6` | `FsFundManagementType_Reserved6` | TField |  |  |
| 9 | `FS.FUND.MANAGEMENT.TYPE.RESERVED5` | `FsFundManagementType_Reserved5` | TField |  |  |
| 10 | `FS.FUND.MANAGEMENT.TYPE.RESERVED4` | `FsFundManagementType_Reserved4` | TField |  |  |
| 11 | `FS.FUND.MANAGEMENT.TYPE.RESERVED3` | `FsFundManagementType_Reserved3` | TField |  |  |
| 12 | `FS.FUND.MANAGEMENT.TYPE.RESERVED2` | `FsFundManagementType_Reserved2` | TField |  |  |
| 13 | `FS.FUND.MANAGEMENT.TYPE.RESERVED1` | `FsFundManagementType_Reserved1` | TField |  |  |
| 14 | `FS.FUND.MANAGEMENT.TYPE.LOCAL.REF` | `FsFundManagementType_LocalRef` |  |  |  |
| 15 | `FS.FUND.MANAGEMENT.TYPE.OVERRIDE` | `FsFundManagementType_Override` |  |  |  |
| 16 | `FS.FUND.MANAGEMENT.TYPE.RECORD.STATUS` | `FsFundManagementType_RecordStatus` | String |  |  |
| 17 | `FS.FUND.MANAGEMENT.TYPE.CURR.NO` | `FsFundManagementType_CurrNo` | String |  |  |
| 18 | `FS.FUND.MANAGEMENT.TYPE.INPUTTER` | `FsFundManagementType_Inputter` |  |  |  |
| 19 | `FS.FUND.MANAGEMENT.TYPE.DATE.TIME` | `FsFundManagementType_DateTime` |  |  |  |
| 20 | `FS.FUND.MANAGEMENT.TYPE.AUTHORISER` | `FsFundManagementType_Authoriser` | String |  |  |
| 21 | `FS.FUND.MANAGEMENT.TYPE.CO.CODE` | `FsFundManagementType_CoCode` | String |  |  |
| 22 | `FS.FUND.MANAGEMENT.TYPE.DEPT.CODE` | `FsFundManagementType_DeptCode` | String |  |  |
| 23 | `FS.FUND.MANAGEMENT.TYPE.AUDITOR.CODE` | `FsFundManagementType_AuditorCode` | String |  |  |
| 24 | `FS.FUND.MANAGEMENT.TYPE.AUDIT.DATE.TIME` | `FsFundManagementType_AuditDateTime` | String |  |  |
