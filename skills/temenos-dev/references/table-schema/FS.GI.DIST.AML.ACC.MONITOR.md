# FS.GI.DIST.AML.ACC.MONITOR — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AML.ACC.MONITOR` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AML.ACC.MONITOR.PARENT.REF.ID` | `FsGiDistAmlAccMonitor_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AML.ACC.MONITOR.ORA.ROWID` | `FsGiDistAmlAccMonitor_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AML.ACC.MONITOR.PARENT.TYPE` | `FsGiDistAmlAccMonitor_ParentType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is ENTITY_TYPE. |
| 4 | `FS.GI.DIST.AML.ACC.MONITOR.PARENT.ID` | `FsGiDistAmlAccMonitor_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ENTITY_ID. |
| 5 | `FS.GI.DIST.AML.ACC.MONITOR.HIT.DATE` | `FsGiDistAmlAccMonitor_HitDate` | TField |  | Date (in DD/MM/YYYY format) when the hit encountered. Multifonds DB Column is HIT_DATE. |
| 6 | `FS.GI.DIST.AML.ACC.MONITOR.HIT.TYPE` | `FsGiDistAmlAccMonitor_HitType` | TField |  | Hit Type. Free text that allows up to 10 alphanumerical characters for hit type. Multifonds DB Column is HIT_TYPE. |
| 7 | `FS.GI.DIST.AML.ACC.MONITOR.HIT.CATEGORY` | `FsGiDistAmlAccMonitor_HitCategory` | TField |  | Hit Category. Free text that allows up to 20 alphanumerical characters for hit category. Multifonds DB Column is HIT_CATEGORY. |
| 8 | `FS.GI.DIST.AML.ACC.MONITOR.HIT.ID` | `FsGiDistAmlAccMonitor_HitId` | TField |  | Hit Identification code. Free text that allows up to 10 alphanumerical characters for hit ID. Multifonds DB Column is HIT_ID. |
| 9 | `FS.GI.DIST.AML.ACC.MONITOR.HIT.NAME` | `FsGiDistAmlAccMonitor_HitName` | TField |  | Hit Name. Free text that allows up to 40 alphanumerical characters for hit name. Multifonds DB Column is HIT_NAME. |
| 10 | `FS.GI.DIST.AML.ACC.MONITOR.HIT.ALIAS` | `FsGiDistAmlAccMonitor_HitAlias` | TField |  | Alias. Free text that allows up to 40 alphanumerical characters for hit alias name. Multifonds DB Column is HIT_ALIAS. |
| 11 | `FS.GI.DIST.AML.ACC.MONITOR.GENDER` | `FsGiDistAmlAccMonitor_Gender` | TField |  | Gender (F/M) of the related party. Multifonds DB Column is GENDER. |
| 12 | `FS.GI.DIST.AML.ACC.MONITOR.DOB` | `FsGiDistAmlAccMonitor_Dob` | TField |  | Date of birth of the related party. Multifonds DB Column is DOB. |
| 13 | `FS.GI.DIST.AML.ACC.MONITOR.COUNTRY` | `FsGiDistAmlAccMonitor_Country` | TField |  | Country code (in 2 letter ISO format). Multifonds DB Column is COUNTRY. |
| 14 | `FS.GI.DIST.AML.ACC.MONITOR.STATUS` | `FsGiDistAmlAccMonitor_Status` | TField |  | Status code. Multifonds DB Column is CSTATUS. |
| 15 | `FS.GI.DIST.AML.ACC.MONITOR.HIT.REASON` | `FsGiDistAmlAccMonitor_HitReason` | TField |  | Hit reason. Multifonds DB Column is HIT_REASON. |
| 16 | `FS.GI.DIST.AML.ACC.MONITOR.HIT.COMMENTS` | `FsGiDistAmlAccMonitor_HitComments` | TField |  | Free text comment that allows upto 150 alpha numerical characters that can be used for hit related comments. Multifonds DB Column is HIT_COMMENTS. |
| 17 | `FS.GI.DIST.AML.ACC.MONITOR.FUND.PROMOTER.ID` | `FsGiDistAmlAccMonitor_FundPromoterId` | TField |  | Fund Promoter ID linked to the client. Multifonds DB Column is NPROMOTER. |
| 18 | `FS.GI.DIST.AML.ACC.MONITOR.JURISDICTION` | `FsGiDistAmlAccMonitor_Jurisdiction` | TField |  | AML Jurisdiction of the client. Multifonds DB Column is JURISDICTION. |
| 19 | `FS.GI.DIST.AML.ACC.MONITOR.RESERVED10` | `FsGiDistAmlAccMonitor_Reserved10` | TField |  |  |
| 20 | `FS.GI.DIST.AML.ACC.MONITOR.RESERVED9` | `FsGiDistAmlAccMonitor_Reserved9` | TField |  |  |
| 21 | `FS.GI.DIST.AML.ACC.MONITOR.RESERVED8` | `FsGiDistAmlAccMonitor_Reserved8` | TField |  |  |
| 22 | `FS.GI.DIST.AML.ACC.MONITOR.RESERVED7` | `FsGiDistAmlAccMonitor_Reserved7` | TField |  |  |
| 23 | `FS.GI.DIST.AML.ACC.MONITOR.RESERVED6` | `FsGiDistAmlAccMonitor_Reserved6` | TField |  |  |
| 24 | `FS.GI.DIST.AML.ACC.MONITOR.RESERVED5` | `FsGiDistAmlAccMonitor_Reserved5` | TField |  |  |
| 25 | `FS.GI.DIST.AML.ACC.MONITOR.RESERVED4` | `FsGiDistAmlAccMonitor_Reserved4` | TField |  |  |
| 26 | `FS.GI.DIST.AML.ACC.MONITOR.RESERVED3` | `FsGiDistAmlAccMonitor_Reserved3` | TField |  |  |
| 27 | `FS.GI.DIST.AML.ACC.MONITOR.RESERVED2` | `FsGiDistAmlAccMonitor_Reserved2` | TField |  |  |
| 28 | `FS.GI.DIST.AML.ACC.MONITOR.RESERVED1` | `FsGiDistAmlAccMonitor_Reserved1` | TField |  |  |
| 29 | `FS.GI.DIST.AML.ACC.MONITOR.LOCAL.REF` | `FsGiDistAmlAccMonitor_LocalRef` |  |  |  |
| 30 | `FS.GI.DIST.AML.ACC.MONITOR.OVERRIDE` | `FsGiDistAmlAccMonitor_Override` |  |  |  |
| 31 | `FS.GI.DIST.AML.ACC.MONITOR.RECORD.STATUS` | `FsGiDistAmlAccMonitor_RecordStatus` | String |  |  |
| 32 | `FS.GI.DIST.AML.ACC.MONITOR.CURR.NO` | `FsGiDistAmlAccMonitor_CurrNo` | String |  |  |
| 33 | `FS.GI.DIST.AML.ACC.MONITOR.INPUTTER` | `FsGiDistAmlAccMonitor_Inputter` |  |  |  |
| 34 | `FS.GI.DIST.AML.ACC.MONITOR.DATE.TIME` | `FsGiDistAmlAccMonitor_DateTime` |  |  |  |
| 35 | `FS.GI.DIST.AML.ACC.MONITOR.AUTHORISER` | `FsGiDistAmlAccMonitor_Authoriser` | String |  |  |
| 36 | `FS.GI.DIST.AML.ACC.MONITOR.CO.CODE` | `FsGiDistAmlAccMonitor_CoCode` | String |  |  |
| 37 | `FS.GI.DIST.AML.ACC.MONITOR.DEPT.CODE` | `FsGiDistAmlAccMonitor_DeptCode` | String |  |  |
| 38 | `FS.GI.DIST.AML.ACC.MONITOR.AUDITOR.CODE` | `FsGiDistAmlAccMonitor_AuditorCode` | String |  |  |
| 39 | `FS.GI.DIST.AML.ACC.MONITOR.AUDIT.DATE.TIME` | `FsGiDistAmlAccMonitor_AuditDateTime` | String |  |  |
