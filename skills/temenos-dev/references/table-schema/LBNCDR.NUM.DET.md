# LBNCDR.NUM.DET — Table Schema

> Source: `INSERTS/I_F.LBNCDR.NUM.DET` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.NUM.CUSTOMER.NUM` | `LbncdrNumDet_CustomerNum` | TField |  |  |
| 2 | `LBNCDR.NUM.TEMP.NUM` | `LbncdrNumDet_TempNum` | TField |  |  |
| 3 | `LBNCDR.NUM.CDRDATE` | `LbncdrNumDet_Cdrdate` | TField |  |  |
| 4 | `LBNCDR.NUM.COMP.CODE` | `LbncdrNumDet_CompCode` | TField |  | Holds the Company code where the T24 Customer record has been created Validation Rules 15 A |
| 5 | `LBNCDR.NUM.RESERVED.10` | `LbncdrNumDet_Reserved10` | TField |  |  |
| 6 | `LBNCDR.NUM.RESERVED.9` | `LbncdrNumDet_Reserved9` | TField |  |  |
| 7 | `LBNCDR.NUM.RESERVED.8` | `LbncdrNumDet_Reserved8` | TField |  |  |
| 8 | `LBNCDR.NUM.RESERVED.7` | `LbncdrNumDet_Reserved7` | TField |  |  |
| 9 | `LBNCDR.NUM.RESERVED.6` | `LbncdrNumDet_Reserved6` | TField |  |  |
| 10 | `LBNCDR.NUM.RESERVED.5` | `LbncdrNumDet_Reserved5` | TField |  |  |
| 11 | `LBNCDR.NUM.RESERVED.4` | `LbncdrNumDet_Reserved4` | TField |  |  |
| 12 | `LBNCDR.NUM.RESERVED.3` | `LbncdrNumDet_Reserved3` | TField |  |  |
| 13 | `LBNCDR.NUM.RESERVED.2` | `LbncdrNumDet_Reserved2` | TField |  |  |
| 14 | `LBNCDR.NUM.RESERVED.1` | `LbncdrNumDet_Reserved1` | TField |  |  |
