# FS.GI.APP.RESPONSE — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.RESPONSE` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.RESPONSE.PARENT.REF.ID` | `FsGiAppResponse_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.RESPONSE.ORA.ROWID` | `FsGiAppResponse_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.RESPONSE.PARENT.TYPE` | `FsGiAppResponse_ParentType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.APP.RESPONSE.PARENT.ID` | `FsGiAppResponse_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.APP.RESPONSE.NAME` | `FsGiAppResponse_Name` | TField |  | Profile role name. Multifonds DB Column is NAME. |
| 6 | `FS.GI.APP.RESPONSE.FIRSTNAME` | `FsGiAppResponse_Firstname` | TField |  | Profile role first name. Multifonds DB Column is FIRST_NAME. |
| 7 | `FS.GI.APP.RESPONSE.QUESTION` | `FsGiAppResponse_Question` | TField |  | Profile role security question Multifonds DB Column is QUESTION. |
| 8 | `FS.GI.APP.RESPONSE.RESPONSE` | `FsGiAppResponse_Response` | TField |  | Response to the security question Multifonds DB Column is RESPONSE. |
| 9 | `FS.GI.APP.RESPONSE.RESERVED10` | `FsGiAppResponse_Reserved10` | TField |  |  |
| 10 | `FS.GI.APP.RESPONSE.RESERVED9` | `FsGiAppResponse_Reserved9` | TField |  |  |
| 11 | `FS.GI.APP.RESPONSE.RESERVED8` | `FsGiAppResponse_Reserved8` | TField |  |  |
| 12 | `FS.GI.APP.RESPONSE.RESERVED7` | `FsGiAppResponse_Reserved7` | TField |  |  |
| 13 | `FS.GI.APP.RESPONSE.RESERVED6` | `FsGiAppResponse_Reserved6` | TField |  |  |
| 14 | `FS.GI.APP.RESPONSE.RESERVED5` | `FsGiAppResponse_Reserved5` | TField |  |  |
| 15 | `FS.GI.APP.RESPONSE.RESERVED4` | `FsGiAppResponse_Reserved4` | TField |  |  |
| 16 | `FS.GI.APP.RESPONSE.RESERVED3` | `FsGiAppResponse_Reserved3` | TField |  |  |
| 17 | `FS.GI.APP.RESPONSE.RESERVED2` | `FsGiAppResponse_Reserved2` | TField |  |  |
| 18 | `FS.GI.APP.RESPONSE.RESERVED1` | `FsGiAppResponse_Reserved1` | TField |  |  |
| 19 | `FS.GI.APP.RESPONSE.LOCAL.REF` | `FsGiAppResponse_LocalRef` |  |  |  |
| 20 | `FS.GI.APP.RESPONSE.OVERRIDE` | `FsGiAppResponse_Override` |  |  |  |
| 21 | `FS.GI.APP.RESPONSE.RECORD.STATUS` | `FsGiAppResponse_RecordStatus` | String |  |  |
| 22 | `FS.GI.APP.RESPONSE.CURR.NO` | `FsGiAppResponse_CurrNo` | String |  |  |
| 23 | `FS.GI.APP.RESPONSE.INPUTTER` | `FsGiAppResponse_Inputter` |  |  |  |
| 24 | `FS.GI.APP.RESPONSE.DATE.TIME` | `FsGiAppResponse_DateTime` |  |  |  |
| 25 | `FS.GI.APP.RESPONSE.AUTHORISER` | `FsGiAppResponse_Authoriser` | String |  |  |
| 26 | `FS.GI.APP.RESPONSE.CO.CODE` | `FsGiAppResponse_CoCode` | String |  |  |
| 27 | `FS.GI.APP.RESPONSE.DEPT.CODE` | `FsGiAppResponse_DeptCode` | String |  |  |
| 28 | `FS.GI.APP.RESPONSE.AUDITOR.CODE` | `FsGiAppResponse_AuditorCode` | String |  |  |
| 29 | `FS.GI.APP.RESPONSE.AUDIT.DATE.TIME` | `FsGiAppResponse_AuditDateTime` | String |  |  |
