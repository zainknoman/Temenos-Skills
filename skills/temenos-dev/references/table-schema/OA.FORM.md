# OA.FORM — Table Schema

> Source: `INSERTS/I_F.OA.FORM` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.FM.DESCRIPTION` | `OaForm_Description` |  |  |  |
| 2 | `OA.FM.DOMAIN.TYPE` | `OaForm_DomainType` | TField |  | Indicates the OA.DOMAIN.TYPE to which this form belongs. |
| 3 | `OA.FM.DOMAIN.CLASS` | `OaForm_DomainClass` | TField |  | Domain class to which this form is linked to. |
| 4 | `OA.FM.STATUS` | `OaForm_Status` | TField |  | It indicates the current status of the FORM. The only status PUBLISHED updated after publishing the form |
| 5 | `OA.FM.PRF.FORMLET` | `OaForm_PrfFormlet` |  |  |  |
| 6 | `OA.FM.PRF.AVAILABLE.DATE` | `OaForm_PrfAvailableDate` | TField |  | Currently, this field is not in use. |
| 7 | `OA.FM.CAT.FORMLET` | `OaForm_CatFormlet` |  |  |  |
| 8 | `OA.FM.AVAILABLE.DATE` | `OaForm_AvailableDate` | TField |  | Available date of the form. |
| 9 | `OA.FM.LAST.PUBLISHED` | `OaForm_LastPublished` | TField |  | Last published date of this form. |
| 10 | `OA.FM.EXPIRY.DATE` | `OaForm_ExpiryDate` | TField |  | Date beyond which the form is not available. |
| 11 | `OA.FM.RESERVED.9` | `OaForm_Reserved9` | TField |  |  |
| 12 | `OA.FM.RESERVED.8` | `OaForm_Reserved8` | TField |  |  |
| 13 | `OA.FM.RESERVED.7` | `OaForm_Reserved7` | TField |  |  |
| 14 | `OA.FM.RESERVED.6` | `OaForm_Reserved6` | TField |  |  |
| 15 | `OA.FM.RESERVED.5` | `OaForm_Reserved5` | TField |  |  |
| 16 | `OA.FM.RESERVED.4` | `OaForm_Reserved4` | TField |  |  |
| 17 | `OA.FM.RESERVED.3` | `OaForm_Reserved3` | TField |  |  |
| 18 | `OA.FM.RESERVED.2` | `OaForm_Reserved2` | TField |  |  |
| 19 | `OA.FM.RESERVED.1` | `OaForm_Reserved1` | TField |  |  |
