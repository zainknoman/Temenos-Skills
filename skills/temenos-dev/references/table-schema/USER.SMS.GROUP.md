# USER.SMS.GROUP — Table Schema

> Source: `INSERTS/I_F.USER.SMS.GROUP` in `EB_Security.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.USG.DESCRIPTION` | `UserSmsGroup_Description` |  |  |  |
| 2 | `EB.USG.APPLICATION` | `UserSmsGroup_Application` |  |  |  |
| 3 | `EB.USG.VERSION` | `UserSmsGroup_Version` |  |  |  |
| 4 | `EB.USG.FUNCTION` | `UserSmsGroup_Function` |  |  |  |
| 5 | `EB.USG.FIELD.NO` | `UserSmsGroup_FieldNo` |  |  |  |
| 6 | `EB.USG.DATA.COMPARISON` | `UserSmsGroup_DataComparison` |  |  |  |
| 7 | `EB.USG.DATA.FROM` | `UserSmsGroup_DataFrom` |  |  |  |
| 8 | `EB.USG.DATA.TO` | `UserSmsGroup_DataTo` |  |  |  |
| 9 | `EB.USG.TEMP.FUNCTION` | `UserSmsGroup_TempFunction` |  |  |  |
| 10 | `EB.USG.START.DATE` | `UserSmsGroup_StartDate` |  |  |  |
| 11 | `EB.USG.END.DATE` | `UserSmsGroup_EndDate` |  |  |  |
| 12 | `EB.USG.ALLOWED.DAYS` | `UserSmsGroup_AllowedDays` |  |  |  |
| 13 | `EB.USG.DAY.ST.TIME` | `UserSmsGroup_DayStTime` |  |  |  |
| 14 | `EB.USG.DAY.END.TIME` | `UserSmsGroup_DayEndTime` |  |  |  |
| 15 | `EB.USG.EXT.ENQ.NAME` | `UserSmsGroup_ExtEnqName` |  |  |  |
| 16 | `EB.USG.EXT.ENQ.CRITERIA` | `UserSmsGroup_ExtEnqCriteria` |  |  |  |
| 17 | `EB.USG.RESERVED.5` | `UserSmsGroup_Reserved5` | TField |  |  |
| 18 | `EB.USG.RESERVED.4` | `UserSmsGroup_Reserved4` | TField |  |  |
| 19 | `EB.USG.RESERVED.3` | `UserSmsGroup_Reserved3` | TField |  |  |
| 20 | `EB.USG.LOCAL.REF` | `UserSmsGroup_LocalRef` |  |  |  |
| 21 | `EB.USG.RESERVED.1` | `UserSmsGroup_Reserved1` | TField |  |  |
| 22 | `EB.USG.RECORD.STATUS` | `UserSmsGroup_RecordStatus` | String |  |  |
| 23 | `EB.USG.CURR.NO` | `UserSmsGroup_CurrNo` | String |  |  |
| 24 | `EB.USG.INPUTTER` | `UserSmsGroup_Inputter` |  |  |  |
| 25 | `EB.USG.DATE.TIME` | `UserSmsGroup_DateTime` |  |  |  |
| 26 | `EB.USG.AUTHORISER` | `UserSmsGroup_Authoriser` | String |  |  |
| 27 | `EB.USG.CO.CODE` | `UserSmsGroup_CoCode` | String |  |  |
| 28 | `EB.USG.DEPT.CODE` | `UserSmsGroup_DeptCode` | String |  |  |
| 29 | `EB.USG.AUDITOR.CODE` | `UserSmsGroup_AuditorCode` | String |  |  |
| 30 | `EB.USG.AUDIT.DATE.TIME` | `UserSmsGroup_AuditDateTime` | String |  |  |
| 31 | `EB.USG.USE.LOCAL.SMS` | `UserSmsGroup_UseLocalSms` |  |  |  |
