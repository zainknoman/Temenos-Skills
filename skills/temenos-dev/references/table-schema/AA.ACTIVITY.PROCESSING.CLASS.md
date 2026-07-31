# AA.ACTIVITY.PROCESSING.CLASS — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY.PROCESSING.CLASS` in `AF_ActivityProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.APCL.DESCRIPTION` | `AaActivityProcessingClass_Description` |  |  |  |
| 2 | `AA.APCL.FULL.DESC` | `AaActivityProcessingClass_FullDesc` |  |  |  |
| 3 | `AA.APCL.TYPE` | `AaActivityProcessingClass_Type` |  |  |  |
| 4 | `AA.APCL.RESERVED.10` | `AaActivityProcessingClass_Reserved10` | TField |  |  |
| 5 | `AA.APCL.RESERVED.9` | `AaActivityProcessingClass_Reserved9` | TField |  |  |
| 6 | `AA.APCL.RESERVED.8` | `AaActivityProcessingClass_Reserved8` | TField |  |  |
| 7 | `AA.APCL.RESERVED.7` | `AaActivityProcessingClass_Reserved7` | TField |  |  |
| 8 | `AA.APCL.RESERVED.6` | `AaActivityProcessingClass_Reserved6` | TField |  |  |
| 9 | `AA.APCL.RESERVED.5` | `AaActivityProcessingClass_Reserved5` | TField |  |  |
| 10 | `AA.APCL.RESERVED.4` | `AaActivityProcessingClass_Reserved4` | TField |  |  |
| 11 | `AA.APCL.RESERVED.3` | `AaActivityProcessingClass_Reserved3` | TField |  |  |
| 12 | `AA.APCL.RESERVED.2` | `AaActivityProcessingClass_Reserved2` | TField |  |  |
| 13 | `AA.APCL.RESERVED.1` | `AaActivityProcessingClass_Reserved1` | TField |  |  |
| 14 | `AA.APCL.RECORD.STATUS` | `AaActivityProcessingClass_RecordStatus` | String |  |  |
| 15 | `AA.APCL.CURR.NO` | `AaActivityProcessingClass_CurrNo` | String |  |  |
| 16 | `AA.APCL.INPUTTER` | `AaActivityProcessingClass_Inputter` |  |  |  |
| 17 | `AA.APCL.DATE.TIME` | `AaActivityProcessingClass_DateTime` |  |  |  |
| 18 | `AA.APCL.AUTHORISER` | `AaActivityProcessingClass_Authoriser` | String |  |  |
| 19 | `AA.APCL.CO.CODE` | `AaActivityProcessingClass_CoCode` | String |  |  |
| 20 | `AA.APCL.DEPT.CODE` | `AaActivityProcessingClass_DeptCode` | String |  |  |
| 21 | `AA.APCL.AUDITOR.CODE` | `AaActivityProcessingClass_AuditorCode` | String |  |  |
| 22 | `AA.APCL.AUDIT.DATE.TIME` | `AaActivityProcessingClass_AuditDateTime` | String |  |  |
