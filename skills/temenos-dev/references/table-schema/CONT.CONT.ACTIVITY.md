# CONT.CONT.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.CONT.CONT.ACTIVITY` in `AC_MiBase.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CON.CON.ACT.ACTIV.YEAR.MONTH` | `ContContActivity_ActivYearMonth` |  |  |  |
| 2 | `CON.CON.ACT.UPDATE.DATE` | `ContContActivity_UpdateDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `CON.CON.ACT.BVAL.DATE` | `ContContActivity_BvalDate` |  |  |  |
| 4 | `CON.CON.ACT.CALC.AVG.FROM.DATE` | `ContContActivity_CalcAvgFromDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `CON.CON.ACT.REFIN.DATE` | `ContContActivity_RefinDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
