# DFE.RESPONSE.CODE — Table Schema

> Source: `INSERTS/I_F.DFE.RESPONSE.CODE` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DFE.RC.DESCRIPTION` | `DfeResponseCode_Description` |  |  |  |
| 2 | `DFE.RC.ENTRY.OVERRIDE` | `DfeResponseCode_EntryOverride` |  |  |  |
| 3 | `DFE.RC.RETURN.CODE` | `DfeResponseCode_ReturnCode` |  |  |  |
| 4 | `DFE.RC.RETURN.REASON` | `DfeResponseCode_ReturnReason` |  |  |  |
| 5 | `DFE.RC.RESERVED.15` | `DfeResponseCode_Reserved15` |  |  |  |
| 6 | `DFE.RC.RESERVED.14` | `DfeResponseCode_Reserved14` |  |  |  |
| 7 | `DFE.RC.RESERVED.13` | `DfeResponseCode_Reserved13` |  |  |  |
| 8 | `DFE.RC.RESERVED.12` | `DfeResponseCode_Reserved12` |  |  |  |
| 9 | `DFE.RC.RESERVED.11` | `DfeResponseCode_Reserved11` |  |  |  |
| 10 | `DFE.RC.RESERVED.10` | `DfeResponseCode_Reserved10` | TField |  |  |
| 11 | `DFE.RC.RESERVED.9` | `DfeResponseCode_Reserved9` | TField |  |  |
| 12 | `DFE.RC.RESERVED.8` | `DfeResponseCode_Reserved8` | TField |  |  |
| 13 | `DFE.RC.RESERVED.7` | `DfeResponseCode_Reserved7` | TField |  |  |
| 14 | `DFE.RC.RESERVED.6` | `DfeResponseCode_Reserved6` | TField |  |  |
| 15 | `DFE.RC.RESERVED.5` | `DfeResponseCode_Reserved5` | TField |  |  |
| 16 | `DFE.RC.RESERVED.4` | `DfeResponseCode_Reserved4` | TField |  |  |
| 17 | `DFE.RC.RESERVED.3` | `DfeResponseCode_Reserved3` | TField |  |  |
| 18 | `DFE.RC.RESERVED.2` | `DfeResponseCode_Reserved2` | TField |  |  |
| 19 | `DFE.RC.RESERVED.1` | `DfeResponseCode_Reserved1` | TField |  |  |
| 20 | `DFE.RC.LOCAL.REF` | `DfeResponseCode_LocalRef` |  |  |  |
| 21 | `DFE.RC.OVERRIDE` | `DfeResponseCode_Override` |  |  |  |
| 22 | `DFE.RC.RECORD.STATUS` | `DfeResponseCode_RecordStatus` | String |  |  |
| 23 | `DFE.RC.CURR.NO` | `DfeResponseCode_CurrNo` | String |  |  |
| 24 | `DFE.RC.INPUTTER` | `DfeResponseCode_Inputter` |  |  |  |
| 25 | `DFE.RC.DATE.TIME` | `DfeResponseCode_DateTime` |  |  |  |
| 26 | `DFE.RC.AUTHORISER` | `DfeResponseCode_Authoriser` | String |  |  |
| 27 | `DFE.RC.CO.CODE` | `DfeResponseCode_CoCode` | String |  |  |
| 28 | `DFE.RC.DEPT.CODE` | `DfeResponseCode_DeptCode` | String |  |  |
| 29 | `DFE.RC.AUDITOR.CODE` | `DfeResponseCode_AuditorCode` | String |  |  |
| 30 | `DFE.RC.AUDIT.DATE.TIME` | `DfeResponseCode_AuditDateTime` | String |  |  |
