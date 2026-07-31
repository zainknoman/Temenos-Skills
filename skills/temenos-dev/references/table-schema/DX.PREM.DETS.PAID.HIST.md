# DX.PREM.DETS.PAID.HIST — Table Schema

> Source: `INSERTS/I_F.DX.PREM.DETS.PAID.HIST` in `DX_Trade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.PAID.HIST.CURRENCY` | `DxPremDetsPaidHist_Currency` | TField |  |  |
| 2 | `DX.PAID.HIST.TRADE.STATUS` | `DxPremDetsPaidHist_TradeStatus` | TField |  |  |
| 3 | `DX.PAID.HIST.DATE` | `DxPremDetsPaidHist_Date` |  |  |  |
| 4 | `DX.PAID.HIST.AMOUNT` | `DxPremDetsPaidHist_Amount` |  |  |  |
| 5 | `DX.PAID.HIST.RESERVED1` | `DxPremDetsPaidHist_Reserved1` |  |  |  |
| 6 | `DX.PAID.HIST.RESERVED2` | `DxPremDetsPaidHist_Reserved2` | TField |  |  |
| 7 | `DX.PAID.HIST.RESERVED3` | `DxPremDetsPaidHist_Reserved3` | TField |  |  |
