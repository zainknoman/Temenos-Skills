# DE.UETR.CATALOG — Table Schema

> Source: `INSERTS/I_F.DE.UETR.CATALOG` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.UCAT.TXN.REFERENCE` | `DeUetrCatalog_TxnReference` |  |  |  |
| 2 | `DE.UCAT.IN.DELIVERY.REF` | `DeUetrCatalog_InDeliveryRef` |  |  |  |
| 3 | `DE.UCAT.OUT.DELIVERY.REF` | `DeUetrCatalog_OutDeliveryRef` |  |  |  |
