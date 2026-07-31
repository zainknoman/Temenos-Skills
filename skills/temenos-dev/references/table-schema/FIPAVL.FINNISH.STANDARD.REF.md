# FIPAVL.FINNISH.STANDARD.REF — Table Schema

> Source: `INSERTS/I_F.FIPAVL.FINNISH.STANDARD.REF` in `FIPAVL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FIN.STD.FINNISH.REFERENCE` | `FipavlFinnishStandardRef_FinnishReference` | TField |  | The Finnish structured creditor reference number. |
| 2 | `FIN.STD.UNSTRUCTURED.REFERENCE` | `FipavlFinnishStandardRef_UnstructuredReference` | TField |  | The unstructured remittance information. |
| 3 | `FIN.STD.RESERVED.8` | `FipavlFinnishStandardRef_Reserved8` | TField |  |  |
| 4 | `FIN.STD.RESERVED.7` | `FipavlFinnishStandardRef_Reserved7` | TField |  |  |
| 5 | `FIN.STD.RESERVED.6` | `FipavlFinnishStandardRef_Reserved6` | TField |  |  |
| 6 | `FIN.STD.RESERVED.5` | `FipavlFinnishStandardRef_Reserved5` | TField |  |  |
| 7 | `FIN.STD.RESERVED.4` | `FipavlFinnishStandardRef_Reserved4` | TField |  |  |
| 8 | `FIN.STD.RESERVED.3` | `FipavlFinnishStandardRef_Reserved3` | TField |  |  |
| 9 | `FIN.STD.RESERVED.2` | `FipavlFinnishStandardRef_Reserved2` | TField |  |  |
| 10 | `FIN.STD.RESERVED.1` | `FipavlFinnishStandardRef_Reserved1` | TField |  |  |
| 11 | `FIN.STD.LOCAL.REF` | `FipavlFinnishStandardRef_LocalRef` |  |  |  |
