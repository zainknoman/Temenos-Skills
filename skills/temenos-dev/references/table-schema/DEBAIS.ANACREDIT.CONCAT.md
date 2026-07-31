# DEBAIS.ANACREDIT.CONCAT — Table Schema

> Source: `INSERTS/I_F.DEBAIS.ANACREDIT.CONCAT` in `DEBAIS_AnaCreditExtract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DEBAIS.CLASSIFICATION` | `DebaisAnacreditConcat_Classification` | TField |  | Field will denote if the arrangement is LENDING or ACCOUNTS with negative of positive balance |
| 2 | `DEBAIS.ANACREDIT.STATUS` | `DebaisAnacreditConcat_AnacreditStatus` | TField |  | Flag to denote if the record needs to be included in the ANACREDIT extract |
| 3 | `DEBAIS.RESERVED.5` | `DebaisAnacreditConcat_Reserved5` | TField |  | Reserved field for future use |
| 4 | `DEBAIS.RESERVED.4` | `DebaisAnacreditConcat_Reserved4` | TField |  | Reserved field for future use |
| 5 | `DEBAIS.RESERVED.3` | `DebaisAnacreditConcat_Reserved3` | TField |  | Reserved field for future use |
| 6 | `DEBAIS.RESERVED.2` | `DebaisAnacreditConcat_Reserved2` | TField |  | Reserved field for future use |
| 7 | `DEBAIS.RESERVED.1` | `DebaisAnacreditConcat_Reserved1` | TField |  | Reserved field for future use |
| 8 | `DEBAIS.LOCAL.REF` | `DebaisAnacreditConcat_LocalRef` |  |  |  |
