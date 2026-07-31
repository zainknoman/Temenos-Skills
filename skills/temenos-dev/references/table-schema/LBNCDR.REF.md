# LBNCDR.REF — Table Schema

> Source: `INSERTS/I_F.LBNCDR.REF` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.REF.CDR.NUM` | `LbncdrRef_CdrNum` | TField |  | Holds the CDR number assigned for this Customer by BDL Validation Rules 15 A |
| 2 | `LBNCDR.REF.CDR.NUM.TEMP` | `LbncdrRef_CdrNumTemp` | TField |  | Holds the CDR number generated in T24 temporarily Validation Rules 15 A |
| 3 | `LBNCDR.REF.CDR.DATE` | `LbncdrRef_CdrDate` | TField |  | Holds the TODAYs date Validation Rules 8 D |
| 4 | `LBNCDR.REF.COMP.CODE` | `LbncdrRef_CompCode` | TField |  | Holds the Company code where the T24 Customer record has been created Validation Rules 15 A |
| 5 | `LBNCDR.REF.RESERVED.10` | `LbncdrRef_Reserved10` | TField |  |  |
| 6 | `LBNCDR.REF.RESERVED.9` | `LbncdrRef_Reserved9` | TField |  |  |
| 7 | `LBNCDR.REF.RESERVED.8` | `LbncdrRef_Reserved8` | TField |  |  |
| 8 | `LBNCDR.REF.RESERVED.7` | `LbncdrRef_Reserved7` | TField |  |  |
| 9 | `LBNCDR.REF.RESERVED.6` | `LbncdrRef_Reserved6` | TField |  |  |
| 10 | `LBNCDR.REF.RESERVED.5` | `LbncdrRef_Reserved5` | TField |  |  |
| 11 | `LBNCDR.REF.RESERVED.4` | `LbncdrRef_Reserved4` | TField |  |  |
| 12 | `LBNCDR.REF.RESERVED.3` | `LbncdrRef_Reserved3` | TField |  |  |
| 13 | `LBNCDR.REF.RESERVED.2` | `LbncdrRef_Reserved2` | TField |  |  |
| 14 | `LBNCDR.REF.RESERVED.1` | `LbncdrRef_Reserved1` | TField |  |  |
