# AA.PERIODIC.RULE — Table Schema

> Source: `INSERTS/I_F.AA.PERIODIC.RULE` in `AA_Rules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PDR.DESCRIPTION` | `AaPeriodicRule_Description` |  |  |  |
| 2 | `AA.PDR.FULL.DESCRIPTION` | `AaPeriodicRule_FullDescription` | TField |  | Detailed description of the definition. |
| 3 | `AA.PDR.CURRENT.VERSION` | `AaPeriodicRule_CurrentVersion` | TField |  | Version number of the definition in effective.. No input if PERIODIC.RULE is specified Allowed Values: Only the Periodic attributes that belong to ACTIVITY.RESTRICTION property class can be specified here. |
| 4 | `AA.PDR.VERSION` | `AaPeriodicRule_Version` |  |  |  |
| 5 | `AA.PDR.EFFECTIVE.DATE` | `AaPeriodicRule_EffectiveDate` |  |  |  |
| 6 | `AA.PDR.PROPERTY.CLASS` | `AaPeriodicRule_PropertyClass` |  |  |  |
| 7 | `AA.PDR.MULTI.ARRANGEMENT` | `AaPeriodicRule_MultiArrangement` | TField |  |  |
| 8 | `AA.PDR.SOURCE.TYPE` | `AaPeriodicRule_SourceType` | TField |  |  |
| 9 | `AA.PDR.RESERVED.4` | `AaPeriodicRule_Reserved4` |  |  |  |
| 10 | `AA.PDR.RESERVED.5` | `AaPeriodicRule_Reserved5` | TField |  |  |
