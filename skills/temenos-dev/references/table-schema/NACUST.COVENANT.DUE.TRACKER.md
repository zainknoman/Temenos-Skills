# NACUST.COVENANT.DUE.TRACKER — Table Schema

> Source: `INSERTS/I_F.NACUST.COVENANT.DUE.TRACKER` in `NACUST_Covenants.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DUE.TRK.PRE.NOTIFY.DATE` | `NacustCovenantDueTracker_PreNotifyDate` | TField |  | Date on which pre notification should start |
| 2 | `DUE.TRK.REVIEW.DATE` | `NacustCovenantDueTracker_ReviewDate` | TField |  | Date on which review is scheduled |
| 3 | `DUE.TRK.COVENANT.ID` | `NacustCovenantDueTracker_CovenantId` | TField |  | The covenant that comes to review first in the list of covenants expected for this arrangement |
| 4 | `DUE.TRK.STATUS` | `NacustCovenantDueTracker_Status` | TField |  | Current status of covenant in COVENANT.ID field |
| 5 | `DUE.TRK.RESERVED.3` | `NacustCovenantDueTracker_Reserved3` | TField |  |  |
| 6 | `DUE.TRK.RESERVED.2` | `NacustCovenantDueTracker_Reserved2` | TField |  |  |
| 7 | `DUE.TRK.RESERVED.1` | `NacustCovenantDueTracker_Reserved1` | TField |  |  |
| 8 | `DUE.TRK.LOCAL.REF` | `NacustCovenantDueTracker_LocalRef` |  |  |  |
