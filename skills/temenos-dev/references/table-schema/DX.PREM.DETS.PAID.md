# DX.PREM.DETS.PAID — Table Schema

> Source: `INSERTS/I_F.DX.PREM.DETS.PAID` in `DX_Trade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.PAID.CURRENCY` | `DxPremDetsPaid_Currency` | TField |  |  |
| 2 | `DX.PAID.TRADE.STATUS` | `DxPremDetsPaid_TradeStatus` | TField |  |  |
| 3 | `DX.PAID.DATE` | `DxPremDetsPaid_Date` |  |  |  |
| 4 | `DX.PAID.AMOUNT` | `DxPremDetsPaid_Amount` |  |  |  |
| 5 | `DX.PAID.RESERVED1` | `DxPremDetsPaid_Reserved1` |  |  |  |
| 6 | `DX.PAID.RESERVED2` | `DxPremDetsPaid_Reserved2` | TField |  |  |
| 7 | `DX.PAID.RESERVED3` | `DxPremDetsPaid_Reserved3` | TField |  |  |
