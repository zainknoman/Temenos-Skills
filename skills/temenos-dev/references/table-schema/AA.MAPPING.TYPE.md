# AA.MAPPING.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.MAPPING.TYPE` in `AF_Mapping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.MPT.DESCRIPTION` | `AaMappingType_Description` |  |  |  |
| 2 | `AA.MPT.CLASS.NAME` | `AaMappingType_ClassName` | TField |  | This field denotes the successfully cataloged class name belonging to the mapping type. |
| 3 | `AA.MPT.STATUS` | `AaMappingType_Status` | TField |  | This field denotes the current status of the product. If the product was published lately it will hold the value PUBLISHED |
| 4 | `AA.MPT.AVAILABLE.DATE` | `AaMappingType_AvailableDate` | TField |  | This field indicates the date from which this mapping type is valid. |
| 5 | `AA.MPT.EXPIRY.DATE` | `AaMappingType_ExpiryDate` | TField |  | This field denotes the expiry date when the mapping type was last cataloged. |
| 6 | `AA.MPT.LAST.PUBLISHED` | `AaMappingType_LastPublished` | TField |  | This field denotes the date when the record was last published |
