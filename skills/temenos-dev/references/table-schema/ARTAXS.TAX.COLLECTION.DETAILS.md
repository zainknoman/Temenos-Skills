# ARTAXS.TAX.COLLECTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.ARTAXS.TAX.COLLECTION.DETAILS` in `ARTAXS_TaxReturns.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARTAXS.TCD.COLLECTED.DATE` | `ArtaxsTaxCollectionDetails_CollectedDate` |  |  |  |
| 2 | `ARTAXS.TCD.COLLECTED.AMOUNT` | `ArtaxsTaxCollectionDetails_CollectedAmount` |  |  |  |
| 3 | `ARTAXS.TCD.REFUNDED.DATE` | `ArtaxsTaxCollectionDetails_RefundedDate` |  |  |  |
| 4 | `ARTAXS.TCD.REFUNDED.AMOUNT` | `ArtaxsTaxCollectionDetails_RefundedAmount` |  |  |  |
