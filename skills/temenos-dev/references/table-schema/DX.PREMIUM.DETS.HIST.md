# DX.PREMIUM.DETS.HIST — Table Schema

> Source: `INSERTS/I_F.DX.PREMIUM.DETS.HIST` in `DX_Trade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.PREM.HIST.CURRENCY` | `DxPremiumDetsHist_Currency` | TField |  |  |
| 2 | `DX.PREM.HIST.TRADE.STATUS` | `DxPremiumDetsHist_TradeStatus` | TField |  |  |
| 3 | `DX.PREM.HIST.DATE` | `DxPremiumDetsHist_Date` |  |  |  |
| 4 | `DX.PREM.HIST.AMOUNT` | `DxPremiumDetsHist_Amount` |  |  |  |
| 5 | `DX.PREM.HIST.RESERVED1` | `DxPremiumDetsHist_Reserved1` |  |  |  |
| 6 | `DX.PREM.HIST.RESERVED2` | `DxPremiumDetsHist_Reserved2` | TField |  |  |
| 7 | `DX.PREM.HIST.RESERVED3` | `DxPremiumDetsHist_Reserved3` | TField |  |  |
