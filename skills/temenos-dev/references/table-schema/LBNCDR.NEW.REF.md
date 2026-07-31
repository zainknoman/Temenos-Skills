# LBNCDR.NEW.REF — Table Schema

> Source: `INSERTS/I_F.LBNCDR.NEW.REF` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.NEW.CDR.CUS.NO` | `LbncdrNewRef_CdrCusNo` |  |  |  |
| 2 | `LBNCDR.NEW.CDR.NUM` | `LbncdrNewRef_CdrNum` | TField |  | Holds the CDR number generated in T24 temporarily Validation Rules 15 A |
| 3 | `LBNCDR.NEW.CDR.DATE` | `LbncdrNewRef_CdrDate` | TField |  | Holds the TODAYs date Validation Rules 8 D |
| 4 | `LBNCDR.NEW.COMP.CODE` | `LbncdrNewRef_CompCode` |  |  |  |
| 5 | `LBNCDR.NEW.RESERVED.10` | `LbncdrNewRef_Reserved10` | TField |  |  |
| 6 | `LBNCDR.NEW.RESERVED.9` | `LbncdrNewRef_Reserved9` | TField |  |  |
| 7 | `LBNCDR.NEW.RESERVED.8` | `LbncdrNewRef_Reserved8` | TField |  |  |
| 8 | `LBNCDR.NEW.RESERVED.7` | `LbncdrNewRef_Reserved7` | TField |  |  |
| 9 | `LBNCDR.NEW.RESERVED.6` | `LbncdrNewRef_Reserved6` | TField |  |  |
| 10 | `LBNCDR.NEW.RESERVED.5` | `LbncdrNewRef_Reserved5` | TField |  |  |
| 11 | `LBNCDR.NEW.RESERVED.4` | `LbncdrNewRef_Reserved4` | TField |  |  |
| 12 | `LBNCDR.NEW.RESERVED.3` | `LbncdrNewRef_Reserved3` | TField |  |  |
| 13 | `LBNCDR.NEW.RESERVED.2` | `LbncdrNewRef_Reserved2` | TField |  |  |
| 14 | `LBNCDR.NEW.RESERVED.1` | `LbncdrNewRef_Reserved1` | TField |  |  |
