# AC.INTEGRITY.ERROR — Table Schema

> Source: `INSERTS/I_F.AC.INTEGRITY.ERROR` in `AC_IntegrityCheck.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.IERR.CHECK.NAME` | `AcIntegrityError_CheckName` | TField |  |  |
| 2 | `AC.IERR.DATE` | `AcIntegrityError_Date` | TField |  |  |
| 3 | `AC.IERR.ERROR.MESSAGE` | `AcIntegrityError_ErrorMessage` | TField |  |  |
| 4 | `AC.IERR.INTEG.DATA.ID` | `AcIntegrityError_IntegDataId` | TField |  |  |
| 5 | `AC.IERR.RECORD.TAG` | `AcIntegrityError_RecordTag` | TField |  |  |
| 6 | `AC.IERR.RECORD.INFO` | `AcIntegrityError_RecordInfo` |  |  |  |
