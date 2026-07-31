# AC.INTEGRITY.CAL.SUMMARY — Table Schema

> Source: `INSERTS/I_F.AC.INTEGRITY.CAL.SUMMARY` in `AC_IntegrityCheck.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.ICS.DATE` | `AcIntegrityCalSummary_Date` | TField |  |  |
| 2 | `AC.ICS.STMT.ENTRY.TOT` | `AcIntegrityCalSummary_StmtEntryTot` | TField |  |  |
| 3 | `AC.ICS.SPEC.ENTRY.TOT` | `AcIntegrityCalSummary_SpecEntryTot` | TField |  |  |
| 4 | `AC.ICS.CON.UPD.WORK.TOT` | `AcIntegrityCalSummary_ConUpdWorkTot` | TField |  |  |
| 5 | `AC.ICS.CON.ENT.TODAY.TOT` | `AcIntegrityCalSummary_ConEntTodayTot` | TField |  |  |
| 6 | `AC.ICS.CON.ASST.LIAB.TOT` | `AcIntegrityCalSummary_ConAsstLiabTot` | TField |  |  |
| 7 | `AC.ICS.CAL.CON.UPD.WORK.TOT` | `AcIntegrityCalSummary_CalConUpdWorkTot` | TField |  |  |
| 8 | `AC.ICS.EOD.CON.UPD.WORK.TOT` | `AcIntegrityCalSummary_EodConUpdWorkTot` | TField |  |  |
| 9 | `AC.ICS.EOD.SPEC.ENTRY.TOT` | `AcIntegrityCalSummary_EodSpecEntryTot` | TField |  |  |
