# TSA.SERVICES.COB — Table Schema

> Source: `INSERTS/I_F.TSA.SERVICES.COB` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TSS.COB.DESCRIPTION` | `TsaServicesCob_Description` |  |  |  |
| 2 | `TSS.COB.COB.STAGE` | `TsaServicesCob_CobStage` |  |  |  |
| 3 | `TSS.COB.OPERATION.MODE` | `TsaServicesCob_OperationMode` |  |  |  |
| 4 | `TSS.COB.SERVER.NAME` | `TsaServicesCob_ServerName` |  |  |  |
| 5 | `TSS.COB.WORK.PROFILE` | `TsaServicesCob_WorkProfile` |  |  |  |
| 6 | `TSS.COB.RESERVED.10` | `TsaServicesCob_Reserved10` |  |  |  |
| 7 | `TSS.COB.RESERVED.9` | `TsaServicesCob_Reserved9` |  |  |  |
| 8 | `TSS.COB.RESERVED.8` | `TsaServicesCob_Reserved8` |  |  |  |
| 9 | `TSS.COB.RESERVED.7` | `TsaServicesCob_Reserved7` |  |  |  |
| 10 | `TSS.COB.RESERVED.6` | `TsaServicesCob_Reserved6` |  |  |  |
| 11 | `TSS.COB.RESERVED.5` | `TsaServicesCob_Reserved5` |  |  |  |
| 12 | `TSS.COB.RESERVED.4` | `TsaServicesCob_Reserved4` | TField |  |  |
| 13 | `TSS.COB.RESERVED.3` | `TsaServicesCob_Reserved3` | TField |  |  |
| 14 | `TSS.COB.RESERVED.2` | `TsaServicesCob_Reserved2` | TField |  |  |
| 15 | `TSS.COB.RESERVED.1` | `TsaServicesCob_Reserved1` | TField |  |  |
| 16 | `TSS.COB.LOCAL.REF` | `TsaServicesCob_LocalRef` |  |  |  |
| 17 | `TSS.COB.OVERRIDE` | `TsaServicesCob_Override` |  |  |  |
| 18 | `TSS.COB.RECORD.STATUS` | `TsaServicesCob_RecordStatus` | String |  |  |
| 19 | `TSS.COB.CURR.NO` | `TsaServicesCob_CurrNo` | String |  |  |
| 20 | `TSS.COB.INPUTTER` | `TsaServicesCob_Inputter` |  |  |  |
| 21 | `TSS.COB.DATE.TIME` | `TsaServicesCob_DateTime` |  |  |  |
| 22 | `TSS.COB.AUTHORISER` | `TsaServicesCob_Authoriser` | String |  |  |
| 23 | `TSS.COB.CO.CODE` | `TsaServicesCob_CoCode` | String |  |  |
| 24 | `TSS.COB.DEPT.CODE` | `TsaServicesCob_DeptCode` | String |  |  |
| 25 | `TSS.COB.AUDITOR.CODE` | `TsaServicesCob_AuditorCode` | String |  |  |
| 26 | `TSS.COB.AUDIT.DATE.TIME` | `TsaServicesCob_AuditDateTime` | String |  |  |
