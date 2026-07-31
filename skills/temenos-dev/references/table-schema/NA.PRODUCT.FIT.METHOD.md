# NA.PRODUCT.FIT.METHOD — Table Schema

> Source: `INSERTS/I_F.NA.PRODUCT.FIT.METHOD` in `NA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.PFM.DESCRIPTION` | `NaProductFitMethod_Description` |  |  |  |
| 2 | `NA.PFM.STATUS` | `NaProductFitMethod_Status` | TField |  |  |
| 3 | `NA.PFM.AVAILABLE.DATE` | `NaProductFitMethod_AvailableDate` | TField |  |  |
| 4 | `NA.PFM.EXPIRY.DATE` | `NaProductFitMethod_ExpiryDate` | TField |  |  |
| 5 | `NA.PFM.LAST.PUBLISHED` | `NaProductFitMethod_LastPublished` | TField |  |  |
