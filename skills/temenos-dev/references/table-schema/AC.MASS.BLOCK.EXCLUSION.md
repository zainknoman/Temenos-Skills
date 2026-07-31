# AC.MASS.BLOCK.EXCLUSION — Table Schema

> Source: `INSERTS/I_F.AC.MASS.BLOCK.EXCLUSION` in `AC_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AMBE.EXCLUDE` | `AcMassBlockExclusion_Exclude` | TField |  |  |
| 2 | `AMBE.RECORD.STATUS` | `AcMassBlockExclusion_RecordStatus` | String |  |  |
| 3 | `AMBE.CURR.NO` | `AcMassBlockExclusion_CurrNo` | String |  |  |
| 4 | `AMBE.INPUTTER` | `AcMassBlockExclusion_Inputter` |  |  |  |
| 5 | `AMBE.DATE.TIME` | `AcMassBlockExclusion_DateTime` |  |  |  |
| 6 | `AMBE.AUTHORISER` | `AcMassBlockExclusion_Authoriser` | String |  |  |
| 7 | `AMBE.CO.CODE` | `AcMassBlockExclusion_CoCode` | String |  |  |
| 8 | `AMBE.DEPT.CODE` | `AcMassBlockExclusion_DeptCode` | String |  |  |
| 9 | `AMBE.AUDITOR.CODE` | `AcMassBlockExclusion_AuditorCode` | String |  |  |
| 10 | `AMBE.AUDIT.DATE.TIME` | `AcMassBlockExclusion_AuditDateTime` | String |  |  |
