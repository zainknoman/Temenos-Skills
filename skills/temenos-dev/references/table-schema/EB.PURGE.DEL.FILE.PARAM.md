# EB.PURGE.DEL.FILE.PARAM — Table Schema

> Source: `INSERTS/I_F.EB.PURGE.DEL.FILE.PARAM` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DEL.APPLICATION.NAME` | `EbPurgeDelFileParam_ApplicationName` |  |  |  |
| 2 | `EB.DEL.PURGE.DATE` | `EbPurgeDelFileParam_PurgeDate` | TField |  | Purges the record, older then the date specified in the PURGE.DATE field." |
| 3 | `EB.DEL.RESERVED.10` | `EbPurgeDelFileParam_Reserved10` | TField |  |  |
| 4 | `EB.DEL.RESERVED.9` | `EbPurgeDelFileParam_Reserved9` | TField |  |  |
| 5 | `EB.DEL.RESERVED.8` | `EbPurgeDelFileParam_Reserved8` | TField |  |  |
| 6 | `EB.DEL.RESERVED.7` | `EbPurgeDelFileParam_Reserved7` | TField |  |  |
| 7 | `EB.DEL.RESERVED.6` | `EbPurgeDelFileParam_Reserved6` | TField |  |  |
| 8 | `EB.DEL.RESERVED.5` | `EbPurgeDelFileParam_Reserved5` | TField |  |  |
| 9 | `EB.DEL.RESERVED.4` | `EbPurgeDelFileParam_Reserved4` | TField |  |  |
| 10 | `EB.DEL.RESERVED.3` | `EbPurgeDelFileParam_Reserved3` | TField |  |  |
| 11 | `EB.DEL.RESERVED.2` | `EbPurgeDelFileParam_Reserved2` | TField |  |  |
| 12 | `EB.DEL.RESERVED.1` | `EbPurgeDelFileParam_Reserved1` | TField |  |  |
| 13 | `EB.DEL.RECORD.STATUS` | `EbPurgeDelFileParam_RecordStatus` | String |  |  |
| 14 | `EB.DEL.CURR.NO` | `EbPurgeDelFileParam_CurrNo` | String |  |  |
| 15 | `EB.DEL.INPUTTER` | `EbPurgeDelFileParam_Inputter` |  |  |  |
| 16 | `EB.DEL.DATE.TIME` | `EbPurgeDelFileParam_DateTime` |  |  |  |
| 17 | `EB.DEL.AUTHORISER` | `EbPurgeDelFileParam_Authoriser` | String |  |  |
| 18 | `EB.DEL.CO.CODE` | `EbPurgeDelFileParam_CoCode` | String |  |  |
| 19 | `EB.DEL.DEPT.CODE` | `EbPurgeDelFileParam_DeptCode` | String |  |  |
| 20 | `EB.DEL.AUDITOR.CODE` | `EbPurgeDelFileParam_AuditorCode` | String |  |  |
| 21 | `EB.DEL.AUDIT.DATE.TIME` | `EbPurgeDelFileParam_AuditDateTime` | String |  |  |
