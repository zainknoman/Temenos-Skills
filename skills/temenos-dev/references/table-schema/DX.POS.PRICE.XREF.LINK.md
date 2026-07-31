# DX.POS.PRICE.XREF.LINK — Table Schema

> Source: `INSERTS/I_F.DX.POS.PRICE.XREF.LINK` in `DX_Position.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.XREF.KEY.FIELDS` | `DxPosPriceXrefLink_KeyFields` |  |  |  |
| 2 | `DX.XREF.XREF` | `DxPosPriceXrefLink_Xref` |  |  |  |
| 3 | `DX.XREF.RESERVED.3` | `DxPosPriceXrefLink_Reserved3` |  |  |  |
| 4 | `DX.XREF.RESERVED.2` | `DxPosPriceXrefLink_Reserved2` |  |  |  |
| 5 | `DX.XREF.MATURITY.DATE` | `DxPosPriceXrefLink_MaturityDate` | TField |  | Holds the maturity date which is one of the component of the key. |
| 6 | `DX.XREF.RESERVED.1` | `DxPosPriceXrefLink_Reserved1` | TField |  |  |
