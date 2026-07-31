# NA.QUESTIONNAIRE.DIARY — Table Schema

> Source: `INSERTS/I_F.NA.QUESTIONNAIRE.DIARY` in `NA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.NDR.STATUS` | `NaQuestionnaireDiary_Status` | TField |  | The status of the Application. Could hold 3 values: ACTIVE - Application is in progress INACTIVE - Application began, but no activity has happened for a long time. The time is controlled by a parameter in AA.ORIGINATION.PARAMETER table. COMPLETE - Application reached its logical end. READY.FOR.ARCHIVE - Indicates the record has crossed its threshold of inactivity or completion and is ready to be picked by Archival service. |
| 2 | `NA.NDR.STATUS.DATE` | `NaQuestionnaireDiary_StatusDate` | TField |  | The date on which the above status was updated. Would be useful to know when the system moved to READY.FOR.ARCHIVE status so that the same can be compared against the RETENTION.PERIOD stated in the ARCHIVE record. Would also be a useful indicator on how long has it remained in this status. |
| 3 | `NA.NDR.RESERVED.17` | `NaQuestionnaireDiary_Reserved17` | TField |  |  |
| 4 | `NA.NDR.RESERVED.16` | `NaQuestionnaireDiary_Reserved16` | TField |  |  |
| 5 | `NA.NDR.RESERVED.15` | `NaQuestionnaireDiary_Reserved15` | TField |  |  |
| 6 | `NA.NDR.ACTIVITY` | `NaQuestionnaireDiary_Activity` |  |  |  |
| 7 | `NA.NDR.RESERVED.14` | `NaQuestionnaireDiary_Reserved14` |  |  |  |
| 8 | `NA.NDR.RESERVED.13` | `NaQuestionnaireDiary_Reserved13` |  |  |  |
| 9 | `NA.NDR.RESERVED.12` | `NaQuestionnaireDiary_Reserved12` |  |  |  |
| 10 | `NA.NDR.DATE` | `NaQuestionnaireDiary_Date` |  |  |  |
| 11 | `NA.NDR.TIME` | `NaQuestionnaireDiary_Time` |  |  |  |
| 12 | `NA.NDR.USER` | `NaQuestionnaireDiary_User` |  |  |  |
| 13 | `NA.NDR.OFS.SOURCE` | `NaQuestionnaireDiary_OfsSource` |  |  |  |
| 14 | `NA.NDR.ACTIVITY.STATUS` | `NaQuestionnaireDiary_ActivityStatus` |  |  |  |
| 15 | `NA.NDR.APPLICATION` | `NaQuestionnaireDiary_Application` |  |  |  |
| 16 | `NA.NDR.REFERENCE` | `NaQuestionnaireDiary_Reference` |  |  |  |
| 17 | `NA.NDR.DEFINITION` | `NaQuestionnaireDiary_Definition` |  |  |  |
| 18 | `NA.NDR.RESERVED.11` | `NaQuestionnaireDiary_Reserved11` |  |  |  |
| 19 | `NA.NDR.RESERVED.10` | `NaQuestionnaireDiary_Reserved10` |  |  |  |
| 20 | `NA.NDR.RESERVED.9` | `NaQuestionnaireDiary_Reserved9` |  |  |  |
| 21 | `NA.NDR.RESERVED.8` | `NaQuestionnaireDiary_Reserved8` |  |  |  |
| 22 | `NA.NDR.RESERVED.7` | `NaQuestionnaireDiary_Reserved7` |  |  |  |
| 23 | `NA.NDR.RESERVED.6` | `NaQuestionnaireDiary_Reserved6` | TField |  |  |
| 24 | `NA.NDR.RESERVED.5` | `NaQuestionnaireDiary_Reserved5` | TField |  |  |
| 25 | `NA.NDR.RESERVED.4` | `NaQuestionnaireDiary_Reserved4` | TField |  |  |
| 26 | `NA.NDR.RESERVED.3` | `NaQuestionnaireDiary_Reserved3` | TField |  |  |
| 27 | `NA.NDR.RESERVED.2` | `NaQuestionnaireDiary_Reserved2` | TField |  |  |
| 28 | `NA.NDR.RESERVED.1` | `NaQuestionnaireDiary_Reserved1` | TField |  |  |
