# OA.APPLICATION.DIARY — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.DIARY` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.ADR.DORMANCY.STATUS` | `OaApplicationDiary_DormancyStatus` | TField |  |  |
| 2 | `OA.ADR.DORM.STAT.CHG.DATE` | `OaApplicationDiary_DormStatChgDate` |  |  |  |
| 3 | `OA.ADR.APPLICATION.STATUS` | `OaApplicationDiary_ApplicationStatus` |  |  |  |
| 4 | `OA.ADR.APP.STAT.CHG.DATE` | `OaApplicationDiary_AppStatChgDate` |  |  |  |
| 5 | `OA.ADR.APP.PURPOSE` | `OaApplicationDiary_AppPurpose` |  |  |  |
| 6 | `OA.ADR.ACTIVITY` | `OaApplicationDiary_Activity` |  |  |  |
| 7 | `OA.ADR.RESERVED.8` | `OaApplicationDiary_Reserved8` |  |  |  |
| 8 | `OA.ADR.RESERVED.7` | `OaApplicationDiary_Reserved7` |  |  |  |
| 9 | `OA.ADR.RESERVED.6` | `OaApplicationDiary_Reserved6` |  |  |  |
| 10 | `OA.ADR.DATE` | `OaApplicationDiary_Date` |  |  |  |
| 11 | `OA.ADR.TIME` | `OaApplicationDiary_Time` |  |  |  |
| 12 | `OA.ADR.USER` | `OaApplicationDiary_User` |  |  |  |
| 13 | `OA.ADR.OFS.SOURCE` | `OaApplicationDiary_OfsSource` |  |  |  |
| 14 | `OA.ADR.ACTIVITY.STATUS` | `OaApplicationDiary_ActivityStatus` |  |  |  |
| 15 | `OA.ADR.APPLICATION` | `OaApplicationDiary_Application` |  |  |  |
| 16 | `OA.ADR.REFERENCE` | `OaApplicationDiary_Reference` |  |  |  |
| 17 | `OA.ADR.DEFINITION` | `OaApplicationDiary_Definition` |  |  |  |
| 18 | `OA.ADR.RESERVED.5` | `OaApplicationDiary_Reserved5` |  |  |  |
| 19 | `OA.ADR.RESERVED.4` | `OaApplicationDiary_Reserved4` |  |  |  |
| 20 | `OA.ADR.RESERVED.3` | `OaApplicationDiary_Reserved3` |  |  |  |
| 21 | `OA.ADR.RESERVED.2` | `OaApplicationDiary_Reserved2` |  |  |  |
| 22 | `OA.ADR.RESERVED.1` | `OaApplicationDiary_Reserved1` |  |  |  |
| 23 | `OA.ADR.STATUS.CODE` | `OaApplicationDiary_StatusCode` |  |  |  |
| 24 | `OA.ADR.PURPOSE` | `OaApplicationDiary_Purpose` |  |  |  |
| 25 | `OA.ADR.STATUS.VALUE` | `OaApplicationDiary_StatusValue` |  |  |  |
| 26 | `OA.ADR.STATUS.CHANGE.DATE` | `OaApplicationDiary_StatusChangeDate` |  |  |  |
| 27 | `OA.ADR.STATUS.CHANGE.TIME` | `OaApplicationDiary_StatusChangeTime` |  |  |  |
| 28 | `OA.ADR.STATUS.OFS.SOURCE` | `OaApplicationDiary_StatusOfsSource` |  |  |  |
