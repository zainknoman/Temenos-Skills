# EV.REQUIREMENT.STATUS.DIARY — Table Schema

> Source: `INSERTS/I_F.EV.REQUIREMENT.STATUS.DIARY` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.RSD.STATUS` | `EvRequirementStatusDiary_Status` | TField |  |  |
| 2 | `EV.RSD.STATUS.DATE` | `EvRequirementStatusDiary_StatusDate` | TField |  | Date in which it was moved to the above mentioned status |
| 3 | `EV.RSD.ACTIVITY` | `EvRequirementStatusDiary_Activity` |  |  |  |
| 4 | `EV.RSD.EVIDENCE.REQUIREMENT` | `EvRequirementStatusDiary_EvidenceRequirement` |  |  |  |
| 5 | `EV.RSD.ACTIVITY.REFERENCE` | `EvRequirementStatusDiary_ActivityReference` |  |  |  |
| 6 | `EV.RSD.RESERVED.8` | `EvRequirementStatusDiary_Reserved8` |  |  |  |
| 7 | `EV.RSD.RESERVED.7` | `EvRequirementStatusDiary_Reserved7` |  |  |  |
| 8 | `EV.RSD.RESERVED.6` | `EvRequirementStatusDiary_Reserved6` |  |  |  |
| 9 | `EV.RSD.DATE` | `EvRequirementStatusDiary_Date` |  |  |  |
| 10 | `EV.RSD.TIME` | `EvRequirementStatusDiary_Time` |  |  |  |
| 11 | `EV.RSD.USER` | `EvRequirementStatusDiary_User` |  |  |  |
| 12 | `EV.RSD.OFS.SOURCE` | `EvRequirementStatusDiary_OfsSource` |  |  |  |
| 13 | `EV.RSD.RESERVED.5` | `EvRequirementStatusDiary_Reserved5` |  |  |  |
| 14 | `EV.RSD.RESERVED.4` | `EvRequirementStatusDiary_Reserved4` |  |  |  |
| 15 | `EV.RSD.RESERVED.3` | `EvRequirementStatusDiary_Reserved3` |  |  |  |
| 16 | `EV.RSD.RESERVED.2` | `EvRequirementStatusDiary_Reserved2` |  |  |  |
| 17 | `EV.RSD.RESERVED.1` | `EvRequirementStatusDiary_Reserved1` |  |  |  |
