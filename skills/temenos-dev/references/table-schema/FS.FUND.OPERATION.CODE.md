# FS.FUND.OPERATION.CODE — Table Schema

> Source: `INSERTS/I_F.FS.FUND.OPERATION.CODE` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.FUND.OPERATION.CODE.DESCRIPTION` | `FsFundOperationCode_Description` |  |  |  |
| 2 | `FS.FUND.OPERATION.CODE.FILTER.KEY` | `FsFundOperationCode_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.FUND.OPERATION.CODE.RECORD.ID` | `FsFundOperationCode_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.FUND.OPERATION.CODE.RESERVED10` | `FsFundOperationCode_Reserved10` | TField |  |  |
| 5 | `FS.FUND.OPERATION.CODE.RESERVED9` | `FsFundOperationCode_Reserved9` | TField |  |  |
| 6 | `FS.FUND.OPERATION.CODE.RESERVED8` | `FsFundOperationCode_Reserved8` | TField |  |  |
| 7 | `FS.FUND.OPERATION.CODE.RESERVED7` | `FsFundOperationCode_Reserved7` | TField |  |  |
| 8 | `FS.FUND.OPERATION.CODE.RESERVED6` | `FsFundOperationCode_Reserved6` | TField |  |  |
| 9 | `FS.FUND.OPERATION.CODE.RESERVED5` | `FsFundOperationCode_Reserved5` | TField |  |  |
| 10 | `FS.FUND.OPERATION.CODE.RESERVED4` | `FsFundOperationCode_Reserved4` | TField |  |  |
| 11 | `FS.FUND.OPERATION.CODE.RESERVED3` | `FsFundOperationCode_Reserved3` | TField |  |  |
| 12 | `FS.FUND.OPERATION.CODE.RESERVED2` | `FsFundOperationCode_Reserved2` | TField |  |  |
| 13 | `FS.FUND.OPERATION.CODE.RESERVED1` | `FsFundOperationCode_Reserved1` | TField |  |  |
| 14 | `FS.FUND.OPERATION.CODE.LOCAL.REF` | `FsFundOperationCode_LocalRef` |  |  |  |
| 15 | `FS.FUND.OPERATION.CODE.OVERRIDE` | `FsFundOperationCode_Override` |  |  |  |
| 16 | `FS.FUND.OPERATION.CODE.RECORD.STATUS` | `FsFundOperationCode_RecordStatus` | String |  |  |
| 17 | `FS.FUND.OPERATION.CODE.CURR.NO` | `FsFundOperationCode_CurrNo` | String |  |  |
| 18 | `FS.FUND.OPERATION.CODE.INPUTTER` | `FsFundOperationCode_Inputter` |  |  |  |
| 19 | `FS.FUND.OPERATION.CODE.DATE.TIME` | `FsFundOperationCode_DateTime` |  |  |  |
| 20 | `FS.FUND.OPERATION.CODE.AUTHORISER` | `FsFundOperationCode_Authoriser` | String |  |  |
| 21 | `FS.FUND.OPERATION.CODE.CO.CODE` | `FsFundOperationCode_CoCode` | String |  |  |
| 22 | `FS.FUND.OPERATION.CODE.DEPT.CODE` | `FsFundOperationCode_DeptCode` | String |  |  |
| 23 | `FS.FUND.OPERATION.CODE.AUDITOR.CODE` | `FsFundOperationCode_AuditorCode` | String |  |  |
| 24 | `FS.FUND.OPERATION.CODE.AUDIT.DATE.TIME` | `FsFundOperationCode_AuditDateTime` | String |  |  |
