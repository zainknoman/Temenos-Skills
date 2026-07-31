# ID.CATEG.ENT.UPDATE — Table Schema

> Source: `INSERTS/I_F.ID.CATEG.ENT.UPDATE` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.CEU.POOL.REF` | `IdCategEntUpdate_PoolRef` |  |  |  |
| 2 | `ID.CEU.EFFECTIVE.DATE` | `IdCategEntUpdate_EffectiveDate` |  |  |  |
| 3 | `ID.CEU.START.DATE` | `IdCategEntUpdate_StartDate` | TField |  | Field to hold the Date from which categ entries are to be generated during pre simulation process. First time when PL category is added, START.DATE and EFFECTIVE.DATE will be the same. Validation Rules: 1. Standard Date format. 2. This is a NOINPUT field. |
| 4 | `ID.CEU.LAST.START.DATE` | `IdCategEntUpdate_LastStartDate` |  |  |  |
| 5 | `ID.CEU.START.DATE.CHANGED` | `IdCategEntUpdate_StartDateChanged` | TField |  | Field to indicate whether START.DATE field has been changed from previous run. When PL category is attached to a new POOL and POOL available date is earlier than START.DATE then this field value will be set to YES. Validation Rules: 1. Valid values are YES or NO. 2. This is a NOINPUT field. |
| 6 | `ID.CEU.LAST.UPDATE.DATE` | `IdCategEntUpdate_LastUpdateDate` | TField |  | Field to hold the date upto categ entries are generated during pre simulation process. Validation Rules: 1. Standard Date format. 2. This is a NOINPUT field. |
| 7 | `ID.CEU.RESTRICT.ENTRY` | `IdCategEntUpdate_RestrictEntry` | TField |  | Field to Indicate whether categ entries are to be generated from LAST.UPDATE.DATE to Last working date. When PL category is removed from all available POOL records, this field value will be set to YES. Validation Rules: 1. Valid values are YES or NO. 2. This is a NOINPUT field. |
