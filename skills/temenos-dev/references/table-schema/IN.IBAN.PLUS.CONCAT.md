# IN.IBAN.PLUS.CONCAT — Table Schema

> Source: `INSERTS/I_F.IN.IBAN.PLUS.CONCAT` in `IN_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IN.PL.CC.BIC.CODE` | `InIbanPlusConcat_BicCode` | TField |  |  |
| 2 | `IN.PL.CC.CUS.BIC.CODE` | `InIbanPlusConcat_CusBicCode` |  |  |  |
| 3 | `IN.PL.CC.FUT.BIC.CODE` | `InIbanPlusConcat_FutBicCode` | TField |  |  |
