# EV.EVIDENCE.DIARY — Table Schema

> Source: `INSERTS/I_F.EV.EVIDENCE.DIARY` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.EVR.STATUS` | `EvEvidenceDiary_Status` | TField |  | The status of the Application. Could hold 3 values: ACTIVE - Application is in progress INACTIVE - Application began, but no activity has happened for a long time. The time is controlled by a parameter in AA.ORIGINATION.PARAMETER table. COMPLETE - Application reached its logical end. READY.FOR.ARCHIVE - Indicates the record has crossed its threshold of inactivity or completion and is ready to be picked by Archival service. |
| 2 | `EV.EVR.STATUS.DATE` | `EvEvidenceDiary_StatusDate` | TField |  | The date on which the above status was updated. Would be useful to know when the system moved to READY.FOR.ARCHIVE status so that the same can be compared against the RETENTION.PERIOD stated in the ARCHIVE record. Would also be a useful indicator on how long has it remained in this status. |
| 3 | `EV.EVR.RESERVED.17` | `EvEvidenceDiary_Reserved17` | TField |  |  |
| 4 | `EV.EVR.RESERVED.16` | `EvEvidenceDiary_Reserved16` | TField |  |  |
| 5 | `EV.EVR.RESERVED.15` | `EvEvidenceDiary_Reserved15` | TField |  |  |
| 6 | `EV.EVR.ACTIVITY` | `EvEvidenceDiary_Activity` |  |  |  |
| 7 | `EV.EVR.RESERVED.14` | `EvEvidenceDiary_Reserved14` |  |  |  |
| 8 | `EV.EVR.RESERVED.13` | `EvEvidenceDiary_Reserved13` |  |  |  |
| 9 | `EV.EVR.RESERVED.12` | `EvEvidenceDiary_Reserved12` |  |  |  |
| 10 | `EV.EVR.DATE` | `EvEvidenceDiary_Date` |  |  |  |
| 11 | `EV.EVR.TIME` | `EvEvidenceDiary_Time` |  |  |  |
| 12 | `EV.EVR.USER` | `EvEvidenceDiary_User` |  |  |  |
| 13 | `EV.EVR.OFS.SOURCE` | `EvEvidenceDiary_OfsSource` |  |  |  |
| 14 | `EV.EVR.ACTIVITY.STATUS` | `EvEvidenceDiary_ActivityStatus` |  |  |  |
| 15 | `EV.EVR.APPLICATION` | `EvEvidenceDiary_Application` |  |  |  |
| 16 | `EV.EVR.REFERENCE` | `EvEvidenceDiary_Reference` |  |  |  |
| 17 | `EV.EVR.DEFINITION` | `EvEvidenceDiary_Definition` |  |  |  |
| 18 | `EV.EVR.RESERVED.11` | `EvEvidenceDiary_Reserved11` |  |  |  |
| 19 | `EV.EVR.RESERVED.10` | `EvEvidenceDiary_Reserved10` |  |  |  |
| 20 | `EV.EVR.RESERVED.9` | `EvEvidenceDiary_Reserved9` |  |  |  |
| 21 | `EV.EVR.RESERVED.8` | `EvEvidenceDiary_Reserved8` |  |  |  |
| 22 | `EV.EVR.RESERVED.7` | `EvEvidenceDiary_Reserved7` |  |  |  |
| 23 | `EV.EVR.RESERVED.6` | `EvEvidenceDiary_Reserved6` | TField |  |  |
| 24 | `EV.EVR.RESERVED.5` | `EvEvidenceDiary_Reserved5` | TField |  |  |
| 25 | `EV.EVR.RESERVED.4` | `EvEvidenceDiary_Reserved4` | TField |  |  |
| 26 | `EV.EVR.RESERVED.3` | `EvEvidenceDiary_Reserved3` | TField |  |  |
| 27 | `EV.EVR.RESERVED.2` | `EvEvidenceDiary_Reserved2` | TField |  |  |
| 28 | `EV.EVR.RESERVED.1` | `EvEvidenceDiary_Reserved1` | TField |  |  |
