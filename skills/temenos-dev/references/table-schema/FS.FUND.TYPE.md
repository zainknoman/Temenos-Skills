# FS.FUND.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.FUND.TYPE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.FUND.TYPE.DESCRIPTION` | `FsFundType_Description` |  |  |  |
| 2 | `FS.FUND.TYPE.FILTER.KEY` | `FsFundType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.FUND.TYPE.RECORD.ID` | `FsFundType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.FUND.TYPE.RESERVED10` | `FsFundType_Reserved10` | TField |  |  |
| 5 | `FS.FUND.TYPE.RESERVED9` | `FsFundType_Reserved9` | TField |  |  |
| 6 | `FS.FUND.TYPE.RESERVED8` | `FsFundType_Reserved8` | TField |  |  |
| 7 | `FS.FUND.TYPE.RESERVED7` | `FsFundType_Reserved7` | TField |  |  |
| 8 | `FS.FUND.TYPE.RESERVED6` | `FsFundType_Reserved6` | TField |  |  |
| 9 | `FS.FUND.TYPE.RESERVED5` | `FsFundType_Reserved5` | TField |  |  |
| 10 | `FS.FUND.TYPE.RESERVED4` | `FsFundType_Reserved4` | TField |  |  |
| 11 | `FS.FUND.TYPE.RESERVED3` | `FsFundType_Reserved3` | TField |  |  |
| 12 | `FS.FUND.TYPE.RESERVED2` | `FsFundType_Reserved2` | TField |  |  |
| 13 | `FS.FUND.TYPE.RESERVED1` | `FsFundType_Reserved1` | TField |  |  |
| 14 | `FS.FUND.TYPE.LOCAL.REF` | `FsFundType_LocalRef` |  |  |  |
| 15 | `FS.FUND.TYPE.OVERRIDE` | `FsFundType_Override` |  |  |  |
| 16 | `FS.FUND.TYPE.RECORD.STATUS` | `FsFundType_RecordStatus` | String |  |  |
| 17 | `FS.FUND.TYPE.CURR.NO` | `FsFundType_CurrNo` | String |  |  |
| 18 | `FS.FUND.TYPE.INPUTTER` | `FsFundType_Inputter` |  |  |  |
| 19 | `FS.FUND.TYPE.DATE.TIME` | `FsFundType_DateTime` |  |  |  |
| 20 | `FS.FUND.TYPE.AUTHORISER` | `FsFundType_Authoriser` | String |  |  |
| 21 | `FS.FUND.TYPE.CO.CODE` | `FsFundType_CoCode` | String |  |  |
| 22 | `FS.FUND.TYPE.DEPT.CODE` | `FsFundType_DeptCode` | String |  |  |
| 23 | `FS.FUND.TYPE.AUDITOR.CODE` | `FsFundType_AuditorCode` | String |  |  |
| 24 | `FS.FUND.TYPE.AUDIT.DATE.TIME` | `FsFundType_AuditDateTime` | String |  |  |
