# CAPL.UBR.PAY.SEQUENCE — Table Schema

> Source: `INSERTS/I_F.CAPL.UBR.PAY.SEQUENCE` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UBR.PYS.LAST.SEQUENCE` | `CaplUbrPaySequence_LastSequence` | TField |  | Field to store the last sequence number of the bill payment towards the vendor.Allowed upto 6 digits |
| 2 | `UBR.PYS.UBR.TRACE` | `CaplUbrPaySequence_UbrTrace` |  |  |  |
| 3 | `UBR.PYS.RESERVED.1` | `CaplUbrPaySequence_Reserved1` | TField |  |  |
| 4 | `UBR.PYS.RESERVED.2` | `CaplUbrPaySequence_Reserved2` | TField |  |  |
| 5 | `UBR.PYS.RESERVED.3` | `CaplUbrPaySequence_Reserved3` | TField |  |  |
| 6 | `UBR.PYS.RESERVED.4` | `CaplUbrPaySequence_Reserved4` | TField |  |  |
| 7 | `UBR.PYS.RESERVED.5` | `CaplUbrPaySequence_Reserved5` | TField |  |  |
| 8 | `UBR.PYS.RESERVED.6` | `CaplUbrPaySequence_Reserved6` | TField |  |  |
| 9 | `UBR.PYS.RESERVED.7` | `CaplUbrPaySequence_Reserved7` | TField |  |  |
| 10 | `UBR.PYS.RESERVED.8` | `CaplUbrPaySequence_Reserved8` | TField |  |  |
| 11 | `UBR.PYS.RESERVED.9` | `CaplUbrPaySequence_Reserved9` | TField |  |  |
| 12 | `UBR.PYS.RESERVED.10` | `CaplUbrPaySequence_Reserved10` | TField |  |  |
