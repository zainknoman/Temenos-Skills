# AA.INTERNAL.CAP.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.INTERNAL.CAP.DETAILS` in `AA_Interest.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.INT.CAP.RECIPIENT.ID` | `AaInternalCapDetails_RecipientId` | TField |  | Deprecated, not used |
| 2 | `AA.INT.CAP.DATE` | `AaInternalCapDetails_Date` |  |  |  |
| 3 | `AA.INT.CAP.DUE.REF` | `AaInternalCapDetails_DueRef` |  |  |  |
| 4 | `AA.INT.CAP.TRANS.REF` | `AaInternalCapDetails_TransRef` |  |  |  |
| 5 | `AA.INT.CAP.TRANS.STATUS` | `AaInternalCapDetails_TransStatus` |  |  |  |
| 6 | `AA.INT.CAP.AMOUNT` | `AaInternalCapDetails_Amount` |  |  |  |
| 7 | `AA.INT.CAP.RESERVED.4` | `AaInternalCapDetails_Reserved4` | TField |  |  |
| 8 | `AA.INT.CAP.RESERVED.3` | `AaInternalCapDetails_Reserved3` | TField |  |  |
| 9 | `AA.INT.CAP.RESERVED.2` | `AaInternalCapDetails_Reserved2` | TField |  |  |
| 10 | `AA.INT.CAP.RESERVED.1` | `AaInternalCapDetails_Reserved1` | TField |  |  |
