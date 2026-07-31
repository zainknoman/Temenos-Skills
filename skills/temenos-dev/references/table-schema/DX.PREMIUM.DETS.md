# DX.PREMIUM.DETS — Table Schema

> Source: `INSERTS/I_F.DX.PREMIUM.DETS` in `DX_Trade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.PREM.CURRENCY` | `DxPremiumDets_Currency` | TField |  |  |
| 2 | `DX.PREM.TRADE.STATUS` | `DxPremiumDets_TradeStatus` | TField |  |  |
| 3 | `DX.PREM.DATE` | `DxPremiumDets_Date` |  |  |  |
| 4 | `DX.PREM.AMOUNT` | `DxPremiumDets_Amount` |  |  |  |
| 5 | `DX.PREM.RESERVED1` | `DxPremiumDets_Reserved1` |  |  |  |
| 6 | `DX.PREM.RESERVED2` | `DxPremiumDets_Reserved2` | TField |  |  |
| 7 | `DX.PREM.RESERVED3` | `DxPremiumDets_Reserved3` | TField |  |  |
