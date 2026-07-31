# LENREN.OFS.FAIL.DET — Table Schema

> Source: `INSERTS/I_F.LENREN.OFS.FAIL.DET` in `LENREN_Renewal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OFS.FAIL.ACTIVITY.ID` | `LenrenOfsFailDet_ActivityId` | TField |  | This field should be a valid Activity ID and the activities which are failed while supressing the lending renewals will be updated here. |
| 2 | `OFS.FAIL.FAILURE.REASON` | `LenrenOfsFailDet_FailureReason` | TField |  | The OFS Response message (Error Message) to be updated here. Alpha numeric |
| 3 | `OFS.FAIL.RUN.DATE` | `LenrenOfsFailDet_RunDate` | TField |  | Date on which Failure happened. Basically it will be same as part of ID |
| 4 | `OFS.FAIL.ROUTINE` | `LenrenOfsFailDet_Routine` | TField |  | OFS failure from Auto suppress job or Pricing generation. Routine name defaulted here |
| 5 | `OFS.FAIL.RESERVED.10` | `LenrenOfsFailDet_Reserved10` | TField |  |  |
| 6 | `OFS.FAIL.RESERVED.9` | `LenrenOfsFailDet_Reserved9` | TField |  |  |
| 7 | `OFS.FAIL.RESERVED.8` | `LenrenOfsFailDet_Reserved8` | TField |  |  |
| 8 | `OFS.FAIL.RESERVED.7` | `LenrenOfsFailDet_Reserved7` | TField |  |  |
| 9 | `OFS.FAIL.RESERVED.6` | `LenrenOfsFailDet_Reserved6` | TField |  |  |
| 10 | `OFS.FAIL.RESERVED.5` | `LenrenOfsFailDet_Reserved5` | TField |  |  |
| 11 | `OFS.FAIL.RESERVED.4` | `LenrenOfsFailDet_Reserved4` | TField |  |  |
| 12 | `OFS.FAIL.RESERVED.3` | `LenrenOfsFailDet_Reserved3` | TField |  |  |
| 13 | `OFS.FAIL.RESERVED.2` | `LenrenOfsFailDet_Reserved2` | TField |  |  |
| 14 | `OFS.FAIL.RESERVED.1` | `LenrenOfsFailDet_Reserved1` | TField |  |  |
