# CANNEX.ORD.EXCEP — Table Schema

> Source: `INSERTS/I_F.CANNEX.ORD.EXCEP` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.EXCEP.EXCEPTION` | `CannexOrdExcep_Exception` |  |  |  |
| 2 | `CANNEX.EXCEP.FILE.NAME` | `CannexOrdExcep_FileName` | TField |  |  |
| 3 | `CANNEX.EXCEP.OTHER.EXCEPTIONS` | `CannexOrdExcep_OtherExceptions` |  |  |  |
| 4 | `CANNEX.EXCEP.RESERVED.1` | `CannexOrdExcep_Reserved1` | TField |  |  |
| 5 | `CANNEX.EXCEP.RESERVED.2` | `CannexOrdExcep_Reserved2` | TField |  |  |
| 6 | `CANNEX.EXCEP.RESERVED.3` | `CannexOrdExcep_Reserved3` | TField |  |  |
| 7 | `CANNEX.EXCEP.RESERVED.4` | `CannexOrdExcep_Reserved4` | TField |  |  |
| 8 | `CANNEX.EXCEP.RESERVED.5` | `CannexOrdExcep_Reserved5` | TField |  |  |
| 9 | `CANNEX.EXCEP.RESERVED.6` | `CannexOrdExcep_Reserved6` | TField |  |  |
| 10 | `CANNEX.EXCEP.RESERVED.7` | `CannexOrdExcep_Reserved7` | TField |  |  |
| 11 | `CANNEX.EXCEP.RESERVED.8` | `CannexOrdExcep_Reserved8` | TField |  |  |
| 12 | `CANNEX.EXCEP.RESERVED.9` | `CannexOrdExcep_Reserved9` | TField |  |  |
| 13 | `CANNEX.EXCEP.RESERVED.10` | `CannexOrdExcep_Reserved10` | TField |  |  |
| 14 | `CANNEX.EXCEP.LOCAL.REF` | `CannexOrdExcep_LocalRef` |  |  |  |
| 15 | `CANNEX.EXCEP.OVERRIDE` | `CannexOrdExcep_Override` |  |  |  |
